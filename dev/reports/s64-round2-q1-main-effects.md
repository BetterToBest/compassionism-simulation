# Round 2, question 1: what each design does at the main row (S64)

Nov 15, 2026. The round-2 batch of the Compassionism Simulation, read as frozen. Engine `104691f` (compassionism-simulation pull request 107), 500 adults, seeds 1-500, Reference, Adverse and Stress, 20 and 40 years. Preregistered before any run: research-update `prereg/2026-11-s63-round2-freeze.md` (with three dated amendments; the third, after the results were read, records the checks and five points of reading, and changes no outcome or rule). Results: compassionism-sim-results `r2-m-<env>-<years>-104691f/` (part M, every key at full precision, with `run.txt` and `SHA256SUMS`). Tables: `dev/runs/s64-round2/s64-q1-main.md`, made by `python3 dev/tools/s64_tables.py`.

## In short

1. **Both designs lower all three poverty measures, in every environment and at both horizons, by large margins.** All 60 primary tests have intervals that exclude zero, and all 60 survive the Holm correction. 48 of them are material; the 12 that are not are all programme inflation, which stays below a fifth of a point a year.
2. **C2.2 does about one and a half to five times as much as the release design.** In Reference at 20 years, C2.2 lowers basket poverty (income below the cost of the basket of essentials) by 32.4 points, from 36.1% of adult-years to 3.7%; the release design by 20.9 points, to 15.2%. In Stress the release design's effects shrink to a third of Reference's (basket poverty −7.7 points), while C2.2's grow.
3. **Median real wealth roughly doubles under C2.2** (Reference, year 20: $223,900 without the programme, $432,300 with it) and rises by 44% under the release design ($323,300).
4. **These are the main row's figures, and the main row assumes full backing.** Every dollar the programme pays is matched by new output: that is the design's statement (ledger decision D25), a design parameter, not something the model estimates. Question 4's report shows what happens when it is not. The wealth figures rest on today's price rule (ledger decision D26).
5. **Seed intervals here are narrow and cover only the model's randomness.** The range across the preregistered readings (question 2's report) comes first in any headline; this report gives the main row alone.

## What was run

- **The main row** (harness.js `r2FreezePair`): the round-2 candidate main row with full backing, today's price rule and S69's two reporting corrections, both designs, each against the same no-programme run with the same random draws (paired seeds).
- **C2.2** pays every adult enough to reach the cost of the basket of essentials (the C2.2 design); **the release design** is the design of release 1, paid by the Source.
- **Effect:** the programme run minus the no-programme run, averaged over 500 seeds, with a 95% interval from a paired bootstrap (2,000 resamples). Holm correction across the 60 primary tests (5 outcomes × 2 designs × 3 environments × 2 horizons).
- **Materiality** (fixed before any run): 1 point for the poverty measures, 1 point a year for inflation, 5% of the no-programme median real wealth (about $11,200 in Reference at 20 years).

## The five headline outcomes (effect, points unless stated; 95% interval)

| | Reference 20 y | Reference 40 y | Adverse 20 y | Adverse 40 y | Stress 20 y | Stress 40 y |
|---|---|---|---|---|---|---|
| **C2.2** | | | | | | |
| basic living (adult-years below 30 days) | −18.7 | −18.9 | −19.8 | −23.0 | −19.8 | −23.0 |
| basket poverty | −32.4 | −30.7 | −40.6 | −46.1 | −40.1 | −45.4 |
| wealth poverty, yearly average | −18.6 | −20.1 | −19.6 | −23.8 | −19.1 | −23.3 |
| median real wealth ($) | +208,400 | +442,700 | +197,400 | +388,800 | +169,500 | +330,700 |
| programme inflation (points a year) | +0.15 | +0.06 | +0.18 | +0.09 | +0.18 | +0.09 |
| **Release design** | | | | | | |
| basic living | −12.3 | −13.5 | −10.6 | −11.2 | −4.3 | −4.5 |
| basket poverty | −20.9 | −20.0 | −18.9 | −16.7 | −7.7 | −6.8 |
| wealth poverty, yearly average | −10.9 | −12.9 | −9.6 | −10.7 | −3.9 | −4.4 |
| median real wealth ($) | +99,400 | +212,100 | +72,000 | +113,300 | +28,800 | +46,400 |
| programme inflation (points a year) | +0.12 | +0.05 | +0.08 | +0.01 | +0.02 | +0.00 |

Every interval is within ±0.2 points of the estimate for the poverty measures and within ±3.1% for median wealth; they are in the tables. Without the programme, basket poverty is 36.1% of adult-years in Reference and 44.6% in Adverse and Stress at 20 years (Stress changes only the programme's own conditions, so its no-programme run is Adverse's).

## Beside the headline

- **Wealth poverty at fixed years.** At year 20 C2.2 lowers it by 22.5 points (Reference) and the release design by 14.4; at year 40, by 19.9 and 14.5. The yearly average (the headline) is smaller than the year-20 figure because the effect builds up over the first years.
- **Median real wealth as a yearly average** is about half the end-of-run figure (C2.2, Reference: +$109,700 over 20 years, +$221,900 over 40), because the gap widens over time.
- **Basket poverty on the within-year count** (costs at the within-year price level, S68) is the same as the published measure to two decimals on the main row: at full backing prices barely move within a year.
- **Programme cost** (cash, endowments, BU, conversions, capital and price cuts, per adult a year in year-0 dollars) is about $80,500 for C2.2 in Reference at 20 years and $38,100 for the release design. In Stress the release design's cost falls to $9,700: Stress sets the programme's take-up at 40% and a smaller PTF share.

## Unfavourable and null results

- **Programme inflation is never material.** It is the one outcome where the programme is worse than no programme in every cell (the interval excludes zero), but by 0.00 to 0.18 points a year. Rule 3 calls this "no material change".
- **The release design in Stress** keeps every effect's sign but loses about two thirds of it. Stress lowers participation in the programme (40%) and the PTF share; the release design depends on both.
- Other unfavourable results (fewer adults working, less mobility out of the lowest wealth fifth, a smaller labour share of income) are in questions 6 and 7's reports.

## What these figures do not cover

The seed intervals measure the model's randomness only. They do not cover the choice of main row (D26) or of full backing (D25), the readings question 2 sweeps, or the engine's structure: one price rule for the whole economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub's statements and S62's costs, 500 adults (the 10,000-adult pair in question 7's report agrees on hours and the tail). The erosion share of each wealth figure (S66) is computed in S64 part 3.
