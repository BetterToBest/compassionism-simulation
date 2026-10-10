#!/usr/bin/env node
/* v5.4 item 7 (Oct 7, 2026; dev/reports/v5-21-v54-design.md, 1.4): WHICH ASSUMPTIONS THE RESULTS DEPEND ON. Global sensitivity of the programme's paired
 * effect (programme minus no programme, same seeds) on the v5.4 configuration (the v5.3 main row with job loss, the PTH balance sheet and PTF by sector).
 *   morris ENV R SEEDS        Morris screening (Morris 1991; Campolongo, Cariboni and Saltelli 2007): R random one-at-a-time trajectories over the k inputs
 *                             below, each on a 4-level grid of its range (step 2/3 of the range); for each input, mu* (the mean absolute elementary effect,
 *                             in the measure's units per full range) ranks how much it moves the result, sigma shows interaction or curvature.
 *   sobol ENV N SEEDS --params=a,b,...   Sobol indices for the named inputs (the others at their main values): Saltelli's design with N base points
 *                             (A, B and one A-with-B's-column matrix per input: N(k+2) points); first-order index S (Saltelli et al. 2010) and total
 *                             index ST (Jansen 1999) of each input's share of the result's variance.
 *   noise ENV SEEDS           run-to-run uncertainty: the paired effect's spread across seeds at the main values.
 * Each point runs SEEDS paired seeds (1..SEEDS): the paired difference is far less noisy than either run, and the same seeds at every point keep the noise
 * out of the comparisons between points. Ranges: sourced constants over their sources' ranges, design parameters over the ranges the reports sweep; each
 * range is the study's choice and is printed with the results. The engine is not changed; every input is restored after each point.
 * Output: dev/runs/v54/gsa-MODE-ENV.json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const C = H.CFG, ROOT = path.join(__dirname, '..', '..');
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : null; };
const pos = process.argv.slice(2).filter(x => !x.startsWith('--'));
const MODE = pos[0], env = pos[1] || 'ref', NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
const V54 = {empl: {}, pthb: {}, ptfs: {}};
const K = ['fgt0PY', 'pov', 'bOAPy', 'cost', 'endoAnn'];
/* The inputs: [name, lo, hi, what, how it is set]. P: the preset; S: the study's spending share; L: LABOR_DEFAULTS; G: CFG; T: the price module's supply
 * responses; E/F: the v54 options. Integer inputs are rounded. */
const IN = [
  ['bu', 900, 1500, 'BU a month (design)', (s, v) => { s.P.bu = v; }],
  ['tax', 0.08, 0.18, 'conversion tax (design)', (s, v) => { s.P.tax = v; }],
  ['part', 0.40, 0.90, 'participation (design)', (s, v) => { s.P.partRate = v; }],
  ['ptfShare', 0.08, 0.30, 'PTF membership ceiling (design)', (s, v) => { s.P.ptfShare = v; }],
  ['pthUptake', 0.10, 0.30, 'PTH uptake (design)', (s, v) => { s.P.pthUptake = v; }],
  ['szhCoh', 0.35, 0.90, 'Social Zone cohesion (design)', (s, v) => { s.P.szhCoh = v; }],
  ['maxOct', 4, 6, 'octaves (design, integer)', (s, v) => { s.P.maxOct = Math.round(v); }],
  ['maxMult', 6, 12, 'top conversion rate (design, integer)', (s, v) => { s.P.maxMult = Math.round(v); }],
  ['spend', 0.45, 0.75, 'share of extra cash spent (BEA saving rate; range of recent years)', (s, v) => { s.sc = v; }],
  ['rho', 0.05, 0.30, 'income effect on earnings per unconditional dollar', (s, v) => { H.LABOR_DEFAULTS.rho = v; H.LABOR_DEFAULTS.rhoBU = v; }],
  ['eps', 0.10, 0.50, 'wage elasticity of hours', (s, v) => { H.LABOR_DEFAULTS.eps = v; }],
  ['bleiBonus', 0, 0.016, 'yearly wage gain with BLEI above 30 days (design)', (s, v) => { C.WAGE_BLEI_BONUS = v; }],
  ['thetaH', 0.3, 0.9, 'housing supply response to demand', (s, v) => { H.PM_DEFAULTS.theta.housing = v; }],
  ['jobLoss', 0.06, 0.14, 'yearly chance of job loss (CPS: 0.085 normal, 0.142 recession)', (s, v) => { C.EMPL_P = v; }],
  ['payCut', 0, 0.20, 'mean pay cut after a permanent job loss (design)', (s, v) => { s.v54.empl = Object.assign({}, s.v54.empl, {cut: v}); }],
  ['ptfOther', 0, 0.25, 'PTF cut in transport, health care, childcare (design)', (s, v) => { s.v54.ptfs = Object.assign({}, s.v54.ptfs, {other: v}); }],
  ['pthExit', 0, 0.12, 'yearly chance a PTH member leaves (CPS: renters 0.062)', (s, v) => { s.v54.pthb = Object.assign({}, s.v54.pthb, {exit: v}); }]
];
const MAIN = {bu: 1200, tax: 0.12, part: null, ptfShare: null, pthUptake: null, szhCoh: null, maxOct: 6, maxMult: 9, spend: H.SPEND_SOURCED, rho: H.LABOR_DEFAULTS.rho, eps: H.LABOR_DEFAULTS.eps,
  bleiBonus: C.WAGE_BLEI_BONUS, thetaH: H.PM_DEFAULTS.theta.housing, jobLoss: C.EMPL_P, payCut: 0.10, ptfOther: 0, pthExit: 0.062};
function mainVals() { const P = H[NAME]; return IN.map(([n]) => n === 'part' ? P.partRate : MAIN[n] !== null && MAIN[n] !== undefined ? MAIN[n] : P[n]); }
const SAVE = {lab: Object.assign({}, H.LABOR_DEFAULTS), th: H.PM_DEFAULTS.theta.housing, blei: C.WAGE_BLEI_BONUS, jl: C.EMPL_P};
function restore() { Object.assign(H.LABOR_DEFAULTS, SAVE.lab); H.PM_DEFAULTS.theta.housing = SAVE.th; C.WAGE_BLEI_BONUS = SAVE.blei; C.EMPL_P = SAVE.jl; }
/* One point: x = values in input order; returns the mean paired effect on each measure and the per-seed effects. */
function evalPoint(x, seeds) {
  const s = {P: Object.assign({}, H[NAME]), sc: H.SPEND_SOURCED, v54: JSON.parse(JSON.stringify(V54))};
  try {
    IN.forEach(([, , , , set], i) => set(s, x[i]));
    const PR = H.tbPresets(s.P), M = H.relMainCfgs(PR), wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000; const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
    try {
      const cfg = [Object.assign(M[0], {sc: s.sc, v54: s.v54}), Object.assign(M[1], {sc: s.sc, v54: s.v54})];
      const R = H.tbStudy(cfg, seeds, s.P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: s.sc}, H.REL_V52_STUDY)), out = {}, per = {};
      K.forEach(k => { const f = k === 'endoAnn' ? 100 : 1, d = Array.from(R[1]._s[k]).map((v, j) => (v - R[0]._s[k][j])*f); per[k] = d; out[k] = d.reduce((a, b) => a + b, 0)/d.length; });
      return {y: out, per};
    } finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
  } finally { restore(); }
}
function rng(seed) { let s = seed >>> 0; return () => { s = (s + 0x6D2B79F5) >>> 0; let t = Math.imul(s ^ (s >>> 15), 1 | s); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0)/4294967296; }; }
const val = (i, u) => IN[i][1] + u*(IN[i][2] - IN[i][1]);
const t0 = Date.now(), dir = path.join(ROOT, 'dev', 'runs', 'v54'); fs.mkdirSync(dir, {recursive: true});
const meta = {what: 'v5.4 item 7: global sensitivity of the paired programme effect', mode: MODE, env, manifest: H.runManifest(), command: 'node dev/tools/gsa.js ' + process.argv.slice(2).join(' '),
  inputs: IN.map(([n, lo, hi, w], i) => ({name: n, lo, hi, what: w, main: mainVals()[i]})), measures: K, v54: V54};
let res;
if (MODE === 'morris') {
  const R = +(pos[2] || 10), S = +(pos[3] || 10), k = IN.length, p = 4, D = p/(2*(p - 1)), r = rng(54001), EE = IN.map(() => K.map(() => []));
  for (let t = 0; t < R; t++) {
    let u = IN.map(() => Math.floor(r()*(p/2))/(p - 1));  /* start on the lower half of the grid so +D stays in range */
    let y0 = evalPoint(u.map((v, i) => val(i, v)), S).y;
    const ord = IN.map((_, i) => i).sort(() => r() - 0.5);
    for (const i of ord) { const u2 = u.slice(); u2[i] = u[i] + D; const y1 = evalPoint(u2.map((v, j) => val(j, v)), S).y;
      K.forEach((m, j) => EE[i][j].push((y1[m] - y0[m])/D)); u = u2; y0 = y1; }
    process.stderr.write('trajectory ' + (t + 1) + ' of ' + R + ' (' + Math.round((Date.now() - t0)/1000) + ' s)\n');
  }
  res = {R, seeds: S, inputs: {}};
  IN.forEach(([n], i) => { res.inputs[n] = {}; K.forEach((m, j) => { const e = EE[i][j], mu = e.reduce((a, b) => a + b, 0)/e.length;
    res.inputs[n][m] = {muStar: e.reduce((a, b) => a + Math.abs(b), 0)/e.length, mu, sigma: Math.sqrt(e.reduce((a, b) => a + (b - mu)*(b - mu), 0)/Math.max(1, e.length - 1))}; }); });
} else if (MODE === 'sobol') {
  const N = +(pos[2] || 64), S = +(pos[3] || 10), names = (arg('params') || '').split(',').filter(Boolean), idx = names.map(n => IN.findIndex(q => q[0] === n));
  if (!names.length || idx.some(i => i < 0)) { console.error('sobol needs --params=a,b,... from: ' + IN.map(q => q[0]).join(', ')); process.exit(1); }
  const r = rng(54002), base = mainVals(), A = [], B = [];
  for (let n = 0; n < N; n++) { A.push(idx.map(() => r())); B.push(idx.map(() => r())); }
  const pt = row => { const x = base.slice(); idx.forEach((i, j) => { x[i] = val(i, row[j]); }); return x; };
  const fA = A.map(a => evalPoint(pt(a), S).y), fB = B.map(b => evalPoint(pt(b), S).y), fAB = idx.map((_, j) => A.map((a, n) => { const m = a.slice(); m[j] = B[n][j]; return evalPoint(pt(m), S).y; }));
  res = {N, seeds: S, params: names, indices: {}};
  K.forEach(m => { const ya = fA.map(y => y[m]), yb = fB.map(y => y[m]), all = ya.concat(yb), mean = all.reduce((a, b) => a + b, 0)/all.length, V = all.reduce((a, b) => a + (b - mean)*(b - mean), 0)/(all.length - 1);
    res.indices[m] = {variance: V, mean};
    names.forEach((nm, j) => { const yab = fAB[j].map(y => y[m]); let s1 = 0, st = 0; for (let n = 0; n < N; n++) { s1 += yb[n]*(yab[n] - ya[n]); st += (ya[n] - yab[n])*(ya[n] - yab[n]); }
      res.indices[m][nm] = {S: V > 0 ? s1/N/V : 0, ST: V > 0 ? st/(2*N)/V : 0}; }); });
} else if (MODE === 'noise') {
  const S = +(pos[2] || 100), e = evalPoint(mainVals(), S); res = {seeds: S, mean: e.y, sd: {}, sd500: {}};
  K.forEach(m => { const d = e.per[m], mu = e.y[m], sd = Math.sqrt(d.reduce((a, b) => a + (b - mu)*(b - mu), 0)/(d.length - 1)); res.sd[m] = sd; res.sd500[m] = sd/Math.sqrt(500); });
} else { console.error('usage: gsa.js morris|sobol|noise ENV ...'); process.exit(1); }
meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(dir, 'gsa-' + MODE + '-' + env + '.json');
fs.writeFileSync(file, JSON.stringify({_meta: meta, result: res}, null, 1) + '\n');
console.log('gsa ' + MODE + ' ' + env + ' (' + meta.seconds + ' s) -> ' + path.relative(ROOT, file));
if (MODE === 'morris') K.forEach(m => { console.log(m + ': ' + IN.map(q => q[0]).sort((a, b) => res.inputs[b][m].muStar - res.inputs[a][m].muStar).slice(0, 6).map(n => n + ' ' + res.inputs[n][m].muStar.toFixed(2)).join(', ')); });
if (MODE === 'sobol') K.forEach(m => console.log(m + ': ' + res.params.map(n => n + ' S ' + res.indices[m][n].S.toFixed(2) + ' ST ' + res.indices[m][n].ST.toFixed(2)).join('; ')));
if (MODE === 'noise') console.log(JSON.stringify(res.sd));
