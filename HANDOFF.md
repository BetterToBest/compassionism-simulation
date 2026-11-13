# Handoff (Nov 13, 2026): engine state after S71 (a creditor side for debt that inflation wipes out)

The project is coordinated from BetterToBest/research-update (its HANDOFF.md and PLAN.md come first); this file records this repository's state. The full Nov 10 handoff, with every shipped item from S6 to S66, is kept word for word in `dev/handoff-archive/2026-11-10-handoff-full.md`. Pitfalls are in `dev/PITFALLS.md`.

## What shipped (latest first)
- S71 (Nov 13, pull request 97): option `cr` of `rt`, a creditor side for household fixed-rate debt (`RT_CR`, `crOpts`, `crRates`, `crYear`; readings `inc: 'pass' | 'hold' | 'hedge'`, `pop: 1`, `out: 0`, `w: 0`; keys `CR_KEYS`). Off = identical; 7 unit tests (`crUnitSuite`). Coefficients: `sources/s71_creditors.py` (the Fed's Financial Accounts, SCF 2022; Doepke and Schneider 2006). Report `dev/reports/s71-creditor-side.md`; tables `dev/runs/s71-creditors/`; results compassionism-sim-results `s71-creditors-f7572fd`. Findings: wealth poverty does not move with the creditor side; the programme still lowers the top 1% share in every creditor reading; the sign turns on whether debt relief happens, not on the lender (a dated note in the S59 report).
- S67 (Nov 13, pull request 96): three dated correction notes (S58 and S57 reports; no figure changed); the capacity rule's closed form (`dev/tools/s67_closed_form.py`); the response speed estimated on the rule's own variable (`sources/s67_pstar.py`: zero within error) and 77 high-inflation episodes (`sources/s67_panel.py`); options `q` (sub-steps within the year), `bv` (velocity response), `bd` (velocity drift) of `pr`, off = identical, 7 unit tests in `prUnitSuite`; reported key `prAvg`. Report `dev/reports/s67-price-rule-derivation.md` (its section 9 is the recommendation for S63: today's rule as the main row); results compassionism-sim-results `s67-price-985f0c3`.
- S59 part 2 (Nov 12-13, pull request 93): switch `WEALTH_TAIL` (row option `wt`), a weighted Pareto tail on the starting wealth (weights `a._w` enter measures only; keys `WT_KEYS`; study option `wtm`); options of `rt`: `bo` (business owners), `ci` (the income wealth pays, `a.yrCapUSD`), `ng`, `rg`; surplus-split option `own: 'eq'`. Off = identical; 8 unit tests (`wtUnitSuite`). Part 1's `RT_EDGES` corrected (they were 9.4% too high; no finding changes). Report `dev/reports/s59-tail-returns.md`; tables `dev/runs/s59-tail/tables.md`; results compassionism-sim-results `s59-tail-62a189b`. Finding: the start's top 1% share of wealth goes from 20.8% to 30.1% (survey 31.5%); the programme lowers it by 0.9-1.8 points at year 20 under the main reading but raises it by 0.1-1.2 without debt relief, so the direction is not established.
- S59 part 1 (Nov 10, pull request 92): switch `RETURNS` (row option `rt`), wealth held by asset class; off = identical. Report `dev/reports/s59-asset-classes.md`; results compassionism-sim-results `s59-assets-1d2cf29`.
- S66 (Nov 10, analysis only): `dev/reports/s66-low-share-trace.md`; results `s66-trace-4e9d841`.
- S58 (Nov 9, pull request 90): switch `PRICE_RULE` (row option `pr`) and study option `mf`; report `dev/reports/s58-price-rule.md`.
- Earlier work (S6, S13, S35 to S39, S47 to S57, S61; S61's report is `dev/reports/s61-baseline-scope.md`): see the archive file above.

## Branch and pull request state
- Branch `claude/s71-creditor-side`, pull request 97 (S71): see research-update HANDOFF.md for whether it merged.

## Long jobs in flight: none.

## Next 3 actions
1. S60 (bargaining power): research-update PLAN.md has the step's text. Preregister first in research-update `prereg/`.
2. S68 places the closed form (`dev/reports/s67-price-rule-derivation.md`, section 3, "For MODEL_SPEC") and the options `q`, `bv`, `bd` and `prAvg` in MODEL_SPEC, ODD and TESTBED_SPEC.
3. Before any engine change, run `node dev/tools/guard_test.js` and record the change with `node dev/tools/engine_lineage.js prove "what changed"`.

## Files to touch
- `index.html`: grep `WEALTH_TAIL`, `WT_`, `RT_`, `rtCap`, `spBase`, `PRICE_RULE`; look the line ranges up in `dev/CODEMAP.md`.
- `harness.js`: grep `wtUnitSuite`, `rtUnitSuite`, `prUnitSuite`, `frozenRow`.
- Price rule: `index.html` `prStep`, `prStepQ`, `PR_DEFAULTS`; pilot tools `dev/tools/s67_price.js`, `dev/tools/s67_table.py`.
- `sources/s59_tail.py`, `sources/s59_capital.py`, `sources/s59_portfolio.py`; pilot tools `dev/tools/s59_tail.js`, `dev/tools/s59_tail_table.py`.
- `dev/DECISIONS.md`: add a section per decision (grep "S59, part 2" for the last one).

## Pitfalls (the ones that bite every session; the rest are in `dev/PITFALLS.md`)
- `cr` reads adults' weights through four yearly totals (the one rule that does). Its totals are taken at the first adult's turn, not before the year's loop: a pathway exit pays equity into wealth in between. With `w: 0` the `cr*` keys are unweighted and not comparable in dollars with other rows.
- The no-debt-relief reading (`chi: 1`) is not a bound for the creditor readings: it removes the borrower's gain; `cr` adds the saver's loss. Quote both beside any wealth result, with `cr: {out: 0}` as the upper bound on creditor losses.
- Never quote an `rt` wealth or concentration result without the no-debt-relief reading (`chi: 1`) beside it: inflated-away mortgages are a gain with no loser, and the sign of the programme's effect on the top 1% share turns on it.
- With the tail (`wt`) on, read only the weighted keys (`wt*`, `dm*`, `rt*`); the unweighted Ginis and top shares are not valid. No rule may read `a._w`.
- A pilot's off rows must carry CPS earnings (`lt: {s: 'all', m: 'all'}`) to match S66's rows.
- `earlier-engine.html` must be resynced after any engine edit: `python3 dev/tools/sync_earlier.py` (domtest fails otherwise).
- Run studies from a clean worktree (a `node_modules` symlink makes the run's manifest "dirty").
- Pilot result files write 0 for keys past the run; never read that 0 as a value.
- Under any price rule, read wealth poverty and median real wealth as yearly averages (`ppov_*`, `pmedW_*`) beside year 20: the year-20 reading changes sign with the rule. The rationed share and shadow prices on a yearly step measure the step (22.5% yearly, 1.9% in quarters).
- `node domtest.js` needs `npm install` first; it fails until the lineage is proved and `earlier-engine.html` is resynced.
- The second implementation (`s50_release.py`) reproduces the old engine until a new packet is built.
