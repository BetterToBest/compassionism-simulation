# Pay by household type and the child and dependent care credit in the "no programme" yardstick: what the model finds

Nov 21, 2026 · engine `e50a3b3` · preregistered before the run (BetterToBest/research-update `prereg/2026-11-s100-part-time-dcc.md`) · Claude. How the question was read before the build: [the reading note](s100-part-time-reading.md).

*Dated note (Nov 21, 2026, at the release engine, v5.9.22).* A defect in the engine affects part of this study's figures. The engine stores each seed's no-programme supply path and reuses it for later runs with the same settings, but its key left out pay by household type. The job ran its rows four groups to a process, so two readings, pay by type alone and pay by type with the credit, took the supply path of the rows before them without pay by type, in both runs of each pair. The other readings (the credit alone, the two bounds, independent partners, the credit for every family) and the rows the yardstick's decision rule reads (the no-programme rows at full take-up of the tax credits) each ran first with their own settings, so the rule's result and the choice to adopt both readings stand. Figures from the two affected readings, in sections 4 to 7, do not stand: the defect is fixed in v5.9.22 and this study is rerun in full on that engine; its figures will replace these, whichever way they move. Preregistered: research-update `prereg/2026-11-s90-private-price-at-sale.md`, Amendment 4.

## 1. What was asked

Every effect the model reports is the programme's run minus a run with no programme, the yardstick. If that run is poorer or richer than the US, the programme's effect is too large or too small. An earlier check against outside data found one gap here: the earned income tax credit (EITC) reached 11.9% of the model's adults against 15.3% in the US. The model has no part-time work, and it had no child and dependent care credit.

The reading note found that most of the gap was in how it was measured. The US figure counts every tax unit in the adult's poverty unit and assumes full take-up. Measured like for like (the adult's own tax unit, full take-up), the model gives 10.9% against 11.8%. What remained was **where** low pay falls. Every adult drew pay from one distribution, so single parents were paid like everyone else. They should be paid less: in the survey the EITC reaches half of them (49.8%) and the model reached 37%. Part-time work is already inside the yearly pay the model reads (43% of the bottom fifth of earners work part time). So the note added it as **pay by household type**, not as hours.

The study measures two additions, each behind an option that leaves today's model unchanged when off:

- **Pay by household type** (row option `eh`). Each adult keeps its place in the pay distribution, with no new random draw, but takes its household type's distribution from the Current Population Survey (CPS, 2026): single adults' median $50,000, single parents' $45,000, couples without children $65,000, couples with children $70,000. Partners' pay is correlated at 0.22, the CPS figure.
- **The child and dependent care credit** (`sn.cdc`), under tax year 2025's rules (IRS Publication 503). It is paid only to the CPS share of families who pay for care (25.5% of single parents, 32.0% of couples with children) and is claimed before the child tax credit.

Each is run on its own and together, in both designs: **full coverage** (every adult takes part) and **opt-in** (the release design). Each design runs in the Reference, Adverse and Stress environments, at 20 and 40 years, on 500 paired seeds. Three bounds were also run: partners' pay independent (correlation 0, as today); the credit read for every family with a child under 13; and the credit paid in the no-programme run only.

## 2. The answer in short

- **The yardstick is closer to the US with both additions.** At Reference and 20 years, with full take-up, EITC reach is 11.32% against 11.77%. All four household types are within 3 points of the survey (single parents 51.4% against 49.8%; couples with children 16.8% against 16.5%). The types' gaps sum to 5.1 points against 19.0 today. By the preregistered rule, Claude recommends this reading for the release's main row. Changing the main row is Duke's decision; until he makes it, the release keeps today's main row and states this study's changes as a limit.
- **The programme's effects barely move.** In the opt-in design, the programme cuts poverty slightly less in every environment and horizon. Its cut in basket poverty (adult-years below one's own cost of living) shrinks by 0.32 to 0.91 points, against cuts of 6.8 to 21.2 points: about 3% to 5% of the effect. In the full-coverage design, the cut in the share below 30 days of basic living grows by 0.41 to 0.73 points in every cell. Its cut in basket poverty shrinks by 0.15 to 0.71 points in five cells and grows by 0.18 in one (Reference, 40 years). Median wealth shows no measurable change except in one cell. Programme inflation moves by at most 0.006 points a year, in either direction.
- **Pay by household type does almost all of it.** The care credit on its own changes no effect by more than 0.02 points. The two additions' interaction is measurable in 12 of 60 tests (its interval excludes zero), but never larger than 0.005 points, which is negligible.
- **The bounds:** with partners' pay independent, the changes are larger (basket poverty up to 1.68 points), and the full-coverage change in the share below 30 days of basic living reverses sign. The correlation is sourced, so this is a bound, not the reading. The two other bounds are within 0.1 points of the main reading on every poverty outcome.
- **Two gaps remain, and are reported, not tuned:** the care credit reaches 18.3% of families with a child under 13 against 21.4% in the tax data, and pays $835 per receiving family against $606.

## 3. Checks, before any table was read

Both preregistered checks pass in all six folders. Today's main rows (no programme, full coverage, opt-in) equal the published rows with the private price at the sale on every key and every seed: 1,465,500 values per folder. Every folder has its completion mark, its run record and verified checksums. Its shards cover seeds 1-500 once, and every row has 500 values per key. The engine's guard test, unit tests (423 of 423, including the seven for these readings) and `validate` passed at the engine commit before the run.

## 4. The yardstick against US data

No-programme runs, Reference, 20 years, 500 seeds. US figures from the CPS ASEC 2026 (EITC and refundable child tax credit: the adult's own tax unit, under the Census tax model, which assumes full take-up) and IRS Statistics of Income (the care credit, tax year 2023). Gap rule, fixed in advance: a share more than 3 points from the US figure, or a dollar amount below 0.80 or above 1.25 times it.

| Measure | US | Today's main row | Both additions |
|---|---|---|---|
| EITC reach, all adults, full take-up | 11.77% | 10.90% | 11.32% |
| single adults | 8.62% | 6.30% | 9.29% |
| single parents | 49.77% | 37.99% (gap) | 51.37% |
| couples without children | 4.55% | 2.66% | 1.88% |
| couples with children | 16.54% | 19.60% (gap) | 16.76% |
| Refundable child tax credit, single parents, full take-up | 45.31% | 36.69% (gap) | 49.79% (gap) |
| couples with children | 19.00% | 21.27% | 18.64% |
| Care credit, share of families with a child under 13 (take-up as measured) | 21.37% | none | 18.30% (gap) |
| care credit per receiving family | $606 | none | $835 (gap) |
| Basket poverty, adult-years | | 36.10% | 36.34% |
| Below 30 days of basic living, adult-years | | 19.62% | 20.31% |

- **The decision rule holds:** overall reach within 3 points, all four types within 3 points (the rule needed three), and a summed gap of 5.15 points against 19.04. The size or sign of any programme effect played no part in it.
- **Couples without children** are the weakest fit with both additions (1.9% against 4.6%). Within the rule, but the model now pays them a little too well at the bottom.
- **The refundable child tax credit** now overshoots for single parents by 4.5 points (it undershot by 8.6 before). That is a gap by the rule, smaller than today's.
- **The care credit** reaches 18.3% of families with a child under 13 against 21.4%, 3.1 points short, just past the rule. With full take-up it reaches 22.7%. Its mean is 1.38 times the tax data's. The model's paying families all pay the full care price, so more of them reach the $3,000 or $6,000 limit than US families do. Both are reported as gaps; nothing was tuned.
- **The overall pay distribution is still the CPS's.** This was not in the run's output, so it is a derived calculation from the engine's four distributions, weighted by the model's household shares. The pooled distribution's quartiles and 90th percentile are within 1% of the CPS's ($36,700, $60,300, $99,000 and $155,200 against $37,000, $60,000, $100,000 and $155,000). The 10th percentile is 17% above it ($23,500 against $20,000), as with today's single distribution, because both are lognormal curves fitted to the quartiles.
- **The other environments are poorer by design**, so their reach is higher than the US's. Adverse at 20 years gives 15.4% with both additions; today's main row gives 15.0%. They are not a test of the yardstick. At 40 years in Reference, reach falls with real wage growth (10.2% with both additions, 9.8% today).

The full table, every environment and horizon, is in the tables file (section 11).

## 5. What it does to the programme's effect

Each figure is the change in the programme's effect: the programme's effect with both additions minus its effect in today's main row, paired by seed, with its 95% interval. The effect itself is the programme minus no programme, so a negative effect is a cut. A positive change means the programme cuts that measure less; a negative change means it cuts it more. Poverty is in points of adult-years; median wealth is in year-0 dollars; inflation is in points a year. **Bold:** the interval excludes zero after correcting for testing five outcomes in each row (Holm). Inflation is shown to four decimals from `s100-summary.json`; the tables file rounds it to three, where several of these print as 0.000.

**Full coverage**

| Environment, years | Effect today: below 30 days | Change: below 30 days | Effect today: basket poverty | Change: basket poverty | Change: too little wealth | Change: median wealth ($) | Change: inflation |
|---|---|---|---|---|---|---|---|
| Reference, 20 | −18.80 | **−0.54 (−0.59 to −0.48)** | −32.95 | **0.15 (0.08 to 0.21)** | 0.02 (−0.04 to 0.07) | 541 (−662 to 1,763) | **0.0062 (0.0059 to 0.0064)** |
| Reference, 40 | −18.94 | **−0.73 (−0.78 to −0.68)** | −31.01 | **−0.18 (−0.23 to −0.13)** | **−0.32 (−0.38 to −0.27)** | **−2,531 (−4,776 to −420)** | **0.0032 (0.0031 to 0.0033)** |
| Adverse, 20 | −19.91 | **−0.44 (−0.49 to −0.38)** | −41.21 | **0.61 (0.54 to 0.69)** | **0.11 (0.06 to 0.17)** | 199 (−961 to 1,361) | **−0.0005 (−0.0006 to −0.0004)** |
| Adverse, 40 | −23.00 | **−0.42 (−0.47 to −0.37)** | −46.40 | **0.63 (0.57 to 0.69)** | −0.03 (−0.08 to 0.03) | −470 (−2,458 to 1,445) | **−0.0002 (−0.0002 to −0.0002)** |
| Stress, 20 | −19.91 | **−0.43 (−0.49 to −0.38)** | −40.72 | **0.64 (0.58 to 0.71)** | **0.15 (0.09 to 0.21)** | 669 (−488 to 1,793) | **−0.0005 (−0.0006 to −0.0005)** |
| Stress, 40 | −22.99 | **−0.41 (−0.46 to −0.36)** | −45.69 | **0.71 (0.65 to 0.77)** | 0.05 (−0.01 to 0.11) | 471 (−1,445 to 2,284) | **−0.0002 (−0.0003 to −0.0002)** |

**Opt-in**

| Environment, years | Effect today: below 30 days | Change: below 30 days | Effect today: basket poverty | Change: basket poverty | Change: too little wealth | Change: median wealth ($) | Change: inflation |
|---|---|---|---|---|---|---|---|
| Reference, 20 | −12.51 | **0.18 (0.13 to 0.24)** | −21.18 | **0.81 (0.74 to 0.88)** | **0.29 (0.23 to 0.35)** | −21 (−1,190 to 1,204) | **0.0031 (0.0028 to 0.0033)** |
| Reference, 40 | −13.64 | **0.11 (0.06 to 0.17)** | −20.11 | **0.58 (0.52 to 0.63)** | **0.30 (0.24 to 0.36)** | −1,267 (−3,416 to 725) | **0.0020 (0.0018 to 0.0021)** |
| Adverse, 20 | −10.82 | **0.27 (0.21 to 0.33)** | −19.10 | **0.91 (0.84 to 0.97)** | **0.33 (0.27 to 0.40)** | −300 (−1,430 to 796) | **−0.0057 (−0.0059 to −0.0055)** |
| Adverse, 40 | −11.31 | **0.38 (0.32 to 0.44)** | −16.75 | **0.76 (0.70 to 0.81)** | **0.40 (0.34 to 0.47)** | −98 (−1,849 to 1,649) | **−0.0025 (−0.0026 to −0.0023)** |
| Stress, 20 | −4.38 | **0.13 (0.08 to 0.17)** | −7.77 | **0.36 (0.31 to 0.41)** | **0.18 (0.13 to 0.23)** | −16 (−970 to 923) | **−0.0041 (−0.0044 to −0.0038)** |
| Stress, 40 | −4.61 | **0.16 (0.12 to 0.20)** | −6.78 | **0.32 (0.28 to 0.35)** | **0.18 (0.14 to 0.23)** | −478 (−1,936 to 1,050) | **−0.0001 (−0.0001 to −0.0000)** |

In plain words:

- **Opt-in:** in every environment and horizon, the programme cuts all three poverty measures a little less: below 30 days of basic living by 0.11 to 0.38 points less, basket poverty by 0.32 to 0.91, and too little wealth by 0.18 to 0.40. These are unfavourable to the programme. They are about 3% to 5% of its effect on basket poverty.
- **Full coverage:** the programme cuts the share below 30 days of basic living by 0.41 to 0.73 points more in every cell. That is favourable to the programme. Basket poverty is cut by 0.15 to 0.71 points less in five cells (unfavourable), and by 0.18 points more in Reference at 40 years. Too little wealth is cut less in Adverse and Stress at 20 years (0.11 and 0.15 points), more in Reference at 40 years (0.32), with no measurable change in the other three cells.
- **Median wealth:** no measurable change in 11 of 12 cells. In the full-coverage design in Reference at 40 years, the programme's gain in median wealth is $2,531 smaller (interval $420 to $4,776), against a gain of $443,135.
- **Inflation:** measurable in every cell but at most 0.006 points a year in either direction, which is immaterial.

**Why, in Claude's reading (an interpretation, not a measured result).** With pay by household type, single parents are paid less and couples with children more. With no programme, more adult-years fall below 30 days of basic living (20.31% against 19.62%, Reference, 20 years). Full coverage pays every adult, so it catches the added shortfall and its cut on that measure grows; the opt-in design reaches only those who opt in, and its cut shrinks. This study does not split the basket-poverty changes by household type, so why they shrink in most cells is not established here.

**The care credit on its own** changes no poverty effect by more than 0.02 points and median wealth by no more than $74. Its changes are measurable only because the seeds are paired. Its contribution is to the yardstick, not to the programme's effect.

The secondary outcomes (deep poverty, cost, median income, wealth poverty in the last year, families in debt, and each tax credit's dollars) are in the tables file. With both additions, the programme's cost changes by −$13 to −$26 per adult a year in the full-coverage design and by +$11 to +$61 in the opt-in design.

## 6. Do the two additions interact?

The interaction is (both − the credit alone) − (pay by type alone − today's): what the two do together beyond the sum of the two alone. Its interval excludes zero in 12 of the 60 tests (five outcomes in twelve cells). The largest is 0.005 points of basket poverty, 0.004 points of the share below 30 days of basic living, and $59 of median wealth. A synergy is stated only where the interval excludes zero. These do, so they are stated here, with their size: about a hundredth of the changes above, and negligible beside the programme's effect.

## 7. The bounds

Change in the programme's effect on basket poverty (points), main reading and the three bounds (bold: Holm-adjusted interval excludes zero):

| Design, environment, years | Both | Partners independent | Credit for every family | Credit in the no-programme run only |
|---|---|---|---|---|
| full coverage, Reference, 20 | **0.15 (0.08 to 0.21)** | **1.10 (1.03 to 1.17)** | **0.14 (0.07 to 0.20)** | **0.14 (0.08 to 0.20)** |
| full coverage, Reference, 40 | **−0.18 (−0.23 to −0.13)** | **0.73 (0.68 to 0.78)** | **−0.19 (−0.24 to −0.14)** | **−0.18 (−0.23 to −0.13)** |
| full coverage, Adverse, 20 | **0.61 (0.54 to 0.69)** | **1.63 (1.56 to 1.70)** | **0.62 (0.55 to 0.69)** | **0.61 (0.54 to 0.68)** |
| full coverage, Adverse, 40 | **0.63 (0.57 to 0.69)** | **1.60 (1.54 to 1.65)** | **0.64 (0.58 to 0.70)** | **0.62 (0.56 to 0.68)** |
| full coverage, Stress, 20 | **0.64 (0.58 to 0.71)** | **1.66 (1.59 to 1.73)** | **0.63 (0.57 to 0.71)** | **0.63 (0.56 to 0.70)** |
| full coverage, Stress, 40 | **0.71 (0.65 to 0.77)** | **1.68 (1.62 to 1.73)** | **0.70 (0.64 to 0.76)** | **0.70 (0.64 to 0.76)** |
| opt-in, Reference, 20 | **0.81 (0.74 to 0.88)** | **1.52 (1.45 to 1.59)** | **0.84 (0.77 to 0.90)** | **0.89 (0.82 to 0.95)** |
| opt-in, Reference, 40 | **0.58 (0.52 to 0.63)** | **1.28 (1.23 to 1.33)** | **0.60 (0.55 to 0.65)** | **0.64 (0.59 to 0.69)** |
| opt-in, Adverse, 20 | **0.91 (0.84 to 0.97)** | **1.31 (1.23 to 1.38)** | **0.92 (0.85 to 0.99)** | **0.98 (0.91 to 1.05)** |
| opt-in, Adverse, 40 | **0.76 (0.70 to 0.81)** | **0.98 (0.93 to 1.05)** | **0.78 (0.72 to 0.83)** | **0.82 (0.76 to 0.88)** |
| opt-in, Stress, 20 | **0.36 (0.31 to 0.41)** | **0.50 (0.44 to 0.55)** | **0.39 (0.34 to 0.44)** | **0.41 (0.36 to 0.46)** |
| opt-in, Stress, 40 | **0.32 (0.28 to 0.35)** | **0.37 (0.33 to 0.41)** | **0.33 (0.29 to 0.37)** | **0.35 (0.31 to 0.39)** |

- **Partners' pay independent** (today's assumption, applied to the new distributions) gives the largest changes. It also reverses the full-coverage design's change in the share below 30 days of basic living: from 0.41 to 0.73 points more cut to between 0.00 and 0.26 points less. With independent pay, fewer couples have two low earners, so with no programme fewer adults are poor (basket poverty 35.4% against 36.3%, Reference, 20 years) and the programme has less to cut. The 0.22 correlation is the CPS couples' figure, so this is a bound on the reading, not a rival reading.
- **The credit for every family** with a child under 13 and **the credit paid only in the no-programme run** are both within 0.08 points of the main reading on basket poverty, and within 0.04 points on the share below 30 days of basic living. Paying the credit only in the no-programme run doubles the change in inflation (0.014 points a year in full coverage, Reference, 20 years), which is still immaterial.

## 8. What this means, and its limits

The yardstick check found the model's no-programme run too uniform: single parents too well paid, couples with children too poorly paid. Fixing that brings the EITC, the child tax credit and the share of families paying for care close to the survey. It moves the programme's poverty effects by under a point, in the unfavourable direction for the opt-in design. For the full-coverage design it moves them in both directions, depending on the measure. No headline result changes sign or loses significance: every programme effect on the three poverty measures keeps its interval clear of zero under every reading.

**The main row.** By decision rule 2, Claude recommends both additions for the release's main row. That is a change to the main row, which is Duke's decision. Until he decides, the release keeps today's main row and states, as a limit, that pay by household type and the care credit would change the programme's effects by the amounts in section 5.

Limits, stated in advance or found here:

- Pay by household type sets who has low yearly pay; it does not model a choice of hours. Hours that respond to the programme, to taxes or to the cost of care enter only through the labour response, which acts on yearly pay.
- Hours are not modelled separately. SNAP's 20-hour work rule is read as met by any week at work, which affects about 3% of earners (the reading note).
- The care credit's mean is 1.38 times the tax data's, and its reach is 3.1 points short. Families in the model pay the full price of care. Families who pay less, or who use a dependent care account at work, are not represented.
- Each type's pay is a lognormal curve fitted to its quartiles. The bottom tenth of pay is 17% too high overall, as it is today.
- Household types are fixed for the run. No one marries, separates or has a first child, so moves between types are not represented.
- The seed intervals cover the model's randomness only, not the choice of reading. The bounds in section 7 show that.

## 9. Text for the findings page

> **The yardstick: pay by household type and the child and dependent care credit.** Every effect here is the programme against a run with no programme, so that run should look like the US. It now gives each household type its own pay from the Current Population Survey. Single parents are paid less and couples with children more, as in the survey, and the overall pay distribution still matches the survey's closely (its bottom tenth is somewhat high, as before). It also adds the child and dependent care credit. With both, the EITC reaches 11.3% of adults (US 11.8%, on the same basis: each adult's own tax unit, full take-up) and every household type is within 3 points of the survey. In today's main row, single parents were 12 points short. The care credit's reach is 3 points short of the tax data, and its average is $835 against $606; both are reported as gaps. The programme's effects barely move. In the opt-in design, its cut in basket poverty is 0.3 to 0.9 points smaller in every environment and horizon (3% to 5% of the effect). In the full-coverage design, its cut in the share below 30 days of basic living is 0.4 to 0.7 points larger, and its cut in basket poverty is 0.2 to 0.7 points smaller in five of the six cells (0.2 points larger in the sixth). Median wealth and inflation do not change materially. The credit alone changes no poverty effect by more than 0.02 points, and the two additions' interaction is negligible (at most 0.005 points). With partners' pay drawn independently rather than correlated as in the survey, the changes are larger (up to 1.7 points of basket poverty). Claude recommends the new reading for the main row; changing it is Duke's decision, and until then these changes are stated as a limit.

## 10. Where everything is

- **Preregistration:** research-update `prereg/2026-11-s100-part-time-dcc.md`.
- **Engine:** `e50a3b3`; row option `eh` (pay by household type), `sn.cdc` (the care credit), `sn.rep` (reporting by household type). Sources: `sources/s100_earnings_by_household.py` and `.json`. The reading note: [s100-part-time-reading.md](s100-part-time-reading.md).
- **Job:** compassionism-sim-results `runner/jobs/s100.js`.
- **Outside readings before publication** (two readers from makers other than Claude, Google's Gemma and NVIDIA's Nemotron; readings, not reviews): research-update `audits/2026-11-21-s100-results-reading.md`, with each point, what it was checked against and what changed.
- **Results:** `s100-{ref,adv,str}-{20,40}-e50a3b3` (run-study runs 173-178), each with `run.txt` and `SHA256SUMS`.

## 11. The tables

`s100-tables-e50a3b3` in compassionism-sim-results (`python3 dev/tools/s100_tables.py <results> <out> --engine e50a3b3`; the tool was written before any result was read): `s100-tables.md` (checks; the yardstick in every environment and horizon; every effect, change, bound and interaction; secondary outcomes) and `s100-summary.json` (every figure with its interval and Holm-adjusted p). The page's data: `data/studies/s100-yardstick.json` and `s100-effects.json` (`python3 dev/tools/s100_page_data.py <tables>/s100-summary.json`).
