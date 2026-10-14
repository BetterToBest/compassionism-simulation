# Handoff (Oct 14, 2026): links, reading notes, suite defaults and the history check on public pages

## What shipped
- **Links:** "Health Study" on the findings, suite and replication pages (file still `study.html`); Findings and Health Study in the simulation page's header; the study page's navigation matches.
- **Findings page "Reading the measures"** (`findings.html`, `savingsNote` in `site/findings.js`): the wealth paragraph, and the savings-kept-up-with-prices paragraph filled from the release. `release_data.py` adds 30 catalogue figures and `inputs.savRealYield` to `data/releases/v5.6.json`.
- **Suite page** opens at 40 years on "Every dollar backed" with the optimistic-end sentence; still `noindex`, still unlinked.
- **Health Study page:** "Tested against history: 2008 and 2020", from `dev/runs/history/history-check.json` via `dev/tools/study_data.py`; linked from the replication page.
- **CI:** `apply-upload.yml` pinned to ubuntu-24.04. **Tool:** `no_figure_change.py` separates added numbers from moved ones.
- **Checks:** validate, unit 222, domtest 153 (Phase 16 new), check_figures 23, glossary, check_versions, no_figure_change (64 moved counts, all allowed). Engine unchanged. Decisions: `dev/DECISIONS.md`, Session 13; notes: `CHANGELOG.md` "Unreleased".

## Branch and pull request state
- Branch `claude/jolly-lovelace-q2ahoi`, draft https://github.com/BetterToBest/compassionism-simulation/pull/35 into main (subscribed; CI not yet reported at writing). Version stays 5.6.0.

## Long jobs in flight
- None.

## Next 3 actions
1. **Pull request 35:** fix any red CI or conflict (merge main in, never rebase). Duke reads the history section on the study page and merges if it reads right.
2. **Part B, only after Duke approves the suite page:** link `suite.html` from `findings.html`, drop `noindex`, add a canonical link, change domtest Phase 15's "stands alone" check (`dev/plans/suite-v2-plan.md`, section 8).
3. **Then:** the CoMSES package and fact sheet (ledger step s119), or Tier B packet B2 (`dev/plans/tier-b-packets.md`).

## Files to touch
- `dev/tools/study_data.py` (grep `def hist`, `'history'`), `dev/tools/release_data.py` (grep `sav.with`, `save_yield`), `domtest.js` (grep `Phase 16`), `dev/tools/check_figures.js` (grep `session 13`), `suite.html` (grep `optimistic`).

## Pitfalls
- A new number in an existing data file needs an `added` line in `dev/tools/no_figure_change_allow.txt`; wording that adds digits needs `moved` lines.
- The domtest count in README and CONTRIBUTING (153) must follow every new check (`node domtest.js --write-counts`, about 8 minutes).
- The simulation page's "per adult a year" interest in the savings paragraph is large because prices compound; it is the page's existing wording, copied.
- The results token expires 2026-10-17 04:16 UTC. No model or assistant names in pushed files.

## Ledger updates for Duke
(No ledger tool was loaded; please apply in one write to `projects/sim`.)
- Steps done: Health Study link text and simulation-page links; findings "Reading the measures"; suite defaults (40 years, Every dollar backed); history check shown on the study page; apply-upload runner pinned (closes issue i20's last item).
- `next`: "Duke reads the history section on the study page and merges pull request 35; then Part B (link the suite page) if he approves."
- Log: "Oct 14: draft PR 35: Health Study links, findings reading notes, suite defaults, history check on the study page, runner pinned."
