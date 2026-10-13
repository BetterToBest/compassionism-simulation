# Handoff (Oct 13, 2026; session 2c, ledger step s153: health financing finished)

## What shipped
- Today's safety net (SNAP, EITC, refundable Child Tax Credit) on in every Compassionism comparison: `health_check.js --grid` runs the six cells (A, B, C, each without and with Compassionism) plus the no-programme, no-safety-net reference line, with costs beside results (2d8e6c8). The switch stays off by default.
- The +0.4 point safety-net reading traced (`dev/tools/sn_trace.js`): it was setting A's own effect folded into the comparison. The safety net's own effect is +0.07 points, through prices.
- Government's share under single payer fixed at its no-programme level (`HEALTH.gov` 'fixed'); the floating share is a sensitivity row and reproduces session 2b exactly.
- Prevention link (`PREV`, row option `pv`, off by default): zero, central and high cases, labelled; small in every case. The claim about genetically modified crops is kept out.
- Speed pass: profiled, no 2x available, stopped with no engine change. **Time per run: 0.375-0.436 s for health rows (use 0.43 s per run per core), 0.35 s without a health setting.**
- Report `dev/reports/v5-28-safety-net-grid.md`; v5-27 updated to Duke's decisions; DECISIONS Session 2c; runs in `dev/runs/health/s2c*-*.json` (50f1a29).
- Checks: validate; unit 221, 0 failed; domtest 125, all passed; guard identical; lineage link 7ec4e6c93ca9 -> 57e00367e58f.

## Branch and pull request state
- Branch `claude/optimistic-wozniak-flwhbn`, from main f3f7f3d (pull request #17 merged).
- Pull request https://github.com/BetterToBest/compassionism-simulation/pull/18 into main, which this session merges once CI is green (the kickoff asked for it, so the auditors read the final engine). If it is still open, check CI and merge it. No version bump: no page change.

## Long jobs in flight
None.

## Next 3 actions
1. **Outside audit (ledger step s154, Duke):** paste `outside-audit-prompt.md` (delivered Oct 12) into GPT and one other AI, each in a fresh chat, against main after pull request #18. Bring both replies to a Claude session, which sorts the findings into fix-before-Runpod, fix-later and reject (with reasons) and applies the first group.
2. **Before the Runpod study (ledger step s137, Duke):** renew the GitHub token for BetterToBest/compassionism-sim-results (**it expires 2026-10-17 04:16 UTC**), update the Runpod secret `github_results_token`, and turn the Runpod connector on.
3. **Runpod study (s137):** sensitivity (Morris, then Sobol), the comparison restudy, and the health financing table: `--grid` cells at 500 seeds in three environments, plus the floating-share rows (`BSNfl`, `CSNfl`) and the prevention link's central case (`ASNpv`, `BSNpv`, `CSNpv`). Cost: the table is about 18,000 runs (2.2 core-hours at 0.43 s) per set of six cells. Spend cap $8.

## Files to touch
`dev/batch/runpod.sh`, `dev/tools/v54_jobs.sh` (pieces, one per core). `dev/tools/health_check.js` (grep `const VAR`, `GRID`). It has no seed-range option yet, and the Runpod pieces need one (`tbStudy` takes a first seed, `lo`). `dev/reports/v5-28-safety-net-grid.md` (Reproduce section).

## Pitfalls
- `health_check.js` runs seeds 1..N in one process. Add the seed-range option before splitting the work into pieces; seeds are paired, so splitting changes no figure.
- After any `index.html` edit, run `python3 dev/tools/sync_earlier.py`. An engine edit makes domtest's two provenance checks fail until `node dev/tools/engine_lineage.js prove "..."` records a link (about 10 minutes; do not edit `index.html` meanwhile).
- `unit` changes the test count quoted in the docs: run `node harness.js unit --write-counts`.
- Run `node --check` on tools before committing (an unescaped apostrophe once broke `health_check.js`).
- Pro ends after Oct 18: Claude Code sessions are scarce, so start the Runpod job early in the session and do not poll it.
