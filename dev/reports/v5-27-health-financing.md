# Health financing: today's safety net, single payer with a private layer, the benefit cliff, and the six-result test

Session 2b, Oct 13, 2026. Engine work only: the page does not change. Every new part is a switch, off by default; switched off, every released figure stays the same (the guard test proves it). Choices, sources and alternatives are in `dev/DECISIONS.md`, Session 2b. This builds on today's health system (setting A, `dev/reports/v5-25-health-today.md`) and single payer with a public plan only (setting B, `dev/reports/v5-26-single-payer.md`).

How to read the labels on figures: **sourced** (taken from a published source), **simulated** (an output of the model's runs), **derived** (arithmetic on sourced or simulated figures), **target** (a figure the model was set to match, so it is not a finding). "Points" means percentage points. "Paired" means the same 20 simulated populations (seeds 1-20) with and without the change, so the difference is not noise from different draws. Dollars are at year-0 prices.

## 1. Today's safety net, as a comparison row

The model's "no programme" world has no SNAP, no earned income tax credit (EITC) and no Child Tax Credit (CTC). This session adds them as a switch, used for a comparison row beside the no-programme run. Each household, children included, gets:

- **SNAP** by the USDA's 2026 rules (sourced): the maximum benefit for its size, less 30% of its income after the standard deductions, childcare and part of its rent. Most states let households in up to twice the poverty guideline (sourced); the federal limit of 1.3 times is also run. 88% of eligible people take it up (sourced, USDA 2022; a national estimate, so the Runpod study also runs 75% and 95%).
- **The EITC** by the IRS's 2025 table (sourced). Couples are treated as married and file jointly (an assumption). 80.8% take it up (sourced, IRS 2022). The refundable Child Tax Credit uses the same take-up draw, because both credits need a filed return: for the Child Tax Credit that rate is a modelling assumption, not a sourced figure.
- **The refundable part of the CTC** ($1,700 per child at most; sourced). The part that only cuts income tax is left out, because the model's cost of living already counts taxes after that credit. Adding it would count it twice.

Eligibility uses the same income test as Medicaid (income against the poverty guideline for the household's size). The benefits are today's programmes, paid for today by today's taxes, so they are not programme cost and they are in both runs of every comparison. The model does not reconcile tax revenue with these outlays: it reports the outlays beside each result but does not show that they are financed. (Corrected Oct 13 after the outside audit; `dev/reports/v5-29-outside-audit.md`.) They count as income for basket poverty and depth, but not for the official poverty measure (which, like Census's, leaves out SNAP and tax credits) and not for Medicaid. People respond to the benefits' phase-outs through the model's one work response, the same as for every other benefit.

**What it does in the model (simulated, 20 paired seeds):**

| | Reference | Adverse | Stress |
|---|---|---|---|
| Adult-years in households receiving SNAP | 18.5% | 29.2% | 29.2% |
| Receiving the EITC / the refundable CTC | 12.3% / 10.3% | 19.4% / 14.6% | 19.4% / 14.6% |
| Benefits per adult-year (SNAP, EITC, CTC together) | $1,114 | $1,694 | $1,694 |
| Children in households receiving any of the three | 44% | 58% | 58% |
| Change in poverty depth (FGT2), against no programme | -0.35 (from 7.75) | -1.09 | -1.09 |
| Change in basket poverty, person-years | +0.04 points | +0.03 | +0.03 |
| Change in hours worked | -3% | -4% | -4% |

(Adverse and Stress share one no-programme world, so their no-programme columns match.)

Today's safety net makes poverty shallower but almost never lifts a household above the cost of living. That line is MIT's living wage ($49,370 for one adult; derived: the unweighted average of the 51 state figures in MIT's Living Wage Calculator, February 2026 data, one adult and no children; MIT publishes no national figure, and weighting by population would give about $51,210), far above what these programmes pay. **Compassionism against the safety-net row** (simulated, Reference): basket poverty -30.3 points (interval -31.5 to -29.0), depth -5.8, child basket poverty -43.9. That is almost the same as against no programme (-30.2), because the safety net changes the headcount so little.

Decided since (Duke, ledger d192, Oct 13): the safety net stays on in every Compassionism run, so every comparison reads "against today's safety net", and the Hub says Compassionism adds to these programmes; no savings from replacing them are claimed. The six-cell grid is in session 2c's report, `dev/reports/v5-28-safety-net-grid.md`.

## 2. Setting C: single payer with a private layer

Setting C is setting B (one public plan for everyone, paid by a flat health tax) plus two things:

- **Medicaid kept.** People who would qualify today stay on Medicaid, run by states and counties and paid for by government as now. In the model their care costs the same per unit as the public base's (an assumption).
- **A private layer.** Other households may take a private plan that the public programme pays for per person, as Medicare pays Medicare Advantage. 55% do (sourced: Medicare Advantage's share in 2025, MedPAC; applying it at every age is an assumption). The programme pays more for an enrollee than the public base would have spent on the same person, for two reasons. Each has a low, central and high value:

| | Low | Central | High | Source |
|---|---|---|---|---|
| **(a) Payment gap**: plans record more diagnoses, so payments run higher for the same person | 0 | 4% | 8% | MedPAC, March 2026 (4%) and March 2025 (8%); low is a design value |
| **(b) Selection**: healthier people choose private plans, so payments set by risk exceed what they would have cost, and the public base keeps the costlier people | 5.5% | 11% | 16.5% | MedPAC, 2025 and 2026 (11%); low and high are design values |

MedPAC estimates private plans are paid about 14% more than the same people would cost in traditional Medicare (2026; 20% in 2025) (sourced; $76 billion in 2026). The model splits this into coding (central 4%, range 0-8%) and selection (central 11%, range 5.5-16.5%); Using 14% or 20% as the gap and adding selection on top would count selection twice, because 11 of MedPAC's 14 points are selection. The central case's two together come to 15.4% (derived: 1.04 x 1.11). That is not a match for MedPAC's 14%: MedPAC's total also includes a part of Medicare Advantage's payment rules (bids and bonuses) that comes to about 1% below traditional Medicare (derived: 1.14 / 1.154 = 0.988), and the model has no counterpart to it, so its central case sits 1.4 points above MedPAC's total. The coding high case with selection central is 1.08 x 1.11 = 19.9%; both high is 1.08 x 1.165 = 25.8% (the "both high" row below), a stress case. The 8% is a design value near MedPAC's 2025 coding estimate. Medicare Advantage's figures stand in for a private layer open to all ages as an analogue, not an estimate for that layer. (Duke accepted the earlier wording, ledger d193; the arithmetic is corrected here.) (Corrected Oct 13 after the outside audit; `dev/reports/v5-29-outside-audit.md`.)

**How much of setting B's savings the private layer gives back** (simulated, 20 paired seeds, no programme; B saves $1,449 per person-year against today's $7,684 in Reference):

| | Reference | Adverse and Stress |
|---|---|---|
| Central (gap 4%, selection 11%) | **30%** (29-31) | **28%** (27-29) |
| Gap 0 / 8% (selection central) | 21% / 39% | 20% / 37% |
| Selection 5.5% / 16.5% (gap central) | 19% / 41% | 18% / 39% |
| Both low / both high | 11% / 50% | 10% / 48% |

| Reference, no programme | Today (A) | Single payer (B) | With private layer (C) |
|---|---|---|---|
| Health spending per person-year (all payers) | $7,684 | $6,235 | $6,668 |
| Health tax, share of money income | none | 13.4% | 14.6% |
| Household's health bill per adult-year | $4,366 | $2,365 | $2,966 |
| Basket poverty, person-years | 50.5% | 46.5% | 47.3% |
| Paid to private plans above the enrollees' public cost, per person-year | | | $434 |

Two limits. Enrollees are drawn at random and selection enters as the payment factor: the programme's cost comes out the same as with a pool of healthier enrollees, but who chooses, and why, is not modelled. And the extra payment pays for plans' extra benefits and profit; it is counted as cost only, not as value to the people enrolled.

## 3. The benefit cliff

Under today's system, a household that earns one dollar over the Medicaid limit can lose Medicaid and face premiums and bills. The measure: for each household within a quarter of the poverty guideline of the adult limit (138% of the guideline in expansion states), the jump in that same household's expected health bill when its income crosses the limit.

| | Reference | Adverse | Stress |
|---|---|---|---|
| **Today's system (A)**: jump at the limit, per household (simulated) | **$4,509** (78% of its medical line) | $4,573 | $4,573 |
| **Single payer (B) and C**: jump in every year under the plan | **0** | 0 | 0 |

Under B and C the household's bill is the health tax on its income less the employer share returned to it. Nothing in it depends on Medicaid, so the cliff disappears. Under C, people on Medicaid and on the public base both pay nothing at the point of care. (Both settings report a small positive figure, 3-4 points of the line, which is year 0: today's system runs in year 0, before the plan starts.)

**Whether the BU counts as income in the Medicaid test** (`HEALTH.countBU`; off in every main run, the cautious reading chosen in session 2a). The sweep, with Compassionism:

| Reference, with the programme | Setting A, BU not counted | Setting A, BU counted |
|---|---|---|
| Adult-years on Medicaid | 6.1% | 1.4% |
| Household health bill per adult-year | $4,334 | $5,063 |
| Basket poverty | 19.2% | 21.0% |
| Child basket poverty | 32.3% | 36.2% |
| The programme's effect on basket poverty, change | | 0.6 points smaller (0.5 to 0.8) |

Adverse: Medicaid 12.0% to 2.6%, basket poverty 30.4% to 32.7%. Stress: 10.9% to 6.8%, and 52.7% to 53.4%.

Under B and C, counting the BU removes no one's coverage. But one effect remains, and it is not a cliff. The government keeps paying what it pays for Medicaid today, so if fewer people qualified, government would pay less and the flat health tax would rise for everyone. The household bill in Reference rises by about $700 per adult-year under B and $770 under C, and basket poverty by 0.4 points. The cost is spread over every taxpayer instead of falling on the households near the limit. Fixing government's share at its no-programme level would remove it. (Since applied in the main runs, Duke's decision d194; the floating share is a sensitivity row: session 2c's report, section 6.)

## 4. Nothing counted twice

- **PTF's health-sector price cut under single payer.** Under today's system, a PTF member's price cut on medical care lowers the member's cost of living. Under single payer the member pays nothing at the point of care, so the cut now lowers the public plan's cost of members' care instead, and the saving lowers the health tax for everyone. At the 25% reading (`ptfs25`; the main row's rate is 0), Reference, with the programme (simulated): the plan's cost falls by $423 per person-year under B and C. The household bill under B falls from $2,343 to $1,731. Basket poverty falls from 16.6% to 16.3% under B and from 17.0% to 16.6% under C (under A the same rate takes it from 19.2% to 18.9%). Under B and C this is an upper reading: the Yale preprint's savings already include lower prices, and PTF's cut is applied on top of them (in every main row PTF's health-sector cut is 0, so nothing overlaps there). (Corrected Oct 13 after the outside audit; `dev/reports/v5-29-outside-audit.md`.)
- **Avoided emergency-room costs, counted once.** Single payer's savings (from the Yale preprint) already include $100 billion of avoided emergency and inpatient care, 6.1% of hospital spending (sourced; derived share). In any run with B or C, the hospital and emergency parts of the public costs Compassionism avoids are counted only on the rest. The effect is small: Reference, setting B, the main estimate of public costs avoided goes from $659 to $657 per adult-year. It is cautious in the other direction too: under single payer the public pays all hospital costs, not today's 66%, so the costs avoided there are understated.

## 5. The six-result test

Twenty paired seeds per setting: A, B and C, each without and with Compassionism (the v5.4 release row), in the three environments. All figures simulated; "person-years" are over the 20 years.

**Basket poverty, person-years (no programme -> with Compassionism; the programme's paired effect):**

| | Reference | Adverse | Stress |
|---|---|---|---|
| A (today) | 50.5% -> 19.2% (-31.3) | 67.3% -> 30.4% (-36.9) | 67.3% -> 52.7% (-14.6) |
| B (single payer) | 46.5% -> 16.6% (-29.8) | 63.0% -> 26.5% (-36.5) | 63.0% -> 48.2% (-14.9) |
| C (with private layer) | 47.3% -> 17.0% (-30.3) | 64.0% -> 27.0% (-37.1) | 64.0% -> 49.0% (-15.1) |

**Other measures, Reference (no programme -> with Compassionism):**

| | Poverty depth (FGT2) | Too little wealth, year 20 | BLEI poverty | Child basket poverty |
|---|---|---|---|---|
| A | 7.8 -> 1.7 | 33.2% -> 44.9% | 26.6% -> 11.6% | 78.0% -> 32.3% |
| B | 6.2 -> 1.2 | 30.5% -> 39.7% | 25.0% -> 10.6% | 70.5% -> 25.5% |
| C | 6.4 -> 1.3 | 31.1% -> 40.4% | 25.3% -> 10.7% | 71.3% -> 25.9% |

**The health and Compassionism interaction, on its own line.** This is how much Compassionism's own effect changes when B or C replaces today's system. A positive number means Compassionism does less, because single payer has already done part of the work. The price part is the interaction with prices free less the same with prices held flat; it comes from the rule that a public payer sets medical prices, not from anything Compassionism saves.

| Change in Compassionism's effect | Reference | Adverse | Stress |
|---|---|---|---|
| **B: basket poverty** | **+1.5** (1.2 to 1.8); price part -1.0 | +0.4 (-0.2 to 0.9); -0.2 | -0.3 (-0.7 to 0.1); +0.1 |
| B: depth (FGT2) | +1.1 | +1.4 | +0.7 |
| B: too little wealth | -2.6 (Compassionism's wealth result is better); price part -4.5 | +0.6 | +0.8 |
| B: child basket poverty | +0.7 (-0.3 to 1.8) | -3.8 (Compassionism does more for children) | -2.5 |
| **C: basket poverty** | **+1.0** (0.7 to 1.3); price part -0.9 | -0.1 (-0.7 to 0.4); -0.2 | -0.5 (-0.9 to -0.1); +0.1 |
| C: depth (FGT2) | +1.0 | +1.2 | +0.5 |
| C: too little wealth | -2.4; price part -3.8 | +0.6 | +0.7 |
| C: child basket poverty | +0.3 | -4.0 | -2.5 |

In short, in Reference single payer takes over part of what Compassionism does for basket poverty and depth, and C, which saves less, takes over less. In the harder environments the interaction on basket poverty is small and not distinguishable from zero. For children it runs the other way: Compassionism does more under single payer. Depth (FGT2) moves the same way in all three. Guardrail 6 asks for gains confirmed on basket poverty and wealth poverty, not depth alone, so the B and C gains are reported on all of them above, and they hold on basket poverty, depth and BLEI poverty in all three environments. Too little wealth, the measure the price rule decides (session 2a), improves under B and C without the programme in every environment.

**Today's safety net under A** (simulated, Reference): adding SNAP, the EITC and the CTC to setting A raises basket poverty without the programme by 0.4 points (interval 0.3 to 0.5), against +0.04 without health coverage, while depth falls by 0.5. Traced in session 2c (`dev/reports/v5-28-safety-net-grid.md`, section 2): most of the 0.4 was this comparison, which set the A-with-safety-net row against the row with no health setting and so folded in setting A's own +0.36. Against setting A, the safety net's own effect is +0.07 points (0.04 to 0.09), and it comes through prices.

**Time per run** (one row and one seed: 500 adults over 20 years, households, a health setting on, the one-year pre-pass for the tax rate included; three runs in parallel on four cores): **0.31 to 0.36 seconds** with prices free and 0.35 to 0.40 with prices flat (`_meta.perRun` in each file). The whole test took 4 to 5 minutes per environment for 20 rows. Session 3's Runpod estimate can use 0.36 seconds per run per core.

## Limits

- The Yale preprint behind B and C is not peer reviewed. MedPAC's figures are for Medicare; applying them to a layer open to everyone is an assumption.
- In setting C, who chooses a private plan is not modelled, and the extra payment is counted as cost, not as value to enrollees.
- The safety-net row leaves out TANF, housing assistance, WIC, SSI and SNAP's time limit for adults who must work, which the 2025 law (Public Law 119-21) widened to adults up to 64 and to parents whose youngest child is 14 or older. Leaving it out makes today's safety net more generous than it is, in both runs. It reads SNAP on last year's income.
- Dollars are 2025 dollars: MIT's February 2026 data, SNAP's fiscal-2026 amounts and the 2025 tax year's credits.
- The model charges every household the cost of living's tax line whatever its income, so low earners' taxes are overstated (a limit of the basket, as before).
- Twenty seeds per setting. These are readings, not release figures; the 500-seed runs are session 3's.
- Health does not yet improve with the care people get (the prevention link, session 2c).

## Reproduce

On this branch: `node dev/tools/health_check.js ENV 20 --rows=off,A,B,C,Cg0,Cg8,Cs55,Cs165,Clow,Chigh,AbuY,BbuY,CbuY,ptf25,Aptf25,Bptf25,Cptf25,SN,SN130,ASN --out=s2b` and, with prices flat, `node dev/tools/health_check.js ENV 20 --rows=off,A,B,C --flat --out=s2bflat`, for ENV = `ref`, `adv`, `st`. Outputs: `dev/runs/health/s2b-*.json` and `s2bflat-*.json`. Checks: `node dev/tools/guard_test.js` (passes: every released figure identical), `node harness.js validate`, `node harness.js unit`, `node domtest.js`.
