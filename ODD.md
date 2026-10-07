# ODD protocol: Compassionism Framework Simulation, release model

Structured after Grimm, V., Railsback, S. F., Vincenot, C. E., et al. (2020), "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism", *Journal of Artificial Societies and Social Simulation* 23(2), 7. This describes the **release model** (the v5.2 engine, shown in v5.2.2). The full equations are in [MODEL_SPEC.md](MODEL_SPEC.md); every switch and reading is in [TESTBED_SPEC.md](TESTBED_SPEC.md); [REPRODUCE.md](REPRODUCE.md) regenerates every published figure. The earlier v4.22 engine has its own ODD notes on the replication page ("Assumptions, ODD protocol, calibration notes and version history").

Authors: the concepts are Duke Johnson's (*Better To Best*; Research Hub, bettertobest.github.io/research-hub/); the math and code were engineered by Claude, an AI model made by Anthropic. The model has not yet been reviewed by an independent economist. Code: Apache-2.0; documentation: CC BY 4.0. DOI 10.17605/OSF.IO/QWTE2.

## 1. Purpose and patterns

**Purpose.** To show what the Compassionism framework's rules imply, as specified on the Research Hub, for poverty, savings, work, prices and cost in a population of working-age US adults, against no programme, under three economic environments; and to make each assumption visible and testable by holding every alternative reading behind a switch. The model is a design-exploration tool, not a forecast.

**Patterns used to evaluate the model.** (1) The no-programme run against US data: the share below the official poverty line among workers (4.3%, Census 2025; model 4.0% in its first year), poverty spell exits and re-entries (PSID, Stevens 1994), the SCF 2022 comparison group's wealth (median, share in debt, wealth Gini), the US income Gini. The gaps are reported, not tuned away (replication page, US-data table). (2) The Research Hub's own Year 7 targets (poverty under 2%, income Gini 0.25 to 0.30, wealth Gini 0.25), reported beside the model's figures. (3) Internal accounting: the cost ledger, the Source's payout and the BU flows add up (unit tests).

## 2. Entities, state variables and scales

**Entities.** Adults (500, the only agents). The programme's institutions (the Source that issues Basic Units, essential-service providers including community-owned PTFs, project collectives, community housing) are represented by aggregate flows and pools, not as agents. The environment is a recession path, outside inflation, an automation wave and the price level.

**Adult state variables.** Monthly wage (SIU; × $100.52 per SIU-month), net wealth (dollars; floor −$10,000), automation risk (0-1), octave (0-6 at the reference), quality (0-9), advancement parameter λ, programme participation, PTF membership, PTH residence (fixed), Acre Equity and PTH tenure, and the latent participation uniform. Full table: MODEL_SPEC.md, section 3.

**Global state.** The expired-BU project pool, the ESP payroll pool and business premium (each paid the next year), the ESP capital account and PTF capacity, the general price level, essentials prices and the basket index, the BU's indexed level, ledgers.

**Scales.** Time step one year; horizon 20 years (years 0-19) or 40. No space (zone coordination, SZH, acts through a coherence parameter and realised PTF density). Money in nominal US dollars, reported in year-0 (2025) dollars by the model's price level.

## 3. Process overview and scheduling

Each year, in this order (MODEL_SPEC.md, section 5, gives every step):

1. **Set-up**: the year's recession multiplier and automation drag; the cost of living (MIT basket × price level); the BU's indexation (raised to the price level in any year prices rise faster than 5%); the spending layer in recessions; PTF capacity; open enrolment; allocation of last year's expired BU to project work; ESP payroll; the split of last year's business premium.
2. **Each adult, in array order**: eight random draws in a fixed order; income shock; BLEI gate; wage growth; price cuts on the adult's basket; BU purchases of essentials (the rest expire); earnings and the labour response; wealth += earnings − cost; payouts; project and payroll conversion; octave advancement; SZH induction into PTF; PTH equity and appreciation; PTF adoption; the spending rule (59.3% of cash surplus consumed); accounting; the wealth floor.
3. **Close**: businesses convert the BU they accepted (20% to next year's payroll; the rest at 3× under the progressive tax, the premium paid next year); year-end reporting; the price step (unmatched new money moves the general price level; demand above capacity moves essentials prices; the basket index is recomputed).

Adults are updated sequentially within a year; the only within-year interaction is through capacity limits (PTF membership while capacity allows), which are checked in array order. Every between-adult interaction otherwise runs through year-level aggregates computed before or after the adult loop.

## 4. Design concepts

- **Basic principles.** The framework's architecture (Research Hub): a monthly allowance of Basic Units (BU) that buy only essentials and expire; expired BU converted to dollars at rates earned through community-valued work (octaves of capacity, multipliers to 9×, the Phi tier for exceptional quality, a progressive conversion tax); community-owned essential-service providers (PTFs) that share their conversion premium as lower prices, reinvestment and a profit share; community housing (PTH) whose payments build equity; zone coordination (SZH); a civic platform (CIP). Around it, standard economic modules: a quantity-theory price rule for unbacked new money, an essentials price response to demand above capacity, a labour-supply response with one income effect per unconditional dollar and one wage elasticity for every change in the return to work (Chetty 2012; Vivalt et al.).
- **Emergence.** Poverty rates, the price level, programme cost, the distribution of wealth, participation and PTF capacity emerge from the adults' rules and the aggregate pools; prices feed back into every adult's cost and the BU's indexation.
- **Adaptation.** Adults join or leave the programme when the BU they would use is worth more or less than the revealed cost of taking part; they take project work when a project hour pays more after tax than an hour of their own wage; they adjust earnings to programme income and raises (labour response). No other optimisation.
- **Objectives.** Implicit in the decision rules above (net gain from taking part; net pay per hour).
- **Learning.** None.
- **Prediction.** None: decisions use last year's or this year's known values.
- **Sensing.** Adults know their own wage, cost, BU value and rates; the participation cost reads the price level; project allocation reads octave capacity and quality.
- **Interaction.** Indirect, through pools (expired BU fund other adults' projects; BU spent at ESPs fund ESP workers' payroll and the price cuts of PTF members), through PTF capacity and Bass diffusion (adoption rises with the PTF share), and through prices (everyone's new money raises everyone's cost).
- **Stochasticity.** Starting attributes are drawn per adult; each year eight uniforms per adult (wage noise, BU spending share, CIP quality step, octave advancement, SZH induction and share, PTH appreciation, PTF adoption); recessions. All are drawn from seeded streams so that the programme and no-programme runs use the same draws (common random numbers; streams in MODEL_SPEC.md, section 8).
- **Collectives.** The programme's participants, PTF members, PTH residents and ESP workers are groups defined by state; the institutions are aggregate flows.
- **Observation.** Per run: shares below the cost of living, below 30 days of basic living (BLEI, two readings), with too little wealth, below the official poverty line; poverty severity (FGT2); unhoused share; Ginis; programme inflation, price level, cost, hours, median savings; Year 7 and last-year snapshots; poverty spells. Per study: means over 500 seeds, paired differences with 95% intervals (MODEL_SPEC.md, section 9).

## 5. Initialization

500 latent adults per seed from the construction stream (seed + 700003): participation, PTF and PTH uniforms; wealth lognormal(10.5, 1.2); wage lognormal(3.5, 0.5); octave shape Beta(2,5); quality score; automation risk (63%/37% Beta mixture); λ uniform. They are instantiated identically into the programme and no-programme runs (participation 78% at the reference, PTF 18%, PTH 20%; PTH residents start with $5,000 of equity). Pools start empty, prices at 1. The recession path is drawn once per seed (seed + 700000). Initial values are not taken from data except as stated in section 6; the no-programme run's first year is compared with US data (section 1).

## 6. Input data

No time-series input drives the model during a run. Fixed inputs (MODEL_SPEC.md and `CFG` in harness.js): the MIT living-wage basket for one adult and its components; the Census CPS median income (wage scale); the Frey and Osborne occupation automation probabilities (risk mixture); the BEA saving rate (spending rule); BEA industry accounts (payroll share, PTF capital per adult, forgone-profit shares, depreciation); BLS employment (ESP workforce); the 2025 official poverty threshold; HUD homelessness counts (unhoused overlay). For the labelled readings: the Census population by age and the NCHS life table (ageing), the SCF 2022 (wealth and wages), TIPS real yields (savings), Kenya cash-transfer evidence and BLS U-6 (backing), housing-voucher studies (rent capture), the 2025 federal income tax schedule.

### Parameters and their basis

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

Each submodel's equations and parameters are in MODEL_SPEC.md, section 6: wages (6.1), BLEI (6.2), cost of living and price cuts (6.3), BU purchases, expiry and saving (6.4), project hiring (6.5), conversion rate and tax (6.6), essential-service providers and the surplus split (6.7), octave advancement (6.8), joining and leaving (6.9), PTF membership and PTH (6.10), the labour response (6.11), financing, new money and prices (6.12). The reasoning for each, with the restudy that tested it, is in `dev/reports/01-esp-split.md` to `dev/reports/12-page.md` and `dev/reports/v5-1` to `v5-11`.

## References

Grimm, V., et al. (2020), JASSS 23(2) 7. Chetty, R. (2012), "Bounds on Elasticities With Optimization Frictions", *Econometrica* 80(3). Vivalt, E., et al. (2024, revised 2026), "The Employment Effects of a Guaranteed Income", NBER Working Paper 32719. Frey, C. B., and Osborne, M. A. (2013/2017), "The Future of Employment", *Technological Forecasting and Social Change* 114. Stevens, A. H. (1994), "The Dynamics of Poverty Spells", *American Economic Review* 84(2). Auerbach, A. J., and Gorodnichenko, Y. (2012), *AEJ: Economic Policy* 4(2). MIT Living Wage Calculator (2026). US Census Bureau, Poverty Thresholds 2025. Board of Governors of the Federal Reserve System, Survey of Consumer Finances 2022. Bureau of Economic Analysis, NIPA and Fixed Assets tables (2025).
