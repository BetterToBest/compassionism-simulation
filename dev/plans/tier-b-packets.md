# Tier B packets: the mechanisms the measures study left out

Oct 14, 2026. Companion to `dev/plans/next-study-plan.md`, section 3. None of these is built. Each packet says what the mechanism is, what has to be sourced first, how its switch would work, and how to prove it. A later session or an outside collaborator can start from here. The rules for every item are the repo's guardrails (`CLAUDE.md`): a labelled switch, switch off = bit-identical (`node dev/tools/guard_test.js`, `node dev/tools/engine_lineage.js prove "..."`), figures shown as a reading beside the main result, never the headline, until Duke decides.

Listed by value to the suite page's goal, highest first.

## B1. A wider safety net (highest value, largest)

- **What:** Medicaid, housing assistance, standard unemployment insurance, Social Security for those under the ageing module's coverage, state programs. Today the model has SNAP (with its work rule), the EITC and the refundable Child Tax Credit only.
- **Why it matters:** the history check found the model's safety net absorbs about 0.5% of a recession's rise in poverty, against about 73% in the data (`dev/reports/v5-34-v56-release.md`, section 6). A weak baseline flatters any comparison in Adverse and Stress.
- **Source first:** for each program, eligibility rules and benefit schedules as of 2025 (CBPP, CRS, HHS poverty guidelines), take-up rates, and the counter-cyclical response (for example, the Census SPM's estimates of how many people each program lifts out of poverty, by year, 2007 to 2012 and 2019 to 2021).
- **Switch design:** extend `SNET` with per-program flags (`SNET.mcaid`, `SNET.hous`, `SNET.ui`), each paid as cash or in kind through the same channel as `_snB` (one income effect per unconditional dollar; one elasticity for the combined marginal rate, guardrail 7). Interacts with the health settings (`HEALTH`): Medicaid must not be counted twice where the health module already pays.
- **Proof:** the history check (`dev/tools/history_check.js`) should move towards the data's 73% without retuning any constant to hit it (guardrail 5): if it does not, report that.
- **Size:** several sessions.

## B3. Spending that raises other people's incomes (a demand multiplier), and calibrating the price rule

- **What:** participants' extra spending raises the earnings of people who sell to them, including non-participants; today the model has only a recession multiplier.
- **Why it matters:** the paper's market-expansion channel (IPBI), and the price rule is the weakest-calibrated rule on the economist checklist (`ECONOMIST-REVIEW.md`, row 7). The study now shows non-participants lose 5% to 9% of real resources in the main reading through prices; a demand channel would act against that.
- **Source first:** local fiscal multipliers for cash transfers (for example, Egger, Haushofer, Miguel, Niehaus and Walker, *Econometrica* 2022, on GiveDirectly in Kenya, and US evidence on stimulus payments and SNAP), with the evidence on whether the gain reaches non-recipients and how much leaks to prices.
- **Switch design:** `DEMAND = {m, leak}`: each year, a share of the program's net new spending is added to non-participants' wage earnings in proportion to their earnings, through the existing labour channel. Swept over the sourced range as a design parameter.
- **Size:** one to two sessions after sourcing.

## B2. More public costs avoided (emergency services, child welfare)

- **What:** two more items beside prisons, hospital and psychiatric stays and homelessness.
- **May be reporting only:** the existing items are computed after the run from the change in the poverty gap (`avoidWide` in `harness.js`), so new items of the same kind need a sourced estimate and a formula, not an engine change and not a pod run.
- **Source first:** a causal estimate of the change in child-welfare involvement per dollar of family income (for example, studies of the EITC and of state minimum-wage changes on maltreatment reports), and a per-case public cost (federal Title IV-E and state outlays); emergency-department use against income for adults (published natural experiments).
- **Size:** half a session after sourcing.

## B5. A cost-of-living line weighted by population

- **What:** today the basket is the MIT living wage for one area profile; a population-weighted line would change who counts as below it (`ECONOMIST-REVIEW.md`, row 9).
- **Source first:** MIT living-wage baskets by county, with county adult populations.
- **Switch design:** `COST_LINE = 'popw'`, changing the basket level and its shares only; everything that reads the basket follows.
- **Size:** about one session.

## B4. People entering the labour force

- **What:** the model's unemployment is below the official rate (`dev/reports/v5-22-v54-report.md`, section 9).
- **Source first:** BLS flows into the labour force by age, and job-finding rates.
- **Size:** one session.

## B6. Disaster response, insurance for community homes, tax on unemployment benefits

- Hub features the model leaves out (`dev/reports/v5-22-v54-report.md`, section 9). Low to medium value; each small once sourced.

## B7. Reconcile tax revenue with today's outlays and government's share of the plan

- **What:** the model reports costs but does not show they are financed (`ECONOMIST-REVIEW.md`, row 13).
- **Needs:** an expert, or at least a published federal and state revenue model; large.
