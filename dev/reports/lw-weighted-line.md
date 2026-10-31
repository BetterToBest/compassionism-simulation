# The cost-of-living line, weighted by where people live (S14)

Oct 31, 2026 · S14 · Claude · engine switch `LW` (study row option `lw`), off by default · preregistration: research-update `prereg/2026-11-lw-weighted-line.md` (study L)

## Why this step

The model's cost of living for one adult is $49,370 a year (`CFG.LIVING_WAGE_ANNUAL`). It is the plain average of MIT's living wage for one adult with no children across the 50 states and DC (MIT Living Wage Calculator, February 2026 data, × 2,080 hours). A plain average counts Wyoming the same as California. Weighting each state by its population gives a national figure for where people actually live, and that figure is higher because the most populous states cost more. The model's wages come from a national survey of all workers (CPS), which already reflects where people live. So a weighted line is the consistent comparison for those wages.

An earlier decision (dev/DECISIONS.md, the cost-of-living line, "fix later") kept $49,370 until two things were done: re-derive the weighted figure from MIT's data, and check that every dollar the engine computes from the line follows it. This report does both, as far as MIT's terms allow, and sets up the run beside the current line.

## 1. Can the weighted figure be re-derived from MIT's data?

**Not without a licence.** MIT's FAQ (opened Oct 31, 2026): "If you plan on using 10 or fewer locations worth of data, you may use it directly off the web ... If you want to use data for more than 10 locations at once, please do not scrape, extract, or export the data ... Instead, please submit a request to license the data." Every state page also says "Please do not scrape the data." A population-weighted national mean needs all 51 figures. The model already uses eight state pages (`sources/mit_household_types.json`), within the ten-location limit. Pulling the other 43 would break the terms, so this step does not. Whether to ask MIT for a licence is for Duke to decide: it is a request to an outside body, and a licence may cost money (ledger decision).

**What is known about the current line.** $49,370 matches an unweighted mean of $23.7355 an hour (51 states, February 2026 data) from a third-party table that MIT's figures feed. Five of those state figures were checked against MIT's own pages in v4.11, and the eight state pages in the repository agree with MIT's February 15, 2026 build. Label: derived calculation (unweighted mean), 2025 dollars.

### Two estimates of the weighted line, with no new MIT data

| Line | Dollars a year | Over the current line | Basis |
|---|---|---|---|
| base (current) | $49,370 | | MIT, unweighted mean of the 51 state figures |
| ext | $51,201 | +3.7% | Population-weighted mean of the 51 MIT figures ($24.6160 an hour), computed outside the project in v4.11 (an AI review, Census Vintage 2025 weights). Five states and the population total were checked; the mean itself was not re-derived. |
| bea | $51,838 | +5.0% | This step's own estimate (`sources/lw_bea.py`), described below. Leaving out one state at a time gives $51,708 to $51,995. |

**How the bea estimate works.** The eight MIT state pages already held give each state's one-adult budget before tax. Across those eight states, the budget tracks BEA's Regional Price Parity (the federal government's index of each state's price level, all items, 2024) closely: a straight line fits with R² = 0.964. Applying that line to all 51 states' price parities gives a predicted budget for every state. The ratio of the population-weighted mean of those predictions (Census Vintage 2025 populations) to their plain mean is 1.0500. The current line × 1.0500 = $51,838. Only the ratio is used, not the predicted level, so the eight states' own bias largely cancels. Both sources are US federal data in the public domain. Using other BEA series instead of all items gives ratios from 1.019 (utilities, R² 0.79) to 1.048 (housing, R² 0.88). All items fits best.

**Reading.** The two estimates agree that weighting raises the line by about 4 to 5%, which is $1,800 to $2,500 a year. They differ by about $640, and neither is MIT's own weighted mean. The study runs both beside the current line. The model does not adopt either one (see 4).

## 2. What else is fitted at the line

Three sets of constants were fitted at $49,370 from the eight MIT state pages: each budget item's dollars regressed on the state's total, then read off at the model's line (`sources/households.py`). At a different line they change, so the switch refits all three by the same method (`sources/lw_line.py`; at $49,369.82 it reproduces the engine's values exactly).

| Fitted at the line | base | ext | bea |
|---|---|---|---|
| Housing share (with utilities) | 27.61% | 28.81% | 29.20% |
| Food share | 9.01% | 8.84% | 8.78% |
| Medical share | 6.85% | 6.53% | 6.43% |
| C2.2 needs (food, housing, medical), share | 43.47% | 44.18% | 44.41% |
| One adult's housing, food, medical, $ a year | 13,631 · 4,448 · 3,382 | 14,751 · 4,526 · 3,343 | 15,137 · 4,551 · 3,333 |
| BU at the C2.2 needs level, $ a month | 1,788.43 | 1,885.06 | 1,918.43 |
| Childcare, first child, $ a year | 12,914 | 13,342 | 13,490 |
| One parent, one child: total budget, $ a year | 74,688 | 77,671 | 78,713 |
| Couple, two children: total budget, $ a year | 97,340 | 100,852 | 102,078 |

So a higher line is mostly higher housing: places with more people have dearer rent, while food and medical care cost about the same everywhere in MIT's data.

## 3. Every dollar path that uses the line

Every place in `index.html` and `harness.js` that reads `CFG.LIVING_WAGE_ANNUAL`, `CFG.BASKET`, `CFG.HH_RATIO` or `CFG.HH_CHILDCARE`, and every dollar constant in `CFG`, was read. Each one falls into one of three groups.

**A. Follows the line automatically: the dollars are computed from it when the run happens.**
- The wealth update: each year's cost of living, × inflation, × the price module's index, × the household's own factor (the main loop's cost, `gCost`, `spMlc`, `mainLoopCostUSD`).
- Every household's budget (`hhNeed`: the line × share × household ratio, plus childcare), and with it the household's factor `_hhF`, its essentials share and its daily cost for the BLEI measure.
- The price module's weights and the cost of the essentials BU can buy (the shares, read each year).
- The cost-of-joining test (`jnM`), the share of income spent, and the CCO and PTH price cuts (shares of the budget).
- SNAP's shelter cost (the household's housing need) and the health module's medical line (`hlLine`).
- The traditional-welfare comparison (`idx`) and every reporting line scaled by the price level (`lf`: the year's budget over the line, a ratio).
- The C2.2 needs level `c22NeedsBU()` and its yearly index (`c22Share`).
- The poverty gap in dollars used for public costs avoided (`avoidWide`: the gap × the line).
- The "below the cost of living" and "basket" counts (income against the line).

**B. Fitted at the line, so it does not follow unless refitted.** The basket shares, household ratios and childcare (section 2), and project pay (`PROJ_DEFAULTS.pay`, the line over 2,080 hours, computed once when the page loads). The switch refits all four.

**C. Does not follow, and should not.** These come from their own sources, which already describe the whole country:
- Wages (CPS, `WAGE_TO_USD`, `CFG.CPS_EARN`), starting wealth (Survey of Consumer Finances), Social Security, taxes, SNAP, the EITC and the Child Tax Credit (federal schedules), health costs (CMS, Medicare, the employer and marketplace surveys), disaster aid (FEMA), and the official poverty lines (`CFG.POVERTY_THRESHOLD_ONE`, `CFG.HH_FPL`). They are federal schedules or national survey figures, and a different cost line does not change them.
- The BU at $1,200 a month: a design value, which stays $1,200 at any line. Only the C2.2 needs level follows the line.
- The BLEI paper's daily cost ($68.33, `BASE_DAILY_COST`) and the member daily cost ($31.67): the BLEI paper's own figures, a separate concept from the MIT budget. The household's BLEI daily cost multiplier is a ratio of fitted items, so it follows the line in part.
- One reporting threshold, flagged: the adult-only "too little wealth" line of $25,000 (`POVERTY_LINE`). From v5.3 it is read as six months of one adult's cost of living (half the line is $24,685), but it is kept at $25,000 so figures stay comparable across releases. At the weighted lines, half the line is $25,601 (ext) or $25,919 (bea). The household reading (`CFG.HH_WEALTH_MONTHS`: six months of each household's own costs; `hhWlthPY`, `hhWlthEnd`) follows the line. The study programme's primary wealth outcome `pov` is the fixed $25,000 reading, so study L reports both: `pov` does not move with the line by construction, and `hhWlthPY` does.

No path was found that should follow the line and does not, apart from group B, which the switch handles. No dollar figure elsewhere in the engine was calibrated to $49,370.

## 4. What the switch does

`lw: 'ext'` or `lw: 'bea'` on a study row sets, for that row only, the line and the three refitted sets from `CFG.LW_SETS` (printed by `sources/lw_line.py`), and project pay. It writes them into the existing objects, so every reference sees them, and puts the values back after the row. The no-programme reference path (the price module's supply path) is keyed by the line, so a weighted row never reuses the current line's path. No random draw is added. Off (no `lw` option) changes nothing. Checks: unit test (`v54UnitSuite`, S14): a row at another line moves that row only. Rows run after it equal rows run alone, all four sets come back exactly, and the needs level follows the line. Also the guard test, the 12-seed release panels (engine lineage) and `runner/jobs/lw.js --check`.

The released line stays $49,370. Changing it would be a calibration change for S47 (design freeze) to consider. It needs the study's results, and ideally MIT's own weighted figure.

## 5. The study

Study L (preregistration: research-update `prereg/2026-11-lw-weighted-line.md`). There are three lines (base, ext, bea), each with three rows: no programme, the release row, and the C2.2 design (automatic, all residents, BU at the needs level of that line, indexed to the needs). It runs in all three environments at 20 and 40 years, with 500 adults and the CPS yardstick. Pilot: seeds 1-100 on GitHub Actions. Full: seeds 1-500 in the S48 batch. The questions: how much does the no-programme world's poverty change with the line, and does the programme's effect against no programme depend on the line? Results: pending (section 6, added when the pilot lands).

## 6. Results

Pending: the pilot `pilot-l-<engine>` in BetterToBest/compassionism-sim-results.

## Limits

- Neither weighted figure is MIT's own. ext was computed outside the project and was only partly checked. bea assumes MIT's budget varies across states the way BEA's price level does.
- The shares are fitted on eight states. At a line further from the middle of those eight, the fit relies more on the straight-line assumption: the eight totals run from $40,627 to $64,504, so $51,838 is well inside.
- One national line for everyone. The model has no regions, so a weighted line is still one figure for the whole country.
- MIT's data are 2026 prices (the engine reads them as 2025 dollars, as before). BEA's price parities are for 2024, and Census populations for July 2025. The ratio barely moves from year to year, but the dates differ.
