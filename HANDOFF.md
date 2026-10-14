# Handoff (Oct 14, 2026, early morning): clarity answers in pull request 27; SNAP's work rule, the visual-suite export and the study job in pull request 28

## What shipped
**Pull request 27** (wording only, no figure; branch `claude/wonderful-fermat-ukn1ph`). Ledger step s160 and issue i20. One commit per decision:
- **d201 with d213:** the study page's damping row and the economist checklist now say "applied to the overall inflation rate". Duke's d201 pick said PTH "holds rents down"; the engine has no rent mechanism behind that constant. Explained in `dev/reports/v5-32-clarity-answers.md`, section 1.
- **d202:** the second BLEI reading is now the "same-rules reading", defined where each page first shows it, with "earlier called design-neutral".
- **d204:** the findings page has the front page's glossary, from one source (`site/glossary.json`, `dev/tools/glossary.py --check` in CI).
- **d206:** the old open-items table and progress boxes are marked as historical records.
- **d207:** the "What would have to be true" panel is labelled Claude's reading, and the economist checklist has a row 13 for it.
- **i20:** CI is pinned to ubuntu-24.04, Node 22.22.0 and Python 3.13.
- **d203 (last):** US spelling.
- **d205:** no change, as decided.
- **Tools:** `no_figure_change.py` now fingerprints the engine exactly as harness.js runs it, and counts the numbers in the page code.

**Pull request 28** (no figure, no page change; branch `claude/wonderful-fermat-ukn1ph-snap`). Ledger steps s166 and s164:
- **SNAP's work rule** behind `SNET.abawd`, off by default. Each element was checked against 7 U.S.C. 2015(o) as amended by Public Law 119-21 sec. 10102 and USDA's Oct 2025 memos (`sources/snap_work_rule.md`). No random draw is added. Report: `dev/reports/v5-33-snap-work-rule.md`.
- **The explore export** for the visual suite: `explore_export.js --suite [--sn|--snab] [--panel=] [--out=]`. Two-seed smoke tests only.
- **The study job:** `dev/tools/s165_jobs.sh`, with `STUDY=s165` in `dev/batch/runpod.sh` and the engine pinned at c88c1e0. Estimate: about 37 core-hours, about 2.6 hours on a 16-vCPU pod (`--estimate`). A full dry run with 2 seeds passed.
- **New harness flags:** `testbed release|backing --sn/--snab`. `snap_rule_check.js --out/--years`.

## Checks (final commits)
- **Pull request 27:** `no_figure_change.py compare` against main at the merge of #26 passes (21 moved number counts, all listed in `no_figure_change_allow.txt`). `harness.js validate` passes. `check_figures.js` passes 16 of 16. The release_data, study_data, review_rows and glossary checks pass. `domtest.js` passes 130 of 130. CI on the pinned runner is green (checks and guard).
- **Pull request 28:** `guard_test.js` is identical (25 rows × 20 seeds × 483 outputs, three environments). `snap_rule_check.js` is identical with the rule off (the safety-net rows, which the guard test lacks; reference made before the edit). `harness.js unit` passes all 222 (the new SNAP test by hand included). The engine_lineage proof, validate, domtest, check_figures and no_figure_change results are in pull request 28's description.

## Decisions taken this session (all in dev/DECISIONS.md, Session 7)
- **The no-figure test's engine check.** Now the engine harness.js runs, plus a count of every number in the page code. Reason: so wording in page code can change while the engine stays byte-checked.
- **d201 wording follows d213.** Reason: the code damps overall inflation; no rent mechanism uses the constant.
- **SNAP rule modelling choices** (report v5-33, section 2): the yearly clock; unemployment insurance weeks exempt; under half of full time counts as not meeting the test; retirees exempt (the cautious choice); State exemptions as an expected 8%; no area waivers (the model's unemployment rate stays under 10%).
- **The study measures the rule's own effect beside the full panel.** Reason: see the open item below.

## Open: for Duke
1. **Read** `dev/reports/v5-32-clarity-answers.md` (section 1, d213), **then merge pull request 27** if it reads right.
2. **New finding (report v5-33, section 5): the published main results have no today's safety net (SNAP, EITC, CTC) in either arm.** d209's note assumed they did. A v5.6 "with the SNAP rule" therefore also adds the safety net, which moves figures on its own. On 20 seeds, basket poverty with Compassionism moves +0.11 (Reference), −0.20 (Adverse) and +0.54 (Stress); the no-program run moves +0.03 to +0.04. The safety net slightly *raising* basket poverty needs explaining before any release; the likely cause is its own work response. It belongs to issue i23.
3. **Pull request 28:** read `dev/reports/v5-33-snap-work-rule.md`. Merging it changes no figure. The study can run from its branch either way: the pod clones every branch.

## Long jobs in flight
- None. No 500-seed job was started.

## Next 3 actions
1. **Wednesday evening, s165:** launch the Runpod study with `STUDY=s165`, using the runner commit = pull request 28's head. Check once that it started, then end the session.
2. **Thursday, s167:** read the results; write the v5.6 release report setting the safety-net effect, the rule's own effect and v5.5 side by side. Duke decides i23.
3. **Thursday, s161:** build the visual suite on the s165 export, or on the v5.5 export if the study is late.

## Files to touch
- **s165:** `dev/batch/runpod.sh` (pod start command in its header), `dev/tools/s165_jobs.sh`. Results go to BetterToBest/compassionism-sim-results, folder `s165-c88c1e0/`.
- **s167:** `dev/tools/merge_panel.py`, `dev/tools/release_data.py`, `dev/tools/set_version.py`. The export file is named `explore-suite-ENV-YRS-snab.json`; release_data reads `explore-ENV-YRS.json`, so map the name. The suite file holds the bands, deciles and lives too.

## Pitfalls
- **Wording passes:** `python3 dev/tools/no_figure_change.py snapshot before.json` before the first edit, then `snapshot after.json` and `compare`. Wording in index.html's script is allowed; the engine and the embedded data are not. Any edit to index.html's main script needs `python3 dev/tools/sync_earlier.py`, or domtest fails ("same script").
- **Running explore_export.js without `--suite` or `--out`** overwrites the published `dev/runs/explore-ENV-YRS.json`.
- **Runtimes:** `node harness.js unit` and `domtest.js` take minutes; run them with the shell's background option, not with `&` (a plain `&` job dies with the shell). GitHub GraphQL is blocked: use the pull request tools.
- **The results token expires 2026-10-17 04:16 UTC.** Pro ends Oct 15.
