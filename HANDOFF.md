# Handoff (Oct 13, 2026, night): the plain-language pass (ledger step s147) is in draft pull request 26; no figure changed

## What shipped
- Wording only, seven commits on the session branch. Findings page text (written by `dev/tools/release_data.py`), study page text (`dev/tools/study_data.py`), front page text in `index.html` (its scripts are byte-identical), `findings.html`, chart row names in `site/findings.js`, `README.md`, and the economist checklist (`dev/tools/review_rows.py`, regenerated).
- New test `dev/tools/no_figure_change.py`: engine fingerprints, a fingerprint of every number in the 34 data files, and the count of each number in the words of 103 files. All identical except 8 named, expected moves (`dev/tools/no_figure_change_allow.txt`).
- The four checks in the old handoff pass before and after: `check_figures.js` (16), `release_data.py --check` (14 files), `study_data.py --check` (9 tables), `domtest.js` (130). `harness.js validate` and `unit` (25 suites) also pass.
- Report `dev/reports/v5-31-clarity-pass.md`: what changed, the test results, and seven wording questions for Duke (section 3), none applied. Decision recorded in `dev/DECISIONS.md` (Session 6).
- Notes added to `CONTRIBUTING.md` and `dev/PROGRESS.md` saying their open-item lists are out of date.

## Branch and pull request state
- Branch `claude/bold-pasteur-57cczu`, draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/26 into `main` (subscribed). CI not yet reported. Merge it when the report reads right; the merge is the release.

## Long jobs in flight
- None.

## Next 3 actions
1. Check pull request 26's CI and fix anything red. Duke reads `dev/reports/v5-31-clarity-pass.md`, section 3, and answers the seven questions (the first, about what the damping constant belongs to, matters most).
2. If Duke has attached the Census poverty series (ledger step s156): the history check, step s146. Otherwise the free-plan chat packets, step s135, including `dev/background/ledger-export.md`.
3. Once Duke answers section 3: apply the approved wording changes in the generators (`study_data.py` unsourced table first), regenerate, and rerun `no_figure_change.py compare`.

## Files to touch
- Action 3: `dev/tools/study_data.py` (grep "inflation damping"), `dev/tools/review_rows.py` (row 2), `dev/tools/release_data.py` (grep "design-neutral" if defined), `site/findings.js` (grep "design-neutral").
- Action 2: `dev/background/` (new `ledger-export.md`).

## Pitfalls
- Before any wording pass: `python3 dev/tools/no_figure_change.py snapshot before.json`; after: `snapshot after.json`, then `compare before.json after.json`. A new number in the words needs a line in `dev/tools/no_figure_change_allow.txt` with a reason.
- Wording on generated pages is changed in the generator, then regenerated; never edit `data/` by hand. Release data for v5.0 to v5.3 is an archive and was left alone.
- Left unrewritten on purpose: `earlier-engine.html` (frozen) and the technical body of `replication.html` (about 60,000 words).
- The study page and the economist checklist now disagree on what PTH is (health programmes versus community housing) until Duke answers question 1.
- `node harness.js unit` and `domtest.js` take minutes each; run them in the background. GitHub GraphQL is blocked: use the pull request tools.
- The results token expires 2026-10-17 04:16 UTC; nothing planned needs it. Pro ends Oct 15.
