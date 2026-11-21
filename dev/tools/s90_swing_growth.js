#!/usr/bin/env node
/* S93 (Nov 21, 2026; research-update prereg/2026-11-s90-private-price-at-sale.md, Amendment 5): the growth-change measure of the BU's swing, for
 * section C1 below full backing, computed from the series dev/tools/s90_swing.js already saved (no run). Per seed: g(t) = BU spent in year t / BU
 * spent in year t - 1 - 1, t = 1-12; the measure is the mean over t = 2-12 of |g(t) - g(t - 1)| (a steady growth rate gives 0, a two-year swing a
 * large value); then averaged over the seeds, and the same on the pooled series beside it. Condition (as section C1): in every environment, at the
 * sale below half of lagged; where the lagged measure is no larger than S92's at-sale measure at full backing (--s92, its series), at the sale no
 * larger than lagged. Chosen after the original measure failed below full backing (Amendment 5), and labelled so.
 * Usage: node dev/tools/s90_swing_growth.js SWING.json [SWING.json ...] --s92=FILE [--out=FILE] */
'use strict';
const fs = require('fs');
const arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const files = process.argv.slice(2).filter(x => !x.startsWith('--')), T1 = 12;
if (!files.length || !arg('s92', '')) { console.error('usage: s90_swing_growth.js SWING.json [...] --s92=FILE [--out=FILE]'); process.exit(1); }
const gm = bu => { const g = []; for (let t = 1; t <= T1; t++) g[t] = bu[t]/bu[t - 1] - 1; let s = 0, k = 0; for (let t = 2; t <= T1; t++) { s += Math.abs(g[t] - g[t - 1]); k++; } return s/k; };
const cell = c => ({perSeed: c.perSeed.reduce((a, r) => a + gm(r.bu), 0)/c.perSeed.length, pooled: gm(c.pooledBU)});
const S92 = JSON.parse(fs.readFileSync(arg('s92', ''), 'utf8')), ENVS = ['ref', 'adv', 'st'], p = x => (100*x).toFixed(2) + '%';
const res = {what: 'growth-change measure of the BU swing (prereg 2026-11-s90, Amendment 5; chosen after the original measure failed below full backing)', years: [2, T1], s92: {}, runs: []};
ENVS.forEach(e => { res.s92[e] = {sale: cell(S92.cells[e].sale), lagged: cell(S92.cells[e].lagged)}; });
let all = true;
files.forEach(f => {
  const d = JSON.parse(fs.readFileSync(f, 'utf8')), r = {file: f.replace(/.*\//, ''), backedShare: d.backedShare, seeds: d.seeds, cells: {}};
  console.log('backed share ' + d.backedShare + ' (' + r.file + ', seeds ' + d.seeds.join('-') + ')');
  console.log('environment  lagged    at the sale  ratio   | pooled: lagged  at the sale  ratio   | S92 at the sale, full backing  | condition');
  ENVS.forEach(e => {
    const L = cell(d.cells[e].lagged), S = cell(d.cells[e].sale), s92 = res.s92[e].sale.perSeed, noSwing = L.perSeed <= s92;
    const pass = noSwing ? S.perSeed <= L.perSeed : S.perSeed < 0.5*L.perSeed; if (!pass) all = false;
    r.cells[e] = {lagged: L, sale: S, ratio: S.perSeed/L.perSeed, ratioPooled: S.pooled/L.pooled, s92sale: s92, noSwing, pass};
    console.log(e.padEnd(11) + '  ' + p(L.perSeed).padStart(7) + '  ' + p(S.perSeed).padStart(11) + '  ' + (S.perSeed/L.perSeed).toFixed(3).padStart(5) + '   |  ' + p(L.pooled).padStart(13) + '  ' +
      p(S.pooled).padStart(11) + '  ' + (S.pooled/L.pooled).toFixed(3).padStart(5) + '   |  ' + p(s92).padStart(28) + '  | ' + (pass ? 'passes' : 'FAILS') + (noSwing ? ' (no lagged swing: fallback)' : ''));
  });
  res.runs.push(r);
});
res.pass = all;
console.log('S92 at full backing on this measure (v5.9 row): ' + ENVS.map(e => e + ' lagged ' + p(res.s92[e].lagged.perSeed) + ', at the sale ' + p(res.s92[e].sale.perSeed)).join('; '));
console.log('section C1 on the growth-change measure: ' + (all ? 'holds' : 'does NOT hold'));
if (arg('out', '')) fs.writeFileSync(arg('out', ''), JSON.stringify(res, null, 1));
process.exit(all ? 0 : 1);
