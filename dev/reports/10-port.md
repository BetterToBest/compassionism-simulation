# Step 10 report: the mechanisms are in the page

Oct 1, 2026 · plan step 10 · Claude · on `next-release` only; the live page on `main` is unchanged

## What was done

Everything built in steps 1-9 lived only in `harness.js`, the copy of the engine used for the 500-seed studies. It is now also in `index.html`, the page itself:

- the model as specified on the Hub (businesses converting BU, project hiring, ESP payroll);
- the ESP split, the production side, open enrolment, the PTF running costs and the octave sensitivity;
- the Source financing, the spending rule, and the price and labour modules the results depend on;
- the runner that produces every figure in the reports.

The code is copied **verbatim** by a script (`dev/tools/port_engine.py`), not retyped. That keeps one engine with two copies, as design default 9 asks. The script can be rerun after any engine change and gives the same page if nothing changed.

## How we know the copies agree

Two new checks run on every change (`node domtest.js`, phase 12):

1. Every one of the 45 ported functions in the page is a character-for-character copy of `harness.js`.
2. The release run (every mechanism, paid for by the Source, at the sourced spending share) gives **identical results** in the page and in the harness on the same seeds, for every one of the 1,386 measure-rows compared, in all three environments, for no programme, the release row and H1.

All 95 earlier checks still pass, so with the new switches off the page behaves exactly as v4.22: same presets, same seed-42 figures, same front door.

## Not yet done (step 12)

The page does not show the release run yet. The comparison table, the controls and the text are still v4.22's. Step 12 rebuilds the page around the release run, following the outline in `00-page-outline.md`. The page grew from 778 KB to 889 KB.

## Not tested

- Real browsers (Safari, Firefox) and phones. Last-digit agreement between browsers is not checked; jsdom (Node) is.
