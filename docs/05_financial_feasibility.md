# 05 · Financial Feasibility

> All numbers come from the **illustrative** inputs in [`model/assumptions/`](../model/assumptions/). They show the analysis, not the real business case. To reproduce them:
> ```bash
> python model/feasibility_model.py --sensitivity
> ```

## Model Structure

```
Orders ─┬─► Units × Price ─────────────────────────► Revenue
        ├─► Units × (Landed cost + Packaging) ─────► COGS
        ├─► Fulfillment + payment fees ────────────► Other variable costs
        └─► New-customer orders × CAC ─────────────► Marketing
Revenue − Variable costs − Marketing − Fixed costs = EBITDA
EBITDA − Tax (with loss carry-forward) − ΔWorking capital = Free cash flow
FCF discounted at the hurdle rate ─► NPV, IRR, payback
```

## Unit Economics (Year 1, per order)

| Metric | Downside | Base | Upside |
|--------|---------:|-----:|-------:|
| Gross margin | 60.4% | 69.7% | 72.6% |
| Contribution after blended CAC | −$5 | $11 | $18 |
| LTV : CAC | 0.7× | 2.0× | 3.2× |

**Benchmark:** for DTC consumer brands, LTV:CAC of **3× or more** is usually considered healthy. The base case is **below** that bar, so retention and CAC are the levers to watch.

## 5-Year Projection: Base Case

| Year | Orders | Revenue | EBITDA | EBITDA margin | Free cash flow |
|-----:|-------:|--------:|-------:|--------------:|---------------:|
| 1 | 4,000 | $153,600 | −$4,768 | −3.1% | −$27,808 |
| 2 | 6,600 | $261,043 | $17,975 | 6.9% | −$915 |
| 3 | 9,570 | $389,868 | $50,779 | 13.0% | $20,792 |
| 4 | 12,441 | $522,033 | $92,456 | 17.7% | $53,215 |
| 5 | 14,929 | $645,233 | $137,274 | 21.3% | $89,967 |

## Scenario Summary

| Metric | Downside | Base | Upside |
|--------|---------:|-----:|-------:|
| Discount rate | 20% | 18% | 16% |
| NPV | −$354,361 | −$9,795 | $496,000 |
| IRR | n/a | 14.7% | 114.0% |
| Payback | Not within 5 yrs | 4.2 yrs | 1.7 yrs |
| Year-1 break-even orders | n/a | 4,441 | 2,708 |

## Sensitivity: Base Case NPV (±20%)

| Driver | −20% | +20% |
|--------|-----:|-----:|
| **Price per unit** | −$181,074 | $147,642 |
| Year-1 orders | −$57,072 | $37,113 |
| Customer acquisition cost | $36,231 | −$56,150 |
| Landed cost per unit | $29,297 | −$49,125 |

## Interpretation

1. **The base case is marginal.** IRR (14.7%) is just below the 18% hurdle rate, and NPV is roughly break-even. The venture works, but it isn't yet compelling.
2. **Price is the dominant lever.** NPV is several times more sensitive to price than to any other driver. The willingness-to-pay research in [02](02_market_analysis.md) is therefore the single most important piece of evidence.
3. **Acquisition economics need proof.** LTV:CAC of 2.0× means growth spending recovers slowly. A small paid-acquisition pilot should confirm CAC before scaling.
4. **The downside is clearly negative.** If price falls and CAC rises together, the model doesn't recover within 5 years, which argues for a staged, capped initial investment.

## Next Steps

- [ ] Replace illustrative inputs with validated quotes and survey results (in a `*.local.json` file)
- [ ] Add a monthly cash-flow view for year 1 to size the minimum cash requirement
- [ ] Test a subscription offer as a lever on repeat-order share
