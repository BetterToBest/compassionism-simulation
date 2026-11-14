#!/usr/bin/env node
/* S73 (Nov 14, 2026): the pilot preregistered in research-update prereg/2026-11-s73-participation.md.
 * (A) today's main row's lf {} ; the yearly flows lf {fl: 'stock'} ; the flows and the participation margin lf {fl: 'stock', pm: 0.43}.
 * (B) pm 0.25, 0.7, 1 with the flows; ageing (ag) with lf {} and with lf {fl: 'panel' | 'stock', pm: 0.43}.
 * (C) C2.2 under the flat contribution on wages (share 1, base w, cap 0.9, fx.fin 'money'; S72's D21 row), without and with pm 0.43.
 * (V) S60's validation: $12,000 a year to every adult and no programme otherwise, with pm 0, 0.43, 1 (fl 'stock'); study fin 'none' as S60, without the government account (it reads a contribution).
 * Every lf reading has its own no-programme run (the flows change the baseline); the margin moves no no-programme run (unit test), so the pm rows
 * share the flows' no-programme run. The candidate main row (r2MainRow, r2MainStudy) otherwise, 500 adults, 20 years.
 * Usage: node dev/tools/s73_pilot.js ENV SEEDS [OUTDIR]     ENV ref | adv | st; writes OUTDIR/s73-pilot-ENV.json (per-seed values of every key read) */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const E = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}, env = process.argv[2] || 'ref', N = +(process.argv[3] || 100);
const OUT = process.argv[4] || path.join(__dirname, '..', 'runs', 's73-participation');
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
try {
  const P = Object.assign({}, H[E[env]], {years: 20, nAgents: 500});
  const row = (d, lf, x) => { const c = H.r2MainPair(P, d === 'none' ? 'c22' : d)[d === 'none' ? 0 : 1]; c.lf = Object.assign({}, lf); if (x) x(c); return c; };
  const ag = c => { c.ag = {}; }, flat = c => { c.o = Object.assign({}, c.o, {fin: 'tax'}); c.fx.fin = 'money'; c.gv = {sh: 1, base: 'w'}; };
  const L0 = {}, F = {fl: 'stock'}, M = {fl: 'stock', pm: 0.43}, L = [];
  [['L0', L0], ['F', F], ['M', M]].forEach(v => ['none', 'rel', 'c22'].forEach(d => L.push([v[0] + ' ' + d, row(d, v[1])])));
  [0.25, 0.7, 1].forEach(pm => ['rel', 'c22'].forEach(d => L.push(['pm' + pm + ' ' + d, row(d, {fl: 'stock', pm})])));
  [['agL0', L0], ['agP', {fl: 'panel', pm: 0.43}], ['agS', M]].forEach(v => ['none', 'rel', 'c22'].forEach(d => L.push([v[0] + ' ' + d, row(d, v[1], ag)])));
  L.push(['flatF c22', row('c22', F, flat)], ['flatM c22', row('c22', M, flat)]);
  const K = H.LF_KEYS.concat(H.LF_FLOW_KEYS, ['fgt0PY', 'pov', 'hrs', 'E', 'E0', 'emp', 'zero', 'endoAnn', 'tauMean', 'finGapSh', 'cost', 'gvTax', 'gvPay', 'wyF0PY'], Array.from({length: 20}, (_, t) => 'ppov_' + t));
  const pick = r => Object.fromEntries(K.map(k => [k, r._s[k] ? Array.from(r._s[k]) : null]));
  const R = H.tbStudy(L.map(x => x[1]), N, P, H.r2MainStudy());
  const PR = H.tbPresets(P), V = [['V base', F, 0], ['V ubi pm0', F, 12000], ['V ubi pm0.43', M, 12000], ['V ubi pm1', {fl: 'stock', pm: 1}, 12000]];
  const RV = H.tbStudy(V.map(v => { const c = row('none', v[1]); delete c.gv; if (v[2]) c.p = PR.ubi(v[2]); return c; }), N, P, Object.assign({}, H.r2MainStudy(), {fin: 'none'}));
  fs.mkdirSync(OUT, {recursive: true});
  const res = {env, seeds: N, manifest: H.runManifest(), command: 'node dev/tools/s73_pilot.js ' + process.argv.slice(2).join(' '), secs: (Date.now() - t0) / 1000,
    rows: L.map((x, i) => ({row: x[0], s: pick(R[i])})).concat(V.map((v, i) => ({row: v[0], s: pick(RV[i])})))};
  fs.writeFileSync(path.join(OUT, 's73-pilot-' + env + '.json'), JSON.stringify(res));
  console.log(env + ': done in ' + res.secs.toFixed(0) + ' s');
} finally { H.resetNR6(svN); H.tbSetG(svG); }
