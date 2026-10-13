# Today's safety net in every run: the six-cell grid with costs, government's share fixed, and the prevention link

Session 2c, Oct 13, 2026. Engine work only: the page does not change. Every new part sits behind a switch, off by default. Switched off, every released figure stays the same, and the guard test proves it. Choices, sources and alternatives are in `dev/DECISIONS.md`, Session 2c. This builds on session 2b's report (`dev/reports/v5-27-health-financing.md`).

How to read the labels on figures: **sourced** (taken from a published source), **simulated** (an output of the model's runs), **derived** (arithmetic on sourced or simulated figures), **target** (a figure the model was set to match, so it is not a finding). "Points" means percentage points. "Paired" means the same 20 simulated populations (seeds 1-20) with and without the change, so the difference is not noise from different draws. Intervals are 95%. Dollars are at year-0 prices. These are 20-seed readings, not release figures; the 500-seed runs are the Runpod study's (ledger step s137).

The three health settings: **A**, today's health system; **B**, single payer with one public plan, paid by a flat health tax; **C**, single payer plus Medicaid kept and a private layer paid per person (as Medicare pays Medicare Advantage). "Compassionism" means the v5.4 release row.

## 1. What changed

- **Today's safety net is on in every Compassionism comparison** (Duke's decision, ledger d192). SNAP, the earned income tax credit (EITC) and the refundable part of the Child Tax Credit (CTC) are paid in every cell of the grid, with and without Compassionism. Every comparison in sections 3 and 5 reads "against today's safety net". On the Hub, Compassionism *adds to* these programmes, and no savings from replacing them are claimed. The run with no programme and no safety net stays only as a reference line. The switch stays off by default, so released figures do not move.
- **Government's share under single payer is fixed** (Duke's decision, d194). Under B and C the government keeps paying what it pays today for Medicaid, the premium tax credits and Medicare; the health tax pays the rest. In the main runs that share is now held, year by year and per person, at its level in the same seed's run without the programme. The old floating share is kept as a sensitivity row (section 6).
- **Setting C's payment gap, in Duke's wording** (d193): MedPAC estimates private plans are paid about 14% more than the same people would cost in traditional Medicare (2026; 20% in 2025) (sourced). The model splits this into coding (central 4%, range 0-8%) and selection (central 11%, range 5.5-16.5%). 20% is the high case of both together. The values are session 2b's; only the wording is new.
- **The prevention link** (ledger step s141) is a new switch, off by default (section 4).
- **The speed pass** (s142) was tried and stopped: no change to the engine (section 7).

## 2. Why the safety net seemed to raise basket poverty under setting A

Session 2b's report (section 5) said adding the safety net to setting A raised basket poverty without the programme by 0.4 points. Three causes were tested, each with a paired run (`dev/tools/sn_trace.js`, Reference, 20 seeds; simulated):

| What the safety net does to basket poverty, no programme | As released | Work response off | Prices held flat |
|---|---|---|---|
| With no health setting | +0.04 (0.03 to 0.05) | +0.11 (0.09 to 0.13) | +0.01 (-0.01 to 0.02) |
| Under setting A, against setting A | **+0.07** (0.04 to 0.09) | +0.10 (0.08 to 0.13) | +0.00 (-0.01 to 0.02) |
| Setting A with the safety net, against neither (session 2b's comparison) | +0.43 (0.33 to 0.52) | +0.46 | +0.31 |

**Finding.**

1. **Most of the 0.4 was the comparison.** Session 2b's tool compared "setting A with the safety net" with "no health setting, no safety net", so its figure included setting A's own +0.36. Against setting A without the safety net, the safety net's own effect is +0.07 points. The tool now uses that comparison.
2. **The work response is not the cause.** Switched off, the rise gets larger, because recipients then keep the whole benefit.
3. **What is left comes through prices.** With prices held flat it is zero. The benefits let poor households buy more of the essentials they were going without. The model's price rule raises essentials' prices when more of them is bought, so the cost of living rises a little for everyone. Some households just above the line (MIT's living wage, $49,370 for one adult; sourced) fall below it. Recipients themselves are mostly far below the line, so their gain shows as less depth: poverty depth (FGT2) falls by 0.57 under A and 0.35 with no health setting.

Under A the safety net also cuts the household health bill by $181 a year (simulated): its phase-outs lower earnings by about 3%, which puts 3.2 points more adult-years on Medicaid. The price rule is the model's one rule for every extra dollar of met need, Compassionism's included, so it is kept as it is, and reported.

## 3. The six-cell grid, against today's safety net

**Basket poverty, person-years (simulated; no programme -> with Compassionism, and the programme's paired effect):**

| | Reference | Adverse | Stress |
|---|---|---|---|
| A (today) | 50.6% -> 18.4% (**-32.2**, -33.4 to -31.0) | 67.3% -> 28.2% (**-39.1**, -40.2 to -38.1) | 67.3% -> 52.6% (**-14.7**, -15.6 to -13.9) |
| B (single payer) | 46.2% -> 16.2% (**-29.9**, -31.1 to -28.8) | 62.5% -> 25.3% (**-37.2**, -38.5 to -35.9) | 62.5% -> 48.0% (**-14.5**, -15.3 to -13.7) |
| C (with private layer) | 47.0% -> 16.5% (**-30.5**, -31.7 to -29.3) | 63.4% -> 25.8% (**-37.7**, -39.0 to -36.4) | 63.4% -> 48.7% (**-14.7**, -15.4 to -13.9) |
| Reference line: no health setting, no safety net | 50.2% -> 19.9% (-30.2) | 67.5% -> 32.2% (-35.3) | 67.5% -> 53.4% (-14.2) |

**Other measures, Reference (simulated; no programme -> with Compassionism):**

| | Poverty depth (FGT2) | Too little wealth, year 20 | BLEI poverty | Child basket poverty |
|---|---|---|---|---|
| A | 7.2 -> 1.5 | 33.2% -> 45.6% | 26.6% -> 11.6% | 78.0% -> 28.7% (-49.3) |
| B | 5.8 -> 1.1 | 30.4% -> 40.5% | 25.0% -> 10.7% | 70.2% -> 23.5% (-46.8) |
| C | 6.0 -> 1.1 | 31.1% -> 41.3% | 25.2% -> 10.8% | 71.0% -> 23.8% (-47.2) |
| Reference line | 7.8 -> 1.6 | 32.9% -> 44.3% | 26.6% -> 11.9% | 76.9% -> 33.0% (-43.9) |

"Too little wealth" rises with Compassionism in every cell. This is the released v5.4 result (people in the programme hold less cash wealth while their basket is covered) and is not new here.

**Costs beside results, Reference** (simulated; per adult-year unless marked; no programme / with Compassionism):

| | Programme cost | Health tax (rate) | Household health bill | Safety-net outlays | Government's share of the plan | Plan spending, per person-year | Paid to private plans above their enrollees' public cost, per person-year |
|---|---|---|---|---|---|---|---|
| A | 0 / $29,754 | none | $4,185 / $4,159 | $1,115 / $1,134 | (today's system) | (today's system) | |
| B | 0 / $29,791 | $6,277 (12.9%) / $6,264 (12.5%) | $2,169 / $2,175 | $1,123 / $1,128 | $2,317 / $2,317 | $6,211 / $6,201 | |
| C | 0 / $29,792 | $6,853 (14.1%) / $6,836 (13.6%) | $2,743 / $2,747 | $1,122 / $1,128 | $2,313 / $2,313 | $6,624 / $6,612 | $414 / $411 |

Under A the household bill is premiums and out-of-pocket cost. Under B and C it is the health tax less the employer's former premium share, which comes back to the household. Safety-net outlays are paid from taxes the cost of living already charges every household, so they are not programme cost (session 2b). Adverse and Stress (the same no-programme world, so the same "no programme" column): programme cost $28,329-28,366 (Adverse) and $11,612-11,614 (Stress); health tax under B $5,419 (14.1%) and under C $5,927 (15.4%); household bill under A $3,633, B $1,654, C $2,162; safety-net outlays $1,694; private-layer overpayment $368.

**What the safety net changes in Compassionism's effect under A** (simulated; the programme's effect with the safety net less without it; negative means Compassionism does more):

| | Reference | Adverse | Stress |
|---|---|---|---|
| Basket poverty | -0.9 (-1.1 to -0.7) | -2.2 (-2.5 to -2.0) | -0.2 (-0.3 to -0.0) |
| Child basket poverty | -3.6 (-4.3 to -3.0) | -7.3 (-8.1 to -6.4) | -0.8 (-1.1 to -0.4) |
| Too little wealth | +0.7 (0.4 to 1.0) | +1.0 (0.7 to 1.4) | +1.2 (0.9 to 1.5) |

With the safety net on, Compassionism lowers basket poverty more, most of all for children. Claude's reading (not fully decomposed): the safety net's dollars change the headcount only for households near the line, and Compassionism moves many households close to it. With no health setting the same comparison is +0.07 (-0.06 to 0.19) in Reference, so under A part of it runs through Medicaid (section 2).

## 4. The prevention link

**What it does.** With the switch on (`PREV`, row option `pv`), an adult's chance of entering the lasting chronic state depends on last year's exposure to two things the programme, the safety net and single payer can change. The chronic state means two or more chronic conditions, which raises a person's need for care about 3.8 times (derived from MEPS: 25.9% of adults, 57% of spending; sourced).

- **Care skipped for cost.** The person skipped some care last year under today's system. Nobody skips in the years under B or C.
- **Food access.** This is the chance the household was food insecure, read from its income for food (money income, safety-net benefits and the BU allowance) against the poverty guideline. The rates are USDA ERS's for 2023 (sourced; Household Food Security in the United States in 2023, ERR-337, Table 2): 38.7% under the guideline, 34.1% from 1.00 to 1.30 times it and 27.6% from 1.30 to 1.85 (derived from the table's counts), and 7.5% above 1.85 times it.

Each run is scaled so that the chronic share stays MEPS's 25.9% in today's world (using year 0, whose exposures the programme cannot touch). No random draw is added.

| Case | Care skipped (risk ratio) | Food insecurity (risk ratio) | Status |
|---|---|---|---|
| Zero | 1 (switch off) | 1 | Sourced reading: the Oregon Health Insurance Experiment found no detectable effect of Medicaid on blood pressure, cholesterol or blood sugar control in two years (Baicker et al., NEJM 2013) |
| Central | 1.10 | 1.10 | Design values: about half the observed associations below, because associations in observational data overstate causal effects |
| High | 1.51 | 1.30 | Care: derived (32.1% against 21.2% reported a significant health decline after restricting medicines for cost; Heisler et al., Medical Care 2004). Food: sourced (adjusted relative risk for hyperlipidemia among food-insecure poor adults, NHANES 1999-2004; hypertension 1.20; Seligman et al., J Nutr 2010) |

**Results (simulated, 20 paired seeds, all with the safety net on).** The link is small in every case.

| Reference | Zero | Central | High |
|---|---|---|---|
| Chronic share, adult-years, no programme: A / B | 25.9% / 25.9% | 25.9% / 25.8% | 25.8% / 25.3% |
| Need per person-year, B, no programme | $9,651 | $9,635 | $9,586 |
| Plan spending per person-year, B, no programme | $6,211 | $6,208 | $6,200 |
| Compassionism's effect on basket poverty under A | -32.2 | -32.2 (moves +0.00, -0.01 to 0.01) | -32.2 (+0.01, -0.00 to 0.03) |
| Interaction under B (section 5) | +2.29 | +2.29 | +2.30 |

Adverse and Stress are as small: Compassionism's effect under A moves by 0.02 points or less, and the interaction under B or C by 0.03 or less. The chronic share hardly moves because people enter the chronic state slowly (about 3.5% of those outside it each year), and the exposures the programme changes shift that chance by a few percent. Under single payer, with nobody skipping care, the share falls by 0.1 points (central) to 0.5 (high).

**Claims kept out of the engine and the pages.** The claim that genetically modified crops cause illness in people is not used. The 2016 US National Academies report on genetically engineered crops found no substantiated evidence of a difference in risk to human health between approved genetically engineered crops and their conventional counterparts. It also noted that subtle or long-term effects are hard to detect.

**Reader notes, with evidence status** (for the page in a later session; none of them enters the engine):

- **Diet and long-term illness: well supported.** Suboptimal diet is linked to about $50.4 billion a year of cardiometabolic disease costs, 18% of their total (Jardim et al., PLoS Medicine 2019, a microsimulation). Higher intake of ultra-processed food is associated with 32 adverse health outcomes, and the evidence is graded convincing or highly suggestive for early death and cardiometabolic and mental health outcomes (Lane et al., BMJ 2024, umbrella review of observational meta-analyses: associations, not proof of cause).
- **Food insecurity and chronic disease: an association.** It is linked to hypertension and hyperlipidemia (Seligman et al. 2010). SNAP participation is associated with about $1,409 lower yearly health spending among low-income adults (95% interval $125 to $2,694; Berkowitz et al., JAMA Internal Medicine 2017; significant only in the fully adjusted model).
- **Pesticides and farm workers: varies by chemical.** In the Agricultural Health Study, Parkinson's disease was associated with use of paraquat (odds ratio 2.5, 1.4 to 4.7) and rotenone (Tanner et al., Environmental Health Perspectives 2011; a small study with self-reported exposure).
- **Herbicide-tolerant crops and herbicide use: mixed.** Use per hectare first fell, and the fall was generally not sustained. Heavy reliance on glyphosate bred resistant weeds (National Academies 2016).
- **Chronic conditions and spending: a figure often misquoted.** The CDC's "90% of the nation's $4.9 trillion" is spending on *people with* chronic and mental health conditions, not spending on treating those conditions.
- **Does prevention save money? Usually not.** Some preventive measures save money, but most of those reviewed do not, although many are worth their cost for the health they bring (Cohen, Neumann and Weinstein, NEJM 2008).

## 5. Health and Compassionism, against today's safety net

How much Compassionism's own effect changes when B or C replaces today's system, both with the safety net (simulated). Positive means Compassionism does less, because single payer already does part of the work. The price part is the interaction with prices free less the same with prices held flat.

| Change in Compassionism's effect | Reference | Adverse | Stress |
|---|---|---|---|
| **B: basket poverty** | **+2.3** (2.0 to 2.6); price part -0.7 | **+1.9** (1.4 to 2.5); +1.0 | +0.2 (-0.2 to 0.7); +0.5 |
| B: depth (FGT2) | +1.0 | +1.2 | +0.6 |
| B: too little wealth | -2.4 (-3.5 to -1.3) | +0.7 (-0.0 to 1.4) | +0.4 (-0.2 to 0.9) |
| B: child basket poverty | +2.6 (1.8 to 3.3) | +0.1 (-1.0 to 1.2) | -1.5 (-2.5 to -0.5) |
| **C: basket poverty** | **+1.8** (1.5 to 2.0); price part -0.5 | **+1.5** (0.9 to 2.0); +1.0 | +0.1 (-0.3 to 0.5); +0.5 |
| C: depth (FGT2) | +0.9 | +1.0 | +0.4 |
| C: too little wealth | -2.2 (-3.1 to -1.4) | +0.6 (-0.0 to 1.2) | +0.5 (-0.1 to 1.0) |
| C: child basket poverty | +2.1 (1.4 to 2.8) | +0.0 (-1.0 to 1.1) | -1.5 (-2.5 to -0.6) |

Against today's safety net the overlap is larger than session 2b found without it (B, basket poverty: Reference +1.5, Adverse +0.4, Stress -0.3). Single payer and the safety net both help the same households, so less is left for Compassionism to do. Even so, Compassionism's effect under B and C stays between 14.5 and 37.7 points in every environment (section 3). Guardrail 6 asks for gains confirmed on basket poverty and wealth poverty, not depth alone. Against setting A, B and C lower basket poverty, depth, BLEI poverty and too little wealth without the programme in every environment (section 3, and the Adverse and Stress files).

## 6. Government's share: fixed against floating

| Reference, with the safety net, with Compassionism | B fixed (main) | B floating | C fixed (main) | C floating |
|---|---|---|---|---|
| Government's share per adult-year | $2,317 | $2,338 | $2,313 | $2,336 |
| Health tax per adult-year | $6,264 | $6,243 | $6,836 | $6,813 |
| Compassionism's effect on basket poverty | -29.94 | -29.94 | -30.47 | -30.49 |

In the main runs the programme slightly *raises* Medicaid enrolment, because its income effects lower earnings a little. So fixing the share moves the health tax by $20-35 a year and Compassionism's effect by under 0.1 point in every environment. The fix matters where session 2b found it: with the BU allowance counted in the Medicaid test (`countBU`, off in every main run), the floating share made the household bill under B rise by about $700. Fixed, there is no rise (Reference, 20 seeds: $2,011 fixed against $3,051 floating; `dev/runs/health/s2cgov-ref.json`). With the share floating, every figure of session 2b's B, C and countBU rows reproduces exactly.

## 7. The speed pass: stopped, no change

A profile of a grid run (four seeds, four rows) shows the time spread across the yearly loop. The per-person loop takes 26.5% of it, and no single line takes more than 7.3%. The per-person records stay in V8's fast storage mode, so there is no structural fix to make. Memoising the expected out-of-pocket cost (2.4%) and similar steps would gain a few percent each, well under the 2x the plan asks for, so by the plan's rule the pass stopped with no engine change. The guard baseline is untouched.

**Time per run, for the Runpod estimate** (one row and one seed: 500 adults over 20 years, households, a health setting and the safety net on, the one-year pre-pass included; three runs in parallel on four cores; `_meta.perRun`): **0.375-0.427 s** with prices free, 0.376-0.436 s with prices flat, and 0.385-0.427 s with the prevention link on. The Runpod study (s137) can use **0.43 s per run per core** for health rows. Rows without a health setting are 0.35 s.

## Limits

- The Yale preprint behind B and C is not peer reviewed. MedPAC's figures are for Medicare; applying them to a layer open to everyone is an assumption.
- The safety net leaves out TANF, housing assistance, WIC, SSI and SNAP's three-month work rule. Its benefits raise essentials' prices through the model's general price rule. That route is real in the model, but its size for SNAP in the economy is not separately sourced.
- Why the safety net makes Compassionism do more under setting A (section 3) is read, not fully decomposed.
- The prevention link's central case is a design value. The high case uses associations, and one outcome (self-reported health decline) stands in for chronic onset. Diet quality beyond access, and any effect of care on how long the chronic state lasts, are not modelled.
- Under B and C, government's share is held per person at the no-programme level. If the programme changed the population's age mix, Medicare's part would be held too; in these runs both arms have the same people.
- Twenty seeds per cell. These are readings, not release figures.

## Reproduce

On this branch:

- The grid: `node dev/tools/health_check.js ENV 20 --grid --rows=SN,BSNfl,CSNfl --out=s2c`.
- With prices flat: `node dev/tools/health_check.js ENV 20 --grid --flat --out=s2cflat`.
- The prevention link: `node dev/tools/health_check.js ENV 20 --grid --rows=ASNpv,BSNpv,CSNpv,ASNpvh,BSNpvh,CSNpvh --out=s2cpv`.

ENV is `ref`, `adv` or `st` for each. Outputs are `dev/runs/health/s2c-*.json`, `s2cflat-*.json` and `s2cpv-*.json`.

- The fixed against floating check: `node dev/tools/health_check.js ref 20 --rows=off,A,B,Bfl,C,Cfl,AbuY,BbuY,BbuYfl --out=s2cgov`.
- The safety-net trace: `node dev/tools/sn_trace.js ref 20` (output `dev/runs/health/sntrace-ref.json`).

Checks: `node dev/tools/guard_test.js` (passes: every released figure identical), `node harness.js validate`, `node harness.js unit` (221 tests), `node domtest.js`, and the lineage proof recorded by `node dev/tools/engine_lineage.js prove`.
