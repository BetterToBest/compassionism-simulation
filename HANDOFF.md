# Handoff (Oct 16, 2026, later): compare page restyled and reordered; history section removed from study page

- compare.html: body now has class `fx` (the shared stylesheet's colours were missing, which is why it looked unstyled); hero and footer match the other pages; Part 1 = current-engine six designs (latest data), Part 2 = today's safety net, Part 3 = earlier engine v4.22 (with the Core note); table row names rewritten in plain words (the duplicate "main row" in Adverse/Stress was the price-damping variant, now named).
- study.html: "Tested against history: 2008 and 2020" section removed (generator `dev/tools/study_data.py`, `data/studies/s137.json` regenerated, `domtest.js` and `check_figures.js` checks replaced, replication.html link now points to the findings page).
- Ledger copy `dev/background/ledger-open-items-oct15.md` updated for s117, s95, s171 (done) and s118 (blocked). The claude.ai ledger artifact itself was not edited: copy those four lines in.
- s118 NOT done: `python-reference-500.json` is in the results repo (s171-cfc3322) but there is no Python program in this repository. Next chat: save the chat's `s118_loop.py` under `dev/reports/s118-independent-implementation/`, run seeds 1-500 for the five presets, compare per the brief.
- Not read: `node domtest.js` and `node dev/tools/check_figures.js` were started; CI runs them. Duke merges when the pull request reads right.

---
Older handoff:
# Handoff (Oct 16, 2026): study s171 finished; page updated

- Study s171 DONE (results: BetterToBest/compassionism-sim-results, folder s171-cfc3322). `index.html` hours paragraph (rel-flourish) and `compare.html` Part 1b written from it; `sync_earlier.py` and `check_figures.js` (154 pass) run. `node domtest.js` was started but not read: CI runs it; if counts differ run `node domtest.js --write-counts`.
- Hours result: project hours 15.0 / 11.7 / 1.9 a year (Reference / Adverse / Stress, 20 years); hours taken from paid work 0 everywhere.
- Still to do: s118 Python check against `python-reference-500.json` (rule in `dev/packets/s118-brief.md`); read CI; Duke merges. 40-year match tables are not on the page (linked only). Ledger not updated.

---
Older handoff:
# Handoff (Oct 15, 2026): study s171 built, not yet launched

## What shipped
- **Study s171** (one Runpod study for the open work): `dev/tools/s171_jobs.sh`, `dev/tools/s171_README.md` (what each result file is, and the next steps for a chat without code), `s171` entry in `dev/batch/runpod.sh` pinned to engine commit cfc33228015b7b1f016e9181486588c1d6867aa7.
- Pieces: (A) release panel with project-hours columns (`--hours`: hours a year per participant, share who took project work, hours taken from paid work) in 3 environments, 20 and 40 years; (B) the six-design comparison with today's safety net in every arm (`--snab --slope` now works on the `match` section), under both financing rules; (C) engine reference output for the Python check, seeds 1-500.
- `harness.js` changes are reporting only; the engine in `index.html` is unchanged. A two-seed dry run of all 38 pieces finished.
- The three project-hours keys were already in the engine's key list; the plan note is corrected.

## Branch and pull request state
- Branch `claude/festive-feynman-64homk`, restarted from main after pull request 37 merged. Draft pull request into main is open. CI not yet read. The guard test and domtest were not run locally (CI runs them).

## Long jobs in flight
- LAUNCHED Oct 15, 2026 22:32 UTC: Runpod pod 7yzaxvjm0tbraq (32 vCPU cpu3c, $0.96/h, EUR-IS-1), STUDY=s171, MAX_HOURS=14, runner commit ab49ab428a6c. Expected about 4-6 hours; it terminates itself. Done when `s171-cfc3322/DONE` exists in BetterToBest/compassionism-sim-results. If the pod is gone with no DONE, relaunch the same way (resumes). A duplicate pod was terminated.

## Next 3 actions
1. (Done: launched, see above.) **Launch the study** on a Runpod pod with 16 or more vCPU: start command from the header of `dev/batch/runpod.sh` with RUNNER = the head of this branch, env `STUDY=s171`, `MAX_HOURS=14`, `GH_TOKEN` = the results secret. Results land in BetterToBest/compassionism-sim-results under `s171-cfc3322/`; a `DONE` file there means all pieces are in; the pod terminates itself. `bash dev/tools/s171_jobs.sh X Y --estimate` prints the time (the comparison pieces are a guess; the 2-seed run uses fixed 60-seed pilots).
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
