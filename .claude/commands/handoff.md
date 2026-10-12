---
description: End the session - rewrite HANDOFF.md, update the ledger, print the next kickoff prompt, then stop.
---
Do these four things, in order, then stop. Do not start new work.

1. **Rewrite `HANDOFF.md`** at the repository root, under 40 lines, plain words, no bare labels. Sections:
   - **What shipped** this session (commits, files, results; one line each).
   - **Branch and pull request state** (branch, head commit, pull request links and whether draft/ready/merged, CI state).
   - **Long jobs in flight** (if any): where they run (Runpod pod id), the pinned commit, where results land, how to tell they are done (the `DONE` file in BetterToBest/compassionism-sim-results).
   - **Next 3 actions**, numbered, each doable from this file alone.
   - **Files to touch** for those actions (paths, with line ranges or grep patterns for files over 300 lines).
   - **Pitfalls** (what went wrong or nearly did; tokens, expiry dates, environment limits).
   Commit it with a clear message and push the session branch.

2. **Update the ledger in one write.** The ledger is the claude.ai artifact KMdxWQ5KAefQVFxQA236pV, database document `projects/sim` (about 275 KB: never read it whole; read only `next`, `phase`, the open issues and the steps whose status is not done). In a single `ArtifactData` update: mark the steps finished this session as done, set `next`, and add one log line (date, what shipped). If no ledger tool is available, put the exact changes under a heading `Ledger updates for Duke` at the end of `HANDOFF.md` instead (this may take it past 40 lines).

3. **Print a kickoff prompt** for the next session, under 120 words, in a fenced block. Its first line must read:
   `Suggested model and effort: <model>, <effort> (<reason in a few words>)`
   choosing: Opus, high effort for engine or statistics work; Opus, medium effort for supervised long runs; Sonnet, medium effort for page work; Sonnet, low effort for packaging. The rest says: read `HANDOFF.md` only, then do its next action.
   (The model name goes in this chat reply only, never in a pushed file.)

4. Stop.
