# Wider public costs avoided: prisons, emergency and hospital care, mental health, policing, child welfare

Session 31, Oct 2, 2026. Design note before code (ledger step s69). Written by Claude.

## What it is, in plain words

Poverty costs governments money beyond welfare: more people in prison, more emergency and hospital visits, more psychiatric care, more child welfare cases. If Compassionism lowers poverty, some of those costs fall. Session 30 counted one of them, homelessness (with the health and justice costs of homeless people), and found it saves $22 to $209 per adult a year at Reference, under 1% of the program's cost. This step adds the others Duke listed.

## The rule for every figure

Each cost needs two published numbers:

1. **What one unit costs the public** (a prison year, a hospital stay), from a primary source.
2. **How much more income actually lowers it** (a causal estimate, from an experiment or a natural experiment). A plain gap between poor and non-poor people is not enough: poor people differ in many ways, and counting the whole gap would overstate the savings.

Where no causal estimate exists, the main figure is zero and the descriptive gap is shown only as an upper bound, labelled. Where a study finds costs going up as well as down, both are shown. Effects are applied only within the income range the study observed (no extrapolation beyond it).

## Sourced figures

| Cost | Cost per unit (public) | Causal effect of more income | Main figure |
|---|---|---|---|
| **Prison** | $33,274 per state prisoner-year, 2015, range $14,780-$69,355 by state (Vera Institute, The Price of Prisons 2015, 45 states) | Losing disability income (SSI) at 18 raised the yearly chance of incarceration by 60% and criminal charges by 20% over two decades (Deshpande and Mueller-Smith 2022, Quarterly Journal of Economics 137(4)) | Applied per dollar of income, within the study's range |
| **Hospital stays** | $11,700 per stay, 2016 (AHRQ HCUP Statistical Brief); public share from HCUP payer data | A guaranteed income lowered hospitalisation by 8.5%, mostly accidents, injuries and mental health (Forget 2011, "The Town with No Poverty", Canadian Public Policy 37(3)) | Applied to adults lifted above the cost of living |
| **Emergency rooms and ambulances** | $660 (ages 18-44) and $880 (45-64) per treat-and-release visit, 2021 (AHRQ HCUP Statistical Brief 311) | No causal estimate found for adults' income | Zero; Forget's 8.5% shown as an upper bound, labelled |
| **State psychiatric hospitals** | $14.8 billion of $61.4 billion state mental health spending, FY2024 (NRI, State Mental Health Agency Expenditures and Funding Sources, FY2001-FY2024) | Forget 2011 (mental health admissions among the 8.5%) | Applied only to state psychiatric care, which the hospital row does not cover |
| **Policing and courts** | $135 billion police, $52 billion courts, 2021 (Urban Institute from Census state and local finance data) | Cash lowered property crime 8% but raised substance-related incidents 10% in the four weeks after Alaska's dividend, with no change in violence (Watson, Guettabi and Reimer 2020, Review of Economics and Statistics) | Zero main: police and court budgets are mostly fixed salaries that do not fall with a few fewer incidents. Both directions of the Alaska finding shown as a range |
| **Child welfare** | $31.4 billion, state fiscal year 2020 (Child Trends, Child Welfare Financing Survey) | Extra income randomly given to low-income mothers lowered child maltreatment risk (Cancian, Yang and Slack 2013, Social Service Review 87(3)) | Not costed: the model has no children yet (ledger step s52). Named on the page as a limit |

## Not counting things twice

- Homelessness costs already include homeless people's health and justice costs, so the new rows apply only to adults who are housed.
- The emergency room row and the hospital row are separate units (treat-and-release visits against inpatient stays); state psychiatric hospitals are outside the HCUP hospital data.
- The widely quoted $1.03 trillion cost of child poverty (McLaughlin and Rank 2018) is not added: most of it is lost earnings and costs to crime victims, not public budgets, and it concerns children.
- Lower Medicaid or SNAP spending because people earn more is a transfer change, not an avoided cost of poverty, and is not counted here.

## Where it shows

A row beside the program's cost: public costs avoided per adult a year, with the main figure and the range, by category. The page says plainly which categories are not costed and why. The expectation in the ledger (that the total strengthens the case without paying for the program) is a hypothesis; the figure is reported as it comes out.

## Switches and checks

- Switch `AVOID_WIDE` (off = session 30's homelessness-only figure). Off is bit-identical. It only reads the model's results; it changes no adult's income, so it cannot move poverty figures.
- Tests: zero income gain gives zero avoided cost; no row applies an effect beyond its study's income range; homeless adults are excluded from the new rows; the ranges' low end is never above the main figure.
- To extract at build time and cite in the code: the dollar size of the SSI loss in Deshpande and Mueller-Smith (to scale the effect per dollar), the HCUP public-payer share for adults 18-64, and the prisoner-year figure's inflation to 2025 dollars (BLS CPI-U).

## Built (session 31, Oct 2, 2026), and results

Built as `avoidWide()` in `harness.js` (reporting only: it changes nobody's income), with 3 unit tests. Two refinements to the plan above:

- **Prisons are scaled to ordinary adults.** The study's young people had a 4.7% yearly chance of being in prison; US adults overall have 0.70% (BJS, 2022: 1,827,600 people in prisons and jails). The main figure scales the study's prison cost ($0.80 per dollar of income) by 0.70/4.7, giving $0.12 per dollar of the poverty gap closed. Police and court costs ($0.29 per dollar in the study) are in the high figure only. The high figure applies the study's own $1.09 per dollar to everyone.
- **Health.** Hospital stays: about $99 saved per person-year lifted above the cost of living; state psychiatric hospitals: about $4; emergency rooms: about $16, high figure only.

Results for v5.0, per adult a year (500 runs; `dev/runs/release-panel.json`):

| | Reference | Adverse | Stress |
|---|---|---|---|
| Prisons (main) | $771 | $1,462 | $668 |
| Hospitals and psychiatric care | $34 | $37 | $13 |
| Homelessness (session 30's low-high) | $29-$283 | $27-$262 | $6-$59 |
| **All, main reading** | **$834-$1,088** | **$1,526-$1,761** | **$686-$739** |
| Share of the programme's cost | 2.8-3.7% | 5.5-6.4% | 6.5-7.0% |
| High figure (the prison study applied to everyone, plus emergency rooms) | about $7,100 | about $13,400 | about $6,100 |

In everyday words: **the public costs Compassionism avoids are real but small next to what it costs**, about 3% at Reference and 6-7% in harder times, when more people are lifted out of poverty. Prisons are most of it. Only if the largest published prison effect applied to every adult would the savings reach a quarter to a half of the cost. As expected, they strengthen the case without paying for the programme.
