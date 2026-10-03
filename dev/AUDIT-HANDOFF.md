# Handoff: continue from the v5.0 external audit pass (Oct 2, 2026)

Read `CLAUDE.md`, then this file, then `dev/reports/v5-0-external-audit-pass.md` (the findings and the priority list). The branch rule in `CLAUDE.md` described the pre-release build; since v5.0 shipped, Duke applies sessions as one zip (`apply-*.zip`, a single top-level `sim/` folder) through `.github/workflows/apply-upload.yml`, which runs the three checks and commits to `main` only if they pass. Deliver work that way; a zip may not touch `.github/`.

## Already applied (in `apply-audit-v5.0.zip`)
Live-run worse-off sentence; static version fields plus `dev/tools/check_versions.js` (run by `domtest` Phase 13); Chart.js guard; verdict wording; `aria-live`. Engine untouched; `domtest` 102 checks.

## Next, in order
1. **V5-02 (mechanics release).** Follow `dev/proposals/V5-02-gate-current-year.md` step by step. Bump the version with `python3 dev/tools/set_version.py <new>` and run `node dev/tools/check_versions.js`. Regenerate the 500-seed panels in the three environments at 20 and 40 years, one process per environment (`dev/runs/`), then `merge_panel.py` and `release_figs.py`.
2. **F3, price level.** In `harness.js` `release` JSON output, write the per-seed median and 10th/90th percentiles beside the mean (`r._s.pLev20` is the per-seed array); rename the key (it is `pLev20` even for 40 years); in `relSentences` show the median and the range, and reword when the level exceeds 1,000x ("a model artefact, not a forecast"). Update `domtest` Phase 11 for the new wording.
3. **E1, Hub-target scoreboard.** Add `giniD` (and an extreme-poverty figure; `epPY` exists) to the panel rows, show achieved against Hub targets per environment and horizon, label the target source, add a `domtest` check.
4. **E2, backing-share curve.** Sweep `a` in {0, .25, .5, .75, 1} for the release row (check `n1Row` accepts fractional `a`), draw one static chart, and keep it to 500 paired seeds. Report as it comes out.
5. **E5/V5-08, manifest and wider parity.** `_meta.commit`, SHA-256 of `index.html` and `harness.js`, Node version; extend the behavioural parity check to all 11 rows, 40 years, and a bindings fingerprint (allow-list: `CFG.FED_POVERTY_LINE_1P`, `CFG.FED_POVERTY_LINE_YEAR`, `TIERS` colours and classes).
6. **V5-05, feature-matrix smoke test** in `harness.js unit`: framework alone, then with project, ESP, price, labour, and all modules; assert accounting identities and determinism.
7. **E3, E4, E6.** Front-door CSV/JSON download; `?env=&years=` deep links; generated check counts.

## Guardrails that apply to every step
New mechanisms behind a switch, bit-identical when off (prove with full-output diffs); CRN-paired seeds 1-500 in Reference, Adverse and Stress; `validate`, `unit` and `domtest` on every change; eight draws per agent-year; no constant retuned to a target; results reported as they come out; record every decision in `dev/DECISIONS.md` in plain words; run the page, do not only read it.
