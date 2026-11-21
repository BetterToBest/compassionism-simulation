#!/usr/bin/env node
/* S93 (Nov 21, 2026; research-update prereg/2026-11-s90-private-price-at-sale.md, Amendment 5): the growth-change measure of the BU's swing, for
 * section C1 below full backing, computed from the series dev/tools/s90_swing.js already saved (no run). Per seed: g(t) = BU spent in year t / BU
 * spent in year t - 1 - 1, t = 1-12; the measure is the mean over t = 2-12 of |g(t) - g(t - 1)| (a steady growth rate gives 0, a two-year swing a
 * large value); then averaged over the seeds, and the same on the pooled series beside it. Condition (as section C1): in every environment, at the
 * sale below half of lagged; where the lagged measure is no larger than S92's at-sale measure at full backing (--s92, its series), at the sale no
 * larger than lagged. Chosen after the original measure failed below full backing (Amendment 5), and labelled so.
 * Beside it (Amendment 5, changes from the outside reading): the yearly growth of BU spent, years 1-12 (mean, lowest, highest over seeds and years),
 * and the sensitivity measure in dollars with the trend removed: per seed, log BU spent in years 1-12 fitted by a least-squares line, x(t) = BU
 * spent / exp(fitted line), and the original measure on x (mean over years 2-12 of |x(t) - x(t - 1)| / x(t)), with the same condition. The
 * condition decides on the growth-change measure; the sensitivity measure is reported, and a disagreement is printed.
 * Usage: node dev/tools/s90_swing_growth.js SWING.json [SWING.json ...] --s92=FILE [--out=FILE] */
'use strict';
const fs = require('fs');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const files = process.argv.slice(2).filter(x => !x.startsWith('--')), T1 = 12;
if (!files.length || !arg('s92', '')) { console.error('usage: s90_swing_growth.js SWING.json [...] --s92=FILE [--out=FILE]'); process.exit(1); }
const gm = bu => { const g = []; for (let t = 1; t <= T1; t++) g[t] = bu[t]/bu[t - 1] - 1; let s = 0, k = 0; for (let t = 2; t <= T1; t++) { s += Math.abs(g[t] - g[t - 1]); k++; } return s/k; };
const dm = bu => { const t = [], y = []; for (let k = 1; k <= T1; k++) { t.push(k); y.push(Math.log(bu[k])); }
  const n = t.length, mt = t.reduce((a, b) => a + b, 0)/n, my = y.reduce((a, b) => a + b, 0)/n;
  let sxy = 0, sxx = 0; t.forEach((v, i) => { sxy += (v - mt)*(y[i] - my); sxx += (v - mt)*(v - mt); }); const b = sxy/sxx, a = my - b*mt;
  const x = []; for (let k = 1; k <= T1; k++) x[k] = bu[k]/Math.exp(a + b*k);
  let s = 0, m = 0; for (let k = 2; k <= T1; k++) { s += Math.abs(x[k] - x[k - 1])/x[k]; m++; } return s/m; };
const growth = c => { const g = []; c.perSeed.forEach(r => { for (let t = 1; t <= T1; t++) g.push(r.bu[t]/r.bu[t - 1] - 1); }); return {mean: g.reduce((a, b) => a + b, 0)/g.length, min: Math.min(...g), max: Math.max(...g)}; };
const avg = (c, f) => c.perSeed.reduce((a, r) => a + f(r.bu), 0)/c.perSeed.length;
const cell = c => ({perSeed: avg(c, gm), pooled: gm(c.pooledBU), detrended: avg(c, dm), growth: growth(c)});
const S92 = JSON.parse(fs.readFileSync(arg('s92', ''), 'utf8')), ENVS = ['ref', 'adv', 'st'], p = x => (100*x).toFixed(2) + '%';
const res = {what: 'growth-change measure of the BU swing (prereg 2026-11-s90, Amendment 5; chosen after the original measure failed below full backing)', years: [2, T1], s92: {}, runs: []};
ENVS.forEach(e => { res.s92[e] = {sale: cell(S92.cells[e].sale), lagged: cell(S92.cells[e].lagged)}; });
let all = true, sens = true;
files.forEach(f => {
  const d = JSON.parse(fs.readFileSync(f, 'utf8')), r = {file: f.replace(/.*\//, ''), backedShare: d.backedShare, seeds: d.seeds, cells: {}};
  console.log('backed share ' + d.backedShare + ' (' + r.file + ', seeds ' + d.seeds.join('-') + ')');
  console.log('environment  lagged    at the sale  ratio   | pooled: lagged  at the sale  ratio   | S92 at the sale, full backing  | condition');
  ENVS.forEach(e => {
    const L = cell(d.cells[e].lagged), S = cell(d.cells[e].sale), s92 = res.s92[e].sale.perSeed, noSwing = L.perSeed <= s92;
    const pass = noSwing ? S.perSeed <= L.perSeed : S.perSeed < 0.5*L.perSeed; if (!pass) all = false;
    const s92d = res.s92[e].sale.detrended, noSwingD = L.detrended <= s92d, passD = noSwingD ? S.detrended <= L.detrended : S.detrended < 0.5*L.detrended; if (!passD) sens = false;
    r.cells[e] = {lagged: L, sale: S, ratio: S.perSeed/L.perSeed, ratioPooled: S.pooled/L.pooled, s92sale: s92, noSwing, pass,
      detrended: {lagged: L.detrended, sale: S.detrended, ratio: S.detrended/L.detrended, s92sale: s92d, noSwing: noSwingD, pass: passD}};
    console.log(e.padEnd(11) + '  ' + p(L.perSeed).padStart(7) + '  ' + p(S.perSeed).padStart(11) + '  ' + (S.perSeed/L.perSeed).toFixed(3).padStart(5) + '   |  ' + p(L.pooled).padStart(13) + '  ' +
      p(S.pooled).padStart(11) + '  ' + (S.pooled/L.pooled).toFixed(3).padStart(5) + '   |  ' + p(s92).padStart(28) + '  | ' + (pass ? 'passes' : 'FAILS') + (noSwing ? ' (no lagged swing: fallback)' : ''));
  });
  ENVS.forEach(e => { const c = r.cells[e], gr = x => p(x.mean) + ' (' + p(x.min) + ' to ' + p(x.max) + ')';
    console.log('  ' + e.padEnd(4) + ' sensitivity (detrended, dollars): lagged ' + p(c.detrended.lagged) + ', at the sale ' + p(c.detrended.sale) + ', ratio ' + c.detrended.ratio.toFixed(3) + ' (S92 at the sale ' + p(c.detrended.s92sale) + '): ' + (c.detrended.pass ? 'passes' : 'FAILS') +
      ';  yearly growth of BU spent, years 1-12: lagged ' + gr(c.lagged.growth) + ', at the sale ' + gr(c.sale.growth)); });
  res.runs.push(r);
});
res.pass = all; res.sensitivityPass = sens;
console.log('S92 at full backing on this measure (v5.9 row): ' + ENVS.map(e => e + ' lagged ' + p(res.s92[e].lagged.perSeed) + ', at the sale ' + p(res.s92[e].sale.perSeed)).join('; '));
console.log('S92 at full backing, sensitivity measure: ' + ENVS.map(e => e + ' lagged ' + p(res.s92[e].lagged.detrended) + ', at the sale ' + p(res.s92[e].sale.detrended)).join('; '));
console.log('section C1 on the growth-change measure: ' + (all ? 'holds' : 'does NOT hold') + '; the sensitivity measure ' + (sens ? 'agrees' : 'DISAGREES (reported; section C4)'));
if (arg('out', '')) fs.writeFileSync(arg('out', ''), JSON.stringify(res, null, 1));
process.exit(all ? 0 : 1);
