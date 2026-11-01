# Model specification: the release model (v5.6)

This document describes **only the active release model**: the main result ("the release row") and its paired no-programme run, as published on the simulation page and the findings explorer.

**Which model (Nov 1, 2026, research-update step S50).** The published panel (v5.4's model, run with today's safety net in both runs since v5.6: `node harness.js testbed 500 release ref,adv,st --v54 --snab --slope`) is v5.3's release row, described in sections 1 to 11, plus four parts added in v5.4 and the safety net (section 12), and the flat contribution that pays for the price cuts (section 12.5). Where section 12 changes an earlier rule, it says so, and the earlier section points to it. The second independent implementation (S50) is written from this document; Appendix A closes the 31 gaps the first one found (S10, `dev/reports/s118-independent-implementation/GAPS.md`), and Appendix B describes the engine's older validation path, which `node harness.js validate` and the earlier engine's presets run. The design freeze (S47) will add its own changes here (for example the audit's corrections, `AUD`, `dev/reports/s13-engine-audit.md`). Every switch, alternative mechanism and labelled reading is listed separately in [TESTBED_SPEC.md](TESTBED_SPEC.md). How to regenerate every published table is in [REPRODUCE.md](REPRODUCE.md); the ODD protocol is [ODD.md](ODD.md).

The code is the reference: the engine in `index.html` (the block between the markers `RELEASE ENGINE` and `END RELEASE ENGINE`, and the earlier engine's core functions listed in `PAGE_CORE` at the top of `harness.js`). Since v5.3 it has one copy: `harness.js` reads it out of the page when it loads and runs it in Node with the study modes and unit suites. Function names below are those in `harness.js`. The plain-words reports in `dev/reports/` give the reasoning behind each mechanism; `dev/DECISIONS.md` records each choice.

The math and code were engineered by Claude (Anthropic) from Duke Johnson's concepts (the book *Better To Best* and the Research Hub). The model has not yet been reviewed by an independent economist.

---

## 1. What is simulated

A fixed population of 500 working-age adults, living in households as US adults do with their children (since v5.3; section 6.13), is followed year by year for 20 years (or 40), twice on the same random draws: once with Compassionism as specified on the Research Hub (a monthly allowance of Basic Units that buy only essentials and expire; expired units converted to dollars at earned rates through project work; community-owned essential-service providers, PTFs; community housing, PTH; zone coordination, SZH; a civic platform, CIP), paid for by a Source that issues the units, and once with no programme. The model tracks each adult's wage, cost of living, savings (net wealth), programme status and conversion income, and the economy-wide price level that the programme's new money and extra demand for essentials move. It reports poverty (three measures for adults, and children's poverty and household measures since v5.3), prices, cost, work and inequality as the average over 500 paired runs (seeds 1 to 500), in three environments.

## 2. Scope

| Item | The release model |
|---|---|
| Unit of analysis | The adult (an agent), grouped into households with their children (since v5.3, section 6.13); a household pools its money and decides together. There are no firms or banks; businesses, the Source and project collectives appear only as aggregate flows. |
| Population | 500 adults (`nAgents`) and their children (about 170), fixed: no births, deaths, entry or exit, and children stay children, in the main row (ageing, with children's lives and estates, is a reading, TESTBED_SPEC.md). |
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
| `_emOcc`, job-loss state | Occupation (one of 700), weeks still out of work, insured or not, the pay cut waiting for the return (12.1) | drawn on the job-loss streams |
| household | Each adult's household (partner, children with ages, the household's needs and BU), section 6.13 | drawn on the household stream |

In the release row (section 12) an adult's starting wealth is replaced by their household's SCF net worth (6.13, `wealth 'scf'`) and their automation risk by their occupation's probability (12.1). Both draws of section 4 are still made, so every later draw stays in place.

**Aggregates** carried from year to year: the expired-BU project pool and the business conversion premium (paid the year after they arise), the ESP payroll pool, the ESP capital account and PTF capacity, the price indices (general `P_G`, essentials, basket `B`), the BU indexation level (COLA ratchet), the Source's and the testbed's ledgers.

**Environment**: the recession path (drawn once per seed), outside inflation `i`, and the automation wave.

## 4. Initialisation

For each seed `s` (one run):

1. **Construction stream** `mulberry32(s + 700003)`: for each adult in order, `uCCO, uPTF, uPTH` (3 draws), wealth (2), wage (2), octave shape Beta(2,5) (a variable number of draws: the gamma sampler's rejection loop), quality z (2), automation risk (2), lambda (1) (`makeLatentAgent`). These are *latent*: the same 500 latent adults are instantiated into every row, so the programme and no-programme runs start with identical people.
2. **Group stream** `mulberry32(s + 900001)`: one uniform per adult for the testbed's targeting tests (not used by the release row's dynamics).
3. **Recession path** `mulberry32(s + 700000)` (Adverse and Stress only): in each year from year 1 to the year before the last, a recession starts with probability 0.10 (none starts in year 0 or in the last year), lasts 1 to 3 years, and multiplies everyone's earned income by 0.70 + 0.25 × Beta(5,2) (`buildRecessionPath`). The main stream is restored afterwards, so the path adds no draw to it.
4. **Main stream** `mulberry32(s)`: the yearly draws (section 5, step B4).
5. **Supply path**: the no-programme run of the same seed sets each essential's capacity (year 0's effective demand, held flat; `s3BaseS`).

Starting values of the aggregates: pools empty, price indices 1, contribution rate from a one-year pre-pass (testbed `tbRun`; 12.5).

### 4.1 The random generator and the samplers (exactly as the engine draws)

- `mulberry32(seed)`: `s = seed >>> 0`; each call: `s = (s + 0x6D2B79F5) >>> 0; t = imul(s ^ (s >>> 15), 1 | s); t = (t + imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296` (32-bit unsigned arithmetic; `imul` is 32-bit integer multiplication).
- Standard normal: `u = max(1e-14, 1 − RNG()), v = RNG(); z = √(−2 ln u) × cos(2π v)` (two draws, the cosine branch only).
- `lognormal(μ, σ) = exp(μ + σ z)` with z drawn as above.
- `gamma(a)`: if a = 1, `−ln(max(1e-14, RNG()))`; if a < 1, `gamma(1 + a) × max(1e-14, RNG())^(1/a)`; otherwise the tangent rejection method (Knuth's algorithm A, after Ahrens): up to 5,000 tries, each drawing **both** uniforms first, `u = RNG(), v = RNG(), y = tan(π u), x = √(2a − 1) y + a − 1`, accept x if `x > 0` and `v ≤ (1 + y²) exp((a − 1) ln(x/(a − 1)) − √(2a − 1) y)`; after 5,000 rejections it returns a.
- `beta(a, b) = G_a / (G_a + G_b)`, with `G_a = gamma(a)` drawn before `G_b = gamma(b)`.
- Automation risk (before the occupation replaces it, 12.1): first draw U₁ picks the group (high risk if U₁ < 0.63), second draw U₂ gives the value, `U₂^(1/6)` for the high-risk group (Beta(6,1) by its exact inverse) and `1 − (1 − U₂)^(1/6)` for the low (Beta(1,6)).
- Quality: `maxMult × 0.5 × exp(0.4 z)`, times `(1 − 0.5 × cipDemo)` only when CIP is on, then floored at 0 and capped at `maxMult`.

The order of the construction draws is that of `makeLatentAgent`: uCCO, uPTF, uPTH, wealth (lognormal), wage (lognormal), octave shape Beta(2,5), quality z (normal), automation risk (two), lambda.

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
`wg = 1.0%` (base growth) `+ 0.8% × max(0.1, 1/(1 + 0.5 × max(0, wage/35 − 1)))` if the BLEI gate exceeds 30 days `+ 0.5% × cipDemo` `+ P_G inflation` (wages indexed to the general price level, `wIdx` 1) `− automation drag × automationRisk`; `wage ← max(0.8 × wage, wage × (1 + wg))`. The octave wage raise is off in the release row (the design pays octaves through conversion). The 80% floor is a stated policy assumption. Since v5.4 the automation drag term is off: automation acts through job loss instead (12.1), and pay falls after a permanent job loss.

### 6.2 BLEI (Basic Living Economic Index)
Days of basic living an adult's resources cover: `BLEI = (0.20 × max(0, wealth) + γ × monthly wage $ + BU food) / daily cost`, with γ = 0.20 for participants and 0.12 otherwise, BU food = one month of the BU spent on essentials, daily cost $68.33 ($31.67 for participants in PTH), lowered by SZH (`agentBLEI`). The **design-neutral** reading applies the no-programme rules to everyone (γ = 0.12, $68.33) and adds one month of the design's regular support (`tbGate`). Both are read in year-0 prices (divided by the price level).

### 6.3 Cost of living and price cuts
The basket is MIT's living-wage budget for one adult (`CFG.BASKET`: food 9.0%, housing incl. utilities 27.6%, medical 6.9%, transport 19.6%, civic 6.6%, internet 3.1%, other 9.2%, taxes 18.0%). Essentials (food, housing, medical: 43.5%) are what BU buy and the essentials prices move. PTF members' basket (excluding taxes) is cut by 12% + 4% × SZH coherence (v5.3; since v5.4 the cut is by sector, 12.3); PTH members' housing component by 35% (`PTH_MODE 'housing'`, `DISC_BASE 'pretax'`). The part of the PTF cut funded from forgone profit (4.94% of the food component and 2.60% of the housing component, utilities; `COST`, BEA) is not counted as programme cost.

### 6.4 BU purchases, expiry and saving
A participant's BU budget is `12 × buEff` a year. BU buy essentials at the adult's own (discounted) prices up to the budget; a BU is worth $1 (N3, N4). Unspent BU expire; all of them go to next year's project pool (`FW.directedShare` 1, `PROJ.share` 1). Each adult then consumes 0.593 of the year's cash surplus (cash income less cost, after conversion and payouts; `SPEND_SOURCED`, derived so the no-programme run's saving rate equals the US personal saving rate of 2025, 5.4%, BEA NIPA Table 2.1), and saves the rest. Since v5.3 `BU_SCOPE 'hub'` (Duke's answer d173) lets BU also buy transport and, in households, childcare, the Hub's list; the release row has it (section 10). The spending share is applied to the household's pooled surplus, and with income-graded spending (6.13) an adult-year whose income is below its cash cost spends `cost × (income/cost)^0.5573` instead.

### 6.5 Project hiring (the conversion of expired BU)
The pool is offered to participants for whom a project hour pays more, after conversion and tax, than an hour of their own wage (contract pay: the living wage per hour, $49,370 / 2,080, indexed). It is shared among them in proportion to octave capacity × quality; each converts at the larger of their own rate and the pool's mean rate (`PROJ.rate 'max'`), with project hours worked beside their job (`hours 'side'`, no cap). Pool that finds no willing worker carries to the next year.

### 6.6 Conversion rate and tax
Own rate `r = min((1 + (q/M) × (C_oct − 1)) × φ × b_PTF, M × 1.618)`, with `C_oct = 1 + (octave/maxOct) × (M − 1)`, `M = maxMult` (9 at the reference), `φ = 1.618` when quality exceeds 0.70 × M (the Phi tier; the threshold's place is a modelling assumption, `dev/reports/v5-11-phi-step.md`), and `b_PTF = 1.30 + θ_SZH` for PTF members. Conversion tax `τ(r) = min(0.75, τ₀(1 − 0.18 × cipDemo) + max(0, (r − 3) × 0.04))`, τ₀ = 12%. Net dollars per BU converted `= r × (1 − τ(r)) × (1 + 0.12 × cipDemo) × income shock`. The tax is kept by the Source.

### 6.7 Essential-service providers (ESPs): payroll, premium and the split
ESPs (grocers, food services, utilities, housing, health care) accept BU at face value. Of what they accept in a year, 20% is next year's payroll in BU (`ESP.lam`, BEA compensation share of essential-industry output), paid to the 23% of adults who are ESP workers (BLS CES; fixed by agent index, no random draw), each up to their last year's wage. A participating worker whose own net rate beats par converts their payroll BU at that rate within octave capacity (net of project BU); otherwise they are paid in dollars and the ESP converts. The ESP converts the rest at 3× under the progressive tax; the premium over face value is split the next year (`SURP`, priv 'prices'):
- The PTFs' share of the premium is the share of BU that PTF members spent. It goes 1/3 to price cuts for PTF members (one uniform cut, capped at 100%; the rest carries), 1/3 to reinvestment (the ESP capital account that builds PTF capacity), 1/3 to a profit share for participating ESP workers by wage, until PTF capacity reaches every adult; then 60% to price cuts and 40% to the profit share.
- Private ESPs pass their premium to the participants who paid them in BU as lower BU prices (in proportion to the BU each spent, capped at their own essentials), after matching the profit-share fraction for their workers (`privWk 'match'`); nothing goes to owners.

### 6.8 Octave advancement
Each year a participant below the top octave advances with probability `1 − exp(−λ' × FBS)`, where `FBS = max(0, Y + BU − basic monthly cost − e × Y)` is the monthly financial bandwidth (Y the monthly wage in dollars, e = 0.12, or 0.025 in PTH) and `λ' = λ × (1 + 0.20 × cipDemo)`. BU is the month's allowance (in a household, the adult's share of the household's BU). The basic monthly cost is the adult's yearly cost of living at this year's prices (in a household, their share of its needs) times their cost factor after the PTF and PTH cuts and before BU purchases, over 12. FBS is in this year's dollars, against a λ set in year-0 dollars (audit finding E7; the `AUD.fbs` correction deflates it).

### 6.9 Joining and leaving
From year 1, an adult takes part when the BU they would use, `min(12 × buEff, M_t × essentials share at own prices)`, is at least the revealed cost of taking part, `12 × 1,200 × uCCO / partRate × P_t`, set so that in year 0 exactly the adults who take part today would; a participant stays at least 2 years (`JOIN`, 'revealed'). With the BU indexed, almost nobody changes their mind (`dev/reports/04-joining.md`).

### 6.10 PTF membership and PTH
PTF: a non-member joins with probability `0.005 + 0.05 × current PTF share` (+0.015 if their BLEI is below 30 days) while capacity allows (Bass diffusion; `uPtfAdopt`), or by SZH induction (`uSzhInduce < 0.16 × θ_SZH` and `uSzhPtfShare < ptfShare`); members never leave (v5.3; since v5.4 they leave at 3.2% a year, 12.3, and PTH members at 6.2%, with Acre Equity growth capped at the price rise + 2%, 12.2). θ_SZH reads the realised PTF density (`THETA_GATE 'density'`: 0 below 55%, rising to 0.25 at 90%). PTH: 25% of the PTH saving is routed from wealth to Acre Equity each year; equity appreciates at 3% + 2% × `uPthAppr` + 1% × SZH coherence; the liquid share of appreciation (15% in the first year, rising linearly to 85% from year 5) is credited to wealth. In v5.2 the whole appreciation also stayed in the Acre Equity, so the liquid share was counted twice; v5.3 takes it out of the equity (`PTH_APPR_CONSERVE`, section 11). The PTH saving here is measured at the BLEI daily cost, so the 25% is 12.6% of the member's actual saving (section 11). A community and zone layer (S37, `COMM`, off in the release) reads the three PTF density tests (the food price cut's 40%, θ and the imitation term) in each community instead of the whole population, and with SZH places the starting members together in zones (`dev/reports/community-layer.md`).

### 6.11 Labour response
Earnings with the programme `E = max(0, E₀ × R^(ε − ρ) − ρ × (unconditional dollars) − ρ_BU × BU spent)`, with ε = 0.33 (Chetty 2012), ρ = ρ_BU = 0.16 (Vivalt et al. 2024/2026), R the programme's raises (the ESP profit share and payroll premium as raises, one elasticity for every change in the return to work); expired BU carry no income effect (ρ_R = 0); every price-cut dollar and last year's liquid PTH appreciation count as unconditional dollars (`LABOR`, `inkindRho`).

### 6.12 Financing, new money and prices
The Source issues the BU, pays conversions and keeps the conversion tax (`fin 'source'`). The release row's cautious reading: of what the Source pays out (BU spent at face value plus conversion proceeds, less output that backs it), none is backed by new output (`a = 0`); counted output is ESP reinvestment (capital goods) and the whole project payout (`PROD.match 'market'`). Unmatched money `U = (1 − a) × (BU spent at face value + conversion paid − matched output)`; the programme's raises are taken as matched by output (`aw` 1) and a write-off at the wealth floor is unmet need, not money. The general price level moves with it: `P_G,t+1 = P_G,t × (1 + λ_G × U_t / Y_t)`, λ_G = 1, Y the year's aggregate cash income (quantity-theory benchmark, a logged placeholder swept in the testbed). Essentials prices move with demand above the no-programme capacity: `P_E,k = 1 + θ_k × (D − S)/S`, θ = 0 (food), 0.6 (housing), 0.5 (medical; unsourced placeholder), and are also multiplied by `P_G`. Basket index `B = 1 + Σ_k share_k × (component_k − 1)`.

### 6.13 Households and children (the main result since v5.3)
`HOUSEHOLDS` (in the v5.3 main result: `REL_V53.hh` = pool 'household', child allowance a quarter of the adult BU, shock 'shore', wealth 'scf'; with income-graded spending `SPEND_GRADE` and BU scope 'hub'; all also in the no-programme run). The adults stay the model's people and are grouped into households once at the start, on their own stream, by the Census CPS ASEC 2023 composition of adults 25-64 (couples with and without children under 18, single parents, single adults; partners paired at random). Children are dependants with an age. A household's needs are MIT's budget for its family type, each component as a ratio to the one-adult budget (so a single adult is exactly the adult-only model), plus childcare for each child under 13 at MIT's prices; each child brings `childBU` (a quarter, d167) of the adult BU. `pool 'household'` (d168) pools a couple's surplus before the spending rule, shares their wealth, applies the debt floor and decides poverty status for the household; `'individual'` has each adult pay an equal share. Partners decide together (participation, PTF, PTH). Household measures count every person, children included, with their household's status (`HH_KEYS`). `BU_SCOPE 'hub'` (Duke's d173) lets BU also buy transport and, in households, childcare. Sources: `sources/households.py`; reports `dev/reports/v5-14-households.md`, `v5-15-bu-scope.md`.

With ageing on (`AGE`), households live through the run (v5.3 B4, B5; `dev/reports/v5-16-childrens-lives.md`): ages at the start are drawn within households (a mother's age from the population at each age times the 2024 birth rate at the age she had each child; the partner's from the Census FG3 spouses' age gap; childless couples and singles from FG3 and the CPS by age); each year children age, leave home at 18 and, from 25, can take the place of an adult who dies (otherwise an unrelated 25-year-old does, as before, and grown children with no place leave the model); women up to 49 give birth at the NCHS 2024 rate for their age times a sourced multiple for having a partner present or not; when the last adult of a household dies its children under 18 leave the model. Estates (d169, `estate 'heirs'`) pass to the surviving partner, else to the children in equal shares (only grown children who are adults in the model receive theirs), else leave the model; Acre Equity stays Acre Equity for an heir in community housing, otherwise it is paid at the liquid share. Partnerships stay as first drawn: no new couples and no separations (a stated limit; it makes the families drift over 20 years, reported in the B4 note).

Calibration readings (v5.3 B7, each off by default and applied in the no-programme run too): `HOUSEHOLDS.wealth 'scf'` starts each household at the 2022 SCF net worth for its type, linked to its wages (ranks combined by a Gaussian copula with the survey's correlation); `SPEND_GRADE` (row option `sg`) has an adult whose income is below their cash cost spend cost x (income / cost)^0.5573 (BLS CE 2024), the measures still using the full cost; `AGE.earn 'cps'` gives wages the shape of US median earnings by age (BLS CPS); `FBS50` (row option `fb`) reads the advancement coefficient as the monthly surplus at which the odds of advancing are even, with an even spread in FBS50 and a scale as options, and reports the share of participant-years at or above it.

Income shocks with households (v5.3 B6, `HOUSEHOLDS.shock`, 0 by default): each adult's yearly swing (uniform 0.90-1.10) shares a household part with their partner's, so the two correlate as set while each keeps its spread; `'shore'` uses Shore (2010): +0.10 in good years, -0.10 in recession years. The macro multiplier (the recession path) stays common to everyone.

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
| Household ages (reading, v5.3) | `s + 500021` | at the start, per household: who is the woman, ages, age gaps (variable count: a gap is redrawn while the partner would be outside 25-66) | only rows with households and ageing |
| Household income shocks (reading, v5.3) | `s + 500041` | per couple-year: 1 (the couple's shared part of the income swing) | only rows with a household shock (`HOUSEHOLDS.shock`) |
| Family events (reading, v5.3) | `s + 500029` | per year: 1 per woman up to 49 (birth), 1 per new adult (sex), 1 per death with more than one grown child waiting (who takes the place) | only rows with households and ageing |
| Job loss (v5.4) | `s + 600031` | 6 per adult-year, whatever the adult's state | both runs of the release row (12.1) |
| Occupations (v5.4) | `s + 600041` | 1 per adult at the start | both runs (12.1) |
| PTH leaving (v5.4) | `s + 600043` | 1 per adult a year from year 1 | programme run (12.2) |
| PTF leaving (v5.4) | `s + 600047` | 1 per adult a year | programme run (12.3) |
| Safety-net take-up (v5.6) | no stream: a hash of (seed + 700001, household head, slot) | none | both runs (12.4) |

A new random process gets its own stream; nothing may add a draw to the main stream. Rows of one study share every stream, so differences between rows come from the rows' rules, not from luck.

## 9. Estimands (what each headline measures)

All are means over the 500 seeds; a change is the mean of the 500 per-seed differences (programme − no programme on the same seed), and its 95% interval is `mean ± 1.96 × sd/√500` of those differences (`tbDiff`).

| Measure (key) | Definition |
|---|---|
| Below the cost of living (`fgt0PY`) | Share of adult-years in which cash income (earnings + conversion + payouts + cash transfers − contribution) is below the adult's own cost of living (the basket after in-kind price cuts and BU purchases). Averaged over all years of the run. |
| Too little wealth (`pov`) | Share of adults whose net wealth at the last year is below $25,000 × the price level (`CFG.POVERTY_LINE`; a design threshold: its origin is undocumented, and the model reads it as about six months of one adult's MIT cost of living, $24,685). |
| Below 30 days of basic living (`bOAPy`) | Share of adult-years with BLEI (the BLEI paper's definition, 6.2) below 30 days, in year-0 prices. Design-neutral version: `bNAPy`. |
| Poverty severity (`fgt2PY`) | Mean over adult-years of the squared shortfall of cash income below own cost, as a share of the basket (FGT2 × 100). |
| Below the US official poverty line (`rep.y7.fpl`, `rep.end.fpl`) | Share of adults whose money income (earnings, conversion, cash transfers; not BU, not SNAP or tax credits) is below $16,749 (`CFG.POVERTY_THRESHOLD_ONE`: the Census threshold for one person under 65, 2025) × the price level, at Year 7 and the last year. `fplX`: the same line on Supplemental-style resources. (`CFG.FED_POVERTY_LINE_1P`, $15,960, is the 2026 HHS guideline: the comparators' guarantee and the validation path's income measures use it, not the release row's.) |
| Gini (`giniD`, `giniX`, `rep.*.giniW`) | Sample Gini of disposable income (`giniD`), of income plus in-kind cuts (`giniX`), of wealth with debts as zero (`giniW`), each × n/(n − 1) (n = 500): an estimate of the Gini of the population the adults are drawn from. The formula (`giniOfArr`): values floored at 0 and sorted, `G = 2 Σ i·v_i / (n Σ v_i) − (n + 1)/n` with i = 1..n, then × n/(n − 1). The uncorrected Gini of the 500 adults is in the release file (`derived.giniFinite`). The validation path's `gini` (Appendix B) is a different quantity; the release row does not compute it. |
| BLEI lines | 7, 30, 120, 365 and 730 days (`CFG.BLEI_CRISIS_MAX` to `BLEI_SECURE_MAX`); the headline uses 30. BLEI keys are computed on three readings: `N` design-neutral, `O` the BLEI paper's (Duke's), `X` net of the contribution; and three groups: `A` all, `P` participants, `N` non-participants as at year 0 (`b<reading><group><Py|Cr|20|Md>`: % of person-years below 30 days, % of person-years below 7 days, % below 30 days at the last year, median days at the last year). |
| Per-seed outputs | The engine keeps every measure unrounded per seed (`tbStudy`'s `_s` arrays); the panel rounds only when it prints (percentages to 1 or 2 decimals, dollars to whole dollars). |
| Programme inflation (`infl`) | Annualised rise of the basket index over the run, `B_{T−1}^{1/(T−1)} − 1`. |
| Price level at the last year (`pLevEnd`, `…Med`, `…P10`, `…P90`) | Full price level `P_{T−1}` across seeds: mean, median, 10th and 90th percentile (the 10th-90th band holds eight runs in ten). |
| Cost per adult (`cost`) | Programme outlays per adult-year in year-0 dollars: BU relief, conversion and the split's price cuts, price-cut dollars (PTF, PTH), liquid PTH appreciation; not the PTF discount funded from forgone profit. |
| Hours (`hrs`) | Change in earnings at a fixed wage from the labour response, % (hours). |
| Median savings (`medWealth`) | Median net wealth at the last year in year-0 dollars. |
| Unhoused (`epPY`) | Share of person-years unhoused, from the extreme-poverty overlay (HUD AHAR 2025 rate scaled by housing distress against year 0). |
| Household reading (`HH_KEYS`, `HH_REP_KEYS`, `HH_LIFE_KEYS`; rows with households) | Every person counted with their household's status: below the cost of living, the official line for the household's size, too little wealth (six months of its costs), below 30 days of basic living; for children alone; by household type; adult-years below the cost of living by age group (with ageing); poverty spells by household type (each household's run of years below the cost of living, the US-data check's spell method, by its type at the start); the Gini and median of income per equivalent adult; with ageing, births, newcomers, children leaving the model and estates. |
| EDC (measured) (`edcM`, `edcMagg`; v5.3, row option `em`, reporting only) | Rent paid to a landlord (MIT housing with utilities; a PTH payment counts 0, as the glossary defines EDC) plus interest paid on debt, over gross income (wages, conversion, Social Security, cash transfers before the contribution, the BU allowance at face): the mean over person-years of the household's ratio (capped at 1) and the ratio of the totals. Beside it, `edcProxy`, the design target proxy (the formula `agentEDC`, set to the BLEI paper's target bands, which the earlier engine shows). |

## 10. The two runs that make the main result

- **Release row, v5.6 (the published panel)** (`releaseRowsV54`, `j: 'release'`): the v5.3 row below with `v54: {rk: true, empl: {}, pthb: {}, ptfs: {}}` (section 12: job loss and re-employment, PTH's books, PTF by sector, the risk measures) and today's safety net with SNAP's work rule and the marginal-rate fix (`sn: {abawd: true, slope: true}`). The no-programme run carries `hh`, `sg`, `g`, `em`, `fb`, `v54` and `sn` too, so every model part that is not the programme is the same in both runs. Every switch and constant in effect while each run goes is listed, as data, in the S50 packet's `release-config.json` (`node dev/packets/make_s50_reference.js config`).
- **Release row, v5.3** (`releaseRowsV53`, `j: 'release'`): the v5.2 release row below with `REL_V53` added: households (`hh`), BU scope 'hub' (`bs`), income-graded spending (`sg`), the two accounting corrections (`g`: `PTH_APPR_CONSERVE`, `SURP_CUT_MARKUP`), and the reporting-only measured EDC and FBS50 (`em`, `fb`). The no-programme run carries `hh`, `sg` and `g` too (`relMainCfgs`).
- **Release row, v5.2** (`releaseRows`, `j: 'release'`): `n1Row(tbPresets(P), 'framework', {fin:'source', a:0, jn:{}, cs:{}, sc:0.593, sp:{priv:'prices'}, pd:{match:'market', speed:'oneyear'}, ml:{}, gc:true})` on the environment's preset `P` (Reference = `FULL_INTEGRATION`: BU $1,200 a month, 78% take part, 18% start in PTF, 20% in PTH, SZH coherence 0.72, CIP 0.65, 6 octaves, multipliers to 9×, conversion tax 12%; Adverse = the same with recessions, automation and 2% inflation; Stress = `STRESS_TEST`: $900, 40%, 8%, 10%, 0.35, 0.30, 4 octaves, 6×, 18%, with recessions, automation and 2% inflation), with project hiring (`PROJ` defaults), ESP payroll (`ESP` defaults), the octave wage raise off and the PTF/PTH inflation damping off.
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

## 12. Added in v5.4 and v5.6 (in both runs unless stated)

The code for each part is a short block in `index.html` whose header comment is the full statement, with sources; this section is the summary an implementer needs. Constants are `CFG` values.

### 12.1 Job loss and re-employment (`EMPL`: auto 'jobs', cut 0.10, rec 'replace', ui on, occupations on)
- **Spells.** Each year an adult who is not still out of work from last year loses their job with chance `pE = 1 − (1 − h)(1 − hA)`: `h` = 8.51% (14.23% in a recession year; `EMPL_P`, `EMPL_P_REC`, CPS flows) and `hA` = the year's automation hazard × the adult's automation risk (automation acts through job loss; the automation wage drag of 5.A1 and 6.1 is off). With the adult's six draws `u0..u5` (12.1's own stream, `s + 600031`, all six taken every adult-year): a spell starts if `u0 < pE` and is an automation loss if `u0 < hA`; its length is `D = emplWeeks(u2)` weeks (the CPS survival curve: `D = 2.5` at u ≥ 1; `2.5 + 7 ln u / ln S₁` for u ≥ S₁; `9.5 + 11 (ln u − ln S₁)/(ln S₂ − ln S₁)` for u ≥ S₂; else `20.5 + τ ln(S₂/u)`, with (S₁, S₂, τ) = (0.4434, 0.1871, 24.18), or (0.5978, 0.3618, 30.90) in recessions); it starts in week `52 u3`; the weeks this year are `min(D, 52 − start)` and the rest carry into later years, at most 52 a year.
- **Unemployment insurance** (both runs): the spell is insured if `u4` < 27.3% (35.6% in recessions); it pays 32.2% of weekly pay for at most 26 weeks of the spell. It is cash income.
- **Back at lower pay.** If the loss was automation's, or `u1` < 41.3% (62.1% in recessions; permanent job losers), pay on return is cut by `2 × cut × u5` (uniform 0 to 20%); the cut applies when the adult is back at work, to the wage and to the wages the reports keep without the programme's raises. After an automation loss the adult's automation risk becomes the low-risk group's mean, 1/7.
- **Hours.** The labour response (6.11) scales with the share of the year at work. In a recession year the recession's income cut for everyone is reduced by the extra weeks recession job loss takes on average, `(EMPL_P_REC × EMPL_W_REC − EMPL_P × EMPL_W)/52` (about 4.2 points), so the loss is not counted twice.
- **Occupations.** At the start each adult gets one of 700 occupations (Frey and Osborne's probabilities, May 2016 BLS employment and pay; `CFG.EMPL_OCC`) on stream `s + 600041`, one draw each: with adults ranked by wage (ties by index), `ρ = √min(1, 0.2651 / var(ln wage))`, `z = ρ Φ⁻¹((rank + 0.5)/n) + √(1 − ρ²) Φ⁻¹(u)`, and the occupation is the first whose cumulative employment share reaches `Φ(z)`. The adult's automation risk becomes that occupation's probability.

### 12.2 PTH's balance sheet (`PTHB`: cap 'hub', x 0.40, exit 0.062; programme run)
- Each PTH home is bought when its first member's books open, at 18.23 years of the member's market housing cost, financed by the trust's debt less the member's starting Acre Equity. Its value moves with the price level and 1.72% real growth a year (FHFA over CPI-U); 37.7% is land.
- The trust's cash each year: in, the market housing cost and the member's equity contribution; out, interest (real 1.80% plus the year's price rise), upkeep (2.31% of the structure's value), property tax (0.65% of value) and appreciation paid in cash. The rest pays down the debt; a shortfall adds to it. Homes − debt = members' equity + community equity, every home every year.
- **Acre Equity grows with the home's value, at most at the year's price rise + 2%** (the Democratic Governance paper's cap); what the home gains beyond that is the community's. The cash part of appreciation (6.10's liquid share) is paid only on the gain above the year's price rise.
- **Leaving.** From year 1 each member leaves the network with chance 6.2% a year (CPS: renters' moves to another county), one draw per adult on `s + 600043` (in a household the head's draw decides). A leaver takes 40% of their Acre Equity in cash (the trust borrows it); the rest becomes the community's. The home passes to the next non-member waiting (in the order of their PTH uptake draw `uPTH`), who starts with no equity.

### 12.3 PTF by sector, and members who leave (`PTFS`: other 0, leave 0.032; programme run)
- **Replaces 6.3's PTF cut.** A member's cut is the sum over sectors of the sector's share of their (household's) basket at this year's component prices times the sector's cut: food `1 − 1/2.64` (`1 − 1/1.65` while fewer than 40% of adults are members; the BLEI paper's epsilons), utilities `1 − 1/1.80` on 12.78% of the housing share (BEA 2025: 487.7 / 3,814.0), transport, health care and childcare 0 (the Hub gives no figure). With SZH the cut is multiplied by `(0.12 + 0.04 × coherence)/0.12`. Capped at 95%.
- **Leaving.** Each year from year 1 a member household leaves with chance 3.2% (one draw per adult on `s + 600047`, the head's draw deciding); leavers can join again through adoption (6.10). The density the food test reads is the members' share of all adults after the year's leavers, at the start of the year.

### 12.4 Today's safety net (`SNET` with `abawd` and `slope`; both runs)
- **SNAP** (USDA FNS FY2026 allotments and deductions, `CFG.SN_SNAP`): net income = gross income − 20% of earnings − the standard deduction − childcare − excess shelter (housing over half of income after the other deductions, capped at $744 a month unless an adult is 60 or older); benefit = allotment − 30% of net income, at least $24 a month for one or two people. Gross income limit 200% of the poverty guideline (broad-based categorical eligibility). Take-up 88%.
- **SNAP's work rule** (7 U.S.C. 2015(o) as amended in 2025): an adult 18-64 in a household with no child under 14 gets SNAP for at most 3 months in 36 in which they do not work 20 hours a week. Countable months are the weeks out of work without unemployment insurance (or every week without it when hours are under half time); each adult's clock holds the last two years' months. A lost month removes the adult from the SNAP household (size one smaller, income still counted); the yearly cut is (lost months / 12) × the difference × (1 − 0.08) (the 8% States may exempt).
- **EITC** (tax year 2025, `CFG.SN_EITC`): phase-in, plateau and phase-out by number of children; couples file jointly, single parents as heads of household, adults without children qualify at 25-64. Take-up 80.8%.
- **Refundable Child Tax Credit** (`CFG.SN_CTC`, `CFG.SN_TAX`): the smaller of $1,700 per child under 17, 15% of earnings above $2,500, and the credit left after income tax before credits.
- Paid on **last year's** income (pay, Social Security, unemployment insurance, conversion income; year 0 reads the pay rate) in year-0 dollars, the amounts indexed to the price level. Take-up is a fixed hash of (seed + 700001, household head, slot): no random stream.
- **Not financed in the model** (the basket's tax line already charges for it): not programme cost, not new money, not in the contribution. It counts as income in basket poverty, FGT and the income-graded spending rule, not in the official poverty measure.
- **Work.** The household's combined marginal rate `m` (benefits lost per extra dollar of earnings, at last year's position; with `slope`, SNAP's gross income test is read as passed, so its cliff is not a marginal rate) scales earnings by `(1 − m)^(ε − ρ)`, and the benefits enter the labour response as unconditional dollars linearised at last year's earnings.

### 12.5 The flat contribution that pays for the price cuts (programme run)
The release row charges every earner `τ_t × max(0, E − X)` (X = 0). The rate for next year is `τ_{t+1} = min(0.90, need_t / base_t)`, where `need_t` is the year's price-cut dollars delivered (PTF and PTH cuts and the split's, less the PTF discount funded by forgone profit) plus the cash part of PTH appreciation, and `base_t = Σ max(0, E − X)`. Year 0's rate comes from a one-year pre-pass with τ = 0 (`tbRun`). The no-programme run pays nothing. The mean rate is about 2.8% in Reference, 3.5% in Adverse and 1.6% in Stress (`tauMean`). This is a modelling reading of who pays for the price cuts (audit finding E2), not part of the Hub's design.

### 12.6 Risk measures (`RISK_MEASURE`; reporting only)
Drawdowns of wealth, recovery times and re-entry into poverty (`RISK_KEYS`, `rkDraw`, `rkReentry`, `tbRiskRes`). No rule reads them and they draw nothing.

## Appendix A. The gaps the first independent implementation found (S10), and where each is now closed

| S10 gap | Closed by |
|---|---|
| 1 The description and the validation results are of two models | The S50 packet's reference is the release row this document describes; the validation path is described in Appendix B. |
| 2 Samplers (lognormal, Beta, gamma) | 4.1 |
| 3, 4 No spending rule; wages not indexed (validation path) | Appendix B; the release row has both (6.4, 6.1). |
| 5, 6 `mulberry32`; the normal generator | 4.1 |
| 7 Quality floor, cap, CIP factor | 4.1 |
| 8 Automation risk draws | 4.1 (replaced by the occupation in the release row, 12.1) |
| 9 Range of the BU spending draw | Appendix B (0.60-0.90; drawn but not used by the release row, whose BU purchases follow 6.4) |
| 10-21 How the validation path's BU, costs, prices, octave raise, CIP bonus, BLEI test, FBS cost, SZH threshold, induction, PTH equity, adoption timing and capacity work | Appendix B |
| 16 "Basic monthly cost" (release row) | 6.8 |
| 22 No recession in year 0 or the last year | 4, item 3 |
| 23 Automation drag cap | Appendix B (the release row has no wage drag: 12.1) |
| 24, 25 `calcMetrics` and its Gini | Appendix B; the release row's measures are section 9 (it does not call `calcMetrics`). |
| 26 The official poverty line ($16,749 against $15,960) | Section 9 |
| 27 Keys whose functions were not in the S10 packet | Section 9; the S50 packet holds every function the release row runs. |
| 28 BLEI tiers | Section 9 |
| 29 Rounding | Section 9 (per-seed outputs are unrounded) |
| 30 Wealth floor −$10,000 | Section 5, B19 (the testbed sets it for every run) |
| 31 Year-0 distributions | Checked again by S50 against the packet's year-0 keys. |

## Appendix B. The validation path (`runScenario`; `node harness.js validate`, the earlier engine's presets)

The validation presets (Traditional Welfare Baseline, CCO Only, Full Integration, Adverse, Stress Test) run the engine's older yearly loop, with every release mechanism of sections 6.4-6.13 and 12 off. They are the engine's regression fixtures, not results. S10 reproduced them exactly (`dev/reports/s118-independent-implementation/`). How they differ from the release row:
- **No spending rule:** the whole cash surplus is saved (`SURPLUS_CONSUMPTION_SHARE` 0). **No price module:** the cost of living rises at the preset's inflation rate, reduced each year by `(1 − 0.5 × PTF share)(1 − 0.10 × PTH share)`, and the year's reduced rate is raised to the power of the year; wages are not indexed to it.
- **BU:** a participant is credited the monthly BU once a year, spends a uniform 0.60-0.90 share of it (`uSpendFrac`) and converts what they spend at their own rate; costs fall through a relief `1 − min(0.5, 0.20 × BU / ($1,200 × price level))` on the whole basket, with the PTF factor `1 − (0.12 + 0.04 × coherence)` and the PTH factor 0.65 on the whole basket.
- **Wages:** the octave raise (0.3% per octave) is on for everyone; the CIP bonus applies to everyone; the BLEI test reads the scenario's own BLEI (γ 0.20 for participants, BU food a fixed 990/1,200 of the monthly BU, the PTH daily cost). The automation drag reaches its 10-point cap in year 13.
- **Octaves:** the basic monthly cost is the BLEI daily cost × 365 × the year's price index × the cost factor after every cut, over 12; this year's wage after growth.
- **PTF and PTH:** θ_SZH reads the coherence setting, not the realised density; SZH induction only for participants; adoption from year 1 on the start-of-year share; no capacity limits. PTH equity and appreciation apply to every member, the saving measured on the whole basket at the BLEI daily cost, and the liquid share of appreciation is also kept in the equity (counted twice; corrected in the release row, section 11).
- **Measures (`calcMetrics`):** wealth poverty below $25,000 nominal; the nominal median; 10th and 90th percentiles by linear interpolation. Its Gini at year 0 is of wealth with debts as zero; later it is the Gini of each adult's wealth less one year of the extractive-debt-cost proxy times their annual wage (EDC × monthly wage × 12), floored at zero, with no n/(n − 1) factor. The income measures use $15,960.
