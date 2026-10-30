# Handoff (Oct 30, 2026): S34, the no-programme baseline against US data

The project is now coordinated from BetterToBest/research-update (its HANDOFF.md and PLAN.md come first); this file records this repository's state.

## What shipped
- Pull request 49 (`claude/s34-baseline-realism`): `dev/reports/baseline-realism.md` (plain words; every table in `baseline-realism-tables.md`), the tools (`dev/tools/baseline_realism.js`, `baseline_realism_table.py`, `sn_households.js`, `pe_households.py`, `sources/baseline_realism_us.py`), results in `dev/runs/baseline-realism/` and in BetterToBest/compassionism-sim-results `s34-baseline-realism-e8f8a77`.
- Engine: `CFG.CPS_EARN` (CPS ASEC 2026 earnings of adults 25-64), read by the wage readings `lt.s`, `lt.m` = 'all' or 'ft'; off by default. Guard test identical; lineage link bc0422920f8c recorded; validate, unit (222), domtest (153) pass. `harness.js` exports `snBenAt` (reporting only).

## Findings to carry
- Safety net matches PolicyEngine-US for six households (within $10; one $138 CTC difference from the missing child and dependent care credit).
- The wage scale is far below US earnings (median $39,200 against $60,000); with US earnings the no-programme share below the cost of living falls from 49.2% to 27.1%. Recommendation: S32 preregisters the 'all' reading as a row; S47 picks the yardstick before results.
- Household debt drifts (15.5% to 33.4% in debt over 20 years): open, the spending rule.

## Pitfalls
- `earlier-engine.html` must be resynced after any engine edit: `python3 dev/tools/sync_earlier.py` (domtest fails otherwise).
- A node_modules symlink in a worktree makes the run's manifest "dirty"; run studies from a clean worktree without it.
- Don't `pkill -f` a pattern that also appears in your own command line (it killed the shell again).
