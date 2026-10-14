# Handoff (Oct 14, 2026, UTC): safety-net question answered; history check built; the study is running on Runpod

## What shipped
- **Issue i24-1 answered (not a bug, mostly behaviour):** as benefits phase out, people near the cost-of-living line work 3-4% fewer hours, so some land just below it while the depth of poverty falls. A smaller part is essential prices rising as the poorest buy more. Report `dev/reports/v5-35-safety-net-poverty.md`; tool `dev/tools/sn_v54_trace.js`; 20-seed results `dev/runs/sn/`.
- **One small flaw fixed behind a switch:** SNAP's income limit leaked into the marginal rate (up to 90% on all earnings for households near the limit). `SNET.slope` (off by default) reads the true slope; −0.05 to −0.12 points with Compassionism. On in every safety-net run of the study (`--slope`).
- **History check built (ledger s146):** plan section 8 committed (8e5faf0) before any run; engine switch `REC_SCRIPT` (off by default); tool `dev/tools/history_check.js`; draft report `dev/reports/v5-34-history-check.md` with 20-seed smoke figures (direction right; rise about 3 times the official and 2 years late; the model's safety net absorbs almost none of it, data about 73%).
- **Proofs:** guard test and SNAP-rule guard identical; engine lineage link recorded (six 12-seed panels identical); validate, unit (222), domtest (130/130), glossary all pass. Decisions in `dev/DECISIONS.md`, Session 9.
- **Study job:** `dev/tools/s165_jobs.sh` gains the history check and the safety-net trace as resumable pieces, `--slope` everywhere, the broken history hook replaced; estimate 38.8 core-hours, about 2.7 h on 16 vCPU. Engine re-pinned c88c1e0 → 5bf5bcc; 2-seed dry run of the whole job passed (54 pieces).

## Branch and pull request state
- Branch `claude/pensive-einstein-93s0r1`, draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/30 into `main` (no page or figure change). CI runs on each push; check its state on the pull request. Pull request 29 is merged.

## Long jobs in flight
- **Runpod pod objddch5qd3pa8** (cpu3c, 16 vCPU, $0.48/h, EU-RO-1, image node:22.22.0-bookworm), created 04:16 UTC Oct 14. Engine 5bf5bcc, runner 1125516, `STUDY=s165 MAX_HOURS=5`. First log line 04:16:53 (results repository HTTP 200). Results go to BetterToBest/compassionism-sim-results, folder `s165-5bf5bcc/` (status.txt, run.txt, then each piece). Done when `s165-5bf5bcc/DONE` exists; the pod then terminates itself. If DONE is missing after 5 hours, read status.txt: a rerun of the same pod command resumes.

## Next 3 actions
1. **Check the study once:** `s165-5bf5bcc/DONE` and status.txt in the results repository; confirm the pod list is empty (Runpod). If pieces are missing, relaunch with the same command (header of `dev/batch/runpod.sh`, runner 1125516) before the Pro plan ends (Thursday).
2. **Fill in the 500-seed figures:** copy `history-check.json` and `sn-trace-*.json` into `dev/runs/history/` and `dev/runs/sn/`; replace the 20-seed tables in `v5-34-history-check.md` (section 1, verdicts from the file, no change to bands) and give the two 500-seed lines in `v5-35-safety-net-poverty.md` (section 5).
3. **Then the v5.6 work (ledger s167, s161), only if Duke still wants it:** the release file from the merged panels (`release_data.py`), `set_version.py 5.6.0`, then the visual suite page.

## Files to touch
- Action 2: `dev/reports/v5-34-history-check.md` (section 1 table, section 2), `dev/reports/v5-35-safety-net-poverty.md` (section 5).
- Action 3: `dev/tools/release_data.py`, `dev/tools/set_version.py`, `dev/PLAN.md` (grep `s167`).

## Pitfalls
- The results token expires **2026-10-17 04:16 UTC**; Claude Code cannot launch another pod after the Pro plan ends (Thursday). This session's GitHub access reaches only this repository, not the results repository (read it from a session that has it, or ask Duke).
- `earlier-engine.html` must be resynced (`python3 dev/tools/sync_earlier.py`) after any engine edit, or domtest fails.
- Compare changes, not levels, in the history check; no retuning (guardrail 5). No model or assistant names in pushed files.
- Do not read the CSVs in `sources/history/` whole; `unit` and `domtest.js` take minutes (use the shell's background option).
