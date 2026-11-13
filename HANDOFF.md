# Handoff (Nov 13, 2026): engine state after S59 part 2 (the weighted top tail, business owners, capital income)

The project is coordinated from BetterToBest/research-update (its HANDOFF.md and PLAN.md come first); this file records this repository's state. The full Nov 10 handoff, with every shipped item from S6 to S66, is kept word for word in `dev/handoff-archive/2026-11-10-handoff-full.md`. Pitfalls are in `dev/PITFALLS.md`.

## What shipped (latest first)
- S59 part 2 (Nov 12-13, pull request 93): switch `WEALTH_TAIL` (row option `wt`), a weighted Pareto tail on the starting wealth (weights `a._w` enter measures only; keys `WT_KEYS`; study option `wtm`); options of `rt`: `bo` (business owners), `ci` (the income wealth pays, `a.yrCapUSD`), `ng`, `rg`; surplus-split option `own: 'eq'`. Off = identical; 8 unit tests (`wtUnitSuite`). Part 1's `RT_EDGES` corrected (they were 9.4% too high; no finding changes). Report `dev/reports/s59-tail-returns.md`; tables `dev/runs/s59-tail/tables.md`; results compassionism-sim-results `s59-tail-62a189b`. Finding: the start's top 1% share of wealth goes from 20.8% to 30.1% (survey 31.5%); the programme lowers it by 0.9-1.8 points at year 20 under the main reading but raises it by 0.1-1.2 without debt relief, so the direction is not established.
- Code map (Nov 13, pull request 94): `dev/CODEMAP.md` (grep it for line numbers; `node dev/tools/codemap.js` rebuilds it). No engine change.
- S59 part 1 (Nov 10, pull request 92): switch `RETURNS` (row option `rt`), wealth held by asset class; off = identical. Report `dev/reports/s59-asset-classes.md`; results compassionism-sim-results `s59-assets-1d2cf29`.
- S66 (Nov 10, analysis only): `dev/reports/s66-low-share-trace.md`; results `s66-trace-4e9d841`.
- S58 (Nov 9, pull request 90): switch `PRICE_RULE` (row option `pr`) and study option `mf`; report `dev/reports/s58-price-rule.md`.
- S61 (Nov 9, pull request 88): switches `LF_SCOPE` (`lf`) and the extended debt reading (`dr`); report `dev/reports/s61-baseline-scope.md`.
- Earlier work (S6, S13, S35 to S39, S47 to S57): see the archive file above.

## Branch and pull request state
- Branch `claude/s59-tail-returns`, pull request 93 (S59 part 2): see research-update HANDOFF.md for whether it merged.

## Long jobs in flight
- None.

## Next 3 actions
1. S67 (price rule: derivation, time step, wording) or S60 (bargaining power): research-update PLAN.md has each step's text. Preregister first in research-update `prereg/`.
2. A creditor side for `rt` (who loses when fixed-rate debt is inflated away) is the largest open gap in the wealth results: every concentration result turns on it (`dev/reports/s59-tail-returns.md`, Limits). Not yet a plan step; S63 decides.
3. Before any engine change, run `node dev/tools/guard_test.js` and record the change with `node dev/tools/engine_lineage.js prove "what changed"`.

## Files to touch
- `index.html`: grep `WEALTH_TAIL`, `WT_`, `RT_`, `rtCap`, `spBase`, `PRICE_RULE`; look the line ranges up in `dev/CODEMAP.md`.
- `harness.js`: grep `wtUnitSuite`, `rtUnitSuite`, `frozenRow`.
- `sources/s59_tail.py`, `sources/s59_capital.py`, `sources/s59_portfolio.py`; pilot tools `dev/tools/s59_tail.js`, `dev/tools/s59_tail_table.py`.
- `dev/DECISIONS.md`: add a section per decision (grep "S59, part 2" for the last one).

## Pitfalls (the ones that bite every session; the rest are in `dev/PITFALLS.md`)
- Never quote an `rt` wealth or concentration result without the no-debt-relief reading (`chi: 1`) beside it: inflated-away mortgages are a gain with no loser, and the sign of the programme's effect on the top 1% share turns on it.
- With the tail (`wt`) on, read only the weighted keys (`wt*`, `dm*`, `rt*`); the unweighted Ginis and top shares are not valid. No rule may read `a._w`.
- A pilot's off rows must carry CPS earnings (`lt: {s: 'all', m: 'all'}`) to match S66's rows.
- `earlier-engine.html` must be resynced after any engine edit: `python3 dev/tools/sync_earlier.py` (domtest fails otherwise).
- Run studies from a clean worktree (a `node_modules` symlink makes the run's manifest "dirty").
- Pilot result files write 0 for keys past the run; never read that 0 as a value.
- The second implementation (`s50_release.py`) reproduces the old engine until a new packet is built.
