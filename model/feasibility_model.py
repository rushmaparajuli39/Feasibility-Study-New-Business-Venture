"""Financial feasibility model for Project HSV.

Builds a simple annual projection from a JSON assumptions file and reports
unit economics, break-even, NPV, IRR, payback and a one-at-a-time sensitivity
table. Standard library only.

Usage:
    python model/feasibility_model.py                     # all scenarios
    python model/feasibility_model.py --scenario base
    python model/feasibility_model.py --file my.local.json
    python model/feasibility_model.py --scenario base --sensitivity
"""

import argparse
import json
from pathlib import Path

ASSUMPTIONS_DIR = Path(__file__).parent / "assumptions"
SCENARIOS = ("downside", "base", "upside")
SENSITIVITY_DRIVERS = {
    "price_per_unit": "Price per unit",
    "landed_cost_per_unit": "Landed cost per unit",
    "year1_orders": "Year-1 orders",
    "cac": "Customer acquisition cost",
}


def load_assumptions(path):
    with open(path) as f:
        a = json.load(f)
    a.pop("_note", None)
    if len(a["order_growth"]) != a["years"] or len(a["fixed_costs_annual"]) != a["years"]:
        raise ValueError(f"{path}: order_growth and fixed_costs_annual must have {a['years']} entries")
    return a


def unit_economics(a, year=0):
    """Per-order economics for a given year index (0 = year 1)."""
    price = a["price_per_unit"] * (1 + a["price_growth"]) ** year
    unit_cost = a["landed_cost_per_unit"] * (1 + a["unit_cost_change"]) ** year
    units = a["units_per_order"]

    revenue = price * units
    variable = (unit_cost + a["packaging_per_unit"]) * units + a["fulfillment_per_order"] + revenue * a["payment_fee_pct"]
    contribution = revenue - variable
    # Only first orders carry acquisition cost; repeat orders are "free".
    blended_cac = a["cac"] * (1 - a["repeat_order_share"])
    # Geometric expectation of orders per customer given a constant repeat share.
    orders_per_customer = 1 / (1 - a["repeat_order_share"])
    ltv = contribution * orders_per_customer

    return {
        "aov": revenue,
        "variable_cost_per_order": variable,
        "contribution_per_order": contribution,
        "gross_margin_pct": (revenue - (unit_cost + a["packaging_per_unit"]) * units) / revenue,
        "contribution_after_cac": contribution - blended_cac,
        "ltv": ltv,
        "ltv_to_cac": ltv / a["cac"] if a["cac"] else float("inf"),
    }


def project(a):
    """Annual projection. Returns a list of per-year dicts."""
    rows = []
    orders = a["year1_orders"]
    prev_revenue = 0.0
    loss_carryforward = 0.0

    for y in range(a["years"]):
        if y > 0:
            orders *= 1 + a["order_growth"][y]
        ue = unit_economics(a, y)

        revenue = orders * ue["aov"]
        variable = orders * ue["variable_cost_per_order"]
        marketing = orders * (1 - a["repeat_order_share"]) * a["cac"]
        fixed = a["fixed_costs_annual"][y]
        ebitda = revenue - variable - marketing - fixed

        taxable = ebitda - loss_carryforward
        if taxable > 0:
            tax = taxable * a["tax_rate"]
            loss_carryforward = 0.0
        else:
            tax = 0.0
            loss_carryforward = -taxable

        delta_wc = (revenue - prev_revenue) * a["working_capital_pct_revenue"]
        fcf = ebitda - tax - delta_wc
        prev_revenue = revenue

        rows.append({
            "year": y + 1,
            "orders": orders,
            "revenue": revenue,
            "variable_costs": variable,
            "marketing": marketing,
            "fixed_costs": fixed,
            "ebitda": ebitda,
            "ebitda_margin": ebitda / revenue if revenue else 0.0,
            "tax": tax,
            "delta_wc": delta_wc,
            "fcf": fcf,
        })
    return rows


def npv(rate, cashflows):
    """cashflows[0] is at t=0."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows, lo=-0.99, hi=10.0, tol=1e-7):
    """IRR by bisection. Returns None if there is no sign change in range."""
    f_lo, f_hi = npv(lo, cashflows), npv(hi, cashflows)
    if f_lo * f_hi > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def payback_years(cashflows):
    """Fractional years until cumulative cash turns positive, or None."""
    cumulative = cashflows[0]
    for t in range(1, len(cashflows)):
        if cumulative + cashflows[t] >= 0:
            return t - 1 + (-cumulative / cashflows[t])
        cumulative += cashflows[t]
    return None


def evaluate(a):
    rows = project(a)
    cashflows = [-a["initial_investment"]] + [r["fcf"] for r in rows]
    ue = unit_economics(a)
    contribution_after_cac = ue["contribution_after_cac"]
    breakeven_orders = (
        a["fixed_costs_annual"][0] / contribution_after_cac if contribution_after_cac > 0 else None
    )
    return {
        "scenario": a.get("scenario", "custom"),
        "unit_economics": ue,
        "rows": rows,
        "cashflows": cashflows,
        "npv": npv(a["discount_rate"], cashflows),
        "irr": irr(cashflows),
        "payback_years": payback_years(cashflows),
        "breakeven_orders_y1": breakeven_orders,
    }


def sensitivity(a, swing=0.20):
    """One-at-a-time +/- swing on key drivers; returns NPV deltas."""
    base_npv = evaluate(a)["npv"]
    out = []
    for key, label in SENSITIVITY_DRIVERS.items():
        low, high = dict(a), dict(a)
        low[key] = a[key] * (1 - swing)
        high[key] = a[key] * (1 + swing)
        out.append({
            "driver": label,
            "npv_low": evaluate(low)["npv"],
            "npv_high": evaluate(high)["npv"],
            "range": abs(evaluate(high)["npv"] - evaluate(low)["npv"]),
        })
    return base_npv, sorted(out, key=lambda r: r["range"], reverse=True)


# ---------- reporting ----------

def _money(x):
    return f"-${abs(x):,.0f}" if x < 0 else f"${x:,.0f}"


def _pct(x):
    return "n/a" if x is None else f"{x:.1%}"


def report(result):
    ue = result["unit_economics"]
    lines = [
        f"\n=== Scenario: {result['scenario'].upper()} ===",
        "",
        "Unit economics (year 1, per order)",
        f"  Average order value      {_money(ue['aov']):>12}",
        f"  Gross margin             {_pct(ue['gross_margin_pct']):>12}",
        f"  Contribution / order     {_money(ue['contribution_per_order']):>12}",
        f"  After blended CAC        {_money(ue['contribution_after_cac']):>12}",
        f"  LTV : CAC                {ue['ltv_to_cac']:>11.1f}x",
        "",
        f"{'Year':>4} {'Orders':>9} {'Revenue':>12} {'EBITDA':>12} {'Margin':>8} {'FCF':>12}",
    ]
    for r in result["rows"]:
        lines.append(
            f"{r['year']:>4} {r['orders']:>9,.0f} {_money(r['revenue']):>12} "
            f"{_money(r['ebitda']):>12} {r['ebitda_margin']:>8.1%} {_money(r['fcf']):>12}"
        )
    be = result["breakeven_orders_y1"]
    pb = result["payback_years"]
    lines += [
        "",
        f"  NPV                      {_money(result['npv']):>12}",
        f"  IRR                      {_pct(result['irr']):>12}",
        f"  Payback                  {'not within horizon' if pb is None else f'{pb:.1f} yrs':>12}",
        f"  Break-even orders (Y1)   {'n/a' if be is None else f'{be:,.0f}':>12}",
    ]
    return "\n".join(lines)


def report_sensitivity(a):
    base_npv, rows = sensitivity(a)
    lines = [f"\nSensitivity (+/-20%, NPV; base {_money(base_npv)})",
             f"  {'Driver':<28}{'-20%':>12}{'+20%':>12}"]
    for r in rows:
        lines.append(f"  {r['driver']:<28}{_money(r['npv_low']):>12}{_money(r['npv_high']):>12}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--scenario", choices=SCENARIOS)
    group.add_argument("--file", type=Path, help="path to a custom assumptions JSON")
    parser.add_argument("--sensitivity", action="store_true", help="add a sensitivity table")
    args = parser.parse_args()

    if args.file:
        paths = [args.file]
    elif args.scenario:
        paths = [ASSUMPTIONS_DIR / f"{args.scenario}.json"]
    else:
        paths = [ASSUMPTIONS_DIR / f"{s}.json" for s in SCENARIOS]

    for path in paths:
        a = load_assumptions(path)
        print(report(evaluate(a)))
        if args.sensitivity:
            print(report_sensitivity(a))


if __name__ == "__main__":
    main()
