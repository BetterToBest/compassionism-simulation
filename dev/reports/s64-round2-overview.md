# Round 2 of the Compassionism Simulation: what the frozen batch shows (S64)

Nov 15, 2026. A guide to the seven reports on round 2, one per preregistered question, and the statements the preregistered rules allow. Engine `104691f` (compassionism-simulation pull request 107), 500 adults (and a 10,000-adult main pair), seeds 1-500, Reference, Adverse and Stress, 20 and 40 years. About 186 runner-hours on GitHub Actions, free, run Nov 14-15 as frozen in research-update `prereg/2026-11-s63-round2-freeze.md` (Amendments 1 and 2 before the run; Amendment 3 after it records the checks and five points of reading, and changes no outcome or rule). Every result, including the unfavourable ones, is in compassionism-sim-results `r2-<part>-<env>-<years>-104691f/` and the tables in `dev/runs/s64-round2/`.

## The statements the rules allow

**Basket poverty (the cost of living).** Across the 62 preregistered readings, the C2.2 design lowers basket poverty by 26 to 33 points in Reference at 20 years; at the main row, 32.4 points (seed interval 32.2 to 32.5). The release design lowers it by 16 to 22 points; at the main row, 20.9 (20.8 to 21.1). Robust in every environment and at both horizons. (Question 2.)

**Basic living and wealth poverty.** Robust likewise: C2.2 lowers adult-years below 30 days of basic living by 16.5 to 19.7 points (main row 18.7) and wealth poverty by 15.7 to 19.7 points (main row 18.6); the release design by 10.7 to 13.0 (12.3) and 9.0 to 12.7 (10.9). Reference, 20 years. (Question 2.)

**Median real wealth.** Across the 62 readings, C2.2 raises median real wealth by $188,000 to $660,000 in Reference at 20 years; at the main row, $208,400 ($207,100 to $209,900); the release design by $85,000 to $282,000 (main row $99,400). These figures rest on today's price rule (ledger decision D26) and on full backing. Less than 3% of any wealth figure is the erosion of the balances adults held at the start, and it works in the programme's favour: slightly higher prices lower what net debtors owe (1.0% of C2.2's median-wealth effect, 1.0% of its wealth-poverty effect; S64 part 3). (Questions 1, 2, 6.)

**Inflation, with the backing statement beside it (rule 4).** At the main row, programme inflation is 0.0-0.2 points a year, no material change, at every reading. The main row assumes every dollar paid is matched by new output, as the design states (ledger decision D25; a design parameter). The model's own mechanism for new output matches 0.2-1.9% of it (14-20% with no ceiling); inflation stays under 5% a year only above about 86-90% backing (74-77% for the release design in Stress), and runs at 15-53 points a year at the mechanism's point. (Question 4.)

**Paid for by a contribution instead (never led with; D23).** C2.2 then needs a mean contribution of 63-77% of all money income and lowers basket poverty by at most 17.5 points (Stress, 20 years: +0.6, worse); the release design, at 46-71% of wages, raises basket poverty by up to 9.6 points. Debt stays under GDP at the main financed rows, but every financed result is fragile across its readings. Run without the weighted top tail. (Question 5.)

## The seven reports

| Question | Report | One line |
|---|---|---|
| 1 Main effects | `s64-round2-q1-main-effects.md` | All 60 primary tests exclude zero and survive Holm; 48 material, the 12 that are not are inflation. |
| 2 Robustness | `s64-round2-q2-robustness.md` | Every Source-row poverty and wealth curve robust (48 of 48); every financed curve fragile. |
| 3 Interactions | `s64-round2-q3-interactions.md` | 22 material interactions on the Source rows, all median wealth (how wealth is held, the spending share); none on poverty or inflation. |
| 4 Backing | `s64-round2-q4-backing.md` | Poverty effects barely depend on backing; inflation and median wealth do; the mechanism falls far short of break-even. Round 1's curve beside it. |
| 5 Financed rows | `s64-round2-q5-financed.md` | Contribution rates of 46-77%; much smaller poverty effects, some reversed; debt manageable at the main rows. |
| 6 Distribution | `s64-round2-q6-distribution.md` | Wealth and income more equal; families in debt fall; less movement out of the lowest wealth fifth; labour's share falls. |
| 7 Work | `s64-round2-q7-work.md` | Participation falls 1-5 points (programme leavers); hours agree at 500 and 10,000 adults. |

## Exploratory displays (no test)

- **Named readings** (`dev/runs/s64-round2/s64-named-fixed.md`): the readings earlier steps named, each against the main row. The largest shifts, all keeping the effects' sign: all wealth held as cash (`rt` off) makes C2.2's poverty effects 4.5-8.2 points larger in Adverse at 40 years; the liquid share at 4.6% makes C2.2's basic-living effect 7.7 points smaller there; `lf` off makes C2.2's basket-poverty effect 10 points smaller in Reference at 40 years; the capacity price rule, the quarterly price rule and S69's corrections off move nothing material.
- **Fixed PTF share rows** (same file): no material low-share optimum at both horizons; none is claimed (rule 7, with rule 3's materiality; Amendment 3 item 3).

## Unfavourable results, together

Programme inflation above no programme in every cell (immaterial at the main row; 15-53 points a year without backing). Lower participation and employment (programme leavers 1-5% of adult-years) and their earnings forgone. Less movement out of the lowest wealth fifth. Labour's share of income down 10-30 points. The release design's effects shrink by two thirds in Stress. Every financed row fragile; the release design paid by a contribution on wages raises basket poverty. At no backing and 40 years, the release design lowers median real wealth.

## What no figure here covers

Seed intervals measure the model's randomness only. They do not cover: the choice of main row (D26) and of full backing (D25, a design statement); the readings S70's screen held at main and the ranges it swept; Stress, which was not screened; 500 adults (the 10,000-adult pair covers hours and the tail); the engine's structure: one price rule for the economy, no central bank, no migration, no value of care, community work or new ventures, PTFs modelled from the Hub's statements and S62's costs, the creditor side's outside share left outside; the financed rows without the weighted tail. The model has not been reviewed by an independent economist.

## Added in S64 part 3 (Nov 15)

- **The erosion share of each wealth figure:** traced on the main row (`dev/tools/s64_erosion.js`, freeze file Amendment 4; the trace reproduced the batch in every seed). 0.0 to 2.9% of every wealth figure, in the programme's favour; S66's all-cash term, as a bound, has the opposite sign and stays within 5.3%. In question 1's report, with the fifths in question 6's.
- **Basket poverty by labour-force reason:** adults outside the labour force stay far more often below the basket under both designs (C2.2: 8.5 to 16.6% of their adult-years, against 1.8% in the labour force; the release design: 28.8 to 58.5%, against 9.5%; Reference, 20 years). In question 6's report.
- **The charts for the findings page:** `dev/runs/s64-round2/charts/` (`python3 dev/tools/s64_charts.py`): a specification-curve chart per headline outcome, design and horizon, with the financed rows beside, and the backing curve with the mechanism's point and the break-even share.
- **The findings-page text for S65:** `dev/reports/s64-findings-page-text.md`.
