# Release checklist (plan step 13)

Oct 2, 2026 · prepared by Claude, session 30; updated in session 31 with Duke's four added items · the release happens only when Duke says "release"

## Gate status

| Gate item | Status |
|---|---|
| Every planned mechanism built (steps 1-9, and Duke's four items, steps 14-17) | Done; each behind a switch, each with a plain-words report in `dev/reports/` |
| 500-seed restudy in Reference, Adverse and Stress | Done (`dev/reports/v5-5-restudy.md`, session 31) |
| Gains confirmed on basket and wealth poverty | **At reference, yes. In Adverse and Stress, no:** income and BLEI poverty fall, but more adults end with too little wealth than with no programme. The page says so plainly. |
| The three checks pass | Yes: `node harness.js validate`, `node harness.js unit` (every suite), `node domtest.js` (97 checks) |
| Page and harness agree on the same seeds | Yes (domtest phase 12: verbatim source, identical results) |
| The octave wage raise and the inflation slow-down off by default, each a labelled switch | Yes (a row in the restudy and on the page's "other readings") |
| No programme compared at the scenario's own inflation; the current conversion design named plainly | Yes: every comparison is against no programme in the same environment; the page names the Source financing as Claude's reading of the design |
| Duke has read the restudy report | **Pending** |

## Proposed version label

**v5.0.** The page now runs Compassionism as specified on the Hub with every mechanism, and opens with that model's results instead of a comparison with other designs, so the headline figures change meaning, not only value. (4.23 would suggest a fix.) Duke assigns it.

## Steps when Duke says "release" (for the session that does it)

1. On `next-release`: `python3 dev/tools/set_version.py 5.0` (sets META.VERSION, the replication page's meta, JSON-LD and labels).
2. In `CONTRIBUTING.md`, change the heading's "Proposed label" sentence to the release date; keep the heading `## v5.0 Release Notes` (the release workflow reads it).
3. Run the three checks.
4. Merge `next-release` into `main` (a merge commit). Pushing `index.html` to `main` starts the release workflow, which tags `v5.0` and writes the GitHub release from the notes. `v4.22` stays tagged for reverting.
5. Research Hub (`BetterToBest/research-hub`, outside this repository): update `ai-index.json` and `research-index.json`. The simulation's entry should drop any mention of the six-design comparison and describe the release in one sentence, for example: "Open agent-based simulation of the Compassionism framework as specified on the Hub: 500 simulated adults over 20 years against no programme in three environments, with BLEI, poverty, savings, work, prices and cost, averaged over 500 paired runs."
6. After the release: record a new walk-through (s65); rewrite the outreach drafts (s37) for the stand-alone page.

## If the panel needs regenerating

`node harness.js testbed 500 release ref --json=dev/runs/release-panel-ref.json` (and `adv`, `st`; about 15 minutes each, run in parallel), then `python3 dev/tools/merge_panel.py` and `python3 dev/tools/release_figs.py`. After any engine change in `harness.js`: `python3 dev/tools/port_engine.py`, then the three checks.

## Not possible from sessions 30 and 31

GitHub write access: every commit is local on `next-release`. Duke has a git bundle of the branch (session 31's is `next-release-session31.bundle`); restore it with `git fetch next-release-session31.bundle next-release:next-release` and push, or reconnect GitHub so a session can push.
