# Session 28 Hand-off: One Release, Everything Planned

Oct 1, 2026 · Compassionism Simulation · v4.22 live · repo at `dc1ef62` · the Simulation ledger (document `sim`) is the source of truth

This replaces `session-27-handoff.md`, which still pointed to reworking the page first. No code and no page change this session.

## Where the project stands

- **Direction (d120, Duke's instruction):** build every planned mechanism first, then release the reworked page once. Compassionism is not shown in a half-finished state. v4.22 stays live and unchanged until then, and stays tagged so the release can be reverted.
- **What this changes:** the page rework (outline, comparison removal, history move, wording fixes) now happens at the release, not before. The earlier choices to match the no-program inflation (d109) and switch off the octave wage raise and inflation slow-down (d117) take effect at the release too. d119 is settled: no interim headline numbers are measured.
- **The comparison study** stays paused with its own ledger (document `compare`); its table stays on the page until the release.
- **Release gate (d122, default):** everything in scope built; 500-seed restudy in the three environments; gains confirmed on basket and wealth poverty; the three checks pass; page and harness agree on the same seeds; Duke has seen the restudy. Results are shown as they come out, with no target to hit.

## What the page can handle (step s61, done this session)

Measured on the live `index.html` and `harness.js` in Node, not in a real browser or phone. Speed is not the limit: one page run is well under a second on a desktop at 500 adults (my estimate for a phone is a few seconds at the 2,000-adult maximum). The port adds roughly 100 to 140 KB to a 769 KB file. The 500-seed restudy cannot run live and is shown as a precomputed panel. Not tested: real browsers (including last-digit agreement in Safari and Firefox), memory, and the mechanisms not yet written. The real cost is keeping two copies of the engine in step (d133). Duke's d121 and d122 picks, "decide what the page can handle first", are answered: the plan stands.

## Next session

**s55: the plain-words outline of the released page.** Read the live page and the replication page from the repo (`index.html` and `replication.html` on main); neither needs to be in the project files. Use Duke's answers to d120 to d133 where he has given them, and my defaults, said plainly, where he has not. Show no interim headline numbers.

## Then, in order

Build the mechanisms: s40 ESP split (designed and sized; privately owned ESPs keep their earnings, not yet sized), s51 production side, s45 financing (checkpoint after it, d121), s50 joining and leaving, s44 PTF and PTH capital and running costs, s60 octave rule, s53 spending rule, s54 BLEI-led reporting, s59 avoided public costs. Then s62 port into the page, s63 restudy, the page items (s56 to s58), s64 release, s65 new walk-through.

## Questions waiting for Duke (in the ledger, under Decisions)

Five need his own design answers before their steps start: d126 what counts as new output backing the BU (and how many years PTF capacity takes to build), d127 how Compassionism pays for itself, d128 how adults join and leave, d129 how an adult moves up an octave, d130 who pays for PTF and PTH capital. The release plan (d121 to d125) and the page questions (d131, d132) have defaults applied.

## Project files

- **Keep:** this file.
- **Remove:** `session-27-handoff.md` (replaced), `N1-design-esp-surplus.md` and `N1-s34-restudy-500.md` (not needed until s40; keep copies in your archive).
- **Bring back with s40:** `N1-design-esp-surplus.md` and `N1-s34-restudy-500.md`.
