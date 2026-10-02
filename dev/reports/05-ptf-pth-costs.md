# Step 5 report: what community businesses and housing cost

Oct 1, 2026 · plan step 5 · Claude · 500 paired seeds, three environments · harness only

## Claude's reading of the design

- **Community businesses (PTFs):** the Hub calls them "not-for-profit, for-community-benefit enterprises" that reinvest surplus instead of paying shareholders. Their capital comes from the ESP split's reinvestment (steps 1-2).
- **Community housing (PTH):** capital comes from government, philanthropy or residents' pay-in. Residents then pay reduced rents covering "taxes, insurance, maintenance only" (PTH Independent Financing). The Hub's example: $1,200 a month against a market rent of $2,000.

## How the model costs them (sourced figures)

**PTF.** A PTF whose capital was paid for by reinvestment does not need to earn a profit or a return on capital. It still pays wages, suppliers, taxes and wear and tear. So it can lower prices by the industry's net profit margin (operating surplus less depreciation). From the US Bureau of Economic Analysis (2025 value added and depreciation by industry) and Census (grocers' 28.8% gross margin):

| Industry | Margin a PTF can give back, per dollar of sales |
|---|---|
| Grocers | 2.7% |
| Restaurants and food services | 7.6% |
| Utilities | 20.3% |

Weighted by what people spend (BEA, 2025), that is 4.9% off food and 2.6% off the housing component (through utilities): about 1.2% of the cost of living, or roughly 8% of the 12%+ discount the model gives PTF members. **That part no longer counts as a programme cost.** The rest of the discount is a running subsidy and is still counted, as before.

**PTH.** There are $156,000 of housing structures per rented home in the US (BEA housing stock / Census renter households, 2025; land not included). In the housing industry, 55% of rents is net return on capital (BEA 2025). So PTH's 35% rent cut fits inside the return a PTH does not have to pay, and residents' rents still cover running costs, taxes and upkeep, as the Hub says. The cost of PTH is that forgone return, which equals the rent cut. The model already counted it that way, so nothing changes.

## What it does

Against step 4's row (paid for by the Source):

| | Reference | Adverse | Stress |
|---|---|---|---|
| Poverty severity | −0.02 | −0.08 | −0.07 |
| Basket poverty (points) | −0.21 | −0.28 | −0.12 |
| Wealth poverty (points) | −0.15 | −0.01 | −0.02 |
| PTF discount now not counted as cost (per adult a year) | $164 | $164 | $85 |

**In everyday words: a small gain, confirmed on all three measures in every environment.** It comes from a slightly lower wage contribution (5.4% → 5.0% at reference).

If every PTF and PTH price cut cost nothing (the "price cuts free" row), the gain is larger: −0.35 / −1.06 / −0.96, with the remaining wage contribution falling to almost zero.

## Limits

- The PTF industries are grocers, food services and utilities only; the Hub also lists transport, childcare, clinics and schools.
- Land under PTH housing is not costed (no BEA figure), so PTH capital is understated.
- The figures are national averages; places differ.

## Exact commands and files

- `node harness.js testbed 500 cost ref`, `… adv`, `… st` (outputs in `dev/runs/step5-cost-500-*.txt`).
- Code: `COST` in `harness.js`, with every source in its comment. Tests: `costUnitSuite`, 3 tests.
- Choices made: `dev/DECISIONS.md`, "Step 5".
