# How much the frozen engine's corrections move the figures (S47, Nov 5, 2026)

Before the full study batch runs, the engine is frozen: every row of every study will run with two sets of corrections switched on. This note measures, before any 500-seed result exists, how far each correction moves the figures. It is a measurement, not a study: nothing was tuned to it, and the frozen design does not depend on what it shows. The full tables are in `dev/reports/s47-fx-tables.md`. The per-seed values are in `dev/runs/s47-fx/`, and the script is `dev/tools/s47_fx_measure.js`.

## What was measured
The two sets of corrections:
- **The outside audit's three corrections** (row option `au`; `dev/reports/s13-engine-audit.md`): the BLEI test for the wage bonus and the price of joining PTF deflated by the price level; spending graded by income once the year's cash income is known; the financial-stability score deflated.
- **The second implementation's four fixes** (row option `fx`; `dev/reports/s50-independent-implementation/GAPS.md`, items 2, 6, 7 and 8):
  - `pthb`: PTH's books are opened after households are formed. Until now about 28% of household members in PTH homes had no books.
  - `hb`: the PTH home's price and the trust's rent are set at the market's housing cost, not the BLEI daily cost.
  - `ab`: SNAP's work rule no longer counts rounding remainders as lost months.
  - `sp` (new in this pull request): the essentials' capacity each year (the supply path) comes from the study's own no-programme run. That run has job loss, today's safety net, the labour response, wage indexation, households, and the study's own population. Until now it came from a separate price-only run that had none of these and always used 500 adults. As a result, prices drifted in the published no-programme run although no programme existed.

The design: three designs (no programme, the release design, and the C2.2 design: automatic, with the BU at the cost of food, housing and medical care, indexed); seven engine settings (published, `au`, `au` plus each `fx` part alone, frozen = `au` plus every `fx` part); all three environments; seeds 1-50, paired; CPS earnings yardstick, 500 adults, 20 years; the runner's reference settings on every row.

## What it shows
- **The supply-path fix works as intended.** With it, the no-programme run's essentials prices stay exactly still in every environment and on every seed (a unit test checks this on seed 1). In Reference the published no-programme price level had reached 1.0068 by year 20, about 0.7% above where it should be. In Adverse and Stress the drift was about 0.1%. Without the drift, the no-programme economy is a little better off: basket poverty is 0.3 to 0.4 points lower, wealth poverty 0.3 points lower, and median real wealth $1,900 to $5,800 higher.
- **The supply-path fix also lowers programme inflation**, by 0.24 to 0.59 points a year under both designs and in every environment. The programme's own demand is now measured against the capacity of the fuller no-programme economy, and on these figures that capacity is larger. Programme inflation stays very high: 16.6% to 45.9% a year on the frozen engine.
- **The other three fixes hardly move anything.** `hb` moves none of the twelve measures (it changes the trust's books, not households' outcomes). `ab` moves only the SNAP work-rule count, by under 0.01 months per adult. `pthb` moves programme inflation by at most 0.01 points, and the other measures by less than their intervals.
- **The audit's corrections are the larger change**, mostly through income-graded spending. On the published engine the C2.2 design cuts wealth poverty by 19.9 points in Reference, 23.5 in Adverse and 11.3 in Stress. On the frozen engine the cut is 17.4, 17.4 and 7.8 points. About 2.1, 5.2 and 2.8 points of that change come from the audit's corrections, and the rest from the fixes.
- **No programme effect changes direction.** On the frozen engine:
  - The C2.2 design's cut in basket poverty is 0.7 to 0.9 points smaller (24.7, 35.3 and 34.6 points).
  - The release design's cut in basket poverty is 0.2 to 0.5 points smaller in Reference and Adverse, and 0.1 points larger in Stress.
  - The release design's rise in wealth poverty in Adverse and Stress stays (10.4 and 11.2 points).
  - The median real wealth both designs leave at year 20 falls by a further $850 to $6,000 against no programme.

## Limits
- 50 seeds, one yardstick, 500 adults and 20 years. The full batch measures every correction again at 500 seeds in study R (the published engine, the audit's corrections only, and the frozen engine side by side).
- At 10,000 and 50,000 adults (studies A, B10, D10, J) the supply-path fix also replaces a supply path drawn from 500 adults. That effect is not measured here; study A's frozen rows carry it.
- The fix adds one no-programme run per seed for each distinct set of economy-wide switches, about one row's cost. The 2-seed dry run times it.
