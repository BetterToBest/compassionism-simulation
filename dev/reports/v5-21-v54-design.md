# v5.4 design note: labour and markets (written before any code or run)

Oct 7, 2026 · Claude · v5.4, item 0 (`dev/plans/v5.3-plan-prompt.md`, section 4) · no code, no runs

This note fixes the design, and writes down the expected results, before anything is built or run. Each item gives the Research Hub's own words (with the paper and section), then **Claude's reading of the design**, then what the model will do. Where the Hub is silent, the most cautious option is taken and labelled a modelling assumption. Three questions are Duke's (section 2); each has a default the build proceeds on until he answers. Section 3 lists the predictions; the v5.4 report will say which held.

Every item goes behind its own switch. With every switch off, every figure is bit-identical to v5.3.1 (proved with full-output diffs and `engine_lineage.js prove`). New randomness comes from its own seeded stream, so the main stream keeps its eight draws per adult-year and the runs stay paired.

## 1. What the Hub says, and what the model will do

### 1.1 Losing a job and finding another (switch `EMPL`), instead of automation as a pay cut

- **What the model does now.** No one loses a job. In the Adverse and Stress environments an "automation wave" slows every worker's pay growth in proportion to their automation risk (Frey and Osborne's probabilities). Recessions cut everyone's income by the same share for a year.
- **The Hub's words.** *Economic Modeling and Simulation Analysis*, section 5.3, "Unemployment Shock (joblessness to 12%): CCO provides immediate income support without application delays; Creator Collectives absorb 34% of newly unemployed; PTF prevents housing displacement during job transitions". *Integrated Implementation Roadmap*, Appendix G, Recession Protocol: "Increase basic units 20%, relax requirements" at once, then "Emergency employment programs". *BLEI paper*, section 8: "automation exposure is bimodal and occupation-dependent rather than uniform — routine-manual occupations face substantially higher displacement risk". *Roadmap*, Phase 5: sector "Automation Target[s]" (health care 30-40%, infrastructure 60-70%) "and wage premiums for essential workers who remain".
- **Claude's reading of the design.** The Hub treats job loss as a spell people pass through, which BU make less damaging (income arrives without an application) and PTH makes less dangerous (people keep their homes). The "34% absorbed by Creator Collectives" is a result of the Hub's own earlier simulation, not a rule of the design, so the model does not assume it; it lets displaced participants earn through the conversion route that already exists, and reports how many do. The Phase 5 automation targets read as something the programme would pursue; whether the programme run should carry them is Duke's question (2.3).
- **What the model will do.**
  - Every working-age adult is in one of four states each year: employed, displaced (lost the job this year), searching, re-employed. Each year an employed adult can be displaced with a probability that rises with a recession and with their occupation's automation risk during an automation wave.
  - A displaced adult is out of work for part of the year (and sometimes longer), drawn from the measured length of unemployment spells; they come back at lower pay, by the measured loss for displaced workers, which is larger for those who change occupation.
  - **Occupation becomes the common cause** of pay, automation risk and hours: each adult gets an occupation group (BLS employment shares), and pay, automation risk and usual hours come from that group. This replaces the statistical link between pay and risk used in the "closer to US data" reading.
  - **Unemployment insurance exists in both runs**, as in the US: about 40-45% of lost pay for up to 26 weeks, for the share of the unemployed who actually receive it (Department of Labor's recipiency rate). It is the same in the programme run and the no-programme run.
  - **The automation wave keeps its schedule** (the years and yearly rates already in the model, design parameters already swept) but now works through job loss: its yearly rate becomes an extra chance of displacement for high-risk occupations, not a slower pay rise for everyone.
  - **No second response to BU.** Unconditional money could lengthen job search. The model already applies one income effect to every unconditional dollar (standing rule 7), so it adds no separate effect on search length: one income effect per dollar. A stated limit.
  - The Recession Protocol's 20% BU increase is already in the model (the automatic stabilisers, off in the release); "emergency employment programmes" are not modelled (no Hub detail on size or pay), a stated limit.

### 1.2 PTH as a housing balance sheet (switch `PTHB`)

- **What the model does now.** PTH members get 35% off their living costs; a quarter of that saving goes into Acre Equity, which grows 3-5% a year (more with Social Zone Harmonization) and becomes partly spendable with tenure. There is no house behind the equity: no property value, no land, no upkeep, no mortgage, and no one ever leaves PTH. The v5.3 accounting check could not test PTH's books for this reason.
- **The Hub's words.** *Transforming the US Real Estate Market*, sections 2-3: "70-80% of monthly payment → Acre Equity; 20-30% → Operating costs and reserves"; "Average 20-year accumulation: $168,000-336,000 Acre Equity; Cash equivalent: $67,000-134,000 upon exit"; "Partial Liquidity Options: Convert up to 25% annually to cash for emergencies"; "Network Portability: Move between PTH properties while maintaining equity status"; buy-in: "Trust assumes ownership and mortgage obligations". *Democratic Governance and PTH*, section 3.2: "Affordability Focus: Acre Equity appreciation capped at inflation + 2%". *PTH Independent Financing*, section 2: once mortgages are paid, "Monthly housing costs reduced to taxes, insurance, maintenance only".
- **Claude's reading of the design.** The trust owns the homes and carries their mortgages; members' payments buy down the debt and are credited as Acre Equity; a member's equity grows at most at inflation plus 2% a year; anything the homes gain beyond that stays with the community (the land and the trust). A member who leaves the network takes a cash value smaller than their credits (the Hub's figures give 40%); one who moves within the network keeps their equity.
- **What the model will do.**
  - The trust gets accounts: the value of its homes (split into building and land), its mortgage debt, members' Acre Equity, and the community's equity, with the identity *homes = debt + members' equity + community equity* checked every year (a new enforced identity beside v5.3's five).
  - Each year: home values move with prices and with real house-price growth (FHFA); upkeep (American Housing Survey) and interest (Freddie Mac mortgage rates) are paid from the 20-30% operating share; members' equity is credited and grows at most at inflation + 2%; **appreciation is reported in three parts**: general price rise, real house-price growth, and the community's share beyond the cap.
  - **The conserving reading** (`PTH_APPR_CONSERVE`, in the main result since v5.3) stays as a labelled row, beside the uncapped reading, so the effect of the cap and of the conserving rule can each be seen.
  - **Members can leave**: at the measured yearly moving rate of renters (Census, CPS ASEC). A move within the network keeps the equity (the share of moves within the same county stands in for this); a move out pays the exit value (Duke's question 2.1) and the unit goes to the next household in the waiting list (fixed at the start, so no new random draw for who gets it).
  - Nothing changes for non-members or in the no-programme run.

### 1.3 PTF members leaving as well as joining, and capacity by sector (switch `PTFS`)

- **What the model does now.** Adults join the community businesses gradually (an adoption curve) and never leave; membership takes 12% off the whole cost of living (more with Social Zone Harmonization), whatever PTF can actually supply.
- **The Hub's words.** *Glossary*, PTF: "grocers, counter-service restaurants, utility providers, transportation services, childcare centers, healthcare clinics, and educational facilities — accept basic units as payment and operate as not-for-profit". *BLEI paper*, section 3: food BU are worth 2.64 times their face value at PTF prices (ε = 2.64) and utility BU 1.80 times (ε_util, range 1.40-2.50); section 7: "Below approximately 40% PTF merchant participation in a given zone, ε falls toward 1.5-1.8×". *Glossary*, Social Zone Harmonization: communities "can withdraw".
- **Claude's reading of the design.** PTF is a set of businesses in several sectors, each of which can serve only as many people as it has capacity for; what a member saves depends on which sectors exist near them and how far each has grown. Members are customers and workers, not owners of a stake they would carry away, so leaving costs them the price cut and nothing else. The Hub gives price figures for food and utilities only.
- **What the model will do.**
  - **Five sectors**: food, utilities, transport, health care, childcare (housing is PTH, item 1.2). Each has its own price cut and its own capacity (the share of members' demand it can serve this year), grown by the capacity rule the model already has.
  - **Price cuts**: food and utilities from the Hub's ε (a price 1/ε of market's at full capacity, with the Hub's low-density figure as the lower reading); transport, health care and childcare are silent in the Hub, so they are **design parameters** with the cautious main value of no cut, swept to 12% and 25%. A member's saving in a sector is the cut times the share of their demand the sector can serve, times that sector's share of their household's basket (BLS spending shares already in the model).
  - **Leaving**: a member leaves when they move away (the Census rate of moves to another county) or when PTF has saved them less than the cost of using it for two years running (the same rule and cost the open-enrolment switch already uses for the programme). People who leave can join again through the adoption curve.
  - The 12% whole-basket cut stays as a labelled row so the change is visible.

### 1.4 Which assumptions the results depend on (global sensitivity, tool `gsa`)

- **The Hub's words.** *BLEI paper*, section 9 (second review): "the need for fuller ablation, sensitivity, and uncertainty analysis".
- **What the model will do.** First screen about 20 inputs (the design parameters and the sourced constants, each over its stated range) with the Morris method, which ranks how much each one moves the results; then measure the leading five or so with Sobol indices, which split the spread of a result into the share each input causes, alone and with others. Results are reported as **three kinds of uncertainty**: run-to-run (the same settings, different random draws), parameter (the settings within their ranges), and structural (the labelled readings, which are different models rather than different numbers). Measures: below the cost of living, too little wealth, BLEI, cost per adult, inflation, each as the paired programme-minus-no-programme difference. Budget: Reference first, 10 paired seeds per point (the paired difference is much less noisy than either run), on 4 cores; Adverse and Stress if time allows. The tool lives in `dev/tools/`; it changes no engine code.

### 1.5 Risk measures beside the stability score (switch `RISK`, reporting only)

- **The Hub's words.** *BLEI paper*, section 1: the BLEI is "a liquidity horizon measure"; *Roadmap*, Appendix I lists "Poverty rate" and "Employment" among the dashboard metrics. The Hub does not name drawdown, recovery or re-entry; these are reporting choices, not claims for the framework.
- **What the model will do.** Three measures for each run, with no effect on any person's path: **drawdown** (the largest fall in a person's real wealth, and in their BLEI days, from its earlier peak); **recovery time** (after a job loss, a recession year or a disaster, the years until income and BLEI return to their level before it, and the share not back by the end); **re-entry into poverty** (of the people who climb above the cost of living, the share who fall back within 1, 3 and 5 years, beside Stevens's PSID figures).

### 1.6 The disaster shock (switch `DIS`)

- **The Hub's words.** *Roadmap*, Appendix G, Natural Disaster Response: "Pre-Impact: Preload emergency units, suspend expiration. Impact Phase: Emergency distributions, shelter operations. Recovery: Reconstruction Collectives, enhanced PTF support".
- **What the model will do.** One disaster year (the same year, and the same people hit, in both runs): a share of households lose part of their wealth (the uninsured part of the damage) and some lose work for part of the year. Both runs receive the federal disaster aid US households get (FEMA's Individuals and Households Program, average award). The programme run adds the Hub's response: BU expiry suspended (already in the model) and an emergency distribution for that year, sized as the Recession Protocol's 20% because the Hub gives no disaster figure (a modelling assumption). Reconstruction Collectives and "enhanced PTF support" have no size in the Hub, so they are not modelled (a stated limit). The share hit and the loss are design parameters, swept (10%, 25%, 50% of households).

### 1.7 A test of the 55% floor

- **The Hub's words.** *BLEI paper*, section 7 and Table 8: "below 55% participation density, cooperative synergies do not activate"; the synergy coefficient θ "scales to 0.25 at 90%".
- **What the model will do.** The model gates θ on Social Zone Harmonization cohesion (0.72 in Reference), with the PTF-density gate as a harness reading. The test runs participation from 35% to 75% under both gates and the floor at 40%, 55% and 70%, and reports whether results jump at the floor (a cliff) or change smoothly, and what the floor means for the Stress Test's 40% participation. No result is tuned; the floor stays at 55% unless Duke changes the design.

### 1.8 What joins the main result

The rule, recorded before any run (as in v5.3): each new part joins the main result unless the restudy finds a modelling error in it; each is also shown as a labelled reading beside it, and the old behaviour (automation as a pay cut, the flat 12% PTF cut, PTH without a balance sheet) stays available as a labelled row. The sensitivity study and the 55% test are reports, not parts of the model.

## 2. The questions for Duke

These are about what the design is, so they are his. The build proceeds on the default until he answers; each is on the dashboard.

1. **What a member takes when leaving PTH.** The Real Estate paper gives a cash value of $67,000-134,000 for $168,000-336,000 of Acre Equity, that is 40%. *Default:* a member who leaves the network takes 40% of their Acre Equity in cash and the rest stays with the community; within the network, equity moves with them in full. *Alternatives:* the full equity in cash; or no cash, equity usable only within the network.
2. **How fast Acre Equity grows.** The Democratic Governance paper caps it at inflation + 2% a year; the model has used 3-5% a year plus a Social Zone bonus. *Default:* the cap (inflation + 2%), with appreciation beyond it going to the community; the old rule shown as a labelled reading. *Alternative:* keep 3-5% plus the bonus.
3. **Whether the programme pushes automation.** The Roadmap's Phase 5 sets automation targets by sector (health care 30-40%, infrastructure 60-70%) with wage premiums for essential workers who remain. *Default:* automation stays an outside condition, the same in both runs; the Phase 5 targets are not in the programme run. *Alternative:* the programme run carries the targets and the premiums (a labelled reading first).

## 3. Predictions before running

For each headline measure, the expected direction when the switch is on, against the v5.3 main result, and why. The v5.4 report will list which held.

| Item | Measure | Expected | Why |
|---|---|---|---|
| Job loss | Below the cost of living, no programme | Up 1-4 points in Reference; more in Adverse | Spells out of work push people below the line; unemployment insurance covers only some of them |
| Job loss | The programme's gain on the cost of living | Larger by 1-3 points | BU arrive during a spell; the no-programme run has only UI |
| Job loss | Too little wealth | Up in both runs; the programme's sign unchanged | Spells drain savings in both runs |
| Job loss | Inequality of income (Gini) | Up 0.01-0.03 in the no-programme run | Losses fall on a few, not on everyone |
| Job loss in Adverse | Automation wave via job loss instead of pay cuts | Mean pay ends higher, poverty about the same or higher | Most workers keep their pay growth; a minority lose a lot |
| PTH balance sheet | Members' wealth | Lower with the cap and exits | Equity growth capped at inflation + 2%; 60% kept by the community on exit |
| PTH balance sheet | Too little wealth with the programme | Up 0.5-2 points in Reference | As above; PTH members are 20% of adults |
| PTH balance sheet | Trust's identity | Holds every year; community equity grows | Appreciation beyond the cap and exit remainders |
| PTF sectors | Members' saving | Smaller than the flat 12% in the early years, similar or larger once capacity grows in food | Capacity limits; food's ε is large; other sectors' cut is zero at the cautious main value |
| PTF sectors | Below the cost of living with the programme | Up 0-2 points | Smaller saving; leavers lose it |
| PTF sectors | Members at Year 20 | 5-15% fewer | Moves out of the area and value-based leaving |
| Risk measures | Re-entry into poverty within 5 years | About half in the no-programme run (PSID: about half); lower with the programme | BU raise the floor under those who climb out |
| Risk measures | Largest drawdown of BLEI days | Smaller with the programme in Reference and Adverse, larger in Stress | Matches the BLEI results so far |
| Disaster | Recovery time | Shorter with the programme by about a year | Suspended expiry and the emergency distribution |
| 55% test | Results across participation | A visible step at the floor under the density gate, none under the cohesion gate | The gate is a step function |
| Sensitivity | Leading inputs | The BU amount, the conversion rate and the spending share lead; PTF and PTH inputs are small | The attribution study: the BU allowance carries nearly the whole effect |

## 4. Data sources (versions as of Oct 2026; exact figures pulled, cited and saved in `sources/` at build)

- **Job loss**: BLS Displaced Worker Survey, January 2024 ("Worker Displacement: 2021-2023") and Farber (2017, *Journal of Labor Economics* 35(S1)), for displacement rates in good and bad years and the pay loss on re-employment; BLS CPS unemployment duration (median and mean weeks, series LNS13008276 and LNS13008275, and the 27-weeks-and-over share), 2015-2025, recession years separated; JOLTS layoffs and discharges rate (JTS000000000000000LDR) as a check; Davis and von Wachter (2011, *Brookings Papers*) for losses by the state of the economy.
- **Occupations**: BLS Occupational Employment and Wage Statistics, May 2024, national, 22 major groups (employment, median and percentiles of pay); Frey and Osborne (2017, *Technological Forecasting and Social Change* 114) probabilities, employment-weighted to the major groups (the file already in `sources/fo_risk_wage.py`); CPS usual weekly hours by occupation group (BLS, 2024 annual averages).
- **Unemployment insurance**: Department of Labor, ETA "UI Data Summary" (recipiency rate, average weekly benefit, replacement rate), 2024-2025.
- **PTH**: FHFA House Price Index (purchase-only, US, 1991-2025) for real house-price growth; Census ACS 2024 median home value (B25077); American Housing Survey 2023 routine maintenance cost; Davis, Larson, Oliner and Shui (2021, *Journal of Monetary Economics* 118) for the land share of home value; Freddie Mac PMMS 30-year rate, 2015-2025; Census CPS ASEC 2024 geographic mobility by tenure (renters' moving rate, share within county).
- **PTF**: BLEI paper ε (food 2.64, utilities 1.80, range 1.40-2.50); BLS Consumer Expenditure Survey 2024 shares (already in the basket); CPS ASEC 2024 moves to another county.
- **Risk measures**: Stevens (1999, *Journal of Human Resources* 34(3)) for re-entry into poverty from the PSID.
- **Disaster**: OpenFEMA Individuals and Households Program awards, 2019-2024 (average amount per approved household); Census Household Pulse Survey disaster displacement items (2022-2024) for the share and duration of displacement.
- **Sensitivity**: Morris (1991, *Technometrics* 33(2)); Campolongo, Cariboni and Saltelli (2007, *Environmental Modelling & Software* 22); Saltelli et al. (2010, *Computer Physics Communications* 181) and Jansen (1999) estimators.

## 5. Build order

1. Risk measures (reporting only; needed to read the other items). 2. Job loss and occupations. 3. PTH balance sheet. 4. PTF sectors and leaving. 5. The disaster shock. 6. The 55% test. 7. The sensitivity study (after the switches are settled). 8. The 500-seed restudy (Reference, Adverse, Stress; paired; from a clean commit), the report, the version (5.4) and the pull request. Each step: switch off reproduces v5.3.1 bit for bit; the three checks pass; unit tests for the new parts; committed and pushed.

## 6. What stays the same

The 500 adults, the 20- and 40-year horizons, the three environments, the households and children of v5.3, the price rule, the financing rule, and every v5.3 reading. The no-programme run changes only where the US has the same thing (job loss, unemployment insurance, FEMA aid, house prices), so both runs face the same world.
