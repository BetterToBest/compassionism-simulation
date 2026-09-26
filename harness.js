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
 * Unreleased (next-round session 1, Sep 26 2026; Duke assigns the version): LEDGER, a reporting-only tally
 * of every money flow runYear() computes, and the `ledger` mode (the A1 issuance ledger); and
 * SURPLUS_CONSUMPTION_BASE, which lets SURPLUS_CONSUMPTION_SHARE apply to all cash surplus. Both are inert
 * by default, and `ledger identity` checks that the tally changes no output. index.html is unchanged.
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
  var buFood=(ccoOn&&a.inCCO&&buAlloc>0)?buAlloc*(990/1200):0;
  var szhD=szhOn?szhCoh*CFG.SZH_ALL_RESIDENTS:0;
  if(szhOn&&ptfOn&&a.inPTF)szhD+=szhTheta(szhCoh)*0.20;
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
  if(p.ptf&&inflRate>0)inflRate*=(1-ptfAdoptFrac*0.5);
  /* v4.15: (1-pthMemberFrac*0.10) replaces the flat *0.90. The 0.10 coefficient (=1-0.90) is
   * unchanged from the historical value and is now the ceiling reached at 100% membership. */
  if(p.pth&&inflRate>0)inflRate*=(1-pthMemberFrac*0.10);
  var dollarCost=CFG.BASE_DAILY_COST*365*Math.pow(1+inflRate,yr);
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
  var buEff=p.bu*stabM*colaF;
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
  var ccoReliefF=CCO_RELIEF_FLAT?0.80:1-Math.min(CFG.CCO_RELIEF_CAP,CFG.CCO_RELIEF_AT_REF*buEff/(CFG.CCO_RELIEF_REF_BU*priceIdx));
  if(LEDGER){LEDGER.idx=Math.pow(1+inflRate,yr);var LY0=LEDGER.y[yr]||(LEDGER.y[yr]={});LY0.pIdx=LEDGER.idx;}  // A1 ledger (reporting only): this year's price index, the one mainLoopCostUSD uses
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
    var wg=CFG.WAGE_BASE_GROWTH;
    if(bleiCheck>CFG.BLEI_PRECARIOUS_MAX&&!PATHWAY_OFF.bleiWage){  // v4.21: harness-only pathway switch
      var drFactor=1/(1+0.5*Math.max(0,a.wage/CFG.WAGE_MEDIAN_SIU-1));
      wg+=CFG.WAGE_BLEI_BONUS*Math.max(0.1,drFactor);
    }
    if(!PATHWAY_OFF.octaveWage)wg+=a.octave*CFG.WAGE_OCTAVE_BONUS;  // v4.21: harness-only pathway switch
    if(p.cip)wg+=p.cipDemo*0.005;
    wg-=popAIDisp*((typeof a.automationRisk==='number'&&!isNaN(a.automationRisk))?a.automationRisk:0.5);  /* v4.17 parity: `||0.5` read a draw of exactly 0 as 0.5 */
    a.wage=Math.max(a.wage*0.80,a.wage*(1+wg));
    if(isNaN(a.wage))a.wage=1;
    var cf=1.0;
    if(p.ptf&&a.inPTF)cf*=(1-(p.szh?0.12+p.szhCoh*0.04:0.12));
    var cfPTF=cf;  // A1 ledger (reporting only)
    if(p.pth&&a.inPTH&&!PATHWAY_OFF.pthCost)cf*=0.65;  // v4.21: harness-only pathway switch
    var cfPreCCO=cf;  // A1 ledger (reporting only)
    if(p.ccoOn&&a.inCCO&&p.bu>0){if(!PATHWAY_OFF.relief)cf*=ccoReliefF;}  // v4.19: was a flat 0.80 (see ccoReliefF). v4.21: pathway switch
    else if(emergLine>=0&&p.ccoOn&&p.bu>0&&!a.inCCO&&typeof a.uCCO==='number'&&a.uCCO<emergLine){cf*=ccoReliefF;emergN++;}  // v4.19: emergency enrollment
    var mainLoopCostUSD=CFG.LIVING_WAGE_ANNUAL*Math.pow(1+inflRate,yr);
    var annualWageUSD=a.wage*12*CFG.WAGE_TO_USD*incomeShock;
    var costUSD=mainLoopCostUSD*cf;
    a.wealth+=annualWageUSD-costUSD;
    if(SURPLUS_CONSUMPTION_SHARE>0&&SURPLUS_CONSUMPTION_BASE==='wage')a.wealth-=SURPLUS_CONSUMPTION_SHARE*Math.max(0,annualWageUSD-costUSD);  // v4.21: harness-only (saving mode)
    var yrCashSurplus=annualWageUSD-costUSD;  // session 1: for SURPLUS_CONSUMPTION_BASE 'cash' (harness-only; no RNG)
    if(LEDGER){  // A1 ledger (reporting only): no RNG, no state read by any dynamic
      ledAdd(yr,'agentYears',1);if(a.inCCO)ledAdd(yr,'partYears',1);
      ledAdd(yr,'wage',annualWageUSD);ledAdd(yr,'cost',costUSD);ledAdd(yr,'basket',mainLoopCostUSD);
      if(SURPLUS_CONSUMPTION_SHARE>0&&SURPLUS_CONSUMPTION_BASE==='wage')ledAdd(yr,'surplusConsumed',SURPLUS_CONSUMPTION_SHARE*Math.max(0,annualWageUSD-costUSD));
      ledAdd(yr,'ptfRelief',mainLoopCostUSD*(1-cfPTF));ledAdd(yr,'pthRelief',mainLoopCostUSD*(cfPTF-cfPreCCO));
      ledAdd(yr,a.inCCO?'ccoRelief':'emergRelief',mainLoopCostUSD*(cfPreCCO-cf));
    }
    a.yrWageUSD=annualWageUSD;a.yrCostUSD=costUSD;a.yrBasketUSD=mainLoopCostUSD;a.yrConvUSD=0;  /* v4.17: income/basket poverty inputs (no RNG) */
    if(isNaN(a.wealth))a.wealth=0;
    if(p.ccoOn&&a.inCCO){
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
      a.wealth+=convGain;totalConversion+=convGain;a.yrConvUSD=convGain;yrCashSurplus+=convGain;
      if(LEDGER){var lcG=PATHWAY_OFF.conversion?0:spend*rate*cipB*incomeShock,lcT=lcG*progTax,lcI=0;while(lcI<LEDGER_RATE_TIERS.length&&rate>=LEDGER_RATE_TIERS[lcI])lcI++;
        var lcTier=LEDGER.tiers[lcI];lcTier.bu+=spend;lcTier.gross+=lcG;lcTier.tax+=lcT;lcTier.net+=convGain;lcTier.n++;
        ledAdd(yr,'buSpent',spend);ledAdd(yr,'convGross',lcG);ledAdd(yr,'convTax',lcT);ledAdd(yr,'convNet',convGain);ledAdd(yr,'convRateXspend',rate*spend);}  // A1 ledger
      if(isNaN(a.wealth))a.wealth=0;
      if(a.octave<p.maxOct){
        var Yusd=a.wage*CFG.WAGE_TO_USD;
        var cBasicMonthly=(dollarCost*cf)/12;
        var edcResidual=(p.pth&&a.inPTH)?CFG.FBS_EDC_RESIDUAL_PTH:CFG.FBS_EDC_RESIDUAL_BASE;
        var fbs=Math.max(0,Yusd+buEff-cBasicMonthly-edcResidual*Yusd);
        var lam=(typeof a.lambda==='number'&&!isNaN(a.lambda))?a.lambda:(CFG.FBS_LAMBDA_LO+CFG.FBS_LAMBDA_HI)/2;
        if(p.cip)lam*=(1+p.cipDemo*CFG.FBS_CIP_LAMBDA_BOOST);
        var pAdvance=1-Math.exp(-lam*fbs);
        if(uAdvance<pAdvance&&!PATHWAY_OFF.octave)a.octave++;  // v4.21: pathway switch
      }
      if(uSzhInduce<szhPartBoost&&!a.inPTF&&p.ptf&&ptfCapAllows()){a.inPTF=uSzhPtfShare<p.ptfShare;if(a.inPTF&&p.ptfCap)ptfLiveCount++;}
    }
    if(p.pth&&a.inPTH&&!PATHWAY_OFF.pthEquity&&!PATHWAY_OFF.pthCost){  // v4.21: pathway switches (off: no routing, no appreciation)
      if(typeof a.pthTenure!=='number'||isNaN(a.pthTenure))a.pthTenure=0;
      a.pthTenure+=1;
      var cfWithoutPTH=cf/0.65;
      var pthSaving=Math.max(0,dollarCost*cfWithoutPTH*(1-0.65));
      var equityContrib=pthSaving*CFG.PTH_EQUITY_CONTRIB_SHARE;
      a.acreEquity+=equityContrib;a.wealth-=equityContrib;yrCashSurplus-=equityContrib;  // session 1: equity routing is not discretionary cash
      var ar=0.030+uPthAppr*0.020+pthApprBonus;var appr=a.acreEquity*ar,lqs=pthLiquidShare(a.pthTenure);a.acreEquity+=PTH_APPR_CONSERVE?appr*(1-lqs):appr;a.wealth+=appr*lqs;yrCashSurplus+=appr*lqs;  /* v4.16: PTH_APPR_CONSERVE=false is bit-identical to index.html */
      if(LEDGER){ledAdd(yr,'pthEquityContrib',equityContrib);ledAdd(yr,'pthAppr',appr);ledAdd(yr,'pthApprLiquid',appr*lqs);}  // A1 ledger
    } else if(a.pthTenure){
      a.pthTenure=0;
    }
    if(p.ptf&&!a.inPTF&&p.ptfShare>0&&yr>0&&ptfCapAllows()){var ap=0.005+CFG.PTF_BASS_Q*ptfAdoptFrac;if(bleiCheck<CFG.BLEI_PRECARIOUS_MAX)ap+=0.015;if(uPtfAdopt<ap){a.inPTF=true;if(p.ptfCap)ptfLiveCount++;}}
    if(SURPLUS_CONSUMPTION_SHARE>0&&SURPLUS_CONSUMPTION_BASE==='cash'){var scC=SURPLUS_CONSUMPTION_SHARE*Math.max(0,yrCashSurplus);a.wealth-=scC;if(LEDGER)ledAdd(yr,'surplusConsumed',scC);}  // session 1: harness-only
    if(a.wealth<CFG.WEALTH_FLOOR){if(LEDGER){var lfA=CFG.WEALTH_FLOOR-a.wealth;ledAdd(yr,'floor',lfA);ledAdd(yr,'floorHits',1);a._ledFloor=(a._ledFloor||0)+lfA;}a.wealth=CFG.WEALTH_FLOOR;}  // A1 ledger inside the clamp
  });
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
  var inc=agents.map(function(a){var w=+a.yrWageUSD,c=+a.yrConvUSD;return (isNaN(w)?0:w)+(isNaN(c)?0:c);});
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
    if (nf) process.exitCode = 1;
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
