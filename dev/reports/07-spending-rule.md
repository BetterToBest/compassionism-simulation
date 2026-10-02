# Step 7 report: how much people spend

Oct 1, 2026 · plan step 7 · Claude · 500 paired seeds, three environments · harness only

## What this step changes, in plain words

The live page assumes people save every dollar they earn above the cost of living. The research runs used a placeholder instead: people spend 90% of it. Neither is measured.

I set the share from a primary source. Americans saved **5.4% of their disposable income in 2025** (US Bureau of Economic Analysis, Personal Income and Its Disposition, Table 2.1). In the model with no programme, people match that if they **spend 59.3% of what they earn above the cost of living** and save the rest. The figure is derived once, on the no-programme run, and not adjusted for any programme result. (2024's rate, 6.3%, gives 55.4%, shown as a row.) This rule now applies to everyone in every run from here on, with the programme and without it.

## What it does

The main row (all mechanisms so far, paid for by the Source):

| | Reference | Adverse | Stress |
|---|---|---|---|
| Poverty severity vs no programme | −5.69 | −14.10 | −6.84 |
| Basket poverty: programme / no programme | 29.8% / 55.2% | 51.6% / 78.2% | 67.5% / 78.2% |
| **Wealth poverty: programme / no programme** | **47.3% / 52.0%** | **87.2% / 82.6%** | **89.4% / 82.6%** |
| Same row at the old 90% spending share | 87.3% / 54.7% | 98.8% / 87.1% | 98.0% / 87.1% |

**In everyday words: with people saving at the rate Americans actually save, Compassionism at the reference settings now lowers poverty on all three measures**, including wealth, despite prices rising about 40% a year. In the Adverse Environment and the Stress Test it still leaves more adults with too little wealth than no programme would, because prices rise even faster there (51% and 23% a year) and savings are not protected from inflation.

The spending share mostly changes savings, not income: poverty severity moves by less than 0.2 between the old and new shares.

If every dollar the Source pays were backed by output (H1), wealth poverty would be 21.5% at reference (against 52.0%), 57.6% in Adverse (against 82.6%) and 73.8% in Stress (against 82.6%).

## Limits

- One spending share for everyone; in reality poorer people spend a larger share and richer people a smaller one.
- Savings earn no interest and are not protected from inflation in the model.

## Exact commands and files

- `node harness.js testbed 500 spend ref`, `… adv`, `… st` (outputs in `dev/runs/step7-spend-500-*.txt`).
- The derivation is checked by `spendUnitSuite` (5.40% on seeds 1-100). Code: `SPEND_SOURCED` in `harness.js`.
