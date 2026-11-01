# S50: a second, independent implementation of the release row

Prepared Nov 1, 2026 (research-update step S50). The project is the Compassionism Simulation, an open agent-based model of Duke Johnson's Compassionism framework (500 simulated adults in their households, 20 years, with and without the programme). Until an outside economist reviews the model, an independent re-implementation is the strongest check one author can arrange: if a second program written from the written description gives the same results, the description and the code agree; where they differ, one of them has a mistake worth finding.

The first such check (S10, Oct 29) rebuilt the engine's validation presets and matched them exactly, but those presets switch off every mechanism behind the published figures. This packet is for **the release row itself and its no-programme run**: the pair behind every figure the Research Hub and the simulation page publish.

## Your task

Write the release row and its paired no-programme run again, in Python, **from the written description first** (`MODEL_SPEC.md`, then `ODD.md`), using `release-config.json` for every setting, and only then use the code excerpt (`code/release-row-code.js`) to settle questions the description leaves open. Every time you open the code to settle something, write it down in `GAPS.md`: each is a gap in the description, and that list is half the value of the exercise.

Do the runs in this order and stop at the first one you cannot match, saying why (if the reason is found and the rest costs little, go on, as S10 did, and say so):

1. **Reference, no programme**: households, wages, job loss and unemployment insurance, today's safety net (SNAP with its work rule, the EITC, the refundable Child Tax Credit), the spending rule, the price level, the poverty measures.
2. **Reference, the release row**: Basic Units, project hiring, ESP payroll and the surplus split, PTF by sector and its capacity, PTH and its books, SZH and CIP, open enrolment, the Source's new money and the price module, the labour response, the flat contribution.
3. **Adverse**, then **Stress** (recessions, 2% outside inflation, the automation wave; Stress has the weaker settings), both runs each.

## What is in the packet

- `MODEL_SPEC.md`, `ODD.md`: the written description. Read these first. `MODEL_SPEC.md` section 12 and Appendix A were written for this check.
- `release-config.json`: for each environment and each of the two runs, the preset, the study options, the row's options, and every engine switch and constant whose value differs from the engine's defaults while that run goes (`switchesDifferentFromLoad`), plus every top-level value at load (`atLoad`). A few entries are run state, not settings (`S3_CACHE`, `HL_GOVREF`, `HHS`, `TB_BLEI_NET`); ignore them.
- `code/release-row-code.js`: the engine code that runs in these six runs, in source order, each piece headed by its file and line. Code inside it that never ran in seeds 1-20 of the six runs is folded to `⟦not run⟧`. `code/release-row-code-full.js` has the same pieces unfolded; `code/not-run.md` lists the functions the code names but never calls here (switches that are off). Nothing else of the engine is needed.
- `reference/s50-ENV-1-500.json` (ENV = `ref`, `adv`, `st`): the real engine's per-seed outputs for seeds 1 to 500, both runs (`rows[0]` no programme, `rows[1]` the release row), every key the engine reports, unrounded. `reference/KEYS.md` says which keys to compare first and what they measure.
- `run.txt` and `SHA256SUMS`: how the packet was made (commands, engine commit, file hashes).

## What counts as a match

1. **Best case, exact.** The generator is `mulberry32` and the samplers are given exactly (`MODEL_SPEC.md` 4.1); the streams and their seeds are in section 8. If your program draws the same numbers in the same order, every key of every seed matches to rounding error (relative difference under 1e-9). Try this first, seed 1, Reference, no programme; it is the strongest result.
2. **Otherwise, statistical.** For each key, compare your 500-seed mean with the reference's by the two-sample test: a key matches if `|mean_yours − mean_ref| ≤ 2 × √(sd_yours²/500 + sd_ref²/500)`. Do the same for the programme's effect (release row minus no programme, per seed). By chance alone about one key in twenty fails at this level; say how many you would expect and how many failed.
3. **Never tune.** Do not change a constant or a rule to make a number agree. If a number disagrees, find which rule differs and report it. A disagreement is a finding, not a failure.

## Two phases (the order matters for what the check proves)

1. **Phase 1, independent.** Work from this packet alone. Do not open the engine (`index.html`, `harness.js`, `earlier-engine.html`), the repository's `dev/` folder outside this packet and your own output folder, the results repository, or the published data until your phase-1 program and its results are **committed and pushed**.
2. **Phase 2, explaining the differences.** Only then may you read the engine to explain each remaining difference. Put each explanation into the program behind a switch (as S10's `--engine-fills`), so phase 1 stays reproducible, and show whether it closes the difference.

## What to hand back

Under `dev/reports/s50-independent-implementation/` in the repository:

1. The Python program (runnable with `python3 -I s50_release.py --env ref --row release --seed 1`, and a mode that runs seeds 1-500 and writes the per-seed results).
2. Comparison tables, phase 1 and phase 2: environment by run by key, reference mean, your mean, the test, match or not; the effect likewise.
3. `GAPS.md`: every gap or contradiction you found in the written description, in plain words, each with the line of the code excerpt that settled it.
4. `REPORT.md`: a short report for Duke in plain words (he is not a programmer or economist): what was checked, what agreed, what did not, and what it means. No bare labels such as "s40" or "d101".
5. `results/` with `run.txt` (commands, versions) and `SHA256SUMS`.
6. State plainly which runs you did not reach.

Add a one-line entry to `dev/DECISIONS.md` saying the acceptance rule above was used.
