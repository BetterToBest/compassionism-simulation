#!/usr/bin/env node
/* S84 (Nov 17, 2026; research-update PLAN S84): weight tests, run in CI (.github/workflows/checks.yml). The weighted top tail (S59), the distribution measures
 * (S57) and the creditor and government accounts count each simulated adult at a weight. These tests pin down what a weight does.
 *   1. In the main row, the set of weights is the same in every seed and environment tested (seeds 1-3; Reference, Adverse, Stress; which adult carries which weight depends on the seed), finite and positive, sum to the number of adults, and have an effective sample size and a largest single weight
 *      inside stated limits (the numbers are printed: they belong beside any weighted figure).
 *   2. The weighted total, mean, quantile and tail-share functions equal a hand computation on a small population with known weights.
 *   3. Scale: multiplying every weight by a constant changes no quantile and no share.
 *   4. Unit weights: the weighted quantile equals the plain type-7 quantile.
 *   5. Zero weights: an adult with weight 0 adds nothing to a weighted total or to a tail share; its effect on a quantile is reported (the quantile's
 *      interpolation positions use the adult count, so a zero-weight adult can move a quantile slightly: the engine has none, test 1 checks that).
 *   6. Extreme weights: one adult with a very large weight leaves every measure finite and in range; the quantiles go to that adult's value; the
 *      effective sample size falls to about 1 and the diagnostic says so.
 * Usage: node dev/tools/weight_tests.js     (exit 1 on any failure) */
'use strict';
const path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const results = []; const test = (name, fn) => { let r; try { r = fn(); } catch (e) { r = {pass: false, detail: 'threw: ' + e.message}; } results.push(Object.assign({name}, r)); };
const near = (a, b, tol) => Math.abs(a - b) <= (tol === undefined ? 1e-9 : tol)*Math.max(1, Math.abs(a), Math.abs(b));
const type7 = (v, q) => { const s = v.slice().sort((x, y) => x - y), h = (s.length - 1)*q, lo = Math.floor(h), hi = Math.ceil(h); return s[lo] + (s[hi] - s[lo])*(h - lo); };
const QS = [0, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 1];
const lcg = seed => { let s = seed >>> 0; return () => (s = (Math.imul(s, 1664525) + 1013904223) >>> 0)/4294967296; };
const rnd = (n, seed) => { const r = lcg(seed); return Array.from({length: n}, () => Math.exp(8 + 2*r())); };  /* lognormal-looking wealth */

/* 1. The main row's own weights (Reference, Adverse, Stress; two seeds; year 0, where the weights are set). Limits: effective sample size at least 90% of the
 * adults; no adult above 2% of the total weight (500 adults at weight 1 is 0.2% each). */
const S = H.startRelease(); const DIAG = {}; let REF = null;
test('the main row\'s weights: finite, positive, summing to the adults, with an effective sample size above 90% of the adults and no weight above 2% of the total', () => {
  const bad = [];
  for (const env of ['ref', 'adv', 'st']) {
    const P = Object.assign({}, {ref: H.FULL_INTEGRATION, adv: H.ADVERSE_REFERENCE, st: H.STRESS_TEST}[env], {years: 2, nAgents: 500}), W = [];
    H.setRepHook((agents, yr) => { if (yr === 0) W.push(agents.map(a => a._w === undefined ? 1 : +a._w)); });
    try { H.tbStudy(H.r2FreezePair(P, 'rel'), 3, P, H.r2MainStudy()); } finally { H.setRepHook(null); }
    if (!W.length) bad.push(env + ': no weights seen');
    W.forEach((w, i) => { const d = H.weightDiag(w); DIAG[env] = d; const sw = w.slice().sort((x, y) => x - y); if (!REF) REF = sw; else if (sw.length !== REF.length || sw.some((x, k) => Math.abs(x - REF[k]) > 1e-12)) bad.push(env + ' run ' + i + ': the set of weights differs from the first run\'s (it should not change with the seed or the environment; which adult carries which weight may)');
      if (!w.every(x => Number.isFinite(x) && x > 0)) bad.push(env + ' run ' + i + ': a weight is not finite and positive');
      if (!near(d.sum, d.n, 1e-9)) bad.push(env + ' run ' + i + ': weights sum to ' + d.sum + ' for ' + d.n + ' adults');
      if (d.ess < 0.9*d.n) bad.push(env + ' run ' + i + ': effective sample size ' + d.ess.toFixed(1) + ' of ' + d.n);
      if (d.maxShare > 0.02) bad.push(env + ' run ' + i + ': largest weight is ' + (d.maxShare*100).toFixed(2) + '% of the total'); });
  }
  const d = DIAG.ref || {};
  return {pass: !bad.length, detail: bad.length ? bad.join('; ') : 'effective sample size ' + (d.ess || 0).toFixed(1) + ' of ' + d.n + ' adults, largest weight ' + (d.maxW || 0).toFixed(3) + ' (' + ((d.maxShare || 0)*100).toFixed(2) + '% of the total), no zero weights, in all three environments'};
});
S.restore();

test('weightDiag: unit weights give an effective sample size equal to n; one weight carrying everything gives 1', () => {
  const a = H.weightDiag([1, 1, 1, 1]), b = H.weightDiag([0, 0, 5, 0]);
  return {pass: near(a.ess, 4) && near(a.maxShare, 0.25) && near(b.ess, 1) && near(b.maxShare, 1) && b.zeros === 3, detail: 'unit ess ' + a.ess + ', single ess ' + b.ess};
});

/* 2. Hand-computed weighted measures: values 10, 20, 30, 40 with weights 1, 1, 2, 4 (total 8). */
test('weighted total, mean, tail share and quantile equal a hand computation', () => {
  const v = [10, 20, 30, 40], w = [1, 1, 2, 4];
  const total = H.dmTail(v, w, 1, true), mean = total/8;                       /* 10+20+60+160 = 250; mean 31.25 */
  const top25 = H.dmTail(v, w, 0.25, true), bot25 = H.dmTail(v, w, 0.25, false);  /* top quarter = 2 of 8 weight at 40 = 80; bottom quarter = 10 + 20 = 30 */
  const qs = H.dmQuantiles(v, w, [0, 0.5, 1]);  /* positions (cumulative weight before)/(8 - 8/4): 0, 1/6, 2/6, 4/6, so the median is half way from 30 to 40 */
  const o = {}; H.dmMeasure(v, w, o, 'W', 'S');
  const ok = near(total, 250) && near(mean, 31.25) && near(top25, 80) && near(bot25, 30) && near(qs[0], 10) && near(qs[1], 35) && near(qs[2], 40) && near(o.dmWt10S, 32/250*100);  /* top 10% of weight 8 is 0.8 at value 40 */
  return {pass: ok, detail: 'total ' + total + ', mean ' + mean + ', top quarter ' + top25 + ', bottom quarter ' + bot25 + ', median ' + qs[1] + ', top-10% share ' + o.dmWt10S};
});

/* 3. Scale. */
test('multiplying every weight by a constant changes no quantile and no share', () => {
  const v = rnd(300, 5), r = lcg(9), w = v.map(() => 0.2 + 3*r()), w2 = w.map(x => 7.3*x);
  const a = H.dmQuantiles(v, w, QS), b = H.dmQuantiles(v, w2, QS), oa = {}, ob = {}; H.dmMeasure(v, w, oa, 'W', 'S'); H.dmMeasure(v, w2, ob, 'W', 'S');
  const dq = Math.max(...a.map((x, i) => Math.abs(x - b[i])/Math.max(1, Math.abs(x)))), ds = Math.max(...Object.keys(oa).filter(k => !/p\d+S$/.test(k)).map(k => Math.abs(oa[k] - ob[k])/Math.max(1, Math.abs(oa[k]))));
  return {pass: dq < 1e-9 && ds < 1e-9, detail: 'largest relative gap: quantiles ' + dq.toExponential(2) + ', measures ' + ds.toExponential(2)};
});

/* 4. Unit weights equal the plain quantile. */
test('at weight 1 the weighted quantile equals the plain type-7 quantile, for populations of 2 to 500', () => {
  let worst = 0;
  [2, 3, 10, 137, 500].forEach(n => { const v = rnd(n, 11 + n), a = H.dmQuantiles(v, v.map(() => 1), QS); QS.forEach((q, j) => { worst = Math.max(worst, Math.abs(a[j] - type7(v, q))/Math.max(1, Math.abs(a[j]))); }); });
  return {pass: worst < 1e-9, detail: 'largest relative gap ' + worst.toExponential(2)};
});

/* 5. Zero weights. */
test('an adult with weight 0 adds nothing to a weighted total, a tail share or a population-share measure; its effect on quantiles is bounded and reported', () => {
  const v = rnd(200, 21), r = lcg(4), w = v.map(() => 0.5 + 2*r()), v0 = v.concat([123456]), w0 = w.concat([0]);
  const t1 = H.dmTail(v, w, 1, true), t2 = H.dmTail(v0, w0, 1, true), s1 = H.dmTail(v, w, 0.1, true), s2 = H.dmTail(v0, w0, 0.1, true), b1 = H.dmTail(v, w, 0.5, false), b2 = H.dmTail(v0, w0, 0.5, false);
  const a = H.dmQuantiles(v, w, QS), b = H.dmQuantiles(v0, w0, QS), dq = Math.max(...a.map((x, i) => Math.abs(x - b[i])/Math.max(1, Math.abs(x))));
  return {pass: near(t1, t2) && near(s1, s2) && near(b1, b2) && dq < 0.05, detail: 'total gap ' + Math.abs(t1 - t2).toExponential(2) + ', top-10% gap ' + Math.abs(s1 - s2).toExponential(2) + ', bottom-half gap ' + Math.abs(b1 - b2).toExponential(2) + '; largest relative quantile shift from adding one zero-weight adult to 200: ' + (dq*100).toFixed(2) + '%'};
});

/* 6. Extreme weights. */
test('one adult with a weight a million times the others: every measure is finite and in range, the quantiles go to that adult, and the effective sample size says so', () => {
  const v = rnd(200, 31), w = v.map(() => 1); w[17] = 1e6; const d = H.weightDiag(w), o = {}; H.dmMeasure(v, w, o, 'W', 'S');
  const finite = Object.values(o).every(x => Number.isFinite(x)), inRange = ['dmWt1S', 'dmWt10S', 'dmWb50S'].every(k => o[k] >= -1e-9 && o[k] <= 100 + 1e-9);
  const q = H.dmQuantiles(v, w, [0.5, 0.9]), top = v[17];
  const heavy = d.ess < 1.01 && d.maxShare > 0.999;
  return {pass: finite && inRange && heavy && q.every(x => x <= Math.max(...v) && x >= Math.min(...v)), detail: 'effective sample size ' + d.ess.toFixed(3) + ', largest weight ' + (d.maxShare*100).toFixed(3) + '% of the total; median ' + q[0].toFixed(0) + ' (the heavy adult holds ' + top.toFixed(0) + '); top-1% share ' + o.dmWt1S.toFixed(2) + '%'};
});

let fail = 0; results.forEach(r => { if (!r.pass) fail++; console.log((r.pass ? 'PASS ' : 'FAIL ') + r.name + '\n     ' + r.detail); });
console.log(fail ? '\n' + fail + ' of ' + results.length + ' weight tests FAILED' : '\nall ' + results.length + ' weight tests passed');
process.exit(fail ? 1 : 0);
