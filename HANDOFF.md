# Handoff (Oct 16, 2026, night): maturing-effect note, Health Study chart fix

## What shipped
- `study.html`: the "What the results depend on" chart now sits in the same white card as the charts on the other pages (its row labels have a white outline that showed against the grey page, so they looked unstyled).
- `dev/tools/study_data.py` (regenerated `data/studies/s137.json`): clearer opening sentence; Basic Unit (BU) and BLEI spelled out where first used; a note that the study covers 20 years and that the compare page's 40-year runs suggest the "too little wealth" rise may be an early stage of a maturing effect.
- `compare.html`: a key point and a note (labelled Claude's reading of the results) that the wealth effect takes time to show: the wealth-poverty gap narrows between year 20 and year 40 in all 11 Source-pays Compassionism rows, and in Reference and Adverse under the wage contribution, not in the Stress Test. The cost-of-living advantage is slightly smaller at 40 years; the page says so.
- Correction, `compare.html` Part 2: the Health Study's safety net has no SNAP work rule and no slope fix (Part 1's has both). That explains 49.3% against 55.2% for no program; the page now says so.
- Checks: `check_figures` (22), `check_versions`, `study_data.py --check` pass; `domtest` was running at the end, CI runs it.

## Branch and pull request state
- Branch `claude/compare-page-40-year-6528wq`, restarted from main after pull request 45 merged. Draft pull request into main, see below.

## Long jobs in flight
- None.

## Next 3 actions
1. Read CI on the draft pull request; fix if red (merge main in, never rebase). Duke merges when it reads right.
2. If Duke wants it: a 40-year Health Study, and a 40-year Part 2 with today's safety net including the work rule, on Runpod. That would test the maturing reading directly. Part 3 (earlier engine) has 20 years only.
3. The maturing claim is checked only inside the current engine (three environments, two financing rules).

## Files to touch
- `dev/tools/study_data.py` (text keys `intro`, `sens`, `cap.other`), then `python3 dev/tools/study_data.py`; `compare.html` (Part 1 tables between the PART1-TABLES markers: regenerate with `dev/tools/compare_tables.py`).

## Pitfalls
- Results are in BetterToBest/compassionism-sim-results, folder s171-cfc3322.
- `compare.html` is not covered by `domtest`; check by eye over `python3 -m http.server`.
- Don't `pkill -f` a pattern that also appears in your own command line (it killed the shell this session).
- Ledger not written (no tool this session).
