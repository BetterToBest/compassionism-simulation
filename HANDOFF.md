# Handoff (Oct 14, 2026, UTC): the visual suite page built

## What shipped
- **The visual suite page** (`suite.html`, "Beyond one poverty line"; ledger step s161). It is stand-alone: no other page links to it and it carries `noindex`. It reads the newest release through `data/manifest.json` and prints every number through `site/findings.js`. Sections: the six BLEI-paper measures, the BLEI ladder year by year, the bottom and the top by backing reading, what the days are made of, participants, four measures side by side, the spread across environments, and limits.
- **Its data**: `release_data.py` copies the suite series into `data/releases/v5.6/suite-20.json` and `suite-40.json` (listed under `explore.suite`). No figure changed and there was no engine change.
- **Checks**: `check_figures.js` block 11 covers 3,804 numbers in 12 views and nothing typed in by hand. `domtest.js` gains Phase 15 (139 checks in all). `set_version.py`, `check_versions.js` and `no_figure_change.py` now cover the page. `site/charts.js` gains `CSC.stack`.
- Report: `dev/reports/v5-33-visual-suite.md`. Decisions: `dev/DECISIONS.md`, Session 11. Progress: `dev/PROGRESS.md`, Session 11.
- All passed before the pull request: validate, unit (222), domtest (139), guard test (identical), check_figures, and `no_figure_change.py compare` (34 moved counts, each allowed with a reason).

## Branch and pull request state
- v5.6 release: branch `claude/nice-fermi-31kcam-v56`, draft https://github.com/BetterToBest/compassionism-simulation/pull/32. CI is green. **Only Duke merges it.**
- Visual suite: branch `claude/magical-einstein-umkin2`, built on the v5.6 branch at a006ded. Draft https://github.com/BetterToBest/compassionism-simulation/pull/33. CI was running at handoff. **It must merge after 32**; until then its diff also shows the release.
- The reports pull request (31) has merged.

## Long jobs in flight
- None. The results token expires 2026-10-17 04:16 UTC.

## Next 3 actions
1. **If 32 or 33 shows red CI or a merge conflict:** fix it on its branch (merge main into it; never rebase) and push. If 32 merges first, merge main into 33's branch.
2. **The CoMSES package and the fact sheet (ledger step s119)**, with every figure traced to the release data (`data/releases/v5.6.json`).
3. **If Duke approves the suite page:** link it from the findings explorer and drop `noindex` (a one-line change each). Domtest Phase 15's "no other page links to it" check must then be changed to expect the link.

## Files to touch
- Suite page: `suite.html` (grep `function indices` / `function floor`), `dev/tools/check_figures.js` (grep `11. session 11`), `domtest.js` (grep `phase15`).
- Release data layout: `dev/tools/release_data.py` (grep `def explore_files`).

## Pitfalls
- `no_figure_change.py` now lists a new data file instead of failing on it. A changed count still needs a line in `dev/tools/no_figure_change_allow.txt`.
- After adding domtest checks, run `node domtest.js --write-counts` (README and CONTRIBUTING quote the count).
- In jsdom, chart legends are also `svg` elements: select `svg.fx-svg` for the drawings.
- No model or assistant names in pushed files. Claude Code's Pro plan ends Thursday.
