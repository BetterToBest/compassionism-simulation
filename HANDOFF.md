# Handoff (Oct 16, 2026, night): compare page now shows 40-year figures

## What shipped
- `compare.html` Part 1: a "Years simulated: 20 years / 40 years" switch (same button style as the other pages). All 12 tables (3 environments x 2 lengths, for each of the 2 financing rules) are in the page; the switch hides the length not chosen. Without JavaScript both lengths show.
- Part 1 tables are now generated from the s171 result files by `dev/tools/compare_tables.py` (run with the results folder; `--check` reports a mismatch). The 20-year tables it builds equal the old hand-written ones cell for cell (61 rows checked).
- Text: new 40-year key point; the wage-contribution paragraph now says the Stress Test result differs by length (20 years both small; 40 years Compassionism level, UBI and negative income tax raise severity); wealth poverty is read at the end of the run; note that equal cost is set per length and rule and that the dollar amount in a name can differ from the measured cost; Parts 2 and 3 say they are 20 years only; Part 3's note wrongly said "Part 3 adds it" (safety net), now "Part 2".
- Checks: `check_versions`, `check_figures` (22 passed) pass; page checked in a browser (switch works, no errors); `domtest` started, see CI.

## Branch and pull request state
- Branch `claude/compare-page-40-year-6528wq` from main (596d2f7). Draft pull request into main, see below. Guard test not run (page text and a page script only).

## Long jobs in flight
- None.

## Next 3 actions
1. Read CI on the draft pull request; fix if red (merge main in, never rebase). Duke merges when it reads right.
2. Part 2 (today's safety net) and Part 3 (earlier engine) have no 40-year version. A 40-year Part 2 needs a new Runpod run of the Health Study (`dev/tools/health_check.js`, see `data/studies/s137.json` meta for the command); ask Duke if wanted.
3. Open question: Part 1's no-program Reference figure below the cost of living is 55.2% but Part 2's is 49.3%, both described as "today's safety net alone". The page now says the parts are separate studies; find the reason (SNAP work rule, test settings) and state it.

## Files to touch
- `compare.html` (Part 1 tables sit between the PART1-TABLES markers: regenerate, do not hand-edit), `dev/tools/compare_tables.py`.

## Pitfalls
- Results are in BetterToBest/compassionism-sim-results, folder s171-cfc3322 (public; `git clone --depth 1`).
- `compare.html` is not covered by `domtest`; check by eye over `python3 -m http.server`, not from a file.
- Ledger not written (no tool this session): nothing changed in ledger steps.
