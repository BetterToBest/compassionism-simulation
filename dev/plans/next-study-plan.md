# The next study: scope, tiers, run sheet

Oct 14, 2026. Companion to `dev/plans/suite-v2-plan.md`. Duke's direction: one dedicated study that carries the measures the visual suite page cannot yet show (Tier A) and the mechanisms the model does not yet have (Tier B), launched in today's Claude Code session (about 11:00 Pacific). This file says what that can honestly include, the order to build it in, where to stop, and what has to happen before and after the launch.

## 0. Constraints from the ledger (read first)

These come from the Simulation ledger as it stood Oct 14, 08:31 UTC. They decide the shape of the study more than any modelling question does.

1. **One launch.** The ledger's rule is that Claude Code cannot launch a pod after the Pro plan ends. Thursday morning is the last safe session; the cut-off time is not published. So the study must be **launched in today's session**.
2. **Ingesting results needs Node.** Merging the pieces and rebuilding release data (`merge_panel.py`, `release_data.py`, `check_figures.js`) cannot be done in a plain chat. So the results must be **ingested in a Pro session**: Thursday morning at the latest.
3. **Runpod is "not renewed" (ledger).** Before building anything for the launch, confirm with Duke that a pod can be launched today and what the cost cap is. The cap set for the v5.4 run was $4; that run took about an hour on a many-core machine against 7 to 8 hours on Claude Code's four-core machine. The results token expires 2026-10-17 04:16 UTC.
4. **The weekly limit is the real budget.** The ledger's plan for the last Pro days was: today, the CoMSES package and fact sheet (6% to 10% of the weekly limit); this evening, the share kit (8% to 12%, only if 15% remains on top of 8% kept for Thursday); Thursday morning, chat packets for the free plan (4% to 6%, keep at least 8%). The study was not in that budget.

**Decision for Duke (put in the ledger; Claude proceeds on option 1 if it is left unconfirmed):** what gives way to the study?
1. **Recommended.** Today = the study (Tier A, plus Tier B as far as the budget goes, then launch). The CoMSES package, fact sheet and share kit move to chat packets or wait. Thursday morning = ingest the results, update the suite page, final handoff and a short set of packets.
2. Keep today's session for the CoMSES package and launch the study Thursday morning. Risk: results cannot be ingested inside the Pro window, and the Thursday cut-off is unknown.
3. Tier A only, no engine change; Tier B written up as a packet for later.

## 1. Tiers

- **Tier A: report-only.** New fields read from quantities the engine already keeps. No engine change; every existing figure stays identical (`guard_test.js`, `no_figure_change.py`).
- **Tier B: new mechanism behind a switch.** Built, proven, then run as **extra rows ("readings") beside the main result**, as the repo's rule requires: a new mechanism joins the main result only after Duke decides.
- **Tier C: needs outside evidence or an expert first.** Not buildable now; listed so the page can say what each would need.

## 2. Tier A: fields to add (reporting only)

Mark each **[Verify exposed]** until the session has confirmed the engine keeps the quantity per adult-year; if one is not exposed, add an accessor behind a switch and prove switch-off identical.

| # | Field | Feeds | Notes |
|---|---|---|---|
| A1 | Per adult-year dollars: cash income; allowance received and spent; safety-net receipts (SNAP, EITC, Child Tax Credit); rent; interest; fees if the engine has them; taxes and contributions paid | EPPM, EDC, who pays | [Verify exposed]. The no-program run keeps the same fields so each adult has a twin. |
| A2 | Each adult's own basket price index (the community-price cuts) and each arm's general price level by year | EPPM's price part, net-of-inflation view | The release panels carry the end-of-run price level per arm; per-year and per-adult are new. |
| A3 | Monthly surplus above basic living (the FBS formula) for **all** adults in **both** arms | FBS | Keep the participant-only advancement reading as it is. |
| A4 | Acre Equity per adult-year and its liquid share | CSI (simulated reading) | The engine keeps it apart from `wealth`. [Verify] it is not also inside `wealth`. |
| A5 | Each adult's BLEI tier every year (six tiers) | transitions, years in Crisis, time to first exit, re-entry | The release already has poverty spells for part of this. |
| A6 | EDC-adjusted wealth Gini (wealth net of drain, the paper's definition) beside the ordinary Gini, both arms | what the Gini misses | [Verify] what `giniD` and `giniX` already are before adding anything. |
| A7 | Breakdowns of the ladder, EPPM and surplus by: no-program income fifth, household type (alone, couple, with children), age band, community-housing member or not, community-business member or not, octave level | who gains, who does not | Fix group membership by the no-program twin so groups are the same people in both arms. |
| A8 | Net fiscal position by income fifth: what each pays (conversion tax, flat contribution, taxes) against what each receives (allowance, price cuts, safety net) | the cost side by person | [Verify exposed]. |
| A9 | Child ladder: BLEI tiers for children in households (`hhBleiKidPY` exists for the average) | children on the page | Fills a stated limit of the suite. |
| A10 | Per-year price level and real wage paths for each arm and environment | explains Adverse and Stress | |

Pairing rule for A1 to A3: inside one seed's loop, match each latent adult across rows (the same 500 latent adults are instantiated into every row), so every ratio is "this person with the program, against this person without it".

## 3. Tier B: mechanisms, with the order to build them in

"Value" is how much the item matters to the page's goal (what current metrics miss); "cost" is a judgment from the repo's own reports, to be re-estimated after reading the code. The two orders differ on purpose: **build by cost, because the budget is small; rank by value, so that what does not fit is written up properly for later.**

| # | Mechanism | Why it matters | Source of the gap | Cost | Value |
|---|---|---|---|---|---|
| B2 | Public costs avoided beyond prison, hospital and homelessness: emergency services, child welfare (children are now modelled) | Completes the public-cost side of IPBI's crime and health channels. **May be reporting-only:** the existing avoided costs are computed after the run from the change in the poverty gap (`avoidWide` in `harness.js`), so new items of the same kind need a sourced estimate and a formula, not an engine change. | `dev/reports/09-avoided-costs.md`; note in `site/simpage.js` that child welfare is not counted | small to medium (sourcing) | medium |
| B5 | Population-weighted cost-of-living line | Known later fix; changes who counts as below the line | `ECONOMIST-REVIEW.md` row 9 | small to medium | medium |
| B3 | A demand multiplier from participants' spending to other people's incomes, and calibrating the price rule | IPBI's market channel; the weakest-calibrated rule on the economist checklist | `ECONOMIST-REVIEW.md` row 7 | medium; needs a sourced range | high |
| B4 | Labour-force entrants | The model's unemployment is below the official rate | `dev/reports/v5-22-v54-report.md` section 9 | medium | medium |
| B6 | Disaster response, insurance for community homes, tax on unemployment benefits | Hub features the model leaves out | `dev/reports/v5-22-v54-report.md` section 9 | medium | low to medium |
| B1 | Wider safety net: Medicaid, housing aid, standard unemployment insurance, Social Security, state programmes | "Today's US policy" is weaker in the model than in reality: the history check found it absorbs 0.48% of a recession's rise in poverty, against 73% in the data. That flatters any comparison in Adverse and Stress. | `dev/reports/v5-34-v56-release.md` section 6 | **large**; interacts with the SNAP work rule and the health settings | **highest** |
| B7 | Reconcile tax revenue with today's outlays and government's share of the plan | The model reports costs but does not show they are financed | `ECONOMIST-REVIEW.md` row 13 | large | medium |

**Expectation, not a promise:** Tier A plus B2 fits today's session. One engine mechanism (B5, then B3) may. B1 and B7 are not expected to; each gets a written packet (what, sources to find, switch design, tests) so a later session or an outside collaborator can pick it up. B1 is the one to plan carefully, because it is the most valuable and the least likely to fit.

**Rules for every B item:** a labelled switch; its figures appear as a reading beside the main result; `node dev/tools/engine_lineage.js prove "what changed"` and `guard_test.js` pass (switch off = bit-identical); a plain-words report and a line in `dev/DECISIONS.md`. **Never launch with an unproven switch.**

**Stop rule.** Reserve first: at least 8% of the weekly limit for Thursday morning (ingest, page update, handoff), plus the launch itself. Check the weekly limit before starting each B item; start a B item only if it can be finished and proven inside what remains above the reserve. Anything started and not proven is left out of the launch (switch off, not run), and its state is written in `HANDOFF.md`.

## 3b. Tier C: not buildable now (the page says so)

- **Property values** and the **neighbourhood side of crime**: need places; the model has none.
- **Labor productivity for non-participants**: needs employers; the model has none.
- **Victims' losses from crime** (the household side of the paper's crime channel).
- **Who becomes homeless**: the homelessness figure is an overlay on housing distress, not a model of people.
- **Calibrations an independent economist should set** (checklist rows 1 to 8): wait for a collaborator.

## 4. Run design

- **Engine pin:** record the commit. If any B item is included, the pin moves and every earlier figure must still match with the switches off.
- **Rows:** the existing four (no program, main, middle, every dollar backed), plus one extra row per B item built and proven before launch.
- **Grid:** ref, adv, st at 20 and 40 years; 500 seeds, paired; resumable pieces (`dev/batch/runpod.sh`, `dev/tools/v54_jobs.sh`, `dev/tools/s165_jobs.sh` is the pattern the last study used: 49 pieces); the exact commands and commit recorded in each output's `_meta.commands`.
- **Size, extrapolated:** a two-seed run of the **existing** suite export (Reference, 20 years) took 8 seconds including start-up and passed its self-check. Linearly, 500 seeds is at most about half an hour per environment-horizon on one core, before the new fields; each extra row adds roughly a quarter of that. That is an extrapolation from one small run (it does not include the full release panel, which the ledger says took about an hour on a many-core pod). Time the other environments and 40 years on the same two-seed test before launching.
- **Dry run first:** two seeds in every environment and horizon, all new self-checks passing, before the job is started.
- **Self-checks to add:** the parts of EPPM reproduce the whole; per-person dollars sum to the aggregates the release already publishes; the new tier series agree with the existing `bO` and tier series year by year; each Tier A field's no-program mean equals the no-program run's own series; every B row with its switch off equals the main row exactly.
- **Outputs:** new series files beside the existing ones, copied through `python3 dev/tools/release_data.py`; list new data files and any moved counts in `dev/tools/no_figure_change_allow.txt` with reasons.
- **Launch and leave:** start the pod, check once that it started, do not wait (CLAUDE.md). The pod saves each piece to the results repository and turns itself off.

## 5. Before the launch: the outside audit (this morning)

Duke's stated plan is an outside audit by two other AI systems before the next 500-seed study, with the prompt written here and the reports brought back. **`dev/plans/next-study-audit-prompt.md` is that prompt.** It is self-contained (the auditors have no repository access) and asks about the **definitions**, not the code. Timeline: paste it into two systems this morning; bring both replies to the 11:00 session; the session reads them first and fixes any definition they correct, before writing code. If a reply is not back by then, the session proceeds on the plan as written and records that the audit was pending; definitions stay changeable until the pod starts.

## 6. Run sheet for today's session

1. Read `HANDOFF.md`, this plan, and the two audit replies if present. Ask Duke the one question in section 0 only if it is still unanswered; otherwise proceed on the recommended option.
2. Confirm a pod can be launched today and the cost cap (section 0, item 3).
3. Check the weekly limit; write the reserve (section 3) into the plan's working note.
4. Tier A: add the fields to `explore_export.js --suite` (reporting only), with self-checks. Two-seed dry run in every environment and horizon. `no_figure_change.py compare` passes.
5. B2 (and B5, then B3, only as the stop rule allows): build behind a switch or as reporting, prove, record.
6. Run `validate`, `unit`, `domtest`, `guard_test.js` (if any engine file changed), `check_versions.js`.
7. Launch the pod (section 4). Check once that it started. Do not wait.
8. Stage 1 page work from `suite-v2-plan.md` (corrections, card layout, IPBI public-cost items, wording) **if budget remains above the reserve**; otherwise leave it for Thursday morning.
9. End with `/handoff`: rewrite `HANDOFF.md` (what was built, what is proven, what is in the launch, what is not), update the ledger (section 8), open the draft pull request, print the kickoff prompt for Thursday morning.

## 7. After the launch (Thursday morning at the latest)

1. Confirm all pieces finished (a DONE file, every piece exit 0, no pod running, as the last study's close-out did).
2. Merge pieces and rebuild release data: `merge_panel.py`, `release_data.py`; run `check_figures.js`, `no_figure_change.py compare`, `domtest.js`; add each moved count to the allow list with a reason.
3. Update `suite.html` with the new series (suite plan, section 3 and 4), extend `check_figures.js` block 11 and `domtest.js` Phase 15, `node domtest.js --write-counts`.
4. Write the plain-words report; update `HANDOFF.md` and the ledger. Part B (go-live: link from the findings explorer, remove `noindex`, change the domtest check) waits for Duke's approval.
5. If this session cannot happen inside the Pro window, the packet for ingesting results (commands, files, expected checks) must already exist in `HANDOFF.md`, so a free-plan chat plus Duke's own computer can do steps 2 to 4. Whether the free plan can run Node and the repo is unconfirmed; do not assume it.

## 8. Ledger entries to add at the end of the session (written to be readable on their own)

- **New step, simulation ledger:** "Run the dedicated measures-and-mechanisms study on one Runpod pod: the per-person dollars, own price index, Acre Equity, surplus for adults outside the program and six-tier transitions the visual suite page lacks, plus the new mechanisms that were built and proven in the session. Ingest the results Thursday morning and add them to the visual suite page."
- **New decision, simulation ledger:** "What gives way to the study in the last Pro days? Options: (1) today is the study; the CoMSES package, fact sheet and share kit become chat packets (recommended); (2) keep the CoMSES package today and launch the study Thursday morning; (3) Tier A only, no engine change. Why the default: the pod can only be launched while Claude Code is available, and the results can only be ingested while Claude Code is available, so the study has to launch today."
- **New issue, simulation ledger (medium):** "Tier B items B1 (wider safety net) and B7 (reconcile financing) will probably not fit before Pro ends; each needs a written packet."

## 9. How the study feeds the pages

- **Suite page:** EPPM, FBS in both arms, simulated CSI with Acre Equity, the transitions and group breakdowns, public costs avoided (suite plan, sections 3 and 4).
- **Findings explorer:** the new series sit in the release data under the same path pattern, so the explorer can show them later with no copy of figures; decide per item.
- **Main page:** after the suite's next update, Duke decides what moves there.
