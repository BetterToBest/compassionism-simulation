# Handoff (Oct 13, 2026, afternoon): version 5.5.0 is live; the findings page still lists 5.4 as latest

## What shipped
- No code or page changes this session; it reassessed the plan for Duke's last Claude Pro days (ends Oct 15, time of day unknown).
- Version 5.5.0 (the 500-seed study on `study.html`) is merged and tagged `v5.5.0`; checks and deploy passed on `main`.
- The tracking ledger now orders the remaining sessions and holds six open choices for Duke.

## Branch and pull request state
- `main` is at 6a1ca3e (pull request #23 merged); pull request #15 (wealth-gap sentence) is also merged. No other pull request is open.
- This file is delivered on branch `claude/handoff-findings-label` as draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/24 into `main`; CI not yet reported. Merge it so the next session sees it.

## Long jobs in flight
- None. The last Runpod pod is gone and its results are merged (`dev/runs/s137/`, `dev/runs/s137b/`).

## Next 3 actions
1. Priority: make the findings page show 5.5.0 as the latest release. Cause: `data/manifest.json` has no 5.5 entry, so v5.4 is still marked `"status": "current"`. 5.5.0 changed no engine figure, so the figures stay v5.4's. Read `dev/ADDING-A-RELEASE.md` (36 lines), add the smallest 5.5 entry that says so in plain words, and change no figure. Record the choice in `dev/DECISIONS.md`. Run the three checks; open a draft pull request.
2. Add the "what would have to be true" panel and a sensitivity bar chart to `study.html`, built from the Morris and Sobol results, naming the two constants with no source (CCO relief 20%; PTF and PTH inflation damping 0.5 and 0.1). Add a one-page economist review checklist and a GitHub issue template with the same rows.
3. After 1 and 2 are merged: the plain-language pass over every page and report, with a test that no figure changed. Wording that changes meaning is flagged for Duke as a decision, not applied.

## Files to touch
- Action 1: `data/manifest.json`, `data/releases/v5.4.json` (read only), `dev/tools/release_data.py` (grep `manifest` and line 792, the "release v" note), `findings.html` (grep `figs:headline`; line 83 is very long), `dev/tools/check_versions.js`.
- Action 2: `dev/tools/study_data.py` (tables are built in `content()`), `study.html`, `data/studies/s137.json`, `dev/reports/v5-30-s137-results.md`, `ODD.md`, `.github/ISSUE_TEMPLATE/` (new).
- Action 3: every `*.html` page at the root, `CONTRIBUTING.md` (its open-items table is headed v5.2 and is out of date), `dev/PROGRESS.md` (grep `\[ \]`).

## Pitfalls
- The findings page note "release v5.4 data" is accurate for the figures; the problem is the missing 5.5 entry, not wrong numbers.
- The results token expires 2026-10-17 04:16 UTC. Nothing planned needs it; Duke may let it lapse.
- GitHub GraphQL is blocked here, so `gh pr list` fails; use `gh api repos/BetterToBest/compassionism-simulation/pulls`.
- Pushes to `main` are refused; work on a branch and open a draft pull request.
- `node harness.js unit`, `domtest.js` and `guard_test.js` each take minutes; run them in the background. A new check in `check_figures.js` changes the domtest count: run `node domtest.js --write-counts`.
- `study.html` has had no visual check at 390 px or 1280 px.
- Duke has not yet confirmed the new ledger choices (backtest, compare page, token, split of the old session, fact sheet, findings label); do not assume them.
