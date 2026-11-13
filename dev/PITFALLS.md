# Pitfalls and findings to carry

Moved from the root HANDOFF.md on Nov 13, 2026, word for word, so the root file can stay short. Read the lines that match the mechanism you are touching (grep the switch or key name here first). Add new pitfalls at the end; the root HANDOFF.md keeps only the few that bite every session.

## Findings to carry (pilot, 50 seeds)
- No outcome depends on population size beyond Monte Carlo error (11 of 504 comparisons, 2.2%); the synergy table and participation curve at 10,000 adults match 500.
- The CCO is almost all of the effect; PTF, PTH and SZH are near inert; material interactions are CCO × CIP (overlap on the cost of living, reinforcement on wealth). So S37 (community layer) goes ahead.
- With ageing on, the release row worsens wealth; non-joiners are worse off with the programme.
- Full batch: about 230 runner-hours on Actions, 2 processes per runner. Report section 9 lists what S47 must add (nulls for keys past the run, design-neutral BLEI at year 20 in 40-year runs, a yearly-rate inflation reading, lower participation levels).

## Pitfalls
- S59 `rt`: the model has no lender, so fixed-rate debt inflated away is a gain with no loser; never quote an `rt` wealth result without the `chi: 1` reading beside it. `rt` with `sv` is refused. A pilot's `off` rows must carry CPS earnings (`lt: {s: 'all', m: 'all'}`) to match S66's rows. In Reference the no-programme run has no inflation; in Adverse and Stress it has.
- S66: the release rows switch PTF and PTH damping of outside inflation off (`n1Row`, d86); no rule or reading of a release row may lean on damping. A fixed-share row's year-20 wealth depends on the year the PTFs' capital account crosses full capacity (the surplus split's phase 2): read 20 and 40 years.
- S58: under `pr` the year-20 wealth readings depend on where the rule's ~9-year inflation wave stands at year 20; read wealth over the yearly path. Do not combine a normal-years slack reading (`pr.h`) with the spending layer's normal-times slack (`ml.nt`): both would use the same slack. The rule acts in testbed runs only (`priceRun` keeps today's rule).
- A no-programme row's PTF capacity keys (`pd*`) read the previous run's PTF state (pre-existing, reporting only): the first study after `paUnitSuite` differs on them from later ones. `prUnitSuite`'s `mf` test runs a warm-up for this.
- S61 `lf` reuses `a._ret`: any new rule that reads `a._ret` as "aged 67 and over" must check `a._lf` too. An adult with no own income has wage 0: guard any ratio to the wage (the `lbRaise` 0/0 was one).
- S55 `pa: 'open'` needs PTF by sector (`v54.ptfs`); the run throws otherwise. Under `'open'` `pfCut` is the mean cut over every adult (over members under `'members'`), and S37's `clHi`/`clTh` still describe members. `dev/tools/study_data.py` and `unsourced_check.py` read the PTF damping constant out of the engine text: keep their patterns in step if that line changes.
- Under `lv`, a business is never paid less than face value (premium floored at 0); `lv: {}` is identical to off. The uncapped protected account paid with new money runs away (about 1,200% a year on seed 1): that is the lever's result, not a bug.
- In Stress the released base tax is 18% (maxMult 6, maxOct 4, BU $900): the job passes `tref` = the design's own tax, so the joining reading is calibrated per environment.
- The supply shock is a preset key (`p.sx`), not a row option: the environment's, so `baselineFor` carries it to the supply path and the no-programme run. A study must give `envP.sx` the same shock path as its rows (shock.js runs each path as its own study). Own cost (`yrCostUSD`) is net of BU spent, so the BU's protection shows in the participant groups.
- The second implementation (`s50_release.py`) reads the packet zip; after any engine change it reproduces the old engine, not the new one, until a new packet is built (`dev/packets/make_s50_reference.js`, `build_s50_packet.py`).
- `c22` on a no-programme row only marks who is left out by status (identical outputs; unit test), so the same adults can be paired. Status is drawn per household on stream seed + 600067.
- Study row option `cm` is the conversion model; the community layer is `cl`. With the layer on, rows without PTF are identical to the layer off, and one community (k at least the population) equals off exactly: keep it so (unit test in `v54UnitSuite`).
- `earlier-engine.html` must be resynced after any engine edit: `python3 dev/tools/sync_earlier.py` (domtest fails otherwise).
- A node_modules symlink in a worktree makes the run's manifest "dirty"; run studies from a clean worktree without it.
- Don't `pkill -f` a pattern that also appears in your own command line (it killed the shell again).
- `s54_levers.py` reads a missing `lv*` key on a no-programme row as 0 (those keys exist only on programme rows); programme inflation is `endoAnn`'s change, in points a year in the tables.
- The S54 issuance caps (2, 4, 8%) give identical rows: each removes the whole premium, since the BU's face value alone exceeds the cap (`lvCap` 0).
- Under the flat wage contribution the 90% and 100% wage rows are identical: wages index to the general price level (`PRICE.piG`), which only new money moves, and a fully taxed payout makes none.
- Pilot result files write 0 for keys past the run (year-40 keys in 20-year rows); never read a 0 there as a value.

- The frozen model is `harness.js frozenRow` (au, fx, sc 0.877): a job that sets `sc` after calling it replaces the frozen share (the measurement tools do this on purpose). Study-level `sc` does not matter under `fx.sp`; the row's does.