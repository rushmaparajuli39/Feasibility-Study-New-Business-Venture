# 06 · Risk Register

**Scoring:** Likelihood (L) and Impact (I) are each rated 1–5. Score = L × I.
🔴 15 or above · 🟠 8–14 · 🟢 7 or below

| ID | Risk | Category | L | I | Score | Mitigation | Owner |
|----|------|----------|:-:|:-:|:-----:|------------|-------|
| R-01 | Customers won't pay the assumed premium | Market | 3 | 5 | 🔴 15 | Validate WTP with a survey and a pre-order test before buying inventory | Research |
| R-02 | CAC is higher than modeled | Market | 4 | 4 | 🔴 16 | Small paid pilot with a fixed budget; invest in organic / content channels and referrals | Marketing |
| R-03 | Shipment held, detained or refused at U.S. entry | Regulatory | 2 | 5 | 🟠 10 | Pre-shipment lab testing, experienced customs broker, FSVP documentation in place | Ops |
| R-04 | Quality varies between lots | Operational | 3 | 4 | 🟠 12 | Written specs, testing of every lot, at least 2 qualified suppliers | Ops |
| R-05 | Single-supplier dependency | Operational | 3 | 4 | 🟠 12 | Qualify a backup supplier before launch | Ops |
| R-06 | Freight cost / FX volatility squeezes margin | Financial | 3 | 3 | 🟠 9 | Price buffer in the model, bundle shipments, review pricing quarterly | Finance |
| R-07 | Well-funded competitor enters the same niche | Competitive | 3 | 3 | 🟠 9 | Build supply relationships and community early; differentiate on provenance | Strategy |
| R-08 | Inventory obsolescence / shelf-life loss | Operational | 2 | 3 | 🟢 6 | Small batches, FIFO, monitor days of cover | Ops |
| R-09 | Founder bandwidth / key-person risk | Organizational | 3 | 3 | 🟠 9 | Outsource fulfillment early; write down processes (SOPs) | Founders |
| R-10 | Product liability claim | Legal | 1 | 5 | 🟢 5 | Product liability insurance, lot traceability, recall plan | Legal |

## Heat Map

```
Impact →     1     2     3     4     5
Likelihood
    5        .     .     .     .     .
    4        .     .     .    R02    .
    3        .     .   R06   R04   R01
                       R07   R05
                       R09
    2        .     .   R08    .    R03
    1        .     .     .     .    R10
```

## Top Risks to Resolve Before a Go Decision

1. **R-02 CAC** and **R-01 willingness to pay**. Together these account for most of the NPV swing in the sensitivity analysis.
2. **R-05 supplier redundancy.** This is a precondition for the operational score.
