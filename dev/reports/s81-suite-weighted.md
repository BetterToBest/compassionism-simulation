# The visual suite's averages, counted by weight (Nov 17, 2026)

**The question.** v5.9's main rows give 18 of the 500 simulated adults the place of rare, very rich families and count each one at its share of the population (a weight). The visual suite's series took plain averages, shares and medians over the 500 adults, so those 18 counted once each. The average days of basic living from savings came out at 550,000 to 730,000 against medians of 1,500 to 3,800: a figure about the 18, not the average adult. The suite page therefore showed no averages for v5.9. Do the other plain figures mix in those 18 adults too, and what are the averages when every adult counts at its weight?

**Dated note (Nov 19, 2026): the private businesses' BU price was paid a year late.** The programme rows here paid the private businesses' lower BU price out of the previous year's premium. The design sets that price at the sale, so this was a defect, now fixed behind an option (see [the report on the private price at the sale](s90-private-price-at-sale.md)). On v5.9's main rows, setting the price at the sale makes every poverty and wealth effect slightly larger in the programme's favour and changes no sign: across both designs, three environments and 20 and 40 years, the cut in basket poverty grows by 0.04 to 0.59 points, the cut in too little wealth by 0.06 to 0.38 points and the rise in median real wealth by $110 to $1,525, and programme inflation moves by less than 0.001 points a year. These runs are v5.9's main rows recorded in more detail, so the change applies to them directly; the weighted averages in this report were not recomputed. No rerun of this study is planned now; a rerun would be its own preregistered amendment.

**What was run.** The export tool (`dev/tools/explore_export.js --suite`) now also writes every mean, median, tier share, share below 30 days, relative poverty and share taking part counted by weight (31 new keys, named with a leading `w`). Nothing in the engine changed (no version change of the model; the plain keys are as before). A second run of v5.9's main row on GitHub Actions: 500 simulated adults, 500 paired seeds, Reference, Adverse and Stress, 20 and 40 years, as preregistered (its preregistration was written before the run). Results: compassionism-sim-results `x4-a60bd3e/`, run-study run 127, engine commit `a60bd3e`.

**Check first: nothing else moved.** Every plain value of every row, year and environment (the bands, deciles, one seed's adults and all suite series, six shards) equals the earlier run's stored series exactly. Every engine output of every row and seed again equals v5.9's stored results. `dev/tools/suite_r2.py` now checks the first of these again each time it writes the suite files.

## The averages, counted by weight (Year 40, Reference, days)

| | Savings, plain average | Savings, average by weight | Savings, median by weight | Pay, average by weight | Allowance, average by weight |
|---|---|---|---|---|---|
| No program | 565,170 | 8,173 | 1,467 | 17.2 | 0 |
| Full-coverage design | 727,276 | 12,340 | 3,735 | 40.6 | 43.9 |
| Opt-in design (release) | 701,913 | 11,003 | 2,630 | 36.8 | 24.5 |

The plain average from savings was about 60 to 70 times the weighted one; the weighted average is still several times the median because a few adults with very large savings pull any average up. That is the real shape of wealth, not an error. Both the weighted average and median are now on the suite page beside each other. All 18 environment-by-horizon-by-design rows are in the data files (`data/releases/r2/suite-20.json`, `suite-40.json`) and the results folder.

## Does any other plain figure mix in the 18 adults? Yes, slightly; only the savings average was wrong in kind.

I compared every plain key with its weighted counterpart in every year (540 environment, design and year cells per key), against the spread across the runs (the 10th to 90th percentile of the weighted figure).

| Plain figure | Largest difference | Largest relative | Cells where it exceeds the spread |
|---|---|---|---|
| Average days from savings | 714,937 days | about 99% | all 540 |
| Average days from pay | 0.32 days | under 1% | 0 |
| Average days from the allowance | 0.02 days | under 0.3% | 0 |
| Median days from savings | 76 days | 4.7% | 0 |
| Median days from pay | 0.15 days | 0.6% | 0 |
| Median days from the allowance | 0.25 days | (a median that is near 0 in many designs, so a relative figure means little) | 10 of 540 |
| Median BLEI (all, participants, non-participants) | 76, 82, 51 days | 4.7%, 4.3%, 4.7% | 0 |
| Share below 30 days (both readings) | 0.61 points | | 0 |
| Share below 60% of the median income | 0.21 points | | 0 |
| Share taking part | 0.09 points | | 0 |
| Tier shares, all adults | 0.85 points | | 0 |
| Tier shares, participants | 1.07 points | | 2 of 360 (the Crisis step, by 0.06 points) |
| Tier shares, non-participants | 0.90 points | | 0 |

So only the savings average was wrong in kind. Every other plain share and median moves by about one point or less (medians by at most 5%) and, with a handful of exceptions among very small quantities, by less than the spread across the runs. Conclusions drawn from them do not change. The suite page still shows the plain shares and tiers (they equal v5.9's published basic-living figure, which is also unweighted; see below); the parts-of-BLEI section now shows the weighted medians and averages, and says so.

## What is not changed, and one decision for Duke

The engine's own share of adults below 30 days of basic living (the `pbO` key behind v5.9's headline basic-living effects, for example the programme's effect on adult-years below 30 days) is also counted once per simulated adult, not by weight. Counted by weight the share is up to 0.61 points different in a single year, less than the spread across the runs. Nothing is changed here: those effects are v5.9's stored published results. Whether the engine's published share should count by weight in a later release is a decision for Duke (ledger).

## Where everything is

- Data: `data/releases/r2/suite-20.json`, `suite-40.json` (weighted keys beside the plain ones; `index.json` records both jobs); written by `python3 dev/tools/suite_r2.py RESULTS/x4-a60bd3e RESULTS/x2-5b62481`, checked by `--check`.
- Page: the suite page's v5.9 view, "What the days are made of" section.
- Results: compassionism-sim-results `x4-a60bd3e/` (run.txt, SHA256SUMS, six shards).
- Preregistration: research-update `prereg/2026-11-x4-weighted-addendum.md` (written before the run).
