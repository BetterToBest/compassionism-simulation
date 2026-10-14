# Handoff (Oct 14, 2026, UTC): study results read; reports and the v5.6 release drafted

## What shipped
- **The study is checked by its files** (`dev/tools/s165_verify.py`): 49 job pieces and 6 merged panels, all 55 files at engine 5bf5bcc on a clean tree with 500 seeds. The pod is gone.
- **History check, 500 seeds** (`dev/reports/v5-34-history-check.md`; file `dev/runs/history/history-check.json`). Direction right. The rise is +6.86 points against +2.6 official (about 2.6 times). The peak comes in 2012 against 2010 (does not match). The safety net absorbs 0.48% against 73%: the file says "same direction, different size", and the report calls it a miss in substance.
- **Safety-net trace, 500 seeds** (`dev/reports/v5-35-safety-net-poverty.md`, section 5; `dev/runs/sn/sn-trace-*.json`). The rise is still mostly the work response. With the fix on: −0.08 at Reference, −0.26 in Adverse, +0.48 in the Stress Test.
- **The v5.6 release draft** (version 5.6.0; report `dev/reports/v5-34-v56-release.md`). The gain moves by less than 1 point for adults and 0.7 to 1.7 for children, and no result changes sign. The SNAP work rule moves it by at most 0.07 points; nearly all of the move is today's safety net.
- Decisions are in `dev/DECISIONS.md`, Session 10 (one section on each branch).

## Branch and pull request state
- Reports: branch `claude/nice-fermi-31kcam`, draft https://github.com/BetterToBest/compassionism-simulation/pull/31. CI is green. Duke can merge it.
- v5.6 release: branch `claude/nice-fermi-31kcam-v56`, head bce176e, draft https://github.com/BetterToBest/compassionism-simulation/pull/32. Its CI was running at handoff, and all local checks passed. **Only Duke merges it** (issues i23 and i24-2). Never merge it ourselves.
- Both pull requests add a section at the end of `dev/DECISIONS.md`. Whichever merges second needs main merged into it, keeping both sections.

## Long jobs in flight
- None. The results token expires 2026-10-17 04:16 UTC.

## Next 3 actions
1. **If either pull request shows red CI or a merge conflict:** fix it on its branch (merge main into it; never rebase) and push.
2. **The visual suite page (ledger step s161):** start a new branch from main, or from the v5.6 branch if 32 is not merged yet. It reads `data/manifest.json` and the latest release. Its extra data is under `suite` in `dev/runs/explore-ENV-YEARS.json` on the v5.6 branch; `release_data.py` does not copy it into `data/releases/`. Stand-alone page, not linked from the others; no engine change.
3. **Then the CoMSES package and the fact sheet (ledger step s119)**, figures traced to the release data.

## Files to touch
- Visual suite: a new page, plus `site/findings.js` (number printing), `domtest.js` (add the page), and `dev/tools/check_figures.js` (grep `5c. the explorer`). Report: `dev/reports/v5-33-visual-suite.md`.
- Release data layout: `dev/tools/release_data.py` (grep `def explore_files`).

## Pitfalls
- The study did not rerun the attribution runs or the US-data check. v5.6 carries v5.3's, and the pages say so.
- After any `index.html` edit, run `python3 dev/tools/sync_earlier.py`. After a version change, run `python3 dev/tools/release_data.py --check`.
- When running checks in the background, set shell variables inside each backgrounded group, or the logs land in `/`.
- No model or assistant names in pushed files. Claude Code's Pro plan ends Thursday.
