# Handoff (Oct 31, 2026): S35, the pilot studies

The project is now coordinated from BetterToBest/research-update (its HANDOFF.md and PLAN.md come first); this file records this repository's state.

## What shipped
- Pull request 50 (S35, part 1): reporting keys `plv_0`..`plv_39`, `hhDebt20`/`hhDebt40`, and the debt reading `c.dr` (off by default). Engine commit `70d23be`, used by every pilot.
- S35, part 2 (`claude/s35-pilot-studies`): `dev/reports/pilot-studies.md` (labelled pilot throughout), its tables and estimates in `dev/runs/pilot-studies/`, written by `dev/tools/pilot_studies.py` from BetterToBest/compassionism-sim-results `pilot-*-70d23be`. No engine change.

## Findings to carry (pilot, 50 seeds)
- No outcome depends on population size beyond Monte Carlo error (11 of 504 comparisons, 2.2%); the synergy table and participation curve at 10,000 adults match 500.
- The CCO is almost all of the effect; PTF, PTH and SZH are near inert; material interactions are CCO × CIP (overlap on the cost of living, reinforcement on wealth). So S37 (community layer) goes ahead.
- With ageing on, the release row worsens wealth; non-joiners are worse off with the programme.
- Full batch: about 230 runner-hours on Actions, 2 processes per runner. Report section 9 lists what S47 must add (nulls for keys past the run, design-neutral BLEI at year 20 in 40-year runs, a yearly-rate inflation reading, lower participation levels).

## Pitfalls
- `earlier-engine.html` must be resynced after any engine edit: `python3 dev/tools/sync_earlier.py` (domtest fails otherwise).
- A node_modules symlink in a worktree makes the run's manifest "dirty"; run studies from a clean worktree without it.
- Don't `pkill -f` a pattern that also appears in your own command line (it killed the shell again).
- Pilot result files write 0 for keys past the run (year-40 keys in 20-year rows); never read a 0 there as a value.
