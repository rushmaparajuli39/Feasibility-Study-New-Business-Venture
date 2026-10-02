# Feasibility Study: New Business Venture (Project HSV)

A structured feasibility study for an early-stage venture in the **specialty food & ingredients** space, carried out the way a research analyst would: define the questions, gather evidence, model the economics, stress-test the assumptions, and make a go / no-go recommendation.

> **Confidentiality note:** The venture is referred to only by its codename, **Project HSV**. Product specifics, sourcing partners, target accounts and real pricing are kept out of this repository on purpose. All figures here are **illustrative placeholders** that show the method, not the actual business case.

---

## Research Questions

| # | Question | Feasibility Dimension |
|---|----------|----------------------|
| RQ1 | Is there a reachable, growing customer segment willing to pay a premium for differentiated specialty ingredients? | Market |
| RQ2 | Can the product be sourced, imported, packaged and distributed reliably and in compliance with food-safety rules? | Operational / Regulatory |
| RQ3 | Do the unit economics support profitability at a realistic sales volume, and how long until break-even? | Financial |
| RQ4 | What are the critical risks, and can they be mitigated at acceptable cost? | Risk |
| RQ5 | Does the founding team have, or can it acquire, the capabilities needed to execute? | Organizational |

## Approach

1. **Desk research:** industry reports, trade data, public company filings, regulatory guidance
2. **Primary research:** customer interviews, a short survey, supplier and logistics quotes (stored privately)
3. **Competitive analysis:** competitor archetypes, positioning map, Porter's Five Forces
4. **Financial modeling:** unit economics, break-even, 5-year projection, NPV/IRR, scenario and sensitivity analysis ([`model/`](model/))
5. **Risk assessment:** likelihood × impact register with mitigations
6. **Weighted scoring:** each dimension is scored against go / no-go thresholds

See [`docs/01_methodology.md`](docs/01_methodology.md) for details.

## Repository Structure

```
.
├── docs/
│   ├── 00_project_charter.md        # scope, objectives, timeline, deliverables
│   ├── 01_methodology.md            # research design and scoring framework
│   ├── 02_market_analysis.md        # TAM / SAM / SOM, segments, demand drivers
│   ├── 03_competitive_landscape.md  # archetypes, Five Forces, positioning
│   ├── 04_operations_regulatory.md  # sourcing, import compliance, logistics
│   ├── 05_financial_feasibility.md  # unit economics, projections, scenarios
│   ├── 06_risk_register.md          # risks, scoring, mitigations
│   ├── 07_findings_recommendation.md# scorecard and go / no-go
│   └── decision_log.md              # key decisions and rationale
├── model/
│   ├── feasibility_model.py         # financial model (Python standard library only)
│   ├── assumptions/                 # scenario inputs (illustrative)
│   └── tests/                       # model sanity tests
├── templates/                       # interview guide, survey, supplier scorecard
├── .github/workflows/               # CI: runs model tests on every push
└── confidential/                    # git-ignored; real data stays local
```

## Running the Financial Model

Requires Python 3.9+ and nothing else.

```bash
python model/feasibility_model.py                    # runs all scenarios
python model/feasibility_model.py --scenario base    # runs one scenario
python -m unittest discover -s model/tests           # runs the sanity tests
```

## Status

| Workstream | Status |
|-----------|--------|
| Project charter and methodology | ✅ Complete |
| Market analysis framework | 🟡 In progress (primary research underway) |
| Competitive landscape | 🟡 In progress |
| Operations and regulatory review | 🟡 In progress |
| Financial model v1 | ✅ Complete (illustrative inputs) |
| Risk register | ✅ v1 complete |
| Research templates (interviews, survey, supplier scorecard) | ✅ Complete |
| Findings and recommendation | 🟡 Preliminary |

## Preliminary Result (illustrative inputs)

| Scenario | NPV | IRR | Payback |
|----------|----:|----:|--------:|
| Downside | −$354k | n/a | > 5 yrs |
| Base | −$10k | 14.7% | 4.2 yrs |
| Upside | $496k | 114% | 1.7 yrs |

Weighted feasibility score **3.10 / 5**, which leads to **Go with conditions**: a capped pilot that has to validate price and customer acquisition cost before full launch. See [`docs/07_findings_recommendation.md`](docs/07_findings_recommendation.md).

## Skills Demonstrated

Market sizing · competitive analysis · primary research design · unit economics · DCF / NPV / IRR · scenario and sensitivity analysis · risk assessment · Python

---

*Author: Rushma Parajuli. This is independent research; no part of it is investment advice.*
