# Handoff (Oct 13, 2026; session 2a)

## What shipped
- Pay-cut check (e43b26d): with prices held flat, the 10% pay cut raises too little wealth by 0.6 points with the programme and 1.5 without (as released: 5.5 and 1.5), so the gap comes through prices. Paragraph in `dev/DECISIONS.md`, Session 2a; outputs in `dev/runs/v54/paycut*-ref.json`.
- Guard test (bc93de3): `dev/tools/guard_test.js` compares every output of 25 v5.4 panel rows, seeds 1-20, three environments, with references made before any engine edit (`dev/runs/guard/`). It runs as its own CI job and is now guardrail 1's proof.
- Today's health coverage, setting A (ae64431): a switch, off by default. It adds medical need by age, coverage, out-of-pocket cost, skipped care, medical debt and who pays, plus the shared income test (`incomeTest`, `medicaidEligible`). Report `dev/reports/v5-25-health-today.md`; sources `sources/health/README.md`.
- The two price rules for health care, recorded in DECISIONS before single payer was written.
- Single payer, public plan only, setting B (da6b80c): three cases from the Yale preprint. Central: health spending -19%, health tax 13.4% of money income, basket poverty without the programme 50.5% to 46.5%. Report `dev/reports/v5-26-single-payer.md`. 20 paired seeds per setting, three environments, in `dev/runs/health/`.
- The attached country comparison failed 3 of 5 spot checks and is not used (kept in `dev/background/health/`).
- Checks: validate passed; unit 214 run, 0 failed; domtest 125 passed; guard passed; two engine-lineage links recorded (`dev/runs/engine-lineage.json`).

## Branch and pull request state
- Session branch `claude/sharp-cori-rxgww2`, started from main 0f2e42e (v5.4.1); head is this handoff commit, on top of da6b80c.
- Draft pull request https://github.com/BetterToBest/compassionism-simulation/pull/16 into main. Its CI (checks and guard) was running when this was written. No version bump: engine switches only, the page is unchanged.

## Long jobs in flight
None.

## Next 3 actions
1. Check CI on #16 and fix anything red. When it is green, mark #16 ready for Duke; his merge needs no release tag (no version change).
2. Session 2b (ledger step "Session 2b"), engine only, behind switches. The guard test must pass, and each engine change needs a lineage proof:
   - (a) the today's-safety-net row (SNAP, EITC, Child Tax Credit, children modelled), moved from 2a, reusing `incomeTest`;
   - (b) single payer with a private layer, and Medicaid kept (setting C);
   - (c) the benefit-cliff check, sweeping `HEALTH.countBU`;
   - (d) under setting B, apply PTF's health-sector cut to the plan's costs, not to households (DECISIONS: "Nothing counted twice", item 7);
   - (e) the prevention link; (f) the speed pass.
3. Before session 3's Runpod job: renew the GitHub token for the results repository (it expires 2026-10-17 04:16 UTC) and update the Runpod secret `github_results_token`.

## Files to touch
`index.html` (never read whole): grep `HEALTH_DEFAULTS`, `function hlYear`, `function hlSingle`, `function incomeTest`, `function tbSetV54`. `harness.js`: grep `function healthUnitSuite`, `HL_KEYS, HEALTH_DEFAULTS`. `dev/tools/health_check.js` (variant table `const VAR`). `dev/DECISIONS.md` (append only; grep `Session 2a`). `dev/reports/` (one report per mechanism).

## Pitfalls
- After any `index.html` edit, run `python3 dev/tools/sync_earlier.py`, or domtest fails twice ("DRIFTED" and "same script false").
- Do not edit `index.html` while `engine_lineage.js prove` runs (about 10 minutes): its panels read the page when they finish.
- A wait loop on a check's output file can read the previous run's file. Delete or timestamp the file first. `pkill -f guard_test.js` killed its own shell.
- Model limits, reported rather than tuned: too few adults on Medicaid (the model has no adults outside the labour force), and medical debt read as an upper bound.
- The ledger document is near the database's 256 KB limit. Shorten finished steps' notes before adding text.
