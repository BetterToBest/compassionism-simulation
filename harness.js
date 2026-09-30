'use strict';
/* ═══════════════════════════════════════════════════════════════════════
 * Standalone Node.js harness — pure functions extracted verbatim from
 * index.html (Compassionism Framework Simulation, pre-harness version v4.7)
 * for out-of-browser verification and sensitivity analysis.
 *
 * Built fresh this session. NOT assumed identical to any prior session's
 * harness (no such file was available to copy). Every function below is
 * transcribed directly from the shipped <script> block. Validated against
 * the documented seed-42/Full Integration/20yr regression figures (see
 * `validate` mode) BEFORE being trusted for the WEALTH_FLOOR sweep — this
 * mirrors HANDOFF.md's explicit instruction for whoever builds this.
 *
 * v4.17: recessions ported (updateRecession/buildRecessionPath; runScenario honours
 * p.shock), structuralStability() parity with index.html restored, income/basket poverty
 * and year-0 reference figures added to runScenario()'s result, and four new modes:
 * headline, year0, stress, participation. `validate` is unchanged in every figure.
 *
 * v4.18: the extreme-poverty overlay (housingDistressOf/housingDistressYear0/extremePovertyOf,
 * CFG.EP_*) ported verbatim; runYear() records start-of-year wealth (reporting only, no RNG);
 * runScenario() returns the overlay and its components; CCO_ONLY mirrors simulate()'s pCCO; and
 * a new `extreme` mode prints the v4.18 tables and the constants' sensitivity. `validate` is
 * unchanged in every pre-v4.18 figure.
 *
 * v4.19: the automatic stabilizers (effective BU per year: recession multiplier, fixed or scaled;
 * suspended expiry; emergency enrollment via the stored latent a.uCCO; COLA) and Option B's
 * BU-scaled CCO cost relief (CFG.CCO_RELIEF_*), ported from index.html; shockRun/shockStudy
 * (the in-page Shock Response study, exported so domtest.js can check the two agree exactly);
 * two harness-only switches, BU_ALLOCATIONS_PER_YEAR and CCO_RELIEF_FLAT, kept for before/after
 * comparison; and a `stabilizer` mode. `validate` was unchanged in every figure.
 * (Added in v4.20: this header had no v4.19 entry, though the code below was current.)
 *
 * v4.20: drawAutomationRisk() samples both mixture components by inverse CDF (exact for
 * Beta(a,1) and Beta(1,b)), so it always takes two RNG draws, and the high-risk share is
 * recalibrated from 0.47 to 0.63 (CFG.AUTO_*), which matches the employment-weighted mean
 * probability of Frey & Osborne's 702 occupations (0.592). Both move the seed-42 regression, once. A harness-only switch,
 * AUTOMATION_SAMPLER_LEGACY, restores v4.3-v4.19's rejection-sampled draw for before/after
 * comparison. `validate` now asserts its figures and exits non-zero on a mismatch, and also
 * checks that the legacy switch reproduces v4.19. New: unitSuite() (pure-function and
 * property tests, run here by `unit` and against the page by domtest.js), and an `automation`
 * mode (the calibration sweep behind the new share).
 *
 * v4.21: runYear() reads CCO relief off effective BU in year-0 dollars (buEff / priceIdx), ported from
 * index.html, with RELIEF_PRICE_LEGACY restoring v4.20; two harness-only switches for studies
 * (PATHWAY_OFF, SURPLUS_CONSUMPTION_SHARE), both inert by default; `--agents=N` for every mode;
 * `validate` asserts seed-42 fixtures for all six presets; and four modes: `largen` (the large-N
 * headline, preset and population-size study), `pathways` (the v4.14 pathway decomposition),
 * `saving` (where the wealth comes from, and a consumption sweep) and `v421` (the investigation
 * behind CONTRIBUTING.md's v4.21 Release Notes).
 *
 * v4.22 (next-round session 1, Sep 26 2026): LEDGER, a reporting-only tally
 * of every money flow runYear() computes, and the `ledger` mode (the A1 issuance ledger); and
 * SURPLUS_CONSUMPTION_BASE, which lets SURPLUS_CONSUMPTION_SHARE apply to all cash surplus. Both are inert
 * by default, and `ledger identity` checks that the tally changes no output. index.html is unchanged.
 *
 * v4.22 (next-round session 2, Sep 26 2026): CFG.BASKET (the living-wage basket by component, N10); PTF_MODE (D4);
 * CONVERSION_MODEL 'framework' (N1-N4); PRICE, the A2 issuance and price module (P_E, P_G, COLA on the endogenous rate,
 * wage indexation), driven by priceRun()/priceStudy(); NEXT_ROUND, the D1 consumption rule as a profile; priceUnitSuite(),
 * run by `unit`; and the `price` mode. Every switch is inert by default: `validate`, domtest's parity checks and the
 * price suite's "fully matched" and "zero issuance" tests confirm bit-identical runs. index.html is unchanged.
 *
 * v4.22 (next-round session 3, Sep 26 2026): the A2 sweep machinery (s3BaseS/s3Point/s3Breakeven/s3Config: breakeven
 * additionality by bracketed secant search on the exact CRN seed mean, with a bootstrap interval over seeds and the a at which 90%
 * of seeds are within tolerance), S3_ROWS (the one-at-a-time sweep) and s3StabArms (the recession stabilizer arms), run by the
 * `price` sections be | inert | sweep | corners | stab; two new price-suite tests; and S3-1, the price module's aw accounting (an
 * unmatched raise enters as the year's change in the premium; awLevel restores session 2's reading). Every default run is
 * unchanged: validate, unit and domtest pass. index.html is unchanged.
 *
 * v4.22 (next-round session 4, Sep 27 2026): LABOR, the A3 labor-supply module (income effect rho on unconditional
 * support; wage elasticity eps on program-induced raises; conversion read as rent, dissipated project time, or between,
 * by delta), and p.ubi, a flat cash transfer to every adult for the matched-cost UBI comparator; laborRun()/laborStudy(),
 * laborUnitSuite() (run by `unit`) and the `labor` mode. Both are inert by default (LABOR null, ubi unset): validate,
 * unit and domtest pass and every shipped figure is bit-identical. index.html is unchanged.
 *
 * v4.22 (next-round session 5, Sep 27 2026): three restudy switches, THETA_GATE (theta on realised PTF density, C08),
 * PTH_MODE (PTH cuts housing only, d4) and DISC_BASE (discounts skip the basket's tax share, d5); a joint price and labor
 * run (priceRun option `labor`); the price-neutral search s5Neutral() (d18: additionality may exceed 1); a lamG 1.41 sweep
 * row (quantity theory at US M2 velocity); s5UnitSuite() (run by `unit`); the `restudy` mode; and `labor --env=`. All
 * inert by default: validate, unit and domtest pass and every shipped figure is bit-identical. index.html is unchanged.
 *
 * v4.22 (session 11, Sep 28 2026, Duke's review): PR.ccoTop and tbMatch('ccoTop') (a participant-only needs-based top-up at
 * equal cost; nit.part), the `topup` section, PR.grocPilot (five stores, TB_GROC_PILOT), PR.xcFull (X-Cents Power of 1; groc.housing),
 * the proposed-size constants (TB_UBI_PROP, TB_NIT_PROP, TB_ENDOW_PROP), a5 rows for all of them, and a second front-door view
 * ('prop'). Every other row is bit-identical; 2 unit tests.
 * v4.22 (next-round session 6, Sep 27 2026): the A4 policy testbed. Comparator presets (UBI, NIT, public grocery, asset
 * endowment, X-Cents) beside Compassionism under one cost ledger, one income effect and one wage elasticity (d24-d26, d28);
 * a tax/money financing switch (TB, p.tb); basket FGT0-2 and a group check; per-row pathway switches (d19); tbUnitSuite()
 * (run by `unit`); and the `testbed` mode. runYear hooks are inert unless a preset carries p.tb: validate, unit and domtest
 * pass and every shipped figure is bit-identical. index.html is unchanged.
 * v4.22 (next-round sessions 7-10, Sep 27-28 2026): the testbed's decomp, alts, a5 and n7 sections; FBS_BU_ONCE,
 * PTH_APPR_CONSERVE and N7_BLEI (the i3 engine questions, harness-only); the `frontdoor` writer, which puts the a5 comparison
 * into index.html's front door; and TB_PROFILE_G, which turns N7_BLEI on in the testbed profile (d40). The engine in
 * index.html is unchanged in every one of these sessions.
 * ═══════════════════════════════════════════════════════════════════════ */

var CFG = {
  POVERTY_LINE:25000, BLEI_CRISIS_MAX:7, BLEI_PRECARIOUS_MAX:30,
  BLEI_THRESHOLD_MAX:120, BLEI_STABLE_MAX:365, BLEI_SECURE_MAX:730,
  BASE_DAILY_COST:68.33, CCO_PTH_DAILY_COST:31.67,
  WEALTH_INIT_MU:10.5, WEALTH_INIT_SIGMA:1.2,
  SZH_ALL_RESIDENTS:0.06, SZH_PTF_BONUS:0.05,
  SZH_THETA_THRESHOLD:0.55, SZH_THETA_MAX_COH:0.90, SZH_THETA_MAX:0.25,
  EDC_BASELINE_LO:0.62, EDC_BASELINE_HI:0.72, EDC_PTH_CAP:0.10,
  PROG_PIVOT:3.0, PROG_RATE:0.040, PROG_TAX_MAX:0.75,
  SIM_COST_SCALE:1500,
  WAGE_MEDIAN_SIU:35,
  WEALTH_FLOOR:-10000,
  WAGE_BASE_GROWTH:0.010, WAGE_BLEI_BONUS:0.008, WAGE_OCTAVE_BONUS:0.003,
  AI_DISPLACEMENT_YEAR_1:5, AI_DISPLACEMENT_YEAR_2:15,
  AI_DISPLACEMENT_RATE_1:0.012, AI_DISPLACEMENT_RATE_2:0.022,
  TARGET_WEALTH:82000, TARGET_STABILITY:0.90, TARGET_POVERTY:0.05,
  TARGET_FLOURISHING:0.50, TARGET_GINI:0.25, TARGET_EDC:0.10,
  NORDIC_GINI:0.28, CCO_OPTIMAL_BU:1200, CCO_MIN_PARTICIPATION:0.55,
  PTF_OPTIMAL_SHARE:0.18, PTF_DISTORTION:0.30,
  PHI_RATIO:1.618, PHI_QUALITY_THRESH:0.70,
  FBS_LAMBDA_LO:0.0001654, FBS_LAMBDA_HI:0.0013233,
  FBS_EDC_RESIDUAL_BASE:0.12, FBS_EDC_RESIDUAL_PTH:0.025,
  FBS_CIP_LAMBDA_BOOST:0.20,
  BASELINE_CPI_RATE:0.03,
  PTH_EQUITY_CONTRIB_SHARE:0.25,
  PTH_LIQUID_SHARE_YEAR1:0.15, PTH_LIQUID_SHARE_YEAR5PLUS:0.85, PTH_LIQUID_SHARE_MATURE_YR:5,
  PTF_BASS_Q:0.05,
  WAGE_TO_USD:100.52,
  LIVING_WAGE_ANNUAL:49370,
  SS_ANCHOR_SSI_ANNUAL:11928, SS_ANCHOR_SSDI_ANNUAL:19560, SS_ANCHOR_RETIRE_ANNUAL:24852,
  /* v4.18: extreme-poverty overlay constants — sources in index.html's CFG. */
  EP_Y0_RATE:0.0022, EP_SMI_SHARE:0.25, EP_VOL_SHARE:0.02, EP_WZ_EFFECT:0.50,
  /* v4.19: automatic-stabilizer reference values — sources and conditions in index.html's CFG. */
  CCO_RELIEF_AT_REF:0.20, CCO_RELIEF_REF_BU:1200, CCO_RELIEF_CAP:0.50,
  STAB_HUB_MULT:1.20, STAB_HUB_THRESH:0.02, STAB_NEUTRAL_MULT:1.35, STAB_NEUTRAL_K:2.8, STAB_MULT_MAX:4,
  STAB_EMERG_TAKEUP:0.50, COLA_HUB_THRESH:0.05, STAB_STUDY_SEEDS:30,
  /* v4.20: automationRisk mixture — sources in index.html's CFG. */
  AUTO_HIGH_SHARE:0.63, AUTO_HIGH_A:6, AUTO_LOW_B:6
};
CFG.FBS_HALF_SAT_LO = Math.log(2) / CFG.FBS_LAMBDA_HI;
CFG.FBS_HALF_SAT_HI = Math.log(2) / CFG.FBS_LAMBDA_LO;

var RNG = Math.random;
/* v4.16: counterfactual switch for the PTH appreciation-accounting question logged in
 * CONTRIBUTING.md's v4.16 notes. false (the default, and the only value any validated mode
 * uses) reproduces index.html exactly: the FULL appreciation is added to acreEquity AND the
 * tenure-based liquid share is credited to wealth. true is the value-conserving alternative
 * (acreEquity keeps only the non-liquid remainder). Read only by the `pth-accounting` mode. */
var PTH_APPR_CONSERVE = false;
/* v4.19: two harness-only switches recording the decision on how the BU amount reaches a
 * household (CONTRIBUTING.md v4.19; Duke chose Option B, which index.html now ships). Both
 * default to index.html's behaviour, bit-identically.
 *  BU_ALLOCATIONS_PER_YEAR — BU allocations credited per simulated year (index.html: 1). 12
 *    approximates monthly tranches at expiry=1: each month's allocation is spent at the year's
 *    spend fraction and the remainder expires. The 3x cap scales with it.
 *    (Option A, not adopted.)
 *  CCO_RELIEF_FLAT — true restores v4.18's flat 0.80 CCO cost relief (index.html: false, i.e.
 *    Option B: relief scales with the effective BU). For before/after comparisons only. */
var BU_ALLOCATIONS_PER_YEAR = 1;
var CCO_RELIEF_FLAT = false;
/* v4.20: harness-only switch. true restores v4.3-v4.19's drawAutomationRisk(): the mixture
 * components drawn by beta() (gamma rejection sampling, a variable number of RNG draws), with
 * the share read from CFG.AUTO_HIGH_SHARE and the shapes fixed at Beta(6,1)/Beta(1,6). With
 * AUTO_HIGH_SHARE set back to 0.47 it reproduces v4.19 exactly (checked by `validate`).
 * index.html: false. */
var AUTOMATION_SAMPLER_LEGACY = false;
/* v4.21: harness-only switch. true restores v4.19-v4.20's CCO relief share, read off NOMINAL
 * effective BU against the year-0 $1,200 reference (an unindexed BU kept its real relief under
 * inflation, and COLA counted inflation twice). Inert at 0% inflation. index.html: false. */
var RELIEF_PRICE_LEGACY = false;
/* v4.21: harness-only switches for the `pathways` and `saving` modes (CONTRIBUTING.md v4.21). Both
 * default to the shipped engine, bit-identically (checked by `validate`).
 *  PATHWAY_OFF — switch off one channel through which CCO or PTH reaches wealth, CRN-paired:
 *    relief (CCO cost relief), conversion (conversion proceeds), octave (octave advancement),
 *    octaveWage (the octave wage-growth bonus), bleiWage (the BLEI-gated wage-growth bonus),
 *    pthCost (PTH's 35% cost reduction, and with it the equity routing it funds),
 *    pthEquity (equity routing and liquid appreciation; the saving stays in wealth).
 *    The v4.14 pathway-decomposition item (Good First Issues, v4.14 (b)).
 *  SURPLUS_CONSUMPTION_SHARE — the share of income above the agent's own basket cost that the
 *    agent consumes. The engine consumes exactly the basket (0), so every dollar above it is saved. */
var PATHWAY_OFF = {relief:false, conversion:false, octave:false, octaveWage:false, bleiWage:false, pthCost:false, pthEquity:false};
var SURPLUS_CONSUMPTION_SHARE = 0;
/* Session 7 (dashboard i3-1, s23): harness-only switch. The engine's FBS gate on octave advancement reads the monthly basic cost
 * AFTER the CCO relief discount and then adds effective BU on top, so BU enters FBS twice (the framework branch already reads the
 * cost before the relief). true: the engine branch reads the pre-relief cost, as the framework branch does. index.html: false. */
var FBS_BU_ONCE = false;
/* Session 9 (dashboard i3-2): N7 attribution of the BLEI-gated wage raise. The N7 split counts the octave and CIP raises as
 * program-induced and the BLEI-gated raise as not, since the Baseline has it too. But in a design the raise can fire only
 * because the design's own support lifts the adult over the gate. N7_BLEI true counts the BLEI raise as program-induced in
 * exactly those adult-years: the gate passes as the run reads it (the shipped or the design-neutral gate) and fails on Baseline
 * rules with no program support (agentBLEI(a, 0, false, ...)). Direct, same-year attribution only: a raise that passes on
 * Baseline rules is not attributed, even where program-built wealth put the adult there. The same rule applies to every
 * design. It moves the labor module's raise (uncompensated response) and, where aw < 1, the price module's unmatched
 * premium; the raise itself is unchanged. Default false (the attribution through session 8). No RNG. */
var N7_BLEI = false;
/* Session 1 of the Sep 26 plan: which income SURPLUS_CONSUMPTION_SHARE applies to. 'wage' (the v4.21
 * behaviour): the share of wage income above the agent's basket, taken right after the wage step, so
 * conversion proceeds and PTH liquid appreciation are always saved in full. 'cash': the share of ALL cash
 * surplus that year (wage + net conversion + liquid PTH appreciation − basket − PTH equity routing), taken at the end of the
 * agent's year, before the floor clamp; conversion proceeds first offset any wage deficit. Inert when the
 * share is 0 (the default), so every shipped figure is bit-identical. For the consumption-rule decision. */
var SURPLUS_CONSUMPTION_BASE = 'wage';
/* A1 issuance ledger (Next Round Plan, Sep 26 2026): harness-only and reporting-only. When LEDGER is
 * an object, runYear() adds each money flow it already computes to it, by year. It draws no random
 * number and writes nothing any dynamic reads (the one per-agent field, _ledFloor, is read only by the
 * `ledger` mode), so a run is bit-identical with it on or off; `ledger` checks this on every scenario.
 * null (the default, and index.html's behaviour) skips every ledger line. Flows are nominal dollars;
 * each year also records its price index so the report can deflate to year-0 dollars. */
var LEDGER = null;
var LEDGER_RATE_TIERS = [1.5, 3, 6, 9];  /* conversion-rate tier upper bounds: <1.5, 1.5-3, 3-6, 6-9, >=9 (3 = PROG_PIVOT, 9 = maxMult) */
function newLedger(){ return {tot:{}, real:{}, idx:1, y:[], tiers:[0,1,2,3,4].map(function(){ return {bu:0, gross:0, tax:0, net:0, n:0}; })}; }
function ledAdd(yr, k, v){ var L = LEDGER, Y = L.y[yr] || (L.y[yr] = {}); L.tot[k] = (L.tot[k] || 0) + v; L.real[k] = (L.real[k] || 0) + v/L.idx; Y[k] = (Y[k] || 0) + v; }
/* ─── Next-round session 2 (Sep 26 2026; Duke assigns the version). Harness-only switches, every one inert by
 * default, so index.html and every shipped figure are unchanged (`validate` and domtest's parity checks).
 *
 * CFG.BASKET (decision N10): components of LIVING_WAGE_ANNUAL as shares of the pre-tax budget. Source: MIT Living
 * Wage Calculator (data of Feb 15, 2026), 1 adult, 0 children, "Typical Expenses". LIVING_WAGE_ANNUAL is the
 * unweighted mean of the 51 state living wages x 2,080 (checked in-session: $49,369.82). The site asks not to be
 * scraped, so the components come from 8 state pages read by hand (AL, CA, CT, HI, ID, IN, ME, WV; about one per
 * sixth of the 2026 ranking): each component's dollars regressed on the state's pre-tax total, evaluated at $49,370.
 * Housing is HUD Fair Market Rent, which includes tenant-paid utilities. `taxes` is income and payroll tax, which no
 * discount can reduce. See session-2-handoff.md for the sample and the fit.
 * ESSENTIALS: the components BU can buy and P_E prices (food, housing incl. utilities, medical: 43.5% of the basket). */
CFG.BASKET = {food:0.0901, housing:0.2761, medical:0.0685, transport:0.1955, civic:0.0663, internet:0.0314, other:0.0924, taxes:0.1797};
CFG.BASKET_KEYS = ['food','housing','medical','transport','civic','internet','other','taxes'];
CFG.ESSENTIALS = ['food','housing','medical'];
/* PTF_MODE (decision D4): 'shipped' = PTF cuts the whole basket by 12% (+4% x SZH coherence), as index.html does;
 * 'food30' = 30% off the food component only (the NYC public-grocery pilot's PROMISED cut, not an observed one);
 * 'food62' = 62% off food only (the hub's eps_food = 2.64: 1 - 1/2.64). Food modes ignore the SZH add-on. */
var PTF_MODE = 'shipped';
var PTF_FOOD_CUT = {food30:0.30, food62:0.62};
/* CONVERSION_MODEL (decisions N1-N4). 'engine' = index.html: each participant converts one allocation of their own
 * spent balance; CCO relief is 20% of the basket. 'framework' = the Research Hub's description:
 *  N3: one BU budget, 12 x effective BU a year per participant.
 *  N4: BU buy essentials at the agent's own (PTF/PTH-discounted) prices, up to the budget; a BU is worth $1 to all.
 *  N1: businesses convert the BU they accept at FW.bizRate (placeholder; hub cafe example 2-4x) on FW.bizCap of it
 *      (operational cap, placeholder; the rest converts at par), under the engine's progressive tax. The premium over
 *      a cash sale (net proceeds - BU accepted) is paid out the next year to ALL agents in proportion to wage income,
 *      standing in for business revenue paid out as wages and profit (the model has no firms: an assumption).
 *  N2: unspent BU expire; FW.directedShare of them go to projects and are converted the next year by participants
 *      in proportion to octave capacity x quality, at each one's own engine rate, within octave capacity
 *      (FW.octaveCapBase x 2^octave BU a month; engine octave k = hub octave k+1). The rest are destroyed.
 * Year-0 pools are empty and the last year's pools are never paid out (the run ends). */
var CONVERSION_MODEL = 'engine';
var FW = {bizRate:3, bizCap:1, directedShare:1, octaveCapBase:1000};
var FWS = null;  /* per-run framework state (pools carried from one year to the next); reset by runYear at yr 0 */
/* N1, session 15 (dashboard s33; decisions d58-d65; N1-design-project-hiring.md): PROJECT HIRING PAID IN EXPIRED BU, the design's
 * mechanism in place of the octave wage raise (d46). PROJ = null (the default) leaves every run bit-identical (checked by `unit`).
 * When an object, in both conversion models:
 *  pool   last year's expired BU x share (engine: the unspent balance that expires, A0 flow 3, destroyed when PROJ is off; framework:
 *         the BU budget left unspent, N2's pool), plus the launch gift (rollout plan: 1,000 expired BU per participant) collected
 *         in year 0 and paid in year 1 when giftMode is 'forward'. Pool that finds no worker carries to the next year.
 *  pay    contract pay, BU per project hour in year-0 dollars, indexed to the basket price level (default: the model's living wage,
 *         $49,370 / 2,080 hours, at par; d63).
 *  alloc  'capq': participants for whom a project hour pays more, after conversion and tax, than an hour of their own wage, weighted
 *         by octave capacity x quality (d61); 'capqAll': the same weights, no willingness test (the framework model's N2 rule);
 *         'low': the willing, lowest wage first, each up to capacity; 'equal': equal shares among the willing.
 *  rate   'max': the higher of the worker's own rate and the contract rate, the capacity x quality-weighted mean own rate of
 *         participants (R4, R5; d62); 'own': own rate only. Progressive conversion tax, CIP bonus and income shock as in the engine.
 *  cap    false (d64, Duke's pick): no conversion cap. true: each participant converts at most 12 x FW.octaveCapBase x 2^octave BU a year: project BU fill what the engine's own
 *         spent-balance conversion leaves (that conversion is left uncapped; it never reaches the smallest capacity at $1,200 BU);
 *         BU above it are saved and converted in later years (d64).
 *  hours  'side' (d63, Duke's pick): project hours are added on top of wage work; 'displace': each project hour replaces an hour
 *         of wage work at the worker's own wage. 'low' allocation always fills each worker up to octave capacity. Project
 *         pay is earned, so it carries no income effect. The testbed's hours measure counts wage plus project hours.
 *  giftMode 'forward' | 'holder' (each participant converts their own gift at their own rate from year 1, with no hours: an
 *         unconditional dollar, so it enters the labor module's rent channel) | 'none'.
 *  giftFin how the testbed's flat contribution pays for the gift's proceeds (d66; issue i7, session 16): 'payg' (Duke's pick) in
 *         the year they are paid, so the year-2 contribution rises; 'run' spread over the remaining years of the run, the rule
 *         the testbed applies to the asset endowment (d26). The cost counted is the same; only its timing, and so the work
 *         response to the contribution, differs. Read only by the testbed's tax and hybrid financing.
 * Allocation is deterministic: no RNG draw is added (CRN holds). With PROJ on, the framework model's N2 allocation is replaced.
 * PJS: per-run state, reset by runYear at yr 0; PJS.acc tallies the flows in year-0 dollars for the testbed and the unit tests. */
var PROJ = null;
var PROJ_DEFAULTS = {share:1, gift:1000, giftMode:'forward', giftFin:'payg', pay:CFG.LIVING_WAGE_ANNUAL/2080, alloc:'capq', rate:'max', hours:'side', cap:false, hrsYr:2080};  /* Duke's picks (Sep 30): d63 side hours, d64 no cap, d66 pay as you go */
var PJS = null;
function pjOwnRate(a, p, pcb){ var oc = 1 + (a.octave/Math.max(1, p.maxOct))*(Math.max(1, p.maxMult) - 1), qf = Math.min(1, a.quality/Math.max(1, p.maxMult));
  var ph = (p.phi && a.quality > p.maxMult*CFG.PHI_QUALITY_THRESH) ? CFG.PHI_RATIO : 1.0, pb = (p.ptf && a.inPTF) ? pcb : 1.0;
  return Math.min((1 + qf*(oc - 1))*ph*pb, p.maxMult*(p.phi ? CFG.PHI_RATIO : 1.0)); }
function pjTax(p, r){ var bT = p.cip ? p.tax*(1 - p.cipDemo*0.18) : p.tax; return Math.min(CFG.PROG_TAX_MAX, bT + Math.max(0, (r - CFG.PROG_PIVOT)*CFG.PROG_RATE)); }
function pjNewAcc(){ return {pool:0, gift:0, exp:0, alloc:0, carry:0, conv:0, giftConv:0, gross:0, net:0, giftNet:0, hrs:0, disp:0, work:0, partY:0, rc:0, rcN:0, overCap:0, unwilling:0}; }
/* N1, session 19 (s38; decisions d70-d76; N1-design-esp-payroll.md): ESP PAYROLL IN EXPIRED BU AT WORKERS' OWN RATES, the design's
 * mechanism (Duke's R7, Sep 29) for the wage part of the Hub-spec model's business conversion (N1 above). Framework model only: the
 * engine model has no business conversion and ignores ESP (d70). ESP = null (the default) leaves every run bit-identical (session 19
 * diffed full outputs against b1bc475; `unit` checks lam 0 against ESP off). When an object:
 *  lam   payroll share (d71): of the BU essential service providers accept in year t, lam are paid out as wages in year t + 1 (the
 *        premium's timing today) and the rest convert at FW.bizRate as now. 0.20 = compensation / gross output in the essential
 *        industries, weighted by CFG.BASKET's essentials (BEA GDP-by-industry, 2024 values: 0.20 on both the Jun 25 and the Sep 30, 2026 releases; range 0.15-0.26,
 *        leaning high because BEA measures a grocer's output as its margin; sources/esp_payroll_share.py).
 *  work  who the ESP workers are (d72): a share of adults (0.230 = BLS CES Table B-1, Aug 2026: grocers, food services, utilities,
 *        real estate and health care / total nonfarm; 0.152 without food services), assigned by agent index (the fractional part of
 *        (i + 1) x 0.618... below the share: no RNG, the same adults in every design and seed); 'ptf' = this year's PTF members (the
 *        Hub's "PTF workers"); 'all' = every adult (today's payout population).
 *        The pool is shared among ESP workers in proportion to last year's wage income, each share capped at that wage; any excess
 *        returns to the ESP.
 *  take  'par' (d73): a participating ESP worker whose own rate (octave, quality, Phi, PTF bonus; the rate project hiring reads) after
 *        the progressive tax, times the CIP bonus, beats par takes their share as expired notes and converts it; 'biz': only where the
 *        own rate beats FW.bizRate (a revenue-maximizing ESP). Everyone else is paid in dollars, and the ESP converts those BU itself.
 *  cap   'dollars' (d74): payroll conversion is capped at 12 x FW.octaveCapBase x 2^octave BU a year, net of this year's project BU;
 *        BU above it are paid in dollars (the ESP converts them). 'save': the excess is saved and converted first in later years (R6).
 *        'none': no cap.
 *  rest  'all' (d75): the ESP's own premium, on the share it keeps and on the BU returned to it, is paid as today: next year (the
 *        returned BU: this year, with the rest of last year's premium) to every adult by last year's wage, the stand-in for the ESP's
 *        other costs and surplus. 'esp': to its own workers by last year's wage (a worker cooperative).
 * Income: wages are unchanged, so BU pay counts at face value in wages and the contribution base; the premium over face value,
 * BU x (rate x (1 - tax) x CIP bonus x income shock - 1), is conversion income: program cost, and P_G under money or hybrid financing.
 * Labor: the premium is earned by working at an ESP, so it enters the wage elasticity as a raise, 1 + premium before the income shock /
 * last year's wage, inside the same uncompensated factor as every other raise, with no income effect (the fairness rule). The ESP's
 * own premium keeps today's treatment. No RNG is drawn in any ESP step.
 * ESS: per-run state, reset by runYear at yr 0; ESS.acc tallies the flows in year-0 dollars for the testbed and the unit tests. */
var ESP = null;
var ESP_DEFAULTS = {lam:0.20, work:0.230, take:'par', cap:'dollars', rest:'all'};
var ESP_GOLD = (Math.sqrt(5) - 1)/2;
var ESS = null;
function esNewAcc(){ return {accBU:0, ownBU:0, poolPaid:0, alloc:0, conv:0, ret:0, retNon:0, retPar:0, retCap:0, retWage:0, retNet:0, gross:0, tax:0, prem:0, rateXbu:0,
  wkY:0, wkY1:0, wage:0, partWkY:0, tk:0, capBind:0, maxShare:0, sv:0}; }
/* PRICE (A2 issuance and price module): null = off (index.html). When an object, runYear() reprices the basket by
 * PRICE.bIdx (the endogenous index, set each year by priceRun from the previous year's flows), reads COLA off the
 * endogenous headline rate, indexes wages to P_G by PRICE.wIdx, and accumulates the year's flows into PRICE.acc.
 * No RNG is drawn; with bIdx = 1 and no accumulation a run is bit-identical (checked by `unit`). */
var PRICE = null;
/* LABOR (A3 labor-supply module, session 4; decisions d14, d15 and d2 on the project dashboard): null = off (index.html).
 * When an object, each agent's wage earnings E0 for the year are replaced by
 *   E = max(0, E0 x raise^eps - rho x cash - rhoBU x BUspent - rhoR x BUexpired - conversion term)
 *  rho     income effect per dollar of unconditional cash (p.ubi). Source: Vivalt et al., NBER w32719 (revised Aug 2026):
 *          $1,000 a month for three years; for every dollar received, individual income excluding the transfer fell about
 *          16 cents and household income about 28 cents. The model's agents are single adults, so 0.16 is central (d15).
 *  rhoBU   income effect per BU spent on the agent's own essentials (engine: the CCO relief dollars; framework: the BU
 *          spent up to the essentials budget). These BU are inframarginal (below own essentials spending), and Hoynes &
 *          Schanzenbach (AEJ Applied 2009) find inframarginal food stamps act like cash, so rhoBU = rho by default. Hastings &
 *          Shapiro (AER 2018) reject fungibility in spending (mental accounting), the case for sweeping rhoBU below rho.
 *  rhoR    income effect per BU that expire unspent (framework: directed to projects). The holder cannot consume them, so 0
 *          by default. d2's "UBI-equivalent toggle" sets rhoBU = rhoR = rho (every BU treated as cash).
 *  eps     compensated (Hicksian) wage elasticity. Chetty (Econometrica 2012): 0.33 on the intensive margin and 0.25 on the
 *          extensive margin, pooled. The program's raises are uncompensated wage increases, so earnings scale by
 *          raise^(eps - rho) (Slutsky: e_u = e_c + eta, with eta = w dh/dI = -rho, the same rho as the income effect), where
 *          raise = wage / wage without the program's raises (octave, CIP; the N7 split) x (1 + the framework's business
 *          payout per wage dollar). One elasticity for every change in the return to work (the plan's fairness rule).
 *  delta   conversion (d14). Conversion proceeds in both models do not depend on effort; the framework says they reward
 *          project work. Last year's creator proceeds C (engine: own conversion; framework: project conversion, not the
 *          wage-linked business payout) enter as  delta x C + rho x (1 - delta) x C : delta = 0 treats C as a rent (an
 *          unconditional dollar, the engine as coded); delta = 1 as fully dissipated project time that displaces wage
 *          time one for one (a fixed BU pool bid for competitively, so a marginal project hour earns the wage).
 * No RNG is drawn. With rho = rhoBU = rhoR = eps = delta = 0 a run is bit-identical to LABOR null (checked by `unit`).
 * LABOR.acc (when an object) tallies each channel in dollars. p.ubi (harness-only): annual cash to every adult, nominal,
 * money-created; counted as cash income in the income and basket measures. Unset in every preset. */
var LABOR = null;
var LABOR_DEFAULTS = {rho:0.16, rhoBU:0.16, rhoR:0, eps:0.33, delta:0};
/* Session 5 restudy switches (harness-only; each off by default, so every shipped figure is bit-identical; checked by `unit`).
 *  THETA_GATE  'szh' = index.html: SZH theta (the PTF conversion bonus add-on, the PTF induction boost and the BLEI term)
 *              is read off the SZH zone-coherence slider. 'density' = the framework's gate (claims ledger C08, dashboard
 *              d12): theta is read off the population's realised PTF share at the start of each year, through the same
 *              szhTheta() curve (55% threshold, full at 90%, cap 0.25). THETA_DENS holds the latest share for agentBLEI().
 *  PTH_MODE    'basket' = index.html: PTH cuts the whole (post-PTF) basket by 35%, which is 127% of MIT's housing
 *              component. 'housing' (d4): PTH cuts the housing component by PTH_HOUSING_CUT (the same 35% rate, applied
 *              to what PTH provides). Under shipped PTF the housing component has already been cut by PTF's rate.
 *  DISC_BASE   'basket' = index.html: PTF, PTH and CCO relief discount the whole basket. 'pretax' (d5): they skip the
 *              basket's income and payroll tax share (17.97% at year-0 prices), which no price cut reduces.
 * With PTH_MODE or DISC_BASE changed, the PTH saving that funds equity routing is PTH's own cut on the agent's post-relief
 * basket (identical to index.html's cf/0.65 formula in the engine model; in the framework model BU purchases are not a
 * price cut, so the saving is PTH's cut before them). BLEI keeps its own daily-cost anchor (dual-anchor table, v4.14),
 * so PTH_MODE and DISC_BASE act on the wealth loop only. */
var THETA_GATE = 'szh', PTH_MODE = 'basket', DISC_BASE = 'basket', THETA_DENS = null, PTH_HOUSING_CUT = 0.35;
function setRestudy(o){ var old = {THETA_GATE:THETA_GATE, PTH_MODE:PTH_MODE, DISC_BASE:DISC_BASE};
  if (o){ if (o.THETA_GATE) THETA_GATE = o.THETA_GATE; if (o.PTH_MODE) PTH_MODE = o.PTH_MODE; if (o.DISC_BASE) DISC_BASE = o.DISC_BASE; }
  return old; }
/* ─── Session 6 (A4): the policy testbed (harness-only; dashboard s11, decisions d24–d29). TB = null (the default) or an unset
 * p.tb leaves every run bit-identical (checked by `unit`). When TB is an object AND p.tb is set, runYear() adds:
 *  - Programs (p.tb): ubi (cash to every adult, year-0 $/yr), xc {amt, delta} (X-Cents adult exchange; delta 1 = the
 *    community-work variant's hours displace wage time one for one, the d14 bracket), nit {G, t} (benefit max(0, G - t x wage
 *    earnings)), groc {cut, cover} (public grocery: a cut on the food component for covered adults), endow {amt, thresh}
 *    (one-time endowment in year 0 to adults whose year-0 wealth is below thresh). Cash amounts follow the same COLA rule as BU
 *    (the preset's cola flag; colaF).
 *  - One income effect for every unconditional dollar (the plan's fairness rule; d25): with LABOR on, earnings fall by rho per
 *    dollar of cash transfer, NIT guarantee (virtual income), endowment annuity value (amt / years), contribution virtual income,
 *    and (TB.inkindRho, default true) every price-cut dollar (PTF, PTH, public grocery) and last year's PTH liquid appreciation.
 *    Session 4's module applied rho to cash and BU only.
 *  - One elasticity for every change in the return to work: earnings scale by (1 - t)^(eps - rho) for adults in the NIT phase-out
 *    and by (1 - tau)^(eps - rho) for adults above the contribution threshold, the same exponent the module applies to raises.
 *  - Financing (TB.fin; d26): 'tax' = a contribution tau on wage earnings above TB.X, set each year to last year's program cost /
 *    last year's base (year 0 from a pre-pass of year 0), capped at tauMax, with the treasury reported; 'money' = the program's
 *    cost is created money, counted in the price module by one rule for every design (d24); 'none' = unfinanced (sessions 2-5).
 *  - A uniform cost ledger (TB.cur, per year) and basket FGT0-2 on income including transfers, less the contribution, plus the
 *    endowment's annuity value, against the agent's own cost (gross basket less in-kind cuts). */
var TB = null;
var TB_DEFAULTS = {fin:'tax', aT:0, eP:0, tauMax:0.9, X:0, inkindRho:true, neutralGate:true};
function tbNewAcc(){ return {pjg:0, n:0, cash:0, endow:0, bu:0, conv:0, cutPT:0, cutG:0, cap:0, pthLiq:0, tax:0, base:0, E:0, f0:0, f1:0, f2:0, idx:1, pd:0, tgt:0, emp:0, hrs:0, bR:0, bP:0,
  bz:0, es:0, n1:0, nP1:0, nN1:0, pyP:0, pyN:0, nWP1:0, esWP:0}; }  /* session 19 (s38): business premium and ESP payroll by group, years 1-19 (reporting only) */
function tbYear(p, colaF){
  var s = p.tb;
  TB.cur = tbNewAcc();
  return {ubi:(s.ubi || 0)*colaF, xc:(s.xc ? s.xc.amt : 0)*colaF, xd:s.xc ? (s.xc.delta || 0) : 0, G:s.nit ? s.nit.G*colaF : 0, t:s.nit ? s.nit.t : 0,
    tau:TB.tau || 0, X:(TB.X || 0)*(TB.xIdx || 1), W:s.endow ? s.endow.amt : 0, T:p.years, gcap:s.groc ? (s.groc.cap || 0) : 0, gcov:s.groc ? s.groc.cover : 0, Gp:!!(s.nit && s.nit.part)};
}
/* d28: the BLEI gate on the engine's wage-growth bonus, read the same way for every design: Baseline rules (gamma 0.12, the base
 * daily cost, no SZH term) plus one month of the design's regular support, BU (the credit agentBLEI gives participants) or cash
 * (UBI, X-Cents, the NIT benefit on last year's earnings). agentBLEI itself, and every BLEI figure reported, are unchanged. */
function tbGate(a, p, buEff, y){
  var Ep = a.yrWageUSD !== undefined ? a.yrWageUSD : a.wage*12*CFG.WAGE_TO_USD, Bx = (y.G > 0 && (!y.Gp || a.inCCO)) ? (y.t > 0 ? Math.max(0, y.G - y.t*Ep) : y.G) : 0;  /* the NIT benefit expected on last year's earnings; session 11: a participant-only top-up (Gp) reaches participants only */
  var m = (y.ubi + y.xc + Bx)/12;
  if (p.ccoOn && a.inCCO && buEff > 0) m += (CONVERSION_MODEL === 'framework' && a._fwBUm !== undefined) ? a._fwBUm : buEff*(990/1200);
  a._tbM = m;  /* session 7: kept for the design-neutral BLEI poverty figure (d28) */
  return agentBLEI(a, 0, false, false, false, 0, false) + m/CFG.BASE_DAILY_COST;
}
function tbNitElig(y, E0){ return y.G > 0 && (y.t <= 0 || E0 < y.G/y.t); }
/* Labor terms for one agent-year: F multiplies earnings (net-of-rate factors), V is extra unconditional dollars (x rho), D is
 * time displaced from wage work. Eligibility for the phase-out and the contribution is read on earnings before the response. */
function tbLab(a, y, E0, cutUSD){
  var ex = LABOR.eps - LABOR.rho, F = 1, el = tbNitElig(y, E0) && (!y.Gp || a.inCCO), tx = y.tau > 0 && E0 > y.X;
  var V = y.ubi + y.xc*(1 - y.xd) + (el ? y.G : 0), D = y.xc*y.xd;  /* cash first, so an NIT at t = 0 is bit-identical to a UBI */
  if (a._tbEl) V += y.W/y.T;
  if (tx){ F *= Math.pow(1 - y.tau, ex); V += y.tau*y.X; }
  if (el) F *= Math.pow(1 - y.t, ex);
  if (TB.inkindRho) V += cutUSD + (a._tbPthPrev || 0);
  return {F:F, V:V, D:D};
}
function tbCashFlow(a, y, E, yr){
  var B = (y.G > 0 && (!y.Gp || a.inCCO)) ? (y.t > 0 ? Math.max(0, y.G - y.t*E) : y.G) : 0, cash = y.ubi + y.xc + B, tax = y.tau > 0 ? y.tau*Math.max(0, E - y.X) : 0;
  a.yrTbCash = cash; a.yrTax = tax; a._tbNit = B;
  return {net:cash - tax, endow:(yr === 0 && a._tbEl) ? y.W : 0};
}
function tbAccount(a, y, yr, mlc, cf, cfPreCCO, costUSD, E, tbG, tbPT){
  var C = TB.cur, idx = mlc/CFG.LIVING_WAGE_ANNUAL, conv = +a.yrConvUSD || 0;
  TB.xIdx = idx;  /* d26: the contribution threshold X is in year-0 dollars, indexed to the basket with a one-year lag */
  C.n++; C.idx = idx; C.E += E; C.cash += a.yrTbCash; C.tax += a.yrTax; C.base += Math.max(0, E - y.X);
  if (yr === 0 && a._tbEl) C.endow += y.W;
  var buR = Math.max(0, mlc*(cfPreCCO - cf) - tbG);
  C.bu += buR; C.conv += conv; C.pjg += a.yrPjGift || 0; a.yrPjGift = 0; C.cutPT += tbPT; C.cutG += tbG; C.pthLiq += a._tbPthNow || 0;
  /* Session 7 (A5 targeting share): program dollars this agent received this year (cash, the endowment's annuity value, BU relief,
   * conversion, price-cut dollars, PTH liquid appreciation; not capital), and the part that closes the agent's shortfall before
   * transfers: the gross basket less wage earnings. Reporting only. */
  var pd = a.yrTbCash + (a._tbEl ? y.W/y.T : 0) + buR + conv + tbPT + tbG + (a._tbPthNow || 0);
  C.pd += pd; C.tgt += Math.min(pd, Math.max(0, mlc - E));
  if (y.gcap && a._tbU < y.gcov) C.cap += y.gcap*idx;
  var inc = E + conv + (a.yrUbiUSD || 0) + a.yrTbCash - a.yrTax + (a._tbEl ? y.W/y.T : 0), g = Math.max(0, costUSD - inc)/mlc;
  C.f0 += g > 0 ? 1 : 0; C.f1 += g; C.f2 += g*g;
  a._tbGap = g; a._tbF0 = (a._tbF0 || 0) + (g > 0 ? 1 : 0); a._tbRes = (a._tbRes || 0) + (inc + mlc - costUSD)/idx; a._tbYrs = (a._tbYrs || 0) + 1;
  /* Session 8 (A5; dashboard s18). Reporting only, no RNG. Spells: a spell starts in any year the agent is below the basket after
   * being above it (or in year 0); spells are censored at the 20-year window. Hours: this year's earnings over the same agent's
   * earnings with no labor response (a._lbE0, set in runYear's LABOR block), which is hours at a fixed wage; 1 with LABOR off.
   * Disposable income, OECD definition (the Hub's C30): wage earnings + conversion proceeds + cash transfers - the contribution;
   * no in-kind benefits, no capital transfer (the endowment), no capital gains (PTH appreciation). Extended income adds the in-kind
   * cuts to the agent's basket (BU relief and PTF, PTH and grocery price cuts). */
  if (g > 0){ if (!a._tbInSp) a._tbSp = (a._tbSp || 0) + 1; a._tbInSp = true; } else a._tbInSp = false;
  C.emp += E > 0 ? 1 : 0; C.hrs += a._lbE0 > 0 ? (a._pjHW ? E + a._pjHW : E)/a._lbE0 : 1;  /* N1 (session 15): + project hours at the worker's own wage */
  C.bR += a._bleiR || 0; C.bP += a._bleiP || 0;  /* session 9 (i3-2): BLEI raises, and those the program's support carried over the gate */
  /* Session 19 (s38): the framework model's business premium as received, the ESP's own payout and ESP payroll, by group, over the years it
   * is paid (1 to 19; year 0 pays none). Reporting only, no RNG; zero in the engine model. */
  if (yr > 0){ var bzY = a._fwPayY || 0, esY = a._esPrY || 0; C.n1++; C.bz += bzY; C.es += esY;
    if (a.inCCO){ C.nP1++; C.pyP += bzY + esY; if (a._esWk){ C.nWP1++; C.esWP += esY; } } else { C.nN1++; C.pyN += bzY; } }
  a._tbDisp = E + conv + (a.yrUbiUSD || 0) + a.yrTbCash - a.yrTax; a._tbExt = a._tbDisp + Math.max(0, mlc - costUSD);
  a._tbPthPrev = a._tbPthNow || 0; a._tbPthNow = 0;
}
function mulberry32(seed){var s=seed>>>0;return function(){s=(s+0x6D2B79F5)>>>0;var t=Math.imul(s^(s>>>15),1|s);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}

function lognormal(mu,sigma){var u=Math.max(1e-14,1-RNG()),v=RNG();return Math.exp(mu+sigma*Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v));}
function beta(a,b){var x=gamma(a);return x/(x+gamma(b));}
function gamma(a){if(a===1)return -Math.log(Math.max(1e-14,RNG()));if(a<1)return gamma(1+a)*Math.pow(Math.max(1e-14,RNG()),1/a);for(var i=0;i<5000;i++){var u=RNG(),v=RNG(),y=Math.tan(Math.PI*u),x=Math.sqrt(2*a-1)*y+a-1;if(x>0&&v<=(1+y*y)*Math.exp((a-1)*Math.log(x/(a-1))-Math.sqrt(2*a-1)*y))return x;}return a;}
function standardNormal(){var u=Math.max(1e-14,1-RNG()),v=RNG();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
function drawAutomationRisk(){
  if(AUTOMATION_SAMPLER_LEGACY){
    if(RNG()<CFG.AUTO_HIGH_SHARE)return beta(6,1);
    return beta(1,6);
  }
  var c=RNG(),v=RNG();
  return c<CFG.AUTO_HIGH_SHARE?Math.pow(v,1/CFG.AUTO_HIGH_A):1-Math.pow(1-v,1/CFG.AUTO_LOW_B);
}

function makeLatentAgent(){
  var uCCO=RNG(),uPTF=RNG(),uPTH=RNG();
  return{uCCO:uCCO,uPTF:uPTF,uPTH:uPTH,
    wealth:lognormal(CFG.WEALTH_INIT_MU,CFG.WEALTH_INIT_SIGMA),wage:lognormal(3.5,0.5),
    octaveShape:beta(2,5),qualityZ:standardNormal(),
    automationRisk:drawAutomationRisk(),lambda:CFG.FBS_LAMBDA_LO+RNG()*(CFG.FBS_LAMBDA_HI-CFG.FBS_LAMBDA_LO)};
}
function makeLatentPopulation(n){var pop=[];for(var i=0;i<n;i++)pop.push(makeLatentAgent());return pop;}
function instantiateAgent(latent,cfgP){
  var qN=cfgP.cip?(1-cfgP.cipDemo*0.5):1.0;
  var maxOct=cfgP.maxOct||1,maxMult=cfgP.maxMult||1;
  var inPTH=!!(cfgP.pth&&latent.uPTH<cfgP.pthUptake);
  return{wealth:latent.wealth,wage:latent.wage,
    initialWage:latent.wage,
    octave:Math.floor(latent.octaveShape*maxOct),
    quality:Math.min(maxMult,Math.max(0,Math.exp(Math.log(maxMult*0.5)+0.4*latent.qualityZ)*qN)),
    automationRisk:latent.automationRisk,lambda:latent.lambda,
    uCCO:latent.uCCO,  // v4.19: kept for deterministic emergency take-up (no RNG)
    inCCO:!!(cfgP.ccoOn&&latent.uCCO<cfgP.partRate),inPTF:!!(cfgP.ptf&&latent.uPTF<cfgP.ptfShare),inPTH:inPTH,
    buBalance:0,acreEquity:inPTH?5000:0,
    pthTenure:0};
}

function szhTheta(coh){
  coh=isNaN(coh)?0:coh;
  if(coh<CFG.SZH_THETA_THRESHOLD)return 0;
  return Math.min(CFG.SZH_THETA_MAX,(coh-CFG.SZH_THETA_THRESHOLD)/(CFG.SZH_THETA_MAX_COH-CFG.SZH_THETA_THRESHOLD)*CFG.SZH_THETA_MAX);
}
function pthLiquidShare(tenure){
  var t=Math.max(1,Math.min(CFG.PTH_LIQUID_SHARE_MATURE_YR,isNaN(tenure)?1:tenure));
  var span=CFG.PTH_LIQUID_SHARE_MATURE_YR-1;
  return span>0?CFG.PTH_LIQUID_SHARE_YEAR1+(t-1)/span*(CFG.PTH_LIQUID_SHARE_YEAR5PLUS-CFG.PTH_LIQUID_SHARE_YEAR1):CFG.PTH_LIQUID_SHARE_YEAR1;
}

var TIERS=[{name:'Crisis',num:0},{name:'Precarious',num:1},{name:'Threshold',num:2},{name:'Stable',num:3},{name:'Secure',num:4},{name:'Flourishing',num:5}];
function getTier(days,top){top=top||'Flourishing';if(days<CFG.BLEI_CRISIS_MAX)return TIERS[0];if(days<CFG.BLEI_PRECARIOUS_MAX)return TIERS[1];if(days<CFG.BLEI_THRESHOLD_MAX)return TIERS[2];if(days<CFG.BLEI_STABLE_MAX)return TIERS[3];if(days<CFG.BLEI_SECURE_MAX)return TIERS[4];return top==='Comfortable'?{name:'Comfortable',num:5}:TIERS[5];}

function agentBLEI(a,buAlloc,ccoOn,pthOn,szhOn,szhCoh,ptfOn){
  var liquid=Math.max(0,(isNaN(a.wealth)?0:a.wealth)*0.20);
  var gammaV=(ccoOn&&a.inCCO)?0.20:0.12;
  var mInc=Math.max(isNaN(a.wage)?1:a.wage,0.1)*CFG.WAGE_TO_USD;
  var buFood=(ccoOn&&a.inCCO&&buAlloc>0)?((CONVERSION_MODEL==='framework'&&a._fwBUm!==undefined)?a._fwBUm:buAlloc*(990/1200)):0;  // session 2, N3: framework credits one month of the BU actually spent on essentials
  var szhD=szhOn?szhCoh*CFG.SZH_ALL_RESIDENTS:0;
  if(szhOn&&ptfOn&&a.inPTF)szhD+=szhTheta(THETA_GATE==='density'&&THETA_DENS!==null?THETA_DENS:szhCoh)*0.20;  // session 5 (C08): harness-only gate
  var baseCost=(ccoOn&&a.inCCO&&pthOn&&a.inPTH)?CFG.CCO_PTH_DAILY_COST:CFG.BASE_DAILY_COST;
  var dc=Math.max(baseCost*(1-szhD),0.1);
  var r=(liquid+gammaV*mInc+buFood)/dc;
  return(isNaN(r)||!isFinite(r))?0:Math.max(0,r);
}
function agentEDC(a,ccoOn,pthOn){
  var mInc=Math.max(isNaN(a.wage)?1:a.wage,1);
  var w=CFG.WAGE_MEDIAN_SIU;
  if(ccoOn&&a.inCCO&&pthOn&&a.inPTH)return Math.min(CFG.EDC_PTH_CAP,(CFG.EDC_PTH_CAP*w)/mInc);
  if(!ccoOn||!a.inCCO)return Math.min(0.75,Math.min(0.50,(0.50*w)/mInc)+0.08);
  return Math.min(0.42,Math.min(0.35,(0.35*w)/mInc)+0.03);
}
function bleiMetrics(agents,buAlloc,ccoOn,pthOn,szhOn,szhCoh,ptfOn,top){
  top=top||'Flourishing';
  var sc=agents.map(function(a){return agentBLEI(a,buAlloc,ccoOn,pthOn,szhOn,szhCoh,ptfOn);});
  sc.sort(function(a,b){return a-b;});
  var n=sc.length,med=n%2===0?(sc[n/2-1]+sc[n/2])/2:sc[Math.floor(n/2)];
  var tc=[0,0,0,0,0,0];sc.forEach(function(d){tc[getTier(d,top).num]++;});
  var sumEDC=agents.reduce(function(s,a){return s+agentEDC(a,ccoOn,pthOn);},0);
  return{med:med,pctF:tc[5]/n*100,avgEDC:sumEDC/n,tc:tc,n:n};
}

function runYear(agentSet,yr,p,recSt){
  var totalBU=0,totalConversion=0;recSt=recSt||{active:false,incomeMultiplier:1.0,yearsLeft:0};
  var pthApprBonus=p.szh?p.szhCoh*0.01:0;
  var szhThetaVal=p.szh?szhTheta(p.szhCoh):0;
  if(THETA_GATE==='density'){var tdN=0;if(p.ptf)agentSet.forEach(function(a){if(a.inPTF)tdN++;});THETA_DENS=tdN/Math.max(1,agentSet.length);szhThetaVal=p.szh?szhTheta(THETA_DENS):0;}  // session 5 (C08/d12): harness-only
  var ptfConvBonus=1.30+((p.szh&&p.ptf)?szhThetaVal:0);
  var szhPartBoost=(p.szh&&p.ccoOn)?szhThetaVal*0.16:0;
  /* v4.14 parity fix — ported from index.html: PTF's inflation-damping term used to read
   * the static initial-share slider (p.ptfShare) rather than the population's actual
   * current PTF membership, which this same function already computes a few lines later
   * (for the Bass-diffusion adoption term) but never reused here. ptfAdoptFrac is moved up
   * and reused for both purposes — it draws no RNG, so this reordering shifts no draw
   * anywhere in the function. Verified inert on the documented seed-42/Full Integration
   * regression (inflRate=0 there, so the guard never fires); see CONTRIBUTING.md's v4.14
   * Release Notes for the full trail and measured effect size on configs it does touch. */
  var ptfAdoptFrac=0;
  if(p.ptf&&p.ptfShare>0){var ptfCount0=0;agentSet.forEach(function(a){if(a.inPTF)ptfCount0++;});ptfAdoptFrac=ptfCount0/Math.max(1,agentSet.length);}
  /* v4.15 parity fix — ported from index.html: PTH's inflation damping used to be the flat,
   * toggle-triggered `inflRate*=0.90` below — the same defect class the v4.14 PTF fix closed
   * one line above it, in a coarser form (it referenced no adoption-scale quantity at all,
   * so 5% PTH uptake got the identical 10% population-wide reduction as 50%). Unlike PTF,
   * PTH membership is drawn once at construction and never changes during a run, so
   * pthMemberFrac is simply the population's fixed realised PTH share — counted the same
   * no-RNG way as ptfAdoptFrac (existing a.inPTH flags only), so no draw shifts anywhere.
   * Verified inert on the documented seed-42/Full Integration regression (inflRate=0 there)
   * and on Baseline (pth=false); see CONTRIBUTING.md's v4.15 Release Notes. */
  var pthMemberFrac=0;
  if(p.pth){var pthCount0=0;agentSet.forEach(function(a){if(a.inPTH)pthCount0++;});pthMemberFrac=pthCount0/Math.max(1,agentSet.length);}
  var inflRate=p.inflRate||0;
  if(p.ptf&&inflRate>0&&!(PRICE&&PRICE.noDamp))inflRate*=(1-ptfAdoptFrac*0.5);  // session 2: PRICE.noDamp (price module only)
  /* v4.15: (1-pthMemberFrac*0.10) replaces the flat *0.90. The 0.10 coefficient (=1-0.90) is
   * unchanged from the historical value and is now the ceiling reached at 100% membership. */
  if(p.pth&&inflRate>0&&!(PRICE&&PRICE.noDamp))inflRate*=(1-pthMemberFrac*0.10);
  var dollarCost=CFG.BASE_DAILY_COST*365*Math.pow(1+inflRate,yr);
  if(PRICE)dollarCost*=PRICE.bIdx;  // session 2: endogenous basket index (price module only)
  var popShock=recSt.active?recSt.incomeMultiplier:1.0;
  var ptfLiveCount=0,ptfLiveTotal=agentSet.length;
  if(p.ptf&&p.ptfCap){agentSet.forEach(function(a){if(a.inPTF)ptfLiveCount++;});}
  function ptfCapAllows(){return !p.ptfCap||ptfLiveCount<ptfLiveTotal*p.ptfShare;}
  var popAIDisp=0;
  if(p.automation){
    if(yr>=CFG.AI_DISPLACEMENT_YEAR_2)popAIDisp=CFG.AI_DISPLACEMENT_RATE_1*(CFG.AI_DISPLACEMENT_YEAR_2-CFG.AI_DISPLACEMENT_YEAR_1)+CFG.AI_DISPLACEMENT_RATE_2*(yr-CFG.AI_DISPLACEMENT_YEAR_2+1);
    else if(yr>=CFG.AI_DISPLACEMENT_YEAR_1)popAIDisp=CFG.AI_DISPLACEMENT_RATE_1*(yr-CFG.AI_DISPLACEMENT_YEAR_1+1);
    popAIDisp=Math.min(0.10,popAIDisp);
  }
  /* v4.19: automatic stabilizers (Research Hub Integrated Implementation Roadmap, Appendix G).
   * All off by default: with p.stab and p.cola unset, buEff===p.bu exactly (a multiply by 1),
   * emergLine is -1 and decay is untouched, so every documented figure is bit-identical.
   *  - Recession trigger: the year's recession is active and its population income loss
   *    (1 - incomeMultiplier) is at least p.stabThresh. The engine has no GDP or unemployment
   *    rate, so the hub's ">2% GDP decline" is read as a >=2% income loss; every engine
   *    recession (5-30%) clears it. The trigger reads the CURRENT year's shock (a timely
   *    trigger); harness.js measures what a one-year data lag costs.
   *  - Increase: fixed multiplier p.stabMult, or scaled 1 + p.stabK x loss (p.stabSev).
   *  - COLA: BU indexed by the same cost index mainLoopCostUSD uses, (1+inflRate)^yr, when the
   *    headline rate p.inflRate is above p.colaThresh (Inflation Surge Protocol: 5%).
   *    Inflation is a constant input rate here, so the threshold acts for the whole run.
   *  - buEff replaces p.bu at every read below: allocation, the 3x cap, FBS, and the BLEI
   *    check that gates the wage-growth bonus.
   *  - Suspended expiry (p.stabSusp, hub Natural Disaster Response): unspent BU carries over
   *    while triggered, up to the 3x cap.
   *  - Emergency enrollment (p.emerg, hub "relax requirements"): while triggered, a
   *    non-participant whose latent CCO uniform lies in [partRate, partRate + take-up x
   *    (1 - partRate)) gets the CCO cost relief for that year only. Deterministic: it reads
   *    a.uCCO, drawn at construction, so no RNG draw is added and CRN pairing holds.
   *    Enrollees do not enter octave advancement or conversion.
   * No RNG is drawn here. */
  var stabLoss=recSt.active?Math.max(0,1-recSt.incomeMultiplier):0;
  var stabOn=!!(p.stab&&p.ccoOn&&recSt.active&&stabLoss>=(p.stabThresh||0));
  var stabM=stabOn?(p.stabSev?1+Math.max(0,p.stabK||0)*stabLoss:Math.max(1,p.stabMult||1)):1;
  var colaF=(p.cola&&(p.inflRate||0)>(p.colaThresh||0))?Math.pow(1+inflRate,yr):1;
  /* Session 2, price module only: COLA reads the headline rate, exogenous plus endogenous, year by year, and ratchets BU
   * up to the full price index in any year that rate exceeds p.colaThresh (Inflation Surge Protocol, 5% in D6). */
  if(PRICE){var pmFull=Math.pow(1+inflRate,yr)*PRICE.bIdx;if(p.cola&&pmFull/PRICE.lastFull-1>(p.colaThresh||0))PRICE.colaLevel=pmFull;PRICE.lastFull=pmFull;colaF=p.cola?PRICE.colaLevel:1;}
  var buEff=p.bu*stabM*colaF;
  var tbY=(TB&&p.tb)?tbYear(p,colaF):null;  // session 6 (A4 testbed): null unless TB and p.tb are both set (harness-only; no RNG)
  var emergLine=(stabOn&&p.emerg)?p.partRate+Math.max(0,Math.min(1,p.emergTakeup||0))*(1-p.partRate):-1;
  var emergN=0;
  /* v4.19, Duke's decision (Option B): CCO's cost relief scales with the effective BU. Through
   * v4.18 it was a flat 0.80 whenever BU > 0, so the BU amount reached a household only through
   * conversion proceeds, credited once a year. BU is "redeemable at PTF businesses for essential
   * goods" (Research Hub glossary), so the amount now moves the relief directly: 20% of the
   * basket at the $1,200 reference, in proportion above and below it, capped at 50%. At $1,200
   * this is exactly 0.80, so every $1,200 preset and the seed-42 regression are bit-identical;
   * Stress Test ($900) and any run at another BU amount move. The 50% cap is a placeholder. */
  /* v4.21 units fix, ported from index.html (see its comment): the relief share reads BU in
   * year-0 dollars, buEff / priceIdx. RELIEF_PRICE_LEGACY (harness-only) restores v4.19-v4.20. */
  var priceIdx=RELIEF_PRICE_LEGACY?1:Math.pow(1+inflRate,yr);
  if(PRICE&&!RELIEF_PRICE_LEGACY)priceIdx*=PRICE.bIdx;  // session 2: BU erodes with the endogenous index too
  var ccoReliefF=CCO_RELIEF_FLAT?0.80:1-Math.min(CFG.CCO_RELIEF_CAP,CFG.CCO_RELIEF_AT_REF*buEff/(CFG.CCO_RELIEF_REF_BU*priceIdx));
  if(LEDGER){LEDGER.idx=Math.pow(1+inflRate,yr);var LY0=LEDGER.y[yr]||(LEDGER.y[yr]={});LY0.pIdx=LEDGER.idx;}  // A1 ledger (reporting only): this year's price index, the one mainLoopCostUSD uses
  /* Session 2: framework conversion state (N1-N4) and the basket's current essentials and food shares (price module). */
  var FWON=CONVERSION_MODEL==='framework';
  if(FWON){if(yr===0||!FWS)FWS={prev:null};FWS.next={bizBU:0,projBU:0,expiredBU:0,destroyedBU:0,wSum:0,pwSum:0,projAlloc:0,projGross:0,projTax:0,projNet:0,projLost:0,bizPaid:0};}
  var PJON=!!PROJ,pjPay=0,pjIdx=1,pjCipB=1,pjFg=0;  /* N1 (session 15): project hiring; see PROJ. No RNG is drawn in any PROJ step. */
  if(PJON){
    if(yr===0||!PJS)PJS={prev:null,acc:pjNewAcc()};PJS.next={pool:0,gpool:0};  // gpool: the launch gift's share, tracked for financing (d66)
    pjIdx=Math.pow(1+inflRate,yr)*(PRICE?PRICE.bIdx:1);pjPay=PROJ.pay*pjIdx;pjCipB=p.cip?(1+p.cipDemo*0.12):1.0;
    var pjP=[],pjWt=0,pjWR=0,pjIn=PJS.prev?PJS.prev.pool+PJS.prev.gpool:0,pjCarry=0;pjFg=pjIn>0?PJS.prev.gpool/pjIn:0;
    if(p.ccoOn)agentSet.forEach(function(a){if(!a.inCCO)return;var r=pjOwnRate(a,p,ptfConvBonus),cap=12*FW.octaveCapBase*Math.pow(2,a.octave),w=cap*Math.max(0,a.quality);
      a._pjR=r;a._pjCap=cap;a._pjW=w;a._pjBU=0;pjWt+=w;pjWR+=w*r;pjP.push(a);});
    var pjRc=pjWt>0?pjWR/pjWt:1,pjSet=[];PJS.acc.rc+=pjRc;PJS.acc.rcN++;
    pjP.forEach(function(a){var ru=PROJ.rate==='max'?Math.max(a._pjR,pjRc):a._pjR,v=pjPay*ru*(1-pjTax(p,ru))*pjCipB,h=a.wage*12*CFG.WAGE_TO_USD/PROJ.hrsYr;
      a._pjRu=ru;a._pjWill=v>h;if(PROJ.alloc==='capqAll'||a._pjWill)pjSet.push(a);});
    if(pjIn>0&&pjSet.length){
      if(PROJ.alloc==='low'){pjSet.sort(function(x,y){return x.wage-y.wage;});var pjL=pjIn;for(var pjI=0;pjI<pjSet.length&&pjL>0;pjI++){var pjT=Math.min(pjL,pjSet[pjI]._pjCap);pjSet[pjI]._pjBU=pjT;pjL-=pjT;}pjCarry=pjL;}
      else if(PROJ.alloc==='equal'){pjSet.forEach(function(a){a._pjBU=pjIn/pjSet.length;});}
      else{var pjS=0;pjSet.forEach(function(a){pjS+=a._pjW;});if(pjS>0)pjSet.forEach(function(a){a._pjBU=pjIn*a._pjW/pjS;});else pjCarry=pjIn;}
    } else pjCarry=pjIn;
    pjP.forEach(function(a){if(a._pjBU>0){PJS.acc.alloc+=a._pjBU/pjIdx;PJS.acc.work++;if(!a._pjWill)PJS.acc.unwilling++;}});
    PJS.acc.carry=pjCarry/pjIdx;PJS.next.pool+=pjCarry*(1-pjFg);PJS.next.gpool+=pjCarry*pjFg;PJS.acc.partY+=pjP.length;
    if(yr===0&&PROJ.giftMode==='forward'&&PROJ.gift>0){PJS.next.gpool+=PROJ.gift*pjP.length;PJS.acc.gift+=PROJ.gift*pjP.length;PJS.acc.pool+=PROJ.gift*pjP.length;}
    if(yr===1&&PROJ.giftMode==='holder'&&PROJ.gift>0)pjP.forEach(function(a){a._pjGiftH=(a._pjGiftH||0)+PROJ.gift;PJS.acc.gift+=PROJ.gift;});
  }
  var ESON=FWON&&!!ESP,esIdx=1,esCipB=1;  /* N1 (session 19, s38): ESP payroll. Framework model only; no RNG is drawn in any ESP step. */
  if(ESON){
    if(yr===0||!ESS)ESS={prev:null,acc:esNewAcc(),y:[]};
    esIdx=Math.pow(1+inflRate,yr)*(PRICE?PRICE.bIdx:1);esCipB=p.cip?(1+p.cipDemo*0.12):1.0;
    var esA=ESS.acc,esPool=ESS.prev?ESS.prev.pool:0,esW=0,esRet=0,esSv=0,esY=ESS.y[yr]={pool:esPool,conv:0,ret:0,sv:0};
    agentSet.forEach(function(a,i){
      if(a._esU===undefined)a._esU=((i+1)*ESP_GOLD)%1;  // d72: fixed by agent index
      a._esWk=ESP.work==='all'?true:ESP.work==='ptf'?!!(p.ptf&&a.inPTF):a._esU<ESP.work;
      a._esBU=0;a._esC=0;a._esX=0;a._esR=0;
      if(a._esWk)esW+=Math.max(0,a._fwW||0);
    });
    ESS.wW=esW;esA.poolPaid+=esPool/esIdx;
    agentSet.forEach(function(a){
      if(!a._esWk&&!(a._esSv>0))return;
      var w=Math.max(0,a._fwW||0),sh=0,bu=0;
      if(a._esWk){esA.wkY++;if(yr>0){esA.wkY1++;esA.wage+=w/esIdx;}
        if(esPool>0&&esW>0){sh=esPool*w/esW;bu=Math.min(sh,w);if(sh>bu){esRet+=sh-bu;esA.retWage+=(sh-bu)/esIdx;}if(w>0)esA.maxShare=Math.max(esA.maxShare,bu/w);}
        a._esBU=bu;esA.alloc+=bu/esIdx;}
      if(!(p.ccoOn&&a.inCCO)){esRet+=bu;esA.retNon+=bu/esIdx;return;}  // d73: non-participants have no earned rate; paid in dollars
      if(a._esWk)esA.partWkY++;
      var r=pjOwnRate(a,p,ptfConvBonus),tx=pjTax(p,r),ok=ESP.take==='biz'?r>FW.bizRate:r*(1-tx)*esCipB>1;
      if(!ok){esRet+=bu;esA.retPar+=bu/esIdx;return;}  // below par (or below the ESP's rate, 'biz'): paid in dollars
      var have=bu+(ESP.cap==='save'?(a._esSv||0):0);
      var cap=ESP.cap==='none'?Infinity:Math.max(0,12*FW.octaveCapBase*Math.pow(2,a.octave)-(PJON?(a._pjBU||0)+(a._pjSaved||0):0));  // d74: net of project BU
      var c=Math.min(have,cap);a._esK=cap;  // _esK: reporting only (the capacity test)
      if(have>c+1e-9){esA.capBind++;if(ESP.cap==='save')a._esSv=have-c;else{esRet+=have-c;esA.retCap+=(have-c)/esIdx;}}
      else if(ESP.cap==='save')a._esSv=0;
      if(c>0){a._esC=c;a._esR=r;a._esX=w>0?c*(r*(1-tx)*esCipB-1)/w:0;esA.tk++;}  // the payroll raise for the labor module (before the income shock)
    });
    if(ESP.cap==='save')agentSet.forEach(function(a){esSv+=a._esSv||0;});
    esY.ret=esRet;esY.sv=esSv;esA.ret+=esRet/esIdx;esA.sv=esSv/esIdx;
    agentSet.forEach(function(a){esY.conv+=a._esC;});
    if(esRet>0&&FWS.prev){  // d73-d75: the BU returned to the ESP convert at FW.bizRate this year, paid with the rest of last year's premium
      var esBT=p.cip?p.tax*(1-p.cipDemo*0.18):p.tax,esTR=Math.min(CFG.PROG_TAX_MAX,esBT+Math.max(0,(FW.bizRate-CFG.PROG_PIVOT)*CFG.PROG_RATE)),esTP=Math.min(CFG.PROG_TAX_MAX,esBT);
      var esRG=esRet*(FW.bizCap*FW.bizRate+(1-FW.bizCap)),esRT=esRet*(FW.bizCap*FW.bizRate*esTR+(1-FW.bizCap)*esTP),esRN=PATHWAY_OFF.conversion?0:esRG-esRT-esRet;
      FWS.prev.bizNet+=esRN;esA.retNet+=esRN/esIdx;
      if(LEDGER){ledAdd(yr,'espRetGross',esRG);ledAdd(yr,'espRetTax',esRT);ledAdd(yr,'espRetPremium',esRN);}
    }
    if(LEDGER){ledAdd(yr,'espPoolPaid',esPool);ledAdd(yr,'espConvBU',esY.conv);ledAdd(yr,'espRetBU',esRet);}
  }
  var eShareCur=0,fShareCur=CFG.BASKET.food;CFG.ESSENTIALS.forEach(function(k){eShareCur+=CFG.BASKET[k]*(PRICE?PRICE.comp[k]:1);});
  if(PRICE){eShareCur/=PRICE.bIdx;fShareCur=CFG.BASKET.food*PRICE.comp.food/PRICE.bIdx;}
  var rsAlt=PTH_MODE!=='basket'||DISC_BASE!=='basket';  // session 5 (d4/d5): harness-only
  var tShareCur=DISC_BASE==='pretax'?CFG.BASKET.taxes*(PRICE?PRICE.comp.taxes/PRICE.bIdx:1):0,hShareCur=CFG.BASKET.housing*(PRICE?PRICE.comp.housing/PRICE.bIdx:1);
  function discMul(c,m){return DISC_BASE==='pretax'?tShareCur+(c-tShareCur)*m:c*m;}
  agentSet.forEach(function(a){
    if(isNaN(a.wealth))a.wealth=0;if(isNaN(a.wage)||a.wage<=0)a.wage=1;
    a.yrWealthStartUSD=a.wealth;  /* v4.18 parity: start-of-year wealth for housingDistressOf() (no RNG) */
    var agentVar=0.90+RNG()*0.20,incomeShock=popShock*agentVar;
    var uSpendFrac=0.60+RNG()*0.30;
    var uCipQuality=RNG();
    var uAdvance=RNG();
    var uSzhInduce=RNG();
    var uSzhPtfShare=RNG();
    var uPthAppr=RNG();
    var uPtfAdopt=RNG();
    var bleiCheck=agentBLEI(a,buEff,p.ccoOn,p.pth,p.szh,p.szhCoh,p.ptf);
    var tbNB=tbY?tbGate(a,p,buEff,tbY):0,wg=CFG.WAGE_BASE_GROWTH,bleiGate=(tbY&&TB.neutralGate)?tbNB:bleiCheck;  // session 6 (d28): design-neutral gate for the wage bonus (testbed only)
    var bleiProg=0;a._bleiR=0;a._bleiP=0;  // session 9 (i3-2): harness-only attribution of the BLEI raise (no RNG)
    if(bleiGate>CFG.BLEI_PRECARIOUS_MAX&&!PATHWAY_OFF.bleiWage){  // v4.21: harness-only pathway switch
      var drFactor=1/(1+0.5*Math.max(0,a.wage/CFG.WAGE_MEDIAN_SIU-1));
      wg+=CFG.WAGE_BLEI_BONUS*Math.max(0.1,drFactor);
      a._bleiR=1;if(!(agentBLEI(a,0,false,false,false,0,false)>CFG.BLEI_PRECARIOUS_MAX)){a._bleiP=1;if(N7_BLEI)bleiProg=CFG.WAGE_BLEI_BONUS*Math.max(0.1,drFactor);}
    }
    if(!PATHWAY_OFF.octaveWage)wg+=a.octave*CFG.WAGE_OCTAVE_BONUS;  // v4.21: harness-only pathway switch
    if(p.cip)wg+=p.cipDemo*0.005;
    if(LABOR&&a._lwNB===undefined)a._lwNB=a.wage;  // session 4 (A3): the wage without program-induced raises
    if(PRICE){if(a._wNB===undefined)a._wNB=a.wage;if(PRICE.wIdx)wg+=PRICE.wIdx*PRICE.piG;}  // session 2: wage indexation to P_G (price module; 0 = nominal drift)
    wg-=popAIDisp*((typeof a.automationRisk==='number'&&!isNaN(a.automationRisk))?a.automationRisk:0.5);  /* v4.17 parity: `||0.5` read a draw of exactly 0 as 0.5 */
    a.wage=Math.max(a.wage*0.80,a.wage*(1+wg));
    if(isNaN(a.wage))a.wage=1;
    if(LABOR){var lbProg=(PATHWAY_OFF.octaveWage?0:a.octave*CFG.WAGE_OCTAVE_BONUS)+(p.cip?p.cipDemo*0.005:0)+bleiProg;a._lwNB=Math.max(a._lwNB*0.80,a._lwNB*(1+wg-lbProg));}
    if(PRICE){var pmProg=(PATHWAY_OFF.octaveWage?0:a.octave*CFG.WAGE_OCTAVE_BONUS)+(p.cip?p.cipDemo*0.005:0)+bleiProg;a._wNB=Math.max(a._wNB*0.80,a._wNB*(1+wg-pmProg));}  // N7: the wage without program-induced raises
    var cf=1.0,rsPtfU=1,rsRel=1;
    if(!rsAlt){
    if(p.ptf&&a.inPTF){if(PTF_MODE==='shipped')cf*=(1-(p.szh?0.12+p.szhCoh*0.04:0.12));else cf*=(1-PTF_FOOD_CUT[PTF_MODE]*fShareCur);}  // session 2: PTF_MODE (D4); 'shipped' is index.html
    var cfPTF=cf;  // A1 ledger (reporting only)
    if(p.pth&&a.inPTH&&!PATHWAY_OFF.pthCost)cf*=0.65;  // v4.21: harness-only pathway switch
    var cfPreCCO=cf;  // A1 ledger (reporting only)
    if(p.ccoOn&&a.inCCO&&p.bu>0){if(!PATHWAY_OFF.relief&&!FWON)cf*=ccoReliefF;}  // v4.19: was a flat 0.80 (see ccoReliefF). v4.21: pathway switch
    else if(emergLine>=0&&p.ccoOn&&p.bu>0&&!a.inCCO&&typeof a.uCCO==='number'&&a.uCCO<emergLine){cf*=ccoReliefF;emergN++;}  // v4.19: emergency enrollment
    } else {  // session 5 (d4/d5): the same chain with PTH_MODE and DISC_BASE (harness-only)
    if(p.ptf&&a.inPTF){if(PTF_MODE==='shipped'){rsPtfU=1-(p.szh?0.12+p.szhCoh*0.04:0.12);cf=discMul(cf,rsPtfU);}else cf-=PTF_FOOD_CUT[PTF_MODE]*fShareCur;}
    var cfPTF=cf;
    if(p.pth&&a.inPTH&&!PATHWAY_OFF.pthCost){if(PTH_MODE==='housing')cf-=PTH_HOUSING_CUT*hShareCur*rsPtfU;else cf=discMul(cf,0.65);}
    var cfPreCCO=cf;
    if(p.ccoOn&&a.inCCO&&p.bu>0){if(!PATHWAY_OFF.relief&&!FWON){cf=discMul(cf,ccoReliefF);rsRel=ccoReliefF;}}
    else if(emergLine>=0&&p.ccoOn&&p.bu>0&&!a.inCCO&&typeof a.uCCO==='number'&&a.uCCO<emergLine){cf=discMul(cf,ccoReliefF);rsRel=ccoReliefF;emergN++;}
    }
    var mainLoopCostUSD=CFG.LIVING_WAGE_ANNUAL*Math.pow(1+inflRate,yr);
    if(PRICE)mainLoopCostUSD*=PRICE.bIdx;  // session 2: endogenous basket index
    if(FWON&&p.ccoOn&&a.inCCO&&p.bu>0&&!PATHWAY_OFF.relief){  // session 2, N3/N4: BU buy essentials at the agent's own prices, up to 12 x BU a year
      var essF=eShareCur;
      if(p.ptf&&a.inPTF)essF=PTF_MODE==='shipped'?essF*(1-(p.szh?0.12+p.szhCoh*0.04:0.12)):essF-PTF_FOOD_CUT[PTF_MODE]*fShareCur;
      if(p.pth&&a.inPTH&&!PATHWAY_OFF.pthCost){if(PTH_MODE==='housing')essF-=PTH_HOUSING_CUT*hShareCur*rsPtfU;else essF*=0.65;}  // session 5 (d4)
      var fwBudget=12*buEff,fwB=Math.min(fwBudget,mainLoopCostUSD*essF),fwLeft=fwBudget-fwB;
      cf=cfPreCCO-fwB/mainLoopCostUSD;a._fwBUm=fwB/12;
      FWS.next.bizBU+=fwB;FWS.next.expiredBU+=fwLeft;FWS.next.projBU+=fwLeft*FW.directedShare;FWS.next.destroyedBU+=fwLeft*(1-FW.directedShare);
      if(PJON){PJS.next.pool+=fwLeft*PROJ.share;PJS.acc.exp+=fwLeft/pjIdx;PJS.acc.pool+=fwLeft*PROJ.share/pjIdx;}  // N1 (session 15): the same pool, paid as project hiring
      if(LEDGER){ledAdd(yr,'fwBudget',fwBudget);ledAdd(yr,'fwBUSpent',fwB);ledAdd(yr,'fwBUExpired',fwLeft);ledAdd(yr,'fwBUDirected',fwLeft*FW.directedShare);}
    }
    var annualWageUSD=a.wage*12*CFG.WAGE_TO_USD*incomeShock;
    var tbG=0,tbPT=0;if(tbY){tbPT=mainLoopCostUSD*(1-cfPreCCO);if(p.tb.groc&&a._tbU<p.tb.groc.cover)tbG=mainLoopCostUSD*p.tb.groc.cut*(fShareCur+(p.tb.groc.housing?hShareCur:0));}  // session 11: X-Cents Power of 1 on housing too (groc.housing)  // session 6: PTF/PTH price-cut dollars; public-grocery cut on the food component
    if(LABOR){  // session 4 (A3): the labor-supply response replaces this year's wage earnings (no RNG)
      var lbE0=annualWageUSD,lbBU=0,lbR=0,lbC=a._labC||0,lbU=p.ubi||0;
      if(p.ccoOn&&a.inCCO&&p.bu>0&&!PATHWAY_OFF.relief){if(FWON){lbBU=fwB;lbR=fwLeft;}else lbBU=mainLoopCostUSD*(cfPreCCO-cf);}
      var lbBiz=(FWON&&FWS.prev&&FWS.prev.wSum>0)?Math.max(0,FWS.prev.bizNet)/FWS.prev.wSum:0;
      if(ESON&&ESP.rest==='esp')lbBiz=(a._esWk&&ESS.wW>0&&FWS.prev)?Math.max(0,FWS.prev.bizNet)/ESS.wW:0;  // d75 alternative: the ESP's premium reaches its own workers only
      var lbRaise=Math.pow(Math.max(1,a.wage/a._lwNB)*(1+lbBiz)*(ESON?1+a._esX:1),LABOR.eps-LABOR.rho);  // uncompensated: Slutsky e_u = e_c + eta, eta = -rho. Session 19: x the ESP payroll raise (earned: one elasticity, no income effect)
      var tbQ=tbY?tbLab(a,tbY,lbE0,tbPT+tbG):null;if(tbQ)lbRaise*=tbQ.F;  // session 6: phase-out and contribution rates (one elasticity), extra unconditional dollars (one income effect)
      var lbInc=LABOR.rho*lbU+LABOR.rhoBU*lbBU+LABOR.rhoR*lbR+LABOR.rho*(1-LABOR.delta)*lbC+(tbQ?LABOR.rho*tbQ.V:0),lbDisp=LABOR.delta*lbC+(tbQ?tbQ.D:0);
      annualWageUSD=Math.max(0,lbE0*lbRaise-lbInc-lbDisp);a._lbE0=lbE0;  // session 8 (A5): earnings with no response, for the hours measure
      if(tbQ&&LABOR.acc)LABOR.acc.cash+=LABOR.rho*tbQ.V;
      if(LABOR.acc){var LA=LABOR.acc;LA.n++;if(a.inCCO)LA.nP++;LA.E0+=lbE0;LA.E+=annualWageUSD;LA.raise+=lbE0*(lbRaise-1);LA.cash+=LABOR.rho*lbU;LA.bu+=LABOR.rhoBU*lbBU;LA.buR+=LABOR.rhoR*lbR;
        LA.rent+=LABOR.rho*(1-LABOR.delta)*lbC;LA.disp+=lbDisp;LA.C+=lbC;LA.U+=lbU+lbBU;LA.projH+=lbE0>0?lbDisp/lbE0:0;if(annualWageUSD===0&&lbE0>0)LA.zero++;}
    }
    if(PJON){a._pjHW=0;if(a._pjBU>0){var pjH=a._pjBU/pjPay,pjHw=a.wage*12*CFG.WAGE_TO_USD*incomeShock/PROJ.hrsYr,pjD=pjH*pjHw;  // N1 (session 15): project hours
      if(PROJ.hours==='displace'){pjD=Math.min(pjD,Math.max(0,annualWageUSD));annualWageUSD-=pjD;if(LABOR&&LABOR.acc)LABOR.acc.E-=pjD;}
      a._pjHW=pjD;PJS.acc.hrs+=pjH;PJS.acc.disp+=(PROJ.hours==='displace'?pjD:0)/pjIdx;}}
    if(tbG)cf-=tbG/mainLoopCostUSD;  // session 6: public grocery (applied after the labor block reads the CCO relief)
    var costUSD=mainLoopCostUSD*cf;
    a.wealth+=annualWageUSD-costUSD;
    if(SURPLUS_CONSUMPTION_SHARE>0&&SURPLUS_CONSUMPTION_BASE==='wage')a.wealth-=SURPLUS_CONSUMPTION_SHARE*Math.max(0,annualWageUSD-costUSD);  // v4.21: harness-only (saving mode)
    if(p.ubi>0){a.wealth+=p.ubi;a.yrUbiUSD=p.ubi;}  // session 4: UBI comparator (harness-only; unset in every preset)
    var yrCashSurplus=annualWageUSD-costUSD+(p.ubi>0?p.ubi:0);  // session 1: for SURPLUS_CONSUMPTION_BASE 'cash' (harness-only; no RNG)
    if(tbY){var tbK=tbCashFlow(a,tbY,annualWageUSD,yr);a.wealth+=tbK.net+tbK.endow;yrCashSurplus+=tbK.net;}  // session 6: cash transfers less the contribution; an endowment is wealth, not consumable surplus
    if(LEDGER){  // A1 ledger (reporting only): no RNG, no state read by any dynamic
      ledAdd(yr,'agentYears',1);if(a.inCCO)ledAdd(yr,'partYears',1);
      ledAdd(yr,'wage',annualWageUSD);ledAdd(yr,'cost',costUSD);ledAdd(yr,'basket',mainLoopCostUSD);
      if(SURPLUS_CONSUMPTION_SHARE>0&&SURPLUS_CONSUMPTION_BASE==='wage')ledAdd(yr,'surplusConsumed',SURPLUS_CONSUMPTION_SHARE*Math.max(0,annualWageUSD-costUSD));
      ledAdd(yr,'ptfRelief',mainLoopCostUSD*(1-cfPTF));ledAdd(yr,'pthRelief',mainLoopCostUSD*(cfPTF-cfPreCCO));
      ledAdd(yr,a.inCCO?'ccoRelief':'emergRelief',mainLoopCostUSD*(cfPreCCO-cf));
    }
    a.yrWageUSD=annualWageUSD;a.yrCostUSD=costUSD;a.yrBasketUSD=mainLoopCostUSD;a.yrConvUSD=0;  /* v4.17: income/basket poverty inputs (no RNG) */
    if(FWON){  // session 2, N1: last year's business conversion premium, paid to every agent in proportion to last year's wage income
      a._fwPayY=0;  // session 19: reporting only (the testbed's premium-by-group columns)
      if(FWS.prev&&FWS.prev.wSum>0){var fwPay=FWS.prev.bizNet*(a._fwW||0)/FWS.prev.wSum;
        if(ESON&&ESP.rest==='esp')fwPay=(a._esWk&&ESS.wW>0)?FWS.prev.bizNet*(a._fwW||0)/ESS.wW:0;  // d75 alternative (session 19): a worker cooperative
        a.wealth+=fwPay;a.yrConvUSD+=fwPay;yrCashSurplus+=fwPay;FWS.next.bizPaid+=fwPay;a._fwPayY=fwPay;
        if(PRICE)PRICE.acc.conv+=fwPay;if(LEDGER)ledAdd(yr,'fwBizPayout',fwPay);}
      if(ESON){a._esPrY=0;if(a._esC>0){  // session 19 (s38, d73): ESP payroll BU converted at the worker's own rate; the premium over face value is conversion income
        var esTx=pjTax(p,a._esR),esG=PATHWAY_OFF.conversion?0:a._esC*a._esR*esCipB*incomeShock,esPr=PATHWAY_OFF.conversion?0:esG*(1-esTx)-a._esC;
        a.wealth+=esPr;a.yrConvUSD+=esPr;yrCashSurplus+=esPr;a._esPrY=esPr;a._esShk=incomeShock;
        var esAc=ESS.acc;esAc.conv+=a._esC/esIdx;esAc.gross+=esG/esIdx;esAc.tax+=esG*esTx/esIdx;esAc.prem+=esPr/esIdx;esAc.rateXbu+=a._esR*a._esC/esIdx;
        if(PRICE)PRICE.acc.conv+=esPr;if(LEDGER){ledAdd(yr,'espGross',esG);ledAdd(yr,'espTax',esG*esTx);ledAdd(yr,'espPremium',esPr);}}}
      a._fwW=annualWageUSD;FWS.next.wSum+=annualWageUSD;
    }
    if(isNaN(a.wealth))a.wealth=0;
    if(p.ccoOn&&a.inCCO&&FWON){
      /* Session 2, CONVERSION_MODEL 'framework' (N1-N4). No personal BU balance and no conversion of one's own spending:
       * the participant converts the BU directed to projects last year (N2), allocated in proportion to octave capacity
       * x quality, capped at their octave capacity, at their own engine rate and under the engine's progressive tax.
       * The draws above are made exactly as in the engine branch, so the two models stay CRN-paired. */
      if(p.cip&&uCipQuality<p.cipDemo*0.15)a.quality=Math.min(p.maxMult,a.quality+0.1);
      var octCeilF=1+(a.octave/Math.max(1,p.maxOct))*(Math.max(1,p.maxMult)-1),qfF=Math.min(1,a.quality/Math.max(1,p.maxMult));
      var phiF=(p.phi&&a.quality>p.maxMult*CFG.PHI_QUALITY_THRESH)?CFG.PHI_RATIO:1.0,ptfBF=(p.ptf&&a.inPTF)?ptfConvBonus:1.0;
      var rateF=Math.min((1+qfF*(octCeilF-1))*phiF*ptfBF,p.maxMult*(p.phi?CFG.PHI_RATIO:1.0));
      var bTaxF=p.cip?p.tax*(1-p.cipDemo*0.18):p.tax,taxF=Math.min(CFG.PROG_TAX_MAX,bTaxF+Math.max(0,(rateF-CFG.PROG_PIVOT)*CFG.PROG_RATE));
      var cipBF=p.cip?(1+p.cipDemo*0.12):1.0,capBU=12*FW.octaveCapBase*Math.pow(2,a.octave);
      if(FWS.prev&&FWS.prev.pwSum>0&&!PJON){  // N1 (session 15): project hiring replaces N2's allocation
        var fwWant=FWS.prev.projBU*(a._fwPW||0)/FWS.prev.pwSum,fwAl=Math.min(capBU,fwWant);
        var fwG=PATHWAY_OFF.conversion?0:fwAl*rateF*cipBF*incomeShock,fwN=fwG*(1-taxF);
        a.wealth+=fwN;a.yrConvUSD+=fwN;yrCashSurplus+=fwN;totalConversion+=fwN;totalBU+=fwAl;if(LABOR)a._labCn=fwN;
        FWS.next.projAlloc+=fwAl;FWS.next.projGross+=fwG;FWS.next.projTax+=fwG*taxF;FWS.next.projNet+=fwN;FWS.next.projLost+=fwWant-fwAl;
        if(PRICE)PRICE.acc.conv+=fwN;
        if(LEDGER){ledAdd(yr,'fwProjBU',fwAl);ledAdd(yr,'fwProjGross',fwG);ledAdd(yr,'fwProjTax',fwG*taxF);ledAdd(yr,'fwProjNet',fwN);ledAdd(yr,'fwProjLost',fwWant-fwAl);ledAdd(yr,'fwProjRateXbu',rateF*fwAl);}
      }
      a._fwPW=capBU*Math.max(0,a.quality);FWS.next.pwSum+=a._fwPW;
      if(a.octave<p.maxOct){  // as in the engine branch, except that the monthly basic cost is read before the BU purchase, since BU is added as income here
        var YusdF=a.wage*CFG.WAGE_TO_USD,cBasicF=(dollarCost*cfPreCCO)/12,edcF=(p.pth&&a.inPTH)?CFG.FBS_EDC_RESIDUAL_PTH:CFG.FBS_EDC_RESIDUAL_BASE;
        var fbsF=Math.max(0,YusdF+buEff-cBasicF-edcF*YusdF),lamF=(typeof a.lambda==='number'&&!isNaN(a.lambda))?a.lambda:(CFG.FBS_LAMBDA_LO+CFG.FBS_LAMBDA_HI)/2;
        if(p.cip)lamF*=(1+p.cipDemo*CFG.FBS_CIP_LAMBDA_BOOST);
        if(uAdvance<1-Math.exp(-lamF*fbsF)&&!PATHWAY_OFF.octave)a.octave++;
      }
      if(uSzhInduce<szhPartBoost&&!a.inPTF&&p.ptf&&ptfCapAllows()){a.inPTF=uSzhPtfShare<p.ptfShare;if(a.inPTF&&p.ptfCap)ptfLiveCount++;}
    } else if(p.ccoOn&&a.inCCO){
      /* v4.14 parity fix — ported from index.html: this was a step function (decay=0 at
       * expiry=1, decay=0.7 at every other slider value, 2-6 all identical) rather than a
       * continuous function of the slider. Replaced with decay=1-1/expiry, a documented
       * annual-approximation interpretation. At expiry=1 (used by every shipped preset and
       * this harness's own FULL_INTEGRATION/BASELINE configs) decay=0, identical to the
       * prior behaviour — zero effect on any documented regression figure. See
       * CONTRIBUTING.md's v4.14 Release Notes. */
      var decay=Math.max(0,1-1/Math.max(1,p.expiry||1));
      if(stabOn&&p.stabSusp)decay=1;  // v4.19: expiry suspended while triggered  /* v4.15 parity: || 1 guards a missing expiry — Math.max(1,undefined) is NaN */
      if(LEDGER){var lbK=a.buBalance*decay,lbI=buEff*BU_ALLOCATIONS_PER_YEAR,lbC=buEff*3*BU_ALLOCATIONS_PER_YEAR;ledAdd(yr,'buIssued',lbI);ledAdd(yr,'buExpired',(a.buBalance-lbK)+Math.max(0,lbK+lbI-lbC));}  // A1 ledger
      if(PJON){var pjK=a.buBalance*decay,pjAl=buEff*BU_ALLOCATIONS_PER_YEAR,pjX=(a.buBalance-pjK)+Math.max(0,pjK+pjAl-buEff*3*BU_ALLOCATIONS_PER_YEAR);PJS.next.pool+=pjX*PROJ.share;PJS.acc.exp+=pjX/pjIdx;PJS.acc.pool+=pjX*PROJ.share/pjIdx;}  // N1 (session 15): expired BU go to projects
      a.buBalance=Math.min(a.buBalance*decay+buEff*BU_ALLOCATIONS_PER_YEAR,buEff*3*BU_ALLOCATIONS_PER_YEAR);  // v4.19: buEff; allocations/yr is a harness-only switch (index.html: 1)
      var spend=a.buBalance*uSpendFrac;a.buBalance-=spend;totalBU+=spend;
      if(p.cip&&uCipQuality<p.cipDemo*0.15)a.quality=Math.min(p.maxMult,a.quality+0.1);
      var octCeiling=1+(a.octave/Math.max(1,p.maxOct))*(Math.max(1,p.maxMult)-1);
      var qualityFactor=Math.min(1,a.quality/Math.max(1,p.maxMult));
      var baseRate=1+qualityFactor*(octCeiling-1);
      var phi=(p.phi&&a.quality>p.maxMult*CFG.PHI_QUALITY_THRESH)?CFG.PHI_RATIO:1.0;
      var ptfB=(p.ptf&&a.inPTF)?ptfConvBonus:1.0;
      var cipB=p.cip?(1+p.cipDemo*0.12):1.0;
      var rate=Math.min(baseRate*phi*ptfB,p.maxMult*(p.phi?CFG.PHI_RATIO:1.0));
      var bTax=p.cip?p.tax*(1-p.cipDemo*0.18):p.tax;
      var progTax=Math.min(CFG.PROG_TAX_MAX,bTax+Math.max(0,(rate-CFG.PROG_PIVOT)*CFG.PROG_RATE));
      var convGain=PATHWAY_OFF.conversion?0:spend*rate*(1-progTax)*cipB*incomeShock;  // v4.21: pathway switch
      a.wealth+=convGain;totalConversion+=convGain;a.yrConvUSD=convGain;yrCashSurplus+=convGain;if(LABOR)a._labCn=convGain;
      if(PRICE)PRICE.acc.conv+=convGain;  // session 2: price module (P_G injection)
      if(LEDGER){var lcG=PATHWAY_OFF.conversion?0:spend*rate*cipB*incomeShock,lcT=lcG*progTax,lcI=0;while(lcI<LEDGER_RATE_TIERS.length&&rate>=LEDGER_RATE_TIERS[lcI])lcI++;
        var lcTier=LEDGER.tiers[lcI];lcTier.bu+=spend;lcTier.gross+=lcG;lcTier.tax+=lcT;lcTier.net+=convGain;lcTier.n++;
        ledAdd(yr,'buSpent',spend);ledAdd(yr,'convGross',lcG);ledAdd(yr,'convTax',lcT);ledAdd(yr,'convNet',convGain);ledAdd(yr,'convRateXspend',rate*spend);}  // A1 ledger
      if(isNaN(a.wealth))a.wealth=0;
      if(a.octave<p.maxOct){
        var Yusd=a.wage*CFG.WAGE_TO_USD;
        var cBasicMonthly=(dollarCost*(FBS_BU_ONCE?cfPreCCO:cf))/12;  // session 7: harness-only switch (i3-1); index.html reads cf
        var edcResidual=(p.pth&&a.inPTH)?CFG.FBS_EDC_RESIDUAL_PTH:CFG.FBS_EDC_RESIDUAL_BASE;
        var fbs=Math.max(0,Yusd+buEff-cBasicMonthly-edcResidual*Yusd);
        var lam=(typeof a.lambda==='number'&&!isNaN(a.lambda))?a.lambda:(CFG.FBS_LAMBDA_LO+CFG.FBS_LAMBDA_HI)/2;
        if(p.cip)lam*=(1+p.cipDemo*CFG.FBS_CIP_LAMBDA_BOOST);
        var pAdvance=1-Math.exp(-lam*fbs);
        if(uAdvance<pAdvance&&!PATHWAY_OFF.octave)a.octave++;  // v4.21: pathway switch
      }
      if(uSzhInduce<szhPartBoost&&!a.inPTF&&p.ptf&&ptfCapAllows()){a.inPTF=uSzhPtfShare<p.ptfShare;if(a.inPTF&&p.ptfCap)ptfLiveCount++;}
    }
    if(PJON&&p.ccoOn&&a.inCCO){  // N1 (session 15): convert project BU (and a holder's own gift) within octave capacity; the rest is saved
      var pjA=PJS.acc,pjCapR=PROJ.cap?Math.max(0,a._pjCap-(FWON?0:spend)):Infinity,pjE=(a._pjSaved||0)+(a._pjBU||0),pjC1=Math.min(pjE,pjCapR);a._pjSaved=pjE-pjC1;pjCapR-=pjC1;
      var pjGh=a._pjGiftH||0,pjC2=Math.min(pjGh,pjCapR);a._pjGiftH=pjGh-pjC2;
      if(PROJ.cap&&pjC1+pjC2>Math.max(0,a._pjCap-(FWON?0:spend))+1e-6)pjA.overCap++;  // project BU fill the capacity the engine's own-spending conversion leaves (that conversion is not capped; at $1,200 BU it never reaches 12,000)
      var pjTx=pjTax(p,a._pjRu),pjG1=PATHWAY_OFF.conversion?0:pjC1*a._pjRu*pjCipB*incomeShock,pjN1=pjG1*(1-pjTx);
      var pjTg=pjTax(p,a._pjR),pjG2=PATHWAY_OFF.conversion?0:pjC2*a._pjR*pjCipB*incomeShock,pjN2=pjG2*(1-pjTg);
      a.wealth+=pjN1+pjN2;a.yrConvUSD+=pjN1+pjN2;yrCashSurplus+=pjN1+pjN2;totalConversion+=pjN1+pjN2;totalBU+=pjC1+pjC2;
      if(LABOR&&pjN2)a._labCn=(a._labCn||0)+pjN2;  // the holder's gift is an unconditional dollar: the rent channel
      a.yrPjGift=pjN1*pjFg+pjN2;  // d66: gift-funded proceeds, tallied so the testbed can finance them as you go or over the run (the carried share is approximate)
      if(PRICE)PRICE.acc.conv+=pjN1+pjN2;
      pjA.conv+=pjC1/pjIdx;pjA.giftConv+=pjC2/pjIdx;pjA.gross+=(pjG1+pjG2)/pjIdx;pjA.net+=pjN1/pjIdx;pjA.giftNet+=pjN2/pjIdx;
      if(LEDGER){ledAdd(yr,'pjBU',a._pjBU||0);ledAdd(yr,'pjConvBU',pjC1+pjC2);ledAdd(yr,'pjNet',pjN1+pjN2);}
      if(isNaN(a.wealth))a.wealth=0;
    }
    if(p.pth&&a.inPTH&&!PATHWAY_OFF.pthEquity&&!PATHWAY_OFF.pthCost){  // v4.21: pathway switches (off: no routing, no appreciation)
      if(typeof a.pthTenure!=='number'||isNaN(a.pthTenure))a.pthTenure=0;
      a.pthTenure+=1;
      var cfWithoutPTH=cf/0.65;
      var pthSaving=Math.max(0,dollarCost*cfWithoutPTH*(1-0.65));
      if(rsAlt)pthSaving=Math.max(0,dollarCost*(cfPTF-cfPreCCO)*rsRel);  // session 5 (d4/d5): PTH's own cut on the post-relief basket
      var equityContrib=pthSaving*CFG.PTH_EQUITY_CONTRIB_SHARE;
      a.acreEquity+=equityContrib;a.wealth-=equityContrib;yrCashSurplus-=equityContrib;  // session 1: equity routing is not discretionary cash
      var ar=0.030+uPthAppr*0.020+pthApprBonus;var appr=a.acreEquity*ar,lqs=pthLiquidShare(a.pthTenure);a.acreEquity+=PTH_APPR_CONSERVE?appr*(1-lqs):appr;a.wealth+=appr*lqs;yrCashSurplus+=appr*lqs;  /* v4.16: PTH_APPR_CONSERVE=false is bit-identical to index.html */
      if(tbY)a._tbPthNow=appr*lqs;  // session 6
      if(LEDGER){ledAdd(yr,'pthEquityContrib',equityContrib);ledAdd(yr,'pthAppr',appr);ledAdd(yr,'pthApprLiquid',appr*lqs);}  // A1 ledger
      if(PRICE)PRICE.acc.pthLiq+=appr*lqs;  // session 2: price module
    } else if(a.pthTenure){
      a.pthTenure=0;
    }
    if(p.ptf&&!a.inPTF&&p.ptfShare>0&&yr>0&&ptfCapAllows()){var ap=0.005+CFG.PTF_BASS_Q*ptfAdoptFrac;if(bleiCheck<CFG.BLEI_PRECARIOUS_MAX)ap+=0.015;if(uPtfAdopt<ap){a.inPTF=true;if(p.ptfCap)ptfLiveCount++;}}
    if(SURPLUS_CONSUMPTION_SHARE>0&&SURPLUS_CONSUMPTION_BASE==='cash'){var scC=SURPLUS_CONSUMPTION_SHARE*Math.max(0,yrCashSurplus);a.wealth-=scC;if(LEDGER)ledAdd(yr,'surplusConsumed',scC);}  // session 1: harness-only
    if(PRICE){  // session 2 (D1/N5): a write-off at the floor is basket consumption that did not happen (unmet need), not spending
      var pmW=a.wealth<CFG.WEALTH_FLOOR?CFG.WEALTH_FLOOR-a.wealth:0,pmB=mainLoopCostUSD*cfPreCCO,pmU=pmB>0?Math.min(1,pmW/pmB):0,A=PRICE.acc;
      A.n++;A.essD+=1-pmU;A.unmet+=pmW;A.basketOwn+=pmB;if(pmW>0)A.unmetN++;A.Y+=annualWageUSD+a.yrConvUSD;if(p.ptf&&a.inPTF)A.ptfN++;
      A.wageBonus+=Math.max(0,a.wage-a._wNB)*12*CFG.WAGE_TO_USD*incomeShock;A.wageBonusNS+=Math.max(0,a.wage-a._wNB)*12*CFG.WAGE_TO_USD;  // session 3: the premium before the income shock, for aw's increment reading
    }
    if(LABOR){a._labC=a._labCn||0;a._labCn=0;if(LABOR.acc){LABOR.acc.conv+=a.yrConvUSD||0;if(a.inCCO)LABOR.acc.convP+=a.yrConvUSD||0;}}  // session 4: creator proceeds carried to next year's labor response
    if(tbY)tbAccount(a,tbY,yr,mainLoopCostUSD,cf,cfPreCCO,costUSD,annualWageUSD,tbG,tbPT);  // session 6: uniform cost ledger and basket FGT (reporting; no RNG)
    if(a.wealth<CFG.WEALTH_FLOOR){if(LEDGER){var lfA=CFG.WEALTH_FLOOR-a.wealth;ledAdd(yr,'floor',lfA);ledAdd(yr,'floorHits',1);a._ledFloor=(a._ledFloor||0)+lfA;}a.wealth=CFG.WEALTH_FLOOR;}  // A1 ledger inside the clamp
  });
  if(FWON){  // session 2, N1: businesses convert this year's accepted BU; the premium over a cash sale is paid out next year
    var nx=FWS.next,bTaxB=p.cip?p.tax*(1-p.cipDemo*0.18):p.tax;
    var taxR=Math.min(CFG.PROG_TAX_MAX,bTaxB+Math.max(0,(FW.bizRate-CFG.PROG_PIVOT)*CFG.PROG_RATE)),taxP=Math.min(CFG.PROG_TAX_MAX,bTaxB);
    var bzB=ESON?nx.bizBU*(1-ESP.lam):nx.bizBU;  // session 19 (d71): with ESP payroll the ESP converts the share it keeps; lam of what it accepted is next year's payroll
    nx.bizGross=bzB*(FW.bizCap*FW.bizRate+(1-FW.bizCap));nx.bizTax=bzB*(FW.bizCap*FW.bizRate*taxR+(1-FW.bizCap)*taxP);
    nx.bizNet=PATHWAY_OFF.conversion?0:nx.bizGross-nx.bizTax-bzB;  // session 7: the conversion switch also covers business-side conversion (harness-only)
    if(LEDGER){ledAdd(yr,'fwBizGross',nx.bizGross);ledAdd(yr,'fwBizTax',nx.bizTax);ledAdd(yr,'fwBizPremium',nx.bizNet);}
    if(ESON){ESS.next={pool:nx.bizBU*ESP.lam};ESS.acc.accBU+=nx.bizBU/esIdx;ESS.acc.ownBU+=bzB/esIdx;ESS.y[yr].acc=nx.bizBU;ESS.y[yr].own=bzB;ESS.y[yr].poolNext=ESS.next.pool;
      if(LEDGER){ledAdd(yr,'espOwnBU',bzB);ledAdd(yr,'espPoolNext',ESS.next.pool);}}
    FWS.prev=nx;
  }
  if(ESON)ESS.prev=ESS.next;  // N1 (session 19)
  if(PJON)PJS.prev=PJS.next;  // N1 (session 15)
  return{bu:totalBU,conversion:totalConversion,stabOn:stabOn,stabM:stabM,colaF:colaF,buEff:buEff,emergN:emergN};  // v4.19
}

/* v4.17: income and basket poverty — ported verbatim to/from index.html (see its comment on
 * incomeBasketMetrics for definitions). Cash income = this year's wage income (after the
 * income shock) + CCO conversion proceeds; PTH appreciation is excluded (a capital gain,
 * excluded from disposable income in the OECD/EU convention). Relative income poverty: cash
 * income below 60% of the same population's median. Basket poverty: cash income below the
 * agent's own inflation-adjusted LIVING_WAGE_ANNUAL basket after its CCO/PTF/PTH cost
 * reductions (net) or before them (gross). incPovExt adds the in-kind value of those cost
 * reductions (gross basket − own cost) to income before applying the 60%-of-median line. */
function medianOf(arr){var s=arr.slice().sort(function(a,b){return a-b;}),n=s.length;return n?(n%2===0?(s[n/2-1]+s[n/2])/2:s[Math.floor(n/2)]):0;}
function incomeBasketMetrics(agents){
  var inc=agents.map(function(a){var w=+a.yrWageUSD,c=+a.yrConvUSD;return (isNaN(w)?0:w)+(isNaN(c)?0:c)+(a.yrUbiUSD||0);});  /* session 4: + UBI (harness-only; absent in every preset) */
  var n=inc.length;if(!n||agents[0].yrBasketUSD===undefined)return null;
  var ext=agents.map(function(a,i){return inc[i]+Math.max(0,(+a.yrBasketUSD||0)-(+a.yrCostUSD||0));});
  var med=medianOf(inc),line=0.6*med,medX=medianOf(ext),rel=0,relX=0,net=0,gross=0;
  agents.forEach(function(a,i){if(inc[i]<line)rel++;if(ext[i]<0.6*medX)relX++;if(inc[i]<a.yrCostUSD)net++;if(inc[i]<a.yrBasketUSD)gross++;});
  return{medianIncome:med,incPov:rel/n*100,incPovExt:relX/n*100,basketPov:net/n*100,basketPovGross:gross/n*100};
}
function incomeBasketYear0(agents){
  var inc=agents.map(function(a){return Math.max(isNaN(a.wage)?0:a.wage,0)*12*CFG.WAGE_TO_USD;});
  var n=inc.length;if(!n)return null;var med=medianOf(inc),rel=0,bsk=0;
  inc.forEach(function(v){if(v<0.6*med)rel++;if(v<CFG.LIVING_WAGE_ANNUAL)bsk++;});
  return{medianIncome:med,incPov:rel/n*100,incPovExt:rel/n*100,basketPov:bsk/n*100,basketPovGross:bsk/n*100};
}
/* v4.18: extreme-poverty overlay, verbatim from index.html (see its comment block there).
 * Expected share from three pathways; draws no RNG and feeds nothing back. */
function housingDistressOf(agents){
  if(!agents||!agents.length||agents[0].yrWealthStartUSD===undefined)return null;
  var n=0;
  agents.forEach(function(a){var inc=(+a.yrWageUSD||0)+(+a.yrConvUSD||0),w=+a.yrWealthStartUSD||0;if(inc+Math.max(0,w)<(+a.yrCostUSD||0))n++;});
  return n/agents.length;
}
function housingDistressYear0(agents){
  if(!agents||!agents.length)return null;
  var n=0;
  agents.forEach(function(a){var inc=Math.max(isNaN(a.wage)?0:a.wage,0)*12*CFG.WAGE_TO_USD,w=isNaN(a.wealth)?0:a.wealth;if(inc+Math.max(0,w)<CFG.LIVING_WAGE_ANNUAL)n++;});
  return n/agents.length;
}
function wellnessZoneReach(p){return(p&&p.pth&&p.szh)?CFG.EP_WZ_EFFECT*Math.max(0,Math.min(1,+p.szhCoh||0)):0;}
function extremePovertyOf(d,d0,p){
  if(d===null||d===undefined||isNaN(d)||!(d0>0))return null;
  var R=CFG.EP_Y0_RATE,s=CFG.EP_SMI_SHARE,v=CFG.EP_VOL_SHARE,wz=p==='year0'?0:wellnessZoneReach(p);
  var econ=R*(1-s-v)*d/d0,smi=R*s*(1-wz),vol=R*v;
  return{total:(econ+smi+vol)*100,econ:econ*100,smi:smi*100,vol:vol*100,distress:d*100,wz:wz};
}
/* v4.17: recessions, ported verbatim from index.html (NEEC maintainers' note 5), so stress
 * runs need nothing from the page. buildRecessionPath() draws on its own stream
 * (seed+700000) and restores RNG, so enabling shocks moves no agent draw — the same
 * paired-shock design simulate() uses for Main/Baseline/CCO-Only. */
function updateRecession(recSt){
  if(recSt.active){recSt.yearsLeft--;if(recSt.yearsLeft<=0){recSt.active=false;recSt.incomeMultiplier=1.0;}}
  else if(RNG()<0.10){recSt.active=true;recSt.yearsLeft=1+Math.floor(RNG()*3);recSt.incomeMultiplier=0.70+beta(5,2)*0.25;}
}
function buildRecessionPath(years,seed){
  var path=[],saved=RNG;
  RNG=(seed===null||seed===undefined||isNaN(seed))?saved:mulberry32(seed+700000);
  var st={active:false,incomeMultiplier:1.0,yearsLeft:0};
  for(var y=0;y<years;y++){
    if(y>0)updateRecession(st);
    path.push({active:st.active,incomeMultiplier:st.incomeMultiplier});
  }
  RNG=saved;
  return path;
}

function interpP(sorted,p){var n=sorted.length;if(!n)return 0;var pos=p*(n-1),lo=Math.floor(pos),hi=Math.ceil(pos);return lo===hi?sorted[lo]:sorted[lo]+(pos-lo)*(sorted[hi]-sorted[lo]);}
function calcMetrics(agentSet,ccoOn,pthOn){
  var useNet=(typeof ccoOn!=='undefined');
  var ws=agentSet.map(function(a){return isNaN(a.wealth)?0:a.wealth;}).sort(function(a,b){return a-b;});
  var n=ws.length,pov=ws.filter(function(w){return w<CFG.POVERTY_LINE;}).length/n;
  var wcl=ws.map(function(w){return Math.max(0,w);});
  var totW=wcl.reduce(function(s,w){return s+w;},0);
  var gini=0;
  if(useNet){
    var netW=agentSet.map(function(a){
      var w=isNaN(a.wealth)?0:a.wealth;
      var edc=agentEDC(a,ccoOn,pthOn);
      var yUsd=Math.max(isNaN(a.wage)?0:a.wage,0)*CFG.WAGE_TO_USD;
      return Math.max(0,w-edc*yUsd*12);
    }).sort(function(a,b){return a-b;});
    var totWN=netW.reduce(function(s,w){return s+w;},0);
    if(totWN>0){var gNumN=0;for(var j=0;j<n;j++)gNumN+=(j+1)*netW[j];gini=(2*gNumN/(n*totWN))-(n+1)/n;}
  } else if(totW>0){
    var gNum=0;for(var i=0;i<n;i++)gNum+=(i+1)*wcl[i];gini=(2*gNum/(n*totW))-(n+1)/n;
  }
  var med=n%2===0?(ws[n/2-1]+ws[n/2])/2:ws[Math.floor(n/2)];
  return{pov:Math.max(0,Math.min(1,pov)),gini:Math.max(0,Math.min(1,gini)),med:med,p10:interpP(ws,0.10),p90:interpP(ws,0.90)};
}
function calcMedianBLEI(agents,p){var sc=agents.map(function(a){return agentBLEI(a,p.bu,p.ccoOn,p.pth,p.szh,p.szhCoh,p.ptf);});sc.sort(function(a,b){return a-b;});var n=sc.length;if(!n)return 0;return n%2===0?(sc[n/2-1]+sc[n/2])/2:sc[Math.floor(n/2)];}

/* calcBLEIComponents — verbatim from index.html, added post-hoc to check the
 * "benefitDays line invisible in the chart" report. */
function calcBLEIComponents(agents,p){
  var cash=[],inc=[],ben=[];
  agents.forEach(function(a){
    var liq=Math.max(0,(isNaN(a.wealth)?0:a.wealth)*0.20);
    var g=(p.ccoOn&&a.inCCO)?0.20:0.12;
    var buF=(p.ccoOn&&a.inCCO&&p.bu>0)?p.bu*(990/1200):0;
    var sD=p.szh?p.szhCoh*CFG.SZH_ALL_RESIDENTS:0;if(p.szh&&p.ptf&&a.inPTF)sD+=szhTheta(p.szhCoh)*0.20;
    var dc=Math.max(((p.ccoOn&&a.inCCO&&p.pth&&a.inPTH)?CFG.CCO_PTH_DAILY_COST:CFG.BASE_DAILY_COST)*(1-sD),0.1);
    cash.push(liq/dc);inc.push(g*Math.max(isNaN(a.wage)?0:a.wage,0)*CFG.WAGE_TO_USD/dc);ben.push(buF/dc);
  });
  function med(arr){arr.sort(function(a,b){return a-b;});var n=arr.length;return n?n%2===0?(arr[n/2-1]+arr[n/2])/2:arr[Math.floor(n/2)]:0;}
  return{cash:med(cash),inc:med(inc),ben:med(ben)};
}
function runScenarioWithComponents(p, seed){
  RNG = mulberry32(seed + 700003);
  var latentPop = makeLatentPopulation(p.nAgents);
  var agents = latentPop.map(function(lat){ return instantiateAgent(lat, p); });
  RNG = mulberry32(seed);
  var rows = [];
  for (var yr = 0; yr < p.years; yr++){
    runYear(agents, yr, p, {active:false, incomeMultiplier:1.0, yearsLeft:0});
    var comp = calcBLEIComponents(agents, p);
    var partFrac = agents.filter(function(a){return a.inCCO;}).length/agents.length;
    rows.push({yr:yr+1, cash:+comp.cash.toFixed(2), inc:+comp.inc.toFixed(2), ben:+comp.ben.toFixed(2), partFrac:+partFrac.toFixed(3)});
  }
  return rows;
}
module.exports.calcBLEIComponents = calcBLEIComponents;
module.exports.runScenarioWithComponents = runScenarioWithComponents;

function coeffVar(arr){
  var n=arr.length;if(n<2)return 0;
  var mean=arr.reduce(function(s,x){return s+x;},0)/n;
  if(Math.abs(mean)<1e-9)return 0;
  var variance=arr.reduce(function(s,x){return s+(x-mean)*(x-mean);},0)/n;
  return Math.sqrt(variance)/Math.abs(mean);
}
/* v4.17 parity fix — ported from index.html's v4.13 fix, which this harness never received:
 * the final-quarter window was Math.max(1,…), so any 5-7 year run used a single point, for
 * which coeffVar() returns 0 and the metric returns its 0.99 ceiling regardless of the run.
 * index.html has used Math.max(2,…) since v4.13. Runs of 8+ years (every documented figure)
 * are unaffected: floor(8/4)=2 already. Reported by the NEEC maintainers (Sessions 38/40). */
function structuralStability(wealthSeries,bleiSeries){
  var q=Math.max(2,Math.floor(wealthSeries.length/4));
  var wStab=1/(1+coeffVar(wealthSeries.slice(-q))),bStab=1/(1+coeffVar(bleiSeries.slice(-q)));
  return Math.max(0,Math.min(0.99,(wStab+bStab)/2));
}

/* ─── Scenario runner ────────────────────────────────────────────────────
 * Mirrors simulate()'s MAIN-trajectory RNG discipline exactly: population
 * drawn on mulberry32(seed+700003), trajectory run on a *fresh, unoffset*
 * mulberry32(seed) closure — these are two independent streams in the
 * shipped code (see the comment block above the baseline trajectory loop
 * in simulate()), so reproducing the Main run does not require also
 * running the baseline/CCO-only comparisons. */
function runScenario(p, seed){
  RNG = mulberry32(seed + 700003);
  var latentPop = makeLatentPopulation(p.nAgents);
  var agents = latentPop.map(function(lat){ return instantiateAgent(lat, p); });
  /* v4.17: year-0 reference (before any year runs; draws no RNG). Wealth poverty and the
   * income measures are policy-neutral (same latent population in every scenario); BLEI is
   * not — agentBLEI() credits BU, γ=0.20 and reduced daily cost to participants — so the
   * policy-neutral BLEI figure evaluates the same agents under Baseline rules. */
  var m0 = calcMetrics(agents);
  var bN0 = bleiMetrics(agents, 0, false, false, false, 0, false), bY0 = bleiMetrics(agents, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf);
  var ib0 = incomeBasketYear0(agents);
  var d0 = housingDistressYear0(agents);  /* v4.18 */
  var yearZero = {pov:+(m0.pov*100).toFixed(1), bleiPovNeutral:+((bN0.tc[0]+bN0.tc[1])/bN0.n*100).toFixed(1),
    bleiPovScenario:+((bY0.tc[0]+bY0.tc[1])/bY0.n*100).toFixed(1), incPov:+ib0.incPov.toFixed(1), incPovExt:+ib0.incPovExt.toFixed(1), basketPov:+ib0.basketPov.toFixed(1), basketPovGross:+ib0.basketPovGross.toFixed(1),
    distress:d0*100, ep:extremePovertyOf(d0,d0,'year0').total};  /* v4.18: unrounded, for the overlay's parity checks */
  /* v4.17: recessions (NEEC note 5). p.shock was silently ignored before this release. */
  var recPath = p.shock ? buildRecessionPath(p.years, seed) : null;
  RNG = mulberry32(seed);
  var aWealth = [], aBlei = [];
  for (var yr = 0; yr < p.years; yr++){
    runYear(agents, yr, p, recPath ? recPath[yr] : {active:false, incomeMultiplier:1.0, yearsLeft:0});
    var m = calcMetrics(agents, p.ccoOn, p.pth);
    var bMed = calcMedianBLEI(agents, p);
    aWealth.push(Math.round(m.med));
    aBlei.push(Math.round(bMed));
  }
  var finalM = calcMetrics(agents, p.ccoOn, p.pth);
  var stab = structuralStability(aWealth, aBlei);
  var top = (p.ccoOn && p.ptf) ? 'Flourishing' : 'Comfortable';
  var bMain = bleiMetrics(agents, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf, top);
  var floor = CFG.WEALTH_FLOOR;
  var atFloor = agents.filter(function(a){ return a.wealth <= floor + 1e-6; }).length;
  var ib = incomeBasketMetrics(agents);
  var dEnd = housingDistressOf(agents), ep = extremePovertyOf(dEnd, d0, p);  /* v4.18 */
  function dShare(ag){ return ag.length ? housingDistressOf(ag)*100 : null; }
  return {
    pov: +(finalM.pov*100).toFixed(1),
    gini: +finalM.gini.toFixed(3),
    wealth: Math.round(finalM.med),
    p10: Math.round(finalM.p10),
    p90: Math.round(finalM.p90),
    bleiMed: Math.round(bMain.med),
    bleiPovPct: +((bMain.tc[0]+bMain.tc[1])/bMain.n*100).toFixed(1),
    pctFlourishing: +bMain.pctF.toFixed(1),
    avgEDC: +(bMain.avgEDC*100).toFixed(1),
    stab: +(stab*100).toFixed(1),
    fracAtFloor: atFloor/agents.length,
    medianPinned: Math.round(finalM.med) === floor,
    incPov: +ib.incPov.toFixed(1),            /* v4.17 */
    incPovExt: +ib.incPovExt.toFixed(1),
    basketPov: +ib.basketPov.toFixed(1),      /* v4.17 */
    basketPovGross: +ib.basketPovGross.toFixed(1),
    yearZero: yearZero,                       /* v4.17 */
    epTotal: ep.total, epEcon: ep.econ, epSmi: ep.smi, epVol: ep.vol,   /* v4.18: percentages, unrounded */
    distress: dEnd*100, distressY0: d0*100, wz: ep.wz,
    distressPart: dShare(agents.filter(function(a){ return a.inCCO; })), distressNonPart: dShare(agents.filter(function(a){ return !a.inCCO; })),
    recessionYears: recPath ? recPath.filter(function(r){ return r.active; }).length : 0
  };
}

var FULL_INTEGRATION = {
  bu:1200, maxOct:6, expiry:1, tax:0.12, maxMult:9,
  nAgents:500, partRate:0.78, years:20,
  ptfShare:0.18, pthUptake:0.20, szhCoh:0.72, cipDemo:0.65,
  phi:true, ptf:true, pth:true, szh:true, cip:true,
  shock:false, automation:false, inflRate:0, ccoOn:true, ptfCap:false
};
var BASELINE = {
  bu:0, maxOct:1, expiry:1, tax:0, maxMult:1,
  nAgents:500, partRate:0, years:20,
  ptfShare:0, pthUptake:0, szhCoh:0, cipDemo:0,
  phi:false, ptf:false, pth:false, szh:false, cip:false,
  shock:false, automation:false, inflRate:0.03, ccoOn:false, ptfCap:false
};

/* Bug fix (found during a Claude session's v4.10 audit, Sep 2026): this line previously
 * read `module.exports = { CFG, mulberry32, runScenario, FULL_INTEGRATION, BASELINE };` —
 * a full reassignment of module.exports, which silently discarded the
 * calcBLEIComponents/runScenarioWithComponents properties set on it near the top of this
 * file (lines ~279-280). Confirmed via `require('./harness.js').calcBLEIComponents` ===
 * undefined before this fix. The CLI's own `blei-components` mode was unaffected (it calls
 * runScenarioWithComponents() as a local function reference within this same file, not via
 * module.exports), so this bug was invisible to anyone only ever running harness.js
 * directly — it would only have bitten a future session or contributor trying to
 * `require()` this file's BLEI-components-checking capability from another script, exactly
 * as this file's own top-of-file comment describes it being "added post-hoc to check the
 * 'benefitDays line invisible in the chart' report." Object.assign onto the existing
 * exports object, rather than replacing it, so both assignment styles compose correctly
 * regardless of which comes first in the file. */
/* v4.17: the two stress presets, mirroring index.html's PRESETS.stress and the new
 * PRESETS.adverse (NEEC maintainers' note 6). STRESS_TEST mixes an adverse environment
 * (recessions, 2% inflation, AI automation) with weaker settings (40% participation, $900 BU,
 * lower PTF/PTH/SZH/CIP); ADVERSE_REFERENCE applies the same environment to the unchanged
 * Full Integration settings, which is what a stress criterion should test. */
var STRESS_TEST = {
  bu:900, maxOct:4, expiry:1, tax:0.18, maxMult:6,
  nAgents:500, partRate:0.40, years:20,
  ptfShare:0.08, pthUptake:0.10, szhCoh:0.35, cipDemo:0.30,
  phi:true, ptf:true, pth:true, szh:true, cip:true,
  shock:true, automation:true, inflRate:0.02, ccoOn:true, ptfCap:false
};
var ADVERSE_REFERENCE = Object.assign({}, FULL_INTEGRATION, {shock:true, automation:true, inflRate:0.02});
/* v4.20: index.html's PRESETS.hiAI — Full Integration over 25 years with AI automation. */
var HIGH_AUTOMATION = Object.assign({}, FULL_INTEGRATION, {years:25, automation:true});
/* v4.20: this file's functions, in the shape unitSuite() expects. */
function unitTargets(){
  return {CFG:CFG, mulberry32:mulberry32, gamma:gamma, beta:beta, lognormal:lognormal, drawAutomationRisk:drawAutomationRisk,
    szhTheta:szhTheta, pthLiquidShare:pthLiquidShare, getTier:getTier, medianOf:medianOf, coeffVar:coeffVar, structuralStability:structuralStability,
    getRNG:function(){ return RNG; }, setRNG:function(r){ RNG = r; }};
}
/* v4.18: CCO Only exactly as simulate() builds pCCO for a given scenario — every CCO setting kept,
 * PTF/PTH/SZH/CIP off. */
function ccoOnlyFor(p){ return Object.assign({}, p, {ptfShare:0, pthUptake:0, szhCoh:0, cipDemo:0, ptf:false, pth:false, szh:false, cip:false}); }
var CCO_ONLY = ccoOnlyFor(FULL_INTEGRATION);
/* The Baseline as simulate() builds it for a given scenario's comparison: shocks and
 * automation follow the scenario, inflation stays at BASELINE_CPI_RATE unless matched. */
function baselineFor(p, matchInfl){ return Object.assign({}, BASELINE, {shock:!!p.shock, automation:!!p.automation, inflRate: matchInfl ? p.inflRate : CFG.BASELINE_CPI_RATE}); }

/* v4.17: per-year trajectory including year 0 and the participant split (NEEC note 4). */
function trajectory(p, seed, marks){
  RNG = mulberry32(seed + 700003);
  var agents = makeLatentPopulation(p.nAgents).map(function(lat){ return instantiateAgent(lat, p); });
  var recPath = p.shock ? buildRecessionPath(p.years, seed) : null;
  RNG = mulberry32(seed);
  function bp(ag){ if(!ag.length) return null; var b = bleiMetrics(ag, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf); return (b.tc[0]+b.tc[1])/b.n*100; }
  var out = {};
  function rec(y){
    var part = agents.filter(function(a){ return a.inCCO; }), np = agents.filter(function(a){ return !a.inCCO; });
    var ib = y === 0 ? incomeBasketYear0(agents) : incomeBasketMetrics(agents);
    out[y] = {pov: calcMetrics(agents).pov*100, bleiPov: bp(agents), bleiPovPart: bp(part), bleiPovNonPart: bp(np), basketPov: ib.basketPov, incPov: ib.incPov};
  }
  rec(0);
  for (var yr = 0; yr < p.years; yr++){
    runYear(agents, yr, p, recPath ? recPath[yr] : {active:false, incomeMultiplier:1.0, yearsLeft:0});
    if (marks.indexOf(yr+1) >= 0) rec(yr+1);
  }
  return out;
}

/* ─── v4.20: PURE-FUNCTION AND PROPERTY TESTS ─────────────────────────────
 * One suite, two targets. `node harness.js unit` runs it against this file's functions;
 * domtest.js Phase 8 runs the SAME suite against index.html's own functions inside the page.
 * This is the "pure-function tests" layer of CONTRIBUTING.md's v4.12 good-first-issue (a).
 *
 * F supplies the functions under test plus CFG and an RNG getter/setter (the samplers read a
 * global RNG). Functions F lacks are reported as skipped: povertyCDF, buildPrefixSum,
 * povertyGapAvg, checkDominance and tCritical95 exist only in index.html. Every sampler test
 * seeds its own mulberry32 stream and restores the caller's RNG before returning (the v4.16
 * rule for anything that reassigns the global). Tolerances are several standard errors wide;
 * the seeds are fixed, so the suite is deterministic. Returns [{name, pass, skipped, detail}].
 */
function unitSuite(F){
  var out = [], C = F.CFG, saved = F.getRNG();
  function t(name, needs, fn){
    for (var i = 0; i < needs.length; i++) if (typeof F[needs[i]] !== 'function'){ out.push({name:name, pass:true, skipped:true, detail:'skipped: ' + needs[i] + ' not supplied'}); return; }
    try { var r = fn(); out.push({name:name, pass:!!r.pass, skipped:false, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, skipped:false, detail:'threw: ' + e.message}); }
    finally { F.setRNG(saved); }
  }
  function seeded(s){ F.setRNG(F.mulberry32(s)); }
  function sample(fn, n){ var a = new Array(n); for (var i = 0; i < n; i++) a[i] = fn(); return a; }
  function mean(a){ var s = 0; for (var i = 0; i < a.length; i++) s += a[i]; return s/a.length; }
  function vari(a){ var m = mean(a), s = 0; for (var i = 0; i < a.length; i++) s += (a[i]-m)*(a[i]-m); return s/(a.length-1); }
  function near(x, y, tol){ return Math.abs(x - y) <= tol; }
  function r4(x){ return (+x).toFixed(4); }
  var N = 20000;

  t('mulberry32: golden values, reproducible, seed-dependent, in [0,1)', ['mulberry32'], function(){
    var a = F.mulberry32(42), b = F.mulberry32(42), c = F.mulberry32(43), gold = [0.6011037519201636, 0.44829055899754167, 0.8524657934904099];
    var g = [a(), a(), a()], same = true, diff = false, inRange = true, sum = 0;
    b(); b(); b();
    for (var i = 0; i < 100000; i++){ var x = a(), y = b(), z = c(); if (x !== y) same = false; if (x !== z) diff = true; if (!(x >= 0 && x < 1)) inRange = false; sum += x; }
    var goldOk = g[0] === gold[0] && g[1] === gold[1] && g[2] === gold[2];
    return {pass: goldOk && same && diff && inRange && near(sum/100000, 0.5, 0.005), detail:'first three (seed 42) ' + g.map(r4).join(', ') + '; mean of 100,000 ' + r4(sum/100000)};
  });
  t('gamma(1) is Exponential(1): mean and variance 1, not a constant (the v4.4 bug)', ['gamma','mulberry32'], function(){
    seeded(101); var a = sample(function(){ return F.gamma(1); }, N), m = mean(a), v = vari(a), distinct = {}, k = 0;
    for (var i = 0; i < 1000; i++){ if (!distinct[a[i]]){ distinct[a[i]] = 1; k++; } }
    return {pass: near(m, 1, 0.03) && near(v, 1, 0.06) && k > 990, detail:'mean ' + r4(m) + ', variance ' + r4(v) + ', distinct values in first 1,000: ' + k};
  });
  t('gamma(a): mean and variance a, for a = 6 and 0.5', ['gamma','mulberry32'], function(){
    seeded(102); var a6 = sample(function(){ return F.gamma(6); }, N); seeded(103); var ah = sample(function(){ return F.gamma(0.5); }, N);
    return {pass: near(mean(a6), 6, 0.12) && near(vari(a6), 6, 0.36) && near(mean(ah), 0.5, 0.02) && near(vari(ah), 0.5, 0.04),
      detail:'a=6: mean ' + r4(mean(a6)) + ' var ' + r4(vari(a6)) + '; a=0.5: mean ' + r4(mean(ah)) + ' var ' + r4(vari(ah))};
  });
  t('beta(a,b): mean a/(a+b) and support (0,1), for (2,5), (6,1), (1,6)', ['beta','mulberry32'], function(){
    var ok = true, d = [];
    [[2,5],[6,1],[1,6]].forEach(function(ab, j){
      seeded(110 + j); var s = sample(function(){ return F.beta(ab[0], ab[1]); }, N), m = mean(s), inS = s.every(function(x){ return x > 0 && x < 1; });
      if (!near(m, ab[0]/(ab[0]+ab[1]), 0.006) || !inS) ok = false; d.push('(' + ab + ') ' + r4(m));
    });
    return {pass: ok, detail: d.join('; ')};
  });
  t('lognormal(mu, sigma): median e^mu (wealth and wage draws)', ['lognormal','mulberry32'], function(){
    seeded(120); var w = sample(function(){ return F.lognormal(C.WEALTH_INIT_MU, C.WEALTH_INIT_SIGMA); }, N).sort(function(x,y){ return x-y; });
    seeded(121); var g = sample(function(){ return F.lognormal(3.5, 0.5); }, N).sort(function(x,y){ return x-y; });
    var mw = w[N/2], mg = g[N/2], ew = Math.exp(C.WEALTH_INIT_MU), eg = Math.exp(3.5);
    return {pass: Math.abs(mw/ew - 1) < 0.04 && Math.abs(mg/eg - 1) < 0.02, detail:'wealth median $' + Math.round(mw).toLocaleString() + ' (e^mu $' + Math.round(ew).toLocaleString() + '); wage median ' + mg.toFixed(2) + ' SIU (e^3.5 ' + eg.toFixed(2) + ')'};
  });
  t('drawAutomationRisk: two RNG draws per call (v4.20), in [0,1], mixture mean and share as CFG specifies', ['drawAutomationRisk','mulberry32'], function(){
    var calls = 0, base = F.mulberry32(130); F.setRNG(function(){ calls++; return base(); });
    var counts = {}, s = [];
    for (var i = 0; i < N; i++){ var before = calls; s.push(F.drawAutomationRisk()); counts[calls - before] = (counts[calls - before] || 0) + 1; }
    var pi = C.AUTO_HIGH_SHARE, a = C.AUTO_HIGH_A, b = C.AUTO_LOW_B;
    var mExp = pi*a/(a+1) + (1-pi)/(b+1), hiExp = pi*(1 - Math.pow(0.5, a)) + (1-pi)*Math.pow(0.5, b);
    var m = mean(s), hi = s.filter(function(x){ return x >= 0.5; }).length/N, inR = s.every(function(x){ return x >= 0 && x <= 1; });
    var two = Object.keys(counts).length === 1 && counts[2] === N;
    return {pass: two && inR && near(m, mExp, 0.008) && near(hi, hiExp, 0.012),
      detail:'draws per call ' + JSON.stringify(counts) + '; mean ' + r4(m) + ' (expected ' + r4(mExp) + '); share >= 0.5 ' + r4(hi) + ' (expected ' + r4(hiExp) + ')'};
  });
  t('szhTheta: zero below the threshold, linear to the cap, capped, monotone, NaN-safe', ['szhTheta'], function(){
    var mono = true, prev = -1;
    for (var c = 0; c <= 1.0001; c += 0.01){ var v = F.szhTheta(c); if (v < prev - 1e-12 || v < 0 || v > C.SZH_THETA_MAX + 1e-12) mono = false; prev = v; }
    var ok = F.szhTheta(NaN) === 0 && F.szhTheta(C.SZH_THETA_THRESHOLD - 0.01) === 0 && F.szhTheta(C.SZH_THETA_THRESHOLD) === 0 &&
      near(F.szhTheta(C.SZH_THETA_MAX_COH), C.SZH_THETA_MAX, 1e-12) && F.szhTheta(0.99) === C.SZH_THETA_MAX &&
      near(F.szhTheta((C.SZH_THETA_THRESHOLD + C.SZH_THETA_MAX_COH)/2), C.SZH_THETA_MAX/2, 1e-12);
    return {pass: ok && mono, detail:'theta(0.72) ' + r4(F.szhTheta(0.72)) + ', theta(0.90) ' + r4(F.szhTheta(0.90))};
  });
  t('pthLiquidShare: year-1 and mature endpoints, linear between, clamped, NaN-safe', ['pthLiquidShare'], function(){
    var Y = C.PTH_LIQUID_SHARE_MATURE_YR, mono = true, prev = -1;
    for (var k = 0; k <= 12; k += 0.5){ var v = F.pthLiquidShare(k); if (v < prev - 1e-12) mono = false; prev = v; }
    var ok = F.pthLiquidShare(1) === C.PTH_LIQUID_SHARE_YEAR1 && near(F.pthLiquidShare(Y), C.PTH_LIQUID_SHARE_YEAR5PLUS, 1e-12) && near(F.pthLiquidShare(40), C.PTH_LIQUID_SHARE_YEAR5PLUS, 1e-12) &&
      F.pthLiquidShare(0) === C.PTH_LIQUID_SHARE_YEAR1 && F.pthLiquidShare(NaN) === C.PTH_LIQUID_SHARE_YEAR1 &&
      near(F.pthLiquidShare((1 + Y)/2), (C.PTH_LIQUID_SHARE_YEAR1 + C.PTH_LIQUID_SHARE_YEAR5PLUS)/2, 1e-12);
    return {pass: ok && mono, detail:'1y ' + F.pthLiquidShare(1) + ', 3y ' + r4(F.pthLiquidShare(3)) + ', 5y+ ' + F.pthLiquidShare(5)};
  });
  t('getTier: every BLEI tier boundary is inclusive at its lower edge', ['getTier'], function(){
    var edges = [[0,'Crisis'],[C.BLEI_CRISIS_MAX - 1e-9,'Crisis'],[C.BLEI_CRISIS_MAX,'Precarious'],[C.BLEI_PRECARIOUS_MAX,'Threshold'],[C.BLEI_THRESHOLD_MAX,'Stable'],[C.BLEI_STABLE_MAX,'Secure'],[C.BLEI_SECURE_MAX,'Flourishing'],[1e6,'Flourishing']];
    var bad = edges.filter(function(e){ return F.getTier(e[0]).name !== e[1]; });
    return {pass: bad.length === 0 && F.getTier(1e6, 'Comfortable').name === 'Comfortable', detail: bad.length ? 'wrong at ' + bad.map(function(e){ return e[0]; }).join(', ') : edges.length + ' boundaries checked'};
  });
  t('medianOf: empty, odd, even, and the input left unsorted', ['medianOf'], function(){
    var arr = [4, 1, 3, 2], copy = arr.slice();
    return {pass: F.medianOf([]) === 0 && F.medianOf([3, 1, 2]) === 2 && F.medianOf(arr) === 2.5 && arr.join() === copy.join(), detail:'[] 0, [3,1,2] 2, [4,1,3,2] 2.5'};
  });
  t('coeffVar and structuralStability: degenerate cases, bounds, and ordering', ['coeffVar','structuralStability'], function(){
    var flat = [5,5,5,5,5,5,5,5], steady = [100,101,102,103,104,105,106,107], wild = [100,300,50,400,20,500,10,600];
    var sFlat = F.structuralStability(flat, flat), sSteady = F.structuralStability(steady, steady), sWild = F.structuralStability(wild, wild);
    var ok = F.coeffVar([7]) === 0 && F.coeffVar([-1, 1]) === 0 && F.coeffVar(flat) === 0 && sFlat === 0.99 && sWild >= 0 && sWild < sSteady && sSteady <= 0.99;
    return {pass: ok, detail:'flat ' + sFlat + ', steady ' + r4(sSteady) + ', volatile ' + r4(sWild)};
  });
  t('povertyCDF: strict "below" count, empty and out-of-range thresholds', ['povertyCDF'], function(){
    var s = [1, 2, 3, 4];
    return {pass: F.povertyCDF([], 5) === 0 && F.povertyCDF(s, 3) === 50 && F.povertyCDF(s, 0) === 0 && F.povertyCDF(s, 99) === 100 && F.povertyCDF([2,2,2,2], 2) === 0, detail:'[1,2,3,4] below 3 = 50%'};
  });
  t('povertyGapAvg: equals a brute-force mean shortfall on 400 random arrays (duplicates, negative lines)', ['buildPrefixSum','povertyGapAvg','mulberry32'], function(){
    var R = F.mulberry32(140), worst = 0;
    for (var k = 0; k < 400; k++){
      var n = 1 + Math.floor(R()*60), a = [];
      for (var i = 0; i < n; i++) a.push(R() < 0.3 ? -10000 : Math.round((R() - 0.2)*100000));
      a.sort(function(x,y){ return x-y; });
      var P = F.buildPrefixSum(a);
      [-20000, -10000, 0, 25000, 60000, R()*80000 - 20000].forEach(function(th){
        var brute = 0; for (var j = 0; j < n; j++) brute += Math.max(0, th - a[j]); brute /= n;
        worst = Math.max(worst, Math.abs(brute - F.povertyGapAvg(a, P, th)));
      });
    }
    return {pass: worst < 1e-6 && F.povertyGapAvg([], [0], 5) === 0, detail:'largest absolute difference ' + worst.toExponential(2)};
  });
  t('checkDominance: identical, each direction, a crossing, and sub-epsilon noise', ['checkDominance'], function(){
    var L = ['a','b','c','d'];
    var cases = [[[1,2,3,4],[1,2,3,4],'identical'],[[1,1,2,3],[1,2,3,4],'a_dominates'],[[2,3,4,5],[1,2,3,4],'b_dominates'],[[1,3,2,5],[2,2,3,4],'cross'],[[1,2,3,4+1e-12],[1,2,3,4],'identical']];
    var bad = cases.filter(function(c){ return F.checkDominance(L, c[0], c[1]).relation !== c[2]; });
    var cross = F.checkDominance(L, [1,3,2,5], [2,2,3,4]);
    return {pass: bad.length === 0 && cross.crossLabel === 'b', detail: bad.length ? bad.length + ' wrong' : '5 cases; crossing found at "' + cross.crossLabel + '"'};
  });
  t('tCritical95: table values, interpolation, the 1.96 limit, non-increasing in df', ['tCritical95'], function(){
    var mono = true, prev = Infinity;
    for (var df = 1; df <= 200; df++){ var v = F.tCritical95(df); if (v > prev + 1e-12) mono = false; prev = v; }
    return {pass: F.tCritical95(1) === 12.706 && F.tCritical95(9) === 2.262 && near(F.tCritical95(49), 2.021 + (2.009 - 2.021)*0.9, 1e-9) && F.tCritical95(500) === 1.96 && F.tCritical95(0) === 12.706 && mono,
      detail:'df 9 (Run 10x) ' + F.tCritical95(9) + ', df 49 (Run 50x) ' + r4(F.tCritical95(49)) + ', df 500 ' + F.tCritical95(500)};
  });
  F.setRNG(saved);
  return out;
}

Object.assign(module.exports, { runYear, makeLatentPopulation, instantiateAgent, agentBLEI, housingDistressOf, housingDistressYear0, buildRecessionPath, calcMetrics, bleiMetrics, setRNG:function(r){RNG=r;}, getRNG:function(){return RNG;}, unitSuite, unitTargets, HIGH_AUTOMATION, setAutomationSampler:function(legacy){AUTOMATION_SAMPLER_LEGACY=!!legacy;}, setReliefPriceLegacy:function(v){RELIEF_PRICE_LEGACY=!!v;}, shockRun, shockStudy, stabRuleText, setStabSwitches:function(n,flat){BU_ALLOCATIONS_PER_YEAR=n;CCO_RELIEF_FLAT=flat;}, CFG, mulberry32, runScenario, trajectory, baselineFor, ccoOnlyFor, extremePovertyOf, FULL_INTEGRATION, BASELINE, CCO_ONLY, STRESS_TEST, ADVERSE_REFERENCE });

function stabRuleText(p){
  if(!p.stab)return 'off';
  return (p.stabSev?'+'+(+p.stabK).toFixed(1)+'% BU per 1% income loss':'×'+(+p.stabMult).toFixed(2)+' BU')+' when income falls ≥'+Math.round((p.stabThresh||0)*100)+'%'+
    (p.stabSusp?', expiry suspended':'')+(p.emerg?', emergency enrollment '+Math.round((p.emergTakeup||0)*100)+'%':'');
}
/* One paired run: distress by group and year, recession flags, BU issued. */
function shockRun(p,seed){
  RNG=mulberry32(seed+700003);
  var ag=makeLatentPopulation(p.nAgents).map(function(l){return instantiateAgent(l,p);});
  var d0=housingDistressYear0(ag);
  var rp=p.shock?buildRecessionPath(p.years,seed):null;
  RNG=mulberry32(seed);
  var part=ag.filter(function(a){return a.inCCO;}),non=ag.filter(function(a){return !a.inCCO;});
  var o={dPart:[],dNon:[],dAll:[],rec:[],d0:d0,base:0,extra:0};
  for(var y=0;y<p.years;y++){
    var rs=rp?rp[y]:{active:false,incomeMultiplier:1.0,yearsLeft:0};
    var r=runYear(ag,y,p,rs);
    o.rec.push(!!rs.active);
    o.dPart.push(part.length?housingDistressOf(part):0);o.dNon.push(non.length?housingDistressOf(non):0);o.dAll.push(housingDistressOf(ag));
    if(p.ccoOn&&p.bu>0){o.base+=p.bu*part.length;o.extra+=p.bu*r.colaF*(r.stabM-1)*part.length;}
    o.extra+=(r.emergN||0)*(r.buEff||0);
  }
  return o;
}
function newShockAcc(){return{xp:0,xn:0,xa:0,xEP:0,n:0,base:0,extra:0};}
function addShockAcc(A,calm,r){
  r.rec.forEach(function(on,y){
    if(!on)return;
    var da=r.dAll[y]-calm.dAll[y];
    A.xp+=r.dPart[y]-calm.dPart[y];A.xn+=r.dNon[y]-calm.dNon[y];A.xa+=da;
    A.xEP+=calm.d0>0?CFG.EP_Y0_RATE*(1-CFG.EP_SMI_SHARE-CFG.EP_VOL_SHARE)*da/calm.d0:0;
    A.n++;
  });
  A.base+=r.base;A.extra+=r.extra;
}
/* Means per recession-year: excess housing distress (pp) and excess expected extreme poverty
 * (per 10,000; the v4.18 overlay's economic pathway, which scales with distress). */
function shockSummary(A){
  var n=Math.max(1,A.n);
  return{partPP:A.xp/n*100,nonPartPP:A.xn/n*100,allPP:A.xa/n*100,extremePer10k:A.xEP/n*1e4,
    extraPctOfBase:A.base>0?A.extra/A.base*100:0,recessionYears:A.n};
}
function shockArmNone(P){return Object.assign({},P,{stab:false});}
function shockArmHub(P){return Object.assign({},P,{stab:true,stabSev:false,stabMult:CFG.STAB_HUB_MULT,stabThresh:CFG.STAB_HUB_THRESH,stabSusp:false,emerg:false});}
function shockArmFixed(P,m){return Object.assign({},P,{stab:true,stabSev:false,stabMult:m,stabSusp:false,emerg:false});}
/* Shock-neutral search (participants): false position on the multiplier, starting from
 * ×1 (no stabilizer) and ×2, widening to ×3 and then ×4 (the slider's maximum) if needed,
 * then up to five refinement passes, bisecting whenever two land on the same side, until the
 * bracket is within ×0.025. The result is rounded to the slider's ×0.05 step. Returns the next
 * multiplier to evaluate, or null when done. */
function shockNextM(S){
  var pts=S.pts;
  if(pts[0].f<=0){S.result={m:1,reached:true};return null;}
  var hi=null,lo=null;pts.forEach(function(q){if(q.f<=0){if(!hi||q.m<hi.m)hi=q;}else{if(!lo||q.m>lo.m)lo=q;}});
  if(!hi){if(lo.m>=CFG.STAB_MULT_MAX){S.result={m:CFG.STAB_MULT_MAX,reached:false};return null;}return lo.m<2?2:lo.m<3?3:CFG.STAB_MULT_MAX;}
  var est=lo.m+(hi.m-lo.m)*lo.f/(lo.f-hi.f);
  if(pts.length>=7||hi.m-lo.m<=0.025){S.result={m:Math.round(est*20)/20,reached:true};return null;}
  var n=pts.length;
  if(n>=4&&(pts[n-1].f>0)===(pts[n-2].f>0))est=(lo.m+hi.m)/2;  // two refinements on one side: bisect so the bracket keeps shrinking
  return Math.round(est*1000)/1000;
}
/* Synchronous twin of index.html's runShockStudy(): same arms, same seeds, same search. */
function shockStudy(P,N){
  var calm=[],acc={none:newShockAcc(),hub:newShockAcc(),yours:P.stab?newShockAcc():null},S={pts:[]},s;
  for(s=1;s<=N;s++){
    var c=shockRun(Object.assign({},P,{shock:false}),s);calm[s]=c;
    addShockAcc(acc.none,c,shockRun(shockArmNone(P),s));
    addShockAcc(acc.hub,c,shockRun(shockArmHub(P),s));
    if(acc.yours)addShockAcc(acc.yours,c,shockRun(P,s));
  }
  S.pts.push({m:1,f:shockSummary(acc.none).partPP});
  for(var m=shockNextM(S);m!==null;m=shockNextM(S)){
    var accm=newShockAcc();
    for(s=1;s<=N;s++)addShockAcc(accm,calm[s],shockRun(shockArmFixed(P,m),s));
    S.pts.push({m:m,f:shockSummary(accm).partPP});
  }
  return{N:N,rule:stabRuleText(P),none:shockSummary(acc.none),hub:shockSummary(acc.hub),yours:acc.yours?shockSummary(acc.yours):null,
    neutral:S.result,points:S.pts.map(function(q){return{m:q.m,partPP:q.f};})};
}
/* Study-only rules the engine does not ship (timing variants, a matched-budget permanent
 * raise): p.bu is multiplied outside runYear(), which the engine's declared rule reproduces
 * exactly (checked in the stabilizer mode). */
function shockRunWith(p,seed,multFor){
  RNG=mulberry32(seed+700003);
  var ag=makeLatentPopulation(p.nAgents).map(function(l){return instantiateAgent(l,p);});
  var d0=housingDistressYear0(ag),rp=p.shock?buildRecessionPath(p.years,seed):null;
  RNG=mulberry32(seed);
  var part=ag.filter(function(a){return a.inCCO;}),non=ag.filter(function(a){return !a.inCCO;});
  var o={dPart:[],dNon:[],dAll:[],rec:[],d0:d0,base:0,extra:0};
  for(var y=0;y<p.years;y++){
    var rs=rp?rp[y]:{active:false,incomeMultiplier:1.0,yearsLeft:0},m=multFor(y,rp);
    runYear(ag,y,m===1?p:Object.assign({},p,{bu:p.bu*m}),rs);
    o.rec.push(!!rs.active);o.dPart.push(housingDistressOf(part));o.dNon.push(housingDistressOf(non));o.dAll.push(housingDistressOf(ag));
    o.base+=p.bu*part.length;o.extra+=p.bu*(m-1)*part.length;
  }
  return o;
}

/* ─── Session 2: the next round's default rule (D1) and the A2 issuance and price module ───────────────
 * NEXT_ROUND: D1, adopted Sep 26 (session-1-handoff.md): consume 0.9 of ALL cash surplus; basket consumption is financed
 * only down to the floor, and a write-off at the floor is reported as unmet need. It is a profile, not a new default for the
 * global switches, so validate/unit/domtest keep testing index.html; the next round's modes apply it (`price`, and
 * `ledger --next`). Setting the share back to 0 restores v4.21. nextRoundPreset(): D6, the hub's 5% COLA trigger, for any
 * preset with CCO on. */
var NEXT_ROUND = {SURPLUS_CONSUMPTION_SHARE:0.9, SURPLUS_CONSUMPTION_BASE:'cash'};
function applyRule(r){ var old = {SURPLUS_CONSUMPTION_SHARE:SURPLUS_CONSUMPTION_SHARE, SURPLUS_CONSUMPTION_BASE:SURPLUS_CONSUMPTION_BASE};
  SURPLUS_CONSUMPTION_SHARE = r.SURPLUS_CONSUMPTION_SHARE; SURPLUS_CONSUMPTION_BASE = r.SURPLUS_CONSUMPTION_BASE; return old; }
function nextRoundPreset(p){ return p.ccoOn ? Object.assign({}, p, {cola:true, colaThresh:CFG.COLA_HUB_THRESH}) : Object.assign({}, p); }
/* A2 defaults. Sources and status in session-2-handoff.md; nothing here is tuned to a target.
 *  a        additionality share: the part of conversion-created primary currency matched by new output. Swept [0,1].
 *  lamG     P_G pass-through of unmatched new money, as a share of that year's aggregate cash income: 1 = the quantity-
 *           theory benchmark (velocity 1, matched output permanent). A logged placeholder, swept 0.25-1.
 *  theta    P_E: each essentials price rises by theta x the % gap between effective essentials demand and supply.
 *           housing 0.6: sourced range 0 (Eriksen & Ross 2015, no overall rent effect) to 0.78 (Fack 2006), with Gibbons &
 *           Manning 2006 at 0.60-0.67. food 0: Cunha, De Giorgi & Jayachandran 2019 find cash transfers raise food prices
 *           negligibly where villages are tied to outside markets. medical 0.5: an unsourced, logged placeholder.
 *  ptfCap   the share of PTF's cost reduction that is added real capacity rather than a transferred margin (supply side of
 *           P_E). No evidence yet, so 0 (the plan's rule); swept.
 *  pthUnmatched  PTH appreciation credited to liquid wealth has no counterparty: counted as unmatched new money (a = 0).
 *  floorUnmatched  N5: false = a floor write-off is unmet need, not money; true = the plan's original treatment.
 *  aw       N7: share of program-induced raises (octave, CIP) matched by output. 1 by default. Session 3 (S3-1): the unmatched
 *           part enters U as the year's CHANGE in the aggregate premium (measured before the income shock): a raise paid from
 *           revenue with no added output passes through to prices once, as a level shift. awLevel: true restores session 2's
 *           reading, which counts the whole premium as new money every year (the raise re-created as currency each year).
 *  wIdx     wage indexation to P_G (0 = the engine's nominal drift).
 *  pgOnE    general (monetary) inflation raises essentials prices too. The plan's text reprices essentials by P_E only;
 *           applying P_G to them as well is the conservative reading (flagged in the hand-off).
 *  lines    D2: 'deflate' (both poverty lines move with the price index) or 'nominal'.
 *  supply   essentials supply (N11, new in session 2). 'capacity' (default; the plan's "baseline growth"): capacity is the
 *           matched Baseline's first-year effective demand, growing at gS a year (0: the model has a fixed population and a
 *           fixed real basket), and prices move only with the demand the program adds ABOVE that capacity, net of any
 *           excess the Baseline itself has. 'baseline': capacity is the matched Baseline's demand in the same year. That
 *           reading shrinks capacity whenever the Baseline impoverishes (Adverse: to about half by year 19) and is kept
 *           as an upper bound. */
var PM_DEFAULTS = {a:0, lamG:1, theta:{food:0, housing:0.6, medical:0.5}, ptfCap:0, pthUnmatched:true, floorUnmatched:false,
  aw:1, awLevel:false, wIdx:0, pgOnE:true, noDamp:false, essMatched:false, lines:'deflate', supply:'capacity', gS:0};
function pmOpts(o){ o = o || {}; var r = Object.assign({}, PM_DEFAULTS, o); r.theta = Object.assign({}, PM_DEFAULTS.theta, o.theta || {}); return r; }
/* Pure price rules (tested by priceUnitSuite). */
function pmEssLevel(D, S, cap, theta){ var s = S*(1 + cap); return s > 0 ? Math.max(0, 1 + theta*(D - s)/s) : 1; }
function pmGenStep(PG, U, Y, lam){ return Y > 0 ? PG*(1 + lam*U/Y) : PG; }
function pmBasketIdx(comp){ var b = 1; CFG.BASKET_KEYS.forEach(function(k){ b += CFG.BASKET[k]*(comp[k] - 1); }); return b; }  /* 1 + weighted deviations: exactly 1 when no price moved */
function newPMAcc(){ return {n:0, essD:0, unmet:0, basketOwn:0, unmetN:0, Y:0, ptfN:0, conv:0, pthLiq:0, wageBonus:0, wageBonusNS:0}; }
/* One run with the price module. S: the supply path for effective essentials demand (per-agent share of basket consumed,
 * by year), normally the matched Baseline's own path under the same rule; null holds P_E at 1. Draws exactly as
 * runScenario() does. Returns the demand path D (for use as S), the price path, and end-of-run metrics under D2. */
function priceRun(p, seed, o, S){
  o = pmOpts(o);
  var CALM0 = {active:false, incomeMultiplier:1.0, yearsLeft:0};
  RNG = mulberry32(seed + 700003);
  var agents = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
  var recPath = p.shock ? buildRecessionPath(p.years, seed) : null;
  RNG = mulberry32(seed);
  var comp = {}; CFG.BASKET_KEYS.forEach(function(k){ comp[k] = 1; });
  PRICE = {bIdx:1, comp:comp, piG:0, colaLevel:1, lastFull:1, wIdx:o.wIdx, noDamp:o.noDamp, acc:null};
  var PG = 1, D = [], path = [], tot = newPMAcc(), wbPrev = 0, labAcc = null;
  THETA_DENS = null;
  if (o.labor){ labAcc = newLabAcc(); LABOR = Object.assign({}, o.labor, {acc:labAcc}); }  /* session 5: the joint price and labor run */
  try {
    for (var yr = 0; yr < p.years; yr++){
      PRICE.acc = newPMAcc();
      runYear(agents, yr, p, recPath ? recPath[yr] : CALM0);
      var A = PRICE.acc, d = A.n ? A.essD/A.n : 1; D.push(d);
      Object.keys(tot).forEach(function(k){ tot[k] += A[k]; });
      var wbInc = A.wageBonusNS - wbPrev; wbPrev = A.wageBonusNS;  /* session 3 (S3-1): an unmatched raise is a cost-push level shift, so only the year's change in the premium is new */
      var U = (1 - o.a)*A.conv + (o.pthUnmatched ? A.pthLiq : 0) + (o.floorUnmatched ? A.unmet : 0) + (1 - o.aw)*(o.awLevel ? A.wageBonus : wbInc);
      var PGn = pmGenStep(PG, U, A.Y, o.lamG), capShare = o.ptfCap*(A.n ? A.ptfN/A.n : 0), PE = {};
      CFG.ESSENTIALS.forEach(function(k){
        var cut = !p.ptf ? 0 : PTF_MODE === 'shipped' ? (p.szh ? 0.12 + p.szhCoh*0.04 : 0.12) : (k === 'food' ? PTF_FOOD_CUT[PTF_MODE] : 0);
        if (!S || o.essMatched){ PE[k] = 1; return; }
        var sRef = o.supply === 'baseline' ? S[yr] : S[0]*Math.pow(1 + o.gS, yr);
        var dEff = o.supply === 'baseline' ? d : sRef + Math.max(0, d - sRef) - Math.max(0, S[yr] - sRef);
        PE[k] = pmEssLevel(dEff, sRef, capShare*cut, o.theta[k]);
      });
      path.push({bIdx:PRICE.bIdx, PG:PG, PEh:PRICE.comp.housing/(o.pgOnE ? PG : 1), d:d, U:U, Y:A.Y, conv:A.conv, unmet:A.unmet, basketOwn:A.basketOwn, unmetN:A.unmetN/A.n, colaLevel:PRICE.colaLevel});
      PRICE.piG = PGn/PG - 1; PG = PGn;
      CFG.BASKET_KEYS.forEach(function(k){ comp[k] = CFG.ESSENTIALS.indexOf(k) >= 0 ? PE[k]*(o.pgOnE ? PG : 1) : PG; });
      PRICE.bIdx = pmBasketIdx(comp);
    }
  } finally { PRICE = null; if (labAcc) LABOR = null; }
  var T = p.years, full = agents[0].yrBasketUSD/CFG.LIVING_WAGE_ANNUAL, lineF = o.lines === 'nominal' ? 1 : full, n = agents.length;
  var ws = agents.map(function(a){ return a.wealth; }), pov = 0, bpov = 0;
  ws.forEach(function(w){ if (w < CFG.POVERTY_LINE*lineF) pov++; });
  agents.forEach(function(a){ if (agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lineF < CFG.BLEI_PRECARIOUS_MAX) bpov++; });
  var ib = incomeBasketMetrics(agents), bI = path[T-1].bIdx, mx = 0;
  for (var t = 1; t < T; t++) mx = Math.max(mx, path[t].bIdx/path[t-1].bIdx - 1);
  var colaLast = path[T-1].colaLevel;
  return {D:D, path:path, agents:agents, tot:tot, res:{
    endoAnn: Math.pow(bI, 1/(T - 1)) - 1, endoMax: mx, endoIdx: bI, PG: path[T-1].PG, PEh: path[T-1].PEh, fullIdx: full,
    pov: pov/n*100, bleiPov: bpov/n*100, basketPov: ib.basketPov, medWealthReal: medianOf(ws)/full,
    unmetShare: tot.basketOwn > 0 ? tot.unmet/tot.basketOwn : 0, unmetYears: tot.unmetN/tot.n, convShare: tot.Y > 0 ? tot.conv/tot.Y : 0,
    buReal: p.bu*(p.cola ? colaLast : 1)/full,
    dE: labAcc && labAcc.E0 > 0 ? (labAcc.E - labAcc.E0)/labAcc.E0 : 0, labE: labAcc ? labAcc.E/Math.max(1, labAcc.n) : 0}};
}
/* Paired study: for each seed, the matched Baseline under the same rule gives the supply path; the scenario is then run at
 * every option set in `grid` against that path. Returns the per-option mean of each metric. */
function priceStudy(p, N, grid, base){
  var bp = baselineFor(p, true), out = grid.map(function(){ return {}; });
  for (var sd = 1; sd <= N; sd++){
    var S = priceRun(bp, sd, base || {}, null).D;
    grid.forEach(function(g, i){ var r = priceRun(p, sd, Object.assign({}, base || {}, g), S).res;
      Object.keys(r).forEach(function(k){ out[i][k] = (out[i][k] || 0) + r[k]/N; }); });
  }
  return out;
}
/* Breakeven additionality: the smallest a on the grid's linear interpolation at which mean endogenous inflation is at or
 * below tol. null if even a = 1 exceeds it (the essentials channel or other unmatched flows alone do). */
function breakevenA(as, infl, tol){
  if (infl[infl.length-1] > tol) return null;
  if (infl[0] <= tol) return as[0];
  for (var i = 1; i < as.length; i++) if (infl[i] <= tol){ var f = (infl[i-1] - tol)/(infl[i-1] - infl[i]); return as[i-1] + f*(as[i] - as[i-1]); }
  return null;
}
/* The unit tests the plan requires for the price rule, plus accounting checks on the framework model. Harness-only (the
 * page has none of these functions), so `unit` runs this suite after unitSuite(). Each test restores every switch. */
function priceUnitSuite(){
  var out = [];
  function t(name, fn){ var sv = {cm:CONVERSION_MODEL, pm:PTF_MODE, r:applyRule(NEXT_ROUND)};
    try { var r = fn(); out.push({name:name, pass:!!r.pass, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, detail:'threw: ' + e.message}); }
    finally { CONVERSION_MODEL = sv.cm; PTF_MODE = sv.pm; applyRule(sv.r); PRICE = null; LEDGER = null; } }
  function plainAgents(p, seed){ RNG = mulberry32(seed + 700003); var ag = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
    var rp = p.shock ? buildRecessionPath(p.years, seed) : null; RNG = mulberry32(seed);
    for (var y = 0; y < p.years; y++) runYear(ag, y, p, rp ? rp[y] : {active:false, incomeMultiplier:1.0, yearsLeft:0}); return ag; }
  function sameAgents(x, y){ return x.every(function(a, i){ return a.wealth === y[i].wealth && a.wage === y[i].wage && a.yrCostUSD === y[i].yrCostUSD; }); }
  var FI = nextRoundPreset(FULL_INTEGRATION), BA = baselineFor(FULL_INTEGRATION, true);
  t('pure rules: no gap and no new money leave prices unchanged; both rise with the gap and with unmatched money', function(){
    var ok = pmEssLevel(0.9, 0.9, 0, 0.6) === 1 && pmEssLevel(0.75, 0.5, 0.5, 0.6) === 1 && pmGenStep(1.2, 0, 1e6, 1) === 1.2 && pmGenStep(1, 5, 0, 1) === 1;
    var prevE = 0, prevG = 0, mono = true;
    for (var x = 0; x <= 20; x++){ var e = pmEssLevel(0.8 + x*0.01, 0.9, 0, 0.6), g = pmGenStep(1, x*1000, 1e6, 1); if (e < prevE || g < prevG) mono = false; prevE = e; prevG = g; }
    return {pass: ok && mono, detail: 'P_E at a 10% gap, theta 0.6: ' + pmEssLevel(0.99, 0.9, 0, 0.6).toFixed(4) + '; P_G step at U/Y = 2%: ' + pmGenStep(1, 2e4, 1e6, 1).toFixed(4)};
  });
  t('zero issuance: the Baseline through the price module never moves the index and is bit-identical to the run without it (seeds 1-3)', function(){
    var ok = true, d = [];
    for (var s = 1; s <= 3; s++){ var r = priceRun(BA, s, {}, null), still = r.path.every(function(x){ return x.bIdx === 1 && x.PG === 1; });
      if (!still || !sameAgents(r.agents, plainAgents(BA, s))) ok = false; d.push(r.res.endoIdx); }
    return {pass: ok, detail: 'final endogenous index ' + d.join(', ')};
  });
  t('fully matched (a = 1, PTH appreciation matched, essentials supply matched): Full Integration never moves the index and is bit-identical to the run without it, in both conversion models', function(){
    var ok = true, d = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm;
      var r = priceRun(FI, 1, {a:1, pthUnmatched:false, essMatched:true}, null), still = r.path.every(function(x){ return x.bIdx === 1; });
      if (!still || !sameAgents(r.agents, plainAgents(FI, 1))) ok = false; d.push(cm + ' ' + r.res.endoIdx + ' (conversion ' + (r.res.convShare*100).toFixed(1) + '% of income)'); });
    return {pass: ok, detail: d.join('; ')};
  });
  t('monotone: endogenous inflation falls as additionality rises, a = 0 to 1 (Full Integration, seed 1, both models)', function(){
    var ok = true, d = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; var S = priceRun(BA, 1, {}, null).D, prev = Infinity, v = [];
      [0, 0.25, 0.5, 0.75, 1].forEach(function(a){ var e = priceRun(FI, 1, {a:a}, S).res.endoAnn; if (e > prev + 1e-15) ok = false; prev = e; v.push((e*100).toFixed(3)); });
      if (!(+v[0] > +v[4])) ok = false; d.push(cm + ': ' + v.join(' > ') + ' % a year'); });
    return {pass: ok, detail: d.join('; ')};
  });
  t('framework accounting: every BU of the budget is spent or expires; directed = expired x share; each year\'s business premium is paid out in full the next year', function(){
    CONVERSION_MODEL = 'framework'; LEDGER = newLedger(); RNG = mulberry32(700004);
    var ag = makeLatentPopulation(FI.nAgents).map(function(l){ return instantiateAgent(l, FI); }); RNG = mulberry32(1);
    for (var y = 0; y < FI.years; y++) runYear(ag, y, FI, {active:false, incomeMultiplier:1.0, yearsLeft:0});
    var Y = LEDGER.y, g = function(o, k){ return o[k] || 0; }, e1 = 0, e2 = 0, e3 = 0;
    for (y = 0; y < FI.years; y++){ e1 = Math.max(e1, Math.abs(g(Y[y],'fwBUSpent') + g(Y[y],'fwBUExpired') - g(Y[y],'fwBudget'))/g(Y[y],'fwBudget'));
      e2 = Math.max(e2, Math.abs(g(Y[y],'fwBUDirected') - FW.directedShare*g(Y[y],'fwBUExpired'))/Math.max(1, g(Y[y],'fwBUExpired')));
      if (y > 0) e3 = Math.max(e3, Math.abs(g(Y[y],'fwBizPayout') - g(Y[y-1],'fwBizPremium'))/Math.max(1, Math.abs(g(Y[y-1],'fwBizPremium')))); }
    return {pass: e1 < 1e-12 && e2 < 1e-12 && e3 < 1e-9, detail: 'max relative errors ' + [e1, e2, e3].map(function(x){ return x.toExponential(1); }).join(', ')};
  });
  t('switches inert at their defaults: PTF_MODE shipped, CONVERSION_MODEL engine, PRICE null give index.html\'s seed-42 Full Integration figures', function(){
    applyRule({SURPLUS_CONSUMPTION_SHARE:0, SURPLUS_CONSUMPTION_BASE:'wage'}); var r = runScenario(FULL_INTEGRATION, 42);
    return {pass: r.pov === 15.8 && r.wealth === 570661 && r.bleiMed === 1975, detail: r.pov + ' / ' + r.wealth + ' / ' + r.bleiMed};
  });
  /* Session 3: the sweep machinery. */
  t('breakeven search (session 3): finds the root of a known monotone curve, handles the none and any-a cases, and its interval covers the root', function(){
    function synth(f){ return function(a){ var n = 200, s = new Float64Array(n), m = 0, R = mulberry32(4242);
      for (var i = 0; i < n; i++){ s[i] = f(a) + (R() - 0.5)*0.002; m += s[i]; } return {a:a, n:n, s:{endoAnn:s}, m:{endoAnn:m/n}}; }; }
    var f1 = function(a){ return 0.05*(1 - a)*(1 - a) + 0.002; }, want = [1 - Math.sqrt(0.003/0.05), 1 - Math.sqrt(0.008/0.05)];
    var pts = {}, b5 = s3Breakeven(pts, 0.005, synth(f1)), b10 = s3Breakeven(pts, 0.010, synth(f1));
    var none = s3Breakeven({}, 0.005, synth(function(a){ return 0.006 + 0.01*(1 - a); })), any = s3Breakeven({}, 0.005, synth(function(a){ return 0.004*(1 - a); }));
    var ok = Math.abs(b5.be - want[0]) < 1e-3 && Math.abs(b10.be - want[1]) < 1e-3 && none.be === null && any.be === 0 && b5.ci[0] <= want[0] + 1e-3 && b5.ci[1] >= want[0] - 1e-3;
    return {pass: ok, detail: 'found ' + b5.be.toFixed(4) + ' and ' + b10.be.toFixed(4) + ' (true ' + want[0].toFixed(4) + ', ' + want[1].toFixed(4) + ') in ' + Object.keys(pts).length + ' points'};
  });
  t('sweep points (session 3): s3Point reproduces priceStudy exactly, and the cached Baseline supply path equals a fresh one (Full Integration, seeds 1-3, a = 0.9, both models)', function(){
    var ok = true, d = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm;
      var q = s3Point(FI, {}, 0.9, 3), r = priceStudy(FI, 3, [{a:0.9}], {})[0];
      ['endoAnn','pov','bleiPov','basketPov','unmetShare'].forEach(function(k){ if (Math.abs(q.m[k] - r[k]) > 1e-12*Math.max(1, Math.abs(r[k]))) ok = false; });
      for (var s = 1; s <= 3; s++){ var A = s3BaseS(FI, s), B = priceRun(baselineFor(FI, true), s, {}, null).D; if (A.length !== B.length || A.some(function(x, i){ return x !== B[i]; })) ok = false; }
      d.push(cm + ' ' + (q.m.endoAnn*100).toFixed(4) + ' = ' + (r.endoAnn*100).toFixed(4) + ' pt/yr'); });
    return {pass: ok, detail: d.join('; ')};
  });
  return out;
}

/* Session 2 exports, for scripts that drive the next round's modules (domtest.js does not use them). */
Object.assign(module.exports, { priceRun, priceStudy, breakevenA, priceUnitSuite, nextRoundPreset, applyRule, NEXT_ROUND, PM_DEFAULTS, FW, newLedger,
  setConversionModel:function(m){ CONVERSION_MODEL = m; }, setPtfMode:function(m){ PTF_MODE = m; }, setLedger:function(L){ LEDGER = L; } });

/* ─── Session 3 (Sep 26 2026; Duke assigns the version): A2 sweeps and the breakeven report ─────────────────
 * Harness-only, and nothing here changes a run: these functions only drive priceRun(). CRN makes the mean over a fixed
 * set of seeds a deterministic function of every input, so each point below is an exact mean, not a noisy estimate,
 * and breakeven additionality can be found by a bracketed secant search instead of a coarse grid.
 *  s3BaseS    the matched Baseline's effective-demand path for P_E (the supply side). The Baseline has no conversion,
 *             no PTH and no floor money under the adopted rules, so its prices never move and the path depends only on
 *             the seed, the environment and the consumption rule: cached.
 *  s3Point    per-seed results at one a (kept, for a bootstrap over seeds and the share of seeds above tolerance).
 *  s3Breakeven  the smallest a at which mean endogenous inflation is at or below tol: anchors at a = 1, 0 and 0.9,
 *             then secant steps inside the tightest bracket until it is 0.002 wide or an end is within 0.01 point of
 *             tol; the estimate interpolates the final bracket. 95% interval: 2,000 bootstrap resamples of the seeds at
 *             the two bracket points (linear inside the bracket, which is narrow).
 *  s3Config   one scenario under one sweep row (switches, preset overrides and module options), both tolerances. */
var S3_CACHE = {};
var S3_KEYS = ['endoAnn','endoMax','pov','bleiPov','basketPov','unmetShare','unmetYears','convShare','buReal','PG','medWealthReal','dE','labE'];
function s3BaseS(p, seed){
  var bp = baselineFor(p, true), k = JSON.stringify(bp) + '|' + SURPLUS_CONSUMPTION_SHARE + '|' + SURPLUS_CONSUMPTION_BASE + '|' + seed;
  if (!S3_CACHE[k]) S3_CACHE[k] = priceRun(bp, seed, {}, null).D;
  return S3_CACHE[k];
}
function s3Set(sw){ var sv = {cm:CONVERSION_MODEL, pm:PTF_MODE, fw:Object.assign({}, FW)};
  if (sw){ if (sw.cm) CONVERSION_MODEL = sw.cm; if (sw.ptfMode) PTF_MODE = sw.ptfMode; if (sw.fw) Object.assign(FW, sw.fw); }
  return sv; }
function s3Reset(sv){ CONVERSION_MODEL = sv.cm; PTF_MODE = sv.pm; Object.assign(FW, sv.fw); }
/* Per-seed results at one a. With wantRec and a shock preset, also pools the endogenous year-on-year rate by whether the
 * previous year was a recession year (prices respond to last year's flows, so a recession in year t shows in year t+1). */
function s3Point(P, opts, a, N, wantRec, noFeedback){
  var o = {a:a, n:N, s:{}, m:{}, rec:null};
  S3_KEYS.forEach(function(k){ o.s[k] = new Float64Array(N); });
  if (wantRec) o.rec = {post:0, postN:0, calm:0, calmN:0};
  for (var sd = 1; sd <= N; sd++){
    var r = priceRun(P, sd, Object.assign({}, opts, {a:a}), noFeedback ? null : s3BaseS(P, sd));
    S3_KEYS.forEach(function(k){ o.s[k][sd-1] = r.res[k]; });
    if (wantRec && P.shock){ var rp = buildRecessionPath(P.years, sd);
      for (var t = 1; t < P.years; t++){ var g = r.path[t].bIdx/r.path[t-1].bIdx - 1;
        if (rp[t-1].active){ o.rec.post += g; o.rec.postN++; } else { o.rec.calm += g; o.rec.calmN++; } } }
  }
  S3_KEYS.forEach(function(k){ var t = 0; for (var i = 0; i < N; i++) t += o.s[k][i]; o.m[k] = t/N; });
  return o;
}
function s3Boot(lo, hi, tol, B){
  var R = mulberry32(987654321), n = lo.n, v = [];
  for (var b = 0; b < B; b++){ var sl = 0, sh = 0;
    for (var i = 0; i < n; i++){ var j = Math.floor(R()*n); sl += lo.s.endoAnn[j]; sh += hi.s.endoAnn[j]; }
    sl /= n; sh /= n; var d = sl - sh;
    v.push(Math.min(1, Math.max(0, lo.a + (d > 0 ? (sl - tol)/d : 0.5)*(hi.a - lo.a)))); }
  v.sort(function(x, y){ return x - y; });
  return [v[Math.floor(0.025*B)], v[Math.min(B - 1, Math.floor(0.975*B))]];
}
function s3Breakeven(pts, tol, evalAt){
  function P(a){ var k = a.toFixed(4); if (!pts[k]) pts[k] = evalAt(+k); return pts[k]; }
  function I(q){ return q.m.endoAnn; }
  if (I(P(1)) > tol) return {be:null};
  if (I(P(0)) <= tol) return {be:0};
  P(0.9);
  var lo, hi, it;
  for (it = 0; it < 14; it++){
    lo = null; hi = null;
    Object.keys(pts).forEach(function(k){ var q = pts[k]; if (I(q) > tol && (!lo || q.a > lo.a)) lo = q; });
    Object.keys(pts).forEach(function(k){ var q = pts[k]; if (q.a > lo.a && I(q) <= tol && (!hi || q.a < hi.a)) hi = q; });
    var w = hi.a - lo.a;
    if (w <= 0.002 || Math.min(I(lo) - tol, tol - I(hi)) < 1e-4) break;
    var x = lo.a + (I(lo) - tol)/(I(lo) - I(hi))*w;
    x = Math.min(hi.a - 0.02*w, Math.max(lo.a + 0.02*w, x));
    if (pts[x.toFixed(4)]) x = lo.a + w/2;
    P(x);
  }
  var f = (I(lo) - tol)/(I(lo) - I(hi)), be = lo.a + f*(hi.a - lo.a), above = 0;
  for (var i = 0; i < lo.n; i++) if (lo.s.endoAnn[i] + f*(hi.s.endoAnn[i] - lo.s.endoAnn[i]) > tol) above++;
  /* a90: the a at which 90% of seeds are within tol, from each seed's own curve (linear between evaluated points). */
  var ks = Object.keys(pts).map(function(k){ return pts[k]; }).sort(function(x, y){ return x.a - y.a; }), cr = [];
  for (i = 0; i < lo.n; i++){ var c = Infinity;
    for (var j = 0; j < ks.length; j++) if (ks[j].s.endoAnn[i] <= tol){ c = j === 0 ? 0 : ks[j-1].a + (ks[j-1].s.endoAnn[i] - tol)/(ks[j-1].s.endoAnn[i] - ks[j].s.endoAnn[i])*(ks[j].a - ks[j-1].a); break; }
    cr.push(c); }
  cr.sort(function(x, y){ return x - y; });
  var a90 = cr[Math.min(cr.length - 1, Math.ceil(0.9*cr.length) - 1)];
  return {be:be, ci:s3Boot(lo, hi, tol, 2000), above:above/lo.n, a90:a90, lo:lo.a, hi:hi.a};
}
var S3_TOLS = [0.005, 0.010];
function s3Config(P0, row, N, extra){
  extra = extra || {};
  var sv = s3Set(row.sw), P = Object.assign({}, P0, row.preset || {}), opts = Object.assign({}, row.opts || {}), pts = extra.pts || {};
  try {
    var evalAt = function(a){ return s3Point(P, opts, a, N, !!extra.rec); };
    var out = {row:row, b:S3_TOLS.map(function(t){ return s3Breakeven(pts, t, evalAt); })};
    ['0.0000','0.9000','1.0000'].forEach(function(k){ if (!pts[k]) pts[k] = evalAt(+k); });
    out.p0 = pts['0.0000']; out.p09 = pts['0.9000']; out.p1 = pts['1.0000']; out.nEval = Object.keys(pts).length; out.pts = pts;
    if (extra.at !== undefined && extra.at !== null){ var k = (+extra.at).toFixed(4); if (!pts[k]) pts[k] = evalAt(+k); out.pAt = pts[k]; }
    return out;
  } finally { s3Reset(sv); }
}
/* The one-at-a-time sweep (session 3). `grp`: 'parameter' (a sourced range or a logged placeholder), 'structural' (an
 * adopted decision's alternative) or 'design' (a framework setting). Rows marked fwOnly apply to the framework model. */
var S3_REF = {id:'ref', grp:'reference', lbl:'Reference: lamG 1; theta food 0, housing 0.6, medical 0.5; ptfCap 0; capacity supply; wIdx 0; COLA ratchet at 5%; PTF shipped'};
var S3_ROWS = [S3_REF,
  {id:'lam25', grp:'parameter', lbl:'lamG 0.25', opts:{lamG:0.25}},
  {id:'lam50', grp:'parameter', lbl:'lamG 0.5', opts:{lamG:0.5}},
  {id:'lam141', grp:'parameter', lbl:'lamG 1.41 (quantity theory at US M2 velocity, FRED M2V Q1 2026; session 5)', opts:{lamG:1.41}},
  {id:'widx1', grp:'parameter', lbl:'Wages indexed to P_G (wIdx 1)', opts:{wIdx:1}},
  {id:'aw0', grp:'parameter', lbl:'Program-induced raises unmatched, level shift (aw 0; N7 alternative, S3-1 reading)', opts:{aw:0}},
  {id:'aw0lvl', grp:'structural', lbl:'  ... session 2 reading: the whole premium re-created as money every year (awLevel)', opts:{aw:0, awLevel:true}},
  {id:'biz2', grp:'parameter', lbl:'Business rate 2x (FW.bizRate)', sw:{fw:{bizRate:2}}, fwOnly:true},
  {id:'biz4', grp:'parameter', lbl:'Business rate 4x (FW.bizRate)', sw:{fw:{bizRate:4}}, fwOnly:true},
  {id:'supB', grp:'structural', lbl:'Supply = the Baseline\'s same-year demand (N11 alternative; upper bound)', opts:{supply:'baseline'}},
  {id:'supBhi', grp:'parameter', lbl:'  ... with theta high: food 0.2*, housing 0.78, medical 1.0* (*placeholder)', opts:{supply:'baseline', theta:{food:0.2, housing:0.78, medical:1.0}}},
  {id:'supBcap', grp:'parameter', lbl:'  ... with ptfCap 1 (all of PTF\'s cut is new capacity)', opts:{supply:'baseline', ptfCap:1}},
  {id:'colaOff', grp:'structural', lbl:'COLA off (D6 alternative)', preset:{cola:false}},
  {id:'colaCont', grp:'structural', lbl:'COLA continuous: BU indexed every year (D6 alternative)', preset:{cola:true, colaThresh:-1}},
  {id:'pthM', grp:'structural', lbl:'PTH liquid appreciation matched (N13 alternative)', opts:{pthUnmatched:false}},
  {id:'floorU', grp:'structural', lbl:'Floor write-offs as unmatched money (N5 alternative)', opts:{floorUnmatched:true}},
  {id:'food30', grp:'design', lbl:'PTF: 30% off food only (NYC pilot\'s promise; D4)', sw:{ptfMode:'food30'}},
  {id:'food62', grp:'design', lbl:'PTF: 62% off food only (hub eps_food 2.64; D4)', sw:{ptfMode:'food62'}}];
/* Recession stabilizer arms (v4.19 rules; the page ships all off). */
function s3StabArms(){
  return [{id:'none', lbl:'No stabilizer', preset:{stab:false}},
    {id:'hub', lbl:'Hub protocol: x1.20 when income falls >=2%', preset:{stab:true, stabSev:false, stabMult:CFG.STAB_HUB_MULT, stabThresh:CFG.STAB_HUB_THRESH, stabSusp:false, emerg:false}},
    {id:'n135', lbl:'Shock-neutral fixed: x1.35', preset:{stab:true, stabSev:false, stabMult:CFG.STAB_NEUTRAL_MULT, stabThresh:CFG.STAB_HUB_THRESH, stabSusp:false, emerg:false}},
    {id:'nk', lbl:'Shock-neutral scaled: +2.8% BU per 1% income loss', preset:{stab:true, stabSev:true, stabK:CFG.STAB_NEUTRAL_K, stabThresh:CFG.STAB_HUB_THRESH, stabSusp:false, emerg:false}},
    {id:'pkg', lbl:'Scaled + expiry suspended + emergency enrollment (50%)', preset:{stab:true, stabSev:true, stabK:CFG.STAB_NEUTRAL_K, stabThresh:CFG.STAB_HUB_THRESH, stabSusp:true, emerg:true, emergTakeup:CFG.STAB_EMERG_TAKEUP}}];
}
Object.assign(module.exports, { s3BaseS, s3Point, s3Breakeven, s3Config, S3_ROWS, s3StabArms });

/* ─── Session 5 (Sep 27 2026; Duke assigns the version): the price-neutral point (d18) and the large-N restudy ──────────
 * Harness-only; nothing here changes a run at its defaults.
 *  s5Neutral  d18: the output per dollar of conversion reward, a, at which the program's endogenous inflation is zero, so
 *             the currency keeps its value. a may exceed 1: then the conversion term of the unmatched flow U is negative
 *             (output beyond the reward), offsetting the program's other unmatched flows (PTH appreciation credited as
 *             cash, the essentials channel, any unmatched raises). Bracketed secant on the exact seed mean (CRN) over
 *             [0, aMax]; 95% interval from 2,000 bootstrap resamples of the seeds at the final bracket (not clamped at 1).
 *             null = still inflationary at aMax.
 *  S5_ROWS    the restudy rows (dashboard s17): R0 is session 3's reference (labor off); R1 adds the A3 labor response at
 *             its central values (the joint run); R2-R6 each change one thing on top of R1; R7 applies the three
 *             text-versus-engine corrections together.
 *  s5Config   one scenario under one row: breakeven at 0.5 point (D3) and the price-neutral point, plus a = 0, a = 1 and
 *             the run with no price feedback. */
function s5Neutral(pts, evalAt, aMax){
  aMax = aMax || 5;
  function P(a){ var k = a.toFixed(4); if (!pts[k]) pts[k] = evalAt(+k); return pts[k]; }
  function I(q){ return q.m.endoAnn; }
  var lo, hi = null, i, q;
  if (I(P(1)) <= 0){ if (I(P(0)) <= 0) return {an:0, ci:[0, 0]}; lo = P(0); hi = P(1); }
  else { lo = P(1); var cand = [2, 3, aMax];
    for (i = 0; i < cand.length; i++){ q = P(cand[i]); if (I(q) <= 0){ hi = q; break; } lo = q; }
    if (!hi) return {an:null, ci:null, aMax:aMax}; }
  for (var it = 0; it < 20; it++){
    var w = hi.a - lo.a; if (w <= 0.002 || Math.min(I(lo), -I(hi)) < 1e-5) break;
    var x = lo.a + I(lo)/(I(lo) - I(hi))*w; x = Math.min(hi.a - 0.02*w, Math.max(lo.a + 0.02*w, x));
    if (pts[x.toFixed(4)]) x = lo.a + w/2;
    q = P(x); if (I(q) > 0) lo = q; else hi = q;
  }
  var f = I(lo)/(I(lo) - I(hi)), an = lo.a + f*(hi.a - lo.a), R = mulberry32(987654321), n = lo.n, v = [];
  for (var b = 0; b < 2000; b++){ var sl = 0, sh = 0;
    for (i = 0; i < n; i++){ var j = Math.floor(R()*n); sl += lo.s.endoAnn[j]; sh += hi.s.endoAnn[j]; }
    sl /= n; sh /= n; var d = sl - sh; v.push(lo.a + (d > 0 ? sl/d : 0.5)*(hi.a - lo.a)); }
  v.sort(function(x, y){ return x - y; });
  return {an:an, ci:[v[50], v[1949]], lo:lo.a, hi:hi.a};
}
function s5Set(row){ var sv = {s3:s3Set(row.sw), rs:setRestudy(row.rs), pw:Object.assign({}, PATHWAY_OFF)}; if (row.pw) Object.assign(PATHWAY_OFF, row.pw); return sv; }
function s5Reset(sv){ s3Reset(sv.s3); setRestudy(sv.rs); Object.assign(PATHWAY_OFF, sv.pw); }
var S5_JOINT = {labor:LABOR_DEFAULTS};
var S5_ROWS = [
  {id:'R0', lbl:'R0 Session 3 reference (labor off; lamG 1)', opts:{}},
  {id:'R1', lbl:'R1 Joint run: R0 + A3 labor response at central values', opts:S5_JOINT},
  {id:'R2', lbl:'R2 R1 + theta gated on realised PTF density (C08, d12)', opts:S5_JOINT, rs:{THETA_GATE:'density'}},
  {id:'R3', lbl:'R3 R1 + PTH cuts housing only, 35% of it (d4)', opts:S5_JOINT, rs:{PTH_MODE:'housing'}},
  {id:'R4', lbl:'R4 R1 + discounts skip the basket\'s tax share (d5)', opts:S5_JOINT, rs:{DISC_BASE:'pretax'}},
  {id:'R5', lbl:'R5 R1 + wages indexed to P_G, with COLA (d6)', opts:Object.assign({wIdx:1}, S5_JOINT)},
  {id:'R6', lbl:'R6 R1 + octave wage bonus off (d19)', opts:S5_JOINT, pw:{octaveWage:true}},
  {id:'R7', lbl:'R7 R1 + R2, R3 and R4 together (the three text-versus-engine corrections)', opts:S5_JOINT, rs:{THETA_GATE:'density', PTH_MODE:'housing', DISC_BASE:'pretax'}}];
function s5Config(P0, row, N, tols){
  var sv = s5Set(row), P = Object.assign({}, P0, row.preset || {}), opts = Object.assign({}, row.opts || {}), pts = {};
  try {
    var evalAt = function(a){ return s3Point(P, opts, a, N); };
    var out = {row:row, b:(tols || [0.005]).map(function(t){ return s3Breakeven(pts, t, evalAt); }), n:s5Neutral(pts, evalAt)};
    ['0.0000','1.0000'].forEach(function(k){ if (!pts[k]) pts[k] = evalAt(+k); });
    out.p0 = pts['0.0000']; out.p1 = pts['1.0000'];
    if (out.b[0].be !== null){ var k = out.b[0].be.toFixed(4); if (!pts[k]) pts[k] = evalAt(+k); out.pBE = pts[k]; }
    out.pNF = s3Point(P, Object.assign({}, opts, {pthUnmatched:false}), 1, N, false, true);
    out.nEval = Object.keys(pts).length;
    return out;
  } finally { s5Reset(sv); }
}
/* Tests for the session 5 switches and search (harness-only; run by `unit`). */
function s5UnitSuite(){
  var out = [];
  function t(name, fn){ var sv = {cm:CONVERSION_MODEL, r:applyRule(NEXT_ROUND), rs:setRestudy({THETA_GATE:'szh', PTH_MODE:'basket', DISC_BASE:'basket'})};
    try { var r = fn(); out.push({name:name, pass:!!r.pass, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, detail:'threw: ' + e.message}); }
    finally { CONVERSION_MODEL = sv.cm; applyRule(sv.r); setRestudy(sv.rs); LABOR = null; PRICE = null; THETA_DENS = null; } }
  function agentsAfter(p, seed){ RNG = mulberry32(seed + 700003); var ag = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
    var rp = p.shock ? buildRecessionPath(p.years, seed) : null; RNG = mulberry32(seed); THETA_DENS = null;
    for (var y = 0; y < p.years; y++) runYear(ag, y, p, rp ? rp[y] : {active:false, incomeMultiplier:1.0, yearsLeft:0}); return ag; }
  function same(x, y){ return x.every(function(a, i){ return a.wealth === y[i].wealth && a.wage === y[i].wage && a.yrCostUSD === y[i].yrCostUSD && a.acreEquity === y[i].acreEquity && a.octave === y[i].octave; }); }
  var FI = nextRoundPreset(FULL_INTEGRATION);
  t('switches inert at their defaults: index.html\'s seed-42 Full Integration figures, with THETA_GATE, PTH_MODE and DISC_BASE set explicitly to their defaults', function(){
    applyRule({SURPLUS_CONSUMPTION_SHARE:0, SURPLUS_CONSUMPTION_BASE:'wage'}); var r = runScenario(FULL_INTEGRATION, 42);
    return {pass: r.pov === 15.8 && r.wealth === 570661 && r.bleiMed === 1975, detail: r.pov + ' / ' + r.wealth + ' / ' + r.bleiMed};
  });
  t('d4/d5 algebra: with PTH_MODE housing at a cut equal to the whole-basket rate over the housing share, and DISC_BASE basket, every agent matches the shipped run (engine, seed 1)', function(){
    var sv = PTH_HOUSING_CUT; PTH_HOUSING_CUT = 0.35/CFG.BASKET.housing; setRestudy({PTH_MODE:'housing'});
    var ok = true, A = agentsAfter(ccoOnlyFor(FI), 1); setRestudy({PTH_MODE:'basket'}); var B = agentsAfter(ccoOnlyFor(FI), 1); if (!same(A, B)) ok = false;
    /* with PTF off and PTH on, 0.35/h x h = 0.35 of the basket, the shipped cut: wealth must agree to rounding */
    var Pn = Object.assign({}, FI, {ptf:false, ptfShare:0}); setRestudy({PTH_MODE:'housing'}); var C = agentsAfter(Pn, 1); setRestudy({PTH_MODE:'basket'}); var Dd = agentsAfter(Pn, 1);
    var md = 0; C.forEach(function(a, i){ md = Math.max(md, Math.abs(a.wealth - Dd[i].wealth)/Math.max(1, Math.abs(Dd[i].wealth))); });
    PTH_HOUSING_CUT = sv;
    return {pass: ok && md < 1e-9, detail: 'CCO alone identical: ' + ok + '; PTF off, PTH on: max relative wealth gap ' + md.toExponential(1)};
  });
  t('d5 direction: skipping the tax share raises every discounted agent\'s cost and leaves undiscounted agents unchanged (Full Integration, seed 1, year 1)', function(){
    function yr1(){ RNG = mulberry32(700004); var ag = makeLatentPopulation(FI.nAgents).map(function(l){ return instantiateAgent(l, FI); }); RNG = mulberry32(1);
      runYear(ag, 0, FI, {active:false, incomeMultiplier:1.0, yearsLeft:0}); return ag; }
    var A = yr1(); setRestudy({DISC_BASE:'pretax'}); var B = yr1(); setRestudy({DISC_BASE:'basket'});
    var up = 0, eq = 0, bad = 0; A.forEach(function(a, i){ var disc = a.inCCO || a.inPTF || a.inPTH; if (disc){ if (B[i].yrCostUSD > a.yrCostUSD) up++; else bad++; } else { if (B[i].yrCostUSD === a.yrCostUSD) eq++; else bad++; } });
    return {pass: bad === 0 && up > 0, detail: up + ' discounted agents cost more, ' + eq + ' undiscounted unchanged, ' + bad + ' exceptions'};
  });
  t('theta density gate: below 55% realised PTF share theta is 0 (conversion bonus 1.30 for PTF members); the reference run\'s realised share stays below it', function(){
    setRestudy({THETA_GATE:'density'}); var ag = agentsAfter(FI, 1), sh = THETA_DENS; setRestudy({THETA_GATE:'szh'});
    return {pass: sh !== null && sh < CFG.SZH_THETA_THRESHOLD && szhTheta(sh) === 0 && szhTheta(0.72) > 0, detail: 'realised PTF share in year 20: ' + (sh*100).toFixed(1) + '%; theta there ' + szhTheta(sh) + ' vs ' + szhTheta(0.72).toFixed(3) + ' on the slider'};
  });
  t('joint run: labor coefficients at zero in priceRun are bit-identical to priceRun without labor, and central coefficients move earnings and inflation (Full Integration, seed 1, a = 0.9, both models)', function(){
    var ok = true, d = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; var S = s3BaseS(FI, 1);
      var r0 = priceRun(FI, 1, {a:0.9}, S), r1 = priceRun(FI, 1, {a:0.9, labor:LAB_ZERO}, S), r2 = priceRun(FI, 1, {a:0.9, labor:LABOR_DEFAULTS}, S);
      if (!same(r0.agents, r1.agents) || r0.res.endoAnn !== r1.res.endoAnn || r1.res.dE !== 0) ok = false; if (r2.res.dE === 0 || r2.res.endoAnn === r0.res.endoAnn) ok = false;
      d.push(cm + ': dE at central ' + (r2.res.dE*100).toFixed(2) + '%'); });
    return {pass: ok, detail: d.join('; ')};
  });
  t('price-neutral search (d18): finds a known root above 1 on a synthetic linear curve, and returns 0 when a = 0 is already non-inflationary', function(){
    function synth(f){ return function(a){ var n = 100, s = new Float64Array(n), m = 0, R = mulberry32(99);
      for (var i = 0; i < n; i++){ s[i] = f(a) + (R() - 0.5)*0.001; m += s[i]; } return {a:a, n:n, s:{endoAnn:s}, m:{endoAnn:m/n}}; }; }
    var r = s5Neutral({}, synth(function(a){ return 0.04*(1 - a) + 0.006; })), z = s5Neutral({}, synth(function(a){ return -0.001 - 0.01*a; }));
    var want = 1 + 0.006/0.04;
    return {pass: Math.abs(r.an - want) < 2e-3 && r.ci[0] <= want + 2e-3 && r.ci[1] >= want - 2e-3 && z.an === 0, detail: 'found ' + r.an.toFixed(4) + ' [' + r.ci[0].toFixed(4) + '-' + r.ci[1].toFixed(4) + '] (true ' + want.toFixed(4) + ')'};
  });
  return out;
}
Object.assign(module.exports, { s5Neutral, s5Config, S5_ROWS, s5UnitSuite, setRestudy });


/* ─── Session 4 (Sep 27 2026; Duke assigns the version): A3 labor supply ─────────────────────────────────────────────
 * laborRun   one run with LABOR set to L (null = off). Draws exactly as runScenario() does, so runs are CRN-paired
 *            across every L and preset. Returns end-of-run poverty (wealth, BLEI, basket) and, per agent-year, the
 *            earnings response by channel, the program's gross cost (BU spent on own essentials + conversion + UBI) and,
 *            with wantBound, the BU that expired unconverted (the most extra conversion could draw on).
 * laborStudy the mean over seeds 1..N of laborRun, under the D1 consumption rule (NEXT_ROUND) and D6 COLA. */
function newLabAcc(){ return {n:0, nP:0, E0:0, E:0, raise:0, cash:0, bu:0, buR:0, rent:0, disp:0, C:0, U:0, projH:0, zero:0, conv:0, convP:0}; }
function laborRun(p, seed, L, wantBound){
  var CALM0 = {active:false, incomeMultiplier:1.0, yearsLeft:0};
  RNG = mulberry32(seed + 700003);
  var agents = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
  var recPath = p.shock ? buildRecessionPath(p.years, seed) : null;
  RNG = mulberry32(seed);
  var acc = newLabAcc();
  THETA_DENS = null;  // session 5
  LABOR = L ? Object.assign({}, L, {acc:acc}) : null;
  if (wantBound) LEDGER = newLedger();
  try { for (var yr = 0; yr < p.years; yr++) runYear(agents, yr, p, recPath ? recPath[yr] : CALM0); }
  finally { LABOR = null; }
  var bound = null;
  if (wantBound){ var T = LEDGER.tot; bound = {expired: CONVERSION_MODEL === 'framework' ? (T.fwProjLost || 0) : (T.buExpired || 0), conv: T.convNet || T.fwProjNet || 0, convBU: T.buSpent || T.fwProjBU || 0}; LEDGER = null; }
  var n = agents.length, pov = 0, bpov = 0;
  agents.forEach(function(a){ if (a.wealth < CFG.POVERTY_LINE) pov++; if (agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf) < CFG.BLEI_PRECARIOUS_MAX) bpov++; });
  var ib = incomeBasketMetrics(agents), N = Math.max(1, acc.n), ubiTot = (p.ubi || 0)*acc.n;
  return {pov:pov/n*100, bleiPov:bpov/n*100, basketPov:ib.basketPov, medWealth:medianOf(agents.map(function(a){ return a.wealth; })),
    E0:acc.E0/N, E:acc.E/N, dE:(acc.E - acc.E0)/Math.max(1, acc.E0), raise:acc.raise/N, cash:acc.cash/N, bu:acc.bu/N, buR:acc.buR/N,
    rent:acc.rent/N, disp:acc.disp/N, C:acc.C/N, zero:acc.zero/N, projH:acc.projH/N, partShare:acc.nP/N,
    cost:(acc.U + acc.conv)/N, costU:acc.U/N, costConv:acc.conv/N, ubiPer:ubiTot/N, bound:bound};
}
var LAB_KEYS = ['pov','bleiPov','basketPov','medWealth','E0','E','dE','raise','cash','bu','buR','rent','disp','C','zero','projH','partShare','cost','costU','costConv'];
function laborStudy(p, N, L, wantBound){
  var old = applyRule(NEXT_ROUND), P = nextRoundPreset(p), m = {}, b = {expired:0, conv:0, convBU:0};
  LAB_KEYS.forEach(function(k){ m[k] = 0; });
  try {
    for (var sd = 1; sd <= N; sd++){ var r = laborRun(P, sd, L, wantBound);
      LAB_KEYS.forEach(function(k){ m[k] += r[k]/N; });
      if (r.bound){ b.expired += r.bound.expired/N; b.conv += r.bound.conv/N; b.convBU += r.bound.convBU/N; } }
  } finally { applyRule(old); }
  if (wantBound) m.bound = b;
  return m;
}
function laborOpts(o){ return Object.assign({}, LABOR_DEFAULTS, o || {}); }
var LAB_ZERO = {rho:0, rhoBU:0, rhoR:0, eps:0, delta:0};
function ubiFor(p, cost){ return Object.assign({}, baselineFor(p, true), {ubi:cost}); }
/* Tests for the labor module (harness-only; run by `unit` after the price suite). */
function laborUnitSuite(){
  var out = [];
  function t(name, fn){ var sv = {cm:CONVERSION_MODEL, r:applyRule(NEXT_ROUND)};
    try { var r = fn(); out.push({name:name, pass:!!r.pass, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, detail:'threw: ' + e.message}); }
    finally { CONVERSION_MODEL = sv.cm; applyRule(sv.r); LABOR = null; LEDGER = null; } }
  function agentsAfter(p, seed, L){ RNG = mulberry32(seed + 700003); var ag = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
    var rp = p.shock ? buildRecessionPath(p.years, seed) : null; RNG = mulberry32(seed); LABOR = L;
    try { for (var y = 0; y < p.years; y++) runYear(ag, y, p, rp ? rp[y] : {active:false, incomeMultiplier:1.0, yearsLeft:0}); } finally { LABOR = null; } return ag; }
  function same(x, y){ return x.every(function(a, i){ return a.wealth === y[i].wealth && a.wage === y[i].wage && a.yrWageUSD === y[i].yrWageUSD && a.octave === y[i].octave; }); }
  var FI = nextRoundPreset(FULL_INTEGRATION), ADV = nextRoundPreset(ADVERSE_REFERENCE);
  t('inert: LABOR with every coefficient 0, and p.ubi = 0, are bit-identical to LABOR off (Full Integration and Adverse, seeds 1-2, both models)', function(){
    var ok = true;
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; [FI, ADV].forEach(function(P){ for (var s = 1; s <= 2; s++){
      if (!same(agentsAfter(P, s, Object.assign({}, LAB_ZERO)), agentsAfter(P, s, null))) ok = false;
      if (!same(agentsAfter(Object.assign({}, P, {ubi:0}), s, null), agentsAfter(P, s, null))) ok = false; } }); });
    return {pass: ok, detail: 'every agent\'s wealth, wage, earnings and octave identical'};
  });
  t('income effect: in the UBI arm with eps 0, earnings fall by exactly rho x UBI wherever the zero floor does not bind (seed 1)', function(){
    var U = ubiFor(FULL_INTEGRATION, 6000), r = laborRun(U, 1, {rho:0.16, rhoBU:0.16, rhoR:0, eps:0, delta:0}), gap = Math.abs((r.E0 - r.E) - 0.16*6000);
    return {pass: r.zero === 0 && gap < 1e-6, detail: 'mean fall $' + (r.E0 - r.E).toFixed(4) + ' vs $' + (0.16*6000).toFixed(4) + '; floor binds in ' + (r.zero*100).toFixed(2) + '% of agent-years'};
  });
  t('monotone: earnings fall as rho rises (UBI arm) and as delta rises (Full Integration, framework), seed 1', function(){
    var U = ubiFor(FULL_INTEGRATION, 6000), prev = Infinity, ok = true, v = [];
    [0, 0.1, 0.16, 0.28].forEach(function(rho){ var e = laborRun(U, 1, {rho:rho, rhoBU:rho, rhoR:0, eps:0, delta:0}).E; if (e > prev) ok = false; prev = e; v.push(e.toFixed(0)); });
    CONVERSION_MODEL = 'framework'; prev = Infinity; var w = [];
    [0, 0.5, 1].forEach(function(d){ var e = laborRun(FI, 1, laborOpts({delta:d})).E; if (e > prev) ok = false; prev = e; w.push(e.toFixed(0)); });
    return {pass: ok, detail: 'UBI earnings by rho: ' + v.join(' > ') + '; framework earnings by delta: ' + w.join(' > ')};
  });
  t('return to work: with no unconditional support (rho 0), a positive eps raises Full Integration earnings and leaves the Baseline unchanged (seed 1)', function(){
    var f0 = laborRun(FI, 1, LAB_ZERO).E, f1 = laborRun(FI, 1, {rho:0, rhoBU:0, rhoR:0, eps:0.33, delta:0}).E;
    var B = nextRoundPreset(baselineFor(FULL_INTEGRATION, true)), b0 = laborRun(B, 1, LAB_ZERO).E, b1 = laborRun(B, 1, {rho:0.16, rhoBU:0.16, rhoR:0, eps:0.33, delta:1}).E;
    return {pass: f1 > f0 && b0 === b1, detail: 'Full Integration $' + f0.toFixed(0) + ' to $' + f1.toFixed(0) + '; Baseline $' + b0.toFixed(0) + ' = $' + b1.toFixed(0)};
  });
  return out;
}
Object.assign(module.exports, { laborRun, laborStudy, laborUnitSuite, laborOpts, LABOR_DEFAULTS, LAB_ZERO, ubiFor, setLabor:function(L){ LABOR = L; } });
/* ─── Session 6 (A4): testbed runs, presets, matching and tests (harness-only). ─────────────────────────────────────────────
 * NR6, the next-round accounting profile Duke confirmed on Sep 27 (dashboard d22, d23): the D1 consumption rule, plus the three
 * text-versus-engine corrections (theta on realised PTF density, PTH cuts housing only, discounts skip the tax share). TB_RUN adds
 * wage indexation to P_G (d23; applied to every preset, since wage indexation is a property of the economy, not of a program)
 * and the A3 labor response at its central values. The globals keep their v4.21 defaults, so the checks still test index.html. */
var NR6 = {rule:NEXT_ROUND, rs:{THETA_GATE:'density', PTH_MODE:'housing', DISC_BASE:'pretax'}};
function applyNR6(){ return {rule:applyRule(NR6.rule), rs:setRestudy(NR6.rs)}; }
function resetNR6(sv){ applyRule(sv.rule); setRestudy(sv.rs); }
var TB_RUN = {wIdx:1, labor:LABOR_DEFAULTS};
/* Session 10 (dashboard d40, confirmed Sep 28, 2026): the testbed profile counts the BLEI-gated raise as program-induced where
 * the design's own support carries the adult over the gate (N7_BLEI; session 9, i3-2), the same rule for every design. The
 * `testbed` mode applies it to every row that does not set N7_BLEI itself (its n7 section sets it both ways, so that section
 * still shows the attribution off and on). The global default stays false, so the unit tests and the index.html parity checks
 * are unchanged; tbUnitSuite checks the profile directly. */
var TB_PROFILE_G = {N7_BLEI:true};
function tbOpts(o){ o = o || {}; var r = Object.assign({}, PM_DEFAULTS, TB_DEFAULTS, TB_RUN, o); r.theta = Object.assign({}, PM_DEFAULTS.theta, o.theta || {}); return r; }
/* Session 8 (A5): Gini coefficient of a list of incomes (negatives count as 0), the standard sorted-rank formula. */
function giniOfArr(x){ var v = x.map(function(z){ return Math.max(0, +z || 0); }).sort(function(a, b){ return a - b; }), n = v.length, t = 0, w = 0;
  for (var i = 0; i < n; i++){ t += v[i]; w += (i + 1)*v[i]; } return n > 0 && t > 0 ? 2*w/(n*t) - (n + 1)/n : 0; }
/* One testbed run: priceRun()'s loop (same draws, same price rules) with TB set. Returns the run's metrics; see tbStudy for keys. */
function tbRunCore(p, seed, o, S, tau0, yMax){
  var CALM0 = {active:false, incomeMultiplier:1.0, yearsLeft:0};
  RNG = mulberry32(seed + 700003);
  var latent = makeLatentPopulation(p.nAgents), agents = latent.map(function(l){ return instantiateAgent(l, p); });
  var recPath = p.shock ? buildRecessionPath(p.years, seed) : null;
  var spec = p.tb || {}, gR = mulberry32(seed + 900001), grp = o.grp || {part:0, pth:0};
  var wq = latent.map(function(l){ return l.wage; }).sort(function(x, y){ return x - y; }), w1 = wq[Math.floor(wq.length/3)], w2 = wq[Math.floor(2*wq.length/3)];
  agents.forEach(function(a, i){ var l = latent[i]; a._tbU = gR(); a._tbEl = !!(spec.endow && l.wealth < spec.endow.thresh); a._tbPart = l.uCCO < grp.part; a._tbPTH = l.uPTH < grp.pth; a._tbLow = l.wage < w1; a._tbTop = l.wage >= w2; });
  RNG = mulberry32(seed);
  var comp = {}; CFG.BASKET_KEYS.forEach(function(k){ comp[k] = 1; });
  PRICE = {bIdx:1, comp:comp, piG:0, colaLevel:1, lastFull:1, wIdx:o.wIdx, noDamp:o.noDamp, acc:null};
  TB = {fin:o.fin, tau:tau0, X:o.X, inkindRho:o.inkindRho, neutralGate:o.neutralGate, cur:null};
  var PG = 1, path = [], wbPrev = 0, labAcc = null, T = p.years;
  var L = {pjg:0, cost:0, cash:0, endow:0, bu:0, conv:0, cutPT:0, cutG:0, cap:0, pth:0, tax:0, need:0, treas:0, f0:0, f1:0, f2:0, n:0, endowTot:0, need0:0, base0:0, pd:0, tgt:0, emp:0, hrs:0, Er:0, bR:0, bP:0,
    bz:0, es:0, n1:0, nP1:0, nN1:0, pyP:0, pyN:0, nWP1:0, esWP:0};  /* session 19 (s38) */
  THETA_DENS = null;
  if (o.labor){ labAcc = newLabAcc(); LABOR = Object.assign({}, o.labor, {acc:labAcc}); }
  try {
    for (var yr = 0; yr < yMax; yr++){
      PRICE.acc = newPMAcc();
      runYear(agents, yr, p, recPath ? recPath[yr] : CALM0);
      var A = PRICE.acc, C = TB.cur || tbNewAcc(), d = A.n ? A.essD/A.n : 1, tauUsed = TB.tau;
      var wbInc = A.wageBonusNS - wbPrev; wbPrev = A.wageBonusNS;
      var extra = (o.floorUnmatched ? A.unmet : 0) + (1 - o.aw)*(o.awLevel ? A.wageBonus : wbInc);
      if (yr === 0) L.endowTot = C.endow;
      /* d26: what the treasury must fund this year: every program dollar at face value (the endowment amortized over the run),
       * less the efficiency share eP of price cuts (added capacity, not a transfer; 0 by the plan's rule). */
      /* d66 (sessions 15-16; issue i7): the launch gift's proceeds are one-time spending. 'payg' (Duke's pick) finances them in the
       * year they are paid, like every other conversion; 'run' spreads them over the remaining years, like the endowment (d26). */
      L.pjg += C.pjg; var gRun = !!(PROJ && PROJ.giftFin === 'run');
      var need = C.cash + L.endowTot/T + C.bu + (o.fin === 'hybrid' ? 0 : gRun ? C.conv - C.pjg + L.pjg/(T - 1) : C.conv) + C.cap + (1 - o.eP)*(C.cutPT + C.cutG) + C.pthLiq, U;  /* session 7 (d26): hybrid leaves conversion rewards to money creation */
      /* d24: created money counted by one rule for every design. aT: output matched to transfer dollars (cash, BU spent at face
       * value, the endowment, capital spending); a: output matched to conversion rewards (H1); eP: price-cut efficiency. */
      /* Session 7 (d24 option b, o.buAtA): output matched at a to a converted BU's face value as well as its reward. */
      if (o.fin === 'money') U = (1 - o.aT)*(C.cash + C.endow + C.cap) + (1 - (o.buAtA ? o.a : o.aT))*C.bu + (1 - o.eP)*(C.cutPT + C.cutG) + (1 - o.a)*C.conv + (o.pthUnmatched ? C.pthLiq : 0) + extra;
      else if (o.fin === 'tax') U = extra;
      else if (o.fin === 'hybrid') U = (1 - o.a)*C.conv + extra;  /* session 7 (d26 option c): transfers taxed, conversion rewards created at a */
      else U = (1 - o.a)*A.conv + (o.pthUnmatched ? A.pthLiq : 0) + extra;  /* 'none': the session 2-5 rule (transfers and price cuts unfinanced) */
      if (yr === 0){ L.need0 = need; L.base0 = C.base; }
      L.cost += (C.cash + C.endow + C.bu + C.conv + C.cap + C.cutPT + C.cutG + C.pthLiq)/C.idx;
      L.cash += C.cash/C.idx; L.endow += C.endow/C.idx; L.bu += C.bu/C.idx; L.conv += C.conv/C.idx; L.cutPT += C.cutPT/C.idx; L.cutG += C.cutG/C.idx; L.cap += C.cap/C.idx; L.pth += C.pthLiq/C.idx;
      L.pd += C.pd/C.idx; L.tgt += C.tgt/C.idx; L.tax += C.tax/C.idx; L.need += need/C.idx; L.treas += (C.tax - need)/C.idx; L.f0 += C.f0; L.f1 += C.f1; L.f2 += C.f2; L.n += C.n;
      L.emp += C.emp; L.hrs += C.hrs; L.Er += C.E/C.idx; L.bR += C.bR; L.bP += C.bP;  /* session 8 (A5): employment, hours, real wage earnings */
      L.bz += C.bz/C.idx; L.es += C.es/C.idx; L.pyP += C.pyP/C.idx; L.pyN += C.pyN/C.idx; L.esWP += C.esWP/C.idx; L.n1 += C.n1; L.nP1 += C.nP1; L.nN1 += C.nN1; L.nWP1 += C.nWP1;  /* session 19 */
      if (o.fin === 'tax' || o.fin === 'hybrid') TB.tau = C.base > 0 ? Math.min(o.tauMax, need/C.base) : 0;
      var PGn = pmGenStep(PG, U, A.Y, o.lamG), capShare = o.ptfCap*(A.n ? A.ptfN/A.n : 0), PE = {};
      CFG.ESSENTIALS.forEach(function(k){
        var cut = !p.ptf ? 0 : PTF_MODE === 'shipped' ? (p.szh ? 0.12 + p.szhCoh*0.04 : 0.12) : (k === 'food' ? PTF_FOOD_CUT[PTF_MODE] : 0);
        if (!S || o.essMatched){ PE[k] = 1; return; }
        var sRef = o.supply === 'baseline' ? S[yr] : S[0]*Math.pow(1 + o.gS, yr);
        var dEff = o.supply === 'baseline' ? d : sRef + Math.max(0, d - sRef) - Math.max(0, S[yr] - sRef);
        PE[k] = pmEssLevel(dEff, sRef, capShare*cut, o.theta[k]);
      });
      path.push({bIdx:PRICE.bIdx, PG:PG, U:U, Y:A.Y, tau:tauUsed, colaLevel:PRICE.colaLevel, full:C.idx});  /* session 8: full price level (exogenous x endogenous) */
      PRICE.piG = PGn/PG - 1; PG = PGn;
      CFG.BASKET_KEYS.forEach(function(k){ comp[k] = CFG.ESSENTIALS.indexOf(k) >= 0 ? PE[k]*(o.pgOnE ? PG : 1) : PG; });
      PRICE.bIdx = pmBasketIdx(comp);
    }
  } finally { PRICE = null; TB = null; if (labAcc) LABOR = null; }
  if (yMax < T) return {tau0: L.base0 > 0 ? Math.min(o.tauMax, L.need0/L.base0) : 0};
  var n = agents.length, NY = n*T, full = agents[0].yrBasketUSD/CFG.LIVING_WAGE_ANNUAL, lineF = o.lines === 'nominal' ? 1 : full, pov = 0, bpov = 0, g0 = 0, g1 = 0, g2 = 0;
  var nbpov = 0;  /* session 7 (d28): design-neutral BLEI, Baseline rules plus one month of the design's regular support (the d28 gate's measure) */
  agents.forEach(function(a){ if (a.wealth < CFG.POVERTY_LINE*lineF) pov++; if (agentBLEI(a, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf)/lineF < CFG.BLEI_PRECARIOUS_MAX) bpov++;
    if ((agentBLEI(a, 0, false, false, false, 0, false) + (a._tbM || 0)/CFG.BASE_DAILY_COST)/lineF < CFG.BLEI_PRECARIOUS_MAX) nbpov++;
    var g = a._tbGap || 0; if (g > 0) g0++; g1 += g; g2 += g*g; });
  /* Groups: mean real resources per year, person-year basket FGT0, and wealth poverty at year 20 (the inflation tax on nominal wealth
   * shows only here: income terms are indexed, wealth is not). */
  function grpOf(f){ var m = 0, k = 0, f0 = 0, wp = 0; agents.forEach(function(a){ if (f(a)){ k++; m += a._tbRes/a._tbYrs; f0 += a._tbF0/a._tbYrs; if (a.wealth < CFG.POVERTY_LINE*lineF) wp++; } });
    return k ? {res:m/k, f0:f0/k*100, wp:wp/k*100, k:k} : {res:0, f0:0, wp:0, k:0}; }
  var gP = grpOf(function(a){ return a._tbPart; }), gN = grpOf(function(a){ return !a._tbPart; }), gH = grpOf(function(a){ return a._tbPTH; }), gL = grpOf(function(a){ return a._tbLow; }), gT = grpOf(function(a){ return a._tbTop; });
  /* Session 8 (A5): spells, persistence, and the year-20 income distribution (reporting only). */
  var sp = 0, spY = 0, ever = 0, chron = 0; agents.forEach(function(a){ sp += a._tbSp || 0; spY += a._tbF0 || 0; if (a._tbF0 > 0) ever++; if ((a._tbF0 || 0) >= T/2) chron++; });
  var giniD = giniOfArr(agents.map(function(a){ return a._tbDisp || 0; })), giniX = giniOfArr(agents.map(function(a){ return a._tbExt || 0; }));
  var pT = path[T-1], p10 = path[Math.min(T-1, 9)], realT = (p.cola ? pT.colaLevel : 1)/pT.full;
  function pjQ(k){ return (PROJ && PJS && PJS.acc.partY > 0) ? PJS.acc[k]/PJS.acc.partY : 0; }  /* N1 (session 15) */
  var pjSv = 0; if (PROJ && PJS && PJS.acc.partY > 0){ agents.forEach(function(a){ pjSv += (a._pjSaved || 0) + (a._pjGiftH || 0); }); pjSv /= Math.max(1, PJS.acc.partY/T); }
  var esOn = !!(ESP && ESS && CONVERSION_MODEL === 'framework'), eA = esOn ? ESS.acc : null;  /* session 19 (s38) */
  var bI = path[T-1].bIdx, mx = 0, tauS = 0;
  for (var t = 1; t < T; t++) mx = Math.max(mx, path[t].bIdx/path[t-1].bIdx - 1);
  path.forEach(function(q){ tauS += q.tau; });
  return {path:path, res:{
    endoAnn:Math.pow(bI, 1/(T - 1)) - 1, endoMax:mx, pov:pov/n*100, bleiPov:bpov/n*100, nbleiPov:nbpov/n*100, tgt:L.pd > 0 ? L.tgt/L.pd : 0, medWealthReal:medianOf(agents.map(function(a){ return a.wealth; }))/full,
    fgt0:g0/n*100, fgt1:g1/n*100, fgt2:g2/n*100, fgt0PY:L.f0/L.n*100, fgt1PY:L.f1/L.n*100, fgt2PY:L.f2/L.n*100,
    cost:L.cost/NY, cCash:L.cash/NY, cEndow:L.endow/NY, cBU:L.bu/NY, cConv:L.conv/NY, cCut:(L.cutPT + L.cutG)/NY, cCap:L.cap/NY, cPth:L.pth/NY,
    tax:L.tax/NY, need:L.need/NY, treas:L.treas/NY, tauMean:tauS/T, tauLast:path[T-1].tau,
    dE:labAcc && labAcc.E0 > 0 ? (labAcc.E - labAcc.E0)/labAcc.E0 : 0, E:labAcc ? labAcc.E/Math.max(1, labAcc.n) : 0, E0:labAcc ? labAcc.E0/Math.max(1, labAcc.n) : 0, zero:labAcc ? labAcc.zero/Math.max(1, labAcc.n) : 0,
    gPartRes:gP.res, gPartF0:gP.f0, gNonRes:gN.res, gNonF0:gN.f0, gPthRes:gH.res, gPthF0:gH.f0, gLowRes:gL.res, gLowF0:gL.f0, gTopRes:gT.res, gTopF0:gT.f0,
    gPartW:gP.wp, gNonW:gN.wp, gPthW:gH.wp, gLowW:gL.wp, gTopW:gT.wp,
    pyPoor:spY/n, everPoor:ever/n*100, spellMean:sp > 0 ? spY/sp : 0, chronic:chron/n*100, emp:L.emp/L.n*100, hrs:L.hrs/L.n - 1, Er:L.Er/NY,
    giniD:giniD, giniX:giniX, pLev10:p10.full, pLev20:pT.full, realT:realT, bleiR:L.bR/L.n*100, bleiP:L.bP/L.n*100,
    /* N1 (session 15): project hiring, per participant-year, year-0 dollars (0 when PROJ is off) */
    pjNet:pjQ('net'), pjGift:pjQ('giftNet'), pjBU:pjQ('alloc'), pjExp:pjQ('exp'), pjHrs:pjQ('hrs'), pjDisp:pjQ('disp'), pjWork:pjQ('work')*100,
    pjRc:(PROJ && PJS && PJS.acc.rcN) ? PJS.acc.rc/PJS.acc.rcN : 0, pjSaved:pjSv,
    /* Session 19 (s38): the business premium and ESP payroll, years 1-19, year-0 dollars. bzPay: the ESP's own premium as paid out
     * (today's whole premium when ESP is off); esPrem: payroll premium; per adult-year, participant-year, non-participant-year and
     * participating ESP worker-year. From ESS (0 when ESP is off): payroll BU per ESP worker-year, BU share of ESP pay (%), mean rate
     * on payroll BU, the share of participating ESP worker-years where the octave cap binds (%), and BU converted or returned per
     * adult-year. */
    bzPay:L.n1 ? L.bz/L.n1 : 0, esPrem:L.n1 ? L.es/L.n1 : 0, payPart:L.nP1 ? L.pyP/L.nP1 : 0, payNon:L.nN1 ? L.pyN/L.nN1 : 0, esPremW:L.nWP1 ? L.esWP/L.nWP1 : 0,
    esBUW:eA && eA.wkY1 ? eA.alloc/eA.wkY1 : 0, esShare:eA && eA.wage > 0 ? eA.alloc/eA.wage*100 : 0, esRate:eA && eA.conv > 0 ? eA.rateXbu/eA.conv : 0,
    esCapB:eA && eA.partWkY ? eA.capBind/eA.partWkY*100 : 0, esConv:eA && L.n1 ? eA.conv/L.n1 : 0, esRet:eA && L.n1 ? eA.ret/L.n1 : 0}};
}
function tbRun(p, seed, o, S){
  o = tbOpts(o);
  var tau0 = ((o.fin === 'tax' || o.fin === 'hybrid') && p.tb) ? tbRunCore(p, seed, o, S, 0, 1).tau0 : 0;
  return tbRunCore(p, seed, o, S, tau0, p.years);
}
var TB_KEYS = ['endoAnn','endoMax','pov','bleiPov','nbleiPov','tgt','medWealthReal','fgt0','fgt1','fgt2','fgt0PY','fgt1PY','fgt2PY','cost','cCash','cEndow','cBU','cConv','cCut','cCap','cPth',
  'tax','need','treas','tauMean','tauLast','dE','E','E0','zero','gPartRes','gPartF0','gNonRes','gNonF0','gPthRes','gPthF0','gLowRes','gLowF0','gTopRes','gTopF0',
  'gPartW','gNonW','gPthW','gLowW','gTopW','pyPoor','everPoor','spellMean','chronic','emp','hrs','Er','giniD','giniX','pLev10','pLev20','realT','bleiR','bleiP',
  'pjNet','pjGift','pjBU','pjExp','pjHrs','pjDisp','pjWork','pjRc','pjSaved',  /* N1 (session 15) */
  'bzPay','esPrem','payPart','payNon','esPremW','esBUW','esShare','esRate','esCapB','esConv','esRet'];  /* N1 (session 19, s38) */
/* Paired study over seeds 1..N (optionally lo..hi). envP: the Compassionism scenario that defines the environment, the essentials
 * supply path (its matched Baseline, as in sessions 2-5) and the groups (participants: latent uCCO < its partRate; PTH members:
 * latent uPTH < its pthUptake, the same agents in every design). cfgs: [{p, o, cm, pw}]; pw switches PATHWAY_OFF entries for that
 * row only (d19). Returns means and per-seed arrays. */
function tbStudy(cfgs, N, envP, o0, lo){
  lo = lo || 1; var M = N - lo + 1, grp = {part:envP.partRate, pth:envP.pthUptake};
  var out = cfgs.map(function(){ var r = {_s:{}}; TB_KEYS.forEach(function(k){ r[k] = 0; r._s[k] = new Float64Array(M); }); return r; });
  for (var sd = lo; sd <= N; sd++){
    var S = s3BaseS(envP, sd);
    cfgs.forEach(function(c, i){ var cm0 = CONVERSION_MODEL, pw0 = Object.assign({}, PATHWAY_OFF); if (c.cm) CONVERSION_MODEL = c.cm;
      if (c.pw) Object.assign(PATHWAY_OFF, c.pw);  /* d19: e.g. {octaveWage:true}, the octave wage bonus off for this row only */
      var g0 = tbSetG(c.g);  /* session 7: per-row engine-question switches (i3), restored below */
      var pj0 = PROJ; if (c.pj) PROJ = Object.assign({}, PROJ_DEFAULTS, c.pj === true ? {} : c.pj);  /* N1 (session 15): project hiring for this row only */
      var es0 = ESP; if (c.es) ESP = Object.assign({}, ESP_DEFAULTS, c.es === true ? {} : c.es);  /* N1 (session 19): ESP payroll for this row only */
      try { var r = tbRun(c.p, sd, Object.assign({grp:grp}, o0 || {}, c.o || {}), S).res;
        TB_KEYS.forEach(function(k){ out[i][k] += r[k]/M; out[i]._s[k][sd - lo] = r[k]; }); }
      finally { CONVERSION_MODEL = cm0; Object.assign(PATHWAY_OFF, pw0); tbSetG(g0); PROJ = pj0; ESP = es0; } });
  }
  return out;
}
/* Session 7: set the i3 engine-question switches for one row; returns the previous values. */
function tbSetG(g){ var old = {FBS_BU_ONCE:FBS_BU_ONCE, PTH_APPR_CONSERVE:PTH_APPR_CONSERVE, N7_BLEI:N7_BLEI};
  if (g){ if ('FBS_BU_ONCE' in g) FBS_BU_ONCE = !!g.FBS_BU_ONCE; if ('PTH_APPR_CONSERVE' in g) PTH_APPR_CONSERVE = !!g.PTH_APPR_CONSERVE; if ('N7_BLEI' in g) N7_BLEI = !!g.N7_BLEI; }
  return old; }
/* Paired difference x - y on a key, with a normal 95% interval over seeds. */
function tbDiff(x, y, k){ var n = x._s[k].length, m = 0, v = 0, i; for (i = 0; i < n; i++) m += (x._s[k][i] - y._s[k][i])/n;
  for (i = 0; i < n; i++){ var e = x._s[k][i] - y._s[k][i] - m; v += e*e/(n - 1); } var h = 1.96*Math.sqrt(v/n); return {m:m, lo:m - h, hi:m + h}; }
/* Presets. The environment (shocks, automation, exogenous inflation, years, population) comes from the Compassionism scenario P.
 * Every comparator gets the same COLA rule as BU (the Inflation Surge Protocol, 5%; D6). */
var TB_XC_AMT = 9.90*365;          /* X-Cents adult daily exchange (d17): a dime for $10 a day, net $9.90: derived, $3,613.50 a year */
var TB_GROC = {cut:0.15, cap:140}; /* d27. cut: nyc.gov (Jul 27, 2026): 30% off a core basket, projected to cut the average grocery bill 15%; a promise,
                                    * not an observed result. cap: the $70M capital budget for five stores over 20 years, per covered adult-year, at an
                                    * assumed 5,000 regular adult shoppers per store: a logged placeholder (the shopper count is unsourced), swept. */
var TB_ENDOW_THRESH = 25000;       /* d27: year-0 wealth below the model's wealth-poverty line (CFG.POVERTY_LINE) */
var TB_NIT_T = 0.5;                /* d27: central phase-out rate; 0.3 and 0.7 swept */
/* Session 11 (Duke's notes on the v4.22 page; dashboard d44-d47).
 * TB_GROC_PILOT  the NYC plan's five stores serve a small share of the city's shoppers: the Mayor puts the existing count at
 *                "more than the thousand existing grocery stores" (nyc.gov transcript, Jul 27, 2026), so five equal-sized stores
 *                would serve 5/1,005 = 0.5%; the first sites are 9,000 sq ft, smaller than a typical supermarket, so this is if
 *                anything high. Derived. The full-cover row (cover 1) is the network at a scale that serves every adult.
 * TB_XC_P1       X-Cents "Power of 1" (the CurrentSea X-Change paper, s3.2): at designated times every coin is worth $1 for
 *                necessities, so food bought with pennies costs 1 cent per dollar (a 99% cut). One designated day a week
 *                (Duke, Sep 28): the share of food bought that day, f, is 1 if adults do their weekly food shopping on it (central)
 *                and 1/7 if they do not shift any (swept). Food only: rent and utilities need the paper's phase-2 service-provider
 *                integration, which the model does not assume centrally; the X-Cents site names food and housing, so a row with
 *                housing (rent and utilities, HUD FMR incl. tenant-paid utilities) paid the same way is shown beside it (d48).
 * TB_UBI_PROP, TB_NIT_PROP, TB_ENDOW_PROP  each comparator at its proposers' size (d45): $1,000 a month (the amount paid in
 *                Vivalt et al.'s study); the guarantee at the 2026 HHS poverty guideline for one person ($15,960, aspe.hhs.gov),
 *                50% phase-out, inside the range the 1968-82 NIT experiments tested; the stakeholder grant's $80,000 of 1999
 *                (Ackerman and Alstott) in 2025 dollars, x 321.943/166.6 (BLS CPI-U annual averages) = $154,594.
 * TB_TOPUP_S     d39/N3: the share of the flat BU moved to the needs-based top-up at equal cost in `topup` (0.1, 0.25 and 0.5 swept).
 *                TB_TOPUP_S_A5 = 0.1 in a5 and on the page (d44): the only share tested that deepens the FGT2 cut in all four cells. */
var TB_GROC_PILOT = 0.005, TB_XC_P1 = 0.99, TB_UBI_PROP = 12000, TB_NIT_PROP = 15960, TB_ENDOW_PROP = 154594, TB_TOPUP_S = 0.25, TB_TOPUP_S_A5 = 0.1;
/* Session 8 (d33; dashboard s24): every Compassionism-versus-comparator result is shown with the PTF/PTH inflation damping on and
 * off. The damping scales the exogenous inflation rate only, so where that rate is 0 the damping-off rows equal the rows shown
 * (checked by `unit`) and are not rerun. */
var D33_NOTE = '  (d33: the PTF/PTH inflation damping acts only on exogenous inflation, which is 0 here, so the damping-off rows equal the rows shown; checked by `unit`.)';
function tbComp(P, spec){ return Object.assign({}, baselineFor(P, true), {nAgents:P.nAgents, years:P.years, cola:true, colaThresh:CFG.COLA_HUB_THRESH, tb:spec}); }
function tbCCO(P, bu){ var q = nextRoundPreset(Object.assign({}, P, bu !== undefined ? {bu:bu} : {})); q.tb = {}; return q; }
function tbPresets(P){
  return {
    baseline: function(){ return tbComp(P, {}); },
    ubi: function(x){ return tbComp(P, {ubi:x}); },
    nit: function(G, t){ return tbComp(P, {nit:{G:G, t:t === undefined ? TB_NIT_T : t}}); },
    groc: function(cover, cap){ return tbComp(P, {groc:{cut:TB_GROC.cut, cover:cover, cap:cap === undefined ? TB_GROC.cap : cap}}); },
    endow: function(W){ return tbComp(P, {endow:{amt:W, thresh:TB_ENDOW_THRESH}}); },
    xc: function(delta){ return tbComp(P, {xc:{amt:TB_XC_AMT, delta:delta || 0}}); },
    cco: function(bu){ return tbCCO(P, bu); },
    ccoAlone: function(bu){ return tbCCO(ccoOnlyFor(P), bu); },
    /* session 11 */
    grocPilot: function(){ return tbComp(P, {groc:{cut:TB_GROC.cut, cover:TB_GROC_PILOT, cap:TB_GROC.cap}}); },
    xcFull: function(f, h){ return tbComp(P, {xc:{amt:TB_XC_AMT, delta:0}, groc:{cut:TB_XC_P1*(f === undefined ? 1 : f), cover:1, cap:0, housing:!!h}}); },
    ccoTop: function(G, s, t){ var q = tbCCO(P, P.bu*(1 - (s === undefined ? TB_TOPUP_S : s))); q.tb = {nit:{G:G, t:t === undefined ? TB_NIT_T : t, part:true}}; return q; }
  };
}
/* Matching a comparator to a target gross cost per adult-year (year-0 dollars) on pilot seeds 1..Np. UBI: one proportional
 * correction (COLA and deflation make real cost differ slightly from the nominal amount). NIT: secant on G. Endowment: exact
 * (paid in year 0, so cost = W x eligible share / years). */
function tbMatch(kind, target, P, Np, o, x){
  var PR = tbPresets(P);
  function cost(q){ return tbStudy([{p:q}], Np, P, o)[0].cost; }
  if (kind === 'ubi'){ var c = cost(PR.ubi(target)); return target*target/Math.max(1, c); }
  if (kind === 'endow'){ var c1 = cost(PR.endow(100000)); return 100000*target/Math.max(1e-9, c1); }
  if (kind === 'nit'){ var x0 = target, x1 = 2*target, f0 = cost(PR.nit(x0)) - target, f1 = cost(PR.nit(x1)) - target;
    for (var it = 0; it < 6 && Math.abs(f1) > 0.002*target; it++){ var x2 = x1 - f1*(x1 - x0)/(f1 - f0); x0 = x1; f0 = f1; x1 = Math.max(100, x2); f1 = cost(PR.nit(x1)) - target; }
    return x1; }
  if (kind === 'ccoTop'){  /* session 11 (d39/N3): the top-up's guarantee G that brings Compassionism with a smaller flat BU back to the target */
    var xs = typeof x === 'object' ? x : {s:x}, g0 = 0.25*target, g1 = target, h0 = cost(PR.ccoTop(g0, xs.s, xs.t)) - target, h1 = cost(PR.ccoTop(g1, xs.s, xs.t)) - target;
    for (var jt = 0; jt < 8 && Math.abs(h1) > 0.002*target; jt++){ var g2 = g1 - h1*(g1 - g0)/(h1 - h0); g0 = g1; h0 = h1; g1 = Math.max(0, g2); h1 = cost(PR.ccoTop(g1, xs.s, xs.t)) - target; }
    return g1; }
  throw new Error('tbMatch: unknown kind ' + kind);
}
/* Tests (harness-only; run by `unit`). Each restores every switch. */
function tbUnitSuite(){
  var out = [];
  function t(name, fn){ var sv = {cm:CONVERSION_MODEL, nr:applyNR6()};
    try { var r = fn(); out.push({name:name, pass:!!r.pass, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, detail:'threw: ' + e.message}); }
    finally { CONVERSION_MODEL = sv.cm; resetNR6(sv.nr); TB = null; LABOR = null; PRICE = null; LEDGER = null; } }
  var FI = FULL_INTEGRATION, PR = tbPresets(FI), S1 = function(P, sd){ return s3BaseS(P, sd); };
  function same(r1, r2, keys){ return keys.every(function(k){ return r1[k] === r2[k]; }); }
  t('inert: TB off, and TB on with no p.tb, leave priceRun bit-identical (Full Integration, seed 1, labor on, both models)', function(){
    var ok = true, ks = ['endoAnn','pov','bleiPov','basketPov','medWealthReal','dE'];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; var P = nextRoundPreset(FI), S = S1(P, 1);
      var r0 = priceRun(P, 1, {a:0.9, labor:LABOR_DEFAULTS, wIdx:1}, S).res; TB = {tau:0, X:0, inkindRho:true}; var r1 = priceRun(P, 1, {a:0.9, labor:LABOR_DEFAULTS, wIdx:1}, S).res; TB = null;
      if (!same(r0, r1, ks)) ok = false; });
    return {pass:ok, detail:'endogenous inflation, wealth, BLEI and basket poverty, median wealth and earnings identical'};
  });
  t("plumbing: tbRun with fin 'none', inkindRho and neutralGate off and no comparator reproduces priceRun exactly (Full Integration and Adverse, seeds 1-2, labor on, both models)", function(){
    var ok = true, v = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; [FI, ADVERSE_REFERENCE].forEach(function(E){ for (var sd = 1; sd <= 2; sd++){
      var P = nextRoundPreset(E), S = S1(P, sd), o = {a:0.7, labor:LABOR_DEFAULTS, wIdx:1};
      var r0 = priceRun(P, sd, o, S).res, r1 = tbRun(Object.assign({}, P, {tb:{}}), sd, Object.assign({fin:'none', inkindRho:false, neutralGate:false}, o), S).res;
      if (r0.endoAnn !== r1.endoAnn || r0.pov !== r1.pov || r0.bleiPov !== r1.bleiPov || r0.dE !== r1.dE || Math.abs(r0.basketPov - r1.fgt0) > 1e-9) ok = false;
      if (sd === 1) v.push(cm + ' ' + (r1.endoAnn*100).toFixed(3) + '%'); } }); });
    return {pass:ok, detail:'inflation, wealth and BLEI poverty, earnings identical; testbed FGT0 equals basket poverty; ' + v.join(', ')};
  });
  t('fairness: an NIT with t = 0 is a UBI of G, and X-Cents with delta 0 is a UBI of $3,613.50 (seed 1, tax and money financing)', function(){
    var ok = true, v = [];
    ['tax','money'].forEach(function(fin){ var S = S1(FI, 1), o = {fin:fin, grp:{part:FI.partRate, pth:FI.pthUptake}};
      var u = tbRun(PR.ubi(8000), 1, o, S).res, n = tbRun(PR.nit(8000, 0), 1, o, S).res, u2 = tbRun(PR.ubi(TB_XC_AMT), 1, o, S).res, x = tbRun(PR.xc(0), 1, o, S).res;
      if (!same(u, n, TB_KEYS) || !same(u2, x, TB_KEYS)) ok = false; v.push(fin + ': UBI $8,000 FGT2 ' + u.fgt2.toFixed(3) + ' = NIT ' + n.fgt2.toFixed(3)); });
    return {pass:ok, detail:v.join('; ')};
  });
  t('income effect and phase-out: with eps 0, a UBI cuts earnings by exactly rho x UBI (floor not binding); an NIT phase-out lowers earnings in its range and not above it (seed 1, fin none)', function(){
    var S = S1(FI, 1), L0 = {rho:0.16, rhoBU:0.16, rhoR:0, eps:0, delta:0}, o = {fin:'none', labor:L0};
    var u = tbRun(PR.ubi(6000), 1, o, S).res, gap = Math.abs((u.E0 - u.E) - 0.16*6000);
    var L1 = {rho:0, rhoBU:0, rhoR:0, eps:0.33, delta:0}, b1 = tbRun(PR.baseline(), 1, {fin:'none', labor:L1}, S).res, n1 = tbRun(PR.nit(10000, 0.5), 1, {fin:'none', labor:L1}, S).res;
    return {pass:u.zero === 0 && gap < 1e-6 && n1.E < b1.E, detail:'UBI: earnings fall $' + (u.E0 - u.E).toFixed(4) + ' vs $' + (0.16*6000).toFixed(4) + ' against the same run with no response (floor binds in ' + (u.zero*100).toFixed(2) + '% of adult-years); NIT (rho 0, eps 0.33): $' + b1.E.toFixed(0) + ' to $' + n1.E.toFixed(0)};
  });
  t('tax financing: the treasury funds the program to within 5% of its cost over 20 years, and the contribution reduces earnings (UBI $6,000, Full Integration engine; seeds 1-3)', function(){
    var ok = true, v = [];
    for (var sd = 1; sd <= 3; sd++){ var S = S1(FI, sd), g = {grp:{part:FI.partRate, pth:FI.pthUptake}};
      [PR.ubi(6000), PR.cco()].forEach(function(q, j){ var r = tbRun(q, sd, Object.assign({fin:'tax'}, g), S).res, rn = tbRun(q, sd, Object.assign({fin:'none'}, g), S).res;
        if (Math.abs(r.treas) > 0.05*r.need || !(r.E < rn.E)) ok = false; if (sd === 1) v.push((j ? 'Full Integration' : 'UBI') + ': tau ' + (r.tauMean*100).toFixed(1) + '%, treasury ' + (r.treas/r.need*100).toFixed(2) + '% of cost'); }); }
    return {pass:ok, detail:v.join('; ')};
  });
  t("money financing: with aT = 1 and essentials supply matched, a UBI adds no endogenous inflation; inflation rises as aT falls (UBI $6,000, seed 1)", function(){
    var S = S1(FI, 1), o = {fin:'money', essMatched:true, grp:{part:FI.partRate, pth:FI.pthUptake}}, r1 = tbRun(PR.ubi(6000), 1, Object.assign({aT:1}, o), S).res, r5 = tbRun(PR.ubi(6000), 1, Object.assign({aT:0.5}, o), S).res, r0 = tbRun(PR.ubi(6000), 1, Object.assign({aT:0}, o), S).res;
    var b = tbRun(PR.baseline(), 1, o, S).res;
    return {pass:Math.abs(r1.endoAnn - b.endoAnn) < 1e-12 && r0.endoAnn > r5.endoAnn && r5.endoAnn > r1.endoAnn, detail:'endogenous inflation at aT 1 / 0.5 / 0: ' + [r1, r5, r0].map(function(r){ return (r.endoAnn*100).toFixed(2); }).join(' / ') + ' pt/yr (Baseline ' + (b.endoAnn*100).toFixed(2) + ')'};
  });
  t('cost ledger: a UBI costs its amount; an endowment costs W x eligible share / years; grocery at zero cover costs nothing and equals the Baseline (seed 1, fin none)', function(){
    var S = S1(FI, 1), o = {fin:'none', essMatched:true}, u = tbRun(PR.ubi(5000), 1, o, S).res, e = tbRun(PR.endow(20000), 1, o, S).res, g = tbRun(PR.groc(0, 0), 1, o, S).res, b = tbRun(PR.baseline(), 1, o, S).res;
    RNG = mulberry32(1 + 700003); var el = makeLatentPopulation(FI.nAgents).filter(function(l){ return l.wealth < TB_ENDOW_THRESH; }).length/FI.nAgents;
    return {pass:Math.abs(u.cost - 5000) < 1e-6 && Math.abs(e.cost - 20000*el/FI.years) < 1e-6 && g.cost === 0 && same(g, b, TB_KEYS),
      detail:'UBI $' + u.cost.toFixed(2) + '; endowment $' + e.cost.toFixed(2) + ' (eligible ' + (el*100).toFixed(1) + '%); grocery at zero cover identical to the Baseline'};
  });
  t('d26 threshold: with X above every earner, no one contributes and the treasury runs the full deficit; at X = 0 the contribution matches the tax-financed default (UBI $6,000, seed 1)', function(){
    var S = S1(FI, 1), g = {grp:{part:FI.partRate, pth:FI.pthUptake}}, r0 = tbRun(PR.ubi(6000), 1, Object.assign({fin:'tax'}, g), S).res, rX = tbRun(PR.ubi(6000), 1, Object.assign({fin:'tax', X:1e9}, g), S).res;
    var rD = tbRun(PR.ubi(6000), 1, Object.assign({fin:'tax', X:0}, g), S).res;
    return {pass:rX.tax === 0 && Math.abs(rX.treas + rX.need) < 1e-6 && same(r0, rD, TB_KEYS), detail:'contribution at X = 1e9: $' + rX.tax.toFixed(2) + '; treasury ' + rX.treas.toFixed(0) + ' = -need'};
  });
  t('session 7: hybrid financing equals tax financing for a design with no conversion (UBI $6,000), and d24 (b) equals the default at a = 0 (Full Integration, seed 1)', function(){
    var ks = ['cost','tauMean','fgt2','pov','dE','endoAnn'], u = PR.ubi(6000), c = PR.cco();
    var rT = tbRun(u, 1, {fin:'tax'}, S1(FI, 1)).res, rH = tbRun(u, 1, {fin:'hybrid', a:0.5}, S1(FI, 1)).res;
    var rM = tbRun(c, 1, {fin:'money', a:0}, S1(FI, 1)).res, rB = tbRun(c, 1, {fin:'money', a:0, buAtA:true}, S1(FI, 1)).res;
    return {pass:same(rT, rH, ks) && same(rM, rB, ks), detail:'UBI tax/hybrid FGT2 ' + rT.fgt2.toFixed(4) + ' / ' + rH.fgt2.toFixed(4) + '; money (a)/(b) at a = 0 inflation ' + (rM.endoAnn*100).toFixed(3) + ' / ' + (rB.endoAnn*100).toFixed(3)};
  });
  t('session 7: the i3 switches (FBS_BU_ONCE, PTH_APPR_CONSERVE) are restored after a per-row study, and FBS_BU_ONCE changes only the engine model (seed 1)', function(){
    var q = PR.cco(), base = tbStudy([{p:q}], 1, FI, {fin:'tax'})[0], fix = tbStudy([{p:q, g:{FBS_BU_ONCE:true, PTH_APPR_CONSERVE:true}}], 1, FI, {fin:'tax'})[0];
    var restored = FBS_BU_ONCE === false && PTH_APPR_CONSERVE === false;
    CONVERSION_MODEL = 'framework'; var f0 = tbStudy([{p:q}], 1, FI, {fin:'tax'})[0], f1 = tbStudy([{p:q, g:{FBS_BU_ONCE:true}}], 1, FI, {fin:'tax'})[0];
    return {pass:restored && base.fgt2 !== fix.fgt2 && f0.fgt2 === f1.fgt2, detail:'engine FGT2 ' + base.fgt2.toFixed(3) + ' -> ' + fix.fgt2.toFixed(3) + '; framework ' + f0.fgt2.toFixed(3) + ' = ' + f1.fgt2.toFixed(3) + '; restored: ' + restored};
  });
  t('session 8 (d33): with no exogenous inflation the PTF/PTH damping switch changes nothing (Full Integration, seed 1, tax and money, both models); in the Adverse Environment it lowers the price level', function(){
    var ok = true, v = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; ['tax','money'].forEach(function(fin){
      var R = tbStudy([{p:PR.cco()}, {p:PR.cco(), o:{noDamp:true}}], 1, FI, {fin:fin});
      if (!same(R[0], R[1], TB_KEYS)) ok = false; }); });
    CONVERSION_MODEL = 'engine'; var PA = tbPresets(ADVERSE_REFERENCE), RA = tbStudy([{p:PA.cco()}, {p:PA.cco(), o:{noDamp:true}}], 1, ADVERSE_REFERENCE, {fin:'tax'});
    return {pass:ok && RA[0].pLev20 < RA[1].pLev20, detail:'reference: identical on every key; Adverse price level at year 20 ' + RA[0].pLev20.toFixed(4) + ' (damped) vs ' + RA[1].pLev20.toFixed(4)};
  });
  t('session 8 (A5): person-years poor per adult = person-year FGT0 x 20 / 100; ever poor >= year-20 FGT0 and >= chronic; spells 1-20 years; Gini of known vectors; with no labor response hours are unchanged (seeds 1-2)', function(){
    var R = tbStudy([{p:PR.baseline()}, {p:PR.cco()}, {p:PR.ubi(8000)}], 2, FI, {fin:'tax'}), ok = true, v = [];
    R.forEach(function(r){ for (var i = 0; i < 2; i++){ var py = r._s.pyPoor[i], f = r._s.fgt0PY[i]*FI.years/100;
      if (Math.abs(py - f) > 1e-9 || r._s.everPoor[i] < r._s.fgt0[i] - 1e-9 || r._s.everPoor[i] < r._s.chronic[i] - 1e-9 || r._s.spellMean[i] < 1 || r._s.spellMean[i] > FI.years) ok = false; } });
    var g1 = giniOfArr([1,1,1,1]), g2 = giniOfArr([0,0,0,1]), g3 = giniOfArr([1,2,3,4]);
    var L0 = {rho:0, rhoBU:0, rhoR:0, eps:0, delta:0}, z = tbStudy([{p:PR.cco()}], 1, FI, {fin:'none', labor:L0})[0];
    var gOk = Math.abs(g1) < 1e-12 && Math.abs(g2 - 0.75) < 1e-12 && Math.abs(g3 - 0.25) < 1e-12;
    return {pass:ok && gOk && Math.abs(z.hrs) < 1e-12 && z.emp === 100, detail:'Gini [1,1,1,1] ' + g1.toFixed(3) + ', [0,0,0,1] ' + g2.toFixed(3) + ', [1,2,3,4] ' + g3.toFixed(3) + '; Compassionism years poor per adult ' + R[1].pyPoor.toFixed(3) + ' = ' + (R[1].fgt0PY*FI.years/100).toFixed(3) + '; no-response hours ' + (z.hrs*100).toFixed(4) + '%'};
  });
  t('session 8 (A5): the price path. Tax-financed Adverse Baseline: price level at year 20 = 1.02^19 (no program, no damping); a UBI below the 5% COLA trigger is worth 1/price level; at reference every level is 1 (seed 1)', function(){
    var PA = tbPresets(ADVERSE_REFERENCE), R = tbStudy([{p:PA.baseline()}, {p:PA.ubi(6000)}], 1, ADVERSE_REFERENCE, {fin:'tax'}), r0 = tbStudy([{p:PR.ubi(6000)}], 1, FI, {fin:'tax'})[0];
    var want = Math.pow(1 + ADVERSE_REFERENCE.inflRate, FI.years - 1);
    return {pass:Math.abs(R[0].pLev20 - want) < 1e-9 && Math.abs(R[1].realT - 1/R[1].pLev20) < 1e-12 && r0.pLev20 === 1 && r0.realT === 1,
      detail:'Adverse Baseline price level ' + R[0].pLev20.toFixed(6) + ' vs 1.02^19 = ' + want.toFixed(6) + '; UBI real value $' + R[1].realT.toFixed(4)};
  });
  t('session 9 (i3-2): N7_BLEI moves attribution only. With no labor response and every raise matched (aw 1) every figure is identical; on the Baseline it changes nothing; program-carried BLEI raises are a subset of BLEI raises; the switch is restored (seeds 1-2)', function(){
    var o = {fin:'tax', labor:null}, R = tbStudy([{p:PR.cco(), o:o}, {p:PR.cco(), o:o, g:{N7_BLEI:true}}, {p:PR.baseline()}, {p:PR.baseline(), g:{N7_BLEI:true}}, {p:PR.cco()}, {p:PR.cco(), g:{N7_BLEI:true}}], 2, FI, {fin:'tax'});
    var sub = R.every(function(r){ for (var i = 0; i < 2; i++) if (r._s.bleiP[i] > r._s.bleiR[i] + 1e-12) return false; return true; });
    return {pass:same(R[0], R[1], TB_KEYS) && same(R[2], R[3], TB_KEYS) && R[2].bleiP === 0 && sub && N7_BLEI === false && R[5].hrs !== R[4].hrs,
      detail:'no response: identical; Baseline: identical, program-carried share ' + R[2].bleiP.toFixed(2) + '%; Full Integration with the response: hours ' + (R[4].hrs*100).toFixed(3) + '% -> ' + (R[5].hrs*100).toFixed(3) + '% (' + R[4].bleiP.toFixed(2) + '% of adult-years carried over the gate)'};
  });
  t('session 10 (d40): the testbed profile turns N7_BLEI on for rows that do not set it, a row\'s own setting still wins, and the global default is restored to false (seeds 1-2)', function(){
    var sv = tbSetG(TB_PROFILE_G), R, on;
    try { on = N7_BLEI; R = tbStudy([{p:PR.cco()}, {p:PR.cco(), g:{N7_BLEI:true}}, {p:PR.cco(), g:{N7_BLEI:false}}], 2, FI, {fin:'tax'}); } finally { tbSetG(sv); }
    return {pass:TB_PROFILE_G.N7_BLEI === true && on === true && same(R[0], R[1], TB_KEYS) && R[2].hrs !== R[0].hrs && N7_BLEI === false,
      detail:'profile row = explicit on: ' + same(R[0], R[1], TB_KEYS) + '; hours ' + (R[0].hrs*100).toFixed(3) + '% (profile) vs ' + (R[2].hrs*100).toFixed(3) + '% (row sets it off); global after: ' + N7_BLEI};
  });
  t('d19 row switch: a per-row PATHWAY_OFF entry is restored after each row, leaves a comparator unchanged, and lowers Full Integration earnings (seeds 1-2)', function(){
    var R = tbStudy([{p:PR.ubi(6000)}, {p:PR.ubi(6000), pw:{octaveWage:true}}, {p:PR.cco()}, {p:PR.cco(), pw:{octaveWage:true}}], 2, FI, {fin:'tax'});
    var restored = Object.keys(PATHWAY_OFF).every(function(k){ return PATHWAY_OFF[k] === false; });
    return {pass:restored && same(R[0], R[1], TB_KEYS) && R[3].E < R[2].E,
      detail:'UBI rows identical; Full Integration earnings $' + R[2].E.toFixed(0) + ' on, $' + R[3].E.toFixed(0) + ' off; switches restored: ' + restored};
  });
  /* Session 11 */
  t('session 11 top-up (d39, d44): with G = 0 Compassionism with a top-up equals Compassionism at the smaller BU; with G > 0 it pays participants only, and costs more (seed 1, tax)', function(){
    var q0 = tbCCO(FI, FI.bu*0.9), R = tbStudy([{p:q0}, {p:PR.ccoTop(0, 0.1)}, {p:PR.ccoTop(8000, 0.1)}], 1, FI, {fin:'tax'});
    var S = S1(FI, 1), got = {part:0, non:0}; TB = Object.assign({}, TB_DEFAULTS, {tau:0, X:0});
    var P2 = PR.ccoTop(8000, 0.1), y = tbYear(P2, 1), ag = [{inCCO:true}, {inCCO:false}].map(function(a){ return tbCashFlow(a, y, 0, 1), a._tbNit; }); TB = null;
    return {pass:same(R[0], R[1], TB_KEYS) && ag[0] === 8000 && ag[1] === 0 && R[2].cost > R[1].cost,
      detail:'G 0 identical to BU x 0.9: ' + same(R[0], R[1], TB_KEYS) + '; with no earnings a participant gets $' + ag[0] + ', a non-participant $' + ag[1] + '; cost $' + R[1].cost.toFixed(0) + ' to $' + R[2].cost.toFixed(0)};
  });
  t('session 11 X-Cents and grocery: Power of 1 with f = 0 equals the flat exchange; five stores cost a small fraction of the full network (under 3% on 2 seeds; 0.5% at 500); adding housing raises the cut (seeds 1-2, tax)', function(){
    var R = tbStudy([{p:PR.xc(0)}, {p:PR.xcFull(0)}, {p:PR.xcFull(1)}, {p:PR.xcFull(1, true)}, {p:PR.groc(1)}, {p:PR.grocPilot()}], 2, FI, {fin:'tax'});
    var ratio = R[5].cost/R[4].cost;
    return {pass:same(R[0], R[1], TB_KEYS) && R[3].cost > R[2].cost && R[2].cost > R[0].cost && ratio > 0 && ratio < 0.03,
      detail:'f 0 identical to the flat exchange: ' + same(R[0], R[1], TB_KEYS) + '; costs $' + R[0].cost.toFixed(0) + ' / $' + R[2].cost.toFixed(0) + ' (food) / $' + R[3].cost.toFixed(0) + ' (food and housing); five stores ' + (ratio*100).toFixed(2) + '% of the full network\'s cost (2 seeds)'};
  });
  return out;
}
Object.assign(module.exports, { tbRun, tbStudy, tbDiff, tbPresets, tbMatch, tbUnitSuite, applyNR6, resetNR6, NR6, TB_PROFILE_G, TB_KEYS, TB_XC_AMT, TB_GROC, giniOfArr, setTB:function(x){ TB = x; } });

/* N1, session 15 (s33): project hiring's tests (harness-only). Each restores PROJ, FW and the conversion model. */
function projUnitSuite(){
  var out = [];
  function t(name, fn){ var sv = {cm:CONVERSION_MODEL, pj:PROJ, cap:FW.octaveCapBase, ds:FW.directedShare, nr:applyNR6()};
    try { var r = fn(); out.push({name:name, pass:!!r.pass, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, detail:'threw: ' + e.message}); }
    finally { CONVERSION_MODEL = sv.cm; PROJ = sv.pj; FW.octaveCapBase = sv.cap; FW.directedShare = sv.ds; resetNR6(sv.nr); TB = null; LABOR = null; PRICE = null; LEDGER = null; } }
  var FI = FULL_INTEGRATION, PR = tbPresets(FI);
  function pj(o){ return Object.assign({}, PROJ_DEFAULTS, o || {}); }
  function same(r1, r2, ks){ return ks.every(function(k){ return r1[k] === r2[k]; }); }
  var KS = TB_KEYS.filter(function(k){ return k.indexOf('pj') !== 0; });
  /* one plain engine run (no price module, no inflation), returning the agents and the project tallies */
  function plain(P, seed){ RNG = mulberry32(seed + 700003); var ag = makeLatentPopulation(P.nAgents).map(function(l){ return instantiateAgent(l, P); });
    RNG = mulberry32(seed); for (var y = 0; y < P.years; y++) runYear(ag, y, P, {active:false, incomeMultiplier:1.0, yearsLeft:0});
    return {ag:ag, acc:PJS ? PJS.acc : null, fin:PJS && PJS.prev ? PJS.prev.pool + PJS.prev.gpool : 0}; }
  t('inert: an empty pool (share 0, no gift) is bit-identical to PROJ off on every testbed measure (engine; framework with N2 unfunded), seeds 1-2, labor on', function(){
    var ok = true, P = nextRoundPreset(FI), S;
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; for (var sd = 1; sd <= 2; sd++){ S = s3BaseS(P, sd);
      if (cm === 'framework') FW.directedShare = 0;
      PROJ = null; var r0 = tbRun(PR.cco(), sd, {fin:'tax', grp:{part:FI.partRate, pth:FI.pthUptake}}, S).res;
      PROJ = pj({share:0, gift:0}); var r1 = tbRun(PR.cco(), sd, {fin:'tax', grp:{part:FI.partRate, pth:FI.pthUptake}}, S).res;
      if (!same(r0, r1, KS)) ok = false; FW.directedShare = 1; } });
    return {pass:ok, detail:KS.length + ' measures identical in both models'};
  });
  t('conservation: BU into the pool = BU allocated + the pool left at the end; BU allocated = BU converted + BU saved (Full Integration, seed 1, both models)', function(){
    var ok = true, v = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; PROJ = pj(); var r = plain(FI, 1), sv = 0;
      r.ag.forEach(function(a){ sv += a._pjSaved || 0; });
      var e1 = Math.abs(r.acc.pool - r.acc.alloc - r.fin), e2 = Math.abs(r.acc.alloc - r.acc.conv - sv);
      if (e1 > 1e-6*r.acc.pool || e2 > 1e-6*r.acc.pool) ok = false;
      v.push(cm + ': in ' + Math.round(r.acc.pool) + ' = allocated ' + Math.round(r.acc.alloc) + ' + left ' + Math.round(r.fin) + '; converted ' + Math.round(r.acc.conv) + ' + saved ' + Math.round(sv)); });
    return {pass:ok, detail:v.join('; ')};
  });
  t('capacity (cap on): project BU never exceed the capacity left after the own-spending conversion (12 x base x 2^octave a year), and with a tiny base they are saved, not lost (Full Integration, seed 1, engine)', function(){
    PROJ = pj({cap:true}); var r = plain(FI, 1), a0 = r.acc.overCap;
    FW.octaveCapBase = 1; var r2 = plain(FI, 1), sv = 0; r2.ag.forEach(function(a){ sv += a._pjSaved || 0; });
    var cons = Math.abs(r2.acc.alloc - r2.acc.conv - sv) < 1e-6*Math.max(1, r2.acc.alloc);
    return {pass:a0 === 0 && r2.acc.overCap === 0 && sv > 0 && cons, detail:'over-capacity agent-years ' + a0 + ' (base 1,000) and ' + r2.acc.overCap + ' (base 1); saved at base 1: ' + Math.round(sv) + ' BU; conservation ' + cons};
  });
  t("rate: the contract rate lies within participants' own rates, and 'max' pays at least 'own' per BU (Full Integration, seed 1, engine)", function(){
    PROJ = pj(); var r = plain(FI, 1), gM = r.acc.gross/Math.max(1e-9, r.acc.conv), rc = r.acc.rc/r.acc.rcN;
    var lo = Infinity, hi = 0; r.ag.forEach(function(a){ if (a.inCCO){ lo = Math.min(lo, a._pjR); hi = Math.max(hi, a._pjR); } });
    PROJ = pj({rate:'own'}); var r2 = plain(FI, 1), gO = r2.acc.gross/Math.max(1e-9, r2.acc.conv);
    return {pass:rc >= 1 && rc <= FI.maxMult*CFG.PHI_RATIO && gM >= gO, detail:'mean contract rate ' + rc.toFixed(3) + 'x (last year own rates ' + lo.toFixed(2) + '-' + hi.toFixed(2) + 'x); gross per BU ' + gM.toFixed(3) + ' (max) vs ' + gO.toFixed(3) + ' (own)'};
  });
  t("willingness: under 'capq' no one is allocated project BU at pay per hour at or below their own wage; 'capqAll' may be (Full Integration, seed 1, engine)", function(){
    PROJ = pj(); var r = plain(FI, 1); PROJ = pj({alloc:'capqAll'}); var r2 = plain(FI, 1);
    return {pass:r.acc.unwilling === 0, detail:'unwilling allocations: ' + r.acc.unwilling + ' (capq), ' + r2.acc.unwilling + ' (capqAll)'};
  });
  t('random numbers: project hiring adds no draw (8 per agent-year, Full Integration, 20 years, both models)', function(){
    var ok = true, v = [];
    ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm; var n = [];
      [null, pj()].forEach(function(q){ PROJ = q; RNG = mulberry32(700004); var ag = makeLatentPopulation(FI.nAgents).map(function(l){ return instantiateAgent(l, FI); });
        var base = mulberry32(1), k = 0; RNG = function(){ k++; return base(); };
        for (var y = 0; y < FI.years; y++) runYear(ag, y, FI, {active:false, incomeMultiplier:1.0, yearsLeft:0}); n.push(k); });
      if (n[0] !== n[1] || n[0] !== 8*FI.nAgents*FI.years) ok = false; v.push(cm + ' ' + n.join(' / ')); });
    return {pass:ok, detail:v.join('; ') + ' (off / on)'};
  });
  t("gift: 'forward' puts 1,000 BU per participant into year 1's pool and, with share 0, all of it is allocated; 'holder' gives each participant their own (Full Integration, seed 1, engine)", function(){
    PROJ = pj({share:0}); var r = plain(FI, 1), nP = r.ag.filter(function(a){ return a.inCCO; }).length;
    PROJ = pj({share:0, giftMode:'holder'}); var r2 = plain(FI, 1), sv = 0; r2.ag.forEach(function(a){ sv += a._pjGiftH || 0; });
    var ok = Math.abs(r.acc.gift - 1000*nP) < 1e-6 && Math.abs(r.acc.alloc - 1000*nP) < 1e-6 && r2.acc.alloc === 0 && Math.abs(r2.acc.gift - r2.acc.giftConv - sv) < 1e-6;
    return {pass:ok, detail:nP + ' participants; forward: gift ' + r.acc.gift + ', allocated ' + Math.round(r.acc.alloc) + '; holder: gift ' + r2.acc.gift + ' = converted ' + Math.round(r2.acc.giftConv) + ' + held ' + Math.round(sv)};
  });
  t("hours: 'displace' takes project hours out of wage earnings and 'side' does not (Full Integration, seed 1, engine)", function(){
    PROJ = pj({hours:'displace'}); var r = plain(FI, 1); PROJ = pj({hours:'side'}); var r2 = plain(FI, 1);
    return {pass:r.acc.disp > 0 && r2.acc.disp === 0 && r.acc.hrs > 0 && Math.abs(r.acc.hrs - r2.acc.hrs) < 1e-9*r.acc.hrs, detail:'wage earnings displaced $' + Math.round(r.acc.disp) + ' (displace) vs $' + r2.acc.disp + ' (side); project hours ' + Math.round(r.acc.hrs) + ' in both'};
  });
  t("financing (d66, i7): 'payg' pays for the launch gift in the year it is converted, so the year-2 contribution rises; 'run' spreads it over the run, like the endowment, so each year carries a small share; the program costs more than with no gift either way (seed 1, engine, tax)", function(){
    var P = nextRoundPreset(FI), S = s3BaseS(P, 1), o = tbOpts({fin:'tax', grp:{part:FI.partRate, pth:FI.pthUptake}});
    PROJ = pj({share:0, gift:0}); var tau0 = tbRunCore(PR.cco(), 1, o, S, 0, 1).tau0, y = tbRunCore(PR.cco(), 1, o, S, tau0, P.years);
    PROJ = pj({share:0, giftFin:'payg'}); var x = tbRunCore(PR.cco(), 1, o, S, tau0, P.years);
    PROJ = pj({share:0, giftFin:'run'}); var z = tbRunCore(PR.cco(), 1, o, S, tau0, P.years);
    var jP = x.path[2].tau - y.path[2].tau, jR = z.path[2].tau - y.path[2].tau, tail = z.path[10].tau - y.path[10].tau;
    return {pass:jP > 0.02 && jR >= 0 && jR < jP/5 && tail > 0 && x.res.cost > y.res.cost && z.res.cost > y.res.cost && Math.abs(x.res.cost - z.res.cost) < 0.01*x.res.cost,
      detail:'year-2 contribution ' + (x.path[2].tau*100).toFixed(2) + '% (as you go) and ' + (z.path[2].tau*100).toFixed(2) + '% (over the run) vs ' + (y.path[2].tau*100).toFixed(2) + '% with no gift; year 10 +' + (tail*100).toFixed(2) + ' pt over the run; cost $' + Math.round(x.res.cost) + ' / $' + Math.round(z.res.cost) + ' vs $' + Math.round(y.res.cost) + ' per adult-year'};
  });
  return out;
}
Object.assign(module.exports, { projUnitSuite, PROJ_DEFAULTS, tbSetG, setProj:function(x){ PROJ = x; }, getPJS:function(){ return PJS; } });

/* N1, session 19 (s38): ESP payroll's tests (harness-only; N1-design-esp-payroll.md, Section 8). Each restores ESP, ESS, PROJ, FW,
 * LABOR, LEDGER and the conversion model. Bit-identity of ESP = null to the harness before ESP existed (b1bc475) was checked in
 * session 19 by diffing full outputs (testbed projcore, proj and a5, ledger, price framework); test 1 checks that ESP null leaves no
 * ESP state, and test 2 that lam 0 reproduces ESP off exactly. */
function espUnitSuite(){
  var out = [];
  function t(name, fn){ var sv = {cm:CONVERSION_MODEL, pj:PROJ, es:ESP, cap:FW.octaveCapBase, nr:applyNR6()};
    try { var r = fn(); out.push({name:name, pass:!!r.pass, detail:r.detail || ''}); }
    catch (e){ out.push({name:name, pass:false, detail:'threw: ' + e.message}); }
    finally { CONVERSION_MODEL = sv.cm; PROJ = sv.pj; ESP = sv.es; ESS = null; FW.octaveCapBase = sv.cap; resetNR6(sv.nr); TB = null; LABOR = null; PRICE = null; LEDGER = null; } }
  var FI = FULL_INTEGRATION, PR = tbPresets(FI), CALM = {active:false, incomeMultiplier:1.0, yearsLeft:0};
  function es(o){ return Object.assign({}, ESP_DEFAULTS, o || {}); }
  function pj(o){ return Object.assign({}, PROJ_DEFAULTS, o || {}); }
  function same(r1, r2, ks){ return ks.every(function(k){ return r1[k] === r2[k]; }); }
  /* a plain framework run (no price module), with a callback after each year */
  function plain(P, seed, each){ CONVERSION_MODEL = 'framework'; RNG = mulberry32(seed + 700003); var ag = makeLatentPopulation(P.nAgents).map(function(l){ return instantiateAgent(l, P); });
    RNG = mulberry32(seed); for (var y = 0; y < P.years; y++){ runYear(ag, y, P, CALM); if (each) each(ag, y); } return ag; }
  var ESK = ['esPrem','esPremW','esBUW','esShare','esRate','esCapB','esConv','esRet'];
  t('off: with ESP null no ESP state is created and no agent carries a payroll field (Full Integration, seed 1, framework, project hiring on)', function(){
    ESP = null; ESS = null; PROJ = pj(); var ag = plain(FI, 1), n = 0;
    ag.forEach(function(a){ if (a._esWk !== undefined || a._esC !== undefined || a._esPrY !== undefined || a._esSv !== undefined) n++; });
    return {pass:ESS === null && n === 0, detail:'ESS ' + (ESS === null ? 'null' : 'set') + '; agents with an ESP field: ' + n};
  });
  t('lam 0 reproduces ESP off exactly on every testbed measure but the payroll ones (framework, project hiring on, labor on; Full Integration seeds 1-2 and Adverse seed 1)', function(){
    var ok = true, v = [], KS = TB_KEYS.filter(function(k){ return ESK.indexOf(k) < 0; });
    [[FI, 1], [FI, 2], [ADVERSE_REFERENCE, 1]].forEach(function(c){ var P = nextRoundPreset(c[0]), S = s3BaseS(P, c[1]), R = tbPresets(c[0]);
      CONVERSION_MODEL = 'framework'; PROJ = pj(); PATHWAY_OFF.octaveWage = true;
      try { ESP = null; var r0 = tbRun(R.cco(), c[1], {fin:'tax', grp:{part:c[0].partRate, pth:c[0].pthUptake}}, S).res;
        ESP = es({lam:0}); var r1 = tbRun(R.cco(), c[1], {fin:'tax', grp:{part:c[0].partRate, pth:c[0].pthUptake}}, S).res; }
      finally { PATHWAY_OFF.octaveWage = false; }
      if (!same(r0, r1, KS) || r1.esPrem !== 0) ok = false; v.push(Math.round(r0.bzPay) + '/' + Math.round(r1.bzPay)); });
    return {pass:ok, detail:KS.length + ' measures identical; business premium per adult-yr (off/lam 0): ' + v.join(', ')};
  });
  t('conservation, every year: BU accepted = the ESP\'s own share + next year\'s payroll pool; each pool = BU converted by workers + BU returned to the ESP + the change in saved BU (defaults; and cap \'save\' at a tiny capacity; Full Integration, seed 1)', function(){
    var ok = true, v = [];
    [[es(), 1000], [es({cap:'save'}), 1]].forEach(function(c){ ESP = c[0]; FW.octaveCapBase = c[1]; PROJ = pj(); plain(FI, 1); var Y = ESS.y, e = 0, tot = 0;
      for (var y = 0; y < Y.length; y++){ e = Math.max(e, Math.abs(Y[y].acc - Y[y].own - Y[y].poolNext)); tot += Y[y].acc;
        if (y > 0) e = Math.max(e, Math.abs(Y[y].pool - Y[y - 1].poolNext), Math.abs(Y[y].pool - Y[y].conv - Y[y].ret - (Y[y].sv - Y[y - 1].sv))); }
      if (e > 1e-6*tot/Y.length) ok = false; v.push(c[0].cap + ' (base ' + c[1] + '): largest gap $' + e.toExponential(1) + ', saved at the end $' + Math.round(Y[Y.length - 1].sv)); });
    return {pass:ok, detail:v.join('; ')};
  });
  t('wage cap: no ESP worker is allocated more BU than last year\'s wage; with every BU paid to a 5% workforce the cap binds and the excess returns to the ESP, conserved (Full Integration, seed 1)', function(){
    ESP = es(); plain(FI, 1); var m0 = ESS.acc.maxShare, r0 = ESS.acc.retWage;
    ESP = es({lam:1, work:0.05}); plain(FI, 1); var m1 = ESS.acc.maxShare, r1 = ESS.acc.retWage, A = ESS.acc, cons = Math.abs(A.poolPaid - A.conv - A.ret) < 1e-6*A.poolPaid;
    return {pass:m0 <= 1 + 1e-12 && m1 <= 1 + 1e-12 && Math.abs(m1 - 1) < 1e-12 && r1 > 0 && cons, detail:'largest BU / wage ' + m0.toFixed(3) + ' (defaults), ' + m1.toFixed(3) + ' (lam 1, work 0.05); returned above the wage $' + Math.round(r0) + ' / $' + Math.round(r1) + ' (year-0 $); conserved ' + cons};
  });
  t('capacity (cap \'dollars\'): no one converts payroll BU above 12 x base x 2^octave net of project BU, and at a tiny base the excess is paid in dollars; \'none\' never binds (Full Integration, seed 1, project hiring on)', function(){
    var over = 0, n = 0; ESP = es(); PROJ = pj(); FW.octaveCapBase = 1;
    plain(FI, 1, function(ag){ ag.forEach(function(a){ if (a._esC > 0){ n++; var k = 12*FW.octaveCapBase*Math.pow(2, a.octave); if (a._esC > a._esK + 1e-9 || a._esK > k + 1e-9) over++; } }); });
    var rc = ESS.acc.retCap, cb = ESS.acc.capBind; ESP = es({cap:'none'}); plain(FI, 1); var cbN = ESS.acc.capBind;
    return {pass:over === 0 && n > 0 && rc > 0 && cb > 0 && cbN === 0, detail:n + ' payroll conversions, ' + over + ' above capacity; paid in dollars over the cap $' + Math.round(rc) + ' (' + cb + ' worker-years); cap \'none\' binds ' + cbN};
  });
  t('non-participants never convert payroll BU; their share is paid in dollars and the ESP converts it (Full Integration, seed 1)', function(){
    var bad = 0, nonWk = 0; ESP = es();
    plain(FI, 1, function(ag){ ag.forEach(function(a){ if (!a.inCCO){ if (a._esC > 0 || a._esPrY !== 0) bad++; if (a._esWk) nonWk++; } }); });
    return {pass:bad === 0 && nonWk > 0 && ESS.acc.retNon > 0, detail:'non-participant ESP worker-years ' + nonWk + ', payroll conversions by non-participants ' + bad + ', returned to the ESP $' + Math.round(ESS.acc.retNon)};
  });
  t('random numbers: ESP adds no draw (8 per agent-year, Full Integration, 20 years); ESP workers are the same adults in every design and seed, 23.0% of 500', function(){
    var n = [], sets = [];
    [null, es()].forEach(function(q){ ESP = q; CONVERSION_MODEL = 'framework'; RNG = mulberry32(700004); var ag = makeLatentPopulation(FI.nAgents).map(function(l){ return instantiateAgent(l, FI); });
      var base = mulberry32(1), k = 0; RNG = function(){ k++; return base(); };
      for (var y = 0; y < FI.years; y++) runYear(ag, y, FI, CALM); n.push(k); });
    ESP = es(); [[FI, 1], [STRESS_TEST, 2], [BASELINE, 3]].forEach(function(c){ var ag = plain(Object.assign({}, c[0], {years:2}), c[1]); sets.push(ag.map(function(a){ return a._esWk ? 1 : 0; }).join('')); });
    var cnt = sets[0].split('1').length - 1;
    return {pass:n[0] === n[1] && n[0] === 8*FI.nAgents*FI.years && sets[1] === sets[0] && sets[2] === sets[0] && Math.abs(cnt - 0.23*FI.nAgents) <= 3,
      detail:'draws ' + n.join(' / ') + ' (off / on); ESP workers ' + cnt + ' of ' + FI.nAgents + ', identical in Full Integration seed 1, Stress Test seed 2 and Baseline seed 3: ' + (sets[1] === sets[0] && sets[2] === sets[0])};
  });
  t('the engine model is unaffected when ESP is set (engine, project hiring on, labor on; Full Integration seeds 1-2)', function(){
    var ok = true, P = nextRoundPreset(FI);
    for (var sd = 1; sd <= 2; sd++){ var S = s3BaseS(P, sd); CONVERSION_MODEL = 'engine'; PROJ = pj();
      ESP = null; var r0 = tbRun(PR.cco(), sd, {fin:'tax', grp:{part:FI.partRate, pth:FI.pthUptake}}, S).res;
      ESP = es(); var r1 = tbRun(PR.cco(), sd, {fin:'tax', grp:{part:FI.partRate, pth:FI.pthUptake}}, S).res;
      if (!same(r0, r1, TB_KEYS)) ok = false; }
    return {pass:ok, detail:TB_KEYS.length + ' measures identical'};
  });
  t('ledger rows add up, and each payroll premium = BU x (rate x (1 - tax) x CIP bonus x income shock - 1) (Full Integration, seed 1)', function(){
    ESP = es(); LEDGER = newLedger(); var cipB = FI.cip ? 1 + FI.cipDemo*0.12 : 1, worst = 0, n = 0;
    plain(FI, 1, function(ag){ ag.forEach(function(a){ if (a._esC > 0){ n++; var x = a._esC*(a._esR*(1 - pjTax(FI, a._esR))*cipB*a._esShk - 1); worst = Math.max(worst, Math.abs(x - a._esPrY)/Math.max(1, Math.abs(x))); } }); });
    var T = LEDGER.tot, Y = LEDGER.y, e1 = Math.abs(T.espGross - T.espTax - T.espConvBU - T.espPremium), e2 = Math.abs(T.espPoolPaid - T.espConvBU - T.espRetBU), acc = 0, own = 0, paid = 0;
    for (var y = 0; y < Y.length; y++){ if (y < Y.length - 1){ acc += Y[y].fwBUSpent || 0; own += Y[y].espOwnBU || 0; } if (y > 0) paid += Y[y].espPoolPaid || 0; }
    var e3 = Math.abs(acc - own - paid), sc = Math.max(1, T.espGross);
    return {pass:n > 0 && worst < 1e-12 && e1 < 1e-6*sc && e2 < 1e-6*sc && e3 < 1e-6*Math.max(1, acc),
      detail:n + ' payroll conversions, largest relative gap from the formula ' + worst.toExponential(1) + '; gross - tax - BU = premium: gap $' + e1.toExponential(1) + '; pools paid = converted + returned: $' + e2.toExponential(1) + '; accepted (yrs 0-18) = ESP share + pools paid: $' + e3.toExponential(1)};
  });
  t('labor: the payroll raise is positive exactly for the workers who take BU pay, and it lifts their earnings response (Full Integration, seed 1, labor at central values)', function(){
    var bad = 0, tk = 0, ratio = {};
    [null, es()].forEach(function(q){ ESP = q; LABOR = Object.assign({}, LABOR_DEFAULTS, {acc:null}); var s = 0, m = 0, who = {};
      ESP = es(); plain(Object.assign({}, FI, {years:6}), 1, function(ag, y){ if (y === 5) ag.forEach(function(a, i){ if (a._esC > 0) who[i] = 1; }); });
      ESP = q; var ag = plain(Object.assign({}, FI, {years:6}), 1, function(ag, y){ if (q) ag.forEach(function(a){ if ((a._esX > 0) !== (a._esC > 0)) bad++; if (a._esC > 0) tk++; }); });
      ag.forEach(function(a, i){ if (who[i] && a._lbE0 > 0){ s += a.yrWageUSD/a._lbE0; m++; } }); ratio[q ? 'on' : 'off'] = s/Math.max(1, m); });
    return {pass:bad === 0 && tk > 0 && ratio.on > ratio.off, detail:tk + ' taker-years, ' + bad + ' mismatches; year-5 takers\' earnings / earnings with no response: ' + ratio.off.toFixed(4) + ' (off) vs ' + ratio.on.toFixed(4) + ' (on)'};
  });
  t("rest 'esp' (d75 alternative): the ESP's own premium reaches its own workers only; 'biz' (d73 alternative): every taker's own rate beats the ESP's rate (Full Integration, seed 1)", function(){
    var leak = 0, got = 0, low = 0, tk = 0;
    ESP = es({rest:'esp'}); plain(FI, 1, function(ag, y){ if (y > 0) ag.forEach(function(a){ if (!a._esWk && a._fwPayY !== 0) leak++; if (a._esWk && a._fwPayY > 0) got++; }); });
    ESP = es({take:'biz'}); plain(FI, 1, function(ag){ ag.forEach(function(a){ if (a._esC > 0){ tk++; if (!(a._esR > FW.bizRate)) low++; } }); });
    return {pass:leak === 0 && got > 0 && low === 0 && tk > 0, detail:'non-workers paid: ' + leak + ', workers paid ' + got + ' worker-years; takers under \'biz\' ' + tk + ', at or below ' + FW.bizRate + 'x: ' + low};
  });
  return out;
}
Object.assign(module.exports, { espUnitSuite, ESP_DEFAULTS, setEsp:function(x){ ESP = x; }, getESS:function(){ return ESS; } });

/* ─── CLI modes ──────────────────────────────────────────────────────── */
if (require.main === module) {
  /* v4.21: `--agents=N` sets the population of every run in every mode (default 500, the page's
   * reference population). Seeds and agents are separate axes: the project's earlier "N=5,000"
   * studies were 5,000 seeds of 500 agents; `--agents` scales the population inside each run. */
  var AGENTS_ARG = process.argv.filter(function(a){ return /^--agents=\d+$/.test(a); })[0];
  process.argv = process.argv.filter(function(a){ return !/^--agents=/.test(a); });
  if (AGENTS_ARG){ var nAgArg = parseInt(AGENTS_ARG.split('=')[1], 10); [FULL_INTEGRATION, BASELINE, STRESS_TEST, ADVERSE_REFERENCE, HIGH_AUTOMATION, CCO_ONLY].forEach(function(q){ q.nAgents = nAgArg; }); }
  var AG = FULL_INTEGRATION.nAgents;
  var mode = process.argv[2] || 'validate';

  if (mode === 'validate') {
    /* v4.20: asserts, and exits 1 on any mismatch, so a CI job (see .github/workflows) fails on
     * a regression instead of printing it for someone to read. Checks the shipped engine against
     * the v4.20 figures, then the legacy automation sampler at the old 0.47 share against v4.19's,
     * which proves the before/after switch reproduces the previous release exactly. */
    CFG.WEALTH_FLOOR = -10000; // shipped default
    if (AG !== 500){ console.log('validate runs the documented 500-agent populations; --agents is ignored here'); [FULL_INTEGRATION, BASELINE, STRESS_TEST, ADVERSE_REFERENCE, HIGH_AUTOMATION, CCO_ONLY].forEach(function(q){ q.nAgents = 500; }); }
    var r = runScenario(FULL_INTEGRATION, 42);
    console.log('=== Validation: seed 42, Full Integration, 20yr, WEALTH_FLOOR=-10000 (shipped default) ===');
    console.log(JSON.stringify(r, null, 2));
    var KEYS = [['bleiMed','Median BLEI (d)'],['bleiPovPct','BLEI poverty (%)'],['wealth','Median wealth ($)'],['pov','Wealth poverty (%)'],
      ['gini','Gini, EDC-adj.'],['stab','System Stability (%)'],['avgEDC','Avg EDC (%)'],['fracAtFloor','Pinned at the floor (share)']];
    var DOC = {
      'v4.21 (shipped)': {bleiMed:1975, bleiPovPct:13.2, wealth:570661, pov:15.8, gini:0.518, stab:88.8, avgEDC:24.2, fracAtFloor:0.088},
      'v4.19 (legacy automation sampler, share 0.47)': {bleiMed:1965, bleiPovPct:13.6, wealth:559223, pov:16.6, gini:0.534, stab:88.5, avgEDC:24.9, fracAtFloor:0.106}
    };
    function check(label, got){
      var want = DOC[label], bad = [];
      console.log('\n' + label + ' (CONTRIBUTING.md regression table):');
      KEYS.forEach(function(k){ var ok = got[k[0]] === want[k[0]]; if (!ok) bad.push(label.split(' ')[0] + ' ' + k[1]);
        console.log('  ' + (ok ? 'ok  ' : 'FAIL') + '  ' + k[1] + ': ' + got[k[0]] + (ok ? '' : '  (documented ' + want[k[0]] + ')')); });
      return bad;
    }
    var fails = check('v4.21 (shipped)', r);
    var savedShare = CFG.AUTO_HIGH_SHARE; AUTOMATION_SAMPLER_LEGACY = true; CFG.AUTO_HIGH_SHARE = 0.47;
    var rl = runScenario(FULL_INTEGRATION, 42);
    AUTOMATION_SAMPLER_LEGACY = false; CFG.AUTO_HIGH_SHARE = savedShare;
    fails = fails.concat(check('v4.19 (legacy automation sampler, share 0.47)', rl));
    /* v4.21: stored seed-42 fixtures for every preset (the v4.12 test-hierarchy item's "regression
     * fixtures beyond the single seed-42 table"), and a check that RELIEF_PRICE_LEGACY reproduces
     * v4.20's two inflation presets, the only ones the v4.21 relief fix moves. */
    var PRESET_KEYS = [['pov','wealth poverty %'],['wealth','median wealth $'],['bleiMed','median BLEI d'],['gini','Gini'],['bleiPovPct','BLEI poverty %']];
    var PRESET_DOC = [
      ['Full Integration', FULL_INTEGRATION, {pov:15.8, wealth:570661, bleiMed:1975, gini:0.518, bleiPovPct:13.2}],
      ['CCO Only', CCO_ONLY, {pov:24.8, wealth:427239, bleiMed:1283, gini:0.575, bleiPovPct:21}],
      ['Traditional Welfare Baseline (3%)', BASELINE, {pov:68.8, wealth:-10000, bleiMed:8, gini:0.824, bleiPovPct:67.6}],
      ['High Automation (25yr)', HIGH_AUTOMATION, {pov:27.8, wealth:382123, bleiMed:1351, gini:0.603, bleiPovPct:25.8}],
      ['Adverse Environment', ADVERSE_REFERENCE, {pov:36.8, wealth:205005, bleiMed:723, gini:0.658, bleiPovPct:32.4}],
      ['Stress Test', STRESS_TEST, {pov:59.8, wealth:-10000, bleiMed:16, gini:0.785, bleiPovPct:57.2}],
      ['Adverse Environment, RELIEF_PRICE_LEGACY (= v4.20)', ADVERSE_REFERENCE, {pov:35, wealth:218851, bleiMed:819, gini:0.646, bleiPovPct:31.2}, true],
      ['Stress Test, RELIEF_PRICE_LEGACY (= v4.20)', STRESS_TEST, {pov:59, wealth:-10000, bleiMed:16, gini:0.781, bleiPovPct:56.6}, true]];
    console.log('\nSeed-42 preset fixtures (v4.21):');
    PRESET_DOC.forEach(function(d){
      RELIEF_PRICE_LEGACY = !!d[3]; var g = runScenario(d[1], 42); RELIEF_PRICE_LEGACY = false;
      var bad = PRESET_KEYS.filter(function(k){ return g[k[0]] !== d[2][k[0]]; });
      if (bad.length) fails.push(d[0] + ': ' + bad.map(function(k){ return k[1] + ' ' + g[k[0]] + ' (documented ' + d[2][k[0]] + ')'; }).join('; '));
      console.log('  ' + (bad.length ? 'FAIL' : 'ok  ') + '  ' + d[0] + ': ' + PRESET_KEYS.map(function(k){ return g[k[0]]; }).join(' / '));
    });
    console.log(fails.length ? '\nVALIDATION FAILED: ' + fails.join(', ') : '\nVALIDATION PASSED: the documented regressions and all preset fixtures reproduce exactly.');
    if (fails.length) process.exitCode = 1;
  }

  if (mode === 'unit') {
    /* v4.20: the pure-function suite against this file. domtest.js Phase 8 runs the same suite
     * against index.html, including the five page-only functions skipped here. */
    var U = unitSuite(unitTargets()), nf = 0;
    console.log('=== unitSuite() against harness.js ===');
    U.forEach(function(x){ if (!x.pass) nf++; console.log('  ' + (x.skipped ? 'SKIP' : x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + U.filter(function(x){ return !x.skipped; }).length + ' run, ' + U.filter(function(x){ return x.skipped; }).length + ' skipped (page-only), ' + nf + ' failed');
    /* Session 2: the price module's tests (harness-only; the page has none of these functions). */
    var PU = priceUnitSuite(), pf = 0;
    console.log('\n=== priceUnitSuite(): A2 price rule and the framework conversion model (harness-only) ===');
    PU.forEach(function(x){ if (!x.pass) pf++; console.log('  ' + (x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + PU.length + ' run, ' + pf + ' failed');
    /* Session 4: the labor module's tests (harness-only). */
    var LU = laborUnitSuite(), lf = 0;
    console.log('\n=== laborUnitSuite(): A3 labor supply and the UBI comparator (harness-only) ===');
    LU.forEach(function(x){ if (!x.pass) lf++; console.log('  ' + (x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + LU.length + ' run, ' + lf + ' failed');
    /* Session 5: the restudy switches (THETA_GATE, PTH_MODE, DISC_BASE), the joint run and the price-neutral search (harness-only). */
    var RU = s5UnitSuite(), rf = 0;
    console.log('\n=== s5UnitSuite(): session 5 restudy switches, joint price and labor run, price-neutral search (harness-only) ===');
    RU.forEach(function(x){ if (!x.pass) rf++; console.log('  ' + (x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + RU.length + ' run, ' + rf + ' failed');
    /* Session 6: the testbed (harness-only). */
    var TU = tbUnitSuite(), tf = 0;
    console.log('\n=== tbUnitSuite(): A4 testbed presets, uniform accounting and the financing switch (harness-only) ===');
    TU.forEach(function(x){ if (!x.pass) tf++; console.log('  ' + (x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + TU.length + ' run, ' + tf + ' failed');
    /* Session 15 (N1): project hiring (harness-only). */
    var JU = projUnitSuite(), jf = 0;
    console.log('\n=== projUnitSuite(): N1 project hiring paid in expired BU (harness-only) ===');
    JU.forEach(function(x){ if (!x.pass) jf++; console.log('  ' + (x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + JU.length + ' run, ' + jf + ' failed');
    /* Session 19 (N1, s38): ESP payroll (harness-only). */
    var EU = espUnitSuite(), ef = 0;
    console.log('\n=== espUnitSuite(): N1 ESP payroll in expired BU at workers\' own rates (harness-only) ===');
    EU.forEach(function(x){ if (!x.pass) ef++; console.log('  ' + (x.pass ? 'PASS' : 'FAIL') + '  ' + x.name + (x.detail ? '\n         ' + x.detail : '')); });
    console.log('\n' + EU.length + ' run, ' + ef + ' failed');
    if (nf || pf || lf || rf || tf || jf || ef) process.exitCode = 1;
  }

  if (mode === 'automation') {
    /* v4.20: the calibration behind CFG.AUTO_*. Sections: fit | sweep (default: both).
     * Data: plotly/datasets job-automation-probability.csv — Frey & Osborne (2013)'s 702
     * occupations with May-2016 BLS OES employment (numbEmployed column); every row checked
     * against the paper's appendix (pp. 57-72) in v4.20 and matching on SOC code, rank and
     * probability. The distribution below is that file's employment-weighted histogram of
     * probabilities in tenths, so this mode needs no network access. */
    CFG.WEALTH_FLOOR = -10000;
    var nA = parseInt(process.argv[3] || '500', 10), secA = process.argv[4] || 'all';
    var EMP_HIST = [0.200, 0.059, 0.034, 0.033, 0.014, 0.050, 0.106, 0.066, 0.110, 0.328];
    var DATA = {mean:0.592, gt07:0.501, lt03:0.293, ge05:0.660};
    function mixCDF(x, pi, a, b){ return pi*Math.pow(x, a) + (1-pi)*(1 - Math.pow(1-x, b)); }
    var VARIANTS = [
      {l:'v4.19: share 0.47, rejection-sampled Beta(6,1)/Beta(1,6)', legacy:true, pi:0.47, a:6, b:6},
      {l:'share 0.47, inverse-CDF (isolates the sampler change)', pi:0.47, a:6, b:6},
      {l:'share 0.50 (F&O >0.7 band at 2016 employment)', pi:0.50, a:6, b:6},
      {l:'v4.20: share 0.63 (mean-matched)', pi:0.63, a:6, b:6},
      {l:'share 0.66 (employment-weighted MLE, shapes fixed)', pi:0.66, a:6, b:6},
      {l:'free-shape MLE: 0.706 Beta(4.02,1) / Beta(1,11.03)', pi:0.706, a:4.017, b:11.028}];
    if (secA === 'fit' || secA === 'all'){
      console.log('=== automationRisk mixture vs Frey & Osborne, employment-weighted (data: mean ' + DATA.mean + ', >0.7 ' + DATA.gt07 + ', <0.3 ' + DATA.lt03 + ', >=0.5 ' + DATA.ge05 + ') ===');
      console.log('variant | mean | >0.7 | <0.3 | >=0.5 | max gap to the data CDF at tenths');
      VARIANTS.forEach(function(v){
        var cum = 0, gap = 0;
        for (var i = 0; i < 10; i++){ cum += EMP_HIST[i]; gap = Math.max(gap, Math.abs(mixCDF((i+1)/10, v.pi, v.a, v.b) - cum)); }
        var m = v.pi*v.a/(v.a+1) + (1-v.pi)/(v.b+1);
        console.log(v.l + ' | ' + m.toFixed(3) + ' | ' + (1-mixCDF(0.7, v.pi, v.a, v.b)).toFixed(3) + ' | ' + mixCDF(0.3, v.pi, v.a, v.b).toFixed(3) + ' | ' + (1-mixCDF(0.5, v.pi, v.a, v.b)).toFixed(3) + ' | ' + gap.toFixed(3));
      });
    }
    if (secA === 'sweep' || secA === 'all'){
      var saveA = [CFG.AUTO_HIGH_SHARE, CFG.AUTO_HIGH_A, CFG.AUTO_LOW_B];
      console.log('=== Outcomes by variant: seeds 1-' + nA + ', ' + AG + ' agents (mean across runs, final year) ===');
      console.log('variant | scenario | wealth poverty % | BLEI poverty % | median wealth | median BLEI (d) | seed 42 wealth poverty % / median wealth');
      [['High Automation (25yr)', HIGH_AUTOMATION], ['Adverse Environment', ADVERSE_REFERENCE], ['Stress Test', STRESS_TEST], ['Full Integration (automation off)', FULL_INTEGRATION]].forEach(function(sc){
        VARIANTS.forEach(function(v){
          AUTOMATION_SAMPLER_LEGACY = !!v.legacy; CFG.AUTO_HIGH_SHARE = v.pi; CFG.AUTO_HIGH_A = v.a; CFG.AUTO_LOW_B = v.b;
          var rs = runMany(sc[1], nA), s42 = runScenario(sc[1], 42);
          console.log(v.l + ' | ' + sc[0] + ' | ' + mean(col(rs,'pov')).toFixed(2) + ' | ' + mean(col(rs,'bleiPovPct')).toFixed(2) + ' | $' + Math.round(mean(col(rs,'wealth'))).toLocaleString() +
            ' | ' + Math.round(mean(col(rs,'bleiMed'))) + ' | ' + s42.pov + '% / $' + s42.wealth.toLocaleString());
        });
      });
      AUTOMATION_SAMPLER_LEGACY = false; CFG.AUTO_HIGH_SHARE = saveA[0]; CFG.AUTO_HIGH_A = saveA[1]; CFG.AUTO_LOW_B = saveA[2];
    }
  }

  if (mode === 'sweep') {
    var nSeeds = parseInt(process.argv[3] || '500', 10);
    var baseSeed = 1;
    var floors = [0, -10000, -25000, -50000];
    var configs = { FullIntegration: FULL_INTEGRATION, Baseline: BASELINE };
    var t0 = Date.now();
    var out = {};
    floors.forEach(function(floor){
      CFG.WEALTH_FLOOR = floor;
      out[floor] = {};
      Object.keys(configs).forEach(function(cname){
        var p = configs[cname];
        var runs = [];
        for (var s = 0; s < nSeeds; s++){ runs.push(runScenario(p, baseSeed + s)); }
        out[floor][cname] = runs;
      });
    });
    var t1 = Date.now();
    console.error('sweep runtime: ' + ((t1-t0)/1000).toFixed(1) + 's for N=' + nSeeds + ' seeds x ' + floors.length + ' floors x 2 configs');

    function summarize(runs, key){
      var vals = runs.map(function(r){ return r[key]; });
      var n = vals.length;
      var mean = vals.reduce(function(s,x){return s+x;},0)/n;
      var sd = Math.sqrt(vals.reduce(function(s,x){return s+(x-mean)*(x-mean);},0)/Math.max(1,n-1));
      var sorted = vals.slice().sort(function(a,b){return a-b;});
      var median = n%2===0 ? (sorted[n/2-1]+sorted[n/2])/2 : sorted[Math.floor(n/2)];
      return {mean:mean, sd:sd, ci95:1.96*sd/Math.sqrt(n), median:median};
    }

    var KEYS = ['wealth','p10','p90','gini','pov','bleiMed','bleiPovPct','pctFlourishing','avgEDC','stab'];
    console.log('=== WEALTH_FLOOR sweep: N=' + nSeeds + ' seeds (1-' + nSeeds + '), 500 agents, 20yr, shock off ===');
    var summary = {};
    floors.forEach(function(floor){
      summary[floor] = {};
      Object.keys(configs).forEach(function(cname){
        var runs = out[floor][cname];
        console.log('--- floor=' + floor + ' / ' + cname + ' ---');
        var s = {};
        KEYS.forEach(function(k){
          s[k] = summarize(runs, k);
          console.log('  ' + k + ': mean=' + s[k].mean.toFixed(3) + ' median=' + s[k].median.toFixed(3) + ' sd=' + s[k].sd.toFixed(3) + ' ci95=\u00b1' + s[k].ci95.toFixed(3));
        });
        var fracAtFloorMean = runs.reduce(function(a,r){return a+r.fracAtFloor;},0)/runs.length;
        var pctMedianPinned = runs.filter(function(r){return r.medianPinned;}).length/runs.length*100;
        console.log('  fracAtFloor (mean across seeds, % of AGENTS pinned): ' + (fracAtFloorMean*100).toFixed(1) + '%');
        console.log('  seeds where the MEDIAN is pinned exactly at floor:  ' + pctMedianPinned.toFixed(1) + '%');
        s.fracAtFloorMean = fracAtFloorMean;
        s.pctMedianPinned = pctMedianPinned;
        summary[floor][cname] = s;
      });
    });
    console.log('\n=== RAW JSON (machine-readable) ===');
    console.log(JSON.stringify(summary));
  }

  if (mode === 'blei-components') {
    CFG.WEALTH_FLOOR = -10000;
    var rows = runScenarioWithComponents(FULL_INTEGRATION, 42);
    console.log('=== calcBLEIComponents() per year, seed 42, Full Integration, 20yr ===');
    console.log('yr\tcashDays\tincomeDays\tbenefitDays\tCCO participation frac');
    rows.forEach(function(r){ console.log(r.yr+'\t'+r.cash+'\t\t'+r.inc+'\t\t'+r.ben+'\t\t'+r.partFrac); });
  }

  /* v4.16: the two studies behind CONTRIBUTING.md's v4.16 Release Notes, so their tables can be
   * regenerated rather than taken on trust. Both hold shocks and automation off (the harness's
   * documented scope) and aggregate seeds 1..N at --agents (default 500) agents / 20 years. */
  function aggregate(p, N){
    var keys = ['pov','gini','wealth','bleiMed','bleiPovPct','fracAtFloor','incPov','incPovExt','basketPov','basketPovGross','stab','recessionYears'], s = {}, pinned = 0, medW = [];  // v4.17: +incPov, basketPov, stab, recessionYears
    keys.forEach(function(k){ s[k] = 0; });
    for (var seed = 1; seed <= N; seed++){
      var r = runScenario(p, seed);
      keys.forEach(function(k){ s[k] += r[k]; });
      if (r.medianPinned) pinned++;
      medW.push(r.wealth);
    }
    keys.forEach(function(k){ s[k] = +(s[k]/N).toFixed(3); });
    medW.sort(function(a,b){ return a-b; });
    s.medianOfMedianWealth = medW[Math.floor(N/2)];
    s.runsMedianPinned = +(pinned/N).toFixed(3);
    return s;
  }
  if (mode === 'infl-match') {
    CFG.WEALTH_FLOOR = -10000;
    var nI = parseInt(process.argv[3] || '500', 10);
    console.log('=== Baseline inflation asymmetry (v4.16): seeds 1-' + nI + ', ' + AG + ' agents, 20yr, shocks off ===');
    [['Baseline @ 3% (shipped default)', BASELINE],
     ['Baseline @ 0% (matched to Full Integration)', Object.assign({}, BASELINE, {inflRate:0})],
     ['Full Integration @ 0% (shipped default)', FULL_INTEGRATION],
     ['Full Integration @ 3% (matched to Baseline)', Object.assign({}, FULL_INTEGRATION, {inflRate:0.03})]
    ].forEach(function(c){ console.log(c[0] + '\n  ' + JSON.stringify(aggregate(c[1], nI))); });
    console.log('seed 42, Baseline @ 0%: ' + JSON.stringify(runScenario(Object.assign({}, BASELINE, {inflRate:0}), 42)));
  }
  if (mode === 'pth-accounting') {
    CFG.WEALTH_FLOOR = -10000;
    var nP = parseInt(process.argv[3] || '500', 10);
    var P50 = Object.assign({}, FULL_INTEGRATION, {pthUptake:0.5});
    console.log('=== PTH appreciation accounting (v4.16): current (full appr -> acreEquity) vs value-conserving ===');
    [false, true].forEach(function(cons){
      PTH_APPR_CONSERVE = cons;
      var lbl = cons ? 'conserving' : 'current   ';
      console.log(lbl + ' seed 42:  ' + JSON.stringify(runScenario(FULL_INTEGRATION, 42)));
      console.log(lbl + ' N=' + nP + ' FI: ' + JSON.stringify(aggregate(FULL_INTEGRATION, nP)));
      console.log(lbl + ' N=' + nP + ' FI, PTH 50%: ' + JSON.stringify(aggregate(P50, nP)));
    });
    PTH_APPR_CONSERVE = false;
  }

  /* ─── v4.17 modes: the studies behind CONTRIBUTING.md's v4.17 Release Notes ─── */
  function mean(arr){ return arr.reduce(function(a,b){ return a+b; }, 0)/arr.length; }
  function runMany(p, N){ var r = []; for (var sd = 1; sd <= N; sd++) r.push(runScenario(p, sd)); return r; }
  function col(runs, k){ return runs.map(function(r){ return r[k]; }); }
  function col0(runs, k){ return runs.map(function(r){ return r.yearZero[k]; }); }
  function f1(x){ return (x === null || x === undefined || isNaN(x)) ? '-' : x.toFixed(1); }

  if (mode === 'headline') {
    /* NEEC note 1: what poverty REDUCTION does the engine produce, against which comparator?
     * Reports ratio-of-means and mean-of-per-run reductions, since the two differ slightly. */
    CFG.WEALTH_FLOOR = -10000;
    var nH = parseInt(process.argv[3] || '500', 10);
    var FI = runMany(FULL_INTEGRATION, nH), FI3 = runMany(Object.assign({}, FULL_INTEGRATION, {inflRate:0.03}), nH);
    var B3 = runMany(BASELINE, nH), B0 = runMany(Object.assign({}, BASELINE, {inflRate:0}), nH);
    console.log('=== Poverty reduction by comparator (v4.17): seeds 1-' + nH + ', ' + AG + ' agents, 20yr, shocks off ===');
    console.log('comparator\tmeasure\tcomparator %\tFull Integration %\treduction (ratio of means)\treduction (mean of per-run)');
    [['pov','wealth poverty'],['bleiPovPct','BLEI poverty'],['incPov','relative income poverty (cash)'],['incPovExt','relative income poverty (incl. in-kind)'],['basketPov','basket poverty (net)'],['basketPovGross','basket poverty (gross)']].forEach(function(m){
      [['Baseline @3% (shipped)', B3, FI, false],['Baseline @0% (inflation-matched)', B0, FI, false],['Baseline @3% vs FI @3%', B3, FI3, false],['Year 0 (policy-neutral)', FI, FI, true]].forEach(function(c){
        var k0 = m[0] === 'pov' ? 'pov' : m[0] === 'bleiPovPct' ? 'bleiPovNeutral' : m[0];
        var cmp = c[3] ? col0(c[1], k0) : col(c[1], m[0]), fi = col(c[2], m[0]);
        var rm = (1 - mean(fi)/mean(cmp))*100;
        var pr = mean(cmp.map(function(v, i){ return v > 0 ? (1 - fi[i]/v)*100 : 0; }));
        console.log(c[0] + '\t' + m[1] + '\t' + f1(mean(cmp)) + '\t' + f1(mean(fi)) + '\t' + f1(rm) + '%\t' + f1(pr) + '%');
      });
    });
    console.log('FI median wealth (mean of run medians): $' + Math.round(mean(col(FI, 'wealth'))) + '; TARGET_WEALTH $' + CFG.TARGET_WEALTH + ', TARGET_POVERTY ' + (CFG.TARGET_POVERTY*100) + '%');
  }

  if (mode === 'year0') {
    /* NEEC notes 3 and 4: the Baseline's deterioration and Full Integration's early rise. */
    CFG.WEALTH_FLOOR = -10000;
    var nY = parseInt(process.argv[3] || '500', 10), marks = [1,2,3,5,10,15,20];
    [['Baseline @3% (shipped)', BASELINE], ['Baseline @0%', Object.assign({}, BASELINE, {inflRate:0})], ['Full Integration', FULL_INTEGRATION]].forEach(function(c){
      var acc = {};
      for (var sd = 1; sd <= nY; sd++){
        var t = trajectory(c[1], sd, marks);
        Object.keys(t).forEach(function(y){ acc[y] = acc[y] || {}; Object.keys(t[y]).forEach(function(k){ if (t[y][k] !== null){ acc[y][k] = (acc[y][k] || 0) + t[y][k]/nY; } }); });
      }
      console.log('=== ' + c[0] + ': seeds 1-' + nY + ' (means). yr / wealthPov / BLEIpov (scenario rules) / BLEIpov CCO participants / BLEIpov non-participants / basketPov (net) / incomePov ===');
      Object.keys(acc).sort(function(a,b){ return a-b; }).forEach(function(y){ var r = acc[y]; console.log('  ' + y + '\t' + f1(r.pov) + '\t' + f1(r.bleiPov) + '\t' + f1(r.bleiPovPart) + '\t' + f1(r.bleiPovNonPart) + '\t' + f1(r.basketPov) + '\t' + f1(r.incPov)); });
    });
    var y0 = runScenario(FULL_INTEGRATION, 42).yearZero;
    console.log('seed 42 year 0: ' + JSON.stringify(y0));
    console.log('median year-0 wage income $' + Math.round(Math.exp(3.5)*12*CFG.WAGE_TO_USD) + ' vs LIVING_WAGE_ANNUAL $' + CFG.LIVING_WAGE_ANNUAL);
  }

  if (mode === 'stress') {
    /* NEEC notes 5 and 6: recessions in the harness; environment vs settings stress. */
    CFG.WEALTH_FLOOR = -10000;
    var nS = parseInt(process.argv[3] || '500', 10);
    console.log('=== Stress decomposition (v4.17): seeds 1-' + nS + ', ' + AG + ' agents, 20yr ===');
    [['Full Integration (reference environment)', FULL_INTEGRATION],
     ['Adverse Environment @ reference settings', ADVERSE_REFERENCE],
     ['Weaker settings @ reference environment', Object.assign({}, STRESS_TEST, {shock:false, automation:false, inflRate:0})],
     ['Stress Test (adverse environment + weaker settings)', STRESS_TEST],
     ['Baseline as compared with the adverse presets (shocks+AI, 3%)', baselineFor(ADVERSE_REFERENCE, false)]
    ].forEach(function(c){ var a = aggregate(c[1], nS); console.log(c[0] + '\n  ' + JSON.stringify(a)); });
    console.log('seed 42, Adverse Environment: ' + JSON.stringify(runScenario(ADVERSE_REFERENCE, 42)));
    console.log('seed 42, Stress Test:         ' + JSON.stringify(runScenario(STRESS_TEST, 42)));
  }

  if (mode === 'participation') {
    /* NEEC note 7: no dynamic in runYear() reads aggregate CCO participation, so nothing
     * happens at the papers' 55% "minimum viable" level. This sweep shows it directly. */
    CFG.WEALTH_FLOOR = -10000;
    var nPp = parseInt(process.argv[3] || '200', 10);
    console.log('=== CCO participation sweep, Full Integration otherwise: seeds 1-' + nPp + ' ===\npartRate\twealthPov\tBLEIpov');
    [0.45,0.50,0.54,0.55,0.56,0.60,0.65].forEach(function(pr){ var r = runMany(Object.assign({}, FULL_INTEGRATION, {partRate:pr}), nPp); console.log(pr.toFixed(2) + '\t\t' + f1(mean(col(r,'pov'))) + '\t\t' + f1(mean(col(r,'bleiPovPct')))); });
  }

  if (mode === 'extreme') {
    /* v4.18: extreme poverty (homeless; necessities via charity, if at all). Expected share,
     * an overlay on engine state — see extremePovertyOf(). Prints the release-notes tables and
     * how the constants move the result (the overlay is analytic, so this re-weights the same
     * runs rather than re-simulating). */
    CFG.WEALTH_FLOOR = -10000;
    var nE = parseInt(process.argv[3] || '500', 10);
    function f2(x){ return (x === null || x === undefined || isNaN(x)) ? '-' : (x*100).toFixed(1); }  /* percent -> per 10,000 */
    var SC = [['Baseline @3% (shipped)', BASELINE], ['Baseline @0% (inflation-matched)', Object.assign({}, BASELINE, {inflRate:0})],
      ['CCO Only', CCO_ONLY], ['Full Integration', FULL_INTEGRATION], ['Adverse Environment', ADVERSE_REFERENCE],
      ['Baseline under the adverse environment (3%)', baselineFor(ADVERSE_REFERENCE, false)], ['Stress Test', STRESS_TEST], ['CCO Only under the adverse environment', ccoOnlyFor(ADVERSE_REFERENCE)]];
    var RUNS = {};
    console.log('=== Extreme poverty overlay (v4.18): seeds 1-' + nE + ', ' + AG + ' agents, 20yr. Per 10,000 people (housing distress in %) ===');
    console.log('scenario\ttotal\teconomic\tSMI\tvoluntary\thousing distress\tdistress, CCO participants\tdistress, non-participants');
    SC.forEach(function(c){
      var r = runMany(c[1], nE); RUNS[c[0]] = r;
      console.log(c[0] + '\t' + f2(mean(col(r,'epTotal'))) + '\t' + f2(mean(col(r,'epEcon'))) + '\t' + f2(mean(col(r,'epSmi'))) + '\t' + f2(mean(col(r,'epVol'))) + '\t' + f1(mean(col(r,'distress'))) + '\t' + f1(mean(col(r,'distressPart').filter(function(v){return v!==null;}))) + '\t' + f1(mean(col(r,'distressNonPart').filter(function(v){return v!==null;}))));
    });
    var fi = RUNS['Full Integration'];
    console.log('year 0 (every scenario): total ' + f2(CFG.EP_Y0_RATE*100) + ' by construction, housing distress ' + f1(mean(col(fi,'distressY0'))));
    function red(a, b){ return f1((1 - a/b)*100) + '%'; }
    var FIt = mean(col(fi,'epTotal')), CCt = mean(col(RUNS['CCO Only'],'epTotal')), B3 = mean(col(RUNS['Baseline @3% (shipped)'],'epTotal')), B0 = mean(col(RUNS['Baseline @0% (inflation-matched)'],'epTotal')), Y0 = CFG.EP_Y0_RATE*100;
    console.log('reductions (ratio of means): FI vs year 0 ' + red(FIt, Y0) + ', vs Baseline@3% ' + red(FIt, B3) + ', vs Baseline@0% ' + red(FIt, B0) + ' | CCO Only vs year 0 ' + red(CCt, Y0) + ', vs Baseline@3% ' + red(CCt, B3) + ', vs Baseline@0% ' + red(CCt, B0));
    var s42 = runScenario(FULL_INTEGRATION, 42);
    console.log('seed 42, Full Integration, per 10,000: total ' + (s42.epTotal*100).toFixed(2) + ' econ ' + (s42.epEcon*100).toFixed(2) + ' smi ' + (s42.epSmi*100).toFixed(2) + ' vol ' + (s42.epVol*100).toFixed(2) + ' | housing distress %: ' + s42.distress.toFixed(1) + ' (year 0 ' + s42.distressY0.toFixed(1) + ') wz ' + s42.wz.toFixed(3));
    /* Sensitivity: each constant varied alone; same runs, re-weighted. */
    function recompute(runs, p, k){ return mean(runs.map(function(r){ var saved = {s:CFG.EP_SMI_SHARE, v:CFG.EP_VOL_SHARE, w:CFG.EP_WZ_EFFECT}; Object.assign(CFG, k); var e = extremePovertyOf(r.distress/100, r.distressY0/100, p).total; CFG.EP_SMI_SHARE = saved.s; CFG.EP_VOL_SHARE = saved.v; CFG.EP_WZ_EFFECT = saved.w; return e; })); }
    console.log('--- sensitivity (Full Integration and CCO Only final; year 0 is EP_Y0_RATE by construction) ---');
    console.log('constant\tvalue\tFI total\tFI vs year 0\tCCO Only total\tCCO Only vs year 0');
    [['EP_SMI_SHARE',[0.15,0.25,0.35]],['EP_VOL_SHARE',[0,0.02,0.05]],['EP_WZ_EFFECT',[0.30,0.50,0.65]]].forEach(function(k){
      k[1].forEach(function(v){ var o = {}; o[k[0]] = v; var a = recompute(fi, FULL_INTEGRATION, o), b = recompute(RUNS['CCO Only'], CCO_ONLY, o);
        console.log(k[0] + '\t' + v + '\t' + f2(a) + '\t' + red(a, Y0) + '\t' + f2(b) + '\t' + red(b, Y0)); });
    });
  }

  if (mode === 'stabilizer') {
    /* v4.19: the studies behind CONTRIBUTING.md's v4.19 Release Notes. Excess = recession years
     * minus the same seed with recessions off (CRN-paired). Sections: rules | neutral | decision
     * | cola | all (default). */
    CFG.WEALTH_FLOOR = -10000;
    var nS = parseInt(process.argv[3] || '300', 10), sec = process.argv[4] || 'all';
    var REC = Object.assign({}, FULL_INTEGRATION, {shock:true});
    function f2(x){ return (x < 0 ? '-' : '') + Math.abs(x).toFixed(2); }
    function line(lbl, a){ console.log([lbl, f2(a.partPP), f2(a.nonPartPP), f2(a.allPP), a.extremePer10k.toFixed(2), a.extraPctOfBase.toFixed(1) + '%'].join(' | ')); }
    var HDR = 'rule | participants: excess distress (pp) | non-participants (pp) | all (pp) | excess extreme poverty (per 10,000) | extra BU (% of base)';
    function arm(P, st){ return Object.assign({}, P, {stab:true, stabSev:false, stabMult:1, stabK:0, stabThresh:0, stabSusp:false, emerg:false, emergTakeup:0}, st); }
    function table(P, rules, N){
      var calm = [], acc = rules.map(function(){ return newShockAcc(); });
      for (var s = 1; s <= N; s++){
        var c = shockRun(Object.assign({}, P, {shock:false}), s), ref3 = null; calm[s] = c;
        rules.forEach(function(r, i){
          var o;
          if (r.p) o = shockRun(r.p, s);
          else if (r.budgetOf){ var b = ref3; o = shockRunWith(P, s, function(){ return 1 + b.extra/b.base; }); }
          else o = shockRunWith(P, s, r.mult);
          if (r.keep) ref3 = o;
          addShockAcc(acc[i], c, o);
        });
      }
      return acc.map(shockSummary);
    }
    if (sec === 'rules' || sec === 'all'){
      var lagFirst = function(m, lag){ return function(y, rp){ if(!rp[y].active) return 1; return (y > 0 && rp[y-1].active) ? m : 1 + (m-1)*(1-lag); }; };
      var R = [
        {l:'no stabilizer', p:Object.assign({}, REC, {stab:false})},
        {l:'hub protocol: x1.20 when income falls >=2%', p:arm(REC, {stabMult:1.2, stabThresh:0.02})},
        {l:'hub x1.20, 2-quarter detection lag (study only)', mult:lagFirst(1.2, 0.5)},
        {l:'fixed x1.1', p:arm(REC, {stabMult:1.1})}, {l:'fixed x1.3', p:arm(REC, {stabMult:1.3})}, {l:'fixed x1.35', p:arm(REC, {stabMult:1.35})},
        {l:'fixed x1.4', p:arm(REC, {stabMult:1.4})}, {l:'fixed x1.5', p:arm(REC, {stabMult:1.5}), keep:true}, {l:'fixed x2', p:arm(REC, {stabMult:2})},
        {l:'x1.35, one-year data lag (study only)', mult:function(y, rp){ return (y > 0 && rp[y-1].active) ? 1.35 : 1; }},
        {l:'x1.35, held one year after (study only)', mult:function(y, rp){ return (rp[y].active || (y > 0 && rp[y-1].active)) ? 1.35 : 1; }},
        {l:'x1.5 when income loss >=10%', p:arm(REC, {stabMult:1.5, stabThresh:0.10})}, {l:'x1.5 when income loss >=15%', p:arm(REC, {stabMult:1.5, stabThresh:0.15})},
        {l:'scaled, +2.5% per 1% loss', p:arm(REC, {stabSev:true, stabK:2.5})}, {l:'scaled, +2.75% per 1% loss', p:arm(REC, {stabSev:true, stabK:2.75})},
        {l:'scaled, +3% per 1% loss', p:arm(REC, {stabSev:true, stabK:3})},
        {l:'x1.35 + expiry suspended', p:arm(REC, {stabMult:1.35, stabSusp:true})},
        {l:'x1.35 + emergency enrollment, 50% take-up', p:arm(REC, {stabMult:1.35, emerg:true, emergTakeup:0.5})},
        {l:'x1.35 + emergency enrollment, 100% take-up', p:arm(REC, {stabMult:1.35, emerg:true, emergTakeup:1})},
        {l:'always-on raise, same 20-yr budget as x1.5 (study only)', budgetOf:true}];
      /* the engine's declared rule and the outside-runYear multiplier must agree exactly */
      var e1 = shockRun(arm(REC, {stabMult:1.35}), 7), e2 = shockRunWith(REC, 7, function(y, rp){ return rp[y].active ? 1.35 : 1; });
      console.log('engine rule = outside multiplier (seed 7, x1.35): ' + (JSON.stringify(e1.dAll) === JSON.stringify(e2.dAll) ? 'identical' : 'DIFFERENT'));
      console.log('=== Rules at the reference settings: Full Integration + recessions, seeds 1-' + nS + ', ' + AG + ' agents, 20yr ===');
      console.log(HDR);
      table(REC, R, nS).forEach(function(a, i){ line(R[i].l, a); });
    }
    if (sec === 'neutral' || sec === 'all'){
      console.log('=== Shock-neutral multiplier (in-page search algorithm), seeds 1-' + nS + ' ===');
      [['Full Integration + recessions', REC], ['Adverse Environment', ADVERSE_REFERENCE], ['CCO Only + recessions', Object.assign({}, CCO_ONLY, {shock:true})], ['Stress Test', STRESS_TEST]].forEach(function(c){
        var st = shockStudy(Object.assign({}, c[1], {stab:false}), nS);
        console.log(c[0] + ': no stabilizer ' + f2(st.none.partPP) + ' pp (participants), ' + f2(st.none.nonPartPP) + ' pp (non-participants); hub ' + f2(st.hub.partPP) +
          ' pp; neutral ' + (st.neutral.reached ? 'x' : '>x') + st.neutral.m.toFixed(2) + '  [points ' + st.points.map(function(q){ return 'x' + q.m.toFixed(2) + ':' + f2(q.partPP); }).join(', ') + ']');
      });
    }
    if (sec === 'decision' || sec === 'all'){
      console.log('=== Pending decision: how the BU amount reaches a household. Seed-42 regression and shock-neutral multiplier under each option (seeds 1-' + nS + ') ===');
      [['v4.18 engine (1 allocation/yr, flat 20% relief)', 1, true], ['A: 12 allocations/yr, flat relief (not adopted)', 12, true], ['B: relief scales with BU (shipped in v4.19)', 1, false]].forEach(function(o){
        BU_ALLOCATIONS_PER_YEAR = o[1]; CCO_RELIEF_FLAT = o[2];
        var r = runScenario(FULL_INTEGRATION, 42), st = shockStudy(Object.assign({}, REC, {stab:false}), nS);
        var so = runScenario(STRESS_TEST, 42);
        console.log(o[0] + ': seed 42 ' + r.pov + '% / $' + r.wealth.toLocaleString() + ' / ' + r.bleiMed + 'd / Gini ' + r.gini + ' (Stress Test ' + so.pov + '% / $' + so.wealth.toLocaleString() + ')' +
          '; recessions, no stabilizer: ' + f2(st.none.partPP) + ' pp; hub x1.2: ' + f2(st.hub.partPP) + ' pp; neutral ' + (st.neutral.reached ? 'x' : '>x') + st.neutral.m.toFixed(2));
      });
      BU_ALLOCATIONS_PER_YEAR = 1; CCO_RELIEF_FLAT = false;
    }
    if (sec === 'cola' || sec === 'all'){
      console.log('=== COLA: Adverse Environment (2% inflation) and 5% inflation, seeds 1-' + nS + ' (final year) ===');
      console.log('scenario | wealth poverty % | basket poverty (net) % | housing distress % | extreme poverty per 10,000 | median wealth');
      [['Adverse Environment', ADVERSE_REFERENCE], ['Adverse Environment at 5% inflation', Object.assign({}, ADVERSE_REFERENCE, {inflRate:0.05})], ['Full Integration at 5.5% inflation', Object.assign({}, FULL_INTEGRATION, {inflRate:0.055})]].forEach(function(c){
        [['no COLA', {}], ['COLA, always (threshold 0)', {cola:true, colaThresh:0}], ['COLA, hub trigger (>5%)', {cola:true, colaThresh:0.05}]].forEach(function(v){
          var rs = runMany(Object.assign({}, c[1], v[1]), nS);
          console.log(c[0] + ', ' + v[0] + ' | ' + mean(col(rs,'pov')).toFixed(2) + ' | ' + mean(col(rs,'basketPov')).toFixed(2) + ' | ' + mean(col(rs,'distress')).toFixed(2) + ' | ' + (mean(col(rs,'epTotal'))*100).toFixed(1) + ' | $' + Math.round(mean(col(rs,'wealth'))).toLocaleString());
        });
      });
    }
  }

  /* ─── v4.21 modes: the studies behind CONTRIBUTING.md's v4.21 Release Notes ─── */
  function tCI(arr){ var n = arr.length, m = mean(arr), v = 0; arr.forEach(function(x){ v += (x-m)*(x-m); }); var sd = n > 1 ? Math.sqrt(v/(n-1)) : 0, df = Math.max(1, n-1);
    return {m:m, h:(1.96 + 2.37/df)*sd/Math.sqrt(n), sd:sd, n:n}; }  // Cornish-Fisher t(0.975, df): within 0.002 of the exact value from df 30
  function fmtCI(arr, d){ var c = tCI(arr); return c.m.toFixed(d) + ' ±' + c.h.toFixed(d); }
  function trackRun(p, seed, ag0){  /* one run with the saving tallies; draws exactly as runScenario() does */
    RNG = mulberry32(seed + 700003);
    var ag = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
    var rp = p.shock ? buildRecessionPath(p.years, seed) : null;
    RNG = mulberry32(seed);
    var inc = 0, net = 0;
    for (var y = 0; y < p.years; y++){
      runYear(ag, y, p, rp ? rp[y] : {active:false, incomeMultiplier:1.0, yearsLeft:0});
      ag.forEach(function(a){ var i = a.yrWageUSD + (a.yrConvUSD || 0); inc += i; net += i - a.yrCostUSD - SURPLUS_CONSUMPTION_SHARE*Math.max(0, a.yrWageUSD - a.yrCostUSD); });
    }
    var m = calcMetrics(ag, p.ccoOn, p.pth), b = bleiMetrics(ag, p.bu, p.ccoOn, p.pth, p.szh, p.szhCoh, p.ptf), ib = incomeBasketMetrics(ag);
    return {pov:m.pov*100, wealth:m.med, gini:m.gini, bleiPov:(b.tc[0]+b.tc[1])/b.n*100, bleiMed:b.med, basketPov:ib.basketPov, saveRate:net/inc*100, agents:ag};
  }

  if (mode === 'largen') {
    /* Large-N confirmation of the headline figures: `node harness.js largen <seeds> <section> --agents=N`.
     * Sections: headline (the v4.17 comparator table, with 95% CIs across runs), presets, popsize (Full
     * Integration at 250-20,000 agents, holding total agents per size fixed, to look for finite-population
     * effects), all. Optional --out=<file> writes every run's figures as JSON. */
    CFG.WEALTH_FLOOR = -10000;
    var OUT = process.argv.filter(function(a){ return /^--out=/.test(a); })[0];
    process.argv = process.argv.filter(function(a){ return !/^--out=/.test(a); });
    var nL = parseInt(process.argv[3] || '500', 10), secL = process.argv[4] || 'all', dump = {agents:AG, seeds:nL, version:'4.21'}, t0L = Date.now();
    var KL = [['pov','wealth poverty %',1],['bleiPovPct','BLEI poverty %',1],['basketPov','basket poverty (net) %',1],['basketPovGross','basket poverty (gross) %',1],['incPov','relative income poverty %',1],['incPovExt','… incl. in-kind %',1],
      ['wealth','median wealth $',0],['bleiMed','median BLEI d',0],['gini','Gini (EDC-adj.)',3],['epTotal','extreme poverty /10k',1],['distress','housing distress %',1],['fracAtFloor','pinned at floor %',1]];
    function lvl(runs, k){ return col(runs, k).map(function(v){ return k === 'epTotal' ? v*100 : k === 'fracAtFloor' ? v*100 : v; }); }
    function levels(name, runs){ console.log(name + ': ' + KL.map(function(k){ return k[1] + ' ' + fmtCI(lvl(runs, k[0]), k[2]); }).join(' | ')); }
    if (secL === 'headline' || secL === 'all'){
      var FIL = runMany(FULL_INTEGRATION, nL), FI3L = runMany(Object.assign({}, FULL_INTEGRATION, {inflRate:0.03}), nL), B3L = runMany(BASELINE, nL), B0L = runMany(Object.assign({}, BASELINE, {inflRate:0}), nL);
      dump.headline = {FI:FIL, FI3:FI3L, B3:B3L, B0:B0L};
      console.log('=== Headline (v4.21 large-N): seeds 1-' + nL + ', ' + AG + ' agents, 20yr, shocks off. Levels are means across runs ±95% CI ===');
      levels('Full Integration', FIL); levels('Baseline @3% (shipped)', B3L); levels('Baseline @0% (matched)', B0L); levels('Full Integration @3%', FI3L);
      console.log('year 0 (policy-neutral): wealth poverty ' + fmtCI(col0(FIL,'pov'),1) + ' | BLEI poverty ' + fmtCI(col0(FIL,'bleiPovNeutral'),1) + ' | basket poverty ' + fmtCI(col0(FIL,'basketPov'),1) + ' | relative income poverty ' + fmtCI(col0(FIL,'incPov'),1));
      console.log('comparator | measure | comparator % | Full Integration % | reduction (ratio of means) | reduction (mean of per-run)');
      [['pov','wealth poverty'],['bleiPovPct','BLEI poverty'],['incPov','relative income poverty (cash)'],['incPovExt','relative income poverty (incl. in-kind)'],['basketPov','basket poverty (net)'],['basketPovGross','basket poverty (gross)']].forEach(function(m){
        [['Baseline @3% (shipped)', B3L, FIL, false],['Baseline @0% (inflation-matched)', B0L, FIL, false],['Baseline @3% vs FI @3%', B3L, FI3L, false],['Year 0 (policy-neutral)', FIL, FIL, true]].forEach(function(c){
          var k0 = m[0] === 'pov' ? 'pov' : m[0] === 'bleiPovPct' ? 'bleiPovNeutral' : m[0];
          var cmp = c[3] ? col0(c[1], k0) : col(c[1], m[0]), fi = col(c[2], m[0]);
          var pr = mean(cmp.map(function(v, i){ return v > 0 ? (1 - fi[i]/v)*100 : 0; }));
          console.log(c[0] + ' | ' + m[1] + ' | ' + f1(mean(cmp)) + ' | ' + f1(mean(fi)) + ' | ' + f1((1 - mean(fi)/mean(cmp))*100) + '% | ' + f1(pr) + '%');
        });
      });
    }
    if (secL === 'presets' || secL === 'all'){
      console.log('=== Presets (v4.21 large-N): seeds 1-' + nL + ', ' + AG + ' agents. Means across runs ±95% CI ===');
      dump.presets = {};
      [['CCO Only', CCO_ONLY], ['High Automation (25yr)', HIGH_AUTOMATION], ['Adverse Environment', ADVERSE_REFERENCE], ['Stress Test', STRESS_TEST],
       ['Weaker settings @ reference environment', Object.assign({}, STRESS_TEST, {shock:false, automation:false, inflRate:0})],
       ['CCO Only, adverse environment', ccoOnlyFor(ADVERSE_REFERENCE)], ['Baseline, adverse environment (3%)', baselineFor(ADVERSE_REFERENCE, false)]].forEach(function(c){
        var rs = runMany(c[1], nL); dump.presets[c[0]] = rs; levels(c[0], rs);
      });
    }
    if (secL === 'popsize' || secL === 'all'){
      var totL = parseInt(process.argv[5] || '1250000', 10);
      console.log('=== Population size (v4.21): Full Integration, ~' + totL.toLocaleString() + ' agent-runs per size (seeds = total / agents). Means ±95% CI ===');
      console.log('agents | seeds | wealth poverty % | BLEI poverty % | basket poverty % | median wealth $ | median BLEI d | Gini | pinned at floor %');
      dump.popsize = {};
      [250, 500, 1000, 2000, 5000, 10000, 20000].forEach(function(nA){
        var sd = Math.max(30, Math.round(totL/nA)), rs = runMany(Object.assign({}, FULL_INTEGRATION, {nAgents:nA}), sd);
        dump.popsize[nA] = rs.map(function(r){ return {pov:r.pov, bleiPovPct:r.bleiPovPct, basketPov:r.basketPov, wealth:r.wealth, bleiMed:r.bleiMed, gini:r.gini, fracAtFloor:r.fracAtFloor}; });
        console.log(nA + ' | ' + sd + ' | ' + fmtCI(col(rs,'pov'),2) + ' | ' + fmtCI(col(rs,'bleiPovPct'),2) + ' | ' + fmtCI(col(rs,'basketPov'),2) + ' | ' + fmtCI(col(rs,'wealth'),0) + ' | ' + fmtCI(col(rs,'bleiMed'),0) + ' | ' + fmtCI(col(rs,'gini'),4) + ' | ' + fmtCI(lvl(rs,'fracAtFloor'),2));
      });
    }
    if (OUT) require('fs').writeFileSync(OUT.split('=')[1], JSON.stringify(dump));
    console.error('largen runtime ' + ((Date.now() - t0L)/1000).toFixed(0) + 's');
  }

  if (mode === 'pathways') {
    /* v4.14 good-first-issue (b): how much of Full Integration's result comes through each channel.
     * Each arm switches one channel off (PATHWAY_OFF), CRN-paired with the full run; the effect of a
     * channel is full minus arm. Channels interact (octave feeds both wages and conversion rates), so
     * the single effects need not sum to the combined one; the gap is reported as the interaction. */
    CFG.WEALTH_FLOOR = -10000;
    var nW = parseInt(process.argv[3] || '200', 10);
    var ARMS = [['CCO cost relief', ['relief']], ['conversion proceeds', ['conversion']], ['octave advancement', ['octave']], ['octave wage bonus', ['octaveWage']],
      ['BLEI-gated wage bonus', ['bleiWage']], ['PTH cost reduction (and the equity it funds)', ['pthCost']], ['PTH equity routing and appreciation', ['pthEquity']],
      ['all four CCO channels', ['relief','conversion','octave','octaveWage']]];
    function armRuns(off){ Object.keys(PATHWAY_OFF).forEach(function(k){ PATHWAY_OFF[k] = off.indexOf(k) >= 0; }); var r = runMany(FULL_INTEGRATION, nW); Object.keys(PATHWAY_OFF).forEach(function(k){ PATHWAY_OFF[k] = false; }); return r; }
    var FULLW = armRuns([]);
    function d(rs, k){ return fmtCI(col(FULLW, k).map(function(v, i){ return v - rs[i][k]; }), k === 'wealth' ? 0 : 2); }
    console.log('=== Pathway decomposition (v4.21): Full Integration, seeds 1-' + nW + ', ' + AG + ' agents. Contribution of each channel = full run minus the run without it (paired, ±95% CI) ===');
    console.log('full run: wealth poverty ' + f1(mean(col(FULLW,'pov'))) + '%, BLEI poverty ' + f1(mean(col(FULLW,'bleiPovPct'))) + '%, basket poverty ' + f1(mean(col(FULLW,'basketPov'))) + '%, median wealth $' + Math.round(mean(col(FULLW,'wealth'))).toLocaleString());
    console.log('channel | median wealth $ | wealth poverty pp | BLEI poverty pp | basket poverty pp');
    var single = 0;
    ARMS.forEach(function(a, i){ var rs = armRuns(a[1]); var dw = mean(col(FULLW,'wealth')) - mean(col(rs,'wealth')); if (i < 4) single += dw;
      console.log(a[0] + ' | ' + d(rs,'wealth') + ' | ' + d(rs,'pov') + ' | ' + d(rs,'bleiPovPct') + ' | ' + d(rs,'basketPov'));
      if (i === 7) console.log('interaction among the four CCO channels (median wealth): combined minus the sum of single effects = $' + Math.round(dw - single).toLocaleString()); });
  }

  if (mode === 'saving') {
    /* v4.21: agents consume exactly their own (discounted) basket, so every dollar above it is saved.
     * `decile` shows the saving rates that implies; `sweep` consumes a share of the surplus
     * (SURPLUS_CONSUMPTION_SHARE, harness-only) and shows what moves. */
    CFG.WEALTH_FLOOR = -10000;
    var nV = parseInt(process.argv[3] || '200', 10), secV = process.argv[4] || 'all';
    if (secV === 'decile' || secV === 'all'){
      var dec = []; for (var q = 0; q < 10; q++) dec.push({inc:0, cost:0, conv:0, w0:0, w20:0, n:0});
      for (var sV = 1; sV <= nV; sV++){
        RNG = mulberry32(sV + 700003); var agV = makeLatentPopulation(FULL_INTEGRATION.nAgents).map(function(l){ return instantiateAgent(l, FULL_INTEGRATION); });
        var w0V = agV.map(function(a){ return a.wealth; }), cumV = agV.map(function(){ return {inc:0, cost:0, conv:0}; });
        RNG = mulberry32(sV);
        for (var yV = 0; yV < FULL_INTEGRATION.years; yV++){ runYear(agV, yV, FULL_INTEGRATION, {active:false, incomeMultiplier:1, yearsLeft:0}); agV.forEach(function(a, i){ cumV[i].inc += a.yrWageUSD; cumV[i].cost += a.yrCostUSD; cumV[i].conv += a.yrConvUSD || 0; }); }
        agV.map(function(a, i){ return i; }).sort(function(i, j){ return agV[i].wealth - agV[j].wealth; }).forEach(function(i, r){ var b = dec[Math.min(9, Math.floor(r/agV.length*10))]; b.inc += cumV[i].inc; b.cost += cumV[i].cost; b.conv += cumV[i].conv; b.w0 += w0V[i]; b.w20 += agV[i].wealth; b.n++; });
      }
      console.log('=== Where Full Integration wealth comes from: final-wealth deciles, seeds 1-' + nV + ', ' + AG + ' agents (per agent, 20-year totals) ===');
      console.log('decile | wage income | own basket cost | conversion | starting wealth | final wealth | floor, PTH and other | 20-yr saving rate');
      dec.forEach(function(b, i){ var f = function(k){ return '$' + Math.round(b[k]/b.n).toLocaleString(); };
        console.log('D' + (i+1) + ' | ' + f('inc') + ' | ' + f('cost') + ' | ' + f('conv') + ' | ' + f('w0') + ' | ' + f('w20') + ' | $' + Math.round((b.w20 - b.w0 - (b.inc - b.cost + b.conv))/b.n).toLocaleString() + ' | ' + ((b.inc - b.cost + b.conv)/(b.inc + b.conv)*100).toFixed(0) + '%'); });
    }
    if (secV === 'sweep' || secV === 'all'){
      console.log('=== Consuming a share of the surplus above the basket (harness-only): seeds 1-' + nV + ', ' + AG + ' agents ===');
      console.log('share consumed | scenario | 20-yr saving rate % | wealth poverty % | BLEI poverty % | basket poverty % | median wealth $ | Gini');
      var keep = {};
      [0, 0.5, 0.75, 0.9].forEach(function(sh){
        SURPLUS_CONSUMPTION_SHARE = sh;
        [['Full Integration', FULL_INTEGRATION], ['Baseline @0% (matched)', Object.assign({}, BASELINE, {inflRate:0})], ['Baseline @3% (shipped)', BASELINE]].forEach(function(c){
          var rs = []; for (var s2 = 1; s2 <= nV; s2++){ var t = trackRun(c[1], s2); delete t.agents; rs.push(t); }
          keep[sh + c[0]] = rs;
          console.log(sh + ' | ' + c[0] + ' | ' + f1(mean(col(rs,'saveRate'))) + ' | ' + f1(mean(col(rs,'pov'))) + ' | ' + f1(mean(col(rs,'bleiPov'))) + ' | ' + f1(mean(col(rs,'basketPov'))) + ' | $' + Math.round(mean(col(rs,'wealth'))).toLocaleString() + ' | ' + mean(col(rs,'gini')).toFixed(3));
        });
        var fi = keep[sh + 'Full Integration'], b0 = keep[sh + 'Baseline @0% (matched)'];
        console.log('   reduction vs matched Baseline at share ' + sh + ': wealth poverty ' + f1((1 - mean(col(fi,'pov'))/mean(col(b0,'pov')))*100) + '%, BLEI poverty ' + f1((1 - mean(col(fi,'bleiPov'))/mean(col(b0,'bleiPov')))*100) + '%');
      });
      SURPLUS_CONSUMPTION_SHARE = 0;
    }
  }

  if (mode === 'ledger') {
    /* A1 issuance ledger (Next Round Plan, Sep 26 2026): `node harness.js ledger <seeds> [section]`.
     * Reporting only. Sums the money flows runYear() already computes (LEDGER, above) for every current
     * scenario: per person per year, per participant per year, 20-year cumulative per person, and as a
     * share of aggregate cash income (wage income + net conversion proceeds, the engine's own income
     * definition since v4.17). Dollar figures are in year-0 dollars (each year's flow divided by that
     * year's price index); shares are ratios of nominal sums. Sections: identity (LEDGER on vs off is
     * bit-identical on every scenario), scenarios, tiers, years, deciles, framework, all. */
    CFG.WEALTH_FLOOR = -10000;
    var nLd = parseInt(process.argv[3] || '500', 10), secLd = process.argv[4] || 'all';
    var SCN = [['Full Integration', FULL_INTEGRATION], ['CCO Only', CCO_ONLY], ['Baseline @3% (shipped comparator)', BASELINE],
      ['Baseline @0% (matched)', Object.assign({}, BASELINE, {inflRate:0})], ['High Automation (25 yr)', HIGH_AUTOMATION],
      ['Adverse Environment', ADVERSE_REFERENCE], ['Stress Test', STRESS_TEST]];
    function ledgerRun(p, seed){  /* draws exactly as runScenario() does; returns the agents for end-of-run stocks */
      RNG = mulberry32(seed + 700003);
      var ag = makeLatentPopulation(p.nAgents).map(function(l){ return instantiateAgent(l, p); });
      var nPTH0 = ag.filter(function(a){ return a.inPTH; }).length;
      var rp = p.shock ? buildRecessionPath(p.years, seed) : null;
      RNG = mulberry32(seed);
      for (var y = 0; y < p.years; y++) runYear(ag, y, p, rp ? rp[y] : {active:false, incomeMultiplier:1.0, yearsLeft:0});
      return {agents:ag, nPTH0:nPTH0};
    }
    function ledgerScenario(p, N){
      var L = newLedger(), outBU = 0, acre0 = 0, dec = []; for (var q = 0; q < 10; q++) dec.push({floor:0, n:0, w:0, hit:0});
      LEDGER = L;
      for (var sd = 1; sd <= N; sd++){
        var r = ledgerRun(p, sd), ag = r.agents;
        acre0 += 5000*r.nPTH0;
        ag.forEach(function(a){ outBU += a.buBalance || 0; });
        ag.map(function(a, i){ return i; }).sort(function(i, j){ return ag[i].wealth - ag[j].wealth; }).forEach(function(i, rk){
          var b = dec[Math.min(9, Math.floor(rk/ag.length*10))]; b.floor += ag[i]._ledFloor || 0; b.w += ag[i].wealth; b.n++; if (ag[i]._ledFloor) b.hit++; });
      }
      LEDGER = null;
      return {L:L, real:L.real, outBU:outBU, acre0:acre0, dec:dec, N:N, p:p};
    }
    function g(o, k){ return o[k] || 0; }
    function usd(x){ return (x < 0 ? '−$' : '$') + Math.round(Math.abs(x)).toLocaleString('en-US'); }
    function pct(x){ return (x*100).toFixed(1) + '%'; }
    var FLOWS = [
      ['buIssued', 'BU credited to the balance (engine: one allocation a year)', 'created'],
      ['buSpent', 'BU spent from the balance (= BU converted)', 'memo'],
      ['buExpired', 'BU expired unspent (destroyed)', 'memo'],
      ['ccoRelief', 'CCO cost relief (the engine\'s proxy for BU spent on essentials)', 'created'],
      ['emergRelief', 'Emergency-enrollment relief (stabilizer; off in every preset)', 'created'],
      ['convGross', 'Conversion, gross (BU × rate × CIP bonus × income shock)', 'memo'],
      ['convTax', 'Conversion-tax leakage (credited to no one)', 'memo'],
      ['convNet', 'Primary currency created by conversion (net of leakage)', 'created'],
      ['ptfRelief', 'PTF cost reduction (no balance sheet or capital cost in the engine)', 'unfunded'],
      ['pthRelief', 'PTH cost reduction (no balance sheet or capital cost in the engine)', 'unfunded'],
      ['pthEquityContrib', 'PTH equity routing (wealth → Acre Equity; an internal transfer)', 'transfer'],
      ['pthAppr', 'PTH appreciation, total (added to Acre Equity)', 'asset'],
      ['pthApprLiquid', '… of which credited to liquid wealth', 'asset'],
      ['floor', 'Wealth-floor absorption (deficits below −$10,000 written off)', 'created'],
      ['surplusConsumed', 'Memo: surplus consumed (only when SURPLUS_CONSUMPTION_SHARE > 0)', 'memo'],
      ['wage', 'Memo: wage income', 'memo'],
      ['cost', 'Memo: basket cost actually paid (after reductions)', 'memo']];

    if (secLd === 'identity' || secLd === 'all'){
      console.log('=== Ledger on vs off: runScenario() output compared field by field, seeds 1-5, every scenario ===');
      var allSame = true;
      SCN.forEach(function(c){ for (var sd = 1; sd <= 5; sd++){ LEDGER = null; var a0 = JSON.stringify(runScenario(c[1], sd)); LEDGER = newLedger(); var a1 = JSON.stringify(runScenario(c[1], sd)); LEDGER = null; if (a0 !== a1){ allSame = false; console.log('  DIFFERS: ' + c[0] + ' seed ' + sd); } } });
      console.log(allSame ? '  identical in all ' + SCN.length*5 + ' runs' : '  NOT IDENTICAL');
      if (!allSame) process.exitCode = 1;
    }
    var RES = {};
    function res(c){ return RES[c[0]] || (RES[c[0]] = ledgerScenario(c[1], nLd)); }

    if (secLd === 'scenarios' || secLd === 'all'){
      SCN.forEach(function(c){
        var R = res(c), T = R.L.tot, rl = R.real, ay = g(T,'agentYears'), py = g(T,'partYears'), nAg = ay/c[1].years, inc = g(T,'wage') + g(T,'convNet');
        console.log('\n=== Issuance ledger: ' + c[0] + ' — seeds 1-' + nLd + ', ' + c[1].nAgents + ' agents, ' + c[1].years + ' yr; participants ' + pct(py/ay) + ' of agent-years; year-0 dollars ===');
        console.log('| Flow | Per person per year | Per participant per year | ' + c[1].years + '-yr cumulative per person | Share of cash income |');
        console.log('|---|---|---|---|---|');
        FLOWS.forEach(function(f){ var v = g(rl, f[0]); if (!v && f[2] === 'memo' && f[0] === 'surplusConsumed') return;
          var pp = ['buIssued','buSpent','buExpired','ccoRelief','convGross','convTax','convNet'].indexOf(f[0]) >= 0 && py > 0 ? usd(v/py) : '—';
          console.log('| ' + f[1] + ' | ' + usd(v/ay) + ' | ' + pp + ' | ' + usd(v/nAg) + ' | ' + pct(g(T,f[0])/inc) + ' |'); });
        console.log('| BU outstanding at the end of the run (stock, per participant) | — | ' + (py ? usd(R.outBU/(py/c[1].years)) : '—') + ' | — | — |');
        console.log('| Acre Equity endowment at year 0 ($5,000 per PTH member; read by no metric) | — | — | ' + usd(R.acre0/nAg) + ' | — |');
        var created = g(T,'ccoRelief') + g(T,'emergRelief') + g(T,'convNet'), unf = g(T,'ptfRelief') + g(T,'pthRelief');
        console.log('Summary, shares of cash income: created by program design (CCO relief + conversion) ' + pct(created/inc) + '; unfunded cost reductions (PTF + PTH) ' + pct(unf/inc) + '; PTH liquid appreciation ' + pct(g(T,'pthApprLiquid')/inc) + '; wealth-floor absorption (unfinanced deficits, in every scenario including the Baseline) ' + pct(g(T,'floor')/inc) + '. Floor hit in ' + pct(g(T,'floorHits')/ay) + ' of agent-years. Last seed\'s final price index ' + (R.L.y[c[1].years-1].pIdx || 1).toFixed(3) + '.');
      });
    }
    if (secLd === 'tiers' || secLd === 'all'){
      ['Full Integration','CCO Only','Adverse Environment','Stress Test'].forEach(function(nm){
        var c = SCN.filter(function(x){ return x[0] === nm; })[0], R = res(c), tt = R.L.tiers, bu = tt.reduce(function(s,t){ return s + t.bu; }, 0), net = tt.reduce(function(s,t){ return s + t.net; }, 0);
        console.log('\n=== Conversion by rate tier: ' + nm + ' (all years; nominal) ===');
        console.log('| Rate tier | Share of conversion events | Share of BU converted | Mean rate | Share of net proceeds | Tax share of gross |');
        console.log('|---|---|---|---|---|---|');
        var lab = ['1–1.5×','1.5–3×','3–6×','6–9×','9× and up'], nEv = tt.reduce(function(s,t){ return s + t.n; }, 0);
        tt.forEach(function(t, i){ console.log('| ' + lab[i] + ' | ' + pct(t.n/nEv) + ' | ' + pct(t.bu/bu) + ' | ' + (t.bu ? (t.gross/t.bu).toFixed(2) + '×' : '—') + ' | ' + pct(t.net/net) + ' | ' + (t.gross ? pct(t.tax/t.gross) : '—') + ' |'); });
        console.log('Mean rate across all BU converted (rate × BU ÷ BU): ' + (g(R.L.tot,'convRateXspend')/g(R.L.tot,'buSpent')).toFixed(2) + '×; net proceeds per BU converted: ' + (net/bu).toFixed(2));
      });
    }
    if (secLd === 'years' || secLd === 'all'){
      ['Full Integration','Adverse Environment'].forEach(function(nm){
        var c = SCN.filter(function(x){ return x[0] === nm; })[0], R = res(c);
        console.log('\n=== By year: ' + nm + ' (share of that year\'s cash income; mean conversion rate) ===');
        console.log('| Year | CCO relief | Conversion (net) | Floor absorption | All created | Mean rate | Floor hits |');
        console.log('|---|---|---|---|---|---|---|');
        [0,4,9,14,19].forEach(function(y){ var Y = R.L.y[y], inc = g(Y,'wage') + g(Y,'convNet');
          console.log('| ' + (y+1) + ' | ' + pct(g(Y,'ccoRelief')/inc) + ' | ' + pct(g(Y,'convNet')/inc) + ' | ' + pct(g(Y,'floor')/inc) + ' | ' + pct((g(Y,'ccoRelief')+g(Y,'emergRelief')+g(Y,'convNet')+g(Y,'floor'))/inc) + ' | ' + (g(Y,'buSpent') ? (g(Y,'convRateXspend')/g(Y,'buSpent')).toFixed(2) + '×' : '—') + ' | ' + pct(g(Y,'floorHits')/g(Y,'agentYears')) + ' |'); });
      });
    }
    if (secLd === 'deciles' || secLd === 'all'){
      console.log('\n=== Wealth-floor absorption by final-wealth decile (per agent, 20-yr total, nominal) ===');
      console.log('| Decile | ' + ['Full Integration','CCO Only','Baseline @0% (matched)','Baseline @3% (shipped comparator)'].join(' | ') + ' |');
      console.log('|---|---|---|---|---|');
      var DS = ['Full Integration','CCO Only','Baseline @0% (matched)','Baseline @3% (shipped comparator)'].map(function(nm){ return res(SCN.filter(function(x){ return x[0] === nm; })[0]); });
      for (var q2 = 0; q2 < 10; q2++) console.log('| D' + (q2+1) + ' | ' + DS.map(function(R){ var b = R.dec[q2]; return usd(b.floor/b.n) + ' (' + pct(b.hit/b.n) + ' hit)'; }).join(' | ') + ' |');
    }
    if (secLd === 'consume'){
      /* The consumption-rule decision (v4.21, open): what each rule does to saving, to spending out of the flows the
       * system creates, to the floor, and to the headline figures. Paired seeds; not part of `all` (it reruns). */
      console.log('\n=== Consumption rule: seeds 1-' + nLd + ', ' + AG + ' agents, 20 yr (shares of cash income = wage + net conversion) ===');
      console.log('| Scenario | Rule | Saving rate, deficits as dissaving | Saving rate, floor write-offs as unmet need | Surplus consumed (share of income) | Floor absorption | Wealth poverty | BLEI poverty | Basket poverty | Median wealth |');
      console.log('|---|---|---|---|---|---|---|---|---|---|');
      var RULES = [[0,'wage','shipped: consume the basket, save the rest'],[0.5,'wage','v4.21 sweep: 0.5 of wage surplus'],[0.9,'wage','v4.21 sweep: 0.9 of wage surplus'],[0.5,'cash','0.5 of all cash surplus'],[0.75,'cash','0.75 of all cash surplus'],[0.9,'cash','0.9 of all cash surplus'],[0.95,'cash','0.95 of all cash surplus']];
      [['Full Integration', FULL_INTEGRATION], ['Baseline @0% (matched)', Object.assign({}, BASELINE, {inflRate:0})], ['Baseline @3% (shipped comparator)', BASELINE], ['Adverse Environment', ADVERSE_REFERENCE]].forEach(function(c){
        RULES.forEach(function(ru){
          SURPLUS_CONSUMPTION_SHARE = ru[0]; SURPLUS_CONSUMPTION_BASE = ru[1]; LEDGER = newLedger();
          var rs = []; for (var sd = 1; sd <= nLd; sd++) rs.push(runScenario(c[1], sd));
          var T = LEDGER.tot; LEDGER = null; SURPLUS_CONSUMPTION_SHARE = 0; SURPLUS_CONSUMPTION_BASE = 'wage';
          var inc = g(T,'wage') + g(T,'convNet'), cons = g(T,'surplusConsumed');
          var sr1 = (inc - g(T,'cost') - cons + g(T,'pthApprLiquid'))/inc, sr2 = (inc - (g(T,'cost') - g(T,'floor')) - cons + g(T,'pthApprLiquid'))/inc;
          function m(k){ return rs.reduce(function(a, r){ return a + r[k]; }, 0)/rs.length; }
          console.log('| ' + c[0] + ' | ' + ru[2] + ' | ' + pct(sr1) + ' | ' + pct(sr2) + ' | ' + pct(cons/inc) + ' | ' + pct(g(T,'floor')/inc) + ' | ' + m('pov').toFixed(1) + '% | ' + m('bleiPovPct').toFixed(1) + '% | ' + m('basketPov').toFixed(1) + '% | ' + usd(m('wealth')) + ' |');
        });
      });
    }
    if (secLd === 'framework' || secLd === 'all'){
      /* Derived, not simulated: the engine converts one allocation a year and nothing it counts as essentials
       * spending. The Research Hub describes businesses and creators converting every BU they accept. */
      var R2 = res(SCN[0]), T2 = R2.L.tot, py2 = g(T2,'partYears'), inc2 = g(T2,'wage') + g(T2,'convNet'), mr = g(T2,'convRateXspend')/g(T2,'buSpent'), taxS = g(T2,'convTax')/g(T2,'convGross');
      var reliefPP = g(T2,'ccoRelief')/py2, fwBU = FULL_INTEGRATION.bu*12;
      console.log('\n=== Derived scale check (Full Integration; arithmetic on the ledger, not a simulation result) ===');
      console.log('Framework issuance at $' + FULL_INTEGRATION.bu + '/month: ' + usd(fwBU) + ' per participant per year.');
      console.log('Engine: relief ' + usd(reliefPP) + ' + balance credit ' + usd(g(T2,'buIssued')/py2) + ' = ' + usd(reliefPP + g(T2,'buIssued')/py2) + ' per participant per year (' + pct((reliefPP + g(T2,'buIssued')/py2)/fwBU) + ' of framework issuance).');
      console.log('Engine conversion creates ' + usd(g(T2,'convNet')/py2) + ' per participant per year (' + pct(g(T2,'convNet')/inc2) + ' of cash income).');
      [['every BU issued, at par (1×)', fwBU, 1], ['every BU issued, at the engine\'s mean participant rate', fwBU, mr], ['the relief-BU only, at par', reliefPP, 1], ['the relief-BU only, at the engine\'s mean rate', reliefPP, mr]].forEach(function(z){
        var cr = z[1]*z[2]*(1-taxS);
        console.log('If receivers converted ' + z[0] + ' (' + z[2].toFixed(2) + '×, less the engine\'s ' + pct(taxS) + ' average tax): ' + usd(cr) + ' per participant per year, ' + pct(cr*py2/inc2) + ' of cash income.');
      });
    }
  }

  if (mode === 'price') {
    /* Session 2 (Next Round Plan A2, and decisions D1, D2, D4, N1-N10): `node harness.js price <seeds> [section]`.
     * Every section runs under the next round's rule (NEXT_ROUND, D1) and D6's COLA unless it says otherwise; each is
     * CRN-paired (the same seeds for every arm). Sections: basket | d1 | framework | ptf | breakeven | sens | all (session 2);
     * be | inert | sweep | corners | stab (session 3, not run by `all`; `sweep`, `inert`, `corners` and `be` take an optional
     * scenario list as the next argument: fi,adv,st). */
    CFG.WEALTH_FLOOR = -10000;
    var nP = parseInt(process.argv[3] || '200', 10), secP = process.argv[4] || 'all';
    var BASKET_LBL = {food:'Food', housing:'Housing (incl. utilities)', medical:'Medical', transport:'Transportation', civic:'Civic', internet:'Internet & mobile', other:'Other necessities', taxes:'Income and payroll taxes'};
    function pc(x, d){ return (x*100).toFixed(d === undefined ? 1 : d) + '%'; }
    function us(x){ return (x < 0 ? '−$' : '$') + Math.round(Math.abs(x)).toLocaleString('en-US'); }
    function meanOf(rs, k){ return rs.reduce(function(a, r){ return a + r[k]; }, 0)/rs.length; }
    var NEUTRAL = {a:1, pthUnmatched:false};   /* with S = null: prices never move, so a run is the plain engine plus unmet-need reporting */
    var ENVS = [['Full Integration', FULL_INTEGRATION], ['Adverse Environment', ADVERSE_REFERENCE], ['Stress Test', STRESS_TEST]];

    if (secP === 'basket' || secP === 'all'){
      var LW = CFG.LIVING_WAGE_ANNUAL, eS = CFG.ESSENTIALS.reduce(function(a, k){ return a + CFG.BASKET[k]; }, 0);
      console.log('=== N10: the living-wage basket by component (MIT LWC, Feb 15 2026, 1 adult 0 children; 8-state fit at $49,370) ===');
      console.log('| Component | Share | Dollars at $49,370 | Essential (BU, P_E) |'); console.log('|---|---|---|---|');
      CFG.BASKET_KEYS.forEach(function(k){ console.log('| ' + BASKET_LBL[k] + ' | ' + pc(CFG.BASKET[k]) + ' | ' + us(CFG.BASKET[k]*LW) + ' | ' + (CFG.ESSENTIALS.indexOf(k) >= 0 ? 'yes' : '—') + ' |'); });
      console.log('| Essentials | ' + pc(eS) + ' | ' + us(eS*LW) + ' | |');
      console.log('\nShipped cuts measured against the components they could plausibly act on (arithmetic):');
      [['PTF, shipped: 12% of the whole basket', 0.12*LW, 'food', CFG.BASKET.food*LW], ['PTF, shipped with SZH at 0.72: 14.9% of the basket', (0.12 + 0.72*0.04)*LW, 'food', CFG.BASKET.food*LW],
       ['PTH, shipped: 35% of the whole basket (non-PTF member)', 0.35*LW, 'housing', CFG.BASKET.housing*LW], ['PTH for a PTF member: 35% of the 88% basket', 0.35*0.88*LW, 'housing', CFG.BASKET.housing*LW],
       ['CCO relief at the $1,200 reference: 20% of the whole basket (non-member)', 0.20*LW, 'essentials', eS*LW]].forEach(function(z){
        console.log('  ' + z[0] + ': ' + us(z[1]) + ' = ' + pc(z[1]/z[3], 0) + ' of the ' + z[2] + ' component (' + us(z[3]) + ').'); });
      console.log('  Every shipped discount is taken on the whole basket, including its ' + pc(CFG.BASKET.taxes) + ' tax share (' + us(CFG.BASKET.taxes*LW) + '), which no price cut reduces.');
      console.log('  D4 settings as shares of the whole basket: food30 = ' + pc(0.30*CFG.BASKET.food) + ', food62 = ' + pc(0.62*CFG.BASKET.food) + ' (shipped 12%-14.9%).');
      console.log('  Framework BU budget, 12 x $1,200 = $14,400: ' + pc(14400/(eS*LW), 0) + ' of a non-member\'s essentials; a PTF+PTH member\'s essentials at shipped cuts cost ' + us(eS*LW*0.88*0.65) + ', so ' + us(14400 - eS*LW*0.88*0.65) + ' of the budget expires.');
    }

    if (secP === 'd1' || secP === 'all'){
      /* D1 before/after, no price module: shipped rule (save everything above the basket) vs the next round's rule. Lines nominal,
       * so the shipped column reproduces runScenario()'s figures. */
      var SC1 = [['Full Integration', FULL_INTEGRATION], ['CCO Only', CCO_ONLY], ['High Automation (25 yr)', HIGH_AUTOMATION], ['Adverse Environment', ADVERSE_REFERENCE],
        ['Stress Test', STRESS_TEST], ['Baseline @0% (matched)', Object.assign({}, BASELINE, {inflRate:0})], ['Baseline @3% (shipped comparator)', BASELINE]];
      console.log('\n=== D1: the consumption rule, before and after (seeds 1-' + nP + ', ' + AG + ' agents, CRN-paired; nominal lines; no price module) ===');
      console.log('| Scenario | Rule | Wealth poverty | BLEI poverty | Basket poverty | Median wealth | Unmet need, share of basket cost | Agent-years with unmet need |');
      console.log('|---|---|---|---|---|---|---|---|');
      var D1R = {};
      SC1.forEach(function(c){
        [['shipped (v4.21)', {SURPLUS_CONSUMPTION_SHARE:0, SURPLUS_CONSUMPTION_BASE:'wage'}, c[1]], ['D1: 0.9 of all cash surplus', NEXT_ROUND, nextRoundPreset(c[1])]].forEach(function(ru){
          var sv = applyRule(ru[1]), rs = []; for (var sd = 1; sd <= nP; sd++) rs.push(priceRun(ru[2], sd, Object.assign({lines:'nominal'}, NEUTRAL), null).res); applyRule(sv);
          D1R[c[0] + '|' + ru[0]] = rs;
          console.log('| ' + c[0] + ' | ' + ru[0] + ' | ' + meanOf(rs,'pov').toFixed(1) + '% | ' + meanOf(rs,'bleiPov').toFixed(1) + '% | ' + meanOf(rs,'basketPov').toFixed(1) + '% | ' + us(meanOf(rs,'medWealthReal')) + ' | ' + pc(meanOf(rs,'unmetShare')) + ' | ' + pc(meanOf(rs,'unmetYears')) + ' |');
        });
      });
      console.log('\nReduction against the matched Baseline under each rule (wealth / BLEI / basket poverty):');
      ['shipped (v4.21)', 'D1: 0.9 of all cash surplus'].forEach(function(ru){ var b = D1R['Baseline @0% (matched)|' + ru];
        ['Full Integration', 'CCO Only'].forEach(function(nm){ var r = D1R[nm + '|' + ru];
          console.log('  ' + ru + ', ' + nm + ': ' + ['pov','bleiPov','basketPov'].map(function(k){ return pc(1 - meanOf(r,k)/meanOf(b,k)); }).join(' / ')); }); });
    }

    if (secP === 'framework' || secP === 'all'){
      /* N1-N4: what the framework model moves, before any price feedback (a = 1, PTH matched, P_E held at 1). Ledger flows are
       * nominal; with no endogenous prices and 0% inflation in Full Integration they are also year-0 dollars. */
      console.log('\n=== N1-N4: engine vs framework conversion model (seeds 1-' + nP + '; D1 rule; no price feedback; FW = ' + JSON.stringify(FW) + ') ===');
      console.log('| Scenario | Model | Wealth poverty | BLEI poverty | Basket poverty | Unmet need | Median wealth (yr-0 $) | Relief (BU on essentials) per participant | BU expired per participant | Conversion net per participant | Conversion, share of cash income |');
      console.log('|---|---|---|---|---|---|---|---|---|---|---|');
      var svF = applyRule(NEXT_ROUND);
      ENVS.forEach(function(c){ var P = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){
          CONVERSION_MODEL = cm; LEDGER = newLedger(); var rs = []; for (var sd = 1; sd <= nP; sd++) rs.push(priceRun(P, sd, NEUTRAL, null).res);
          var T = LEDGER.real, py = LEDGER.tot.partYears || 1; LEDGER = null; CONVERSION_MODEL = 'engine';
          var conv = cm === 'engine' ? (T.convNet || 0) : (T.fwBizPayout || 0) + (T.fwProjNet || 0), expd = cm === 'engine' ? (T.buExpired || 0) : (T.fwBUExpired || 0);
          console.log('| ' + c[0] + ' | ' + cm + ' | ' + meanOf(rs,'pov').toFixed(1) + '% | ' + meanOf(rs,'bleiPov').toFixed(1) + '% | ' + meanOf(rs,'basketPov').toFixed(1) + '% | ' + pc(meanOf(rs,'unmetShare')) + ' | ' + us(meanOf(rs,'medWealthReal')) + ' | ' + us((T.ccoRelief || 0)/py) + ' | ' + us(expd/py) + ' | ' + us(conv/py) + ' | ' + pc(meanOf(rs,'convShare')) + ' |');
          if (cm === 'framework') console.log('|  | … of which business premium paid out ' + us((T.fwBizPayout || 0)/py) + ', projects ' + us((T.fwProjNet || 0)/py) + ' (mean project rate ' + ((T.fwProjRateXbu || 0)/Math.max(1, T.fwProjBU || 0)).toFixed(2) + '×; BU lost to octave caps ' + us((T.fwProjLost || 0)/py) + ') | | | | | | | | | |');
        });
      });
      applyRule(svF);
    }

    if (secP === 'ptf' || secP === 'all'){
      /* D4: three PTF settings on the split basket (engine model, D1 rule, no price feedback). */
      console.log('\n=== D4: PTF calibration settings (Full Integration, seeds 1-' + nP + ', engine model, D1 rule, no price feedback) ===');
      console.log('| PTF setting | Cut, share of a member\'s basket | PTF reduction per member-year | Wealth poverty | BLEI poverty | Basket poverty | Unmet need | Median wealth |');
      console.log('|---|---|---|---|---|---|---|---|');
      var svT = applyRule(NEXT_ROUND), P4 = nextRoundPreset(FULL_INTEGRATION);
      [['shipped', 'shipped: 12% + 4% × SZH on the whole basket'], ['food30', 'food30: the NYC pilot\'s promised 30%, food only'], ['food62', 'food62: the hub\'s ε_food = 2.64 (62%), food only']].forEach(function(m){
        PTF_MODE = m[0]; LEDGER = newLedger(); var ptfYears = 0, rs = [];
        for (var sd = 1; sd <= nP; sd++){ var rr = priceRun(P4, sd, NEUTRAL, null); rs.push(rr.res); ptfYears += rr.tot.ptfN; }
        var T = LEDGER.tot; LEDGER = null; PTF_MODE = 'shipped';
        var cutShare = m[0] === 'shipped' ? 0.12 + P4.szhCoh*0.04 : PTF_FOOD_CUT[m[0]]*CFG.BASKET.food;
        console.log('| ' + m[1] + ' | ' + pc(cutShare) + ' | ' + us((T.ptfRelief || 0)/ptfYears) + ' | ' + meanOf(rs,'pov').toFixed(1) + '% | ' + meanOf(rs,'bleiPov').toFixed(1) + '% | ' + meanOf(rs,'basketPov').toFixed(1) + '% | ' + pc(meanOf(rs,'unmetShare')) + ' | ' + us(meanOf(rs,'medWealthReal')) + ' |');
      });
      applyRule(svT);
    }

    var AGRID = [0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 1];
    if (secP === 'breakeven' || secP === 'all'){
      /* A2 headline, PRELIMINARY (session 3 sweeps the elasticities and PTF range): endogenous inflation against additionality a,
       * and the breakeven a at D3's tolerance (0.5 point a year) and at 1 point. Endogenous inflation is the annualized growth
       * of the endogenous basket index over the run (on top of any exogenous rate). The last row of each block holds a = 1 and
       * also counts PTH appreciation as matched, which leaves only the essentials channel. */
      var svB = applyRule(NEXT_ROUND);
      console.log('\n=== A2 breakeven additionality, PRELIMINARY (seeds 1-' + nP + '; D1, D2, D6; lamG ' + PM_DEFAULTS.lamG + '; theta ' + JSON.stringify(PM_DEFAULTS.theta) + '; ptfCap ' + PM_DEFAULTS.ptfCap + '; supply ' + PM_DEFAULTS.supply + ') ===');
      ENVS.forEach(function(c){ var P = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){
          CONVERSION_MODEL = cm;
          var grid = AGRID.map(function(a){ return {a:a}; }).concat([{a:1, pthUnmatched:false}, {a:1, supply:'baseline'}]), R = priceStudy(P, nP, grid, {});
          CONVERSION_MODEL = 'engine';
          var inf = R.slice(0, AGRID.length).map(function(r){ return r.endoAnn; });
          var b5 = breakevenA(AGRID, inf, 0.005), b10 = breakevenA(AGRID, inf, 0.010);
          console.log('\n' + c[0] + ', ' + cm + ' model: conversion ' + pc(R[0].convShare) + ' of cash income at a = 0. Breakeven a: ' + (b5 === null ? 'none (exceeds 0.5 pt even at a = 1)' : b5.toFixed(3)) + ' at 0.5 pt/yr; ' + (b10 === null ? 'none' : b10.toFixed(3)) + ' at 1 pt/yr.');
          console.log('| a | Endogenous inflation, mean pt/yr | Worst year | Endogenous index, yr 20 | P_G, yr 20 | Housing P_E, yr 20 | Real BU, yr 20 (yr-0 $) | Wealth poverty (D2) | BLEI poverty (D2) | Basket poverty | Unmet need |');
          console.log('|---|---|---|---|---|---|---|---|---|---|---|');
          R.forEach(function(r, i){ var lab = i < AGRID.length ? AGRID[i].toFixed(2) : i === AGRID.length ? '1.00, PTH matched' : '1.00, supply = Baseline same-year demand (upper bound)';
            console.log('| ' + lab + ' | ' + (r.endoAnn*100).toFixed(2) + ' | ' + (r.endoMax*100).toFixed(2) + ' | ' + r.endoIdx.toFixed(3) + ' | ' + r.PG.toFixed(3) + ' | ' + r.PEh.toFixed(3) + ' | ' + us(r.buReal) + ' | ' + r.pov.toFixed(1) + '% | ' + r.bleiPov.toFixed(1) + '% | ' + r.basketPov.toFixed(1) + '% | ' + pc(r.unmetShare) + ' |'); });
        });
      });
      applyRule(svB);
    }

    if (secP === 'sens' || secP === 'all'){
      /* A first look at how the breakeven moves with the two least-certain inputs (session 3 does the full sweep). */
      var svS = applyRule(NEXT_ROUND), P5 = nextRoundPreset(FULL_INTEGRATION);
      console.log('\n=== Breakeven a (0.5 pt / 1 pt) vs pass-through, Full Integration, seeds 1-' + nP + ' ===');
      console.log('| Model | lamG | Housing theta | Wage indexation | COLA (D6) | Supply | Breakeven at 0.5 pt | Breakeven at 1 pt | Inflation at a = 0 | Inflation at a = 1 |'); console.log('|---|---|---|---|---|---|---|---|---|---|');
      ['engine','framework'].forEach(function(cm){
        [[0.25, 0.6, 0, true, 'capacity'], [0.5, 0.6, 0, true, 'capacity'], [1, 0.6, 0, true, 'capacity'], [1, 0, 0, true, 'capacity'], [1, 0.78, 0, true, 'capacity'],
         [1, 0.6, 1, true, 'capacity'], [1, 0.6, 0, false, 'capacity'], [1, 0.6, 0, true, 'baseline']].forEach(function(z){
          CONVERSION_MODEL = cm; var Pz = Object.assign({}, P5, {cola:z[3]});
          var R = priceStudy(Pz, nP, AGRID.map(function(a){ return {a:a}; }), {lamG:z[0], theta:{housing:z[1]}, wIdx:z[2], supply:z[4]}); CONVERSION_MODEL = 'engine';
          var inf = R.map(function(r){ return r.endoAnn; }), b5 = breakevenA(AGRID, inf, 0.005), b10 = breakevenA(AGRID, inf, 0.010);
          console.log('| ' + cm + ' | ' + z[0] + ' | ' + z[1] + ' | ' + z[2] + ' | ' + (z[3] ? 'on (5%)' : 'off') + ' | ' + z[4] + ' | ' + (b5 === null ? 'none' : b5.toFixed(3)) + ' | ' + (b10 === null ? 'none' : b10.toFixed(3)) + ' | ' + (inf[0]*100).toFixed(2) + ' pt | ' + (inf[inf.length-1]*100).toFixed(2) + ' pt |');
        });
      });
      applyRule(svS);
    }

    /* ─── Session 3 sections (A2 sweeps and the breakeven report): be | inert | sweep [fi|adv|st] | corners | stab ───
     * Every section: D1 rule, D2 lines, D6 COLA (unless a row changes it), CRN-paired seeds 1-N. Endogenous inflation is the
     * annualized growth of the endogenous basket index over the run, on top of any exogenous rate. Breakevens come from
     * s3Breakeven (bracketed secant on the exact seed mean), with a 95% bootstrap interval over seeds and the share of seeds
     * whose own inflation exceeds the tolerance at that a. */
    function fmtB(b){ return b.be === null ? 'none' : b.be === 0 ? '0 (any a)' : b.be.toFixed(3) + ' [' + b.ci[0].toFixed(3) + '–' + b.ci[1].toFixed(3) + ']'; }
    function fmtA(b){ return b.be === null ? 'none' : b.be === 0 ? '0' : b.a90 === Infinity ? 'none (above 1)' : b.a90.toFixed(3); }
    function fmtS(b){ return b.be === null || b.be === 0 ? '—' : pc(b.above, 0); }
    function fmtN(n){ return n.an === null ? 'none up to ' + n.aMax : n.an.toFixed(3) + ' [' + n.ci[0].toFixed(3) + '–' + n.ci[1].toFixed(3) + ']'; }
    function pt(x){ return isFinite(x) && Math.abs(x) < 10 ? (x*100).toFixed(2) : 'diverges'; }
    var ENV3 = {fi:['Full Integration', FULL_INTEGRATION], adv:['Adverse Environment', ADVERSE_REFERENCE], st:['Stress Test', STRESS_TEST]};
    var envSel = (process.argv[5] || 'fi,adv,st').split(',');

    if (secP === 'be'){
      var svE = applyRule(NEXT_ROUND);
      console.log('\n=== A2 breakeven additionality, reference settings (seeds 1-' + nP + ', ' + AG + ' agents; D1, D2, D6; ' + S3_REF.lbl + ') ===');
      console.log('| Scenario | Model | Conversion, share of cash income (no feedback) | Inflation at a = 0 (pt/yr) | at a = 0.9 | at a = 1 | Breakeven a at 0.5 pt [95% CI] | Seeds above 0.5 pt there | a with 90% of seeds within 0.5 pt | Breakeven a at 1 pt [95% CI] | a with 90% of seeds within 1 pt | Price-neutral a (d18) [95% CI] | Points evaluated |');
      console.log('|---|---|---|---|---|---|---|---|---|---|---|---|---|');
      var BE = [];
      envSel.forEach(function(e){ var c = ENV3[e], P = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){
          var r = s3Config(P, Object.assign({}, S3_REF, {sw:{cm:cm}}), nP);
          if (r.b[0].be !== null){ var k = Math.round(r.b[0].be*1000)/1000; r.pBE = s3Config(P, Object.assign({}, S3_REF, {sw:{cm:cm}}), nP, {pts:r.pts, at:k}).pAt; r.kBE = k; }
          var sv0 = s3Set({cm:cm}); r.pNF = s3Point(P, {a:1, pthUnmatched:false}, 1, nP, false, true);
          r.n = s5Neutral(r.pts, function(a){ return s3Point(P, {}, a, nP); }); s3Reset(sv0);  /* session 5 (d18): the price-neutral point */
          BE.push([c[0], cm, r]);
          console.log('| ' + c[0] + ' | ' + cm + ' | ' + pc(r.pNF.m.convShare) + ' | ' + pt(r.p0.m.endoAnn) + ' | ' + pt(r.p09.m.endoAnn) + ' | ' + pt(r.p1.m.endoAnn) + ' | ' + fmtB(r.b[0]) + ' | ' + fmtS(r.b[0]) + ' | ' + fmtA(r.b[0]) + ' | ' + fmtB(r.b[1]) + ' | ' + fmtA(r.b[1]) + ' | ' + fmtN(r.n) + ' | ' + Object.keys(r.pts).length + ' |');
        });
      });
      console.log('\nPoverty under D2 (lines deflated by the full index): no price feedback, at the 0.5-pt breakeven, and at a = 1');
      console.log('| Scenario | Model | No feedback: wealth / BLEI / basket poverty | Unmet need | At breakeven (a) | Wealth / BLEI / basket poverty | Unmet need | Real BU, yr 20 (yr-0 $) | At a = 1: wealth / BLEI / basket | At a = 0: wealth / BLEI / basket |');
      console.log('|---|---|---|---|---|---|---|---|---|---|');
      BE.forEach(function(z){ var r = z[2], f = function(q){ return q.m.pov.toFixed(1) + '% / ' + q.m.bleiPov.toFixed(1) + '% / ' + q.m.basketPov.toFixed(1) + '%'; };
        console.log('| ' + z[0] + ' | ' + z[1] + ' | ' + f(r.pNF) + ' | ' + pc(r.pNF.m.unmetShare) + ' | ' + (r.pBE ? r.kBE.toFixed(3) : 'none') + ' | ' + (r.pBE ? f(r.pBE) : '—') + ' | ' + (r.pBE ? pc(r.pBE.m.unmetShare) : '—') + ' | ' + (r.pBE ? us(r.pBE.m.buReal) : '—') + ' | ' + f(r.p1) + ' | ' + f(r.p0) + ' |'); });
      applyRule(svE);
    }

    if (secP === 'inert'){
      /* Checks behind two shortcuts: (1) under capacity supply P_E never leaves 1, so theta and ptfCap cannot matter there
       * and the reference equals supply = baseline with theta 0; (2) the same holds with each stabilizer arm on. */
      var svI = applyRule(NEXT_ROUND);
      console.log('\n=== Capacity supply: does P_E ever move? (seeds 1-' + nP + '; a = 0 and a = 1; every stabilizer arm in the shock scenarios) ===');
      console.log('| Scenario | Model | Arm | Seed-years with essentials demand above capacity (a = 0 / a = 1) | Max P_E housing | Reference identical to supply = baseline with theta 0 |');
      console.log('|---|---|---|---|---|---|');
      envSel.forEach(function(e){ var c = ENV3[e], P0 = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){ var sv1 = s3Set({cm:cm});
          (c[1].shock ? s3StabArms() : [{id:'none', lbl:'—', preset:{}}]).forEach(function(arm){
            var P = Object.assign({}, P0, arm.preset), cnt = [0, 0], mx = 1, same = true;
            [0, 1].forEach(function(a, ai){
              for (var sd = 1; sd <= nP; sd++){ var S = s3BaseS(P, sd), r = priceRun(P, sd, {a:a}, S);
                r.path.forEach(function(q, t){ if (q.d > S[0] + 1e-12) cnt[ai]++; mx = Math.max(mx, q.PEh); });
                if (ai === 0 && arm.id === 'none'){ var r2 = priceRun(P, sd, {a:a, supply:'baseline', theta:{food:0, housing:0, medical:0}}, S); if (r2.res.endoAnn !== r.res.endoAnn || r2.res.pov !== r.res.pov) same = false; } }
            });
            console.log('| ' + c[0] + ' | ' + cm + ' | ' + arm.lbl + ' | ' + cnt[0] + ' / ' + cnt[1] + ' of ' + nP*P.years + ' | ' + mx.toFixed(4) + ' | ' + (arm.id === 'none' ? (same ? 'yes, bit-identical' : 'no') : '—') + ' |');
          });
          s3Reset(sv1); });
      });
      /* How much theta can move endogenous inflation under capacity supply (it replaces two sweep rows). */
      console.log('\nMean endogenous inflation (pt/yr) under capacity supply by essentials pass-through, seeds 1-' + nP + ':');
      console.log('| Scenario | Model | a | theta 0 (no essentials channel) | Reference (0 / 0.6 / 0.5) | theta high (0.2* / 0.78 / 1.0*) |'); console.log('|---|---|---|---|---|---|');
      envSel.forEach(function(e){ var c = ENV3[e], P = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){ var sv3 = s3Set({cm:cm});
          [0.9, 1].forEach(function(a){ var v = [{food:0, housing:0, medical:0}, {}, {food:0.2, housing:0.78, medical:1.0}].map(function(th){ return s3Point(P, {theta:th}, a, nP).m.endoAnn; });
            console.log('| ' + c[0] + ' | ' + cm + ' | ' + a + ' | ' + v.map(function(x){ return (x*100).toFixed(3); }).join(' | ') + ' |'); });
          s3Reset(sv3); });
      });
      applyRule(svI);
    }

    if (secP === 'sweep'){
      var svW = applyRule(NEXT_ROUND);
      envSel.forEach(function(e){ var c = ENV3[e], P = nextRoundPreset(c[1]), bp = baselineFor(P, true);
        var n5 = 0; for (var sd = 1; sd <= nP; sd++) n5 += priceRun(bp, sd, {floorUnmatched:true}, null).res.endoAnn/nP;
        console.log('\n=== A2 one-at-a-time sweep: ' + c[0] + ' (seeds 1-' + nP + ', ' + AG + ' agents; D1, D2) ===');
        console.log('N5 alternative, shown once: under it the matched Baseline (no program) has endogenous inflation of ' + pt(n5) + ' pt/yr from its own floor write-offs.');
        console.log('| Row | Group | Engine: breakeven at 0.5 pt [95% CI] | at 1 pt | Inflation at a = 0 / 1 (pt) | Framework: breakeven at 0.5 pt [95% CI] | at 1 pt | Inflation at a = 0 / 1 (pt) |');
        console.log('|---|---|---|---|---|---|---|---|');
        S3_ROWS.forEach(function(row){
          var cells = ['engine','framework'].map(function(cm){
            if (row.fwOnly && cm === 'engine') return ['n/a', 'n/a', '—'];
            var sw = Object.assign({}, row.sw || {}, {cm:cm}), r = s3Config(P, Object.assign({}, row, {sw:sw}), nP);
            return [fmtB(r.b[0]), fmtB(r.b[1]), pt(r.p0.m.endoAnn) + ' / ' + pt(r.p1.m.endoAnn)];
          });
          console.log('| ' + row.lbl + ' | ' + row.grp + ' | ' + cells[0].join(' | ') + ' | ' + cells[1].join(' | ') + ' |');
        });
      });
      applyRule(svW);
    }

    if (secP === 'corners'){
      /* The parameter envelope: every 'parameter' row of the sweep set at the end of its range that gave the higher (or lower)
       * breakeven in the one-at-a-time sweep, under the adopted structure (capacity supply, where theta and ptfCap are inert),
       * and the upper bound: the high corner plus the structural alternatives that raised the breakeven. */
      var svC = applyRule(NEXT_ROUND);
      var CORNERS = [
        {id:'lo', grp:'envelope', lbl:'Low corner: lamG 0.25, wIdx 1, aw 1; framework: bizRate 2', opts:{lamG:0.25, wIdx:1}, fw:{bizRate:2, bizCap:1}},
        {id:'hi', grp:'envelope', lbl:'High corner: lamG 1, wIdx 0, aw 0; framework: bizRate 4, bizCap 1', opts:{lamG:1, wIdx:0, aw:0}, fw:{bizRate:4, bizCap:1}},
        {id:'ub', grp:'upper bound', lbl:'High corner + Baseline same-year supply + theta high + floor write-offs unmatched', opts:{lamG:1, wIdx:0, aw:0, supply:'baseline', theta:{food:0.2, housing:0.78, medical:1.0}, floorUnmatched:true}, fw:{bizRate:4, bizCap:1}}];
      console.log('\n=== A2 envelope: breakeven a at the corners of the swept parameter ranges (seeds 1-' + nP + ', ' + AG + ' agents) ===');
      console.log('| Scenario | Corner | Engine: breakeven at 0.5 pt [95% CI] | at 1 pt | Inflation at a = 0 / 1 (pt) | Framework: breakeven at 0.5 pt [95% CI] | at 1 pt | Inflation at a = 0 / 1 (pt) |');
      console.log('|---|---|---|---|---|---|---|---|');
      envSel.forEach(function(e){ var c = ENV3[e], P = nextRoundPreset(c[1]);
        CORNERS.forEach(function(k){
          var cells = ['engine','framework'].map(function(cm){ var r = s3Config(P, {id:k.id, opts:k.opts, sw:{cm:cm, fw:cm === 'framework' ? k.fw : undefined}}, nP);
            return [fmtB(r.b[0]), fmtB(r.b[1]), pt(r.p0.m.endoAnn) + ' / ' + pt(r.p1.m.endoAnn)]; });
          console.log('| ' + c[0] + ' | ' + k.lbl + ' | ' + cells[0].join(' | ') + ' | ' + cells[1].join(' | ') + ' |');
        });
      });
      applyRule(svC);
    }

    if (secP === 'stab'){
      /* Plan A2: does raising BU in recessions produce endogenous inflation, and how much? Adverse Environment and Stress Test
       * (the reference environment has no recessions). Each arm vs no stabilizer, CRN-paired. Extra BU: BU issued (engine) or
       * the BU budget (framework), relative to no stabilizer, at a = 1. The year-after-recession rate pools the endogenous
       * year-on-year rate over years whose previous year was a recession (prices respond to last year's flows). */
      var svR = applyRule(NEXT_ROUND);
      console.log('\n=== Recession stabilizer under the price module (seeds 1-' + nP + ', ' + AG + ' agents; D1, D2, D6; reference settings) ===');
      console.log('| Scenario | Model | Arm | Extra BU (% of no stabilizer) | Inflation at a = 0 (pt/yr) | at a = 1 | Year after a recession, a = 0: rate (pt) | Difference vs none | Year after a recession, a = 1 | Difference vs none | Breakeven a at 0.5 pt [95% CI] | at 1 pt | Wealth / BLEI / basket poverty at a = 1 | Unmet need at a = 1 |');
      console.log('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');
      ['adv','st'].filter(function(e){ return envSel.indexOf(e) >= 0; }).forEach(function(e){ var c = ENV3[e], P0 = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){
          var ref = null;
          s3StabArms().forEach(function(arm){
            var P = Object.assign({}, P0, arm.preset), sv2 = s3Set({cm:cm}); LEDGER = newLedger();
            var p1 = s3Point(P, {}, 1, nP, true); var T = LEDGER.tot, iss = cm === 'engine' ? (T.buIssued || 0) : (T.fwBudget || 0); LEDGER = null; s3Reset(sv2);
            var r = s3Config(P0, {id:arm.id, preset:arm.preset, sw:{cm:cm}}, nP, {rec:true, pts:{'1.0000':p1}});
            var q = {iss:iss, post0:r.p0.rec.post/Math.max(1, r.p0.rec.postN), post1:r.p1.rec.post/Math.max(1, r.p1.rec.postN)};
            if (!ref) ref = q;
            console.log('| ' + c[0] + ' | ' + cm + ' | ' + arm.lbl + ' | ' + (arm.id === 'none' ? '—' : '+' + pc(q.iss/ref.iss - 1)) + ' | ' + pt(r.p0.m.endoAnn) + ' | ' + pt(r.p1.m.endoAnn) + ' | ' + pt(q.post0) + ' | ' + (arm.id === 'none' ? '—' : (q.post0 - ref.post0 >= 0 ? '+' : '') + pt(q.post0 - ref.post0)) + ' | ' + pt(q.post1) + ' | ' + (arm.id === 'none' ? '—' : (q.post1 - ref.post1 >= 0 ? '+' : '') + pt(q.post1 - ref.post1)) + ' | ' + fmtB(r.b[0]) + ' | ' + fmtB(r.b[1]) + ' | ' + r.p1.m.pov.toFixed(1) + '% / ' + r.p1.m.bleiPov.toFixed(1) + '% / ' + r.p1.m.basketPov.toFixed(1) + '% | ' + pc(r.p1.m.unmetShare) + ' |');
          });
        });
      });
      applyRule(svR);
    }
  }

  if (mode === 'labor') {
    /* Session 4 (A3): node harness.js labor [seeds] [head|sweep|all] [--agents=N]. head: CCO alone and Full Integration
     * against a UBI at matched gross cost, both conversion models, three environments, earnings response by channel.
     * sweep: one parameter at a time around the central values (LABOR_DEFAULTS), CCO alone, reference environment. */
    var LN = parseInt(process.argv[3], 10) || 500, LSEC = (process.argv[4] && process.argv[4].indexOf('--') !== 0) ? process.argv[4] : 'all', nA = FULL_INTEGRATION.nAgents;
    var ENVS = [['Reference', FULL_INTEGRATION], ['Adverse Environment', ADVERSE_REFERENCE], ['Stress Test', STRESS_TEST]];
    var ENVF = process.argv.filter(function(a){ return /^--env=/.test(a); })[0];  /* session 5: --env=ref,adv,st runs a subset */
    if (ENVF){ var envKeep = ENVF.split('=')[1].split(','), envKey = {ref:'Reference', adv:'Adverse Environment', st:'Stress Test'}; ENVS = ENVS.filter(function(E){ return envKeep.some(function(k){ return envKey[k] === E[0]; }); }); }
    function f0(x){ var v = Math.round(x); return v === 0 ? '0' : (v > 0 ? '+' : '') + v.toLocaleString('en-US'); }
    function pc(x){ return (x*100 >= 0 ? '+' : '') + (x*100).toFixed(2) + '%'; }
    function pv(r){ return r.pov.toFixed(1) + ' / ' + r.bleiPov.toFixed(1) + ' / ' + r.basketPov.toFixed(1); }
    function chan(r){ return 'raise ' + f0(r.raise) + ', BU ' + f0(-r.bu - r.buR) + ', cash ' + f0(-r.cash) + ', conv. rent ' + f0(-r.rent) + ', displaced ' + f0(-r.disp); }
    var svCM = CONVERSION_MODEL;
    console.log('=== A3 labor supply (session 4): seeds 1-' + LN + ', ' + nA + ' agents, D1 consumption rule, D6 COLA ===');
    console.log('Central: rho ' + LABOR_DEFAULTS.rho + ' (w32719, individual), rhoBU = rho (inframarginal BU act like cash), rhoR 0, eps ' + LABOR_DEFAULTS.eps + ' (Chetty 2012), raise exponent eps - rho, delta 0 (conversion as rent).');
    console.log('Earnings change = mean change in wage earnings per adult-year vs the same run with no labor response (hours x wage; wages per hour unchanged).');
    console.log('Poverty: wealth / BLEI / basket, % at year 20; "no response" is the same preset with LABOR off in effect (all coefficients 0).');
    if (LSEC === 'head' || LSEC === 'all') ['engine', 'framework'].forEach(function(cm){ CONVERSION_MODEL = cm;
      console.log('\n##### Conversion model: ' + cm + ' #####');
      ENVS.forEach(function(E){
        var P = Object.assign({}, E[1], {nAgents:nA}), C = ccoOnlyFor(P);
        var cz = laborStudy(C, LN, LAB_ZERO, true), cc = laborStudy(C, LN, LABOR_DEFAULTS), cd = laborStudy(C, LN, laborOpts({delta:1}));
        var U = Object.assign(ubiFor(P, cz.cost), {nAgents:nA}), uz = laborStudy(U, LN, LAB_ZERO), uc = laborStudy(U, LN, LABOR_DEFAULTS);
        var fz = laborStudy(P, LN, LAB_ZERO, true), fc = laborStudy(P, LN, LABOR_DEFAULTS), fd = laborStudy(P, LN, laborOpts({delta:1}));
        var B = Object.assign({}, baselineFor(P, true), {nAgents:nA}), bz = laborStudy(B, LN, LAB_ZERO);
        console.log('\n--- ' + E[0] + ' ---');
        console.log('  Gross cost per adult-year: CCO alone $' + Math.round(cz.cost).toLocaleString('en-US') + ' (BU spent on essentials $' + Math.round(cz.costU).toLocaleString('en-US') + ', conversion $' + Math.round(cz.costConv).toLocaleString('en-US') + '); Full Integration $' + Math.round(fz.cost).toLocaleString('en-US') + '. UBI matched to CCO alone: $' + Math.round(cz.cost).toLocaleString('en-US') + ' a year to every adult.');
        console.log('  Mean wage earnings with no response: CCO alone $' + Math.round(cz.E0).toLocaleString('en-US') + ', UBI $' + Math.round(uz.E0).toLocaleString('en-US') + ', Baseline $' + Math.round(bz.E0).toLocaleString('en-US'));
        [['CCO alone, delta 0 (rent)', cc, cz], ['CCO alone, delta 1 (dissipated)', cd, cz], ['UBI at matched cost', uc, uz], ['Full Integration, delta 0', fc, fz], ['Full Integration, delta 1', fd, fz]].forEach(function(row){
          console.log('  ' + (row[0] + '                                ').slice(0, 32) + ' earnings ' + pc(row[1].dE) + ', work time incl. projects ' + pc((row[1].E - row[1].E0 + row[1].disp)/Math.max(1, row[1].E0)) + ' ($' + f0(row[1].E - row[1].E0) + ': ' + chan(row[1]) + ')');
          console.log('  ' + '                                '.slice(0, 32) + ' poverty ' + pv(row[2]) + ' -> ' + pv(row[1]) + (row[1].zero > 0 ? '; earnings at zero in ' + (row[1].zero*100).toFixed(1) + '% of adult-years' : ''));
        });
        console.log('  Baseline (no program)            poverty ' + pv(bz));
        console.log('  CCO alone minus UBI, earnings: ' + ((cc.dE - uc.dE)*100 >= 0 ? '+' : '') + ((cc.dE - uc.dE)*100).toFixed(2) + ' points (delta 0), ' + ((cd.dE - uc.dE)*100 >= 0 ? '+' : '') + ((cd.dE - uc.dE)*100).toFixed(2) + ' points (delta 1)');
        var bd = cz.bound;
        var perPY = bd.expired/(cz.partShare*P.years*nA), rateBar = bd.convBU > 0 ? bd.conv/bd.convBU : 0;
        console.log('  Upper bound for a positive conversion channel: BU that expired unconverted, $' + Math.round(perPY).toLocaleString('en-US') + ' per participant-year (CCO alone), which at the mean net rate ' + rateBar.toFixed(2) + 'x could fund $' + Math.round(perPY*rateBar).toLocaleString('en-US') + ' of extra proceeds.');
      });
    });
    if (LSEC === 'sweep' || LSEC === 'all') ['engine', 'framework'].forEach(function(cm){ CONVERSION_MODEL = cm;
      var P = Object.assign({}, FULL_INTEGRATION, {nAgents:nA}), C = ccoOnlyFor(P), cz = laborStudy(C, LN, LAB_ZERO), Uc = Object.assign(ubiFor(P, cz.cost), {nAgents:nA});
      console.log('\n##### One-at-a-time sweep, reference environment, conversion model ' + cm + ' (CCO alone vs UBI at $' + Math.round(cz.cost).toLocaleString('en-US') + ') #####');
      var rows = [['central', {}], ['rho 0', {rho:0, rhoBU:0}], ['rho 0.10', {rho:0.10, rhoBU:0.10}], ['rho 0.28 (household)', {rho:0.28, rhoBU:0.28}], ['rho 0.30', {rho:0.30, rhoBU:0.30}],
        ['rhoBU 0.08 (mental accounting, half of rho)', {rhoBU:0.08}], ['UBI-equivalent toggle (every BU at rho, d2)', {rhoR:LABOR_DEFAULTS.rho}],
        ['eps 0', {eps:0}], ['eps 0.25 (extensive)', {eps:0.25}], ['eps 0.5 (placeholder high)', {eps:0.5}], ['raise channel off (eps = rho)', {eps:LABOR_DEFAULTS.rho}],
        ['delta 0.5', {delta:0.5}], ['delta 1', {delta:1}], ['octave wage bonus off (PATHWAY_OFF)', {}, null, {octaveWage:true}]];
      if (cm === 'framework') rows.push(['business rate 2x', {}, {bizRate:2}], ['business rate 4x', {}, {bizRate:4}]);
      rows.forEach(function(r){ var sv = Object.assign({}, FW), svP = Object.assign({}, PATHWAY_OFF); if (r[2]) Object.assign(FW, r[2]); if (r[3]) Object.assign(PATHWAY_OFF, r[3]);
        try { var L = laborOpts(r[1]), c = laborStudy(C, LN, L), u = laborStudy(Uc, LN, L), cz2 = (r[2] || r[3]) ? laborStudy(C, LN, LAB_ZERO) : cz;
          console.log('  ' + (r[0] + '                                              ').slice(0, 46) + ' CCO ' + pc(c.dE) + ' (work ' + pc((c.E - c.E0 + c.disp)/Math.max(1, c.E0)) + ')  UBI ' + pc(u.dE) + '  diff ' + ((c.dE - u.dE)*100).toFixed(2) + ' pt | CCO poverty ' + pv(cz2) + ' -> ' + pv(c) + (r[2] || r[3] ? ' (CCO cost here $' + Math.round(cz2.cost).toLocaleString('en-US') + '; UBI kept at the reference cost; mean earnings with no response $' + Math.round(cz2.E0).toLocaleString('en-US') + ' vs $' + Math.round(cz.E0).toLocaleString('en-US') + ')' : ''));
        } finally { Object.assign(FW, sv); Object.assign(PATHWAY_OFF, svP); } });
    });
    CONVERSION_MODEL = svCM;
  }

  if (mode === 'restudy') {
    /* Session 5 (dashboard s17): node harness.js restudy <seeds> <section> [fi,adv,st] [--agents=N]. Every section: D1 rule, D2
     * lines, D6 COLA, CRN-paired seeds 1-N. Sections:
     *  lam    lamG 0.25 and 1.41 against the reference 1: breakeven at 0.5 pt and the price-neutral point (Full Integration).
     *  grid   S5_ROWS x scenarios x both conversion models: breakeven at 0.5 pt, the price-neutral point (d18), inflation at
     *         a = 0 and 1, and poverty with no price feedback, at the breakeven and at a = 1; earnings change for joint rows.
     *  labor  prices off: CCO alone against a UBI at matched gross cost, and Full Integration, under each restudy switch. */
    CFG.WEALTH_FLOOR = -10000;
    var nR = parseInt(process.argv[3] || '500', 10), secR = process.argv[4] || 'grid', envR = (process.argv[5] || 'fi,adv,st').split(',');
    var ENV5 = {fi:['Full Integration', FULL_INTEGRATION], adv:['Adverse Environment', ADVERSE_REFERENCE], st:['Stress Test', STRESS_TEST]};
    function b5(b){ return b.be === null ? 'none' : b.be === 0 ? '0 (any a)' : b.be.toFixed(3) + ' [' + b.ci[0].toFixed(3) + '–' + b.ci[1].toFixed(3) + ']'; }
    function n5(n){ return n.an === null ? 'none up to ' + n.aMax : n.an.toFixed(3) + ' [' + n.ci[0].toFixed(3) + '–' + n.ci[1].toFixed(3) + ']'; }
    function p5(x){ return isFinite(x) && Math.abs(x) < 10 ? (x*100).toFixed(2) : 'diverges'; }
    function v5(q){ return q.m.pov.toFixed(1) + ' / ' + q.m.bleiPov.toFixed(1) + ' / ' + q.m.basketPov.toFixed(1); }
    var t0R = Date.now(), svR = applyRule(NEXT_ROUND);
    if (secR === 'lam'){
      console.log('=== Restudy: lamG and the price-neutral point (Full Integration, seeds 1-' + nR + ', ' + AG + ' agents) ===');
      console.log('| Model | lamG | Breakeven a at 0.5 pt [95% CI] | Price-neutral a [95% CI] | Inflation at a = 0 / 1 (pt/yr) | Points |'); console.log('|---|---|---|---|---|---|');
      ['engine','framework'].forEach(function(cm){ [0.25, 1, 1.41].forEach(function(lam){
        var r = s5Config(nextRoundPreset(FULL_INTEGRATION), {id:'lam', sw:{cm:cm}, opts:{lamG:lam}}, nR);
        console.log('| ' + cm + ' | ' + lam + ' | ' + b5(r.b[0]) + ' | ' + n5(r.n) + ' | ' + p5(r.p0.m.endoAnn) + ' / ' + p5(r.p1.m.endoAnn) + ' | ' + r.nEval + ' |'); }); });
    }
    if (secR === 'grid'){
      var rowSel = process.argv[6] ? process.argv[6].split(',') : null;
      console.log('=== Restudy grid (seeds 1-' + nR + ', ' + AG + ' agents; D1, D2, D6; reference settings, lamG 1; tolerance 0.5 pt, D3) ===');
      console.log('| Scenario | Model | Row | Breakeven a at 0.5 pt [95% CI] | Price-neutral a (d18) [95% CI] | Inflation at a = 0 / 1 (pt/yr) | Poverty, no price feedback (wealth / BLEI / basket %) | At the breakeven | At a = 1 | Earnings change at a = 1 | Points |');
      console.log('|---|---|---|---|---|---|---|---|---|---|---|');
      envR.forEach(function(e){ var c = ENV5[e], P = nextRoundPreset(c[1]);
        ['engine','framework'].forEach(function(cm){
          S5_ROWS.filter(function(row){ return !rowSel || rowSel.indexOf(row.id) >= 0; }).forEach(function(row){
            var rr = Object.assign({}, row, {sw:{cm:cm}}), r = s5Config(P, rr, nR);
            console.log('| ' + c[0] + ' | ' + cm + ' | ' + row.lbl + ' | ' + b5(r.b[0]) + ' | ' + n5(r.n) + ' | ' + p5(r.p0.m.endoAnn) + ' / ' + p5(r.p1.m.endoAnn) + ' | ' + v5(r.pNF) + ' | ' + (r.pBE ? v5(r.pBE) : '—') + ' | ' + v5(r.p1) + ' | ' + (row.opts && row.opts.labor ? (r.p1.m.dE*100).toFixed(2) + '%' : '—') + ' | ' + r.nEval + ' |');
          });
        });
      });
    }
    if (secR === 'labor'){
      console.log('=== Restudy, labor (prices off; seeds 1-' + nR + ', ' + AG + ' agents; reference environment; central rho 0.16, eps 0.33, delta 0) ===');
      console.log('Earnings change vs the same preset with no labor response. The UBI is matched to CCO alone\'s gross cost under each row.');
      console.log('| Model | Row | CCO alone: earnings | UBI at matched cost: earnings | CCO minus UBI (pt) | CCO alone gross cost / adult-yr | CCO alone poverty, response on (wealth / BLEI / basket) | UBI poverty | Full Integration: earnings | Full Integration poverty |');
      console.log('|---|---|---|---|---|---|---|---|---|---|');
      var LR = [{id:'central', lbl:'Central (shipped engine)'}, {id:'oct', lbl:'Octave wage bonus off (d19)', pw:{octaveWage:true}},
        {id:'tax', lbl:'Discounts skip the tax share (d5)', rs:{DISC_BASE:'pretax'}}, {id:'taxoct', lbl:'d5 and d19 together', rs:{DISC_BASE:'pretax'}, pw:{octaveWage:true}},
        {id:'theta', lbl:'Theta on realised PTF density (C08)', rs:{THETA_GATE:'density'}, fiOnly:true}, {id:'pth', lbl:'PTH housing only (d4)', rs:{PTH_MODE:'housing'}, fiOnly:true},
        {id:'r7', lbl:'C08 + d4 + d5 together', rs:{THETA_GATE:'density', PTH_MODE:'housing', DISC_BASE:'pretax'}, fiOnly:true}];
      function pv5(r){ return r.pov.toFixed(1) + ' / ' + r.bleiPov.toFixed(1) + ' / ' + r.basketPov.toFixed(1); }
      function pp(x){ return (x*100 >= 0 ? '+' : '') + (x*100).toFixed(2) + '%'; }
      ['engine','framework'].forEach(function(cm){ CONVERSION_MODEL = cm;
        LR.forEach(function(row){ var sv = s5Set(row);
          try {
            var P = FULL_INTEGRATION, fc = laborStudy(P, nR, LABOR_DEFAULTS), cell = ['—', '—', '—', '—', '—', '—'];
            if (!row.fiOnly){ var C = ccoOnlyFor(P), cz = laborStudy(C, nR, LAB_ZERO), cc = laborStudy(C, nR, LABOR_DEFAULTS), U = ubiFor(P, cz.cost), uc = laborStudy(U, nR, LABOR_DEFAULTS);
              cell = [pp(cc.dE), pp(uc.dE), ((cc.dE - uc.dE)*100).toFixed(2), '$' + Math.round(cz.cost).toLocaleString('en-US'), pv5(cc), pv5(uc)]; }
            console.log('| ' + cm + ' | ' + row.lbl + ' | ' + cell.join(' | ') + ' | ' + pp(fc.dE) + ' | ' + pv5(fc) + ' |');
          } finally { s5Reset(sv); } });
      });
      CONVERSION_MODEL = 'engine';
    }
    applyRule(svR);
    console.log('\n(' + ((Date.now() - t0R)/60000).toFixed(1) + ' min)');
  }

  if (mode === 'testbed') {
    /* Session 6 (A4; dashboard s11): node harness.js testbed <seeds> <section> [ref,adv,st] [--agents=N] [--pilot=N] [--models=engine,framework].
     * Every section: the NR6 profile (D1 rule; d22 corrections; d23 wage indexation), labor at central values, lines deflated (D2),
     * CRN-paired seeds 1-N, one cost ledger and one financing rule for every design (d24-d26).
     *  match     each Compassionism preset against UBI, NIT and asset endowment matched to its gross cost per adult-year, plus X-Cents
     *            and public grocery at their own cost; tax-financed and money-created (aT = 0; Compassionism also at a = 1); group check.
     *  frontier  cost against basket FGT2 per design family, tax-financed (and money-created with --fin=money).
     *  esp       (session 19, s38) ESP payroll in the Hub-spec model: today's main row against ESP payroll at the defaults, its
     *            sensitivities (d71-d75), the page's other rows with it, and hybrid financing at a = 0 and 1. Framework model only. */
    CFG.WEALTH_FLOOR = -10000;
    var nT = parseInt(process.argv[3] || '500', 10), secT = process.argv[4] || 'match';
    var envT = (process.argv[5] && process.argv[5].indexOf('--') !== 0 ? process.argv[5] : 'ref').split(',');
    var PILOT = (process.argv.filter(function(a){ return /^--pilot=\d+$/.test(a); })[0] || '--pilot=60').split('=')[1] | 0;
    var MODELS = (process.argv.filter(function(a){ return /^--models=/.test(a); })[0] || '--models=engine,framework').split('=')[1].split(',');
    var FINS = (process.argv.filter(function(a){ return /^--fin=/.test(a); })[0] || (secT === 'frontier' ? '--fin=tax' : '--fin=tax,money')).split('=')[1].split(',');
    var XT = +((process.argv.filter(function(a){ return /^--X=\d+$/.test(a); })[0] || '--X=0').split('=')[1]);  /* d26: contribution threshold, year-0 dollars */
    var ENVT = {ref:['Reference (Full Integration settings)', FULL_INTEGRATION], adv:['Adverse Environment', ADVERSE_REFERENCE], st:['Stress Test', STRESS_TEST]};
    var MLBL = {engine:'Compassionism: shipped (engine model)', framework:'Compassionism: hub spec (framework model)'};
    var t0T = Date.now(), svT = applyNR6(), svG = tbSetG(TB_PROFILE_G);  /* session 10 (d40): N7_BLEI on in the testbed profile */
    function $(x){ return (x < 0 ? '-$' : '$') + Math.round(Math.abs(x)).toLocaleString('en-US'); }
    function f1(x){ return x.toFixed(1); } function f2(x){ return x.toFixed(2); }
    function pinf(x){ return isFinite(x) && Math.abs(x) < 10 ? (x*100).toFixed(2) : 'diverges'; }
    function sg(x, d){ return (x >= 0 ? '+' : '') + x.toFixed(d === undefined ? 2 : d); }
    function grpCell(r, b){  /* resources change % and person-year FGT0 change (pt) vs the Baseline, per group */
      var q = [['part', r.gPartRes, b.gPartRes, r.gPartF0, b.gPartF0, r.gPartW, b.gPartW], ['non', r.gNonRes, b.gNonRes, r.gNonF0, b.gNonF0, r.gNonW, b.gNonW],
        ['PTH', r.gPthRes, b.gPthRes, r.gPthF0, b.gPthF0, r.gPthW, b.gPthW], ['low', r.gLowRes, b.gLowRes, r.gLowF0, b.gLowF0, r.gLowW, b.gLowW],
        ['top', r.gTopRes, b.gTopRes, r.gTopF0, b.gTopF0, r.gTopW, b.gTopW]], worse = [];
      /* worse off: resources down more than 0.5%, or person-year basket FGT0 or year-20 wealth poverty up more than 0.5 point */
      var txt = q.map(function(g){ var dr = (g[1]/g[2] - 1)*100, df = g[3] - g[4], dw = g[5] - g[6], why = [];
        if (dr < -0.5) why.push('r'); if (df > 0.5) why.push('i'); if (dw > 0.5) why.push('w'); if (why.length) worse.push(g[0] + ' (' + why.join('') + ')');
        return sg(dr, 1) + '% / ' + sg(df, 1) + ' / ' + sg(dw, 1); }).join('; ');
      return txt + ' | ' + (worse.length ? worse.join(', ') : 'none'); }
    console.log('=== A4 testbed (session 6): seeds 1-' + nT + ', ' + AG + ' agents; NR6 profile (D1; d22: theta on PTF density, PTH housing only, discounts skip the tax share; d23: wages indexed to P_G); labor at central values (rho 0.16, eps 0.33, delta 0); d40: N7_BLEI on (BLEI raise attributed to the design where its support carries the adult over the gate); lines deflated (D2); lamG 1 ===');
    console.log('Gross cost: every program dollar at face value per adult-year, year-0 dollars (cash, BU spent at face value, conversion net of tax, PTF/PTH/grocery price-cut dollars, capital, PTH liquid appreciation). Basket FGT: income incl. transfers, less the contribution, plus an endowment\'s annuity value, against own cost; x100.');
    if (secT === 'match') envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P);
      MODELS.forEach(function(cm){ CONVERSION_MODEL = cm;
        FINS.forEach(function(fin){
          var o = {fin:fin, aT:0, a:0, X:XT}, tgt = tbStudy([{p:PR.cco()}], PILOT, P, o)[0].cost;
          var mU = tbMatch('ubi', tgt, P, PILOT, o), mN = tbMatch('nit', tgt, P, PILOT, o), mE = tbMatch('endow', tgt, P, PILOT, o);
          var rows = [['Baseline (no program)', PR.baseline()], [MLBL[cm] + (fin === 'money' ? ', a = 0' : ''), PR.cco()]];
          rows.push([MLBL[cm] + (fin === 'money' ? ', a = 0' : '') + ', octave wage bonus off (d19)', PR.cco(), null, {octaveWage:true}]);
          if (P.inflRate > 0) rows.push([MLBL[cm] + (fin === 'money' ? ', a = 0' : '') + ', PTF/PTH inflation damping off (d33)', PR.cco(), {noDamp:true}],
            [MLBL[cm] + (fin === 'money' ? ', a = 0' : '') + ', octave raise and damping off (d19 + d33)', PR.cco(), {noDamp:true}, {octaveWage:true}]);  /* session 8 (s24) */
          if (fin === 'money') rows.push([MLBL[cm] + ', a = 1 (H1: every reward dollar matched by output)', PR.cco(), {a:1}]);
          rows.push(['UBI ' + $(mU) + '/yr', PR.ubi(mU)], ['NIT: G ' + $(mN) + ', t ' + TB_NIT_T, PR.nit(mN)], ['Asset endowment ' + $(mE) + ' (wealth < $25,000)', PR.endow(mE)],
            ['X-Cents, flat ($3,614/yr)', PR.xc(0)], ['X-Cents, community-work variant (delta 1)', PR.xc(1)], ['Public grocery, full coverage (15% off food)', PR.groc(1)]);
          var R = tbStudy(rows.map(function(r){ return {p:r[1], o:r[2] || undefined, pw:r[3]}; }), nT, P, o), B = R[0];
          console.log('\n--- ' + E[0] + ' | ' + MLBL[cm] + ' | ' + (fin === 'tax' ? 'tax-financed' + (XT ? ', contribution on wages above ' + $(XT) : '') : 'money-created, aT = 0') + ' | target ' + $(tgt) + '/adult-yr (pilot ' + PILOT + ' seeds) ---');
          console.log('| Design | Gross cost | Cash / BU / conv / cuts / PTH | Contribution rate (mean) | Treasury | Endogenous inflation (pt/yr) | Earnings | Wealth pov % | Basket FGT0 / FGT1 / FGT2 (yr 20) | FGT0 / FGT2, person-years | FGT2 vs Baseline [95% CI] | PY FGT2 vs Baseline [95% CI] | Groups vs Baseline: resources % / PY FGT0 pt / wealth pov pt (participants; non-participants; PTH; bottom third by year-0 wage; top third) | Worse off (r resources, i income poverty, w wealth poverty) |');
          console.log('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');
          R.forEach(function(r, i){ var dF = tbDiff(R[i], B, 'fgt2'), dP = tbDiff(R[i], B, 'fgt2PY');
            console.log('| ' + rows[i][0] + ' | ' + $(r.cost) + ' | ' + [r.cCash + r.cEndow, r.cBU, r.cConv, r.cCut + r.cCap, r.cPth].map($).join(' / ') + ' | ' + (fin === 'tax' ? (r.tauMean*100).toFixed(1) + '%' : '—') + ' | ' + (fin === 'tax' ? $(r.treas) : '—') +
              ' | ' + pinf(r.endoAnn) + ' | ' + sg(r.dE*100) + '% | ' + f1(r.pov) + ' | ' + f1(r.fgt0) + ' / ' + f2(r.fgt1) + ' / ' + f2(r.fgt2) + ' | ' + f1(r.fgt0PY) + ' / ' + f2(r.fgt2PY) +
              ' | ' + (i ? sg(dF.m) + ' [' + sg(dF.lo) + ', ' + sg(dF.hi) + ']' : '—') + ' | ' + (i ? sg(dP.m) + ' [' + sg(dP.lo) + ', ' + sg(dP.hi) + ']' : '—') + ' | ' + (i ? grpCell(r, B) : '— | —') + ' |'); });
          if (!(P.inflRate > 0)) console.log(D33_NOTE);
        });
      });
      CONVERSION_MODEL = 'engine';
    });
    if (secT === 'frontier') envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P);
      FINS.forEach(function(fin){ var o = {fin:fin, aT:0, a:0, X:XT}, cf = [];
        cf.push({f:'Baseline', l:'no program', p:PR.baseline()});
        [2000, 4000, 6000, 8000, 12000, 16000, 24000].forEach(function(x){ cf.push({f:'UBI', l:$(x), p:PR.ubi(x)}); });
        [5000, 10000, 15000, 20000, 30000].forEach(function(x){ cf.push({f:'NIT t 0.5', l:'G ' + $(x), p:PR.nit(x)}); });
        [10000, 20000].forEach(function(x){ [0.3, 0.7].forEach(function(tt){ cf.push({f:'NIT t ' + tt, l:'G ' + $(x), p:PR.nit(x, tt)}); }); });
        [25000, 50000, 100000, 200000, 400000].forEach(function(x){ cf.push({f:'Asset endowment', l:$(x), p:PR.endow(x)}); });
        [0.25, 0.5, 1].forEach(function(x){ cf.push({f:'Public grocery', l:'cover ' + (x*100) + '%', p:PR.groc(x)}); });
        cf.push({f:'Public grocery', l:'cover 100%, capital $0', p:PR.groc(1, 0)}, {f:'Public grocery', l:'cover 100%, capital $700', p:PR.groc(1, 700)});
        [0, 1].forEach(function(dl){ cf.push({f:'X-Cents', l:dl ? 'community-work variant (delta 1)' : 'flat', p:PR.xc(dl)}); });
        MODELS.forEach(function(cm){ (cm === 'engine' ? [600, 900, 1200, 1800] : [300, 600, 900, 1200]).forEach(function(bu){ cf.push({f:MLBL[cm], l:'BU ' + $(bu) + '/mo', p:PR.cco(bu), cm:cm}); });
          cf.push({f:MLBL[cm] + ', octave wage bonus off (d19)', l:'BU $1,200/mo', p:PR.cco(1200), cm:cm, pw:{octaveWage:true}});
          cf.push({f:MLBL[cm] + ', CCO alone', l:'BU $1,200/mo', p:PR.ccoAlone(1200), cm:cm});
          if (P.inflRate > 0) cf.push({f:MLBL[cm] + ', PTF/PTH inflation damping off (d33)', l:'BU $1,200/mo', p:PR.cco(1200), cm:cm, o:{noDamp:true}},
            {f:MLBL[cm] + ', octave raise and damping off (d19 + d33)', l:'BU $1,200/mo', p:PR.cco(1200), cm:cm, o:{noDamp:true}, pw:{octaveWage:true}}); });  /* session 8 (s24) */
        if (fin === 'money') MODELS.forEach(function(cm){ cf.push({f:MLBL[cm] + ', a = 1', l:'BU $1,200/mo', p:PR.cco(1200), cm:cm, o:{a:1}}); });
        var R = tbStudy(cf, nT, P, o), B = R[0];
        console.log('\n--- Frontier: ' + E[0] + ' | ' + (fin === 'tax' ? 'tax-financed' + (XT ? ', contribution on wages above ' + $(XT) : '') : 'money-created, aT = 0') + ' ---');
        console.log('| Family | Setting | Gross cost / adult-yr | Contribution rate | Endogenous inflation (pt/yr) | Earnings | Wealth pov % | Basket FGT0 / FGT2 (yr 20) | FGT2 person-years | FGT2 cut per $1,000 of cost: yr 20 / person-years | Groups vs Baseline |');
        console.log('|---|---|---|---|---|---|---|---|---|---|---|');
        R.forEach(function(r, i){ var per = r.cost > 1 ? (B.fgt2 - r.fgt2)/(r.cost/1000) : 0, perP = r.cost > 1 ? (B.fgt2PY - r.fgt2PY)/(r.cost/1000) : 0;
          console.log('| ' + cf[i].f + ' | ' + cf[i].l + ' | ' + $(r.cost) + ' | ' + (fin === 'tax' ? (r.tauMean*100).toFixed(1) + '%' : '—') + ' | ' + pinf(r.endoAnn) + ' | ' + sg(r.dE*100) + '% | ' + f1(r.pov) + ' | ' + f1(r.fgt0) + ' / ' + f2(r.fgt2) + ' | ' + f2(r.fgt2PY) + ' | ' + (i ? f2(per) + ' / ' + f2(perP) : '—') + ' | ' + (i ? grpCell(r, B).split(' | ')[1] : '—') + ' |'); });
        if (!(P.inflRate > 0)) console.log(D33_NOTE);
      });
    });
    /* Session 7 (dashboard s23): decompose Compassionism's per-dollar edge, tax-financed, BU $1,200. One channel off per arm, CRN-paired;
     * the BLEI-raise arms are paired with a Baseline whose BLEI raise is also off (the Baseline has that raise too). The i3 arms fix
     * FBS counting BU twice (FBS_BU_ONCE) and the PTH appreciation double-count (PTH_APPR_CONSERVE). */
    if (secT === 'decomp') envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P), o = {fin:'tax', aT:0, a:0, X:XT};
      var rows = [{l:'Baseline (no program)', p:PR.baseline(), b:0}, {l:'Baseline, BLEI raise off', p:PR.baseline(), pw:{bleiWage:true}, b:1}];
      MODELS.forEach(function(cm){ var q = PR.cco(), tag = cm === 'engine' ? 'engine' : 'framework';
        var arms = [['full design', {}], [cm === 'engine' ? 'CCO relief off' : 'BU purchases off (so no BU reaches producers or projects)', {pw:{relief:true}}], ['conversion off', {pw:{conversion:true}}], ['PTF off (cut, conversion bonus, damping)', {p:Object.assign({}, q, {ptf:false})}],
          ['PTF/PTH inflation damping off', {o:{noDamp:true}}], ['PTH cost cut off (and equity)', {pw:{pthCost:true}}], ['PTH equity routing and appreciation off', {pw:{pthEquity:true}}],
          ['octave advancement off', {pw:{octave:true}}], ['octave wage raise off (d19)', {pw:{octaveWage:true}}], ['BLEI raise off (both runs)', {pw:{bleiWage:true}, b:1}],
          ['all program raises off (both runs)', {pw:{octaveWage:true, bleiWage:true}, b:1}], ['i3-1: FBS counts BU once', {g:{FBS_BU_ONCE:true}}],
          ['i3-3: PTH appreciation conserved', {g:{PTH_APPR_CONSERVE:true}}], ['i3-1 + i3-3 + damping off', {g:{FBS_BU_ONCE:true, PTH_APPR_CONSERVE:true}, o:{noDamp:true}}],
          ['i3-1 + i3-3 + damping off + octave raise off', {g:{FBS_BU_ONCE:true, PTH_APPR_CONSERVE:true}, o:{noDamp:true}, pw:{octaveWage:true}}]];
        arms.forEach(function(A){ rows.push({l:tag + ': ' + A[0], p:A[1].p || q, pw:A[1].pw, g:A[1].g, o:A[1].o, cm:cm, b:A[1].b || 0, full:A[0] === 'full design'}); });
        CONVERSION_MODEL = cm; var tgt = tbStudy([{p:q}], PILOT, P, o)[0].cost, mU = tbMatch('ubi', tgt, P, PILOT, o); CONVERSION_MODEL = 'engine';
        rows.push({l:tag + ': matched UBI ' + $(mU) + '/yr', p:PR.ubi(mU), b:0});
      });
      var R = tbStudy(rows.map(function(r){ return {p:r.p, o:r.o, pw:r.pw, g:r.g, cm:r.cm}; }), nT, P, o), full = {};
      rows.forEach(function(r, i){ if (r.full) full[r.cm] = i; });
      console.log('\n--- Decomposition: ' + E[0] + ' | tax-financed | seeds 1-' + nT + ' ---');
      console.log('| Arm | Gross cost | BU relief / conversion / price cuts / PTH liq | Contribution | Earnings | Targeting share | Wealth pov % | FGT2 (yr 20) | FGT2 vs own Baseline [95% CI] | Cut per $1,000 | Cut lost vs full design (pt) | FGT2 person-years | PY FGT2 vs own Baseline [95% CI] | PY cut per $1,000 | PY cut lost (pt) | Worse off |');
      console.log('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');
      R.forEach(function(r, i){ var row = rows[i], B = R[row.b], d = i > 1 ? tbDiff(R[i], B, 'fgt2') : null, per = d && r.cost > 1 ? -d.m/(r.cost/1000) : 0;
        var dp = i > 1 ? tbDiff(R[i], B, 'fgt2PY') : null, perP = dp && r.cost > 1 ? -dp.m/(r.cost/1000) : 0;  /* session 8 (s18): person-year FGT2 beside year 20 */
        var fi = row.cm ? full[row.cm] : null, lost = (fi !== null && fi !== undefined && i !== fi) ? (-tbDiff(R[fi], R[rows[fi].b], 'fgt2').m) - (-d.m) : null;
        var lostP = (fi !== null && fi !== undefined && i !== fi) ? (-tbDiff(R[fi], R[rows[fi].b], 'fgt2PY').m) - (-dp.m) : null;
        console.log('| ' + row.l + ' | ' + $(r.cost) + ' | ' + [r.cBU, r.cConv, r.cCut, r.cPth].map($).join(' / ') + ' | ' + (r.tauMean*100).toFixed(1) + '% | ' + sg(r.dE*100) + '% | ' + (r.tgt*100).toFixed(1) + '% | ' + f1(r.pov) +
          ' | ' + f2(r.fgt2) + ' | ' + (d ? sg(d.m) + ' [' + sg(d.lo) + ', ' + sg(d.hi) + ']' : '—') + ' | ' + (d ? f2(per) : '—') + ' | ' + (lost === null ? '—' : sg(lost)) +
          ' | ' + f2(r.fgt2PY) + ' | ' + (dp ? sg(dp.m) + ' [' + sg(dp.lo) + ', ' + sg(dp.hi) + ']' : '—') + ' | ' + (dp ? f2(perP) : '—') + ' | ' + (lostP === null ? '—' : sg(lostP)) + ' | ' + (i > 1 ? grpCell(r, B).split(' | ')[1] : '—') + ' |'); });
    });
    /* Session 7: Duke's d24-d29 follow-ups, reference environment, side by side (CRN-paired within each model):
     *  d24 money-mode rules (a) default, (b) a also on a converted BU's face value, (c) the session 2-5 rule ('none': BU and cuts outside
     *  money creation); d25 in-kind income effect off; d26 hybrid financing; d28 the shipped BLEI gate, and BLEI poverty on both
     *  definitions; d29 group losses in dollars. */
    if (secT === 'alts') envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P);
      MODELS.forEach(function(cm){ CONVERSION_MODEL = cm;
        var oT = {fin:'tax', aT:0, a:0, X:XT}, oM = {fin:'money', aT:0, a:0, X:XT};
        var tgtT = tbStudy([{p:PR.cco()}], PILOT, P, oT)[0].cost, tgtM = tbStudy([{p:PR.cco()}], PILOT, P, oM)[0].cost;
        var uT = tbMatch('ubi', tgtT, P, PILOT, oT), nT_ = tbMatch('nit', tgtT, P, PILOT, oT), uM = tbMatch('ubi', tgtM, P, PILOT, oM), nM = tbMatch('nit', tgtM, P, PILOT, oM);
        var C = MLBL[cm], rows = [
          ['Baseline (no program)', PR.baseline(), oT, null, 'tax'],
          [C + ' [default: neutral gate, in-kind rho]', PR.cco(), oT, null, 'tax'],
          [C + ', octave wage raise off (d19)', PR.cco(), oT, {octaveWage:true}, 'tax'],
          ['UBI ' + $(uT) + '/yr', PR.ubi(uT), oT, null, 'tax'], ['NIT: G ' + $(nT_) + ', t 0.5', PR.nit(nT_), oT, null, 'tax'],
          ['Public grocery, full cover', PR.groc(1), oT, null, 'tax'],
          [C + ', d28 shipped BLEI gate', PR.cco(), Object.assign({}, oT, {neutralGate:false}), null, 'd28'],
          [C + ', d28 shipped gate, octave raise off', PR.cco(), Object.assign({}, oT, {neutralGate:false}), {octaveWage:true}, 'd28'],
          ['UBI ' + $(uT) + '/yr, d28 shipped gate', PR.ubi(uT), Object.assign({}, oT, {neutralGate:false}), null, 'd28'],
          ['NIT: G ' + $(nT_) + ', d28 shipped gate', PR.nit(nT_), Object.assign({}, oT, {neutralGate:false}), null, 'd28'],
          [C + ', d25 rho on cash and BU only', PR.cco(), Object.assign({}, oT, {inkindRho:false}), null, 'd25'],
          ['Public grocery, full cover, d25 rho on cash and BU only', PR.groc(1), Object.assign({}, oT, {inkindRho:false}), null, 'd25'],
          [C + ', d26 hybrid, a = 0', PR.cco(), Object.assign({}, oT, {fin:'hybrid', a:0}), null, 'd26'],
          [C + ', d26 hybrid, a = 1', PR.cco(), Object.assign({}, oT, {fin:'hybrid', a:1}), null, 'd26'],
          [C + ', d24 (a) default, a = 0', PR.cco(), oM, null, 'money'],
          [C + ', d24 (a) default, a = 1', PR.cco(), Object.assign({}, oM, {a:1}), null, 'money'],
          [C + ', d24 (b) a on face value too, a = 1', PR.cco(), Object.assign({}, oM, {a:1, buAtA:true}), null, 'money'],
          [C + ', d24 (c) session 2-5 rule, a = 0', PR.cco(), Object.assign({}, oM, {fin:'none', a:0}), null, 'money'],
          [C + ', d24 (c) session 2-5 rule, a = 1', PR.cco(), Object.assign({}, oM, {fin:'none', a:1}), null, 'money'],
          ['UBI ' + $(uM) + '/yr, money', PR.ubi(uM), oM, null, 'money'], ['NIT: G ' + $(nM) + ', t 0.5, money', PR.nit(nM), oM, null, 'money']];
        if (P.inflRate > 0) rows.push([C + ', PTF/PTH inflation damping off (d33)', PR.cco(), Object.assign({}, oT, {noDamp:true}), null, 'd33'],
          [C + ', octave raise and damping off (d19 + d33)', PR.cco(), Object.assign({}, oT, {noDamp:true}), {octaveWage:true}, 'd33']);  /* session 8 (s24) */
        var R = tbStudy(rows.map(function(r){ return {p:r[1], o:r[2], pw:r[3] || undefined}; }), nT, P, {}), B = R[0];
        console.log('\n--- Follow-ups d24-d29: ' + E[0] + ' | ' + C + ' | seeds 1-' + nT + ' | tax target ' + $(tgtT) + ', money target ' + $(tgtM) + ' ---');
        console.log('| Design | Set | Gross cost | Contribution (mean) | Treasury | Inflation (pt/yr) | Earnings | Wealth pov % | BLEI pov %, shipped def. | BLEI pov %, design-neutral | Targeting share | FGT0 / FGT2 (yr 20) | FGT2 vs Baseline [95% CI] | Cut per $1,000 | PY FGT2 vs Baseline [95% CI] | Worse off |');
        console.log('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|');
        R.forEach(function(r, i){ var d = i ? tbDiff(R[i], B, 'fgt2') : null, dp = i ? tbDiff(R[i], B, 'fgt2PY') : null, fin = rows[i][2].fin, tx = fin === 'tax' || fin === 'hybrid';
          console.log('| ' + rows[i][0] + ' | ' + rows[i][4] + ' | ' + $(r.cost) + ' | ' + (tx ? (r.tauMean*100).toFixed(1) + '%' : '—') + ' | ' + (tx ? $(r.treas) : '—') + ' | ' + pinf(r.endoAnn) + ' | ' + sg(r.dE*100) + '% | ' + f1(r.pov) +
            ' | ' + f1(r.bleiPov) + ' | ' + f1(r.nbleiPov) + ' | ' + (r.tgt*100).toFixed(1) + '% | ' + f1(r.fgt0) + ' / ' + f2(r.fgt2) + ' | ' + (d ? sg(d.m) + ' [' + sg(d.lo) + ', ' + sg(d.hi) + ']' : '—') +
            ' | ' + (d && r.cost > 1 ? f2(-d.m/(r.cost/1000)) : '—') + ' | ' + (dp ? sg(dp.m) + ' [' + sg(dp.lo) + ', ' + sg(dp.hi) + ']' : '—') + ' | ' + (i ? grpCell(r, B).split(' | ')[1] : '—') + ' |'); });
        if (!(P.inflRate > 0)) console.log(D33_NOTE);
        /* d29: how much worse off, in real dollars per adult-year and poverty points, per group (tax default rows) */
        console.log('\n  d29 group detail (tax-financed defaults; change vs Baseline: real resources $/adult-yr (%), person-year basket FGT0 pt, year-20 wealth poverty pt):');
        console.log('| Group | Baseline resources $/yr | ' + [1, 3, 4, 5].map(function(i){ return rows[i][0]; }).join(' | ') + ' |');
        console.log('|---|---|' + [1, 3, 4, 5].map(function(){ return '---|'; }).join(''));
        [['participants', 'gPart'], ['non-participants', 'gNon'], ['PTH members', 'gPth'], ['bottom third by year-0 wage', 'gLow'], ['top third by year-0 wage', 'gTop']].forEach(function(g){
          var b = B[g[1] + 'Res'];
          console.log('| ' + g[0] + ' | ' + $(b) + ' | ' + [1, 3, 4, 5].map(function(i){ var r = R[i], dr = r[g[1] + 'Res'] - b;
            return (dr >= 0 ? '+' : '-') + $(Math.abs(dr)).replace('$', '$') + ' (' + sg((r[g[1] + 'Res']/b - 1)*100, 1) + '%), ' + sg(r[g[1] + 'F0'] - B[g[1] + 'F0'], 1) + ' pt, ' + sg(r[g[1] + 'W'] - B[g[1] + 'W'], 1) + ' pt'; }).join(' | ') + ' |'); });
        console.log('  Not modeled (d29): public costs that poverty imposes on everyone, such as crime, homelessness services, incarceration, and emergency and');
        console.log('  institutional health care. The framework argues that removing poverty lowers them (Johnson, "Economic Liberation and Women\'s Autonomy",');
        console.log('  working paper). The model has no such costs, so these group losses are gross of any saving; a saving would follow any design in');
        console.log('  proportion to the poverty it removes, and sizing it needs primary sources verified in-session.');
      });
      CONVERSION_MODEL = 'engine';
    });
    /* Session 9 (dashboard i3-2): the N7 attribution of the BLEI-gated raise, off (through session 8) and on, for Compassionism and
     * the matched UBI and NIT, tax-financed; and Compassionism money-created at a = 1 with every program raise unmatched (aw 0),
     * where the attribution also reaches the price module. CRN-paired within each model. */
    if (secT === 'n7') envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P), o = {fin:'tax', aT:0, a:0, X:XT};
      var rows = [{l:'Baseline (no program)', p:PR.baseline()}];
      MODELS.forEach(function(cm){ CONVERSION_MODEL = cm; var q = PR.cco(), tgt = tbStudy([{p:q}], PILOT, P, o)[0].cost, mU = tbMatch('ubi', tgt, P, PILOT, o), mN = tbMatch('nit', tgt, P, PILOT, o), C = MLBL[cm]; CONVERSION_MODEL = 'engine';
        [[C, q], ['UBI ' + $(mU) + '/yr (matched, ' + cm + ')', PR.ubi(mU)], ['NIT: G ' + $(mN) + ', t 0.5 (matched, ' + cm + ')', PR.nit(mN)]].forEach(function(d){
          [false, true].forEach(function(on){ rows.push({l:d[0] + ', tax' + (on ? ', N7_BLEI on' : ''), p:d[1], cm:cm, g:{N7_BLEI:on}}); }); });
        [false, true].forEach(function(on){ rows.push({l:C + ', money, a = 1, aw 0' + (on ? ', N7_BLEI on' : ''), p:q, cm:cm, g:{N7_BLEI:on}, o:{fin:'money', a:1, aw:0}}); });
      });
      var R = tbStudy(rows.map(function(r){ return {p:r.p, o:r.o, cm:r.cm, g:r.g}; }), nT, P, o), B = R[0];
      console.log('\n--- i3-2, N7 attribution of the BLEI-gated raise: ' + E[0] + ' | seeds 1-' + nT + ' ---');
      console.log('| Design | Gross cost | Adult-years with a BLEI raise | ... of which the design\'s support carried over the gate | Hours vs no response | Earnings response | Inflation (pt/yr) | FGT2 vs Baseline: yr 20 / 20-yr avg | Change from switching N7_BLEI on: hours (pt) / FGT2 yr 20 / 20-yr avg / inflation (pt/yr) |');
      console.log('|---|---|---|---|---|---|---|---|---|');
      R.forEach(function(r, i){ var on = i && rows[i].g && rows[i].g.N7_BLEI, pr = on ? R[i - 1] : null;
        var dd = i ? sg(tbDiff(R[i], B, 'fgt2').m) + ' / ' + sg(tbDiff(R[i], B, 'fgt2PY').m) : '—';
        var ch = pr ? sg((r.hrs - pr.hrs)*100, 3) + ' / ' + sg(tbDiff(R[i], pr, 'fgt2').m, 3) + ' / ' + sg(tbDiff(R[i], pr, 'fgt2PY').m, 3) + ' / ' + sg((r.endoAnn - pr.endoAnn)*100, 3) : '—';
        console.log('| ' + rows[i].l + ' | ' + $(r.cost) + ' | ' + f1(r.bleiR) + '% | ' + (i ? f2(r.bleiP) + '%' : '—') + ' | ' + sg(r.hrs*100) + '% | ' + sg(r.dE*100) + '% | ' + pinf(r.endoAnn) + ' | ' + dd + ' | ' + ch + ' |'); });
    });
    /* Session 8 (A5, dashboard s18; d33 s24; d26 shown for Duke's call): the reporting upgrade. Tax-financed (d26 default) at matched
     * gross cost, design-neutral BLEI gate (d34), per environment and model: Compassionism with the octave wage raise (d19) and the
     * PTF/PTH inflation damping (d33) on and off, the d26 hybrid at a = 0 and a = 1 beside it, and the comparators. Four tables:
     * poverty (FGT0-2 at year 20 and over person-years, persistence and spells), cost and efficiency, prices, work and income
     * distribution, and the group check in dollars. --json=<path> writes the rows the page's front door reads (A6). */
    /* Session 11 (d39; the plan's N3): Compassionism with part of its flat BU moved to a needs-based top-up for participants
     * (max(0, G - 0.5 x wage earnings), paid in BU; the model treats it as cash), at the same total cost, beside Compassionism and
     * the matched NIT. Shares s = 0.25 and 0.5 of the BU. Tax-financed, design-neutral gate, as a5. */
    if (secT === 'topup') envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P), o = {fin:'tax', aT:0, a:0, X:XT};
      MODELS.forEach(function(cm){ CONVERSION_MODEL = cm; var tgt = tbStudy([{p:PR.cco()}], PILOT, P, o)[0].cost;
        var G25 = tbMatch('ccoTop', tgt, P, PILOT, o, 0.25), G50 = tbMatch('ccoTop', tgt, P, PILOT, o, 0.5), G10 = tbMatch('ccoTop', tgt, P, PILOT, o, 0.1), G25t = tbMatch('ccoTop', tgt, P, PILOT, o, {s:0.25, t:0.3}), mN = tbMatch('nit', tgt, P, PILOT, o);
        var rows = [{l:'Baseline', p:PR.baseline()}, {l:'Compassionism', p:PR.cco(), cm:cm}, {l:'Compassionism, theoretical mechanisms off', p:PR.cco(), cm:cm, pw:{octaveWage:true}, o:{noDamp:true}},
          {l:'Compassionism + top-up, s 0.25, G ' + $(G25), p:PR.ccoTop(G25, 0.25), cm:cm}, {l:'  same, theoretical mechanisms off', p:PR.ccoTop(G25, 0.25), cm:cm, pw:{octaveWage:true}, o:{noDamp:true}},
          {l:'Compassionism + top-up, s 0.5, G ' + $(G50), p:PR.ccoTop(G50, 0.5), cm:cm}, {l:'Compassionism + top-up, s 0.1, G ' + $(G10), p:PR.ccoTop(G10, 0.1), cm:cm},
          {l:'Compassionism + top-up, s 0.25, t 0.3, G ' + $(G25t), p:PR.ccoTop(G25t, 0.25, 0.3), cm:cm}, {l:'NIT matched, G ' + $(mN), p:PR.nit(mN)}];
        CONVERSION_MODEL = 'engine';
        var R = tbStudy(rows.map(function(r){ return {p:r.p, o:r.o, pw:r.pw, cm:r.cm}; }), nT, P, o), B = R[0];
        console.log('\n--- topup (d39/N3): ' + E[0] + ' | ' + cm + ' | target ' + $(tgt) + ' | seeds 1-' + nT + ' ---');
        console.log('| Design | Cost | FGT2 20-yr avg vs Baseline [95% CI] | FGT2 yr 20 vs Baseline | FGT0 20-yr avg | Hours | Contribution | vs Compassionism, FGT2 20-yr [95% CI] |');
        console.log('|---|---|---|---|---|---|---|---|');
        R.forEach(function(r, i){ var d = i ? tbDiff(R[i], B, 'fgt2PY') : null, dc = i > 1 ? tbDiff(R[i], R[1], 'fgt2PY') : null;
          console.log('| ' + rows[i].l + ' | ' + $(r.cost) + ' | ' + (d ? sg(d.m) + ' [' + sg(d.lo) + ', ' + sg(d.hi) + ']' : f2(r.fgt2PY)) + ' | ' + (i ? sg(tbDiff(R[i], B, 'fgt2').m) : f2(r.fgt2)) + ' | ' + f1(r.fgt0PY) + '% | ' + sg(r.hrs*100, 1) + '% | ' + (r.tauMean*100).toFixed(1) + '% | ' + (dc ? sg(dc.m) + ' [' + sg(dc.lo) + ', ' + sg(dc.hi) + ']' : '—') + ' |'); });
      }); });
    /* Session 16 (issue i7): 'projcore' runs only the rows the page will carry (d65), each with the launch gift financed both ways
     * (d66): as you go (Duke's pick, the design as intended) and over the run (the endowment's rule, equal terms). */
    if (secT === 'proj' || secT === 'projcore'){  /* N1, session 15 (s33; d58-d65): project hiring paid in expired BU, in place of the octave wage raise */
      var PJROWS = [['Compassionism as it runs now (octave wage raise on)', null, null], ['octave wage raise off (d19)', {octaveWage:true}, null],
        ['PROJECT HIRING (defaults d59-d66), raise off', {octaveWage:true}, {}],
        ['  launch gift financed over the run, like the endowment (d66 alternative)', {octaveWage:true}, {giftFin:'run'}],
        ['  directed share 0.5 (d59)', {octaveWage:true}, {share:0.5}], ['  directed share 0: the launch gift only', {octaveWage:true}, {share:0}],
        ['  gift converted by each holder (d60 alternative)', {octaveWage:true}, {giftMode:'holder'}], ['  no launch gift', {octaveWage:true}, {giftMode:'none'}],
        ['  all participants, no willingness test (d61)', {octaveWage:true}, {alloc:'capqAll'}], ['  lowest wage first (d61)', {octaveWage:true}, {alloc:'low'}],
        ['  equal shares among the willing (d61)', {octaveWage:true}, {alloc:'equal'}], ['  own rate only (d62)', {octaveWage:true}, {rate:'own'}],
        ['  side hours, added on top (d63)', {octaveWage:true}, {hours:'side'}], ['  pay at the median wage, $19.20 an hour (d63)', {octaveWage:true}, {pay:19.20}],
        ['  project hiring with the octave wage raise kept on', null, {}]];
      var CORE = secT === 'projcore';
      if (CORE) PJROWS = [PJROWS[0], PJROWS[1], ['PROJECT HIRING, raise off; gift paid as you go (d66, the design as intended)', {octaveWage:true}, {}],
        ['PROJECT HIRING, raise off; gift financed over the run (d66 alternative: the endowment\'s rule)', {octaveWage:true}, {giftFin:'run'}],
        ['  project hiring with the raise kept on; gift as you go', null, {}], ['  project hiring with the raise kept on; gift over the run', null, {giftFin:'run'}]];
      envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P), o = {fin:'tax', aT:0, a:0, X:XT}, infl = P.inflRate > 0;
        MODELS.forEach(function(cm){
          var cfg = [{p:PR.baseline()}], lbl = ['No program (Baseline)'];
          PJROWS.forEach(function(r){ cfg.push({p:PR.cco(), cm:cm, pw:r[1], pj:r[2]}); lbl.push(r[0]); });
          if (infl){ cfg.push({p:PR.cco(), cm:cm, pw:{octaveWage:true}, o:{noDamp:true}}); lbl.push('octave raise and damping off (the page\'s mechanisms-off row)');
            cfg.push({p:PR.cco(), cm:cm, pw:{octaveWage:true}, pj:{}, o:{noDamp:true}}); lbl.push('PROJECT HIRING, raise and damping off' + (CORE ? '; gift as you go' : ''));
            if (CORE){ cfg.push({p:PR.cco(), cm:cm, pw:{octaveWage:true}, pj:{giftFin:'run'}, o:{noDamp:true}}); lbl.push('PROJECT HIRING, raise and damping off; gift over the run'); } }
          if (!CORE){ cfg.push({p:PR.cco(), cm:cm, pw:{octaveWage:true}, pj:{}, o:{fin:'hybrid', a:0}}); lbl.push('PROJECT HIRING, hybrid financing, a = 0');
          cfg.push({p:PR.cco(), cm:cm, pw:{octaveWage:true}, pj:{}, o:{fin:'hybrid', a:1}}); lbl.push('PROJECT HIRING, hybrid financing, a = 1 (H1)'); }
          var t0 = Date.now(), R = tbStudy(cfg, nT, P, o), B = R[0], OFF = R[2];
          console.log('\n--- ' + secT + ' (N1): ' + E[0] + ' | ' + MLBL[cm] + ' | tax-financed at own cost unless stated | seeds 1-' + nT + ' | ' + ((Date.now() - t0)/1000).toFixed(0) + ' s ---');
          console.log('| Design | Cost | FGT2 20-yr avg vs Baseline [95% CI] | vs raise off [95% CI] | FGT2 yr 20 vs Baseline | Per $1,000 | FGT0 20-yr | Wealth poverty yr 20 | Hours | Contribution | Endogenous inflation | Project net / participant-yr | Project hours / participant-yr | Share working | Contract rate | Pool (expired) / participant-yr | Groups: resources % / FGT0 pt / wealth pov pt (part; non; PTH; low; top) | Worse off |');
          console.log('|' + Array(19).join('---|'));
          R.forEach(function(r, i){ var d = i ? tbDiff(r, B, 'fgt2PY') : null, dO = (i && i !== 2) ? tbDiff(r, OFF, 'fgt2PY') : null;
            console.log('| ' + lbl[i] + ' | ' + $(r.cost) + ' | ' + (d ? sg(d.m) + ' [' + sg(d.lo) + ', ' + sg(d.hi) + ']' : f2(r.fgt2PY)) + ' | ' + (dO ? sg(dO.m) + ' [' + sg(dO.lo) + ', ' + sg(dO.hi) + ']' : '—') +
              ' | ' + (i ? sg(tbDiff(r, B, 'fgt2').m) : f2(r.fgt2)) + ' | ' + (i && r.cost > 0 ? sg(d.m/(r.cost/1000), 3) : '—') + ' | ' + f1(r.fgt0PY) + '% | ' + f1(r.pov) + '% | ' + sg(r.hrs*100, 1) + '% | ' + (r.tauMean*100).toFixed(1) + '% | ' + pinf(r.endoAnn) +
              '% | ' + (r.pjNet || r.pjGift ? $(r.pjNet + r.pjGift) : '—') + ' | ' + (r.pjHrs ? f1(r.pjHrs) : '—') + ' | ' + (r.pjWork ? f1(r.pjWork) + '%' : '—') + ' | ' + (r.pjRc ? f2(r.pjRc) + 'x' : '—') + ' | ' + (r.pjExp ? $(r.pjExp) : '—') +
              ' | ' + (i ? grpCell(r, B) : '—') + ' |'); });
        }); });
    }
    if (secT === 'esp'){  /* N1, session 19 (s38; d70-d76; N1-design-esp-payroll.md, Section 8): ESP payroll in the Hub-spec model. Framework model only. */
      var ES_P = {octaveWage:true};
      var ESROWS = [['TODAY: Hub-spec main row (project hiring, raise off, gift as you go); flat 3x premium to every adult by wage', ES_P, {}, null],
        ['ESP PAYROLL at the defaults (lam 0.20, 23.0% of adults, own rate above par, cap on, rest as today)', ES_P, {}, {}],
        ['  today, gift financed over the run (the d67 row)', ES_P, {giftFin:'run'}, null], ['  ESP payroll, gift financed over the run (the d67 row)', ES_P, {giftFin:'run'}, {}],
        ['  lam 0.15 (d71, low end)', ES_P, {}, {lam:0.15}], ['  lam 0.26 (d71, high end)', ES_P, {}, {lam:0.26}], ['  lam 1: every BU accepted goes to workers (upper bound)', ES_P, {}, {lam:1}],
        ['  workforce 15.2%: no food services (d72)', ES_P, {}, {work:0.152}], ['  workforce: PTF members (d72)', ES_P, {}, {work:'ptf'}], ['  workforce: every adult (today\'s payout population; d72)', ES_P, {}, {work:'all'}],
        ['  BU pay only where the own rate beats the ESP\'s 3x (d73)', ES_P, {}, {take:'biz'}],
        ['  no octave cap (d74)', ES_P, {}, {cap:'none'}], ['  octave cap, excess saved for later years (d74, R6)', ES_P, {}, {cap:'save'}],
        ['  the ESP\'s own premium to its own workers (d75: worker cooperative)', ES_P, {}, {rest:'esp'}],
        ['  today, with the octave wage raise kept on', null, {}, null], ['  ESP payroll, with the octave wage raise kept on', null, {}, {}]];
      envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P), o = {fin:'tax', aT:0, a:0, X:XT}, infl = P.inflRate > 0, cm = 'framework';
        var cfg = [{p:PR.baseline()}], lbl = ['No program (Baseline)'];
        ESROWS.forEach(function(r){ cfg.push({p:PR.cco(), cm:cm, pw:r[1], pj:r[2], es:r[3]}); lbl.push(r[0]); });
        if (infl){ cfg.push({p:PR.cco(), cm:cm, pw:ES_P, pj:{}, o:{noDamp:true}}); lbl.push('  today, raise and damping off (the mechanisms-off row)');
          cfg.push({p:PR.cco(), cm:cm, pw:ES_P, pj:{}, es:{}, o:{noDamp:true}}); lbl.push('  ESP payroll, raise and damping off'); }
        [0, 1].forEach(function(a){ cfg.push({p:PR.cco(), cm:cm, pw:ES_P, pj:{}, o:{fin:'hybrid', a:a}}); lbl.push('  today, hybrid financing, a = ' + a + (a ? ' (H1)' : ''));
          cfg.push({p:PR.cco(), cm:cm, pw:ES_P, pj:{}, es:{}, o:{fin:'hybrid', a:a}}); lbl.push('  ESP payroll, hybrid financing, a = ' + a + (a ? ' (H1)' : '')); });
        var t0 = Date.now(), R = tbStudy(cfg, nT, P, o), B = R[0], TD = R[1];
        function vsT(i){ if (i < 2) return null; var j = lbl[i].indexOf('ESP payroll, with the octave') >= 0 ? lbl.indexOf('  today, with the octave wage raise kept on') :
          lbl[i].indexOf('ESP payroll, raise and damping') >= 0 ? lbl.indexOf('  today, raise and damping off (the mechanisms-off row)') :
          lbl[i].indexOf('ESP payroll, hybrid financing, a = 0') >= 0 ? lbl.indexOf('  today, hybrid financing, a = 0') :
          lbl[i].indexOf('ESP payroll, hybrid financing, a = 1') >= 0 ? lbl.indexOf('  today, hybrid financing, a = 1 (H1)') :
          lbl[i].indexOf('ESP payroll, gift financed over the run') >= 0 ? lbl.indexOf('  today, gift financed over the run (the d67 row)') : /^  today/.test(lbl[i]) ? -1 : 1;
          return j > 0 ? {j:j, d:tbDiff(R[i], R[j], 'fgt2PY')} : null; }
        console.log('\n--- esp (N1, s38): ' + E[0] + ' | ' + MLBL[cm] + ' | tax-financed at own cost unless stated | seeds 1-' + nT + ' | ' + ((Date.now() - t0)/1000).toFixed(0) + ' s ---');
        console.log('Poverty, money and work. "vs its today row": each ESP row against the same configuration with today\'s rule (the main row unless the label says otherwise).');
        console.log('| Design | Cost | FGT2 20-yr avg vs Baseline [95% CI] | vs its today row [95% CI] | FGT2 yr 20 vs Baseline | Per $1,000 | FGT0 20-yr | Wealth poverty yr 20 | Hours | Contribution | Endogenous inflation | Worse off |');
        console.log('|' + Array(13).join('---|'));
        R.forEach(function(r, i){ var d = i ? tbDiff(r, B, 'fgt2PY') : null, v = vsT(i);
          console.log('| ' + lbl[i] + ' | ' + $(r.cost) + ' | ' + (d ? sg(d.m) + ' [' + sg(d.lo) + ', ' + sg(d.hi) + ']' : f2(r.fgt2PY)) + ' | ' + (v ? sg(v.d.m) + ' [' + sg(v.d.lo) + ', ' + sg(v.d.hi) + ']' : '—') +
            ' | ' + (i ? sg(tbDiff(r, B, 'fgt2').m) : f2(r.fgt2)) + ' | ' + (i && r.cost > 0 ? sg(d.m/(r.cost/1000), 3) : '—') + ' | ' + f1(r.fgt0PY) + '% | ' + f1(r.pov) + '% | ' + sg(r.hrs*100, 1) + '% | ' + (r.tauMean*100).toFixed(1) + '% | ' + pinf(r.endoAnn) +
            '% | ' + (i ? grpCell(r, B).split(' | ')[1] : '—') + ' |'); });
        console.log('\nPremium and groups. Premium columns: years 1-19 (year 0 pays none), year-0 dollars, per adult-year unless stated. Groups: change in real resources per adult-year, 20 years, vs the Baseline and vs today\'s main row (part = participants, non = non-participants, low / top = bottom / top third by year-0 wage).');
        console.log('| Design | ESP\'s own premium paid | Payroll premium | Total | Payroll premium per participating ESP worker-yr | Total per participant-yr / non-participant-yr | Payroll BU per ESP worker-yr | BU share of ESP pay | Mean payroll rate | Cap binds (% of participating ESP worker-yrs) | Groups vs Baseline: part / non / low / top | Groups vs today: part / non / low / top |');
        console.log('|' + Array(13).join('---|'));
        R.forEach(function(r, i){ if (!i) return; var g = function(x, y){ return [['gPartRes'], ['gNonRes'], ['gLowRes'], ['gTopRes']].map(function(k){ var dv = x[k[0]] - y[k[0]]; return (dv >= 0 ? '+' : '-') + $(Math.abs(dv)); }).join(' / '); };
          var es = r.esPrem > 0 || r.esBUW > 0;
          console.log('| ' + lbl[i] + ' | ' + $(r.bzPay) + ' | ' + (es ? $(r.esPrem) : '—') + ' | ' + $(r.bzPay + r.esPrem) + ' | ' + (es ? $(r.esPremW) : '—') + ' | ' + $(r.payPart) + ' / ' + $(r.payNon) +
            ' | ' + (es ? $(r.esBUW) : '—') + ' | ' + (es ? f1(r.esShare) + '%' : '—') + ' | ' + (es ? f2(r.esRate) + 'x' : '—') + ' | ' + (es ? r.esCapB.toFixed(2) + '%' : '—') + ' | ' + g(r, B) + ' | ' + (i > 1 ? g(r, TD) : '—') + ' |'); });
        if (!infl) console.log(D33_NOTE);
      });
    }
    if (secT === 'a5'){ var JS = {}, JPATH = (process.argv.filter(function(a){ return /^--json=/.test(a); })[0] || '').split('=')[1];
      envT.forEach(function(e){ var E = ENVT[e], P = Object.assign({}, E[1]), PR = tbPresets(P), o = {fin:'tax', aT:0, a:0, X:XT}, infl = P.inflRate > 0;
        var rows = [{l:'Baseline (no program)', p:PR.baseline(), k:'base'}], tg = {};
        MODELS.forEach(function(cm){ CONVERSION_MODEL = cm; var q = PR.cco(), tgt = tbStudy([{p:q}], PILOT, P, o)[0].cost;
          var mU = tbMatch('ubi', tgt, P, PILOT, o), mN = tbMatch('nit', tgt, P, PILOT, o), mE = tbMatch('endow', tgt, P, PILOT, o), C = MLBL[cm];
          var gT = tbMatch('ccoTop', tgt, P, PILOT, o, {s:TB_TOPUP_S_A5, t:TB_NIT_T});  /* session 11 (d39, d44): the top-up variant at the same cost */
          CONVERSION_MODEL = 'engine'; tg[cm] = tgt;
          rows.push({l:C, p:q, cm:cm, k:'cco', m:cm}, {l:C + ', octave wage raise off (d19)', p:q, cm:cm, pw:{octaveWage:true}, k:'d19', m:cm});
          if (infl) rows.push({l:C + ', PTF/PTH inflation damping off (d33)', p:q, cm:cm, o:{noDamp:true}, k:'d33', m:cm},
            {l:C + ', octave raise and damping off (d19 + d33)', p:q, cm:cm, o:{noDamp:true}, pw:{octaveWage:true}, k:'d19d33', m:cm});
          rows.push({l:C + ', d26 hybrid, a = 0', p:q, cm:cm, o:{fin:'hybrid', a:0}, k:'hyb0', m:cm}, {l:C + ', d26 hybrid, a = 1 (H1)', p:q, cm:cm, o:{fin:'hybrid', a:1}, k:'hyb1', m:cm},
            {l:'UBI ' + $(mU) + '/yr (matched, ' + cm + ')', p:PR.ubi(mU), k:'ubi', m:cm, amt:mU}, {l:'NIT: G ' + $(mN) + ', t 0.5 (matched, ' + cm + ')', p:PR.nit(mN), k:'nit', m:cm, amt:mN},
            {l:'Asset endowment ' + $(mE) + ', wealth < $25,000 (matched, ' + cm + ')', p:PR.endow(mE), k:'endow', m:cm, amt:mE},
            {l:C + ' with a needs-based top-up (s ' + TB_TOPUP_S_A5 + ', G ' + $(gT) + ', t 0.5; same cost)', p:PR.ccoTop(gT, TB_TOPUP_S_A5), cm:cm, k:'top', m:cm, amt:gT},
            {l:C + ' with the top-up, theoretical mechanisms off (d19 + d33)', p:PR.ccoTop(gT, TB_TOPUP_S_A5), cm:cm, o:{noDamp:true}, pw:{octaveWage:true}, k:'topc', m:cm});
        });
        /* session 11: grocery at full scale (cover 1) and as planned (five stores); X-Cents with Power of 1 (k 'xc') and the exchange alone
         * ('xc0'); each comparator at its proposers' size (d45) */
        rows.push({l:'Public grocery, full cover (own cost)', p:PR.groc(1), k:'groc'}, {l:'Public grocery, five stores (cover ' + (TB_GROC_PILOT*100).toFixed(1) + '%; own cost)', p:PR.grocPilot(), k:'grocP'},
          {l:'X-Cents, exchange $3,614/yr + Power of 1 on food, one day a week (own cost)', p:PR.xcFull(1), k:'xc'}, {l:'X-Cents, Power of 1 with no shift in shopping (f = 1/7; own cost)', p:PR.xcFull(1/7), k:'xc7'},
          {l:'X-Cents, flat $3,614/yr (own cost)', p:PR.xc(0), k:'xc0'}, {l:'X-Cents, Power of 1 on food and housing, one day a week (own cost)', p:PR.xcFull(1, true), k:'xcH'},
          {l:'UBI $12,000/yr (proposed size)', p:PR.ubi(TB_UBI_PROP), k:'ubiP'}, {l:'NIT: G $15,960 (poverty guideline), t 0.5 (proposed size)', p:PR.nit(TB_NIT_PROP), k:'nitP'},
          {l:'Stakeholder grant $154,594 once, wealth < $25,000 (proposed size)', p:PR.endow(TB_ENDOW_PROP), k:'endowP'});
        var R = tbStudy(rows.map(function(r){ return {p:r.p, o:r.o, pw:r.pw, cm:r.cm}; }), nT, P, o), B = R[0];
        function ci(d){ return sg(d.m) + ' [' + sg(d.lo) + ', ' + sg(d.hi) + ']'; }
        function cpp(r, k){ var cut = B[k] - r[k]; return r.cost > 1 ? (cut > 0.005 ? $(r.cost/cut) : 'no cut') : '—'; }
        var hdr = '\n--- A5: ' + E[0] + ' | tax-financed at matched cost (d26 default) | design-neutral BLEI gate (d34) | seeds 1-' + nT + ' | targets ' + MODELS.map(function(cm){ return cm + ' ' + $(tg[cm]); }).join(', ') + '/adult-yr ---';
        console.log(hdr + '\n\nA5-1 Poverty. Basket FGT x 100 (income incl. transfers less the contribution, against own cost). Person-years: the 20-year mean, i.e. the area under the poverty curve / 20.');
        console.log('| Design | Gross cost | FGT0 / FGT1 / FGT2, yr 20 | FGT0 / FGT1 / FGT2, person-years | Years poor per adult (of 20) | Ever poor % | Mean spell (yrs) | Poor 10+ of 20 yrs % | Wealth pov % | FGT2 vs Baseline, yr 20 [95% CI] | FGT2 vs Baseline, person-years [95% CI] |');
        console.log('|---|---|---|---|---|---|---|---|---|---|---|');
        R.forEach(function(r, i){ console.log('| ' + rows[i].l + ' | ' + $(r.cost) + ' | ' + f1(r.fgt0) + ' / ' + f2(r.fgt1) + ' / ' + f2(r.fgt2) + ' | ' + f1(r.fgt0PY) + ' / ' + f2(r.fgt1PY) + ' / ' + f2(r.fgt2PY) +
          ' | ' + f2(r.pyPoor) + ' | ' + f1(r.everPoor) + ' | ' + f2(r.spellMean) + ' | ' + f1(r.chronic) + ' | ' + f1(r.pov) + ' | ' + (i ? ci(tbDiff(R[i], B, 'fgt2')) : '—') + ' | ' + (i ? ci(tbDiff(R[i], B, 'fgt2PY')) : '—') + ' |'); });
        console.log('\nA5-2 Cost and efficiency. Cost per point: gross cost per adult-year / points of poverty removed against the Baseline.');
        console.log('| Design | Gross cost | Contribution (mean) | Targeting share | Cut per $1,000: FGT2 yr 20 / FGT2 person-years | Cost per point removed: FGT0 person-years / FGT2 person-years | Worse off (r resources, i income poverty, w wealth poverty) |');
        console.log('|---|---|---|---|---|---|---|');
        R.forEach(function(r, i){ var per = r.cost > 1 ? f2((B.fgt2 - r.fgt2)/(r.cost/1000)) + ' / ' + f2((B.fgt2PY - r.fgt2PY)/(r.cost/1000)) : '—';
          console.log('| ' + rows[i].l + ' | ' + $(r.cost) + ' | ' + (r.tauMean*100).toFixed(1) + '% | ' + (r.cost > 1 ? (r.tgt*100).toFixed(1) + '%' : '—') + ' | ' + per + ' | ' + cpp(r, 'fgt0PY') + ' / ' + cpp(r, 'fgt2PY') + ' | ' + (i ? grpCell(r, B).split(' | ')[1] : '—') + ' |'); });
        console.log('\nA5-3 Prices, work and income distribution. Hours: earnings over the same adult\'s earnings with no labor response (hours at a fixed wage), adult-year mean. Earnings response: the aggregate version (the earlier tables\' "Earnings"). Real wage earnings: before the contribution, in year-1 dollars. Income Gini at year 20: disposable income, OECD definition (the Hub\'s C30: wages + conversion + cash transfers - contribution); and with in-kind cuts added.');
        console.log('| Design | Endogenous inflation (pt/yr) | Price level yr 10 / yr 20 (yr 1 = 1) | Real value of $1 of cash or BU at yr 20 | Employed (% of adult-years) | Hours vs no response | Earnings response | Real wage earnings vs Baseline | Income Gini yr 20: disposable / incl. in-kind |');
        console.log('|---|---|---|---|---|---|---|---|---|');
        R.forEach(function(r, i){ console.log('| ' + rows[i].l + ' | ' + pinf(r.endoAnn) + ' | ' + r.pLev10.toFixed(3) + ' / ' + r.pLev20.toFixed(3) + ' | ' + (/^(cco|d19|d33|d19d33|hyb0|hyb1|ubi|nit|xc|top|topc|ubiP|nitP|xc0|xc7)$/.test(rows[i].k) ? '$' + r.realT.toFixed(3) : '—') +
          ' | ' + f1(r.emp) + ' | ' + sg(r.hrs*100) + '% | ' + sg(r.dE*100) + '% | ' + sg((r.Er/B.Er - 1)*100) + '% | ' + r.giniD.toFixed(3) + ' / ' + r.giniX.toFixed(3) + ' |'); });
        console.log('\nA5-4 Groups (d29): change vs Baseline in real resources per adult-year (%), person-year basket FGT0 (pt), year-20 wealth poverty (pt).');
        var GK = [['participants', 'gPart'], ['non-participants', 'gNon'], ['PTH members', 'gPth'], ['bottom third by year-0 wage', 'gLow'], ['top third by year-0 wage', 'gTop']];
        var gi = []; R.forEach(function(r, i){ if (i && /^(cco|d19|d19d33|hyb1|ubi|nit|groc|top|xc|ubiP|nitP)$/.test(rows[i].k)) gi.push(i); });
        console.log('| Design | ' + GK.map(function(g){ return g[0]; }).join(' | ') + ' |'); console.log('|---|' + GK.map(function(){ return '---|'; }).join(''));
        console.log('| Baseline resources $/adult-yr | ' + GK.map(function(g){ return $(B[g[1] + 'Res']); }).join(' | ') + ' |');
        gi.forEach(function(i){ var r = R[i]; console.log('| ' + rows[i].l + ' | ' + GK.map(function(g){ var b = B[g[1] + 'Res'], dr = r[g[1] + 'Res'] - b;
          return (dr >= 0 ? '+' : '-') + $(Math.abs(dr)) + ' (' + sg((r[g[1] + 'Res']/b - 1)*100, 1) + '%), ' + sg(r[g[1] + 'F0'] - B[g[1] + 'F0'], 1) + ', ' + sg(r[g[1] + 'W'] - B[g[1] + 'W'], 1); }).join(' | ') + ' |'); });
        if (!infl) console.log(D33_NOTE);
        console.log('  Not modeled (d29): public costs of poverty (crime, homelessness services, incarceration, emergency and institutional health care); group losses are gross of any saving.');
        /* JSON for the front door (A6): one record per row */
        JS[e] = {env:E[0], seeds:nT, agents:AG, targets:tg, rows:R.map(function(r, i){ var d2 = i ? tbDiff(R[i], B, 'fgt2') : null, dp = i ? tbDiff(R[i], B, 'fgt2PY') : null, d0 = i ? tbDiff(R[i], B, 'fgt0PY') : null;
          var worse = i ? grpCell(r, B).split(' | ')[1] : 'none';
          return {k:rows[i].k, m:rows[i].m || null, l:rows[i].l, cost:+r.cost.toFixed(0), tau:+(r.tauMean*100).toFixed(1), infl:+(r.endoAnn*100).toFixed(2),
            fgt0PY:+r.fgt0PY.toFixed(2), fgt2PY:+r.fgt2PY.toFixed(3), fgt2:+r.fgt2.toFixed(3), pyPoor:+r.pyPoor.toFixed(2), spell:+r.spellMean.toFixed(2), wpov:+r.pov.toFixed(1),
            d2:d2 ? [+d2.m.toFixed(2), +d2.lo.toFixed(2), +d2.hi.toFixed(2)] : null, dp:dp ? [+dp.m.toFixed(2), +dp.lo.toFixed(2), +dp.hi.toFixed(2)] : null, d0:d0 ? [+d0.m.toFixed(2), +d0.lo.toFixed(2), +d0.hi.toFixed(2)] : null,
            hrs:+(r.hrs*100).toFixed(2), giniD:+r.giniD.toFixed(3), tgt:+(r.tgt*100).toFixed(1), worse:worse,
            grp:GK.map(function(g){ return [g[0], Math.round(r[g[1] + 'Res'] - B[g[1] + 'Res']), +(r[g[1] + 'F0'] - B[g[1] + 'F0']).toFixed(1)]; })}; })};
      });
      if (JPATH){ var prev = {}; try { prev = JSON.parse(require('fs').readFileSync(JPATH, 'utf8')); } catch (x) {}
        Object.keys(JS).forEach(function(k){ prev[k] = JS[k]; }); prev._meta = {engine:(require('fs').readFileSync(require('path').join(__dirname, 'index.html'), 'utf8').match(/VERSION:'([^']+)'/) || [0, '?'])[1], cmd:'node harness.js testbed <seeds> a5 <env> --json=' + JPATH, written:new Date().toISOString().slice(0, 10)};
        require('fs').writeFileSync(JPATH, JSON.stringify(prev)); console.log('\nwrote ' + JPATH); }
    }
    tbSetG(svG); resetNR6(svT);
    console.log('\n(' + ((Date.now() - t0T)/60000).toFixed(1) + ' min)');
  }

  if (mode === 'frontdoor') {
    /* Session 8 (A6): node harness.js frontdoor <a5.json> [index.html]. Builds the front door's comparison from the testbed's a5
     * JSON (written by `testbed <seeds> a5 <envs> --json=<a5.json>`) and writes it into the page's #fd-data block. Reporting only:
     * no run, no engine change. Row order per environment and model: the Baseline; Compassionism; Compassionism with its two
     * unsourced mechanisms off (d19 octave raise + d33 damping; at the reference, with no inflation, the damping has no effect);
     * sensitivity rows (each mechanism alone, d26 hybrid at a = 0 and a = 1); then the comparators. */
    var fsF = require('fs'), pathF = require('path'), SRC = process.argv[3], PAGE = process.argv[4] || pathF.join(__dirname, 'index.html');
    var A = JSON.parse(fsF.readFileSync(SRC, 'utf8')), OUT = {_meta:{engine:A._meta ? A._meta.engine : '?', agents:500, written:A._meta ? A._meta.written : ''}, envs:{}};
    var ENVF = {ref:['Reference: Full Integration settings, no recessions, no inflation', FULL_INTEGRATION], adv:['Adverse Environment: reference settings with recessions, 2% inflation and AI automation', ADVERSE_REFERENCE],
      st:['Stress Test: the adverse environment with weaker settings (40% participation, $900 BU)', STRESS_TEST]};
    var GN = {participants:'participants', 'non-participants':'adults who chose not to take part',  /* session 11: participation is open to all; not taking part is a choice */
      'PTH members':'PTH members', 'bottom third by year-0 wage':'bottom third by wage', 'top third by year-0 wage':'top third by wage'};
    var FK = {part:'participants', non:'non-participants', PTH:'PTH members', low:'bottom third by year-0 wage', top:'top third by year-0 wage'};
    function mon(x){ return '<span style="white-space:nowrap">' + (x < 0 ? '\u2212$' : '+$') + Math.round(Math.abs(x)).toLocaleString('en-US') + ' a year</span>'; }
    function amt(l){ var m = l.match(/\$(\d[\d,]*\d)/); return m ? '$' + m[1] : ''; }
    function worse(r, w, cco){ if (!r.worse || r.worse === 'none') return 'No group'; var fl = {}; r.worse.split(', ').forEach(function(x){ var m = x.match(/^(\w+) \((\w+)\)$/); if (m) fl[FK[m[1]]] = m[2]; });
      var G = {}; r.grp.forEach(function(g){ G[g[0]] = g; }); function one(n){ var f = fl[n], g = G[n]; return GN[n] + (f.indexOf('r') >= 0 ? ' (' + mon(g[1]) + ')' : ' (more poverty)'); }
      var out = [];
      if (cco) Object.keys(GN).forEach(function(n){ if (fl[n]) out.push(one(n)); });
      else { if (fl.participants && fl['non-participants']){ var av = w*G.participants[1] + (1 - w)*G['non-participants'][1]; out.push('most adults (' + (av < 0 ? 'about ' + mon(av) : 'more poverty') + ')'); }
        ['bottom third by year-0 wage', 'top third by year-0 wage'].forEach(function(n){ if (fl[n]) out.push(one(n)); });
        if (!out.length) Object.keys(GN).forEach(function(n){ if (fl[n]) out.push(one(n)); }); }
      var s0 = out.join('; '); return s0.charAt(0).toUpperCase() + s0.slice(1); }
    Object.keys(ENVF).forEach(function(e){ if (!A[e]) return; var X = A[e], w = ENVF[e][1].partRate, rows = {};
      function find(k, m){ return X.rows.filter(function(r){ return r.k === k && (m === null ? true : r.m === m); })[0]; }
      /* Session 11 (d45): two views. 'rows' (equal cost): the basic income, NIT and asset endowment matched to Compassionism's cost.
       * 'prop' (proposed size): each comparator at its proposers' size. Grocery and X-Cents run at their own cost in both, and the
       * Compassionism rows are the same in both. Each view keeps the Baseline first and the mechanisms-off row directly beneath Compassionism. */
      var prop = {};
      ['engine', 'framework'].forEach(function(m){ var C = m === 'engine' ? 'Compassionism, as coded' : 'Compassionism, as specified on the Hub';
        function build(view){ var L = [];
        function add(k, r, label, o){ if (!r) return; o = o || {}; var cco = /^(cco|corr|d19|d33|hyb0|hyb1|top|topc)$/.test(k);
          L.push({k:k, label:label, note:o.note || '', sens:!!o.sens, cost:r.cost, tau:r.tau, infl:r.infl, dp:r.dp, d2:r.d2, fgt2PY:r.fgt2PY, fgt2:r.fgt2, f0:r.fgt0PY, hrs:r.hrs, worse:k === 'base' ? '' : worse(r, w, cco)}); }
        add('base', find('base', null), 'No program (Baseline)');
        add('cco', find('cco', m), C);
        var corr = find('d19d33', m);
        if (corr) add('corr', corr, C + ', without its two theoretical mechanisms', {note:'octave wage raise and PTF/PTH inflation damping off (theoretical, yet to be empirically tested)'});
        else add('corr', find('d19', m), C + ', without its two theoretical mechanisms', {note:'octave wage raise off (theoretical, yet to be empirically tested); with no inflation the damping has no effect'});
        var tp = find('top', m), tc = find('topc', m);
        if (tp) add('top', tp, C + ', with a needs-based top-up', {note:'same cost; a tenth of the flat allowance moved to extra BU for low earners, reduced by 50 cents per dollar earned' + (tc && tc.dp ? '; with the two theoretical mechanisms off: ' + (tc.dp[0] > 0 ? '+' : '\u2212') + Math.abs(tc.dp[0]).toFixed(2) : '')});
        if (corr){ add('d19', find('d19', m), 'octave wage raise off only', {sens:true}); add('d33', find('d33', m), 'inflation damping off only', {sens:true}); }
        add('hyb0', find('hyb0', m), 'conversion rewards paid as new money, no matching output (a = 0)', {sens:true, note:'transfers still paid by the contribution'});
        add('hyb1', find('hyb1', m), 'conversion rewards paid as new money, fully matched by new output (a = 1)', {sens:true, note:'assumes H1, which the model cannot test'});
        if (view === 'cost'){ var u = find('ubi', m), n = find('nit', m), en = find('endow', m);
          if (u) add('ubi', u, 'Basic income, ' + amt(u.l) + ' a year to every adult', {note:'same cost as the Compassionism row'});
          if (n) add('nit', n, 'Negative income tax, ' + amt(n.l) + ' guarantee, 50% phase-out', {note:'same cost; means-tested'});
          if (en) add('endow', en, 'Asset endowment, ' + amt(en.l) + ' once to adults with under $25,000', {note:'same cost; baby-bond-style, but the model has no children'}); }
        else {
          add('ubi', find('ubiP', null), 'Basic income, $12,000 a year to every adult', {note:'its proposed size: $1,000 a month'});
          add('nit', find('nitP', null), 'Negative income tax, $15,960 guarantee, 50% phase-out', {note:'its proposed size: the guarantee at the 2026 poverty guideline for one adult'});
          add('endow', find('endowP', null), 'Stakeholder grant, $154,594 once to adults with under $25,000', {note:'its proposed size: $80,000 in 1999 dollars; the model has no young adults, so it goes to adults with little wealth'}); }
        add('groc', find('groc', null), 'Public grocery network at full scale, 15% off food for every adult', {note:'its own cost; enough stores to serve everyone'});
        add('grocP', find('grocP', null), 'Public grocery network as planned: five stores', {note:'its own cost; serves about 0.5% of shoppers'});
        add('xc', find('xc', null), 'X-Cents: the adult exchange plus Power of 1', {note:'its own cost; one day a week, coins buy food at $1 each'});
        add('xc0', find('xc0', null), 'X-Cents adult exchange only, $3,614 a year', {sens:true});
        add('xcH', find('xcH', null), 'X-Cents with Power of 1 on food and housing', {sens:true, note:'assumes landlords and utilities accept coins at $1 on the designated day'});
        return L; }
        rows[m] = build('cost'); prop[m] = build('prop'); });
      OUT.envs[e] = {name:ENVF[e][0], seeds:X.seeds, rows:rows, prop:prop, cmd:'node harness.js testbed ' + X.seeds + ' a5 ' + e,
        caption:'Tax-financed: each design is paid for by a flat contribution on wages set to cover its cost. Shaded row: the Compassionism design with its two theoretical mechanisms, yet to be empirically tested, switched off. Worse off: each group is compared with itself under no program, and the losses come from the contribution that pays for each design; under Compassionism they fall mainly on adults who chose not to take part, who pay the contribution and receive no BU. Participation is open to every adult; in the model each adult\'s choice is set at the start and kept for 20 years. The comparison runs on the testbed\'s profile, which the live scenarios do not use, so their figures differ; among its differences, PTH cuts housing costs only, discounts skip the tax share of the basket, wages follow prices, and adults adjust how much they work.' +
          (ENVF[e][1].inflRate > 0 ? ' Amounts in the labels are nominal. With 2% inflation, below the 5% cost-of-living trigger, a dollar of cash is worth 0.686 year-1 dollars by year 20, so the costs, which are in year-1 dollars, are lower.' : '')};
    });
    var html = fsF.readFileSync(PAGE, 'utf8'), re = /(<script type="application\/json" id="fd-data">)[\s\S]*?(<\/script>)/;
    if (!re.test(html)) throw new Error('frontdoor: no #fd-data block in ' + PAGE);
    html = html.replace(re, function(m0, a, b){ return a + JSON.stringify(OUT).replace(/</g, '\\u003c') + b; });
    fsF.writeFileSync(PAGE, html);
    console.log('frontdoor: wrote ' + Object.keys(OUT.envs).join(', ') + ' (' + JSON.stringify(OUT).length + ' bytes) into ' + PAGE);
  }

  if (mode === 'v421') {
    /* The investigation behind CONTRIBUTING.md's v4.21 Release Notes: why several v4.19/v4.20
     * figures read counter-intuitively. Sections: hump | margin | neutralbu | relief | lines | ha42 | all. */
    CFG.WEALTH_FLOOR = -10000;
    var nQ = parseInt(process.argv[3] || '200', 10), secQ = process.argv[4] || 'all';
    var CALM = {active:false, incomeMultiplier:1, yearsLeft:0};
    function popFor(P, s){ RNG = mulberry32(s + 700003); return makeLatentPopulation(P.nAgents).map(function(l){ return instantiateAgent(l, P); }); }
    function poorB(a, P){ return agentBLEI(a, P.bu, P.ccoOn, P.pth, P.szh, P.szhCoh, P.ptf) < CFG.BLEI_PRECARIOUS_MAX; }
    function poorN(a){ return agentBLEI(a, 0, false, false, false, 0, false) < CFG.BLEI_PRECARIOUS_MAX; }
    if (secQ === 'hump' || secQ === 'all'){
      var YQ = 40, PQ = Object.assign({}, FULL_INTEGRATION, {years:YQ}), tr = [], cells = {}, tot = 0, trans = {pp:0, pn:0, np:0, nn:0};
      for (var yq = 0; yq <= YQ; yq++) tr.push({all:0, neu:0, part:0, non:0, wpov:0});
      for (var sq = 1; sq <= nQ; sq++){
        var agQ = popFor(PQ, sq), p0 = agQ.map(poorN), nq = agQ.length;
        var recQ = function(y){ var t = tr[y], a = 0, ne = 0, pa = 0, pn = 0, no = 0, nn = 0, wp = 0;
          agQ.forEach(function(x){ var b = poorB(x, PQ); a += b; ne += poorN(x); if (x.inCCO){ pa += b; pn++; } else { no += b; nn++; } wp += x.wealth < CFG.POVERTY_LINE; });
          t.all += a/nq/nQ*100; t.neu += ne/nq/nQ*100; t.part += pa/pn/nQ*100; t.non += no/nn/nQ*100; t.wpov += wp/nq/nQ*100; };
        recQ(0); RNG = mulberry32(sq);
        for (var y2 = 0; y2 < YQ; y2++){ runYear(agQ, y2, PQ, CALM); recQ(y2+1);
          if (y2+1 === 20) agQ.forEach(function(x, i){ var b = poorB(x, PQ), g = (x.inCCO ? 'CCO participant' : 'non-participant') + (x.inPTH ? ', PTH member' : ', not in PTH'); tot++;
            cells['n|'+g] = (cells['n|'+g] || 0) + 1; if (b){ cells['p|'+g] = (cells['p|'+g] || 0) + 1; cells.poor = (cells.poor || 0) + 1; if (x.wealth <= CFG.WEALTH_FLOOR + 1e-6) cells.floor = (cells.floor || 0) + 1; if (x.yrWageUSD + (x.yrConvUSD || 0) < x.yrCostUSD) cells.deficit = (cells.deficit || 0) + 1; }
            trans[(p0[i] ? 'p' : 'n') + (b ? 'p' : 'n')]++; }); }
      }
      console.log('=== BLEI poverty over 40 years, Full Integration: seeds 1-' + nQ + ', ' + AG + ' agents ===');
      console.log('year | BLEI poverty (scenario rules) | (policy-neutral rules) | CCO participants | non-participants | wealth poverty');
      [0,1,2,3,5,7,10,15,20,22,24,25,30,35,40].forEach(function(y){ var t = tr[y]; console.log(y + ' | ' + [t.all, t.neu, t.part, t.non, t.wpov].map(function(v){ return v.toFixed(1); }).join(' | ')); });
      var cross = null; for (var y3 = 1; y3 <= YQ; y3++){ if (tr[y3].all < tr[0].neu && tr[y3-1].all >= tr[0].neu){ cross = y3; } }
      console.log('first year after the peak at or below the year-0 policy-neutral level (' + tr[0].neu.toFixed(1) + '%): year ' + cross);
      console.log('Year 20, BLEI poverty by group:');
      Object.keys(cells).filter(function(k){ return k.indexOf('n|') === 0; }).sort().forEach(function(k){ var g = k.slice(2); console.log('  ' + g + ': ' + ((cells['p|'+g] || 0)/cells[k]*100).toFixed(1) + '% (population share ' + (cells[k]/tot*100).toFixed(1) + '%, contributes ' + ((cells['p|'+g] || 0)/tot*100).toFixed(2) + ' pp)'); });
      console.log('  of the BLEI-poor at year 20: at the wealth floor ' + (cells.floor/cells.poor*100).toFixed(1) + '%, cash deficit in year 20 ' + (cells.deficit/cells.poor*100).toFixed(1) + '%');
      console.log('  year 0 (policy-neutral) -> year 20: poor at both ' + (trans.pp/tot*100).toFixed(2) + '%, poor at year 0 only ' + (trans.pn/tot*100).toFixed(2) + '%, poor at year 20 only ' + (trans.np/tot*100).toFixed(2) + '%');
      console.log('  CCO+PTH floor: one month of BU food value (BU x 990/1200) / CCO_PTH_DAILY_COST = ' + (FULL_INTEGRATION.bu*990/1200/CFG.CCO_PTH_DAILY_COST).toFixed(1) + ' days at $' + FULL_INTEGRATION.bu + '; >= 30 days from BU $' + Math.ceil(30*CFG.CCO_PTH_DAILY_COST*1200/990));
    }
    if (secQ === 'margin' || secQ === 'all'){
      console.log('=== Excess recession distress vs how many participants are near the margin: seeds 1-' + nQ + ', ' + AG + ' agents ===');
      console.log('environment | participants in distress, calm arm (recession years) | within one recession of distress | excess distress (pp) | excess as share of calm distress');
      [['Full Integration + recessions', Object.assign({}, FULL_INTEGRATION, {shock:true})], ['Adverse Environment', ADVERSE_REFERENCE], ['CCO Only + recessions', Object.assign({}, CCO_ONLY, {shock:true})], ['Stress Test', STRESS_TEST]].forEach(function(c){
        var P = c[1], dC = 0, band = 0, ex = 0, n = 0;
        for (var s = 1; s <= nQ; s++){
          var rp = buildRecessionPath(P.years, s), calmP = Object.assign({}, P, {shock:false});
          var a1 = popFor(P, s), a2 = popFor(P, s), p1 = a1.filter(function(a){ return a.inCCO; }), p2 = a2.filter(function(a){ return a.inCCO; });
          var R1 = mulberry32(s), R2 = mulberry32(s);
          for (var y = 0; y < P.years; y++){
            RNG = R1; runYear(a1, y, calmP, CALM); RNG = R2; runYear(a2, y, P, rp[y]);
            if (rp[y].active){ var L = 1 - rp[y].incomeMultiplier, d = 0, b = 0;
              p1.forEach(function(a){ var inc = a.yrWageUSD + (a.yrConvUSD || 0), h = inc + Math.max(0, a.yrWealthStartUSD) - a.yrCostUSD; if (h < 0) d++; else if (h < L*inc) b++; });
              dC += d/p1.length; band += b/p1.length; ex += housingDistressOf(p2) - housingDistressOf(p1); n++; }
          }
        }
        console.log(c[0] + ' | ' + (dC/n*100).toFixed(1) + '% | ' + (band/n*100).toFixed(1) + '% | ' + (ex/n*100).toFixed(2) + ' | ' + (ex/dC*100).toFixed(0) + '%');
      });
    }
    if (secQ === 'neutralbu' || secQ === 'all'){
      console.log('=== Shock-neutral multiplier vs BU amount: Full Integration + recessions, seeds 1-' + nQ + ', ' + AG + ' agents ===');
      console.log('BU | no stabilizer (pp) | neutral multiplier | extra BU at neutrality ($/month) | extra relief (% of basket)');
      [900, 1200, 1500, 1800].forEach(function(bu){
        var st = shockStudy(Object.assign({}, FULL_INTEGRATION, {shock:true, bu:bu, stab:false}), nQ), pts = st.points, lo = null, hi = null;
        pts.forEach(function(q){ if (q.partPP > 0){ if (!lo || q.m > lo.m) lo = q; } else if (!hi || q.m < hi.m) hi = q; });
        var mu = lo && hi ? lo.m + (hi.m - lo.m)*lo.partPP/(lo.partPP - hi.partPP) : st.neutral.m;
        console.log('$' + bu + ' | ' + st.none.partPP.toFixed(2) + ' | x' + st.neutral.m.toFixed(2) + ' (x' + mu.toFixed(3) + ' unrounded) | $' + Math.round((mu - 1)*bu) + ' | ' + (CFG.CCO_RELIEF_AT_REF*(mu - 1)*bu/CFG.CCO_RELIEF_REF_BU*100).toFixed(1) + '%');
      });
    }
    if (secQ === 'relief' || secQ === 'all'){
      var ADVC = Object.assign({}, ADVERSE_REFERENCE, {shock:false});
      console.log('=== CCO relief share under inflation (Adverse Environment settings, recessions off, seed 1): a participant outside PTF and PTH, years 1 / 5 / 10 / 15 / 20 ===');
      [['v4.20, no COLA', true, {}], ['v4.20, COLA', true, {cola:true, colaThresh:0}], ['v4.21, no COLA', false, {}], ['v4.21, COLA', false, {cola:true, colaThresh:0}]].forEach(function(v){
        RELIEF_PRICE_LEGACY = v[1]; var P = Object.assign({}, ADVC, v[2]), ag = popFor(P, 1), out = []; RNG = mulberry32(1);
        for (var y = 0; y < P.years; y++){ runYear(ag, y, P, CALM); var a = ag.filter(function(x){ return x.inCCO && !x.inPTF && !x.inPTH; })[0]; out.push(1 - a.yrCostUSD/a.yrBasketUSD); }
        console.log(v[0] + ': ' + [0,4,9,14,19].map(function(i){ return (out[i]*100).toFixed(1) + '%'; }).join(' / '));
      });
      RELIEF_PRICE_LEGACY = false;
      console.log('=== v4.20 vs v4.21 wherever inflation and CCO are both on: seeds 1-' + nQ + ', ' + AG + ' agents (final year) ===');
      console.log('scenario | version | wealth poverty % | BLEI poverty % | basket poverty (net) % | housing distress % | extreme /10k | median wealth $ | median BLEI d');
      [['Adverse Environment', ADVERSE_REFERENCE], ['Stress Test', STRESS_TEST], ['CCO Only, adverse environment', ccoOnlyFor(ADVERSE_REFERENCE)],
       ['Adverse Environment + COLA', Object.assign({}, ADVERSE_REFERENCE, {cola:true, colaThresh:0})], ['Adverse Environment at 5%', Object.assign({}, ADVERSE_REFERENCE, {inflRate:0.05})],
       ['Adverse Environment at 5% + COLA', Object.assign({}, ADVERSE_REFERENCE, {inflRate:0.05, cola:true, colaThresh:0})], ['Full Integration at 5.5%', Object.assign({}, FULL_INTEGRATION, {inflRate:0.055})],
       ['Full Integration at 5.5% + COLA', Object.assign({}, FULL_INTEGRATION, {inflRate:0.055, cola:true, colaThresh:0})], ['Full Integration @3%', Object.assign({}, FULL_INTEGRATION, {inflRate:0.03})]].forEach(function(c){
        [true, false].forEach(function(leg){ RELIEF_PRICE_LEGACY = leg; var rs = runMany(c[1], nQ); RELIEF_PRICE_LEGACY = false;
          console.log(c[0] + ' | ' + (leg ? 'v4.20' : 'v4.21') + ' | ' + mean(col(rs,'pov')).toFixed(2) + ' | ' + mean(col(rs,'bleiPovPct')).toFixed(2) + ' | ' + f1(mean(col(rs,'basketPov'))) + ' | ' + f1(mean(col(rs,'distress'))) + ' | ' + f1(mean(col(rs,'epTotal'))*100) + ' | $' + Math.round(mean(col(rs,'wealth'))).toLocaleString() + ' | ' + Math.round(mean(col(rs,'bleiMed')))); });
      });
    }
    if (secQ === 'lines' || secQ === 'all'){
      console.log('=== Poverty lines under inflation (measurement only): seeds 1-' + nQ + ', ' + AG + ' agents ===');
      console.log('scenario | final price index | wealth poverty, nominal $25,000 | $25,000 in year-0 dollars | BLEI poverty, year-0 daily cost | current daily cost');
      [['Baseline @3% (shipped comparator)', BASELINE], ['Adverse Environment (2%)', ADVERSE_REFERENCE], ['Stress Test (2%)', STRESS_TEST], ['Full Integration @3%', Object.assign({}, FULL_INTEGRATION, {inflRate:0.03})], ['Full Integration @0% (reference)', FULL_INTEGRATION]].forEach(function(c){
        var P = c[1], acc = {P:0, wn:0, wr:0, bn:0, br:0};
        for (var s = 1; s <= nQ; s++){ var ag = popFor(P, s), rp = P.shock ? buildRecessionPath(P.years, s) : null; RNG = mulberry32(s);
          for (var y = 0; y < P.years; y++) runYear(ag, y, P, rp ? rp[y] : CALM);
          var Pi = ag[0].yrBasketUSD/CFG.LIVING_WAGE_ANNUAL, n = ag.length; acc.P += Pi/nQ;
          ag.forEach(function(a){ var d = agentBLEI(a, P.bu, P.ccoOn, P.pth, P.szh, P.szhCoh, P.ptf); acc.wn += (a.wealth < CFG.POVERTY_LINE)/n/nQ*100; acc.wr += (a.wealth < CFG.POVERTY_LINE*Pi)/n/nQ*100; acc.bn += (d < 30)/n/nQ*100; acc.br += (d/Pi < 30)/n/nQ*100; }); }
        console.log(c[0] + ' | ' + acc.P.toFixed(3) + ' | ' + acc.wn.toFixed(1) + ' | ' + acc.wr.toFixed(1) + ' | ' + acc.bn.toFixed(1) + ' | ' + acc.br.toFixed(1));
      });
    }
    if (secQ === 'ha42' || secQ === 'all'){
      console.log('=== Seed 42, High Automation: the v4.20 regression row, split into its two steps ===');
      var saveS = CFG.AUTO_HIGH_SHARE, rowHA = function(l){ var x = runScenario(HIGH_AUTOMATION, 42); console.log(l + ': ' + x.pov + '% / $' + x.wealth.toLocaleString() + ' / ' + x.bleiMed + 'd'); };
      AUTOMATION_SAMPLER_LEGACY = true; CFG.AUTO_HIGH_SHARE = 0.47; rowHA('v4.19 (legacy sampler, share 0.47)');
      AUTOMATION_SAMPLER_LEGACY = false; rowHA('new sampler, share 0.47 (new population realisation only)');
      CFG.AUTO_HIGH_SHARE = 0.63; rowHA('new sampler, share 0.63 (v4.20 and v4.21)');
      var down = 0; for (var s4 = 1; s4 <= nQ; s4++){ CFG.AUTO_HIGH_SHARE = 0.47; var a4 = runScenario(HIGH_AUTOMATION, s4).pov; CFG.AUTO_HIGH_SHARE = 0.63; if (runScenario(HIGH_AUTOMATION, s4).pov < a4) down++; }
      CFG.AUTO_HIGH_SHARE = saveS;
      console.log('seeds 1-' + nQ + ', same sampler: wealth poverty lower at share 0.63 than at 0.47 in ' + down + ' seeds');
    }
  }
}
