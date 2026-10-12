# Handoff (Oct 12, 2026; session 1b)

## What shipped
- The 33 pieces from BetterToBest/compassionism-sim-results (`v54-fe88599/`) merged into the six release panels with `merge_parts.py`; panels, backing chart and six explore exports (500 seeds; self-checks pass) built.
- Version 5.4, release data (`data/releases/v5.4.json`, date 2026-10-12), release notes in CONTRIBUTING.md (v5.3.1's moved to CHANGELOG.md), replication timeline entry, Duke's report `dev/reports/v5-23-v54-release.md`.
- Checks: validate passed, unit 208 run and 0 failed, domtest 125 passed.

## Branch and pull request state
- Session branch `claude/loving-brahmagupta-ygq40l`, head 152ab4c (all of the above), merged into #13's branch as pull request #14 (merge commit 10c8474).
- [Pull request #13](https://github.com/BetterToBest/compassionism-simulation/pull/13) (`claude/awesome-sagan-75dsu9`): marked ready. Waiting for Duke to read the report and merge; the merge is the release. CI on #13 not yet checked by me.
- This HANDOFF.md is on the session branch only, after #14 merged; #13's copy is the older one.

## Long jobs in flight
None. Job A is finished (pod gone, $0.98).

## Next 3 actions
1. Check CI on #13's head; fix anything red (checks are in `.github/workflows/checks.yml`).
2. Find why Reference's 20-year too-little-wealth gap grew (+11.0 vs v5.3's +5.5): compare the `pthbold`, `ptfs25`, `cut0`, `cut20` rows in `dev/runs/release-panel.json`, then add a sentence to the report and notes.
3. After Duke merges #13: confirm the release workflow tagged v5.4; then start Job B (below).

## Files to touch
`dev/runs/release-panel.json` (rows by key), `dev/reports/v5-23-v54-release.md` (the wealth bullet), `CONTRIBUTING.md` (v5.4 notes).

## Pitfalls
- GitHub token for the results repository expires 2026-10-17 04:16 UTC; renew the Runpod secret `github_results_token` before Job B.
- Re-running `release_data.py` rewrites `replication.html`; my timeline entry there was added by hand and may need re-adding.
- The ledger (artifact KMdxWQ5KAefQVFxQA236pV) read was denied by the permission classifier this session.

## Ledger updates for Duke
Mark done: v5.4 500-seed batch (Job A), panel merge, explore exports, version 5.4, release data, notes, report, checks. Set `next`: check CI on #13, then Duke merges. Log: "2026-10-12: v5.4 figures merged and released-ready in #13 (checks pass); #14 merged into #13."
