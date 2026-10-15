# Handoff (Oct 15, 2026): flourishing measures, compare page, chat packets

## What shipped
- **Simulation page:** a "Beyond money: time and taking part" paragraph under Work (hours worked change; enrolment by year 20), from figures already in the release. `earlier-engine.html` re-synced.
- **`compare.html`** (noindex, linked from the findings header and footer): saved six-design comparison (engine 4.22, `data/studies/compare-v422.json`), Compassionism Core versus the version with its untested mechanisms, and today's-safety-net rows from the Health Study (engine 5.5/5.6). Points to the Normative Evaluation site. No new study.
- **Chat packets** in `dev/packets/` (README there): second Python implementation (`s118-...zip`, reference outputs match the seed-42 regression table), four outside audits (`s148-...zip`), CoMSES text and fact sheet (`s119-...zip`). Open ledger items copied to `dev/background/ledger-open-items-oct15.md`.
- `dev/plans/s117-community-hours-study.md`; decisions in `dev/DECISIONS.md` (Session 14). Engine unchanged; version 5.6.0.
- Ledger step s195 was not found in the ledger or the repository; nothing was built under that name.

## Branch and pull request state
- Branch `claude/vigilant-pasteur-1ve1rw`; draft pull request 37 into main (https://github.com/BetterToBest/compassionism-simulation/pull/37). CI not yet reported at writing.
- Local: validate, unit 222, glossary, check_figures 23, check_versions pass. domtest 154 had one failure (earlier-engine script out of step), fixed by `sync_earlier.py`; a full rerun was started and its result is not recorded here. The guard test was not run locally (no engine change; CI runs it).

## Long jobs in flight
- None.

## Next 3 actions
1. **Pull request 37:** read CI; if domtest or guard is red, fix and push (merge main in, never rebase). Duke reads the compare page and the new paragraph, then merges.
2. **Community-project hours (third flourishing measure):** follow `dev/plans/s117-community-hours-study.md` (add keys to the written-out list, 500-seed Runpod run via `dev/tools/s165_jobs.sh`, show on the page).
3. **Chat packets:** give the zips in `dev/packets/` to free-plan chats; paste replies back. A like-for-like re-run of all six designs on the current engine (compare page, Part 1) also needs a Runpod study.

## Files to touch
- `index.html` (grep `rel-flourish`), `compare.html`, `dev/plans/s117-community-hours-study.md`, `dev/packets/`.

## Pitfalls
- Any edit to `index.html` script needs `python3 dev/tools/sync_earlier.py` or domtest fails.
- The results token expires 2026-10-17 04:16 UTC. No model or assistant names in pushed files.
- Do not edit files while domtest runs (about 8 minutes).

## Ledger updates for Duke
(Applied to `projects/sim` in the same session if the write succeeded; otherwise apply: s117 doing, s118 doing (packet built), s171 doing (draft pull request 37), s135 doing (packets built); `next`: Duke reviews pull request 37.)
