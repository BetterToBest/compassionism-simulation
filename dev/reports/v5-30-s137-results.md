# The 500-seed study's results: health financing, the price channel and what the results depend on

Oct 13, 2026 (ledger step s137, the paid study on a rented server). This report gives the results of the study the outside audit shaped (`dev/reports/v5-29-outside-audit.md`), framed as that audit's "fix later, E" asks. No engine code changed; the page does not change. The choices made while reading the results are in `dev/DECISIONS.md`, Sessions 2f and 2g.

**How to read it.** Labels: **sourced** (from a published source), **simulated** (an output of the model's runs), **derived** (arithmetic on sourced or simulated figures), **design value** (a modelling choice, swept), **input from a preprint** (a figure taken from a study that is not yet peer reviewed). "Points" means percentage points. Every comparison is **paired**: the same 500 simulated populations (seeds 1-500, 500 adults each, 20 years) with and without the change, so a difference is not noise from different draws. Intervals are 95%. Dollars are at year-0 prices (2025 dollars). These are the study's 500-seed figures; they replace the 20-seed readings in the health reports (`v5-27`, `v5-28`).

**The three environments.** **Reference** (today's economy), **Adverse** (Reference with recession shocks, automation and 2% background inflation) and **Stress** (the Adverse economy with the programme's cautious settings: a smaller BU, a higher conversion tax, fewer octaves and lower conversion rates; its programme cost is about 40% of Reference's). Adverse and Stress share one world without the programme, so their "no programme" figures match.

**The three health settings.** **A**, today's health system; **B**, single payer with one public plan, paid by a flat health tax; **C**, single payer with Medicaid kept and a private layer paid per person (as Medicare pays Medicare Advantage). "Compassionism" means the v5.4 release row. Today's safety net (SNAP, the earned income tax credit and the refundable part of the Child Tax Credit) is on in every cell, with and without Compassionism (Duke's decision, ledger d192).

## In short

1. **Compassionism lowers basket poverty in every cell.** Basket poverty counts the adult-years spent below the cost of living (MIT's living wage; $49,370 a year for one adult, derived). In Reference it falls from about 50% to 18% of adult-years under today's health system (**-31.7 points**). It falls by 38.4 points in Adverse and 14.3 in Stress. Single payer lowers poverty before Compassionism starts, so Compassionism's own drop is about 2 points smaller under it. The level reached with both is the lowest of the three settings (15.7% in Reference).
2. **"Too little wealth" rises with Compassionism in every cell.** It rises by 9 to 12 points in Reference and by 31 to 36 in Adverse and Stress. The flat-price runs show this rise comes from the model's price response. With prices held flat it turns into a large fall (-26 points in Reference). This is the released v5.4 result. Health financing does not cause it (section 6).
3. **Single payer's results depend on the Yale preprint**, which is not peer reviewed. With its cautious savings, single payer still lowers poverty. In the high-cost case, single payer spends more per person than today's system, and setting C's comparison with B then has no savings left to measure (section 3).
4. **Today's safety net helps Compassionism a little** (basket poverty falls 1.0 more points in Reference and 2.2 more in Adverse). Its own small rise in basket poverty without the programme comes mostly through the model's prices (section 5).
5. **What the results depend on.** Participation and the BU amount explain most of the spread in every outcome. The income effect on earnings (rho) is third for poverty. The share of extra cash people spend leads for "too little wealth". The follow-up Sobol's 11 inputs add little beyond those leaders (section 8).

## 1. Poverty results

**Table 1. Basket poverty, adult-years** (simulated; no programme -> with Compassionism, and the programme's paired effect with its 95% interval):

| | Reference | Adverse | Stress |
|---|---|---|---|
| A (today's system) | 49.6% -> 17.9% (**-31.7**, -31.9 to -31.6) | 65.9% -> 27.5% (**-38.4**, -38.6 to -38.2) | 65.9% -> 51.6% (**-14.3**, -14.5 to -14.2) |
| B (single payer) | 45.0% -> 15.7% (**-29.3**, -29.5 to -29.1) | 61.1% -> 24.9% (**-36.2**, -36.4 to -36.0) | 61.1% -> 47.2% (**-14.0**, -14.1 to -13.8) |
| C (with private layer) | 45.8% -> 16.1% (**-29.8**, -30.0 to -29.6) | 62.1% -> 25.4% (**-36.7**, -36.9 to -36.5) | 62.1% -> 48.0% (**-14.1**, -14.3 to -14.0) |
| Reference line: no health setting, no safety net | 49.2% -> 19.6% (-29.6) | 66.0% -> 31.3% (-34.6) | 66.0% -> 52.3% (-13.7) |

*Caption.* Results for B and C depend on the single-payer savings taken from the Yale preprint (Galvani, Pandey, Wells and Ye, medRxiv 2026; not peer reviewed); their range is in Table 4. "With Compassionism" is the v5.4 release row. Today's safety net is on in both runs of rows A, B and C.

**Table 2. Other measures** (simulated; no programme -> with Compassionism, paired effect):

| | Poverty depth (FGT2) | BLEI poverty, adult-years | Children below the cost of living, child-years | Too little wealth, adults, year 20 |
|---|---|---|---|---|
| Reference, A | 7.2 -> 1.6 (-5.6) | 26.5% -> 11.3% (-15.2) | 77.5% -> 28.5% (-49.0) | 32.9% -> 44.9% (+12.0) |
| Reference, B | 5.6 -> 1.0 (-4.6) | 24.7% -> 10.5% (-14.2) | 69.4% -> 23.4% (-46.0) | 30.1% -> 39.2% (+9.2) |
| Reference, C | 5.8 -> 1.1 (-4.7) | 25.0% -> 10.6% (-14.4) | 70.2% -> 23.8% (-46.4) | 30.5% -> 39.9% (+9.4) |
| Adverse, A | 11.2 -> 2.5 (-8.7) | 31.4% -> 17.0% (-14.4) | 89.4% -> 39.3% (-50.1) | 44.9% -> 81.1% (+36.3) |
| Adverse, B | 9.3 -> 1.8 (-7.5) | 29.3% -> 16.0% (-13.3) | 84.1% -> 34.4% (-49.7) | 41.8% -> 78.1% (+36.3) |
| Stress, A | 11.2 -> 6.9 (-4.3) | 31.4% -> 34.6% (**+3.3**) | 89.4% -> 72.6% (-16.8) | 44.9% -> 76.3% (+31.4) |
| Stress, B | 9.3 -> 5.7 (-3.7) | 29.3% -> 32.5% (**+3.2**) | 84.1% -> 65.9% (-18.3) | 41.8% -> 73.4% (+31.6) |

*Caption.* Poverty depth (FGT2) weighs each person's shortfall below the line by its square, so the deepest poverty counts most. BLEI poverty is the share of adult-years whose savings would cover too few days of basic living. Setting C is within 1 point of B on every measure here (the full figures are in `dev/runs/s137/s137table-*.json`). "Too little wealth" rises with Compassionism in every cell, as in the v5.4 release: people in the programme hold less cash once their basket is covered. Section 6 shows that this rise depends on the model's price response. It is not caused by health financing. In Stress, BLEI poverty also rises slightly.

**How single payer changes Compassionism's effect** (simulated; the programme's effect under B or C less its effect under A, both with the safety net; positive means Compassionism lowers basket poverty by less):

| | Reference | Adverse | Stress |
|---|---|---|---|
| B against A | +2.44 (2.36 to 2.52) | +2.16 (2.07 to 2.25) | +0.36 (0.28 to 0.43) |
| C against A | +1.95 (1.87 to 2.03) | +1.69 (1.59 to 1.78) | +0.17 (0.09 to 0.24) |

Single payer has already lifted some people above the line, so Compassionism has fewer people left to lift. The combined level is still the lowest under B.

## 2. Government's costs, in a separate table

**Table 3. Costs beside the results** (simulated; per adult-year unless marked; no programme / with Compassionism):

| | Programme cost | Health tax (rate on money income) | Household health bill | Today's safety-net outlays (not financed in the model) | Government's share of the plan | Plan spending, per person-year | Paid to private plans above their enrollees' public cost, per person-year |
|---|---|---|---|---|---|---|---|
| Reference, A | 0 / $29,866 | none | $4,220 / $4,177 | $1,087 / $1,115 | (today's system) | (today's system) | |
| Reference, B | 0 / $29,901 | $6,333 (12.9%) / $6,331 (12.5%) | $2,193 / $2,242 | $1,095 / $1,110 | $2,321 / $2,321 | $6,283 / $6,282 | |
| Reference, C | 0 / $29,902 | $6,911 (14.1%) / $6,900 (13.6%) | $2,771 / $2,811 | $1,094 / $1,110 | $2,320 / $2,320 | $6,702 / $6,694 | $419 / $412 |
| Adverse, A | 0 / $28,448 | none | $3,688 / $3,658 | $1,619 / $1,612 | | | |
| Adverse, B | 0 / $28,483 | $5,503 (14.1%) / $5,476 (13.5%) | $1,687 / $1,749 | $1,620 / $1,605 | $3,176 / $3,176 | $6,301 / $6,281 | |
| Adverse, C | 0 / $28,484 | $6,021 (15.4%) / $5,982 (14.7%) | $2,205 / $2,254 | $1,620 / $1,604 | $3,176 / $3,176 | $6,677 / $6,649 | $376 / $368 |
| Stress, A | 0 / $11,691 | none | $3,688 / $3,652 | $1,619 / $1,639 | | | |
| Stress, B | 0 / $11,689 | $5,503 (14.1%) / $5,496 (14.1%) | $1,687 / $1,735 | $1,620 / $1,645 | $3,176 / $3,176 | $6,301 / $6,296 | |
| Stress, C | 0 / $11,689 | $6,021 (15.4%) / $6,005 (15.4%) | $2,205 / $2,244 | $1,620 / $1,644 | $3,176 / $3,176 | $6,677 / $6,666 | $376 / $370 |

*Caption.* The safety net's outlays are today's programmes, paid in both runs. They are not programme cost. **The model does not reconcile tax revenue with these outlays.** It reports them; it does not show that they are financed. Under A the household health bill is premiums and out-of-pocket costs. Under B and C it is the health tax less the employer's former premium share, which comes back to the household. Government's share of the plan is held at its level in the same seed's run without the programme (d194).

**Public costs avoided** (simulated, per adult-year, main estimate / high estimate, with Compassionism against without; as in the v5.4 release): Reference A $749 / $6,566, B $646 / $5,646, C $660 / $5,775. Adverse A $1,079 / $9,524, B $953 / $8,392. Stress A $488 / $4,328, B $429 / $3,797. Under B and C the hospital and emergency part is counted only once. The Yale preprint's savings already include **$100 billion of avoided emergency and inpatient care (an input from a preprint)**, so that part of Compassionism's avoided costs is counted only on the rest. This lowers B's main estimate in Reference by $2, from $646 to $644.

## 3. Single payer depends on the Yale preprint

The savings in settings B and C are inputs from the Yale preprint, not results of this model. The study ran the preprint's central case and two other cases beside it. **Cautious** is the preprint's lower bound for net savings, with the drug-price and fraud savings cut. In the **high-cost** case, providers are paid near commercial rates, so the savings vanish and only the added care remains.

**Table 4. Single payer's range** (simulated; Reference, today's safety net on; Adverse and Stress in `dev/runs/s137/s137table-adv.json` and `-st.json`):

| Cost case | Plan spending per person-year, no programme | Health tax rate | Basket poverty, no programme -> with Compassionism (effect) | Change in Compassionism's effect against A |
|---|---|---|---|---|
| Today's system (A, for comparison) | $7,748 (all payers) | none | 49.6% -> 17.9% (-31.7) | |
| B central | $6,283 | 12.9% | 45.0% -> 15.7% (-29.3) | +2.44 (2.36 to 2.52) |
| B cautious | $6,872 | 14.6% | 46.2% -> 16.2% (-30.0) | +1.75 (1.67 to 1.83) |
| B high cost | $7,905 | 17.5% | 48.3% -> 17.0% (-31.2) | +0.51 (0.43 to 0.58) |
| C central | $6,702 | 14.1% | 45.8% -> 16.1% (-29.8) | +1.95 (1.87 to 2.03) |
| C cautious | $7,331 | 15.9% | 47.1% -> 16.6% (-30.5) | +1.20 (1.12 to 1.27) |
| C high cost | $8,435 | 19.0% | 49.4% -> 17.5% (-31.9) | -0.15 (-0.23 to -0.08) |

*Caption.* Even in the high-cost case, poverty under single payer without the programme is a little lower than under today's system. The flat health tax and care free at the point of use move costs away from poor households. In that case, though, the plan costs more per person than today's system, so the result depends on the financing rule, not on savings.

## 4. Setting C's private layer: how much of single payer's savings it uses up

The share of setting B's savings (today's spending per person less B's) that setting C's payments to private plans use up (simulated; no programme; paired by seed):

| Setting C case | Reference | Adverse and Stress |
|---|---|---|
| No overpayment (diagnostic) | 0% | 0% |
| Central (55% enrolment; payment factor 1.04 x 1.11, 15.4%) | 28.7% (28.5 to 29.0) | 26.4% (26.2 to 26.7) |
| 25% enrolment | 13.2% (13.0 to 13.3) | 12.1% |
| 75% enrolment | 39.1% (38.8 to 39.4) | 35.9% |
| Coding high, selection central (1.08 x 1.11, 19.9%) | 37.0% (36.7 to 37.3) | 34.0% |
| Both high (1.08 x 1.165, 25.8%; a stress case) | 48.1% (47.7 to 48.5) | 44.2% |
| With B's cautious savings | 52.8% (52.3 to 53.3) | 49.4% |
| With the high-cost case | not meaningful: B saves nothing | not meaningful |

*Caption.* Medicare Advantage's enrolment and payment figures (MedPAC) are used as an analogue for a private layer open to all ages. They are not an estimate for all ages. The 55% enrolment and the payment factors are design values around MedPAC's figures (`v5-28`, section 1).

## 5. Today's safety net

**What the safety net changes in Compassionism's effect under A** (simulated; the effect with the safety net less without it; negative means Compassionism does more):

| | Reference | Adverse | Stress |
|---|---|---|---|
| Basket poverty | -1.01 (-1.05 to -0.96) | -2.15 (-2.21 to -2.09) | -0.20 (-0.23 to -0.17) |
| Too little wealth | +0.69 (0.64 to 0.74) | +1.01 (0.95 to 1.06) | +0.93 (0.88 to 0.99) |
| At low take-up (SNAP 75%, tax credits 70%): basket poverty | -0.80 | -1.72 | -0.12 |
| At high take-up (SNAP 95%, tax credits 90%): basket poverty | -1.15 | -2.46 | -0.28 |

*Caption.* The take-up rates are design values around USDA's 88% for SNAP and IRS's 80.8% for the EITC. The two tax credits share one take-up draw, which is a modelling assumption. Without the programme, the safety net raises basket poverty under A slightly: +0.08 points in Reference (0.07 to 0.08). **This rise comes mostly through the model's prices.** With prices held flat it is +0.02 (0.01 to 0.02). With every price response 1.5 times, it is +0.11 (0.10 to 0.11). It is a consequence of the model's price rule, not a real-world effect of SNAP. Meanwhile poverty depth falls by 0.57 points (Reference) to 1.28 (Adverse and Stress). The benefits go mostly to households far below the line.

## 6. The price channel

The model raises essentials' prices when more of them are bought, and the programme's spending also raises the general price level. The study ran the grid three ways: with prices as released, with prices held flat (no price response at all), and with every essentials' price response at 1.5 times its value.

**Table 5. Compassionism's effect under A with the safety net, by price rule** (simulated, paired):

| | Prices flat | As released | Responses 1.5 times |
|---|---|---|---|
| Basket poverty, Reference | **-37.5** | -31.7 | -31.4 |
| Basket poverty, Adverse | -36.1 | -38.4 | -38.1 |
| Basket poverty, Stress | -14.3 | -14.3 | -14.2 |
| Too little wealth, Reference | **-26.1** | +12.0 | +12.9 |
| Too little wealth, Adverse | **-24.9** | +36.3 | +36.9 |
| Too little wealth, Stress | **-9.6** | +31.4 | +31.5 |
| BLEI poverty, Stress | -8.3 | +3.3 | +3.4 |
| Price level at year 20 with Compassionism, Reference (year 0 = 1) | 1 | about 2,500 | about 2,700 |
| Programme cost, Reference | $39,499 | $29,866 | $29,799 |
| B's change to the effect on basket poverty, Reference | +3.06 | +2.44 | +2.33 |

*Caption.* The flat rows switch off every price response, including the programme's own inflation. They show what prices do in the model; they are not a scenario anyone proposes. "As released" carries the programme inflation the v5.4 release reports (prices rise about 48% a year in Reference). In Adverse and Stress, the flat runs' price level at year 20 is 1.46: the environments' 2% background inflation, which the flat rule does not remove. Programme cost is higher with prices flat; why was not decomposed in this study.

**Finding.** The rise in "too little wealth" with Compassionism comes through the price response. With prices flat it becomes a large fall in every environment. As released, programme inflation erodes cash savings, so more adults end with too little real wealth, even though their basket is covered. The v5.4 release gave this reason (`dev/reports/v5-22-v54-report.md`). These runs confirm it and measure it. Making the price response stronger (1.5 times) changes little, so what decides the result is whether the programme's inflation happens, not how strong the essentials' responses are. How strongly prices really respond to benefit-funded demand is still unsettled (outside audit, fix later F).

## 7. Smaller rows

- **Government's share floating** (the sensitivity row for d194): the health tax falls a little with Compassionism (Reference, B: $6,242 instead of $6,331). Single payer's change to Compassionism's effect (section 1) moves by 0.05 to 0.15 points on basket poverty and by 0.2 to 0.4 on too little wealth, across the three environments.
- **The prevention link** (s141, central case): Compassionism's effect under A does not move (0.00, to two decimals, in every environment). The change to the effect under B or C is 0.01 or less. As the 20-seed reading found, the chronic state is entered too slowly for the programme's exposures to move it within 20 years.
- **The safety net without a health setting** (against the reference line): Compassionism's effect on basket poverty moves -0.03 (Reference), -0.16 (Adverse) and **+0.50** (Stress). Claude's reading: in Stress, where the programme is small, the safety net and the programme reach the same households and partly overlap.

## 8. What the results depend on (sensitivity)

**Morris screening** (Morris 1991). 20 random one-at-a-time paths over 17 inputs, each path run on 20 paired seeds, in each environment. It ranks how much each input moves the programme's effect over its range. A noise check was set before the run: the seeds were split into two blocks (1-10 and 11-20), and an input's effect counts as measured only if the blocks agree to within a quarter of it.

| Outcome | Leading inputs, Stress (effect over the input's range) | Same leaders in both seed blocks? |
|---|---|---|
| Basket poverty | participation 19.6 points, BU amount 13.6, income effect on earnings 9.2, BLEI wage bonus 5.5, conversion tax 1.7, wage elasticity 1.0 | Yes, in all three environments |
| Too little wealth | share of extra cash spent 15.2, BU amount 6.3, income effect 6.3, participation 6.2, pay cut after job loss 5.9, BLEI wage bonus 2.6 | Yes in Reference and Stress; in Adverse one of six differs (BLEI wage bonus or wage elasticity) |
| BLEI poverty | participation 19.5, BU amount 9.2, income effect 2.3, pay cut 1.8, PTH uptake 1.6, BLEI wage bonus 1.0 | Yes |
| Programme cost | participation $13,867, BU amount $10,673, conversion tax $1,788, top conversion rate $1,091, PTF cut outside food and housing $1,024, PTH uptake $852 | One of six differs in Reference and Adverse (PTH uptake or PTF membership), the same in Stress |
| Programme inflation | participation 33.4 points a year, BU amount 14.7, income effect 7.8, pay cut 4.8, wage elasticity 2.4, BLEI wage bonus 2.2 | Yes |

The leaders hardly differ between environments. In Reference, the pay cut after job loss and the chance of job loss replace the conversion tax and the wage elasticity among the basket-poverty leaders (all four are minor). Each outcome had one or two inputs that did not pass the noise check, and every one of them is a minor input (for example, the yearly chance a PTH member leaves). Full tables: `dev/runs/s137/gsa-morris-*.json` and `morrisjoin-*.log`.

**The first Sobol run was too noisy for its first-order figures.** It measured Sobol indices (Saltelli et al. 2010; Jansen 1999) in Stress for v5.4's six leading inputs, with 64 base points and 10 seeds per point. A Sobol index splits the spread of a result into each input's share. The **total index** counts the input alone and together with others. The **first-order index** counts the input alone. A first-order index must lie between 0 and its total index. In the first run several did not: for too little wealth, the spending share's first-order index was -0.58 (total 0.38) and the pay cut's was 0.34 (total 0.10); for basket poverty, the BU amount's was 0.42 (total 0.27). Its first-order figures are therefore not used. Its total indices agree with the follow-up's ranking.

**The follow-up Sobol** (Session 2f's rule: run it if Morris names new leaders). It covered 11 inputs (the union of Stress's per-outcome leaders), 128 base points and 32 paired seeds per point, with 95% bootstrap intervals (1,000 resamples of the base points; Archer, Saltelli and Sobol 1997). Its raw first-order figures were still noisy (participation 1.09 for basket poverty, 1.83 for inflation). The estimator multiplies by the result itself, and the result's mean is far from zero relative to its spread (for basket poverty, a mean of -28.2 points against a spread of 7.4). Centring the result on its mean before that product removes the noise without changing what is estimated (Session 2g). The centred figures are given below. The raw ones stay in the file.

**Table 6. Follow-up Sobol, Stress** (simulated; total index, then first-order index (centred), each with its 95% interval; inputs whose total index is 0.01 or less on every outcome are left out: spending share for all but too little wealth, wage elasticity, PTH uptake, top conversion rate, PTF cut outside food and housing):

| Input | Basket poverty | Too little wealth | BLEI poverty | Programme cost | Programme inflation |
|---|---|---|---|---|---|
| Participation | **0.62** (0.50-0.78); 0.60 (0.44-0.76) | 0.13 (0.09-0.18); 0.10 (0.03-0.17) | **0.85** (0.70-1.02); 0.86 (0.69-1.02) | **0.64** (0.53-0.77); 0.64 (0.50-0.80) | **0.85** (0.71-1.03); 0.87 (0.70-1.06) |
| BU amount | **0.39** (0.30-0.50); 0.31 (0.17-0.45) | 0.12 (0.09-0.16); 0.07 (-0.01-0.17) | 0.25 (0.19-0.33); 0.17 (0.05-0.29) | **0.50** (0.40-0.63); 0.40 (0.26-0.53) | 0.20 (0.15-0.25); 0.13 (0.02-0.23) |
| Income effect on earnings | 0.10 (0.07-0.13); 0.15 (0.07-0.22) | 0.15 (0.11-0.21); 0.12 (0.03-0.21) | 0.01; 0.03 | 0.00 | 0.03; 0.00 |
| Share of extra cash spent | 0.00 | **0.46** (0.34-0.61); 0.30 (0.16-0.47) | 0.00 | 0.00 | 0.00 |
| Pay cut after job loss | 0.00 | 0.11 (0.07-0.14); 0.00 (-0.06-0.06) | 0.01 | 0.00 | 0.02; 0.04 |
| BLEI wage bonus | 0.05 (0.04-0.07); 0.07 (0.02-0.12) | 0.02 | 0.00 | 0.00 | 0.00 |
| Conversion tax | 0.01 | 0.01 | 0.00 | 0.01 | 0.00 |

*Reading.* Participation and the BU amount explain most of the spread in poverty, BLEI poverty, cost and inflation. These are design choices about the programme's size, not uncertain facts about the world. For basket poverty, the income effect on earnings (rho, sourced range 0.05-0.30) is the one uncertain behavioural constant that matters. "Too little wealth" depends most on the share of extra cash people spend (from the BEA saving rate's range of recent years), then on rho and the pay cut after a job loss. For that outcome the totals add to more than the first-order indices (1.0 against about 0.6), so the inputs act together: for example, a pay cut matters only for people near the wealth line (its first-order index is 0, its total 0.11). The inputs Morris added in Stress (conversion tax, wage elasticity, PTH uptake, top conversion rate, PTF's cut outside food and housing) each have a total index of 0.01 or less on every outcome. Morris ranked them because it measures effects over the full range, but they explain almost none of the spread. A larger Sobol run (256 base points) is not needed: the intervals already separate the leaders from the rest.

## 8b. What would have to be true (added with version 5.5.0's study page)

The study page now has a panel that says, for each headline result, what would have to be true for it to stand and what the sensitivity runs found when those inputs were varied (basket poverty needs enough take-up, the BU amount as designed and an income effect on earnings inside its range; "too little wealth" needs the model's price rule and its share of extra cash spent; and so on). Under it, a bar chart shows how much of the spread in each outcome each input explains. Every number in both comes from the Morris and Sobol results above.

**Two constants have no source.** The cost relief for community-organisation members (20% of the basket at the reference BU, ceiling 50%) and the inflation damping of the food and health programmes (0.5 and 0.1 times the share who joined). The decision log records the search for sources. This session also tested whether they matter to the released figures (`python3 dev/tools/unsourced_check.py`, result in `dev/runs/unsourced-constants-check.txt`): raising the relief from 0.20 to 0.35 changed no line of the Adverse environment's release output; raising the damping changed only the one optional row labelled "the two former stand-ins on". The test covers the Adverse environment (where outside inflation lets damping act), 4 seeds and 8 years, not the full 500 seeds; the 500-seed figures are unchanged because no engine line changed.

## 9. Limits and what is still open

- All single-payer results rest on the Yale preprint's savings, which are not peer reviewed. The range in Table 4 is the preprint's own range plus a no-savings case.
- The model does not reconcile tax revenue with today's safety-net outlays or with government's share of the plan.
- The price response drives the "too little wealth" result (section 6). The model's price rule is not calibrated to outside evidence on benefit-funded demand (fix later F).
- The cost-of-living line is the unweighted state average. A run at the population-weighted line waits (fix later A).
- SNAP's work rules and a separate Child Tax Credit take-up are not modelled (fix later C and D). The take-up rows bound the second.
- PTF's 25% health-sector cut under single payer is an upper reading (fix later B). The main rows use 0.
- **Not done: the study's comparison restudy.** The plan names it, but no file defines it, so it was not guessed. It needs its own definition before it runs.

## Where the figures are

- The health table, the price channel and the Morris runs: `dev/runs/s137/` (engine a3582e2, runner 3000ae6, Node v22.22.0, 16 cores, seeds 1-500, started 10:30 UTC Oct 13, 2026). Command `dev/tools/s137_jobs.sh /w/engine /w/res/s137-a3582e2 --max-hours=5`. Per-seed pieces in BetterToBest/compassionism-sim-results, folder `s137-a3582e2/`. All 187 hashes checked.
- The follow-up Sobol: `dev/runs/s137b/` (engine 41f2361, byte-identical page to a3582e2; runner b0a36f8; 16 blocks of 2 seeds, started 18:14 UTC, finished 18:42). Command `dev/tools/s137b_jobs.sh /w/engine /w/res/s137b-41f2361 --max-hours=3`. Block files in the results repository, folder `s137b-41f2361/`; all 17 hashes checked. The centred first-order figures are `gsa-sobol-st-sc.json`, recomputed from the same 16 block files with `node dev/tools/gsa.js sobjoin st <the 16 block files> --out=s137b-sobol-st-sc`. Its S, ST and intervals equal the pod's to the last digit.

---

The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.
