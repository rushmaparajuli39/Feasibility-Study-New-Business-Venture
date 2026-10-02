# 04 · Operations & Regulatory Review

## Value Chain

```
Sourcing ─► Quality testing ─► Export / freight ─► U.S. customs & FDA ─► Packaging / co-pack ─► 3PL fulfillment ─► Customer
```

## Regulatory Checklist (U.S. food import, general)

| Requirement | Authority | Applies to | Status |
|-------------|-----------|------------|:------:|
| Food facility registration (foreign suppliers and U.S. packers) | FDA | Supplier / co-packer | ⚪ |
| Foreign Supplier Verification Program (FSVP) | FDA (FSMA) | Importer of record | ⚪ |
| Prior Notice of imported food shipments | FDA | Each shipment | ⚪ |
| Customs entry, HTS classification, duties | CBP | Each shipment | ⚪ |
| Customs bond (single-entry or continuous) | CBP | Importer | ⚪ |
| Food labeling (ingredients, allergens, net weight, country of origin) | FDA / CBP | Each SKU | ⚪ |
| Contaminant screening (microbial, heavy metals, pesticide residues) | FDA guidance / buyer specs | Each lot | ⚪ |
| State / local business and sales-tax registration | State | Entity | ⚪ |
| Product liability insurance | — | Entity | ⚪ |

Legend: ⚪ not started · 🟡 in progress · ✅ done

> Inspection, detention or refusal of a shipment at entry is a material operational risk. See R-03 in the [risk register](06_risk_register.md).

## Supplier Evaluation

Suppliers are scored using [`templates/supplier_scorecard.md`](../templates/supplier_scorecard.md) on these criteria:

| Criterion | Weight |
|-----------|-------:|
| Quality and lab-test history | 30% |
| Food-safety certifications / documentation | 20% |
| Capacity and scalability | 15% |
| Price and payment terms | 15% |
| Lead time and reliability | 10% |
| Ethical / sustainability practices | 10% |

**Minimum to proceed:** at least 2 qualified suppliers scoring 3.5 or higher out of 5, so there is no single point of failure.

## Logistics Options

| Mode | Lead time | Cost / kg | Best for |
|------|-----------|-----------|----------|
| Air freight | Short | High | Launch inventory, samples, top-ups |
| Ocean LCL | Long | Low–Medium | Routine replenishment once demand stabilizes |
| Ocean FCL | Long | Lowest | Year 3+ volumes |

## Fulfillment Model

| Option | Pros | Cons | Recommended phase |
|--------|------|------|-------------------|
| Self-fulfillment | Low fixed cost, full control | Doesn't scale, takes founders' time | Pilot (< 200 orders/mo) |
| 3PL | Scalable, faster shipping | Fees per order, minimums | Year 1+ |
| Marketplace fulfillment | Buy-box eligibility, Prime-style reach | Storage fees, less customer data | Selective SKUs |

## Operational KPIs to Track

- Landed cost per unit (product + freight + duty + brokerage + testing)
- Inventory turns and days of cover
- Order fill rate and on-time shipment rate
- Lot rejection rate at quality testing
