# Handoff (Oct 13, 2026; session 2e, ledger step s137: the 500-seed study relaunched and running)

## What shipped
- The s137 study (health check, 500 seeds; Morris sensitivity with its noise check; Sobol in Stress) is running on Runpod; no code change this session.
- The fix for the stuck pod: the official image `node:22.22.0-bookworm` (has bash, git, curl and the pinned Node) in data center EUR-IS-1, in place of `runpod/base:1.0.2-ubuntu2204` in EU-RO-1.
- `HANDOFF.md` and `dev/PROGRESS.md` (session 2e line) updated.

## Branch and pull request state
- Branch `claude/gallant-lovelace-mj922v`, restarted from main 3000ae6 (pull request #19 merged). This handoff goes in a draft pull request into `main`; Duke merges it (no engine or page change).

## Long jobs in flight
- Pod `e61osh5oyurspn` ("s137-study"; cpu3c, 16 vCPU, $0.48/h, EUR-IS-1, image `node:22.22.0-bookworm`), created 10:30:01 UTC Oct 13. Runner commit 3000ae6; engine pinned at a3582e2 (`STUDY=s137`, `MAX_HOURS=5`, so at most about $2.40).
- Checked: the container log printed "results repository: HTTP/2 200; token expiry: 2026-10-17 04:16:25 UTC", and CPU use read 1533% (all cores busy).
- Results land in BetterToBest/compassionism-sim-results, folder `s137-a3582e2/`. It is done when the file `DONE` is there. The pod then terminates itself. If the folder holds `status.txt` without `DONE` after 5 hours, the run stopped at the time cap; relaunching the same pod settings resumes it and skips finished pieces.

## Next 3 actions
1. Check `s137-a3582e2/DONE` in the results repository, and check on Runpod that the pod list is empty. If the pod is still there with `DONE` present, terminate it.
2. Copy the folder to `dev/runs/s137/` and check `SHA256SUMS`. Then read the Morris noise check (`gsa-morris-ENV.json`: `leaders`, `check`). If the leaders differ from part, bu, rho, spend, payCut and bleiBonus, run a follow-up Sobol on the new leaders (on Runpod).
3. Write `dev/reports/v5-30-s137-results.md` with the framing under "Fix later, E" in `dev/reports/v5-29-outside-audit.md`: results conditional on the Yale preprint; poverty and government cost in separate tables; captions.

## Files to touch
`dev/tools/s137_jobs.sh` (lines 1-41: output names), `dev/tools/gsa.js` (grep `morrisjoin`), `dev/tools/health_check.js` (grep `MERGE`), `dev/reports/v5-29-outside-audit.md` (grep `Fix later`), `dev/PROGRESS.md` (last section), `dev/DECISIONS.md` (grep `Session 2d`).

## Pitfalls
- A pod can read RUNNING with no runtime and no logs. That means the container never started (the EU-RO-1 pod with the `runpod/base` image did this). Within 10 minutes, check the logs for the line starting `[runpod.sh`.
- The results token expires **2026-10-17 04:16 UTC**. Renew it and update the Runpod secret `github_results_token` before any later run.
- The image used for the Oct 12 run was not recorded anywhere. Record the image and data center for every pod from now on.
- Each piece needs two or more seeds (`--lo` fails on a piece of one seed).
- Pro ends after Oct 18, so sessions are scarce.
