# s118: a second, independent implementation of the core yearly loop

Prepared Oct 15, 2026 for a plain chat (no repository access, no Claude Code). The project is the Compassionism Simulation, an open agent-based model of Duke Johnson's Compassionism framework (500 simulated adults over 20 years). Until an outside economist reviews the model, an independent re-implementation is the strongest check one author can arrange: if a second program written from the written description gives the same results, the description and the code agree; where they differ, one of them has a mistake worth finding.

## Your task

Write the core yearly loop again, in Python, **from the written description first** (`ODD.md`, then `MODEL_SPEC.md`), and only then use `core-loop.js` to settle questions the description leaves open. Every time you had to open `core-loop.js` to settle something, write it down: each is a gap in the description, and that list is half the value of the exercise.

Do the presets in this order and stop at the first one you cannot match, saying why:

1. **Traditional Welfare Baseline (3% inflation)**: no programme. Wages, wealth, prices, the cost of living, the poverty measures.
2. **CCO Only**: Basic Units, expiry, conversion, the tax; none of the other institutions.
3. **Full Integration**, then **Adverse** and **Stress Test** if there is room.

## What is in the packet

- `ODD.md`, `MODEL_SPEC.md`: the written description. Read these first.
- `core-loop.js`: the real engine's core, excerpted (JavaScript). Mechanisms outside the core are listed in `later-modules.md`; every one of them is switched off in the presets above, so you can ignore them.
- `reference-outputs.json`: the real engine's results for five presets, seeds 1 to 30 and 42, 500 adults each, in the keys that `node harness.js validate` prints (wealth poverty %, median wealth $, median BLEI d, Gini, BLEI poverty %, and more). Each preset's parameters are included.
- Seed-42 documented values (the engine's own regression fixtures; the reference file reproduces them):

| Preset | wealth poverty % | median wealth $ | median BLEI days | Gini | BLEI poverty % |
|---|---|---|---|---|---|
| Full Integration | 15.8 | 570661 | 1975 | 0.518 | 13.2 |
| CCO Only | 24.8 | 427239 | 1283 | 0.575 | 21 |
| Traditional Welfare Baseline (3%) | 68.8 | -10000 | 8 | 0.824 | 67.6 |
| Adverse Environment | 36.8 | 205005 | 723 | 0.658 | 32.4 |
| Stress Test | 59.8 | -10000 | 16 | 0.785 | 57.2 |

## What counts as a match

1. **Best case, exact:** the random generator is `mulberry32` (given in the description); if your program draws the same numbers in the same order, seed 42 reproduces the table above exactly. Try this first; it is the strongest result.
2. **Otherwise, statistical:** run your program for seeds 1 to 30 and compare the mean and the spread of each key with the reference file's. A key matches if your mean lies within two standard errors of the reference mean (standard error = the reference's standard deviation over 30 seeds, divided by the square root of 30). Report every key, matching or not.
3. **Never tune.** Do not change a constant, or a rule, to make a number agree. If a number disagrees, find which rule differs and report it. A disagreement is a finding, not a failure.

## What to hand back

1. The Python program (one file, runnable with `python3 -I s118_loop.py --preset baseline --seed 42`).
2. A comparison table: preset by key, reference mean, your mean, and match or not.
3. A list of every gap or contradiction you found in the written description, in plain words, each with the line of `core-loop.js` that settled it.
4. A short report for Duke in plain words (he is not a programmer or economist): what was checked, what agreed, what did not, and what it means. No bare labels such as "s40" or "d101".
5. State plainly which presets you did not reach.

Put the files in the repository under `dev/reports/s118-independent-implementation/` (or send them to whoever has repository access); add a one-line entry to `dev/DECISIONS.md` saying the acceptance rule above was used.
