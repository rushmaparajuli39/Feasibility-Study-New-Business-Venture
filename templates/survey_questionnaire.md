# Survey Questionnaire

**Target:** 100+ responses · **Length:** about 5 minutes · **Tool:** any online survey platform
**Purpose:** quantify purchase behavior and willingness to pay (WTP) to validate model inputs.

## Section A · Screener
1. In the past 12 months, have you bought any premium or specialty cooking ingredients? (Yes / No → end)
2. Where do you usually buy them? (Grocery / Specialty store / Online marketplace / Brand website / Other)

## Section B · Behavior
3. How often do you buy specialty ingredients? (Weekly / Monthly / Every few months / Rarely)
4. Typical spend per purchase? ($0–15 / $15–30 / $30–50 / $50+)
5. How important are the following? (1–5): Freshness · Origin · Price · Packaging · Ethical sourcing · Brand

## Section C · Price Sensitivity (Van Westendorp)
_After showing the concept card:_

6. At what price would this be **so expensive** you would not consider it?
7. At what price would it be **expensive**, but you would still consider it?
8. At what price would it be **a bargain**, a great buy for the money?
9. At what price would it be **so cheap** you would doubt its quality?

## Section D · Intent
10. How likely are you to buy this product? (1–5)
11. How likely would you be to subscribe for regular delivery? (1–5)

## Section E · Demographics (optional)
12. Age band · 13. Household size · 14. Region

## Analysis Plan
- The **acceptable price range** comes from the crossing points of the Van Westendorp curves. It is compared with `price_per_unit` in the model.
- Purchase intent of 4 or 5 is discounted by 50% or more to estimate realistic conversion.
- Results are cut by purchase frequency to identify the heavy-user segment.
