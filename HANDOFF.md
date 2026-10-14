# Handoff (Oct 14, 2026, UTC): outside history data staged; history check ready to build; study launch next

## What shipped
- **Pull request 29 (draft; data and plan only, no engine, page or figure change):** `sources/history/` (two outside data packs, a read-first README, `CROSSCHECK.csv`, and `history_series.json`, 22 KB), `dev/tools/history_data.py` (build, check, crosscheck), `dev/plans/s146-history-check.md` (the plan, with seven comparisons and pass bands fixed before any run), and Session 8 entries in `dev/DECISIONS.md`. Ledger steps s156 and s168 done.
- **The two packs agree on 166 of 217 shared cells.** 44 of the 51 differences have a reason (a threshold label, a first-published value, the other row of a split table); 7 supplemental-rate cells are disputed. All the data are unverified against Census, BLS and the Federal Reserve (this machine cannot reach them).
- **Pull requests 27 and 28 are merged** (main head 0282579 before pull request 29).

## Branch and pull request state
- Branch `claude/history-data-s156`, draft pull request 29 into `main` (head = the newest commit on the branch). It touches no code the checks run, so CI is expected green (checks and guard run on every push). If it is still unmerged, branch from it; if merged, restart from `main`.

## Long jobs in flight
- None. The study (ledger s165) is not launched. The results token expires 2026-10-17 04:16 UTC.

## Next 3 actions
1. **Explain issue i24-1 (20 seeds):** why today's safety net slightly raises basket poverty (`dev/reports/v5-33-snap-work-rule.md`, section 5, names the likely cause: people working a little less as benefits phase out). Show it with hours and income traced in the safety-net arm (`dev/tools/sn_trace.js`). A bug would change the engine, so this comes before the launch. If it is behaviour, write two plain lines for the report; add a row to the study job only if it is cheap.
2. **Build the history check (ledger s146)** exactly as `dev/plans/s146-history-check.md` says. Commit the plan with any change, and its reason, before the first 500-seed run. Smoke test on 20 seeds locally. Fix the hook at the end of `dev/tools/s165_jobs.sh` (it looks for the tool inside the pinned engine worktree, where it cannot exist). Do not change the engine pin c88c1e0.
3. **Launch the study (s165) once, then stop:** runner = the commit that holds the history check (merged `main`, or the branch head); `STUDY=s165 MAX_HOURS=5`; before launch run `SEEDS=2 bash dev/tools/s165_jobs.sh ...` end to end and `--estimate` (it should now include the history check). After launch check once that `s165-c88c1e0/status.txt` and `run.txt` appear in BetterToBest/compassionism-sim-results; write the pod id here; end the session. Do not wait.

## Files to touch
- Action 1: `dev/tools/snap_rule_check.js`, `dev/tools/sn_trace.js` (trace tools); engine code in `index.html` only via a switch (grep `SNET.abawd`).
- Action 2: new `dev/tools/history_check.js`; `dev/tools/s165_jobs.sh` (grep `history check`); `dev/reports/v5-34-history-check.md` (new); data in `sources/history/history_series.json`.
- Action 3: `dev/batch/runpod.sh` (start command in its header), `dev/tools/s165_jobs.sh`.

## Pitfalls
- **Compare changes, not levels:** the start population is built from 2022 data. Say so first in the report.
- **No retuning to fit history** (guardrail 5), and no model or assistant names in any pushed file (the packs are "pack A" and "pack B").
- **Do not read the CSVs in `sources/history/` whole** (330 KB); read `history_series.json` and the README.
- **Claude Code cannot launch another pod after the Pro plan ends (Thursday):** anything that could change the engine or the job is settled before this launch.
- Wording passes need `no_figure_change.py` snapshots; `explore_export.js` without `--suite` or `--out` overwrites published data; `unit` and `domtest.js` take minutes: use the shell's background option. GitHub GraphQL is blocked (use the REST API).
