# Handoff (Oct 13, 2026; session 2f, ledger step s137: results in, follow-up Sobol running)

## What shipped
- The s137 study finished (11:36 UTC); all 187 output hashes match; merged outputs copied to `dev/runs/s137/` (2.6 MB; the per-seed pieces stay in the results repository, folder `s137-a3582e2/`).
- Morris noise check read: the leaders are the same in both seed blocks for every Stress outcome, but Stress also names tax, eps, pthUptake, maxMult and ptfOther, which the first Sobol left out. The pre-set rule therefore calls for a follow-up Sobol (`dev/DECISIONS.md`, "Session 2f").
- `dev/tools/gsa.js`: new mode `sobjoin` joins Sobol runs on seed blocks and adds 95% bootstrap intervals (tested: equals one run to 2e-14). New job `dev/tools/s137b_jobs.sh`; `dev/batch/runpod.sh` gains `STUDY=s137b`. The engine is unchanged (`index.html` identical to a3582e2). validate, unit and domtest all pass.

## Branch and pull request state
- Branch `claude/handoff-next-action-advycj` from main f371708 (pull request #20 merged). Draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/21 into `main`; CI not yet reported at handoff. Duke merges it (tools and results only, no page change).

## Long jobs in flight
- Pod `lf78qp1tncv9hb` ("s137b-sobol"; cpu3c, 16 vCPU, $0.48/h, EU-CZ-1, image `node:22.22.0-bookworm`), created 18:14 UTC Oct 13. Runner b0a36f8, engine 41f2361, `STUDY=s137b`, `MAX_HOURS=3` (at most about $1.44). The log showed "results repository: HTTP/2 200" at 18:14:42.
- Sobol in Stress: 11 inputs, N=128, 32 seeds in 16 blocks of 2 (about 30-60 minutes). Results land in BetterToBest/compassionism-sim-results, folder `s137b-41f2361/`. It is done when `DONE` is there, and the pod then terminates itself. Relaunching the same settings resumes and skips finished blocks.

## Next 3 actions
1. Check `s137b-41f2361/DONE` in the results repository (clone it read-only) and check that the Runpod pod list is empty. If `DONE` is present and the pod is still there, terminate it.
2. Copy `gsa-sobol-st.json`, `sobjoin-st.log`, `status.txt`, `run.txt` and `SHA256SUMS` to `dev/runs/s137b/`, then check the hashes.
3. Write `dev/reports/v5-30-s137-results.md`, framed as under "Fix later, E" in `dev/reports/v5-29-outside-audit.md`: results conditional on the Yale preprint; poverty and government cost in separate tables; captions. Sources: `dev/runs/s137/` (health tables `s137table-*.json`, price channel `s137flat-*`/`s137thx-*`, Morris `gsa-morris-*.json`) and the new Sobol with its intervals. Report the first Sobol's noise (negative S values).

## Files to touch
`dev/runs/s137/*.log` (one-line summaries), `dev/tools/gsa.js` (grep `sobjoin`), `dev/tools/health_check.js` (grep `MERGE`), `dev/reports/v5-29-outside-audit.md` (grep `Fix later`), `dev/DECISIONS.md` (grep `Session 2f`), `dev/PROGRESS.md` (last section).

## Ledger
- Updated (version 396): s137 stays "doing" with a session 2f note; next, phase and a log line set.

## Pitfalls
- The first create in EUR-IS-1 with a 20 GB disk failed ("no instances available") although the catalog showed HIGH stock; the default disk with EUR-IS-1 or EU-CZ-1 worked.
- A pod can read RUNNING with no logs (the container never started): check for the `[runpod.sh` line within 10 minutes.
- The results token expires **2026-10-17 04:16 UTC**. Renew it and update the Runpod secret `github_results_token` before any later run.
- Each Sobol or Morris block needs two or more seeds. Pro ends after Oct 18.
