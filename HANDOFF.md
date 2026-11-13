# Handoff (Nov 13, 2026): engine state after S59 part 1; handoff shortened

The project is coordinated from BetterToBest/research-update (its HANDOFF.md and PLAN.md come first); this file records this repository's state. The full Nov 10 handoff, with every shipped item from S6 to S66, is kept word for word in `dev/handoff-archive/2026-11-10-handoff-full.md`. Pitfalls are in `dev/PITFALLS.md`.

## What shipped (latest first)
- Code map (Nov 13, pull request 94): `dev/CODEMAP.md` (grep it for line numbers; `node dev/tools/codemap.js` rebuilds it). No engine change.
- S59 part 1 (Nov 10, pull request 92): switch `RETURNS` (row option `rt`), wealth held by asset class; off = identical. Report `dev/reports/s59-asset-classes.md`; results compassionism-sim-results `s59-assets-1d2cf29`.
- S66 (Nov 10, analysis only): `dev/reports/s66-low-share-trace.md`; results `s66-trace-4e9d841`.
- S58 (Nov 9, pull request 90): switch `PRICE_RULE` (row option `pr`) and study option `mf`; report `dev/reports/s58-price-rule.md`.
- S61 (Nov 9, pull request 88): switches `LF_SCOPE` (`lf`) and the extended debt reading (`dr`); report `dev/reports/s61-baseline-scope.md`.
- Earlier work (S6, S13, S35 to S39, S47 to S57): see the archive file above.

## Branch and pull request state
- `main` is at the merge of pull request 94. Pull request 94 passed all checks before it merged. This session left no other pull request open.

## Long jobs in flight
- None.

## Next 3 actions
1. S59 part 2 (research-update PLAN.md, S59 "Part 2"): preregister first in research-update `prereg/`, then build the weighted top tail (`WEALTH_TAIL`), returns that differ by wealth, business ownership and its income, the check against the Fed's accounts, and the owners rule. Behind switches; off = identical.
2. S67 (price rule: derivation, time step, wording) and S60 (bargaining power) can start too.
3. Before any engine change, run `node dev/tools/guard_test.js` and record the change with `node dev/tools/engine_lineage.js prove "what changed"`.

## Files to touch
- `index.html`: grep `RETURNS`, `RT_` (the asset-class switch to extend) and `PRICE_RULE`; look the line ranges up in `dev/CODEMAP.md`.
- `harness.js`: grep `rt` row options and `frozenRow`.
- `sources/s59_portfolio.py`, `sources/s59_real_gains.py`; pilot tool `dev/tools/s59_assets.js`; unit suite `rtUnitSuite`.
- `dev/DECISIONS.md`: add a section per decision (grep "S59, part 1" for the last one).

## Pitfalls (the ones that bite every session; the rest are in `dev/PITFALLS.md`)
- Never quote an `rt` wealth result without the no-debt-relief reading (`chi: 1`) beside it: inflated-away mortgages are a gain with no loser.
- A pilot's off rows must carry CPS earnings (`lt: {s: 'all', m: 'all'}`) to match S66's rows.
- `earlier-engine.html` must be resynced after any engine edit: `python3 dev/tools/sync_earlier.py` (domtest fails otherwise).
- Run studies from a clean worktree (a `node_modules` symlink makes the run's manifest "dirty").
- Pilot result files write 0 for keys past the run; never read that 0 as a value.
- The second implementation (`s50_release.py`) reproduces the old engine until a new packet is built.
