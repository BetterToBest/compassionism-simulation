# Handoff (Oct 13, 2026, evening): findings page lists 5.5; study page panel, chart and review kit are in draft pull request 25

## What shipped
- Release list has a 5.5 entry (plain words: no engine change, figures identical to 5.4, so the 5.4 data stays the data shown); the findings page opens on it, labelled "latest". Duke's choice d200, option 1. No figure or data file changed.
- `study.html`: a "What would have to be true" panel, a sensitivity bar chart (Sobol results, one outcome at a time) and a table naming the two constants with no source (CCO relief 20%; PTF and PTH damping 0.5 and 0.1). Numbers all come from `data/studies/s137.json`.
- `dev/tools/unsourced_check.py` shows the released figures do not use either constant (relief: no line changed; damping: only the optional "two former stand-ins on" row). Result in `dev/runs/unsourced-constants-check.txt`.
- `ECONOMIST-REVIEW.md` (twelve rows) and `.github/ISSUE_TEMPLATE/economist-review.yml`, both written by `dev/tools/review_rows.py`; a check keeps them equal.
- `index.html` and `harness.js` are untouched, so the engine is bit-identical. Decisions are in `dev/DECISIONS.md` (Session 5); the report has a new section 8b.

## Branch and pull request state
- Branch `claude/relaxed-davinci-b6gp1b`, draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/25 into `main`; CI not yet reported (subscribed). Locally `validate`, `unit` (221), `domtest` (130) and `check_figures.js` (16 checks) pass. Merge it: the merge is the release.

## Long jobs in flight
- None.

## Next 3 actions
1. Check pull request 25's CI; fix anything red. Duke reads report section 8b and the panel text, and merges.
2. After 25 is merged: the plain-language pass over every page and report (ledger step s147), with a test that no figure changed (run `node dev/tools/check_figures.js`, `python3 dev/tools/release_data.py --check`, `python3 dev/tools/study_data.py --check` and `node domtest.js` before and after). List wording that changes meaning for Duke as a decision; apply nothing of that kind.
3. History check (s146) only if Duke has attached the Census poverty files; otherwise the free-plan chat packets (s135).

## Files to touch
- Action 2: every `*.html` at the root (grep long lines first), `dev/tools/study_data.py` (the page's words are in `content()`, lines 95 on), `dev/tools/release_data.py` (texts), `CONTRIBUTING.md` (its open-items table is headed v5.2 and is out of date), `dev/PROGRESS.md` (grep `\[ \]`).
- Wording on generated pages is changed in the generator, then regenerated; never edit `data/` by hand.

## Pitfalls
- The two-constants test covers only the Adverse environment, 4 seeds, 8 years; the 500-seed figures are unchanged because no engine line changed.
- The panel's "what would have to be true" wording is Claude's reading of the sensitivity results, not Duke's words; Duke should check it.
- The 5.5 entry has status "latest" and shares the 5.4 data file; the 5.4 entry stays "current". Do not copy the data file (`dev/ADDING-A-RELEASE.md` explains).
- A new check in `check_figures.js` changes the domtest count: run `node domtest.js --write-counts`.
- Playwright for screenshots is at `/opt/node22/lib/node_modules/playwright`, not in the repository.
- `node harness.js unit` and `domtest.js` take minutes each; run them in the background. GitHub GraphQL is blocked: use the pull request tools.
- The results token expires 2026-10-17 04:16 UTC; nothing planned needs it. Pro ends Oct 15.
