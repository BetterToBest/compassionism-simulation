# Model specification: the release model (v5.2 engine, shown in v5.2.2)

This document describes **only the active release model**: the main result ("the release row") and its paired no-programme run, as published on the simulation page and the findings explorer. Every switch, alternative mechanism and labelled reading is listed separately in [TESTBED_SPEC.md](TESTBED_SPEC.md). How to regenerate every published table is in [REPRODUCE.md](REPRODUCE.md); the ODD protocol is [ODD.md](ODD.md).

The code is the reference: the engine in `index.html` (the block between the markers `RELEASE ENGINE` and `END RELEASE ENGINE`, and the earlier engine's core functions listed in `PAGE_CORE` at the top of `harness.js`). Since v5.3 it has one copy: `harness.js` reads it out of the page when it loads and runs it in Node with the study modes and unit suites. Function names below are those in `harness.js`. The plain-words reports in `dev/reports/` give the reasoning behind each mechanism; `dev/DECISIONS.md` records each choice.

The math and code were engineered by Claude (Anthropic) from Duke Johnson's concepts (the book *Better To Best* and the Research Hub). The model has not yet been reviewed by an independent economist.

---

## 1. What is simulated

A fixed population of 500 working-age adults, each living alone, is followed year by year for 20 years (or 40), twice on the same random draws: once with Compassionism as specified on the Research Hub (a monthly allowance of Basic Units that buy only essentials and expire; expired units converted to dollars at earned rates through project work; community-owned essential-service providers, PTFs; community housing, PTH; zone coordination, SZH; a civic platform, CIP), paid for by a Source that issues the units, and once with no programme. The model tracks each adult's wage, cost of living, savings (net wealth), programme status and conversion income, and the economy-wide price level that the programme's new money and extra demand for essentials move. It reports poverty (three measures), prices, cost, work and inequality as the average over 500 paired runs (seeds 1 to 500), in three environments.

## 2. Scope

| Item | The release model |
|---|---|
| Unit of analysis | The adult (an agent). There are no households, children, firms or banks; businesses, the Source and project collectives appear only as aggregate flows. |
| Population | 500 adults (`nAgents`), fixed: no births, deaths, entry or exit in the main row (ageing is a reading, TESTBED_SPEC.md). |
| Time step | One year. Within a year, events happen in the fixed order of section 5. |
| Horizon | 20 years (years 0 to 19) for the main tables; 40 years (`--years=40`) for the long-run tables. |
| Accounting unit | US dollars of the year in question (nominal); reported figures are deflated to year-0 dollars ("today's dollars", 2025) by the model's own price level. Wages are held internally in "SIU" per month and converted by `WAGE_TO_USD`. |
| Price numeraire | The basket price level `P_t = (1 + i)^t × B_t`, where `i` is the environment's outside inflation and `B_t` the price module's basket index (section 6.12). The BU is pegged one to one to the dollar. |
| Boundary | One country's prices and wages (US). No foreign sector, government budget outside the programme, interest rate, central bank, credit market (beyond a debt floor), land market or asset prices. Taxes appear only as a basket component (MIT's "taxes") and the programme's own conversion tax. |
| Replications | 500 seeds, common random numbers: the same seed gives the same adults and the same draws in every row (section 8). |

## 3. Entities and state variables

**Adult** (one object per agent; `instantiateAgent`, then updated by `runYear`):

| Variable | Meaning | Start |
|---|---|---|
| `wage` | Monthly wage in SIU (× `WAGE_TO_USD` = $100.52 per SIU-month) | lognormal(3.5, 0.5): median 35 SIU = $39,945 a year |
| `wealth` | Net wealth in nominal dollars (savings less debts; floored at −$10,000) | lognormal(10.5, 1.2): median $36,316 |
| `automationRisk` | Exposure to automation's wage drag, 0 to 1 | 63%/37% mixture of Beta(6,1) and Beta(1,6), by exact inverse CDF |
| `octave` | CCO octave level (0 to `maxOct`), sets conversion capacity `12 × 1,000 × 2^octave` BU a year | ⌊Beta(2,5) × `maxOct`⌋ |
| `quality` | Contribution quality, 0 to `maxMult` | `maxMult × 0.5 × exp(0.4 z) × (1 − 0.5 × cipDemo)`, capped |
| `lambda` | Advancement rate parameter (financial-bandwidth score) | Uniform[0.0001654, 0.0013233] |
| `inCCO` | Takes part in the programme | `uCCO < partRate` (then open enrolment, 6.9) |
| `inPTF` | Member (customer) of a community business (PTF) | `uPTF < ptfShare` (then adoption, 6.10) |
| `inPTH` | Lives in community housing (fixed for the run) | `uPTH < pthUptake`; members start with $5,000 of Acre Equity |
| `acreEquity`, `pthTenure` | PTH equity and years in PTH | 0 or $5,000; 0 |
| `uCCO` | The adult's latent participation uniform (kept for the revealed cost of taking part, 6.9) | drawn at construction |

**Aggregates** carried from year to year: the expired-BU project pool and the business conversion premium (paid the year after they arise), the ESP payroll pool, the ESP capital account and PTF capacity, the price indices (general `P_G`, essentials, basket `B`), the BU indexation level (COLA ratchet), the Source's and the testbed's ledgers.

**Environment**: the recession path (drawn once per seed), outside inflation `i`, and the automation wave.

## 4. Initialisation

For each seed `s` (one run):

1. **Construction stream** `mulberry32(s + 700003)`: for each adult in order, `uCCO, uPTF, uPTH` (3 draws), wealth (2), wage (2), octave shape Beta(2,5) (a variable number of draws: the gamma sampler's rejection loop), quality z (2), automation risk (2), lambda (1) (`makeLatentAgent`). These are *latent*: the same 500 latent adults are instantiated into every row, so the programme and no-programme runs start with identical people.
2. **Group stream** `mulberry32(s + 900001)`: one uniform per adult for the testbed's targeting tests (not used by the release row's dynamics).
3. **Recession path** `mulberry32(s + 700000)` (Adverse and Stress only): each year after year 0, a recession starts with probability 0.10, lasts 1 to 3 years, and multiplies everyone's earned income by 0.70 + 0.25 × Beta(5,2) (`buildRecessionPath`).
4. **Main stream** `mulberry32(s)`: the yearly draws (section 5, step B4).
5. **Supply path**: the no-programme run of the same seed sets each essential's capacity (year 0's effective demand, held flat; `s3BaseS`).

Starting values of the aggregates: pools empty, price indices 1, contribution rate from a one-year pre-pass (testbed `tbRun`).

## 5. Order of events inside one simulated year

`tbRunCore` calls, for `t = 0, …, T − 1`: `runYear(agents, t, p, recession[t])`, then year-end reporting, then the price step. Inside `runYear`:

**A. Year set-up (no random draws)**
1. Read the year's recession multiplier (1 outside recessions) and the automation drag on wage growth: 1.2 percentage points in year 5, rising by 1.2 points a year to year 14 and by 2.2 points a year from year 15, capped at 10 points; each adult's growth falls by the drag × their automation risk (`popAIDisp`; Adverse and Stress only).
2. Cost of living for the year: `M_t = LIVING_WAGE_ANNUAL × P_t` ($49,370 at year 0).
3. BU indexation (the Hub's Inflation Surge Protocol): if the year's headline price rise exceeds 5%, the BU is raised to the full price level (a ratchet: `colaLevel`); effective monthly BU `buEff = 1,200 × colaLevel`.
4. Spending layer (recession years only): wages restored = min(0.508 × 1.5 × last year's net Source payout, the recession's wage loss), shared in proportion to the loss (`MULT`).
5. PTF capacity `c_t` (share of adults the PTFs can serve) = min(1, c₀ + ESP capital per adult / $18,862), with last year's turned-away adults served on borrowed capacity (`PROD`, speed 'oneyear').
6. Open enrolment (from year 1): each adult compares the BU they would use with the revealed cost of taking part and joins or leaves (6.9).
7. Project hiring: last year's expired-BU pool (plus, in year 1, the launch gift of 1,000 BU per participant) is allocated to willing participants (6.5).
8. ESP payroll: last year's payroll pool (20% of the BU the essential-service providers accepted) is paid to ESP workers; participating workers whose own net rate beats par convert their share (6.7).
9. The ESP surplus split: last year's business conversion premium is divided into price cuts, reinvestment, a profit share and (for private ESPs) lower BU prices (6.7).

**B. Each adult in array order**
1. Floor any non-finite value (wealth 0, wage 1).
2. Record start-of-year wealth.
3. **Eight random draws, in this order, for every adult every year whatever their status** (`agentVar, uSpendFrac, uCipQuality, uAdvance, uSzhInduce, uSzhPtfShare, uPthAppr, uPtfAdopt`). Each is used only where the adult's state calls for it; the count never changes (checked by `matrixUnitSuite`), which keeps the runs paired adult by adult.
4. Income shock `= recession multiplier × agentVar`, `agentVar` uniform on [0.90, 1.10].
5. BLEI gate (6.2) on this year's BU spending (`GATE_CURRENT`), read the design-neutral way (`tbGate`).
6. Wage growth (6.1).
7. Cost factor: PTF and PTH price cuts on the adult's own basket (6.3).
8. BU purchases: participants spend up to `12 × buEff` on essentials at their own prices; what is left expires to the project pool (6.4). The split's price cuts and private ESPs' lower BU prices apply here.
9. Earnings: `E = wage × 12 × WAGE_TO_USD × income shock × (1 + slack fill)`, then the labour response (6.11).
10. Cost: `cost = M_t × cf` (cf after price cuts and BU purchases). `wealth += E − cost`.
11. Testbed cash flows (none for the release row) and ledgers.
12. Business payout: last year's remaining business premium paid by last year's wage (the release row pays it through the split's profit share and price pools instead; 6.7). ESP payroll conversion credited.
13. **Project conversion** (participants): project BU converted at the adult's rate under the progressive tax, × CIP bonus × income shock (6.5, 6.6). Octave advancement (6.8). SZH induction into PTF.
14. **PTH**: equity routing and appreciation (6.10).
15. PTF adoption (Bass diffusion; 6.10).
16. **Spending rule**: `wealth −= 0.593 × max(0, cash surplus)` (6.4).
17. Price-module accumulators (demand for essentials, unmet need, income).
18. Cost ledger and poverty accounting (`tbAccount`, section 9).
19. Wealth floor: wealth below −$10,000 is set to −$10,000 (the shortfall is unmet need, not money).

**C. Year close**
1. Businesses convert the BU they accepted: 20% becomes next year's payroll pool; the rest converts at 3× under the progressive tax, and the premium over face value is next year's split pool (`FW.bizRate` 3, `FW.bizCap` 1).
2. Year-end reporting: BLEI by group, unhoused share, the v5.2 Year-7/last-year snapshot and spells (`tbBleiYear`, `extremePovertyOf`, `tbRepYear`).
3. **Financing and prices** (`tbRunCore`): the year's unmatched new money `U` (6.12) moves the general price level for next year; essentials prices move with demand above capacity; the basket index is recomputed.

## 6. Submodels

### 6.1 Wages
`wg = 1.0%` (base growth) `+ 0.8% × max(0.1, 1/(1 + 0.5 × max(0, wage/35 − 1)))` if the BLEI gate exceeds 30 days `+ 0.5% × cipDemo` `+ P_G inflation` (wages indexed to the general price level, `wIdx` 1) `− automation drag × automationRisk`; `wage ← max(0.8 × wage, wage × (1 + wg))`. The octave wage raise is off in the release row (the design pays octaves through conversion). The 80% floor is a stated policy assumption.

### 6.2 BLEI (Basic Living Economic Index)
Days of basic living an adult's resources cover: `BLEI = (0.20 × max(0, wealth) + γ × monthly wage $ + BU food) / daily cost`, with γ = 0.20 for participants and 0.12 otherwise, BU food = one month of the BU spent on essentials, daily cost $68.33 ($31.67 for participants in PTH), lowered by SZH (`agentBLEI`). The **design-neutral** reading applies the no-programme rules to everyone (γ = 0.12, $68.33) and adds one month of the design's regular support (`tbGate`). Both are read in year-0 prices (divided by the price level).

### 6.3 Cost of living and price cuts
The basket is MIT's living-wage budget for one adult (`CFG.BASKET`: food 9.0%, housing incl. utilities 27.6%, medical 6.9%, transport 19.6%, civic 6.6%, internet 3.1%, other 9.2%, taxes 18.0%). Essentials (food, housing, medical: 43.5%) are what BU buy and the essentials prices move. PTF members' basket (excluding taxes) is cut by 12% + 4% × SZH coherence; PTH members' housing component by 35% (`PTH_MODE 'housing'`, `DISC_BASE 'pretax'`). The part of the PTF cut funded from forgone profit (4.94% of the food component and 2.60% of the housing component, utilities; `COST`, BEA) is not counted as programme cost.

### 6.4 BU purchases, expiry and saving
A participant's BU budget is `12 × buEff` a year. BU buy essentials at the adult's own (discounted) prices up to the budget; a BU is worth $1 (N3, N4). Unspent BU expire; all of them go to next year's project pool (`FW.directedShare` 1, `PROJ.share` 1). Each adult then consumes 0.593 of the year's cash surplus (cash income less cost, after conversion and payouts; `SPEND_SOURCED`, derived so the no-programme run's saving rate equals the US personal saving rate of 2025, 5.4%, BEA NIPA Table 2.1), and saves the rest.

### 6.5 Project hiring (the conversion of expired BU)
The pool is offered to participants for whom a project hour pays more, after conversion and tax, than an hour of their own wage (contract pay: the living wage per hour, $49,370 / 2,080, indexed). It is shared among them in proportion to octave capacity × quality; each converts at the larger of their own rate and the pool's mean rate (`PROJ.rate 'max'`), with project hours worked beside their job (`hours 'side'`, no cap). Pool that finds no willing worker carries to the next year.

### 6.6 Conversion rate and tax
Own rate `r = min((1 + (q/M) × (C_oct − 1)) × φ × b_PTF, M × 1.618)`, with `C_oct = 1 + (octave/maxOct) × (M − 1)`, `M = maxMult` (9 at the reference), `φ = 1.618` when quality exceeds 0.70 × M (the Phi tier; the threshold's place is a modelling assumption, `dev/reports/v5-11-phi-step.md`), and `b_PTF = 1.30 + θ_SZH` for PTF members. Conversion tax `τ(r) = min(0.75, τ₀(1 − 0.18 × cipDemo) + max(0, (r − 3) × 0.04))`, τ₀ = 12%. Net dollars per BU converted `= r × (1 − τ(r)) × (1 + 0.12 × cipDemo) × income shock`. The tax is kept by the Source.

### 6.7 Essential-service providers (ESPs): payroll, premium and the split
ESPs (grocers, food services, utilities, housing, health care) accept BU at face value. Of what they accept in a year, 20% is next year's payroll in BU (`ESP.lam`, BEA compensation share of essential-industry output), paid to the 23% of adults who are ESP workers (BLS CES; fixed by agent index, no random draw), each up to their last year's wage. A participating worker whose own net rate beats par converts their payroll BU at that rate within octave capacity (net of project BU); otherwise they are paid in dollars and the ESP converts. The ESP converts the rest at 3× under the progressive tax; the premium over face value is split the next year (`SURP`, priv 'prices'):
- The PTFs' share of the premium is the share of BU that PTF members spent. It goes 1/3 to price cuts for PTF members (one uniform cut, capped at 100%; the rest carries), 1/3 to reinvestment (the ESP capital account that builds PTF capacity), 1/3 to a profit share for participating ESP workers by wage, until PTF capacity reaches every adult; then 60% to price cuts and 40% to the profit share.
- Private ESPs pass their premium to the participants who paid them in BU as lower BU prices (in proportion to the BU each spent, capped at their own essentials), after matching the profit-share fraction for their workers (`privWk 'match'`); nothing goes to owners.

### 6.8 Octave advancement
Each year a participant below the top octave advances with probability `1 − exp(−λ' × FBS)`, where `FBS = max(0, Y + BU − basic monthly cost − e × Y)` is the monthly financial bandwidth (Y the monthly wage in dollars, e = 0.12, or 0.025 in PTH) and `λ' = λ × (1 + 0.20 × cipDemo)`.

### 6.9 Joining and leaving
From year 1, an adult takes part when the BU they would use, `min(12 × buEff, M_t × essentials share at own prices)`, is at least the revealed cost of taking part, `12 × 1,200 × uCCO / partRate × P_t`, set so that in year 0 exactly the adults who take part today would; a participant stays at least 2 years (`JOIN`, 'revealed'). With the BU indexed, almost nobody changes their mind (`dev/reports/04-joining.md`).

### 6.10 PTF membership and PTH
PTF: a non-member joins with probability `0.005 + 0.05 × current PTF share` (+0.015 if their BLEI is below 30 days) while capacity allows (Bass diffusion; `uPtfAdopt`), or by SZH induction (`uSzhInduce < 0.16 × θ_SZH` and `uSzhPtfShare < ptfShare`); members never leave (a stated limit). θ_SZH reads the realised PTF density (`THETA_GATE 'density'`: 0 below 55%, rising to 0.25 at 90%). PTH: 25% of the PTH saving is routed from wealth to Acre Equity each year; equity appreciates at 3% + 2% × `uPthAppr` + 1% × SZH coherence; the liquid share of appreciation (15% in the first year, rising linearly to 85% from year 5) is credited to wealth. In v5.2 the whole appreciation also stayed in the Acre Equity, so the liquid share was counted twice; v5.3 takes it out of the equity (`PTH_APPR_CONSERVE`, section 11). The PTH saving here is measured at the BLEI daily cost, so the 25% is 12.6% of the member's actual saving (section 11).

### 6.11 Labour response
Earnings with the programme `E = max(0, E₀ × R^(ε − ρ) − ρ × (unconditional dollars) − ρ_BU × BU spent)`, with ε = 0.33 (Chetty 2012), ρ = ρ_BU = 0.16 (Vivalt et al. 2024/2026), R the programme's raises (the ESP profit share and payroll premium as raises, one elasticity for every change in the return to work); expired BU carry no income effect (ρ_R = 0); every price-cut dollar and last year's liquid PTH appreciation count as unconditional dollars (`LABOR`, `inkindRho`).

### 6.12 Financing, new money and prices
The Source issues the BU, pays conversions and keeps the conversion tax (`fin 'source'`). The release row's cautious reading: of what the Source pays out (BU spent at face value plus conversion proceeds, less output that backs it), none is backed by new output (`a = 0`); counted output is ESP reinvestment (capital goods) and the whole project payout (`PROD.match 'market'`). Unmatched money `U = (1 − a) × (BU spent at face value + conversion paid − matched output)`; the programme's raises are taken as matched by output (`aw` 1) and a write-off at the wealth floor is unmet need, not money. The general price level moves with it: `P_G,t+1 = P_G,t × (1 + λ_G × U_t / Y_t)`, λ_G = 1, Y the year's aggregate cash income (quantity-theory benchmark, a logged placeholder swept in the testbed). Essentials prices move with demand above the no-programme capacity: `P_E,k = 1 + θ_k × (D − S)/S`, θ = 0 (food), 0.6 (housing), 0.5 (medical; unsourced placeholder), and are also multiplied by `P_G`. Basket index `B = 1 + Σ_k share_k × (component_k − 1)`.

## 7. Endogenous and exogenous variables

**Endogenous**: wages, wealth, participation, PTF membership, octaves, quality (CIP step), conversion income, the business premium and its split, PTF capacity, the price level (general and essentials), the BU's indexed level, the contribution rate where used, poverty, Gini.
**Exogenous**: the starting population (drawn), outside inflation (0% Reference, 2% Adverse and Stress), the recession path, the automation wave, the basket's composition, every constant in section 8.

## 8. Random streams (common random numbers)

| Stream | Seed | Draws | Used by |
|---|---|---|---|
| Main (yearly) | `s` | exactly 8 per adult-year, fixed order | every row; the count is checked by `matrixUnitSuite` |
| Construction | `s + 700003` | per adult at year 0 (variable count: gamma rejection) | every row (identical latent adults) |
| Recession path | `s + 700000` | 1-3 per year | Adverse and Stress |
| Testbed groups | `s + 900001` | 1 per adult | targeting groups (reporting) |
| Ageing (reading) | `s + 600011` | per adult and per adult-year | only rows with ageing |
| Review errors (reading) | `s + 800023` | 1 per adult-year | only rows with review errors |
| Households (reading, v5.3) | `s + 500009` | at the start: an order of the adults, then per household with children 1 + 2 per child | only rows with households (`HOUSEHOLDS`) |

A new random process gets its own stream; nothing may add a draw to the main stream. Rows of one study share every stream, so differences between rows come from the rows' rules, not from luck.

## 9. Estimands (what each headline measures)

All are means over the 500 seeds; a change is the mean of the 500 per-seed differences (programme − no programme on the same seed), and its 95% interval is `mean ± 1.96 × sd/√500` of those differences (`tbDiff`).

| Measure (key) | Definition |
|---|---|
| Below the cost of living (`fgt0PY`) | Share of adult-years in which cash income (earnings + conversion + payouts + cash transfers − contribution) is below the adult's own cost of living (the basket after in-kind price cuts and BU purchases). Averaged over all years of the run. |
| Too little wealth (`pov`) | Share of adults whose net wealth at the last year is below $25,000 × the price level (`CFG.POVERTY_LINE`; a design threshold whose provenance is open, settled in v5.3). |
| Below 30 days of basic living (`bOAPy`) | Share of adult-years with BLEI (the BLEI paper's definition, 6.2) below 30 days, in year-0 prices. Design-neutral version: `bNAPy`. |
| Poverty severity (`fgt2PY`) | Mean over adult-years of the squared shortfall of cash income below own cost, as a share of the basket (FGT2 × 100). |
| Below the US official poverty line (`rep.y7.fpl`, `rep.end.fpl`) | Share of adults whose money income (earnings, conversion, cash transfers; not BU) is below $16,749 (2025, one person under 65) × the price level, at Year 7 and the last year. `fplX`: the same line on Supplemental-style resources. |
| Gini (`giniD`, `giniX`, `rep.*.giniW`) | Sample Gini of disposable income (`giniD`), of income plus in-kind cuts (`giniX`), of wealth with debts as zero (`giniW`), each × n/(n − 1) (n = 500): an estimate of the Gini of the population the adults are drawn from. The uncorrected Gini of the 500 adults is in the release file (`derived.giniFinite`). |
| Programme inflation (`infl`) | Annualised rise of the basket index over the run, `B_{T−1}^{1/(T−1)} − 1`. |
| Price level at the last year (`pLevEnd`, `…Med`, `…P10`, `…P90`) | Full price level `P_{T−1}` across seeds: mean, median, 10th and 90th percentile (the 10th-90th band holds eight runs in ten). |
| Cost per adult (`cost`) | Programme outlays per adult-year in year-0 dollars: BU relief, conversion and the split's price cuts, price-cut dollars (PTF, PTH), liquid PTH appreciation; not the PTF discount funded from forgone profit. |
| Hours (`hrs`) | Change in earnings at a fixed wage from the labour response, % (hours). |
| Median savings (`medWealth`) | Median net wealth at the last year in year-0 dollars. |
| Unhoused (`epPY`) | Share of person-years unhoused, from the extreme-poverty overlay (HUD AHAR 2025 rate scaled by housing distress against year 0). |

## 10. The two runs that make the main result

- **Release row** (`releaseRows`, `j: 'release'`): `n1Row(tbPresets(P), 'framework', {fin:'source', a:0, jn:{}, cs:{}, sc:0.593, sp:{priv:'prices'}, pd:{match:'market', speed:'oneyear'}, ml:{}, gc:true})` on the environment's preset `P` (Reference = `FULL_INTEGRATION`: BU $1,200 a month, 78% take part, 18% start in PTF, 20% in PTH, SZH coherence 0.72, CIP 0.65, 6 octaves, multipliers to 9×, conversion tax 12%; Adverse = the same with recessions, automation and 2% inflation; Stress = `STRESS_TEST`: $900, 40%, 8%, 10%, 0.35, 0.30, 4 octaves, 6×, 18%, with recessions, automation and 2% inflation), with project hiring (`PROJ` defaults), ESP payroll (`ESP` defaults), the octave wage raise off and the PTF/PTH inflation damping off.
- **No programme** (`tbPresets(P).baseline()`): every architecture off, no BU, at the environment's own outside inflation and shocks.
- **Study options** for both: the NR6 profile (`applyNR6`: SZH θ from realised PTF density, PTH cuts housing, discounts skip taxes), `N7_BLEI` on, wages indexed to `P_G`, the labour response at central values, lines deflated by the price level, `fin 'tax'` for rows that do not set their own financing, the spending share 0.593, the v5.2 reporting (`rep52`, `giniNN1`), wealth floor −$10,000.

The full list of constants, with their basis, is in [ODD.md](ODD.md), section 7 (Input data and parameters), and in CONTRIBUTING.md's calibration table.

## 11. Accounting identities (checked)

Since v5.3 (plan item B2) the engine can check its own books while it runs (`ACCT`, off by default; `acctNew()` turns it on). It draws no random number and no rule reads it, so every result is bit-identical with it on. Every year it checks, to a relative tolerance of 10⁻⁹ of the gross size of the flows:

| Identity | What must balance |
|---|---|
| Money, per adult | Ending net wealth = beginning + interest + wage earnings − living costs + Social Security + cash transfers less the contribution + conversion income − PTH equity contribution + the cash part of the PTH appreciation − surplus consumed + debt written off at the floor. Every term except interest and the PTH terms is the adult's own yearly record (`yrWageUSD`, `yrCostUSD`, `yrConvUSD`, ...), the one the income and poverty measures read, so the check also proves those measures see every dollar that reaches wealth. |
| Acre Equity, per PTH member | Ending equity = beginning + equity contribution + appreciation not paid out in cash. |
| BU, per adult (engine model) | Ending balance = beginning + issued − expired − spent. |
| BU stock (framework model) | The year's stock (the ESP payroll pool, the project pool, BU adults hold for later conversion, BU directed but not yet allocated) = the stock at the start + BU issued (allowances, launch gift) − BU converted (by adults; by the ESP, including BU returned to it) − BU destroyed (expired BU not directed; BU beyond a cap). BU an adult holds when they die lapse, as unspent BU do (tallied, not an error). |
| The ESP premium | The premium paid out this year with last year's carries = price cuts delivered + dollars paid to adults + reinvestment + capital charges + what carries to next year. |
| The Source's books against the households' | BU face value the Source pays = BU adults spent; conversion the Source pays = adults' conversion income + the split's price cuts + reinvestment + capital charges; BU issued = allowances; the price module's injection = the same less the price cuts. |
| The Source's financing | What the Source pays (BU face value and conversion) = new money + the output that backs it (Source financing). |

`acctUnitSuite` (in `node harness.js unit`) runs every release row and no-programme pair in all three environments with the check on, and also the framework alone, with each module added, and the engine model; it also plants an unrecorded dollar and an unrecorded BU to show the check catches them. `node dev/tools/acct_check.js ENV N` runs it over N seeds.

The check found two places where v5.2 did not conserve money; both are corrected in v5.3 behind switches (false reproduces v5.2): the cash part of the PTH appreciation was paid to the member and also kept in the Acre Equity, so it was counted twice and compounded (`PTH_APPR_CONSERVE`); and in the two rent mark-up readings the ESP split sized its price cut on rents before the mark-up but applied it after, handing out more than its pool (`SURP_CUT_MARKUP`). What the corrections change is in `dev/reports/v5-13-accounting-check.md`.

Not checked, because the model has no such accounts yet: the PTH organisation's own books (a member's housing payment split into operating cost, equity contribution, community surplus and financing cost; planned with the PTH balance sheet in v5.4). The model represents PTH from the member's side only: a 35% cut in the housing component, a quarter of that saving routed to Acre Equity, and the equity's appreciation. The saving the quarter is taken of is measured at the BLEI daily cost ($68.33 a day, the BLEI paper's anchor) rather than the basket the cut applies to (MIT's $49,370 a year), so a member routes 12.6% of their actual PTH saving to equity; money is conserved either way, and the base is part of the same unsourced design setting (25%), so it is listed for the v5.4 sensitivity study rather than changed.
