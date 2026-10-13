# Handoff (Oct 13, 2026; session 2g, ledger step s137 done: the 500-seed study's results report)

## What shipped
- Follow-up Sobol (s137b) finished 18:42 UTC; `DONE` present; all 17 hashes match; copied to `dev/runs/s137b/` (commit 1169426). The Runpod pod list is empty.
- `dev/tools/gsa.js`: every Sobol output also gives Sc, a centred first-order index (less noise; S, ST and intervals bit-identical). Recomputed from the s137b blocks into `dev/runs/s137b/gsa-sobol-st-sc.json` (commit 698bce2).
- `dev/reports/v5-30-s137-results.md`: the study's results report, framed as the outside audit's "fix later, E" asks. `dev/DECISIONS.md`, Session 2g, records the choices (commit dff9b15). The engine is unchanged; validate, unit and domtest all pass.
- Main findings: Compassionism lowers basket poverty in every cell (Reference, today's health system: -31.7 points). "Too little wealth" rises, but with prices held flat it falls instead, so the price response drives that rise. Participation and the BU amount explain most of the spread.

## Branch and pull request state
- Branch `claude/pensive-knuth-nqiqvu`, from main 00b5866 (pull request #21 merged). Draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/22 into `main`; CI not yet reported at handoff. Duke reads the report and merges (report, results and tools only; no page change).

## Long jobs in flight
- None.

## Next 3 actions
1. Check that CI on pull request #22 is green. If a check fails, fix it on the same branch.
2. Session 4 (ledger step s133): put the results on the pages as version 5.5: uncertainty and sensitivity, the compare page, and the health panel with and without Compassionism. Figures and wording come from `dev/reports/v5-30-s137-results.md`; keep its captions (single payer depends on the Yale preprint; the safety net's outlays are not financed in the model; "too little wealth" comes through prices). Set the version with `python3 dev/tools/set_version.py 5.5.0`, then run `node dev/tools/check_versions.js`. Run the three checks and `node dev/tools/guard_test.js`.
3. Open its own draft pull request; do not stack on #22 once #22 has merged (restart the branch from `main`).

## Files to touch
`dev/reports/v5-30-s137-results.md` (sections 1-8), `index.html` (over 300 lines: grep `rel-panel`, `id="answer"`, `fx-sec`), `dev/runs/s137/s137table-*.json`, `dev/runs/s137b/gsa-sobol-st-sc.json`, `dev/PLAN.md` (grep `v5.5`), `dev/PROGRESS.md` (last section).

## Pitfalls
- The results token expires **2026-10-17 04:16 UTC**. Renew it and update the Runpod secret `github_results_token` before any later Runpod run.
- Duke's Claude Pro plan ends Oct 15 (ledger issue i19). Page work suits Sonnet at medium effort.
- The study's comparison restudy is still undefined (it belongs to ledger step s95); do not guess it.
- The first Sobol (s137) kept no per-point results, so its noisy first-order figures cannot be recomputed. Use its totals only.
- `node harness.js unit` can take several minutes. Run it in the background, not in a 2-minute foreground call.
