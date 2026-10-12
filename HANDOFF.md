# Handoff (Oct 12, 2026; session 1c)

## What shipped
- CI checked: pull request #13 (v5.4) merged into main as 270348b. Checks, release and pages workflows are all green, and the v5.4 tag exists.
- Found why Reference's 20-year too-little-wealth gap grew from +5.5 to +11.0 points (`dev/runs/release-panel-ref.json`, rows `cut0`, `cut20`, `pthbold`, `ptfs25`, `v53`). Most of it is the 10% lower pay on return to work: with no cut the gap is +6.6, with 10% +11.0, with 20% +15.7. For each 10% of pay, the programme run rises about 6 points and the no-programme run 1.4. The PTH and PTF rules move it less than 0.3.
- One sentence each added to `dev/reports/v5-23-v54-release.md` (the wealth bullet) and `CONTRIBUTING.md` (v5.4 Figures line). Commit 5b08a47. Validate passed, unit 208 run 0 failed, domtest 125 passed, versions match.
- Duke asked for a note on reading the wealth measure (a guaranteed minimum means people need a savings reserve less). Added as v5.4.1, words only. The note, "How to read this measure", sits under the Savings result on the release page (`index.html` `relSentences`, id `rel-wealth-frame`). It gives his framing and cites Hubbard, Skinner and Zeldes (1995). It also states that the model has no such behaviour: the spending share is the same in both runs. Also: report `dev/reports/v5-24-wealth-measure-reading.md`, DECISIONS session 1c, v5.4.1 notes (CONTRIBUTING; v5.4's moved to CHANGELOG), and a replication timeline entry. The engine block is unchanged, so no lineage proof was needed.

## Branch and pull request state
- Session branch `claude/beautiful-wozniak-lqpv4t` started from main (270348b). Head 5b08a47, plus this handoff.
- Draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/15 into main. It now carries v5.4.1 (words only; merging it is the release, and the workflow tags v5.4.1). Its CI had not reported when this was written. The session is subscribed to its events.

## Long jobs in flight
None. Job A (v5.4) is finished, and its pod is gone.

## Next 3 actions
1. Check CI on #15 and fix anything red. When it is green, mark it ready so Duke can merge. After the merge, confirm the release workflow tagged v5.4.1.
2. Session 2a (ledger step "Session 2a: guard test, today's-safety-net row, and single payer"), engine work only, in this order. (a) Build a guard test: rerun 20 fixed seeds on the v5.4 engine (main, 270348b) and fail if any figure changes. Make its reference before editing the engine. (b) Add the stylised current-US-policy row (SNAP, EITC, Child Tax Credit, with children modelled) to the comparison engine. (c) Add health setting B: single payer, public plan only, behind a switch, with central, cautious and costs-run-higher cases. (d) Test with 20 runs per setting, commit, then hand off. No long runs.
3. Optional, if time is left: find why the programme run reacts about four times as strongly to the pay cut. Compare `medWealth`, `pov`, `srcPay`, `tau` and `infl` on rows `cut0`, `release` and `cut20` (`dev/runs/release-panel-ref.json`), and read the re-employment code (`index.html`, grep `_emCut`). Then refine the report sentence.

## Files to touch
`harness.js` and `index.html` (grep `REL_V54`, `relMainCfgs`, `_emCut`; never read whole) · `dev/DECISIONS.md` (append; never read whole) · `dev/PROGRESS.md` (grep `^- \[ \]`) · `dev/tools/engine_lineage.js` (`prove`) · `dev/reports/v5-23-v54-release.md` line 26 and `CONTRIBUTING.md` line 51 (action 3 only).

## Pitfalls
- The GitHub token for the results repository expires 2026-10-17 04:16 UTC. Renew the Runpod secret `github_results_token` before any new Runpod job.
- The three checks together take more than 10 minutes. Run them in the background.
- Re-running `release_data.py` rewrites `replication.html`, and its v5.4 timeline entry was added by hand.
- Ledger artifact KMdxWQ5KAefQVFxQA236pV, document `projects/sim` (about 280 KB): read it to a file with `out_dir` and query it with Python. That worked this session.
- Session 2a's health setting may use a country comparison that Duke attaches (ledger step "Optional, saves tokens"). Spot-check five of its figures against their sources before using any of them.
