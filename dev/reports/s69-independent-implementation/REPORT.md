# A third, independent implementation of the simulation: the candidate main row of round 2

> **Note (Nov 28, 2026).** The results repository named in this document, `BetterToBest/compassionism-sim-results`, is offline: GitHub disabled it. Every figure can be reproduced from the engine commit named beside it, with the commands in `REPRODUCE.md`. The results folders are deposited in an archive with a permanent identifier, DOI 10.5281/zenodo.24615619 (copied on OSF at osf.io/7v5ur); folders not in the archive are listed in `data/results-manifest.json`.

*Report for Duke Johnson, November 14, 2026 (research-update step S69, part 2; phase 1).*

**Note on the title (Nov 17, 2026; the release reviews' triage, research-update `audits/2026-11-release-review-triage.md`).** This program was written from the description with the engine's code excerpts and per-seed results to check against, so it is not an independent model. Its exact agreement shows that the description, the code and a careful port agree, and it found three gaps between the description and the code. It cannot catch a modelling choice that both share, for example that the model has no limit on what the economy can supply. The findings below stand.

## What was checked

The simulation follows 500 adults and their households for 20 years, twice on the same random draws: once with the programme and once without. Since the last check, round 2 added a great deal to the model:
- open access to the community businesses (PTFs), and the growth of their share of sales;
- the PTFs' running costs and who pays them;
- adults outside the labour force, and adults moving in and out of work each year;
- a borrowing limit for ordinary spending;
- wealth held as homes, shares, businesses and savings, the income that wealth pays, and who loses when inflation shrinks a debt;
- a weighted top tail for the very wealthy;
- bargaining;
- a government account.

The question is whether the model's written description and its code do the same thing. An outside economist has not yet reviewed the model, so the strongest check one author can arrange is to write the model again, separately, and see whether the two give the same numbers.

This check (the third, after October 29 and November 1) did that for the main row Claude recommends for the design freeze: the C2.2 design (every adult receives Basic Units that cover the C2.2 needs, indexed every year, paid for by the Source), with every round-2 part at its recommended setting, and the same economy with no programme. A new program, in a different language (Python), was written from the packet the engine produced: the written description, every setting as data, the code that runs, and the engine's results for 500 seeds in three environments (Reference; Adverse, with recessions, automation and 2% outside inflation; Stress, the same with weaker settings). The session that wrote it had not read the engine and read nothing outside the packet until these results were saved.

## What agreed

**Everything, to the last digit, apart from rounding.** For each of the six runs (two runs in three environments) the new program reproduced the engine's figures seed by seed, for all 958 measures of the no-programme run and 990 of the programme run:

| Environment | Run | Measures | Exact in all 500 seeds | Exact in at least 499 seeds | Failing the 2-SE test |
|---|---|---|---|---|---|
| Reference | no programme | 958 | 948 | 950 | 0 |
| Reference | candidate main row | 990 | 687 | 968 | 0 |
| Adverse | no programme | 958 | 948 | 950 | 0 |
| Adverse | candidate main row | 990 | 677 | 714 | 0 |
| Stress | no programme | 958 | 948 | 950 | 0 |
| Stress | candidate main row | 990 | 694 | 706 | 0 |

Counted as single values (one measure in one seed), 99.6% to 99.96% of them agree to one part in a billion.

"Exact" means the two programs agree to within one part in a billion for that measure in every one of the 500 seeds. Every measure also passes the brief's statistical test: its 500-seed average agrees with the engine's within two standard errors. So does the programme's effect on every measure (the programme run minus the no-programme run, seed by seed). By chance alone one measure in twenty could fail that test; none did.

The headline figures, Reference, average of 500 seeds (engine / new program):

| Measure | No programme | Candidate main row | Effect |
|---|---|---|---|
| Adult-years below the cost of living (%) | 36.10 / 36.10 | 5.14 / 5.14 | −30.96 / −30.96 |
| Poverty severity (FGT2 × 100) | 9.464 / 9.464 | 0.2319 / 0.2319 | −9.232 / −9.232 |
| Adults with too little wealth at year 20 (%, weighted) | 24.26 / 24.26 | 2.375 / 2.375 | −21.89 / −21.89 |
| Adult-years below 30 days of basic living (%) | 19.62 / 19.62 | 0.502 / 0.502 | −19.11 / −19.11 |
| Median wealth at year 20 (today's $) | 231,269 / 231,269 | 316,315 / 316,315 | +85,046 / +85,046 |
| Programme inflation (a year) | 0 / 0 | 40.33% / 40.33% | |
| Price level at year 20 | 1 / 1 | 634.26 / 634.26 | |
| Programme cost per adult-year (today's $) | 0 / 0 | 60,426 / 60,426 | |
| PTF share of essential sales (mean, %) | | 43.15 / 43.15 | |

Agreement is to every digit shown; the two averages differ by less than one part in a million (the cost per adult, the price level and median wealth differ at all only through seed 246, below). These are the figures at the packet's backed share of 0, the low end of the backing curve; Duke's decision of November 14 makes the main row the full-backing reading, for which these figures are not the headline.

## What did not agree, and why

The measures that are not exact in every seed differ for two reasons, both about rounding in the last binary digit of a number. Neither is a difference in any rule.

1. **A year in which the income effect takes all of someone's earnings.** When the programme's unconditional dollars are as large as a worker's earnings, the model's labour response leaves that worker earning nothing. In exact arithmetic the figure is zero; on a computer it comes out a tiny amount above or below zero (about one ten-billionth of a dollar). Whether that year then counts as "worked" depends on which side of zero the rounding falls. So does the next year's EITC: the tiny earnings make the household eligible for the credit's phase-in, which changes its marginal rate and so its hours. The two programs round such figures differently, so in some seeds the share of adult-years with earnings differs by 0.01 points. The knock-on effect reached dollar figures in 1 seed of 500 in Reference (seed 246) and 3 in Adverse and Stress; the largest effect on the price level at year 20 was 1 part in 100,000, and basket poverty agrees exactly in every seed of every environment.
2. **Households at the borrowing limit.** In the no-programme run many households end the year at exactly minus the $2,500 borrowing limit; on a computer, some come out a hair above it and some a hair below. The distribution measures rank adults by wealth with weights (the top tail's weights differ by household type), so the order of these near-ties, and so which side of a fifth's edge an adult falls, depends on the last digit. In a few seeds some low percentiles of wealth and some fifth-to-fifth mobility shares differ; their 500-seed averages agree.

Both are small faults in how the engine counts and ranks, not in the model's behaviour, and both have a simple remedy: count earnings below a billionth of a dollar as zero, and rank wealth rounded to the cent. They are listed for the design freeze (in GAPS.md, items 22 and 24); nothing in the engine was changed.

## What the written description is missing

The description gave the shape of every mechanism and every random draw correctly. It did not give enough to reproduce the numbers exactly: almost every part needed some detail from the code, such as the order in which things happen, a tie rule, a default or a table. GAPS.md lists them (items 1-21; items 22-25 are what the check found in the engine). The most important:
- One sentence of the description is contradicted by the code. When adults have no ages, as here, the year-0 draw of who is outside the labour force uses survey shares by household type, not the "fitted stock" the text describes.
- The US-data reading of wages, which every run uses, is named but not described.
- Several tables the runs need (the balance sheets by wealth group, the top tail's cut-offs, today's government debt) are not in the packet's configuration file.

A fourth implementation written from the description alone would need these.

Both rounding effects start in the same place: the two languages' mathematical functions (powers, exponentials, logarithms) sometimes differ in the last of their 53 binary digits. Adverse's price index at year 12, 1.02¹², is an example: Python's value is the correctly rounded one and the engine's is one digit off. Such differences are invisible except where a rule compares two quantities that are equal in exact arithmetic.

## What it means

The second implementation (November 1) found eight places where the description and the code disagreed. This one found three, and only one matters (the year-0 labour-force draw, above). It also found that the code behind the round-2 results does exactly what a separately written program does: in every seed, for every measure the engine reports, in all three environments. For the round-2 parts (open access, running costs, labour-force flows, asset classes, the creditor side, the tail, the government account) it is the first such check. It does not say whether the model's assumptions are right; that is the outside economist's question. It says the published numbers are what the model, as described, produces, with no hidden step and no coding slip that changes a result.

## What was not reached

All six runs were done. Phase 2 (reading the engine to explain each remaining difference) is short here: both kinds of difference are explained by rounding, and the second implementation's own program (November 1) has not yet been compared with this one. Duke's decision of November 14 makes the design freeze's main row the full-backing reading (backed share 1); this packet is the backed share 0 (the curve's low end). Before the full study batch runs, the program is to be run on the full-backing row (the step's own rule), which needs a packet built on that row.

## Files

- `s69_main.py` (with `s69_*.py`): the program. `python3 -I s69_main.py --env ref --row main --seed 1 --cmp` runs one seed and compares it with the engine; `--seeds 1-500 --jobs 4 --out FILE` runs a batch.
- `s69_compare.py`: the comparison tables; `results/compare.md` and `results/compare-*.csv` (every measure, every environment).
- `GAPS.md`: what the description lacked, and what the check found in the engine.
- `results/run.txt`, `results/SHA256SUMS`: commands, versions and file hashes.

## Rerun on the frozen main row (Nov 14, 2026, S63 part 3)

Round 2's batch runs a slightly different main row from the one checked above. It has full backing (every programme dollar matched by new output, the design's statement; `o.a` 1), and it has S69's two reporting corrections switched on. The first correction counts earnings below 1e-9 dollars as zero (`fx.ez`, item 22 of GAPS.md). The second ranks the weighted distribution measures on wealth rounded to the cent (`fx.rk`, item 24). S69's own rule was that the program is run again on that row before the batch is dispatched.

- **The packet:** `dev/packets/s69-frozen-row.zip`, built from engine commit `104691f` with `make_s69_reference.js --frozen` (`harness.js` `r2FreezePair`). Seed 1's rows equal the round-2 dry run's main rows (compassionism-sim-results `r2dry-104691f`) on every key.
- **The program:** two changes, each read from the row's settings and inactive when the setting is off. `fx.ez` sets earnings under 1e-9 dollars to zero at the same point in the year as the engine. `fx.rk` makes the distribution measures rank on the value rounded to the cent, with ties broken by index. On the earlier packet the program gives the same results as before.
- **The result:** all six runs (no programme and the main row, Reference, Adverse and Stress, seeds 1-500) agree with the engine **exactly**. That is every key in every seed, 958 keys in each no-programme run and 990 in each main-row run, at a relative difference under 1e-9. No key fails the two-standard-error test, and no effect fails it either. On the candidate row, 10 keys of each no-programme run and 296 to 313 keys of each main-row run differed in some seeds. Every one of those differences came from the two rounding-decided cases that the corrections now settle. The Stress supply-path settings rule still holds (`s69_check_capture.py`).
- **Files:** `results-frozen/` (`compare.md`, `compare-*.csv`, the per-seed results, `run.txt`, `SHA256SUMS`); commands in `results-frozen/run.txt`.
