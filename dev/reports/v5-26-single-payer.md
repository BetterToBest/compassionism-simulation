# Single payer, public plan only (setting B)

Session 2a, Oct 13, 2026. Engine work only: the page does not change. It builds on today's system made explicit (setting A, `dev/reports/v5-25-health-today.md`). Choices, sources and alternatives: `dev/DECISIONS.md`, Session 2a.

## What the setting does

Setting B is a switch, off by default. Switched off, every figure stays the same (the guard test proves it). Switched on, from year 1 everyone has one public plan, as in the Medicare for All Act: no premiums, no deductibles and no bills at the point of care. Today's system keeps running in the background for the same people with the same medical needs, so every comparison is like for like.

- **More care is used.** No one skips care for cost any more, and people who would have been uninsured use 25% more care (the Oregon Health Insurance Experiment found about that). In the model, total care rises 12% over what is delivered today.
- **Each unit of care costs less (or not), in three cases from the Yale preprint** (Galvani and colleagues, 2026; not yet peer reviewed). The savings come from drug prices, Medicare rates for providers, administration, fraud, and avoided emergency care. The **central** case takes the preprint's own estimate. The **cautious** case takes its lower bound. In the **costs run higher** case, providers are paid near commercial rates and the savings vanish.
- **Who pays.** Government keeps paying what it pays today (Medicaid, Medicare, tax credits). The rest of the plan's cost is a flat health tax on money income. The employer's former premium share goes back to the household, because it was always part of pay.
- **Waits.** Today's health-care capacity grows to meet half the extra demand (a design value; tested at a quarter and at all of it). The rest waits.
- **Jobs.** At the start, about 1% of working adults lose administrative jobs in insurance and billing. They go through the model's usual job-loss path: a spell out of work, unemployment insurance, and lower pay on return.
- **Prices.** Medical prices no longer rise with demand, because the public payer sets the rates. A shortage shows up as waits instead (this rule was recorded before the setting was written).

## Results (Reference, 20 paired seeds)

**Spending and the household bill.** These are per person-year, today's dollars at year-0 prices, without the programme:

| | Today | Single payer: central | Cautious | Costs run higher |
|---|---|---|---|---|
| Health spending (all payers) | $7,684 | $6,235 (-19%) | $6,818 (-11%) | $7,842 (+2%) |
| Health tax, share of money income | none | 13.4% | 15.0% | 17.9% |
| Household's health bill per adult-year (today: premiums and out-of-pocket; single payer: tax less the returned employer share) | $4,366 | $2,365 | $3,174 | $4,594 |
| Needed care delayed (waits) | none | 5.5% | 5.5% | 5.5% |
| Adults skipping some care for cost, in a year | 12% | none | none | none |

**Poverty, without the programme (central case):**

| | Today's system | Single payer |
|---|---|---|
| Basket poverty, person-years | 50.5% | 46.5% |
| FGT2 (depth) | 7.82 | 6.19 |
| Too little wealth at year 20 | 33.2% | 30.5% |
| BLEI poverty | 26.6% | 25.0% |

**Poverty, with Compassionism:** basket poverty is 19.2% under today's system and 16.6% under single payer.

**How the two interact.** This is the change in the programme's own effect when single payer replaces today's system. It is reported on its own line, so that neither is credited with the other's work:

| | Total | Of which through prices |
|---|---|---|
| Basket poverty | +1.5 points (the programme's effect is smaller: single payer has already done part of the work) | -1.0 |
| FGT2 | +1.1 | -0.2 |
| Too little wealth | -2.6 (the programme's wealth result is better) | -4.5 |
| BLEI poverty | +0.6 | -0.7 |

Most of the price part comes from the price rule. Under today's system, the programme's extra demand for care raises medical prices; under single payer the public payer sets rates and it does not. That reflects how the model treats a public payer. It is not a saving Compassionism makes, and it is labelled that way.

Adverse and Stress show the same pattern. The no-programme gains are similar, and the interaction is smaller on basket poverty (files `dev/runs/health/all-adv.json`, `all-st.json`).

## Limits

- The preprint is not yet peer reviewed. Its savings factors are applied to the model's care, not re-derived.
- The administrative job figure comes from secondary summaries of a 2018 study; the study itself was not read.
- Waits come from a design parameter, not from country data. The attached country comparison failed three of five spot checks, so it was not used.
- The health tax is flat. A progressive health tax, Medicare for All's transition years, and how providers respond to Medicare rates over time are not modelled, beyond the costs-run-higher case.
- With PTF's health-sector price cut switched on, single payer would count that cut twice. Its figures hold only with the cut at 0, as in the main row; session 2b fixes this.
- Health does not yet improve with care received. That is session 2b's prevention link.

## Reproduce

`node dev/tools/health_check.js ref 20 --rows=off,A,Anx,B,Bcau,Bhigh --out=all` (also `adv`, `st`). Prices held flat: add `--flat --out=flat`. Sweeps: `--rows=Bnx,Bcap25,Bcap100,Badm0,Badm2,Bind0 --out=sweep`. Outputs are in `dev/runs/health/`.
