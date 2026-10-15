# Handoff (Oct 15, 2026): study s171 built, not yet launched

## What shipped
- **Study s171** (one Runpod study for the open work): `dev/tools/s171_jobs.sh`, `dev/tools/s171_README.md` (what each result file is, and the next steps for a chat without code), `s171` entry in `dev/batch/runpod.sh` pinned to engine commit cfc33228015b7b1f016e9181486588c1d6867aa7.
- Pieces: (A) release panel with project-hours columns (`--hours`: hours a year per participant, share who took project work, hours taken from paid work) in 3 environments, 20 and 40 years; (B) the six-design comparison with today's safety net in every arm (`--snab --slope` now works on the `match` section), under both financing rules; (C) engine reference output for the Python check, seeds 1-500.
- `harness.js` changes are reporting only; the engine in `index.html` is unchanged. A two-seed dry run of all 38 pieces finished.
- The three project-hours keys were already in the engine's key list; the plan note is corrected.

## Branch and pull request state
- Branch `claude/festive-feynman-64homk`, restarted from main after pull request 37 merged. Draft pull request into main is open. CI not yet read. The guard test and domtest were not run locally (CI runs them).

## Long jobs in flight
- None launched. This session has no tool that creates a pod.

## Next 3 actions
1. **Launch the study** on a Runpod pod with 16 or more vCPU: start command from the header of `dev/batch/runpod.sh` with RUNNER = the head of this branch, env `STUDY=s171`, `MAX_HOURS=14`, `GH_TOKEN` = the results secret. Results land in BetterToBest/compassionism-sim-results under `s171-cfc3322/`; a `DONE` file there means all pieces are in; the pod terminates itself. `bash dev/tools/s171_jobs.sh X Y --estimate` prints the time (the comparison pieces are a guess; the 2-seed run uses fixed 60-seed pilots).
2. **Read CI on the pull request**; fix if red (merge main in, never rebase). Duke merges when the report reads right.
3. **When results are in:** a chat follows `dev/tools/s171_README.md` (hours paragraph, compare page Part 1b, Python check); Claude Code then updates `index.html` (grep `rel-flourish`), `compare.html`, runs `python3 dev/tools/sync_earlier.py`, `node domtest.js --write-counts`, `node dev/tools/check_figures.js`.

## Files to touch
- `dev/tools/s171_jobs.sh`, `dev/batch/runpod.sh`, `harness.js` (grep `--hours`, `SNM`), `compare.html`, `index.html`.

## Pitfalls
- The results token expires 2026-10-17 04:16 UTC: a run that ends after that cannot push. Launch today and keep it under that.
- Any edit to `index.html` script needs `python3 dev/tools/sync_earlier.py`. No model names in pushed files.
- If `pjDisp` comes back 0 everywhere, report it as is (project hours add to paid work in this model).

## Ledger updates for Duke
(Ledger write not attempted: little limit left.) s117 doing (study built), s95/s171 doing (study built), s118 doing (500-seed reference in the study); `next`: launch study s171 on Runpod.
