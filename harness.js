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
  SS_ANCHOR_SSI_ANNUAL:11928, SS_ANCHOR_SSDI_ANNUAL:19560, SS_ANCHOR_RETIRE_ANNUAL:24852
};
CFG.FBS_HALF_SAT_LO = Math.log(2) / CFG.FBS_LAMBDA_HI;
CFG.FBS_HALF_SAT_HI = Math.log(2) / CFG.FBS_LAMBDA_LO;

var RNG = Math.random;
function mulberry32(seed){var s=seed>>>0;return function(){s=(s+0x6D2B79F5)>>>0;var t=Math.imul(s^(s>>>15),1|s);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}

function lognormal(mu,sigma){var u=Math.max(1e-14,1-RNG()),v=RNG();return Math.exp(mu+sigma*Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v));}
function beta(a,b){var x=gamma(a);return x/(x+gamma(b));}
function gamma(a){if(a===1)return -Math.log(Math.max(1e-14,RNG()));if(a<1)return gamma(1+a)*Math.pow(Math.max(1e-14,RNG()),1/a);for(var i=0;i<5000;i++){var u=RNG(),v=RNG(),y=Math.tan(Math.PI*u),x=Math.sqrt(2*a-1)*y+a-1;if(x>0&&v<=(1+y*y)*Math.exp((a-1)*Math.log(x/(a-1))-Math.sqrt(2*a-1)*y))return x;}return a;}
function standardNormal(){var u=Math.max(1e-14,1-RNG()),v=RNG();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
function drawAutomationRisk(){
  var HIGH_RISK_SHARE=0.47;
  if(RNG()<HIGH_RISK_SHARE)return beta(6,1);
  return beta(1,6);
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
  var inflRate=p.inflRate||0;
  if(p.ptf&&inflRate>0)inflRate*=(1-p.ptfShare*0.5);
  if(p.pth&&inflRate>0)inflRate*=0.90;
  var dollarCost=CFG.BASE_DAILY_COST*365*Math.pow(1+inflRate,yr);
  var popShock=recSt.active?recSt.incomeMultiplier:1.0;
  var ptfAdoptFrac=0;
  if(p.ptf&&p.ptfShare>0){var ptfCount=0;agentSet.forEach(function(a){if(a.inPTF)ptfCount++;});ptfAdoptFrac=ptfCount/Math.max(1,agentSet.length);}
  var ptfLiveCount=0,ptfLiveTotal=agentSet.length;
  if(p.ptf&&p.ptfCap){agentSet.forEach(function(a){if(a.inPTF)ptfLiveCount++;});}
  function ptfCapAllows(){return !p.ptfCap||ptfLiveCount<ptfLiveTotal*p.ptfShare;}
  var popAIDisp=0;
  if(p.automation){
    if(yr>=CFG.AI_DISPLACEMENT_YEAR_2)popAIDisp=CFG.AI_DISPLACEMENT_RATE_1*(CFG.AI_DISPLACEMENT_YEAR_2-CFG.AI_DISPLACEMENT_YEAR_1)+CFG.AI_DISPLACEMENT_RATE_2*(yr-CFG.AI_DISPLACEMENT_YEAR_2+1);
    else if(yr>=CFG.AI_DISPLACEMENT_YEAR_1)popAIDisp=CFG.AI_DISPLACEMENT_RATE_1*(yr-CFG.AI_DISPLACEMENT_YEAR_1+1);
    popAIDisp=Math.min(0.10,popAIDisp);
  }
  agentSet.forEach(function(a){
    if(isNaN(a.wealth))a.wealth=0;if(isNaN(a.wage)||a.wage<=0)a.wage=1;
    var agentVar=0.90+RNG()*0.20,incomeShock=popShock*agentVar;
    var uSpendFrac=0.60+RNG()*0.30;
    var uCipQuality=RNG();
    var uAdvance=RNG();
    var uSzhInduce=RNG();
    var uSzhPtfShare=RNG();
    var uPthAppr=RNG();
    var uPtfAdopt=RNG();
    var bleiCheck=agentBLEI(a,p.bu,p.ccoOn,p.pth,p.szh,p.szhCoh,p.ptf);
    var wg=CFG.WAGE_BASE_GROWTH;
    if(bleiCheck>CFG.BLEI_PRECARIOUS_MAX){
      var drFactor=1/(1+0.5*Math.max(0,a.wage/CFG.WAGE_MEDIAN_SIU-1));
      wg+=CFG.WAGE_BLEI_BONUS*Math.max(0.1,drFactor);
    }
    wg+=a.octave*CFG.WAGE_OCTAVE_BONUS;
    if(p.cip)wg+=p.cipDemo*0.005;
    wg-=popAIDisp*(a.automationRisk||0.5);
    a.wage=Math.max(a.wage*0.80,a.wage*(1+wg));
    if(isNaN(a.wage))a.wage=1;
    var cf=1.0;
    if(p.ptf&&a.inPTF)cf*=(1-(p.szh?0.12+p.szhCoh*0.04:0.12));
    if(p.pth&&a.inPTH)cf*=0.65;
    if(p.ccoOn&&a.inCCO&&p.bu>0)cf*=0.80;
    var mainLoopCostUSD=CFG.LIVING_WAGE_ANNUAL*Math.pow(1+inflRate,yr);
    var annualWageUSD=a.wage*12*CFG.WAGE_TO_USD*incomeShock;
    var costUSD=mainLoopCostUSD*cf;
    a.wealth+=annualWageUSD-costUSD;
    if(isNaN(a.wealth))a.wealth=0;
    if(p.ccoOn&&a.inCCO){
      var decay=p.expiry<2?0:0.7;
      a.buBalance=Math.min(a.buBalance*decay+p.bu,p.bu*3);
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
      var convGain=spend*rate*(1-progTax)*cipB*incomeShock;
      a.wealth+=convGain;totalConversion+=convGain;
      if(isNaN(a.wealth))a.wealth=0;
      if(a.octave<p.maxOct){
        var Yusd=a.wage*CFG.WAGE_TO_USD;
        var cBasicMonthly=(dollarCost*cf)/12;
        var edcResidual=(p.pth&&a.inPTH)?CFG.FBS_EDC_RESIDUAL_PTH:CFG.FBS_EDC_RESIDUAL_BASE;
        var fbs=Math.max(0,Yusd+p.bu-cBasicMonthly-edcResidual*Yusd);
        var lam=(typeof a.lambda==='number'&&!isNaN(a.lambda))?a.lambda:(CFG.FBS_LAMBDA_LO+CFG.FBS_LAMBDA_HI)/2;
        if(p.cip)lam*=(1+p.cipDemo*CFG.FBS_CIP_LAMBDA_BOOST);
        var pAdvance=1-Math.exp(-lam*fbs);
        if(uAdvance<pAdvance)a.octave++;
      }
      if(uSzhInduce<szhPartBoost&&!a.inPTF&&p.ptf&&ptfCapAllows()){a.inPTF=uSzhPtfShare<p.ptfShare;if(a.inPTF&&p.ptfCap)ptfLiveCount++;}
    }
    if(p.pth&&a.inPTH){
      if(typeof a.pthTenure!=='number'||isNaN(a.pthTenure))a.pthTenure=0;
      a.pthTenure+=1;
      var cfWithoutPTH=cf/0.65;
      var pthSaving=Math.max(0,dollarCost*cfWithoutPTH*(1-0.65));
      var equityContrib=pthSaving*CFG.PTH_EQUITY_CONTRIB_SHARE;
      a.acreEquity+=equityContrib;a.wealth-=equityContrib;
      var ar=0.030+uPthAppr*0.020+pthApprBonus;var appr=a.acreEquity*ar;a.acreEquity+=appr;a.wealth+=appr*pthLiquidShare(a.pthTenure);
    } else if(a.pthTenure){
      a.pthTenure=0;
    }
    if(p.ptf&&!a.inPTF&&p.ptfShare>0&&yr>0&&ptfCapAllows()){var ap=0.005+CFG.PTF_BASS_Q*ptfAdoptFrac;if(bleiCheck<CFG.BLEI_PRECARIOUS_MAX)ap+=0.015;if(uPtfAdopt<ap){a.inPTF=true;if(p.ptfCap)ptfLiveCount++;}}
    if(a.wealth<CFG.WEALTH_FLOOR)a.wealth=CFG.WEALTH_FLOOR;
  });
  return{bu:totalBU,conversion:totalConversion};
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
function structuralStability(wealthSeries,bleiSeries){
  var q=Math.max(1,Math.floor(wealthSeries.length/4));
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
  RNG = mulberry32(seed);
  var aWealth = [], aBlei = [];
  for (var yr = 0; yr < p.years; yr++){
    runYear(agents, yr, p, {active:false, incomeMultiplier:1.0, yearsLeft:0});
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
    medianPinned: Math.round(finalM.med) === floor
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

module.exports = { CFG, mulberry32, runScenario, FULL_INTEGRATION, BASELINE };

/* ─── CLI modes ──────────────────────────────────────────────────────── */
if (require.main === module) {
  var mode = process.argv[2] || 'validate';

  if (mode === 'validate') {
    CFG.WEALTH_FLOOR = -10000; // shipped default
    var r = runScenario(FULL_INTEGRATION, 42);
    console.log('=== Validation: seed 42, Full Integration, 20yr, WEALTH_FLOOR=-10000 (shipped default) ===');
    console.log(JSON.stringify(r, null, 2));
    console.log('\nDocumented (CONTRIBUTING.md v4.5/v4.6/v4.7 regression tables, unchanged across all three):');
    console.log('  Median BLEI:      1965 d');
    console.log('  BLEI poverty:     13.6 %');
    console.log('  Median wealth:    $559223');
    console.log('  Wealth poverty:   16.6 %');
    console.log('  Gini (EDC-adj):   0.534');
    console.log('  System Stability: 88.5 %');
    console.log('  Avg EDC:          24.9 %');
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
}
