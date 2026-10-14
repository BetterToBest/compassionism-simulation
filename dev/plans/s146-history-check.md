# The history check (ledger step s146): a rough shape check of a 500-person model

Written Oct 14, 2026, before any run. Commit this file, with the comparisons in section 4 as written or changed with a stated reason, **before** the first 500-seed result exists. Changing a comparison after seeing results is not allowed; add a new one and say when it was added.

## 1. What it is, and what it is not
It runs the model through two real shocks, the 2008-2010 recession and 2020, and compares **how the simulated poverty rate moves** with how the official and supplemental poverty rates moved. It is a rough check of shape and direction. It is not a calibration: no constant is retuned to fit (guardrail 5), there is no target result, and a mismatch is reported as plainly as a match.

**The limit that shapes everything.** The model's starting population is built from 2022 data (SCF, CPS; 2025 dollars). So the check asks "how would a population like today's respond to a shock like 2008?", not "does the model reproduce 2007". **Compare changes from the year before the shock, never levels.** Say this in the report's first paragraph.

## 2. The data (in the repository already)
`sources/history/history_series.json` (22 KB: read this, not the CSVs) and `sources/history/README.md` (what is unverified and what is missing). Paths the check needs, in percent unless noted:

| | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2019 | 2020 | 2021 |
|---|---|---|---|---|---|---|---|---|---|
| Official rate, all | 12.5 | 13.2 | 14.3 | 15.1 | 15.0 | 15.0 | 10.5 | 11.5 | 11.6 |
| Official rate, under 18 | 18.0 | 19.0 | 20.7 | 22.0 | 21.9 | 21.8 | 14.4 | 16.0 | 15.3 |
| Supplemental rate (Columbia, history method) | 14.4 | 14.8 | 15.2 | 16.0 | 16.1 | 16.0 | | | |
| Supplemental rate, Census | | | 15.1 | 15.9 | 16.1 | 16.0 | 11.7 | 9.1 | 7.7 |
| Before taxes and transfers (Columbia) | 23.2 | 24.5 | 28.3 | 28.9 | 28.9 | 29.0 | | | |
| Unemployment rate (annual average) | 4.6 | 5.8 | 9.3 | 9.6 | 8.9 | 8.1 | 3.7 | 8.1 | 5.3 |
| Real GDP growth | 2.0 | 0.1 | -2.6 | 2.7 | 1.6 | 2.3 | 2.6 | -2.1 | 6.3 |
| Price inflation (CPI-U) | 2.8 | 3.8 | -0.4 | 1.6 | 3.2 | 2.1 | 1.8 | 1.2 | 4.7 |
| Real median household income ($2025) | 74,810 | 72,260 | 71,790 | 70,110 | 69,070 | 69,070 | 85,320 | 83,590 | 83,270 |

Two things the numbers already say: (a) in 2007-2012 the before-transfers rate rose 5.8 points while the supplemental rate rose 1.6, so taxes and transfers absorbed about three quarters of the shock; (b) in 2020 the official rate **rose** 1.0 point while the supplemental rate **fell** 2.6 (stimulus payments, the $600 weekly unemployment top-up). The engine has no stimulus payments or weekly top-up, so 2020 is a test of the shock alone unless section 5 adds them.

## 3. Mapping the model to the data (Claude Code decides; record it in `dev/DECISIONS.md`)
- **Model arms to data series.** The model run **without** today's safety net (no SNAP, EITC, CTC; unemployment insurance stays, as in the engine) ↔ Columbia's before-transfers rate (2005-2012 only). The model run **with** today's safety net (the `sn` rows) ↔ the supplemental rate; the official rate is the second comparator. Closest model measure to the supplemental rate: basket poverty (income against the cost-of-living basket). Report wealth poverty beside it but do not compare it with these series.
- **The scripted shock.** The engine draws its recessions at random (`buildRecessionPath(years, seed)` in index.html, an income multiplier of 0.70 + 0.25 x beta(5,2), 1 to 3 years). The check replaces that with one fixed path, the same for every seed and both arms. Candidate rules, to be **fixed in writing before any poverty output is looked at**: (a) the multiplier from the year-on-year change in real median household income; (b) the job-loss chance in recession years scaled from the unemployment path (4.6% to 9.6%), through the engine's own employment parameters (`CFG.EMPL_P_REC`, `CFG.EMPL_W_REC`); (c) both. Optional: scripted outside inflation from the CPI row. Whichever is chosen, no constant may be adjusted after seeing a poverty result.
- **Calendar.** Map engine year 0 to the last year before the shock (2007; 2019). Run 5 years after it so recovery is visible (to 2012; to 2024 optional).
- **Draws.** No new random draw (guardrail 4); the scripted path replaces the stream, it does not add to it. Seeds 1-500, paired with a no-shock control run of the same seed, so each effect is "shock minus no shock".

## 4. Comparisons fixed in advance (the verdict for each is one of: matches / same direction, different size / does not match)
Model figures are 500-seed means with the 5th to 95th percentile of the seed-to-seed spread. "Rise" is the change from the base year (2007 for the recession, 2019 for 2020).
1. **Direction, recession.** Basket poverty (with safety net) is higher in 2009 and 2010 than in 2007. Data: the official rate rises 1.8 points by 2009 and 2.6 by 2010.
2. **Size, recession.** The model's rise at its peak is between half and double the official rise (1.3 to 5.2 points, from 2.6 at the 2010 peak). "Same direction, different size" otherwise.
3. **Timing.** The model's peak falls within one year of 2010.
4. **Recovery.** Report, without a verdict, how much of the rise is gone two years after the peak (data: almost none; the official rate was still 15.0 in 2012).
5. **How much the safety net absorbs.** The rise without the safety net minus the rise with it, as a share of the rise without it (data: about 70-75%, Columbia, 2007 to 2012). Verdict band: within 20 percentage points of the data. Say which transfers the model has and which it lacks (Social Security, housing aid, the tax system).
6. **Direction, 2020, official-style measure.** Poverty is higher in 2020 than in 2019 in the model with the shock (data: +1.0 point).
7. **2020, supplemental measure.** Reported without a verdict unless section 5 is done: the data fell 2.6 points because of payments the engine does not have.

## 5. Optional, only if the budget is left: the 2020-21 payments
`policy_events.csv` has the amounts and dates (the $1,200 and $600 payments, the weekly $600 then $300 top-up, the 2021 Child Tax Credit). If Claude Code adds them as a scripted transfer, it must be a labelled switch, off by default and bit-identical when off, and comparison 7 then gets a verdict. If it is not done, say so in the report and leave it as an invitation to whoever forks the repository.

## 6. Build and run
- **Preferred: no engine change.** A driver, `dev/tools/history_check.js`, loads the engine's `harness.js` and supplies the scripted path through what it exports. If the path cannot be injected that way, add a switch (default off, `dev/tools/guard_test.js` and `snap_rule_check.js` identical with it off, `engine_lineage.js prove`) and nothing else.
- **Where it runs on the pod.** The study pod (`STUDY=s165`) runs the engine pinned at c88c1e0. **Do not change that pin**: its two-seed dry run passed. Run the history check from the **runner checkout** (the repository at the runner commit, `$W/sim`), not from the pinned worktree. That also covers a switch added to the engine.
- **Known bug in the existing hook.** The end of `dev/tools/s165_jobs.sh` tests for `dev/tools/history_check.js` and `sources/census_poverty_2007.json` after `cd`-ing into the engine worktree, where neither exists. Replace both paths with the runner's (`R=$(cd "$(dirname "$0")/../.." && pwd)`), point the driver at `$R/sources/history/history_series.json`, and pass the engine directory as an argument. The file `sources/census_poverty_2007.json` is not needed: its job is done by `history_series.json`.
- **Cost.** Two arms x shock and control x 500 seeds x 5 to 6 years is small beside the 37 core-hours of the study; estimate it from a 20-seed timing and add it to `--estimate`. Run the 20-seed smoke test locally (a few minutes) and the full 500 seeds on the pod, in a piece that is saved on its own (resumable, like the others).
- **Output.** `history-check.json` into the results folder, and a plain-words report `dev/reports/v5-34-history-check.md`: the comparison table with verdicts first, then the scripted-shock rule, then the limits. No page change tonight; the page may carry the result with the v5.6 release.

## 7. Limits to state in the report
The start-state is 2022-based (compare changes). The data are outside, unverified (`sources/history/README.md`). Seven supplemental cells are disputed between the packs; none lies in the windows except one 65-and-over cell in 2020 (0.1 point). The data have a 2013 and a 2017 series break, both outside the windows. Before-transfers history exists only to 2012. The engine's transfers are SNAP, EITC, CTC and unemployment insurance; Social Security, housing aid and taxes are not modelled as a response to the shock. The 2020 survey had pandemic non-response.

## 8. Choices fixed before any run (Oct 14, 2026, session 9; written and committed before the tool was first run, even on 2 seeds)
- **Arms.** The v5.4 no-programme run in the Reference Environment (the rows of `dev/tools/snap_rule_check.js`; history has no Compassionism), (i) without today's safety net and (ii) with it (`sn` with `SNET.slope` on, the corrected marginal rate the s165 study uses, issue i24-1). SNAP's work rule is off: it was suspended nationwide in 2009-2010 (ARRA) and 2020-2021 (FFCRA). Unemployment insurance is in both arms, as in the engine.
- **The scripted shock: rule (a).** In each year after the base year the income multiplier is that year's real median household income over the base year's (`macro.real_median_household_income`), capped at 1; the recession flag is on in every year it is below 1. With the flag on the engine's own recession job-loss rates apply (`CFG.EMPL_P_REC`, `CFG.EMPL_W_REC`), and its rule 'replace' reduces the income cut by the extra job loss, so the year's whole loss is the median income's fall. Why (a): it uses only the path the engine already reads, and the engine already splits a recession's loss between job loss and pay. Not (b): scaling the job-loss chance by the unemployment path needs a second switch and a mapping from the unemployment rate to the engine's yearly chance that would itself be a choice. Not (c): with (a)'s multiplier the job loss would be counted again beyond what 'replace' removes. No scripted inflation (the environment's own, 0 at Reference): the comparison is shock minus no shock, and both have the same prices outside the model.
- **Calendar.** Engine year 0 = 2007, years 1-5 = 2008-2012 (multipliers 0.966, 0.960, 0.937, 0.923, 0.923). Engine year 0 = 2019, years 1-2 = 2020-2021 (0.980, 0.976). 2022 is left out: its income fall came with 8% inflation, not a recession.
- **Measure.** The share of adults below the cost-of-living basket in each year (the engine's yearly path, `pf0_t`), shock minus no shock, seed by seed; reported as the 500-seed mean with the 5th to 95th percentile over seeds. Wealth poverty (`ppov_t`) is reported beside it, not compared.
- **Comparison 2's peak** is the year 2008-2012 with the largest mean rise. **Comparison 4:** if that peak is later than 2010, two years after it lies outside the window, and the report says so. **Comparison 5** uses 2012 (engine year 5) and Columbia's historical SPM rate, before and after transfers.
- **Comparison 6, amended (before any run).** The engine keeps no year-by-year record of its official-line measure, and adding one would change the list of outputs the guard tests check. So the official-style measure is basket poverty **without** the safety net: income before SNAP and tax credits, which the official measure also leaves out. Direction only, as written.
- **Engine.** One switch, `REC_SCRIPT` in `index.html` (null by default; read by the testbed run and by the price run that gives its supply path, so both see the same path, as they see the same random path today). No draw is added. With it null, `guard_test.js` and `snap_rule_check.js` must be identical; `engine_lineage.js prove` records it.
- **Runs.** A 2-seed run tests the code; a 20-seed smoke test runs locally; the 500 seeds run on the study pod as one resumable piece (`history-check.json`). The verdicts are computed by the tool from the bands in section 4; nothing is changed after a result is seen.
