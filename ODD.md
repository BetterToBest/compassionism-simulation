# ODD protocol: the Compassionism Simulation, v5.9

Structured after Grimm, V., Railsback, S. F., Vincenot, C. E., et al. (2020), "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism", *Journal of Artificial Societies and Social Simulation* 23(2), 7.

**What this describes (rebuilt for v5.9, Nov 17, 2026).** v5.9 is the current release: engine commit `104691f`, frozen and registered on OSF before it ran on Nov 14, 2026 (osf.io/msdzk), shown on the simulation and findings pages since v5.9.0. The model is a **dynamic microsimulation with a reduced-form price level**: 500 simulated US adults and their children, in households, followed year by year with and without the programme on the same random draws; the programme's institutions, firms and the government appear as aggregate flows, and prices move by a rule fitted to the economy as a whole, not by markets between agents. The full equations are in [MODEL_SPEC.md](MODEL_SPEC.md) (v5.9's main row: sections 10, 13 and 14; the central-bank and history studies: sections 15 and 16); every switch and its value in v5.9's main row is in [TESTBED_SPEC.md](TESTBED_SPEC.md), section 0; [REPRODUCE.md](REPRODUCE.md) gives the commands and fingerprints of every v5.9 result; [model-card.html](model-card.html) is a one-page summary of what the model is and is not. Before Nov 17, 2026 this file described v5.2; the v5.2 parameter table is kept below (section 6.2) as written, because most of its values still hold in v5.9.

Authors: the concepts are Duke Johnson's (*Better To Best*; Research Hub, bettertobest.github.io/research-hub/); the math and code were engineered by Claude, an AI model made by Anthropic. The model has not yet been reviewed by an independent economist. Code: Apache-2.0; documentation: CC BY 4.0. DOI 10.17605/OSF.IO/QWTE2.

## 1. Purpose and patterns

**Purpose.** To show what the Compassionism framework's rules imply, as specified on the Research Hub, for poverty, basic living, savings, work, prices, cost and the distribution of wealth in a population of US adults and their children, against no programme, under three economic environments; and to make each assumption visible and testable by holding every alternative reading behind a switch. The model is a design-exploration tool, not a forecast.

**The headline condition.** v5.9's main row assumes **full backing**: every dollar the programme pays is matched by new output, as the design states. This is a design parameter, not something the model shows: the model's own mechanism for new output reaches about 1% of the payout. Below full backing the model has **no limit on what the economy can supply**: demand never runs into what can be produced, wages follow prices in full, and the Basic Unit and the cost-of-living basket follow the same prices. That is why the poverty effects barely depend on backing while inflation and median wealth do (the backing curve, at backed shares 0, 0.25, 0.5, 0.75 and 1, is published beside the main row).

**Patterns used to evaluate the model** (each gap is reported, not tuned away). (1) The no-programme run against US data: the starting top 1% share of wealth (30.1% in the model with the weighted top tail, 31.5% in the SCF 2022); wealth and earnings by household from the SCF 2022 and CPS ASEC; labour-force status, exits and returns from linked CPS ASEC 2025-2026; the share below the official poverty line; poverty spells (PSID). (2) The participation margin against the US guaranteed-income experiment (Vivalt et al.): the model's effect on participation is −1.3 points (interval −7.5 to −0.9). (3) The Research Hub's own Year 7 targets, reported beside the model's figures. (4) Internal accounting: every identity of MODEL_SPEC section 11 holds every year (unit and on-together tests).

## 2. Entities, state variables and scales

**Entities.** Adults (500, the agents), grouped into households with their children (about 170; children do not decide). Of the 500, 18 stand for the top tail of wealth (a Pareto tail fitted to the SCF above the 97.5th percentile) and carry small population weights; every other adult's weight makes the types sum to their share of US adults. **Weights enter measures and the government's and creditors' books only, never a decision.** The programme's institutions (the Source that issues Basic Units, essential-service providers including community-owned PTFs, project collectives, community housing), businesses, lenders and the government are aggregate flows and accounts, not agents. The environment is a recession path, outside inflation, an automation wave and the price level.

**Adult state variables.** Wage, labour-force status (in, or out for a reason: disability, early retirement, care, school, other) with its own income; net wealth held by asset class (home, other real estate, shares, private business, other goods, nominal assets, fixed-rate and floating debt) and business ownership; a borrowing limit; automation risk; octave, quality and advancement parameter; programme participation, PTF membership, PTH residence, Acre Equity and PTH tenure; a personal participation-margin draw; the weight. Full table: MODEL_SPEC.md sections 3 and 14.

**Global state.** The pools and accounts of the v5.6 model (expired-BU project pool, ESP payroll pool and premium, PTF capital and capacity, the PTF share of essential sales, PTF running costs), the general price level, essentials prices and the basket index, the BU's indexed level, the creditor totals, the government account (contribution, programme debt, interest), ledgers.

**Scales.** Time step one year; horizon 20 years or 40. No space (zones act through a coherence parameter and the realised PTF density). Money in nominal US dollars, reported in year-0 (2025) dollars by the model's own price level. The main row's population is fixed: no births, deaths, ageing, partnerships or separations (ageing is a reading).

## 3. Process overview and scheduling

Each year, in this order (MODEL_SPEC.md section 5 gives every step; section 14.0 where each part added for v5.9 acts):

1. **Set-up**: the year's recession multiplier and automation drag; the cost of living (MIT basket × price level); the BU's indexation; the spending layer in recessions; the PTF share's growth (as far as owned capital, operations and a demand ceiling allow; it never falls) and PTF running costs; open enrolment; last year's expired BU allocated to project work; ESP payroll; last year's business premium split; the creditor totals.
2. **Each adult, in array order**: movement in or out of the labour force; eight random draws on the main stream in a fixed order (the common-random-numbers guarantee; the added parts have their own streams); income shock and job loss; BLEI gate; wage growth (wages follow the price level in full); the bargained raise (zero at the main pass-through); price cuts on the adult's basket (open PTF access: the zone's PTF share at PTF prices); BU purchases of essentials (the rest expire); earnings and the labour response (one income effect per unconditional dollar, split between leaving work and working less); payouts and today's safety net; project and payroll conversion; octave advancement; PTH equity; the spending rule (87.7% of the cash surplus consumed; a household that would spend more than its income draws on savings and a $2,500 borrowing limit, then cuts spending); wealth revalued by asset class and capital income paid; accounting.
3. **Close**: businesses convert the BU they accepted; the government account; year-end reporting; the price step (unmatched new money moves the general price level: at full backing almost none is unmatched; demand above capacity moves essentials prices; the basket index is recomputed); the financing identity.

Adults are updated sequentially within a year; between-adult interaction otherwise runs through year-level aggregates computed before or after the adult loop.

## 4. Design concepts

- **Basic principles.** The framework's architecture (Research Hub): a monthly allowance of Basic Units (BU) that buy only essentials and expire; expired BU converted to dollars at rates earned through community-valued work (octaves, multipliers to 9×, the Phi tier, a progressive conversion tax); community-owned essential-service providers (PTFs) that share their premium as lower prices, reinvestment and a profit share; community housing (PTH) whose payments build equity; zone coordination (SZH); a civic platform (CIP). v5.9 leads with **the full-coverage design** (built to meet NEEC's criterion C2.2: unconditional provision covering 100% of basic needs for everyone; the BU set at each household's needs, everyone enrolled) and shows **the opt-in design** ($1,200 a month, 78% taking part in Reference) beside it. Around it, standard economic modules: a quantity-theory price rule for unmatched new money, an essentials price response to demand above capacity, a labour-supply response (Chetty 2012; Vivalt et al.), household balance sheets by asset class (SCF 2022), and a government account.
- **Emergence.** Poverty, the price level, programme cost, the distribution of wealth, participation, the PTF share and the government's books emerge from the adults' rules and the aggregate pools; prices feed back into every adult's cost and the BU's indexation.
- **Adaptation.** Adults join or leave the opt-in programme when the BU they would use is worth more or less than the revealed cost of taking part; take project work when it pays more after tax than their own wage; adjust earnings to programme income (and some leave work for the year); households borrow to their limit, then cut spending. No other optimisation.
- **Objectives, learning, prediction.** Implicit in the rules above; no learning; no expectations (decisions use last year's or this year's known values).
- **Sensing.** Adults know their own wage, cost, BU value and rates.
- **Interaction.** Indirect, through pools (expired BU fund other adults' projects; BU spent at ESPs fund ESP payroll and PTF price cuts), PTF capacity and adoption, the creditor side (who loses when inflation erodes fixed-rate debt) and prices.
- **Stochasticity.** Starting attributes are drawn per adult; each year eight uniforms per adult on the main stream, plus the added parts' own streams (labour-force flows, the participation margin, the tail, business owners; MODEL_SPEC 8 and 14.12); recessions. The programme and no-programme runs use the same draws (common random numbers).
- **Collectives.** Households pool their money and decide together; the programme's participants, PTF members, PTH residents and ESP workers are groups defined by state.
- **Observation.** Per study: means over 500 paired seeds (100 in the central-bank and history studies), paired differences with 95% intervals (seed bootstrap), each outcome across the 62 preregistered readings (specification curves) and along the backing curve. **Each published measure says how it counts the adults:**
  - *unweighted* (each of the 500 simulated adults counted once, the 18 tail adults included): the share of adult-years below the cost of living (basket poverty), below 30 days of basic living, with too little wealth (yearly average and at the end), employment and hours, the suite page's plain shares and tiers. Counted by weight they differ by up to about 0.6 points in a single year, less than the spread across runs.
  - *weighted* (each adult at its population weight): median real wealth, participation, adult-years outside the labour force, programme leavers and their earnings forgone, the distribution measures (top 1% and 10% and bottom half shares, percentiles, mobility, debt, labour's share), the central-bank and history studies' stability and who-gains measures, the suite page's weighted averages and medians.
  - *weighted in the accounts*: the government account's contribution and its base, and the creditor totals, are weighted sums; the payout, prices and every decision count each adult once, so programme inflation and the cost per adult are unweighted (a limit, MODEL_SPEC 14.14).
  - *BLEI* is the days of basic living that an adult's savings, income and BU together cover (the BLEI paper's definition); it is a capacity measure, not cash on hand.

## 5. Initialization

Per seed, from the construction stream: households formed as US adults live with their children; each household's wealth drawn from the SCF 2022 by household type and split into asset classes by wealth group (with business owners); earnings from CPS ASEC; the outside-the-labour-force draw by reason; the top tail (three households per type above the 97.5th percentile, with weights); automation risk; octave, quality and λ; participation, PTF and PTH uniforms. They are instantiated identically into the programme and no-programme runs. Pools start empty, prices at 1. The recession path is drawn once per seed. MODEL_SPEC sections 4, 6.13, 14.4, 14.6 and 14.8.

## 6. Input data

No time-series input drives the main row during a run. Fixed inputs: the MIT living-wage basket and its components (by household type); CPS ASEC 2023-2026 (earnings, labour-force status and own incomes by reason, yearly exits and returns); the SCF 2022 and 2025 (balance sheets by wealth group, business ownership, capital income, unsecured debt, the tail); the Fed's Financial Accounts 2022 (who holds household debt); Shiller (real price gains); Drechsler, Savov and Schnabl 2017 (deposit rates); Smith, Zidar and Zwick 2023 (top returns); Azar, Berry and Marinescu 2022 and Yeh, Macaluso and Hershbein 2022 (markdowns); BEA, Census, BLS and EIA (PTF running costs, payroll and jobs; the saving rate behind the spending share); Frey and Osborne (automation); the 2025 official poverty threshold; HUD homelessness counts; Treasury and BEA (today's federal debt and GDP per adult). The central-bank and history studies add the actual US paths of 2005-2025 and of four policy eras since 1946 (CPI-U, home and share prices, the federal funds rate, the 30-year mortgage rate, recessions, real family income; Piketty, Saez and Zucman's tax rates; medical inflation). Each figure is given as read in its report in `dev/reports/`.

### 6.1 Parameters that v5.9 changes or adds (against the v5.2 table below)

| Parameter | v5.9's main row | Basis |
|---|---|---|
| Backing of the programme's payout (`o.a`) | 1: every dollar matched by new output (v5.2: 0) | Design (the design's statement); a design parameter, read along 0-1 |
| The programme | the full-coverage design, with the opt-in design beside it (v5.2: the opt-in design) | Design (NEEC's criterion C2.2; Hub) |
| Spending rule | 87.7% of the cash surplus consumed (v5.2: 59.3%) | Derived: the BEA 2025 saving rate re-derived on the frozen no-programme run (MODEL_SPEC 13.3); 59.3% is a reading, and the largest mover of median wealth |
| Wages, wealth | CPS earnings; SCF 2022 wealth by household and asset class, with a weighted Pareto tail (exponent 1.490, standard error 0.136) (v5.2: lognormals) | Sourced |
| Wage indexation to prices (`wIdx`) | 1 (full) | Assumed; the largest mover at no backing |
| Labour force | adults out by reason; yearly flows that keep each cell's share; participation margin 0.43 (the extensive share of Chetty's elasticities) | Sourced (CPS ASEC; Chetty 2012) |
| Borrowing limit for ordinary spending | $2,500 | Sourced and swept: the median unsecured debt of families aged 25-64 in the bottom 40% of income who hold any (SCF 2025); a design parameter read at 0, 5,000, 8,700 and 10,000 |
| Asset returns | real gains by class (Shiller), nominal assets 0.46 of inflation, floating debt 1, fixed-rate debt 0 (eroded by inflation) | Sourced; the creditor side read five ways |
| Bargaining pass-through | 0 (markdown 1/1.21) | Sourced (the evidence gives about 0) |
| PTF access, running costs, demand ceiling | open; costs from BEA, Census, BLS, EIA; ceiling 49% | Sourced |
| PTH equity routing | "25% of the PTH saving" to equity, but the saving is measured at the BLEI daily cost ($68.33 a day) rather than the basket the cut applies to, so a member routes 12.6% of its actual PTH saving (money is conserved either way; a basket-based base is a planned reading) | Design (internal design choice) |
| Population | fixed (no ageing) | Modelling assumption; ageing is a reading |


### 6.2 The v5.2 parameter table, kept as written (Oct 2026)

Basis: **sourced** (a cited primary source), **derived** (computed from sourced figures), **design** (a policy lever of the framework, from the Hub or a recorded decision; swept where it matters), **assumed** (no evidence; labelled, swept or kept off the main result unless costed).

| Parameter | Value (reference) | Basis |
|---|---|---|
| Living-wage basket, one adult (`LIVING_WAGE_ANNUAL`) | $49,370 a year | Sourced: MIT Living Wage Calculator (Feb 2026), 51-jurisdiction unweighted mean × 2,080 h. The population-weighted $51,201 is a candidate for v5.3. |
| Basket shares (`CFG.BASKET`) | food 9.0%, housing 27.6%, medical 6.9%, transport 19.6%, civic 6.6%, internet 3.1%, other 9.2%, taxes 18.0% | Derived: MIT state pages, components regressed on totals |
| Wage scale (`WAGE_TO_USD`) | $100.52 per SIU-month | Derived: CPS ASEC 2023 median personal income $42,220 / (35 × 12) |
| Wage distribution | lognormal(3.5, 0.5): median $39,945 | Assumed (framework spec); below the US spread; readings in v5.2 |
| Starting wealth | lognormal(10.5, 1.2): median $36,316 | Assumed; cited as SCF 2022 but below it (open; SCF reading in v5.2; v5.3 calibration) |
| Wealth line (`POVERTY_LINE`) | $25,000 (moved with prices) | Design threshold: origin undocumented; read as about six months of one adult's MIT cost of living ($24,685); households: six months of their own costs (v5.3) |
| Official poverty threshold | $16,749 (2025, one person under 65) | Sourced: Census, via CRS IN12737 |
| BLEI lines | 30 days (precarious), 7 (crisis) | Design: BLEI paper |
| BLEI daily cost | $68.33; $31.67 for participants in PTH | Sourced (BLS CES 2023); design (BLEI paper §3.2) |
| Monthly BU | $1,200 ($900 Stress) | Design (Hub) |
| Participation at the start | 78% (40% Stress) | Design reference (Hub minimum 55%) |
| Octaves, multipliers | 6 octaves, up to 9× (4, 6× Stress); capacity 1,000 × 2^octave BU a month | Design (Hub) |
| Phi tier | ×1.618 above quality 0.70 × maximum | Design (Hub: the tier); assumed (the threshold's place) |
| Conversion tax | 12% (18% Stress), +4 points per rate point above 3×, capped at 75% | Design (Hub's 12%); assumed (progression) |
| Business conversion rate | 3× on all BU accepted | Assumed placeholder (Hub café example 2-4×) |
| BU indexation | to prices in any year they rise faster than 5% | Design (Hub, Inflation Surge Protocol) |
| PTF price cut | 12% + 4% × SZH coherence of the non-tax basket | Assumed (framework spec) |
| PTH housing cut, equity routing | 35% of housing; 25% of the saving to equity | Design (BLEI paper; internal design choice) |
| PTH appreciation, liquid share | 3-5% (+1% × SZH) a year; 15% → 85% over 5 years | Assumed; derived (BLEI paper Table 1a midpoints) |
| PTF adoption | 0.5% + 5% × PTF share (+1.5% if BLEI < 30 days) | Assumed (no cooperative-specific source) |
| SZH θ curve | 0 below 55% density, 0.25 at 90% | Design (BLEI paper Table 6) |
| ESP payroll share, workforce | 20% of BU accepted; 23% of adults | Sourced: BEA GDP by industry 2024; BLS CES Aug 2026 |
| Surplus split | phase 1: 1/3 prices, 1/3 reinvestment, 1/3 profit share; phase 2: 60/0/40 | Design (decisions d97-d106) |
| PTF capital per adult (`SURP.K`) | $18,862 | Sourced: BEA Fixed Assets 2025 / Census adults |
| Capacity charge | depreciation 4.53% + real interest | Sourced: BEA Fixed Assets Table 3.4ESI; interest from published yields (harness.js) |
| Forgone-profit share of the PTF cut | 4.94% (food), 2.60% (housing utilities) | Sourced: BEA |
| Spending rule | 59.3% of cash surplus consumed | Derived: BEA NIPA 2025 saving rate 5.4% on the no-programme run |
| Labour response | ε = 0.33; ρ = ρ_BU = 0.16; expired BU 0 | Sourced: Chetty (2012); Vivalt et al. (NBER w32719) |
| Wage growth | 1.0% + 0.8% BLEI bonus (scaled down above the median) + 0.5% × CIP; floor 80% of last year | Assumed (framework spec); the floor a stated policy boundary |
| Automation | drag rising 1.2 points a year from year 5 (2.2 from year 15), cap 10 points, × risk; risk mixture 63%/37% Beta(6,1)/Beta(1,6) | Assumed (drag); sourced (risk: Frey and Osborne 2013, BLS OES weights) |
| Recessions | 10% a year, 1-3 years, income × (0.70 + 0.25 × Beta(5,2)) | Sourced in shape (NBER post-war recessions) |
| Octave advancement | 1 − exp(−λ × FBS), λ ~ U[0.000165, 0.00132] | Design (BLEI paper §Index IV), rescaled v4.4 (calibration open) |
| CIP effects | quality step +0.1 with probability 0.15 × CIP; conversion bonus +12% × CIP; tax −18% × CIP; λ +20% × CIP | Assumed (framework) |
| New-money pass-through (`lamG`) | 1 (quantity-theory benchmark) | Assumed placeholder, swept |
| Essentials price response θ | food 0, housing 0.6, medical 0.5 | Sourced (food, housing ranges); assumed (medical) |
| Spending layer | multiplier 1.5 in recessions; labour share 0.508 | Sourced: CBO; Auerbach and Gorodnichenko (2012); BEA |
| Joining | revealed cost; stay at least 2 years | Derived (year-0 participation); design parameter (stay) |
| Wealth floor | −$10,000 | Assumed (SCF comparison group's 10th percentile −$10,543) |
| Launch gift; project pay | 1,000 BU per participant; the living wage per hour | Design (Hub rollout plan; decision d63) |
| Unhoused overlay | HUD AHAR 2025 base rate; 2% unhoused by choice | Sourced; assumed (swept 0-5%) |

## 7. Submodels

Each submodel's equations and parameters are in MODEL_SPEC.md: the v5.6 model's submodels in section 6 (wages, BLEI, cost of living and price cuts, BU purchases, project hiring, conversion, ESPs and the surplus split, octaves, joining, PTF and PTH, the labour response, financing and prices, households) and section 12 (job loss, PTH's books, PTF by sector, today's safety net, the flat contribution); the frozen model's corrections in section 13; the parts added for v5.9 in section 14 (open PTF access and growth 14.1; PTF running costs 14.2; the capacity price rule, a reading, 14.3; adults outside the labour force 14.4 and their movement in and out 14.15; borrowing 14.5; wealth by asset class 14.6; the creditor side 14.7; the weighted tail 14.8; bargaining 14.9; who pays 14.10; the government account 14.14); the central-bank rule in section 15 and the policy eras in section 16. The reasoning for each part, with its checks, is in its report in `dev/reports/`; `dev/DECISIONS.md` records each choice.

**Sensitivity and what would have to be true.** Every v5.9 outcome is published across the 62 preregistered readings (a specification curve: each reading changes one assumption, or a pair, in both runs), along the backing curve, and with the financed rows (the programme paid by a contribution instead of the Source; shown, never led with). An assumptions screen ranked which inputs move each outcome at full backing; Stress and the financed rows were not screened. The intervals measure the model's randomness over seeds only; they do not cover the choice of main row, full backing or the engine's structure. `ECONOMIST-REVIEW.md` is the checklist for an outside reviewer. (The v5.5 study's Morris and Sobol screens on the v5.6 model are in `dev/reports/v5-30-s137-results.md`.)

## 8. Verification

Every part added for v5.9 is behind its own switch (off = the earlier model exactly, proved by full-output diffs, the guard test); each has unit tests; the on-together tests apply each part's other reading alone and in every pair to the main row in three environments (identities, draws, finite outputs, each part's own checks, run order); a 10,000-adult check covers the tail and the creditor totals and agrees on hours and the top of the wealth distribution. A second implementation of the main row was written from MODEL_SPEC and a packet that also held the engine's code excerpts and per-seed results to check against; its exact agreement shows that the description, the code and a careful port agree, but it cannot catch a modelling choice they share (wording corrected Nov 17, 2026, from "independent").

## 9. What the model is not

Not a forecast, and not a reconstruction of any past period (the history readings put today's households under earlier settings). No limit on supply below full backing; no expectations; one price rule for the whole economy; no central bank in the main row (a policy-rate rule is a study, with no channel to the price of essentials); no migration; a fixed population in the main row; no value of care, community work or new ventures; PTFs modelled from the Hub's statements and measured costs; the creditor side is not a full accounting of who holds the losses inflation imposes (part goes outside the model). The model measures poverty, cost and work, not the cultural effects Compassionism aspires to.

## References

Grimm, V., et al. (2020), JASSS 23(2) 7. Chetty, R. (2012), "Bounds on Elasticities With Optimization Frictions", *Econometrica* 80(3). Vivalt, E., et al. (2024, revised 2026), "The Employment Effects of a Guaranteed Income", NBER Working Paper 32719. Frey, C. B., and Osborne, M. A. (2013/2017), "The Future of Employment", *Technological Forecasting and Social Change* 114. Stevens, A. H. (1994), "The Dynamics of Poverty Spells", *American Economic Review* 84(2). Auerbach, A. J., and Gorodnichenko, Y. (2012), *AEJ: Economic Policy* 4(2). MIT Living Wage Calculator (2026). US Census Bureau, Poverty Thresholds 2025. Board of Governors of the Federal Reserve System, Survey of Consumer Finances 2022. Bureau of Economic Analysis, NIPA and Fixed Assets tables (2025). Taylor, J. B. (1993), "Discretion versus policy rules in practice", *Carnegie-Rochester Conference Series on Public Policy* 39. Piketty, T., Saez, E., and Zucman, G. (2018), "Distributional National Accounts", *Quarterly Journal of Economics* 133(2). Other sources are cited where they are used, in MODEL_SPEC.md and the reports.
