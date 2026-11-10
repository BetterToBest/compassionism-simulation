#!/usr/bin/env node
/* S59 (Nov 10, 2026; research-update prereg/2026-11-s59-asset-classes.md and its Amendment 1): the asset-class pilot. The frozen release row and the C2.2
 * design, each against its own no-programme run on the same seeds (the rows of S66's erosion table: frozenRow with today's safety net and CPS earnings), with wealth held
 * as today (off: one number of dollars) and by asset class (switch RETURNS, row option rt): the main reading and one change at a time from it.
 * Per reading it keeps, per seed and row, the wealth and poverty measures, S57's distribution measures and RT_KEYS (real wealth in three parts), and
 * writes the paired effects (programme minus no programme) with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates over seeds.
 * A pilot is a mechanism check at 100 seeds, not a result.
 * Usage: node dev/tools/s59_assets.js ENV [SEEDS] [YEARS] [--rows=A,B] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years;
 *        writes dev/runs/s59-assets/s59-assets-ENV.json, per-seed values included) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now(), SN = {abawd: true, slope: true}, LT = {s: 'all', m: 'all'};  /* today's safety net and CPS earnings, as S66's rows */
const W83 = {home: 0.0181, ore: 0.0181, eq: 0.0571, bus: 0.0571}, W90 = {home: 0.0059, ore: 0.0059, eq: 0.0232, bus: 0.0232};  /* sources/s59_real_gains.json */
const ROWS = [['off', null, 'today: all wealth is one number of dollars'], ['main', true, 'by asset class, main reading'], ['phi0', {phi: 0}, 'nominal assets earn nothing'],
  ['phi1', {phi: 1}, 'nominal assets keep up with prices in full'], ['ix05', {ix: 0.5}, 'real assets follow half of inflation'], ['rho0', {rho: 0}, 'no real price gain'],
  ['rho83', {rho: W83}, 'real price gains of 1983-2022'], ['rho90', {rho: W90}, 'real price gains of 1890-2022'], ['port', {ns: 'port'}, 'new saving split by the group\'s asset shares'],
  ['chi1', {chi: 1}, 'fixed-rate debt reprices too (no debt relief)'], ['check', {all: 'nom', phi: 0, psi: 0}, 'check: every asset nominal, no pass-through (must equal off)']];
const ONLY = opt('rows') ? opt('rows').split(',') : null;
const KEYS = ['pov', 'fgt0PY', 'hhCostPY', 'endoAnn', 'pLev20', 'hhDebt20', 'bOAPy', 'giniD', 'eGiniW', 'eGiniWN'];
const keep = k => KEYS.indexOf(k) >= 0 || /^rt/.test(k) || /^dm(Wt1|Wt10|Wb50|Fd|Dm|Di)[SE]$/.test(k) || /^dmWp(10|25|50|75|90|99)[SE]$/.test(k);
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function boot(x, y, B){  /* paired bootstrap of the mean difference over seeds (fixed generator, so the interval is reproducible) */
  const n = x.length, d = Array.from(x, (v, i) => v - y[i]), m = d.reduce((s, v) => s + v, 0)/n, r = H.mulberry32(20261110), b = [];
  for (let j = 0; j < B; j++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; b.push(s/n); }
  return {m, lo: q(b, 0.025), hi: q(b, 0.975)}; }
const r6 = v => +(+v).toPrecision(8);
const out = {_meta: {what: 'S59: asset-class pilot (research-update prereg/2026-11-s59-asset-classes.md)', env, seeds: N, years: YRS, rows: ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0),
  designs: ['none', 'rls', 'c22'], defaults: H.RT_DEFAULTS, frozen: H.FROZEN, manifest: H.runManifest(), command: 'node dev/tools/s59_assets.js ' + process.argv.slice(2).join(' ')}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS, nAgents: 500}), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY, {dm: true, rep52: true});
  const pair = () => H.relMainCfgs(H.tbPresets(P)).map(c => Object.assign(c, {sc: H.SPEND_SOURCED, sn: SN, lt: JSON.parse(JSON.stringify(LT))})).map(c => H.frozenRow(c));
  ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0).forEach(function (row) {
    const cf = [pair()[0], pair()[1], H.c22Design(pair()[1])]; if (row[1]) cf.forEach(c => { c.rt = JSON.parse(JSON.stringify(row[1])); });
    const R = H.tbStudy(cf, N, P, so), o = {label: row[2], rt: row[1], mean: {}, effect: {}, seeds: {}};
    ['none', 'rls', 'c22'].forEach((d, i) => { o.mean[d] = {}; o.seeds[d] = {};
      Object.keys(R[i]._s).filter(keep).forEach(k => { o.mean[d][k] = r6(R[i][k]); o.seeds[d][k] = Array.from(R[i]._s[k], r6); });
      if (i){ o.effect[d] = {}; Object.keys(R[i]._s).filter(keep).forEach(k => { if (R[0]._s[k]){ const b = boot(R[i]._s[k], R[0]._s[k], 2000); o.effect[d][k] = {m: r6(b.m), lo: r6(b.lo), hi: r6(b.hi)}; } }); } });
    out.rows[row[0]] = o;
    console.log(env, row[0], 'pov effect rls', o.effect.rls.pov.m.toFixed(2), 'c22', o.effect.c22.pov.m.toFixed(2), '| median real wealth none/rls/c22', ['none', 'rls', 'c22'].map(d => Math.round(o.mean[d].dmWp50E)).join(' / '), ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
  if (out.rows.off && out.rows.check){ const bad = []; ['none', 'rls', 'c22'].forEach(d => Object.keys(out.rows.off.seeds[d]).forEach(k => { const a = out.rows.off.seeds[d][k], b = out.rows.check.seeds[d][k]; if (!b || a.some((v, i) => v !== b[i])) bad.push(d + '.' + k); }));
    out._meta.checkEqualsOff = bad.length === 0; out._meta.checkMoved = bad.slice(0, 20); console.log('check row equals off on every kept key: ' + (bad.length === 0)); }
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's59-assets', 's59-assets-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
