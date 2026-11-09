# Distribution measures (S57): what was added, and what the pilot shows

Plain-words report. Preregistration: BetterToBest/research-update `prereg/2026-11-s57-distribution-measures.md` (with Amendment 1 of Nov 9). Engine: this repository, branch `claude/s57-distribution-measures`, tool commit `f156393`. Results: BetterToBest/compassionism-sim-results `s57-distribution-f156393` (per-seed values, `tables.md`, `estimates.csv`, run.txt, SHA256SUMS).

## What this step is
The model already reported two wealth Ginis. This step adds the other ways to describe a distribution that reviewers asked for: how much the top 1%, top 10% and bottom 50% hold; the Palma ratio; real wealth and income at 21 points of the distribution; how families move between wealth fifths; labour's share of money income; and how deep debt goes. It only measures: no random draw and no rule changes, and with the option off every output is identical to before (guard test, 25 rows × 20 seeds × 483 outputs in each environment). The option is `dm` on a study's options.

Both runs of every row get the measures, so every programme result sits beside its own no-programme run on the same seed. The frozen full batch holds none of these (it stores no per-adult data), except the Gini with debts kept (`eGiniWN`), which was already in it. Re-running the batch's main rows with `dm` on is for the freeze step (S63) to decide.

## The pilot
100 seeds, 500 adults, 20 years, the three environments, the frozen yardstick (CPS earnings, today's safety net): the no-programme run, the release row and the C2.2 design. Family: preregistered secondary. Differences are programme minus no programme on the same seed; intervals are the 95% paired-bootstrap interval (2,000 resamples) and are **not adjusted**. 378 estimates in all (environments × designs × measures, percentile points and mobility summaries); 366 have an interval that excludes zero, and 359 of those survive Holm within the family (using the normal tail of the mean over its bootstrap standard error, Amendment 1). "Excludes zero" does not mean large: read the sizes.

## Checks of the no-programme start (never targets)
At the end of Year 0, with no programme (identical in all three environments, which differ only in later years):

| Measure | Model | Outside figure | Gap |
|---|---|---|---|
| Top 1% share of wealth | 20.8% (20.2 to 21.3) | 32.5% (Fed Distributional Financial Accounts, Q2 2026) | 11.7 points below |
| Top 10% share of wealth | 64.6% (63.9 to 65.4) | 69% without Social Security wealth, 60% with (CBO, 2022) | 4.4 points below the first; 4.6 above the second |
| Bottom 50% share of wealth | 3.6% (3.5 to 3.7) | 6% (CBO, 2022) | 2.4 points below |

The start is close at the top 10%. The top 1% is far below: the engine's starting wealth comes from the Survey of Consumer Finances' percentile table, which leaves out the Forbes 400, and the weighted top tail (S59) is the planned fix. The preregistered 10-point rule applies to the top 10%, which passes; the top 1% gap is reported and handed to S59. Nothing was tuned to these figures.

## Findings (end of year 20; programme minus no programme)

**Wealth is far more equal with the programme, more with the C2.2 design than the release row.** Top 10% share of wealth, no programme 58.9% (Reference): −27.0 points (−27.6 to −26.3) with the release row and −33.3 (−34.0 to −32.5) with the C2.2 design. Bottom 50% share: 5.2% without the programme, +11.9 and +20.9 points. The Gini with debts kept (eGiniWN) falls from 0.73 by 0.25 and 0.38. Adverse and Stress show the same direction with smaller release-row effects (Stress top 10% share −13.0 points; bottom 50% share +1.7). In Stress the release row raises families in debt by 3.7 points (3.3 to 4.1) while the C2.2 design lowers it by 25.5.

**Income shares move little and in different directions by design.** Top 10% share of disposable income, no programme 24.9% (Reference): +1.0 point with the release row (0.9 to 1.1), −1.7 with the C2.2 design. The income Palma ratio goes from 1.29 by +0.10 (release row) and −0.24 (C2.2 design). So the release row widens income shares slightly while narrowing wealth sharply; the C2.2 design narrows both.

**Families in debt fall under both designs** (Reference: 22.0% without; −12.4 and −21.2 points). The median debt of families in debt is $10,000 in every no-programme Reference run because the engine's borrowing floor (−$10,000 in Year-0 dollars) binds for the median indebted family; it is not a free measure of debt depth, and the fall to near zero under the programme means that few families remain at the floor. Debt against income (0.25 without the programme) falls to about zero.

**Real wealth falls at most points under the release row, because of its price level, not because wealth is destroyed.** The measures are in Year-0 dollars, using each run's own price level. The release row's prices rise about 32% a year in the Reference environment (the engine's `endoAnn`, seeds 1-3), so a nominal dollar of wealth buys much less at Year 20. The median real wealth reported here equals the engine's own `medWealthReal` exactly (checked on three seeds: $192,950 without the programme, $27,166 with the release row). Shares, ratios and Ginis do not depend on the price level; the dollar percentiles and growth-incidence curves do. Under the release row the real wealth of the poorest tenth is $12,171 higher in Reference (the no-programme poorest tenth sits at the −$10,000 debt floor) and the real wealth of the median is $182,831 lower. This is the price-rule question S58 takes up; it is not a finding about the programme's design intent.

**Real disposable income** (the growth-incidence curve of income) is nearly flat under the release row across the distribution (Reference: −$1,270 at P1, −$791 at P50, +$24,071 at P99) and rises by $14,000 to $45,000 under the C2.2 design (+$21,304 at the median). The income curves compare the same rank in the two distributions, not the same person.

**Rank mobility rises with the programme, but read this carefully.** In Reference, 65.6% of adults stay in their starting wealth fifth without the programme; with the release row that falls by 30.4 points (−31.0 to −29.7), and with the C2.2 design by 32.0. Both up and down moves rise by about 15 points. The share of the poorest fifth reaching the top two fifths goes from 0.4% to 10.2% (release row) and 12.0% (C2.2 design). Part of this is arithmetic: when wealth is compressed, small dollar differences reorder ranks, so rank movement rises even if little money changes hands. Do not read it as more opportunity without a dollar-based mobility measure, which this step does not provide.

## Limits, stated plainly
- **Labour's share is close to 100% by construction.** The model's money income is wages, conversion proceeds and transfers, with no capital income, and the basic unit (BU) is in kind. So the share of wages falls with the programme only because transfers enter money income (−10.4 points release row, −28.7 C2.2 design, Reference), and wages plus conversion proceeds stay at 99.8%. It is not national labour share.
- **The wealth ratio (top 10% over bottom 40%) is unstable where the bottom 40% hold little**: Adverse and Stress no-programme mean 388 with an interval from −846 to −129 on the difference. It is reported only for seeds where the bottom 40% hold positive wealth (Stress uses 97 to 100 seeds), and the share measures should be preferred.
- Real-dollar percentiles depend on each run's price level (see above).
- 100 seeds, 500 adults, 20 years; the full batch cannot be recomputed. No P99.9 or top 0.1% share: 500 adults cannot support it.
- A family's income is the sum of its members' per-adult disposable income as the engine defines it.
- Adverse and Stress share the same no-programme run (they differ only in the programme's settings), so their no-programme columns are identical.

## For S63 and later steps
- Decide whether the main rows run again with `dm` on (the frozen batch cannot supply these measures).
- S58 (price rule) should report these measures too; the real-dollar results here are dominated by the release row's price level.
- S59's tail should close the top-1% gap against the Fed's accounts; `dm` is already weighted, with weights all 1.

## Reproducing
```
node dev/tools/s57_dm.js ENV 100 20 --out=s57-dm-ENV.json      ENV = ref, adv, st (about 90 s each, from a clean checkout)
python3 dev/tools/s57_table.py DIR --data data/studies/s57-distribution.json
```
Tests: `dmUnitSuite` in `harness.js` (8 tests; unit total now 272).
