# Outside poverty-history data (Oct 14, 2026): read this before using any file here

**What this is.** Official and supplemental poverty rates for the United States, 2005 to 2025, with the economic series that go with them (unemployment, prices, income, housing, household wealth, SNAP, the 2009 and 2020-21 relief laws). It exists for one job: the rough shape check of the simulation against history (`dev/plans/s146-history-check.md`).

**What it is not.** It is not verified. Two outside AI assistants with web access gathered it from Census, BLS, BEA, the Federal Reserve, USDA and Columbia University pages. Each opened ten random values against the source and found them right. Nothing here has been checked against the sources by this repository, because the machine that builds the simulation cannot reach those sites (census.gov refuses automated requests). Treat every figure as "as reported by the pack", and say so wherever one is quoted.

## What is where
| File | What it holds |
|---|---|
| `history_series.json` | **Read this one.** About 22 KB: every series the check needs, built from the CSVs by `dev/tools/history_data.py build`, with the series breaks and the disputed cells listed. |
| `poverty_official.csv`, `poverty_spm.csv`, `poverty_spm_history.csv`, `thresholds.csv`, `macro_drivers.csv`, `snap.csv`, `policy_events.csv`, `scf_wealth.csv` | Pack A, the full set (about 330 KB; do not read them whole). Columns: series, year, group, value, unit, value_original, source_name, source_url, table_or_page, notes. |
| `SOURCES.md`, `GAPS_AND_DOUBTS.md` | Pack A's own list of sources and its own list of what it could not do. Read the second one. |
| `cross-check-pack/` | Pack B: a second, smaller, independent gathering of three of the same files (official rates, supplemental rates, thresholds). It has no economic, SNAP, relief-law or wealth files, and its Columbia file is empty. Used only to check pack A. |
| `CROSSCHECK.csv` | Every cell both packs report where they disagree (51 of 217), with the reason. Rebuilt by `dev/tools/history_data.py crosscheck`. |

## How the two packs compare
166 of the 217 cells reported by both packs agree to the last digit. The 51 that differ fall into five groups:
- **21 thresholds (definition).** Pack B's "two adults, two children" threshold is really the weighted-average four-person threshold (Census Historical Table 1), which is higher by $160 to $320. Pack A gives the actual two-adult, two-child cell. Pack A is right for this label.
- **14 first-published values.** In the survey-redesign years (2013, 2017) and the 2019 restatement, pack B gives the figure first published and pack A the forward-comparable or restated one (pack A keeps the first-published one in `value_original`). Not an error in either.
- **8 other rows of the same table.** For the supplemental measure in 2013 and 2017 pack B picked the other of the two rows Census prints (traditional questions; prior processing). Pack A names both in its notes.
- **1 rounding** (the 2025 renters' threshold).
- **7 disputed cells with no explanation:** the supplemental rate for 2014 (all people, under 18, 18-64: pack A 15.6, 17.1, 15.3; pack B 15.3, 16.7, 14.7), 2015 (under 18, 18-64: 16.2, 14.1 against 16.1, 13.8), 2018 (65 and over: 13.6 against 12.8) and 2020 (65 and over: 9.4 against 9.3). Only the 2020 cell lies in a window the check uses, and it differs by 0.1 point. They are listed under `disputed` in `history_series.json`. A third source opening Table 8 of Census report P60-290 would settle them.

## Choices made in building `history_series.json` (decision log: `dev/DECISIONS.md`, Session 8)
1. Pack A is the base; pack B only cross-checks. Reason: pack A covers every series asked for, uses the correct threshold cell, and documents its breaks.
2. Where a series has a break, `value` is the forward-comparable figure and the first-published one is kept beside it (`rate_first_published`). The 2013 and 2017 breaks lie outside the two periods the check uses (2007-2010 and 2020).
3. Every year is the income year (the year the money was earned), not the publication year. 2025 is the newest.

## Known gaps and doubts (the full list is in `GAPS_AND_DOUBTS.md`)
- **No market-income poverty series after 2012.** Columbia's "before taxes and transfers" rates run 2005-2012 only; Census gives one count (2023). The model's no-safety-net run can be compared with history only for the 2007-2010 recession.
- **No supplemental measure before 2009 from Census.** For 2005-2008 the file uses Columbia's historical series (a different method; its 2009-2012 values are within 0.01 to 0.06 point of Census's).
- **Program-effect counts are partial.** Counts of people lifted out of poverty exist for 2019-2025 only, with holes (the earned income tax credit alone is blank for 2019-2023; 2021 gives percentage points, not counts). They are marginal effects: never add them up.
- **Relief-law amounts (2020-21) come from agency pages**, not from payment data.
- **Corrected supplemental renters' thresholds for 2020-2023 are blank** (BLS blocks automated download); the first-published values are in `value_original`.
- **Economic series are the latest revisions**, not what was published at the time (`value_original` is empty throughout `macro_drivers.csv`). Only pack A has them; pack B never checked them.
- **Two equal consecutive values worth a glance:** real median household income is 69,070 in both 2011 and 2012.
- **2020:** the survey had pandemic non-response; Census research puts the official rate about 0.5 point higher with other weights. Compare 2020 with that in mind.

## Using it
`python3 dev/tools/history_data.py check` fails if `history_series.json` no longer matches the CSVs, or if a series has a hole. After editing any CSV, run `build` then `crosscheck`.
