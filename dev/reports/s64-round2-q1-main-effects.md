# The v5.9 model, question 1: what each design does at the main row

> **Note (Nov 28, 2026).** The results repository named in this document, `BetterToBest/compassionism-sim-results`, is offline: GitHub disabled it. Every figure can be reproduced from the engine commit named beside it, with the commands in `REPRODUCE.md`. The results folders are deposited in an archive with a permanent identifier, DOI 10.5281/zenodo.24615619 (copied on OSF at osf.io/7v5ur); folders not in the archive are listed in `data/results-manifest.json`.

Nov 15, 2026. The v5.9 batch of the Compassionism Simulation, read as frozen. Engine `104691f` (compassionism-simulation pull request 107), 500 adults, seeds 1-500, Reference, Adverse and Stress, 20 and 40 years. Preregistered before any run: research-update `prereg/2026-11-s63-round2-freeze.md` (with three dated amendments; the third, after the results were read, records the checks and five points of reading, and changes no outcome or rule). Results: compassionism-sim-results `r2-m-<env>-<years>-104691f/` (part `M`, every key at full precision, with `run.txt` and `SHA256SUMS`). Tables: `dev/runs/s64-round2/s64-q1-main.md`, made by `python3 dev/tools/s64_tables.py`.

## In short

1. **Both designs lower all three poverty measures, in every environment and at both horizons, by large margins.** All 60 primary tests have intervals that exclude zero, and all 60 survive the Holm correction. 48 of them are material; the 12 that are not are all programme inflation, which stays below a fifth of a point a year.
2. **The full-coverage design, built to meet NEEC's criterion C2.2, does about one and a half to five times as much as the opt-in design.** In Reference at 20 years, the full-coverage design lowers basket poverty (income below the cost of the basket of essentials) by 32.4 points, from 36.1% of adult-years to 3.7%; the opt-in design by 20.9 points, to 15.2%. In Stress the opt-in design's effects shrink to a third of Reference's (basket poverty −7.7 points), while the full-coverage design's grow.
3. **Median real wealth roughly doubles under full coverage** (Reference, year 20: $223,900 without the programme, $432,300 with it) and rises by 44% under the opt-in design ($323,300). Less than 3% of any wealth figure is the erosion of the balances adults held at the start (added Nov 15), and that small part helps the programme: slightly higher prices lower what net debtors owe.
4. **These are the main row's figures, and the main row assumes full backing.** Every dollar the programme pays is matched by new output: that is the design's statement, a design parameter, not something the model estimates. Question 4's report shows what happens when it is not. The wealth figures rest on full backing (corrected Nov 17, 2026: this sentence said today's price rule, which full backing barely tests).
5. **Seed intervals here are narrow and cover only the model's randomness.** The range across the preregistered readings (question 2's report) comes first in any headline; this report gives the main row alone.

## What was run

- **The main row** (harness.js `r2FreezePair`): the v5.9 candidate main row with full backing, today's price rule and the second implementation's two reporting corrections, both designs, each against the same no-programme run with the same random draws (paired seeds).
- **Full coverage** pays every adult enough to reach the cost of the basket of essentials (the full-coverage design); **the opt-in design** is the design of v5.6, paid by the Source.
- **Effect:** the programme run minus the no-programme run, averaged over 500 seeds, with a 95% interval from a paired bootstrap (2,000 resamples). Holm correction across the 60 primary tests (5 outcomes × 2 designs × 3 environments × 2 horizons).
- **Materiality** (fixed before any run): 1 point for the poverty measures, 1 point a year for inflation, 5% of the no-programme median real wealth (about $11,200 in Reference at 20 years).

## The five headline outcomes (effect, points unless stated; 95% interval)

| | Reference 20 y | Reference 40 y | Adverse 20 y | Adverse 40 y | Stress 20 y | Stress 40 y |
|---|---|---|---|---|---|---|
| **Full coverage** | | | | | | |
| basic living (adult-years below 30 days) | −18.7 | −18.9 | −19.8 | −23.0 | −19.8 | −23.0 |
| basket poverty | −32.4 | −30.7 | −40.6 | −46.1 | −40.1 | −45.4 |
| wealth poverty, yearly average | −18.6 | −20.1 | −19.6 | −23.8 | −19.1 | −23.3 |
| median real wealth ($) | +208,400 | +442,700 | +197,400 | +388,800 | +169,500 | +330,700 |
| programme inflation (points a year) | +0.15 | +0.06 | +0.18 | +0.09 | +0.18 | +0.09 |
| **Opt-in design** | | | | | | |
| basic living | −12.3 | −13.5 | −10.6 | −11.2 | −4.3 | −4.5 |
| basket poverty | −20.9 | −20.0 | −18.9 | −16.7 | −7.7 | −6.8 |
| wealth poverty, yearly average | −10.9 | −12.9 | −9.6 | −10.7 | −3.9 | −4.4 |
| median real wealth ($) | +99,400 | +212,100 | +72,000 | +113,300 | +28,800 | +46,400 |
| programme inflation (points a year) | +0.12 | +0.05 | +0.08 | +0.01 | +0.02 | +0.00 |

Every interval is within ±0.2 points of the estimate for the poverty measures and within ±3.1% for median wealth; they are in the tables. Without the programme, basket poverty is 36.1% of adult-years in Reference and 44.6% in Adverse and Stress at 20 years (Stress changes only the programme's own conditions, so its no-programme run is Adverse's).

## Beside the headline

- **Wealth poverty at fixed years.** At year 20 the full-coverage design lowers it by 22.5 points (Reference) and the opt-in design by 14.4; at year 40, by 19.9 and 14.5. The yearly average (the headline) is smaller than the year-20 figure because the effect builds up over the first years.
- **Median real wealth as a yearly average** is about half the end-of-run figure (full coverage, Reference: +$109,700 over 20 years, +$221,900 over 40), because the gap widens over time.
- **Basket poverty on the within-year count** (costs at the within-year price level) is the same as the published measure to two decimals on the main row: at full backing prices barely move within a year.
- **Programme cost** (cash, endowments, BU, conversions, capital and price cuts, per adult a year in year-0 dollars) is about $80,500 for the full-coverage design in Reference at 20 years and $38,100 for the opt-in design. In Stress the opt-in design's cost falls to $9,700: Stress sets the programme's take-up at 40% and a smaller PTF share.

## How much of each wealth figure is the erosion of opening balances (added Nov 15)

The question (preregistered in the freeze file's Q6 and decision rule 6): when the programme raises prices, the money adults held at the start buys less. How much of each wealth result is that, and nothing else? The main row holds wealth by asset class, so homes, shares and businesses keep up with prices and only money claims are eroded: deposits, bonds and the non-stock part of funds, less floating- and fixed-rate debt. The erosion term is the change in the real value of each adult's opening money claims, held untouched at the engine's own returns, between the programme run and the no-programme run (freeze file Amendment 4, written before the trace ran). The trace (`dev/tools/s64_erosion.js`) ran the batch's own rows, seeds 1-500, and reproduced the batch's stored figures in every seed.

- **Under 3% everywhere, and in the programme's favour.** Erosion accounts for 0.4 to 1.8% of the headline wealth-poverty effect and 0.0 to 1.5% of the headline median-wealth effect; at most 2.9% of any wealth figure (median wealth as a yearly average, opt-in design, Reference, 20 years). Without it, the full-coverage design lowers wealth poverty by 18.4 points instead of 18.6 (Reference, 20 years) and raises median real wealth by $206,400 instead of $208,400.
- **Why it helps rather than hurts.** At full backing the programme's prices rise only 0.0 to 0.2 points a year faster, but over the years that lowers the real value of what adults owe. In each of the lowest four fifths of opening wealth, adults owe more in money terms than they hold on average (fixed-rate debt such as a mortgage, against a home that keeps its value), so the erosion term is a small gain there ($80 to $2,200 per adult at year 20, 0.5 to 1.7% of the fifth's wealth gain); it adds to the median and lifts some adults over the $25,000 line. Creditors lose: in the top fifth the erosion term is a loss.
- **The low-share trace's all-cash term, as a bound.** If all opening wealth were cash, as before the v5.9 model, the sign reverses for median wealth (−0.0 to −5.3%) and is near zero for wealth poverty (−0.6 to +0.1%). Either way it is small.

Erosion share of each wealth figure, the main reading, with the all-cash bound in brackets. A positive share means erosion is part of the published gain; every published effect here is material, so every share is read.

| Figure | Design | Reference 20 y | Reference 40 y | Adverse 20 y | Adverse 40 y | Stress 20 y | Stress 40 y |
|---|---|---|---|---|---|---|---|
| wealth poverty, yearly average | Full coverage | 1.0% (0.1%) | 0.5% (0.1%) | 0.9% (0.1%) | 0.4% (0.0%) | 1.0% (0.1%) | 0.4% (0.0%) |
| wealth poverty, yearly average | release | 1.8% (−0.2%) | 1.1% (−0.1%) | 1.6% (−0.3%) | 0.8% (−0.1%) | 1.6% (−0.6%) | 0.7% (−0.3%) |
| median real wealth (weighted, end of run) | Full coverage | 1.0% (−1.7%) | 0.4% (−0.7%) | 0.8% (−1.6%) | 0.3% (−0.5%) | 0.9% (−1.8%) | 0.3% (−0.6%) |
| median real wealth (weighted, end of run) | release | 1.5% (−2.8%) | 0.6% (−1.2%) | 1.0% (−1.8%) | 0.1% (−0.2%) | 0.5% (−0.9%) | 0.0% (0.0%) |
| median real wealth, yearly average | Full coverage | 1.8% (−3.4%) | 0.9% (−1.6%) | 1.8% (−3.2%) | 0.8% (−1.5%) | 2.0% (−3.7%) | 0.9% (−1.7%) |
| median real wealth, yearly average | release | 2.9% (−5.3%) | 1.4% (−2.6%) | 2.5% (−4.6%) | 1.0% (−1.9%) | 2.3% (−4.1%) | 0.8% (−1.3%) |
| wealth poverty at the year | Full coverage | 0.2% (0.0%) | 0.0% (0.0%) | 0.1% (0.0%) | 0.0% (0.0%) | 0.1% (0.0%) | 0.0% (0.0%) |
| wealth poverty at the year | release | 0.9% (0.0%) | 0.3% (0.0%) | 0.5% (−0.2%) | 0.0% (0.0%) | 0.3% (−0.2%) | 0.0% (0.0%) |
| median real wealth at the year | Full coverage | 0.9% (−1.9%) | 0.4% (−0.7%) | 0.8% (−1.6%) | 0.3% (−0.5%) | 1.0% (−1.8%) | 0.3% (−0.6%) |
| median real wealth at the year | release | 1.6% (−2.9%) | 0.6% (−1.2%) | 1.0% (−1.9%) | 0.1% (−0.2%) | 0.5% (−0.9%) | 0.0% (0.0%) |

Full tables (intervals, the effect without erosion, the mean gap per adult and by fifth): `dev/runs/s64-erosion/tables.md`; results in compassionism-sim-results `r2-erosion-104691f/`.

## Unfavourable and null results

- **Programme inflation is never material.** It is the one outcome where the programme is worse than no programme in every cell (the interval excludes zero), but by 0.00 to 0.18 points a year. Rule 3 calls this "no material change".
- **The opt-in design in Stress** keeps every effect's sign but loses about two thirds of it. Stress lowers participation in the programme (40%) and the PTF share; the opt-in design depends on both.
- Other unfavourable results (fewer adults working, less mobility out of the lowest wealth fifth, a smaller labour share of income) are in questions 6 and 7's reports.

## What these figures do not cover

The seed intervals measure the model's randomness only. They do not cover the choice of main row or of full backing, the readings question 2 sweeps, or the engine's structure: one price rule for the whole economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub's statements and the PTF-realism study's costs, 500 adults (the 10,000-adult pair in question 7's report agrees on hours and the tail). The erosion share above covers the opening balances only: the creditor charge on shares, which also moves with prices, is printed beside it in the tables as a check and not counted in it.
