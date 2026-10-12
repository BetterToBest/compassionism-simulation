# Handoff (Oct 12, 2026, 19:00 UTC; end of session 1 of the last Pro week)

## What shipped
- Token kit: `CLAUDE.md` (sessions start here), `/handoff` (`.claude/commands/handoff.md`), a startup hook that installs jsdom (`.claude/settings.json`).
- Runpod batch: `dev/tools/v54_jobs.sh` (one piece per core, `--max-hours`, `ON_DONE` hook, still resumes) and `dev/batch/runpod.sh` (pinned engine, pushes each piece, writes DONE, terminates the pod).
- Smoke test passed: the push was accepted (`smoke-20261012T184609Z.txt`), the pod terminated itself and billing showed $0.00.
- Timing (20 seeds on one core): 48 s per seed at 40 years, 25 s at 20 years, 2 s for backing, so the batch is 31.4 core-hours.

## Branch and pull request state
- Session branch `claude/loving-brahmagupta-ygq40l` (on top of #13's head fe88599). Draft PR https://github.com/BetterToBest/compassionism-simulation/pull/14 goes into #13's branch.
- Draft PR https://github.com/BetterToBest/compassionism-simulation/pull/13 (`claude/awesome-sagan-75dsu9`, head fe88599): v5.4, waiting for the figures.

## Long job in flight: Job A (the v5.4 500-run batch)
- Pod `3kk175fnxz7qvs`: cpu3c, 16 vCPU, $0.48/h, EU-SE-1. Started 18:57 UTC on Oct 12, hard stop after 7 h. Expected about 2.3 h and $1.22.
- Pinned engine commit `fe88599f9d2f4d26651f6e01370454206257beab`, runner commit `097d13879e5fa79857bdd7d2c0b8b9ae5b1532c6`.
- Results: BetterToBest/compassionism-sim-results, branch main, folder `v54-fe88599/` (33 pieces, `status.txt`, `run.txt`, logs).
- **It is done when `v54-fe88599/DONE` exists.** If the last commit there says `stopped before the end` and there is no DONE, relaunch the same pod command: finished pieces are skipped.
- At launch no piece had arrived yet. The first was due about 20:05 UTC, so check that the folder exists.

## Next 3 actions (session 1b)
1. `git clone https://github.com/BetterToBest/compassionism-sim-results`. Confirm `v54-fe88599/DONE` and that `run.txt` names engine fe88599. Confirm the Runpod pod list no longer has `3kk175fnxz7qvs`.
2. Copy the pieces to an output folder. Run `python3 dev/tools/merge_parts.py OUT ENV 40 6 dev/runs/release-panel-40-ENV.json` and `... ENV 20 4 dev/runs/release-panel-ENV.json` for ref, adv and st. Copy `backing-share-ENV.json` to `dev/runs/`.
3. Do the rest of `dev/PROGRESS.md`, "Next session: start here", steps 3-5: merge_panel, explore_export, set_version 5.4, release_data, notes, report, the three checks. Then merge #14 into #13 and mark #13 ready.

## Files to touch
- `dev/PROGRESS.md` lines 183-191 (the steps), `dev/tools/merge_parts.py`, `dev/tools/merge_panel.py`, `dev/tools/explore_export.js`, `CONTRIBUTING.md`, `CHANGELOG.md`, `dev/reports/v5-23-v54-release.md` (new).

## Pitfalls
- **The GitHub token expires 2026-10-17 04:16 UTC.** Session 3's Runpod job (Job B) needs a renewed token if it runs later. Update the Runpod secret `github_results_token` with the new value.
- Merge on #13's branch with a clean worktree. The engine must stay fe88599's, or the manifests read dirty.
- The `runpodctl` on `runpod/base` uses `remove pod`; `pod delete` is unknown there (runpod.sh tries both).
- This session cannot read the results repository through the GitHub tools. Clone it (it is public).
