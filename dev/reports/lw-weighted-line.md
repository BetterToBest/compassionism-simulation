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
| ext | $51,201 | +3.7% | Population-weighted mean of the 51 MIT figures ($24.6160 an hour), first reported by an outside AI review in v4.11 (Census Vintage 2025 weights). **Re-derived Oct 31** (`sources/lw_check_ext.py`, below): $51,201.27, one cent from the figure used. |
| bea | $51,838 | +5.0% | This step's own estimate (`sources/lw_bea.py`), described below. Leaving out one state at a time gives $51,708 to $51,995. |

**How the bea estimate works.** The eight MIT state pages already held give each state's one-adult budget before tax. Across those eight states, the budget tracks BEA's Regional Price Parity (the federal government's index of each state's price level, all items, 2024) closely: a straight line fits with R² = 0.964. Applying that line to all 51 states' price parities gives a predicted budget for every state. The ratio of the population-weighted mean of those predictions (Census Vintage 2025 populations) to their plain mean is 1.0500. The current line × 1.0500 = $51,838. Only the ratio is used, not the predicted level, so the eight states' own bias largely cancels. Both sources are US federal data in the public domain. Using other BEA series instead of all items gives ratios from 1.019 (utilities, R² 0.79) to 1.048 (housing, R² 0.88). All items fits best.

**Reading.** The two estimates agree that weighting raises the line by about 4 to 5%, which is $1,800 to $2,500 a year. They differ by about $640. The study runs both beside the current line. The model does not adopt either one (see 4).

### ext re-derived from MIT's 51 figures (Oct 31)

After the study ran, the outside review's source was found: a Money Talks News article ("How much is really a living wage in every state") that republishes MIT's "Required annual income before taxes" for one adult with no children, for the 50 states. Duke copied the table from the page (the site refuses automated access). DC is not in it; its figure is MIT's $26.72 an hour, read directly from MIT's site in v4.11. `sources/lw_check_ext.py` runs the check. The 51 figures are not committed, because of MIT's ten-location limit. The input file is identified by its SHA-256.

- The eight states held in `sources/mit_household_types.json` equal the article's figures exactly, to the dollar (Alabama, California, Connecticut, Hawaii, Idaho, Indiana, Maine, West Virginia).
- Plain mean of the 51 hourly living wages (annual ÷ 2,080, to the cent): $23.7357, which is $49,370.23 a year. The line is $49,369.82, $0.41 away; the third-party table the line came from must differ by a cent or two in one place.
- Population-weighted mean (Census Vintage 2025, total 341,784,857, the same total the review used): $24.6160, which is **$51,201.27 a year**. ext is $51,201.28. Moving DC's figure by 5 cents either way moves this by under $0.25.
- So ext is the population-weighted mean of MIT's own February 2026 figures. The weighting ratio is 1.0371. bea's ratio (1.0500) overstates it by 1.2%: BEA's price levels spread wider across states, weighted by population, than MIT's budgets do.


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

Study L (preregistration: research-update `prereg/2026-11-lw-weighted-line.md`). There are three lines (base, ext, bea), each with three rows: no programme, the release row, and the C2.2 design (automatic, all residents, BU at the needs level of that line, indexed to the needs). It runs in all three environments at 20 and 40 years, with 500 adults and the CPS yardstick. Pilot: seeds 1-100 on GitHub Actions. Full: seeds 1-500 in the S48 batch. The questions: how much does the no-programme world's poverty change with the line, and does the programme's effect against no programme depend on the line? Pilot results: section 6.

## 6. Results (pilot, 100 seeds)

**These are pilot figures** (seeds 1-100). The full study reruns every row at 500 seeds in the S48 batch, and the report will say if any label below changes. Source: compassionism-sim-results `pilot-l-f66dc67` (engine `f66dc67`, all 10 shards checked, SHA256SUMS verified), analysed by `dev/tools/lw_pilot.py`. Every cell (three environments, 20 and 40 years) with 95% intervals is in `dev/runs/lw-pilot/tables.md` and `estimates.csv`. "Headline" means Reference, 20 years, CPS earnings, octave raise off. Intervals are 95% paired bootstrap intervals over seeds; every one quoted here excludes zero unless it says otherwise.

### What the higher line does to the world with no programme (Q14a)

A higher line puts more people below it, by about as much as the line rises. In the headline cell, at ext (+3.7%) and bea (+5.0%):

| Measure (no programme) | At $49,370 | Change at ext | Change at bea |
|---|---|---|---|
| Below 30 days of basic living (% adult-years) | 17.6 | +0.9 (0.8 to 1.0) | +1.2 (1.1 to 1.3) |
| Below the cost of living (% adult-years) | 27.2 | +1.7 (1.6 to 1.7) | +2.3 (2.2 to 2.3) |
| Too little wealth at the end, $25,000 line (% adults) | 20.3 | +1.2 (1.1 to 1.3) | +1.6 (1.4 to 1.7) |
| Too little wealth, household reading (% adult-years) | 23.8 | +1.2 (1.1 to 1.3) | +1.6 (1.5 to 1.7) |
| Children below the cost of living (% child-years) | 44.0 | +2.4 (2.3 to 2.5) | +3.2 (3.1 to 3.4) |

The $25,000 wealth line does not follow the cost-of-living line, yet it moves too. The likely channel (not tested separately) is that households' spending follows the basket's cost, so at a higher line they save less. The official poverty line (fixed in dollars) barely moves (-0.1 points). The other environments show the same pattern and sizes (tables).

### Does the programme's effect depend on the line? (Q14b, decision rule 1)

The test is the difference in differences: the programme's effect against no programme at the higher line, minus its effect at $49,370. Rule 1 labels it *not changed by the line* when its interval lies inside ±1 point.

**The release row ($1,200, opt-in): not changed by the line, in the headline cell.** On all four primary share outcomes, at both ext and bea, the interval lies inside ±1 point:

| Release row, headline cell | Effect at $49,370 | ext | bea | Difference in differences (bea) | Label |
|---|---|---|---|---|---|
| Basic living, design-neutral (points fewer below) | 10.6 | 10.6 | 10.6 | -0.1 (-0.2 to 0.0, includes zero) | not changed |
| Basic living, the design's reading | 11.4 | 11.7 | 11.8 | +0.4 (0.3 to 0.4) | not changed |
| Cost of living | 17.1 | 17.4 | 17.5 | +0.3 (0.3 to 0.4) | not changed |
| Wealth at the end ($25,000) | 3.8 | 3.3 | 3.2 | -0.6 (-0.8 to -0.4) | not changed |

So, under rule 2, **the release row's headline findings are robust to the line.** Stated with the range across the three lines: it cuts the share of adult-years below 30 days of basic living by 10.6 points at every line, the share below the cost of living by 17.1-17.5 points, and the share of adults with too little wealth by 3.2-3.8 points.

Outside the headline cell, the release row's effect is *changed by the line* in five comparisons, all in the Adverse environment and all smaller at the higher line: wealth at 20 years (-1.2 points at ext, -1.5 at bea), basic living at 40 years (-1.1, -1.4), and the cost of living at 40 years at bea (-1.0). Everywhere else (Reference and Stress Test, both horizons; Adverse on the other outcomes) it is not changed by the line. On the household wealth reading, which follows the line, the release row's effect is about 1 point smaller at the higher lines in the headline cell (bea: -0.9, small change; at the end of the run: -1.0, changed).

**The C2.2 design: changed by the line, mostly by construction.** The C2.2 design sets the BU at the needs level of whichever line is used, so at a higher line it pays more ($1,885 or $1,918 a month instead of $1,788) and still keeps almost everyone above the line (basic living 0.0-0.2%, cost of living 1.8% at every line, headline). Its effect therefore grows by about as much as the no-programme share rises: in the headline cell +1.1 and +1.4 points on basic living, +1.7 and +2.2 on the cost of living, +1.4 and +1.8 on wealth at the end (all *changed*, except the design's own basic-living reading at ext, +0.9, *small change*). These are not a finding about the design's strength; they say the design closes whatever gap the line defines. In the Adverse and Stress Test environments, the wealth effect grows by more than the gap (for example Adverse, 40 years, bea: +7.5 points against a rise of 2.3 in the no-programme share), because a higher BU also lets households save more. Under rule 2, the C2.2 design's headline figures are **not** robust to the line, so every one is stated with its range: it cuts the share below 30 days of basic living by 17.3-18.7 points, below the cost of living by 25.4-27.6 points, and with too little wealth by 19.8-21.6 points (base to bea).

### Cost and inflation (Q14c)

| Headline cell | Cost per adult-year at $49,370 | Cost at ext, % of base | at bea | Inflation effect at ext, % of base | at bea |
|---|---|---|---|---|---|
| Release row | $32,583 | 99.7% | 99.7% | 105.9% | 107.9% |
| C2.2 design | $61,278 | 105.9% | 107.9% | 109.1% | 112.4% |

- The release row's BU is $1,200 at every line, so its cost hardly moves (99.4-100.4% of the base cost in every cell). Its inflation is 6-8% higher at 20 years in Reference (14-19% at 40 years, up to 26% in Adverse at 40 years), because project pay follows the line. In the Stress Test it barely moves (+1%).
- The C2.2 design's cost rises 5.5-6.0% at ext and 7.4-8.1% at bea, in step with its BU (the needs level rises 5.4% and 7.3%). Its inflation rises more: 9-18% at 20 years, 12-37% at 40 years (the most in the Stress Test at 40 years, bea).
- Rule 1 labels every inflation comparison *changed by the line*. That label carries little information: cumulative inflation compounds and runs to tens of thousands of points (the release row's prices are about 195 times their start after 20 years in Reference), so a ±1-point band is far narrower than any seed-to-seed spread. The percentages above are the readable scale. The pilot studies report (section 9) already proposed reading inflation on its yearly rate; that is for S47 to settle for every study.

### The released line (decision rule 3)

ext and bea differ by 1.2% ($51,201 and $51,838), more than the 1% the rule allows. Rule 3's other route is a weighted figure that is MIT's own, from licensed data. Since Oct 31, ext is known to be the weighted mean of MIT's own figures (section 1), but they come from a published third-party table, not a licence. The current line, $49,370, comes from the same kind of table. The rule leaves the choice to S47 (design freeze), so this study adopts nothing: the release keeps $49,370 for now, and study L's rows are published beside it.

**Claude's recommendation to S47:** adopt ext ($51,201) as the line, with the $49,370 rows kept beside it. It uses MIT's data the same way the current line does, as one national mean of the 51 state figures, so it needs a licence no more than the current line does. It is the consistent comparison for wages drawn from a national survey. And the release row's findings do not change between the two lines in the headline cell (above). If S47 adopts it, the fitted sets are those `sources/lw_line.py` prints for ext, and the release keeps the base rows as a sensitivity.

**Where the 51 state figures are (Oct 31).** Duke's answer to decision D9 was to look in the project's own repositories first. They were searched on Oct 31: the Simulation (every file and its whole history), NEEC (every file, and file names across its history) and the Research Hub. None holds the 51 state figures. Each holds only the two summary means from the outside review in v4.11: $23.7355 an hour unweighted (the current line) and $24.6160 weighted (ext). The 51 figures were in that review's reply and were never committed. Duke then found the review's source page (decision D10), and ext was re-derived from it (section 1).

### What this means

- The release row's findings do not depend on which of the three lines is used, in the headline cell and in 2 of the 3 environments. In the Adverse environment its wealth effect (20 years) and its basic-living effect (40 years) are 1-1.5 points smaller at a higher line.
- The C2.2 design's measured effect is larger at a higher line, by about the gap the higher line opens, and it costs about as much more as the line rises. Its findings are stated with their range across the lines.
- At a higher line the no-programme world is worse off by 1-3 points on every poverty measure. Any figure quoted as "people below the cost of living" depends on the line by about that much.


## Limits

- ext is MIT's own weighted mean (re-derived Oct 31 from a third-party copy of MIT's table, checked against the eight MIT pages held), but not from licensed data. bea assumes MIT's budget varies across states the way BEA's price level does, and overstates the weighting by 1.2%.
- The shares are fitted on eight states. At a line further from the middle of those eight, the fit relies more on the straight-line assumption: the eight totals run from $40,627 to $64,504, so $51,838 is well inside.
- One national line for everyone. The model has no regions, so a weighted line is still one figure for the whole country.
- MIT's data are 2026 prices (the engine reads them as 2025 dollars, as before). BEA's price parities are for 2024, and Census populations for July 2025. The ratio barely moves from year to year, but the dates differ.
