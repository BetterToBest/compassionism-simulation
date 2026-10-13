# Handoff (Oct 13, 2026; session 2b, health financing)

## What shipped
- Today's safety net (6d40e6f): SNAP, the EITC and the refundable Child Tax Credit as a comparison row (`SNET`, row option `sn`, off by default). It makes poverty shallower (FGT2 -0.35 in Reference) but leaves basket poverty almost unchanged.
- Health setting C (3317679): single payer plus Medicaid kept plus a private layer. The payment gap and selection are split as MedPAC's March 2026 report splits its 14% (coding 4%, selection 11%). C gives back 30% of setting B's savings (low to high cases: 10-50%).
- Benefit cliff (3317679): a household's own expected bill jumps $4,509 at the Medicaid limit under today's system, and 0 under B and C. The `HEALTH.countBU` sweep is included.
- Overlaps (3317679): under B and C, PTF's health-sector cut lowers the plan's costs, not the household's. Avoided emergency and inpatient care is counted once (`avoidWide` takes the setting).
- Six-result test and report (73592fa): `dev/reports/v5-27-health-financing.md`; outputs in `dev/runs/health/s2b-*.json` and `s2bflat-*.json`. Time per run 0.31-0.40 s. Decisions: `dev/DECISIONS.md`, Session 2b.
- Checks: validate passed; unit 219 run, 0 failed; domtest 125 passed; guard identical; lineage links ad7817234bcb and 7ec4e6c93ca9.

## Branch and pull request state
- Branch `claude/kind-cray-obtb9m`, from main 5ab5225 (pull request #16 merged); head is this handoff commit.
- Draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/17 into main, watched. Its CI was starting when this was written. No version bump: there is no page change.

## Long jobs in flight
None.

## Next 3 actions (session 2c, ledger step s150)
1. Check CI on #17 and fix anything red. **Prevention link (s141)**: behind a new switch, off by default, care received lowers later need. Make it labelled assumptions with a zero, central and high case, each sourced or marked as a design value. Keep the genetically modified crop claim out. Guard test and a lineage proof as usual.
2. **Speed pass (s142)**, time-boxed to about 2 hours. Results must stay identical under the guard test. Stop and revert if the gain is under 2x. Baseline: 0.35 s per run (`_meta.perRun`).
3. Rerun the six-result test with the prevention link (commands under "Reproduce" in the report). Write report v5-28, open a pull request, then do `/handoff`. Also decide or trace: (a) why the safety net under setting A raises basket poverty 0.4 points (report section 5); (b) whether government's Medicaid share under B and C should be fixed at its no-programme level (the countBU financing effect, report section 3).

## Decisions flagged for Duke (meaning, not applied)
- Should Compassionism runs keep today's safety net, so that every comparison is "against today's safety net"?
- The payment gap is read as MedPAC's coding part (4%), not "roughly 20%". 20% is the high case of the gap and selection together.

## Files to touch
`index.html` (never read whole): grep `HEALTH_DEFAULTS`, `function hlYear`, `function hlSingle`, `function hlNeedOf`, `function snYear`. `harness.js`: grep `function healthUnitSuite`. `dev/tools/health_check.js` (`const VAR`). `dev/DECISIONS.md` (append; grep `Session 2b`).

## Pitfalls
- After any `index.html` edit, run `python3 dev/tools/sync_earlier.py`. Do not edit while `engine_lineage.js prove` runs (about 10 minutes).
- `unit` changes the test count quoted in the docs: run `node harness.js unit --write-counts`.
- A string with an unescaped apostrophe broke `health_check.js` once. Run `node --check` on tools before committing.
- Before session 3's Runpod job, renew the GitHub token for the results repository (it expires 2026-10-17 04:16 UTC) and update the Runpod secret `github_results_token`.
