# One engine copy: is it workable? (v5.3 plan item B1, feasibility only)

Oct 6, 2026 · Claude · dashboard decision d166 ("read the engine straight out of the page") · no code changed yet

## The question

Households will touch almost every part of the engine. Today the engine exists in two files, `harness.js` (Node, used for the 500-seed studies) and `index.html` (the page). The dashboard's decision (d166) is to keep `index.html` one file and have the harness read the engine out of it, instead of carrying its own copy, if that is workable; otherwise keep the copy and extend the equality checks.

## What is actually duplicated today

Counting top-level declarations (functions and variables) in `harness.js` before its command-line part (279 in all):

| Group | Count | How the two files are kept equal |
|---|---|---|
| The release engine (the testbed, every module, the yearly loop `runYear`) | 165 | Already one source: `dev/tools/port_engine.py` copies them verbatim from `harness.js` into the page's marked block; domtest's parity check (12 rows × 154 measures) and the engine-block hash in each panel's manifest confirm the copy |
| The shared core of the earlier engine (random numbers, the starting population, BLEI, recessions, metrics: `makeLatentAgent`, `agentBLEI`, `buildRecessionPath`, ...) | 42 | Hand-kept in both files; domtest's "bindings fingerprint" compares them and allows five listed differences |
| Harness-only (study modes, unit suites, comparators, legacy switches) | 72 | Not on the page |

So the real drift risk is the 42 hand-kept core functions, and the fact that the release engine is edited in one file and copied into another by a tool someone must remember to run. The five allowed differences: the page adds two display-only keys to `CFG` and a colour and CSS class to the tiers (`TIERS`, `getTier`); the harness adds a legacy branch to `drawAutomationRisk` (behind `AUTOMATION_SAMPLER_LEGACY`, off by default; `validate` uses it to reproduce v4.19) and a UBI term to `incomeBasketMetrics` (zero outside the UBI comparators).

## Can the harness read the engine out of the page?

Yes. The page's inline script has only five top-level statements that act at load (a Chart.js stand-in, two settings of `REL_HUB`, and three event listeners); everything else is declarations. The same chunker `port_engine.py` uses (split the script at each top-level `function`, `var` or `CFG.X =`) can pick out, by name, the 165 release-engine declarations and the 42 core ones, in page order, without running any page code.

One detail decides how: `harness.js` is in strict mode, so a direct `eval` of the engine inside it would keep the engine's declarations to itself. The loader therefore compiles one script, the engine text cut from the page followed by the harness-only code, as a single function body with the CommonJS arguments (`require, module, exports, __dirname, __filename`), exactly as Node wraps a module. Every name stays in one scope, as now; `require.main === module` still works; the tools that `require('./harness.js')` see the same exports.

The harness's two behavioural differences move into the page behind their existing off-switches (`AUTOMATION_SAMPLER_LEGACY` in `drawAutomationRisk`; the UBI term in `incomeBasketMetrics`, zero unless a comparator sets `p.ubi`). With the switches off, the page computes exactly what it computes now; the page's display-only additions do nothing in Node.

## A prototype, run the same day

`dev/drafts/build_from_page.py` builds such a harness in a scratch copy: it takes from `index.html` the 210 chunks whose names `harness.js` also declares (235 names), in page order, then the harness's own 100 chunks and its command line, and keeps `drawAutomationRisk` and `incomeBasketMetrics` from the harness (standing in for step 1 below). Against the real `harness.js`, at the same commit:

- `validate`: passes (every seed-42 fixture, and the v4.19 legacy check).
- `unit`: 170 of 171 pass; the one failure is the manifest test that needs a git checkout, which the scratch copy is not.
- `testbed 12 release` in Reference, Adverse and Stress (20 years) and `testbed 6 release ref --years=40`: the panels' fingerprints are identical (`dev/tools/panel_hash.py`); the printed tables differ only in one line giving the run time.

So the single copy reproduces the release engine exactly; B1 proper is the clean version of the same thing.

## The plan (if Duke has nothing against it, as d166 records)

1. Move the two harness-only branches into the page's copies (bit-identical: switches off).
2. Split `harness.js` into the loader plus the harness-only code (the 72 declarations and the command line), and have the loader build the engine from `index.html` at start-up. Engine edits from then on are made in `index.html`'s engine section (its banner changes from "ported from harness.js, do not edit here" to "the engine; harness.js reads it from here"); `port_engine.py` retires.
3. Prove nothing moved: `validate` (the seed-42 fixtures and the v4.19 legacy check), `unit` (171 tests), `domtest` (the parity and fingerprint checks keep running, now as a check of the loader), and full-output diffs of `node harness.js testbed 12 release ENV --json=...` (and `--years=40`) before and after, then one 500-seed panel per environment compared by fingerprint (`dev/tools/panel_hash.py`) with the v5.2 files.
4. Only then start the household work (B2 onward) on the single copy.

**Fallback** (only if step 3 shows any difference that cannot be traced and fixed): keep the copy, extend the parity check to every household measure, and record why.

## Cost and risk

Moderate work, all mechanical, and it removes the step most likely to go wrong during a round that touches every module (forgetting to port, or porting a half-finished change). Stack traces from the harness will name the generated script instead of `harness.js` line numbers; the loader passes a file name to keep them readable. Contributors edit the engine in `index.html`, which is large; MODEL_SPEC.md and the section markers keep it navigable.
