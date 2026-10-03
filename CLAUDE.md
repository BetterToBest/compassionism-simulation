# Working rules for Claude Code in this repo

Read this file, then `dev/PROGRESS.md`, at the start of every session. Then continue from the first unfinished item in `dev/PROGRESS.md`.

## The project in one paragraph

This repo is the Compassionism Simulation: an open, in-browser agent-based model of the Compassionism framework (500 simulated adults over 20 years; poverty, work, cost and prices against no program). The live page is `index.html` on `main` (v5.0 is tagged; later fixes are tagged as they merge). `harness.js` is the Node copy of the engine used for 500-seed studies. The author, Duke Johnson, wrote the concepts (his book *Better To Best* and the Research Hub at bettertobest.github.io/research-hub/). Claude wrote the math and code. Duke is not a programmer or economist and has delegated every math and code decision to Claude until an independent expert joins.

## Duke's role, and yours

- **You decide** every math, code, modelling and calibration question. Do not stop to ask Duke. Record each decision in `dev/DECISIONS.md`: the question, what you chose, the alternatives, and why, in plain words.
- **Concept questions** (what Duke's design says, as opposed to how to model it): read the Hub papers first, write your reading in `dev/reports/` as a short plain-words note, then proceed on it. Label it "Claude's reading of the design" wherever it shows on the page. Do not invent claims for the framework; where his writing is silent, choose the most cautious option and label it a modelling assumption.
- **Duke's only jobs:** read the plain-words report written after each mechanism (`dev/reports/`), say if anything misrepresents his vision, and merge the pull request when its report reads right: the merge is the release.
- Never write a report that requires Duke to decode labels like s40 or d101. Every entry must make sense on its own. Labels may follow in parentheses.

## Branch rule (protects the live page)

Since v5.0 shipped, the live page is whatever is on `main`, and merging a pull request into `main` is the release. (The earlier `next-release` branch and the `apply-*.zip` route are retired.)

- Work on your session branch (the one the session names; create it if it does not exist). Deliver each piece of work as a pull request from that branch into `main`, created as a draft. Never commit or push directly to `main`. A set of changes that should be released separately goes in a separate pull request.
- Keep the `v5.0` tag where it is, and never move, delete or re-create any tag. A corrected release is a new version: bump it with `python3 dev/tools/set_version.py <version>` and run `node dev/tools/check_versions.js`; `.github/workflows/release.yml` tags the new version when the pull request merges and `index.html` changes.
- Commit after every completed sub-step with a clear message, and push, so an interruption (usage limit, closed window) loses nothing.
- This kit (CLAUDE.md, dev/) reaches `main` the same way, in the pull request that changes it.
- Every session starts by reading `dev/PROGRESS.md` on its session branch. If the branch's last pull request has merged, restart the branch from the latest `main` (`git fetch origin main && git checkout -B <branch> origin/main`) before new work; never stack new commits on merged history.
- The `apply-upload` workflow's commit step is currently broken (cause and a one-line fix are in `dev/PROGRESS.md`, session 34), so do not use the zip route until a person has fixed that workflow.
- Split 500-seed runs by environment (and by model if needed) so no single run outlasts a session; seeds are paired, so the split changes no figure.
- If you cannot reach the Research Hub (bettertobest.github.io) or GitHub, say so in `dev/PROGRESS.md` and tell Duke the environment's network access needs to allow it.

## Standing guardrails (from earlier sessions; keep all of them)

1. Every new mechanism sits behind a switch; with the switch off, output is bit-identical to before (prove it with full-output diffs).
2. Before/after comparisons are CRN-paired on seeds 1-500, in the Reference, Adverse and Stress environments.
3. The three checks run on every change: `validate`, `unit`, `domtest`. Find their exact commands in `.github/workflows/checks.yml`; do not guess.
4. Eight random draws per agent-year (the CRN guarantee) must hold.
5. No constant is retuned to hit a target. Constants come from primary sources (cite them: table, year, file) or are labelled design parameters and swept.
6. Every gain is confirmed on basket poverty and wealth poverty, not FGT2 alone.
7. Fairness rule: one income effect per unconditional dollar; one wage elasticity for every change in the return to work.
8. Model limits are reported, not hidden. Results are reported as they come out; there is no target result.
9. Long runs (500 seeds) go in the background with output saved to `dev/runs/`; record the exact command beside each result.

## Attribution (goes on the released page, README and replication page)

Use this wording at the release (step "release" in `dev/PLAN.md`):

> The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.

## Where things are

- `dev/PLAN.md`: the build order, the design defaults, and the release gate.
- `dev/PROGRESS.md`: what is done and what is next. Update it after every sub-step.
- `dev/DECISIONS.md`: every decision you make, in plain words.
- `dev/reports/`: one plain-words report per mechanism, for Duke.
- `dev/background/`: the ESP split design and sizing, the last 500-seed restudy, and the latest hand-off.
