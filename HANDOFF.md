# Handoff (Oct 14, 2026, 12:45 UTC): the measures study and the visual suite's second pass

## What shipped
- **The measures study's export (reporting only):** `dev/tools/explore_export.js --study` with `dev/tools/study_fields.js`. It gives EPPM against each adult's no-program twin, the monthly surplus for everyone in both runs, Acre Equity and the simulated CSI reading, the wealth Gini net of drain, movement between tiers, and breakdowns. The engine is unchanged; with the new switches on, all 4,696 results of a three-seed comparison were identical.
- **Runpod job** `STUDY=study12` (`dev/tools/study12_jobs.sh`; `dev/batch/runpod.sh`). All six pieces finished at 12:29 UTC (DONE) and are ingested (`dev/runs/explore-study-ENV-YRS.json`, `data/releases/v5.6/study-20.json` and `study-40.json`); every 500-seed self-check passed.
- **Suite page, second pass** (`suite.html`): one card per BLEI-paper measure with a status badge; IPBI shows the public costs avoided; the plan's corrections; a new "Who gains, and how people move" section. Every view fills in from the study.
- **Checks:** domtest 142 (Phase 15 gains three), check_figures (20 passed), validate, unit 222, glossary, and `no_figure_change.py` (10 moved counts, each allowed). The two-seed test fixture is at `dev/tools/fixtures/study-fixture-20.json`.
- **Written up:** report `dev/reports/v5-36-measures-study.md` (with the 20- and 40-year results); `dev/DECISIONS.md` Session 12; plans in `dev/plans/` (suite-v2, next-study, audit prompt, `tier-b-packets.md`).

## Branch and pull request state
- Branch `claude/fervent-hypatia-ypn11h`, draft https://github.com/BetterToBest/compassionism-simulation/pull/34 into main (subscribed; CI not yet reported at writing). Version unchanged (5.6.0): Duke assigns versions.

## Long jobs in flight
- None. Pod `hsa5yxhf0lwj4s` finished at 12:29 UTC and deleted itself (Runpod list-pods at 12:45 UTC: no pods). Results: BetterToBest/compassionism-sim-results, `study12-65abdc6/` (DONE).

## Next 3 actions
1. **Pull request 34:** fix any red CI or conflict (merge main in, never rebase). Duke reads `dev/reports/v5-36-measures-study.md` and merges.
2. **Part B, only after Duke approves the page:** a separate pull request that links `suite.html` from `findings.html`, drops `noindex`, adds a canonical link, and changes domtest Phase 15's "stands alone" check (`dev/plans/suite-v2-plan.md`, section 8).

3. **Then the deferred work:** the CoMSES package and fact sheet (ledger step s119), or a Tier B packet from `dev/plans/tier-b-packets.md` (B2 first: reporting only, needs sources).

## Files to touch
- `dev/tools/release_data.py` (grep `study = {`), `suite.html` (grep `function indices`, `function moves`), `domtest.js` (grep `session 12`), `dev/tools/check_figures.js` (grep `session 12`), `dev/tools/no_figure_change_allow.txt` (end of file).

## Pitfalls
- In the main reading the program's prices rise about 50% a year (the release's `infl` is a yearly compound rate, checked). EPPM's parts are therefore split in real terms; a split with a separate price-level part gave two huge parts that cancelled.
- Without ageing, adults have no `_id`: twins are matched by position (`study_fields.js`). A shared id silently paired everyone once; the export now fails on duplicate ids.
- The 500-seed 40-year export uses about 2.2 GB, so the job gives Node a 6 GB heap.
- The results token expires 2026-10-17 04:16 UTC. Claude Code's Pro plan ends Thursday. The audit prompt had no replies by the launch.
- No model or assistant names in pushed files.

## Ledger updates for Duke
(No ledger tool was loaded this session; please apply in one write to `projects/sim`.)
- Steps done: the measures study run and all its results ingested (new step: "Run the dedicated measures study on one Runpod pod"); the suite page's second pass (Stage 1) built, draft pull request 34.
- Decision recorded: "What gives way to the study in the last Pro days?" Answer: option 1 (Duke, Oct 14): the study today; CoMSES package, fact sheet and share kit wait.
- New issue (medium): "Tier B (wider safety net, financing, demand multiplier, cost line, more avoided costs) is not built; packets in dev/plans/tier-b-packets.md."
- `next`: "Duke reads report v5-36 and merges pull request 34; then Part B (link the suite page) if he approves."
- Log: "Oct 14: measures study run on Runpod (all results in); suite page cards with status badges; draft PR 34."
