# Working rules for Claude Code in this repo

## Start, work, stop (token rules)

- Begin every session by reading `HANDOFF.md` only. Open other files only when the next action needs them.
- Use grep and line ranges (`sed -n A,Bp`, Read with offset/limit). Never read a whole file over 300 lines (index.html, harness.js, dev/PROGRESS.md, dev/DECISIONS.md are all longer).
- No screenshots unless a visual check is the task.
- Never wait or poll for long jobs. Start them on Runpod (`dev/batch/runpod.sh`), check once that they started, and end the session.
- No model names in commit messages, pull request text, release notes or any pushed file.
- End every session with `/handoff` (`.claude/commands/handoff.md`).

## The project

The Compassionism Simulation: an open, in-browser agent-based model of the Compassionism framework (500 simulated adults over 20 years; poverty, work, cost and prices against no program). The live page is `index.html` on `main`. `harness.js` runs the page's engine (read out of `index.html`, the one copy) in Node for 500-seed studies. Duke Johnson wrote the concepts (*Better To Best*, the Research Hub at bettertobest.github.io/research-hub/); Claude wrote the math and code. Duke is not a programmer or economist and has delegated every math and code decision to Claude until an independent expert joins.

## Duke's role, and yours

- **You decide** every math, code, modelling and calibration question; do not stop to ask Duke. Record each in `dev/DECISIONS.md` (question, choice, alternatives, why, in plain words).
- **Concept questions:** read the Hub papers first, write your reading in `dev/reports/` as a short plain-words note, proceed on it, label it "Claude's reading of the design" on the page. Never invent claims for the framework; where his writing is silent, choose the most cautious option and label it a modelling assumption.
- **Duke's only jobs:** read the plain-words report after each mechanism, say if anything misrepresents his vision, and merge the pull request when its report reads right (the merge is the release).
- Reports must make sense on their own: no bare labels like s40 or d101 (labels may follow in parentheses).

## Branches and releases

- Work on the session branch the session names; deliver each piece as a draft pull request into `main`. Never push to `main`. Separate releases go in separate pull requests.
- If the branch's last pull request has merged, restart it from `main` (`git fetch origin main && git checkout -B <branch> origin/main`); never stack on merged history.
- Never move, delete or re-create a tag. A new version: `python3 dev/tools/set_version.py <version>`, then `node dev/tools/check_versions.js`; `.github/workflows/release.yml` tags it on merge.
- Commit and push after every completed sub-step. Do not use the `apply-upload` zip route (its workflow is broken; see `dev/PROGRESS.md`, session 34).
- If the Research Hub or GitHub is unreachable, say so in `HANDOFF.md` and tell Duke the environment's network access must allow it.

## Standing guardrails (keep all)

1. Every new mechanism sits behind a switch; switch off = bit-identical output (prove with full-output diffs; `node dev/tools/guard_test.js` must pass, about 3 minutes, also run in CI). Record each engine change with `node dev/tools/engine_lineage.js prove "what changed"`.
2. Before/after comparisons are CRN-paired on seeds 1-500 in the Reference, Adverse and Stress environments.
3. The three checks (`validate`, `unit`, `domtest`; exact commands in `.github/workflows/checks.yml`) run on every change.
4. Eight random draws per agent-year (the CRN guarantee) must hold.
5. No constant is retuned to hit a target. Constants come from cited primary sources or are labelled design parameters and swept.
6. Every gain is confirmed on basket poverty and wealth poverty, not FGT2 alone.
7. Fairness: one income effect per unconditional dollar; one wage elasticity for every change in the return to work.
8. Model limits are reported, not hidden; there is no target result.
9. 500-seed runs go on Runpod in resumable pieces (`dev/tools/v54_jobs.sh`, `dev/batch/runpod.sh`), results pushed to BetterToBest/compassionism-sim-results; record the exact command and commit beside each result. Seeds are paired, so splitting changes no figure.

## Attribution (released page, README, replication page)

> The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.

## Where things are

`HANDOFF.md` (start here) · `dev/PLAN.md` (build order, release gate) · `dev/PROGRESS.md` (done and next) · `dev/DECISIONS.md` · `dev/reports/` (one plain-words report per mechanism) · `dev/background/`.
