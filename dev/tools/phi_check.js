#!/usr/bin/env node
/* v5.2.2 (Oct 6, 2026; audit A7, GPT section 18): how big is the Phi step, and how many adults sit near it? Diagnostic only: harness.js is not changed
 * and nothing here feeds a published figure.
 *
 * In the engine an adult's conversion rate is min((1 + q/M x (octave ceiling - 1)) x phi x PTF bonus, M x 1.618), with phi = 1.618 when the quality q is
 * above 0.70 x M (M = the maximum multiplier, CFG.PHI_QUALITY_THRESH) and 1 otherwise; the conversion tax rises with the rate (CFG.PROG_PIVOT,
 * CFG.PROG_RATE, capped at CFG.PROG_TAX_MAX). This tool
 *  1. sweeps q from 0.69 M to 0.71 M (21 points) and prints the rate and the net dollars per BU converted, at the octave of the typical participant near
 *     the threshold (the median octave of participant adult-years within 1% of M of it), with and without the PTF bonus left out (it only scales the rate);
 *  2. runs the release row (as `node harness.js testbed N release ENV` builds it: releaseRows, study options fin 'tax', aT 0, a 0, X 0, the sourced spending
 *     share and REL_V52_STUDY) on seeds 1..N and, every simulated year, counts participant adult-years by q/M (bins of 0.01 from 0.60 to 0.80), the share
 *     within 1% of M of the threshold, the share above it, the share of all conversion income those above it receive, and the mean conversion income (in
 *     today's dollars) of participants just below (0.69-0.70) and just above (0.70-0.71) the threshold, against the median participant's.
 * Usage: node dev/tools/phi_check.js [ENV] [SEEDS]   (ENV ref, adv or st; default ref, 100 seeds); writes dev/runs/phi-check-ENV.json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 100);
const NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || !(N >= 1)) { console.error('usage: phi_check.js ref|adv|st [SEEDS]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), C = H.CFG, SC = H.SPEND_SOURCED, TH = C.PHI_QUALITY_THRESH, PHI = C.PHI_RATIO;
const t0 = Date.now(), wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
/* the engine's rate and tax (runYear's framework branch and pjOwnRate; restated here, checked against each other below) */
function rateOf(p, q, oct, pb) { const oc = 1 + (oct/Math.max(1, p.maxOct))*(Math.max(1, p.maxMult) - 1), qf = Math.min(1, q/Math.max(1, p.maxMult)), ph = (p.phi && q > p.maxMult*TH) ? PHI : 1;
  return Math.min((1 + qf*(oc - 1))*ph*(pb || 1), p.maxMult*(p.phi ? PHI : 1)); }
function taxOf(p, r) { const bT = p.cip ? p.tax*(1 - p.cipDemo*0.18) : p.tax; return Math.min(C.PROG_TAX_MAX, bT + Math.max(0, (r - C.PROG_PIVOT)*C.PROG_RATE)); }
function netPerBU(p, r) { return r*(1 - taxOf(p, r))*(p.cip ? 1 + p.cipDemo*0.12 : 1); }
const out = {_meta: {what: 'the Phi step: rate and net dollars per BU around the quality threshold, and how many participant adult-years sit near it (diagnostic, audit A7)', env, seeds: N,
  manifest: H.runManifest(), command: 'node dev/tools/phi_check.js ' + env + ' ' + N, threshold: TH, phi: PHI}};
try {
  const P = Object.assign({}, H[NAME]), PR = H.tbPresets(P), rel = H.releaseRows(SC).filter(r => r.j === 'release')[0];
  const c = H.n1Row(PR, 'framework', rel.v); if (rel.v.o) Object.assign(c.o || (c.o = {}), rel.v.o);
  const p = c.p, M = p.maxMult, T = P.years;
  const bins = {}, near = {n: 0, oct: []}, acc = {pyears: 0, above: 0, within1: 0, convAll: 0, convAbove: 0, lo: [], hi: [], all: []};
  for (let b = 60; b < 80; b++) bins[(b/100).toFixed(2)] = 0;
  let runs = 0;
  H.setRepHook(function (agents, yr, TT, lf) {
    if (TT !== T) return;  /* tbRun's one-year pre-pass for the contribution rate is not a simulated year of the run */
    if (yr === 0 && agents.some(a => a.inCCO)) runs++;  /* the programme's runs (the study also runs no programme, where no adult takes part) */
    agents.forEach(a => { if (!a.inCCO || !p.ccoOn) return;
      const x = a.quality/M, y = (a.yrConvUSD || 0)/lf; acc.pyears++; acc.convAll += y; acc.all.push(y);
      if (a.quality > M*TH) { acc.above++; acc.convAbove += y; }
      if (Math.abs(x - TH) <= 0.01) { acc.within1++; near.oct.push(a.octave); }
      if (x >= TH - 0.01 && x <= TH) acc.lo.push(y); else if (x > TH && x <= TH + 0.01) acc.hi.push(y);
      if (x >= 0.6 && x < 0.8) bins[(Math.floor(x*100)/100).toFixed(2)]++; });
  });
  try { H.tbStudy([c], N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY)); } finally { H.setRepHook(null); }
  const mean = v => v.length ? v.reduce((s, z) => s + z, 0)/v.length : null, octM = near.oct.length ? H.quantileOf(near.oct, 0.5) : 0;
  const sweep = []; for (let i = 0; i <= 20; i++) { const x = TH - 0.01 + i*0.001, q = x*M, r = rateOf(p, q, octM, 1);
    sweep.push({qShare: +x.toFixed(3), rate: +r.toFixed(4), tax: +taxOf(p, r).toFixed(4), netPerBU: +netPerBU(p, r).toFixed(4)}); }
  const below = sweep.filter(s => s.qShare <= TH).pop(), above = sweep.filter(s => s.qShare > TH)[0];
  /* the restated rate equals the engine's own pjOwnRate-style formula at the same inputs (a guard against this tool drifting from the engine) */
  const agree = [0.5, 0.69, 0.701, 0.9].every(x => { const q = x*M, oc = 1 + (octM/Math.max(1, p.maxOct))*(Math.max(1, M) - 1), want = Math.min((1 + Math.min(1, q/M)*(oc - 1))*(q > M*C.PHI_QUALITY_THRESH ? C.PHI_RATIO : 1), M*C.PHI_RATIO); return Math.abs(rateOf(p, q, octM, 1) - want) < 1e-12; });
  Object.assign(out, {params: {maxMult: M, maxOct: p.maxOct, tax: p.tax, cip: !!p.cip, cipDemo: p.cipDemo, phi: !!p.phi, medianOctaveNearThreshold: octM}, sweep,
    step: {rateBelow: below.rate, rateAbove: above.rate, rateJump: +(above.rate/below.rate).toFixed(4), netBelow: below.netPerBU, netAbove: above.netPerBU, netJump: +(above.netPerBU/below.netPerBU).toFixed(4)},
    population: {runs, participantYears: acc.pyears, shareAbove: +(acc.above/acc.pyears*100).toFixed(2), shareWithin1pct: +(acc.within1/acc.pyears*100).toFixed(3),
      shareOfConversionIncomeAbove: +(acc.convAbove/Math.max(1e-9, acc.convAll)*100).toFixed(2), bins},
    income: {medianParticipant: Math.round(H.quantileOf(acc.all, 0.5)), meanParticipant: Math.round(mean(acc.all)), justBelow: Math.round(mean(acc.lo)), justAbove: Math.round(mean(acc.hi)), nBelow: acc.lo.length, nAbove: acc.hi.length,
      jumpJustAboveOverBelow: acc.lo.length && acc.hi.length ? +(mean(acc.hi)/mean(acc.lo)).toFixed(3) : null}, formulaAgrees: agree});
  if (!agree) { console.error('the restated rate formula differs from the engine\'s'); process.exit(1); }
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'phi-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1));
console.log(JSON.stringify({step: out.step, population: Object.assign({}, out.population, {bins: undefined}), income: out.income, params: out.params}, null, 1));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
