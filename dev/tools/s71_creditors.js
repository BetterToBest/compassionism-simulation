#!/usr/bin/env node
/* S71 (Nov 13, 2026; research-update prereg/2026-11-s71-creditor-side.md): the pilot of the creditor side (option cr of rt): the households that hold
 * the other side of household fixed-rate debt lose what the debtors gain when inflation wipes the debt out.
 * The frozen release row and the C2.2 design, each against its own no-programme run on the same seeds (the rows of S59 and S66: frozenRow with today's
 * safety net and CPS earnings). Readings: main and chi1 (S59's main and no-debt-relief readings, cr off: they must equal S59's per-seed files), cr (the
 * creditor side, main: incidence 'pass', outside parts left outside, weighted totals), crhold and crhedge (the other incidence readings), crpop (the
 * model's families as the whole household sector), crall (nothing outside), cru (unweighted totals), r2 and r2cr (without the tail).
 * Per reading it keeps, per seed and row, the wealth and poverty measures, S57's distribution measures, RT_KEYS, WT_KEYS and CR_KEYS, and writes the
 * paired effects (programme minus no programme) with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates over seeds.
 * A pilot is a mechanism check at 100 seeds, not a result.
 * Usage: node dev/tools/s71_creditors.js ENV [SEEDS] [YEARS] [--rows=A,B] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years;
 *        writes dev/runs/s71-creditors/s71-creditors-ENV.json, per-seed values included) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now(), SN = {abawd: true, slope: true}, LT = {s: 'all', m: 'all'};  /* today's safety net and CPS earnings, as S66's rows */
const R2 = {bo: true, ci: true}, MN = {bo: true, ci: true, ng: 'base'}, X = (o, x) => Object.assign({}, o, x);
const CR = c => X(MN, {cr: c});
const ROWS = [['main', MN, true, null, 'S59 main: owners, capital income and the tail; no creditor side (bound 1)'], ['chi1', X(MN, {chi: 1}), true, null, 'S59: fixed-rate debt reprices too, no debt relief (bound 2)'],
  ['cr', CR(true), true, null, 'creditor side, main: bonds charged, deposits keep their pass-through, lenders\' shareholders take the rest; outside parts left outside'],
  ['crhold', CR({inc: 'hold'}), true, null, 'creditor side, holders of record: deposits that fund the debt are charged like bonds'],
  ['crhedge', CR({inc: 'hedge'}), true, null, 'creditor side, lenders\' shareholders not charged'],
  ['crpop', CR({pop: 1}), true, null, 'creditor side, the model\'s families as the whole household sector'],
  ['crall', CR({out: 0}), true, null, 'creditor side, nothing outside: every dollar of relief is lost by a household in the model'],
  ['cru', CR({w: 0}), true, null, 'creditor side, unweighted totals (no rule reads a weight)'],
  ['r2', R2, null, null, 'no tail, no creditor side'], ['r2cr', X(R2, {cr: true}), null, null, 'no tail, creditor side (main)']];
const ONLY = opt('rows') ? opt('rows').split(',') : null;
const KEYS = ['pov', 'fgt0PY', 'hhCostPY', 'endoAnn', 'pLev20', 'hhDebt20', 'bOAPy', 'giniD', 'eGiniW', 'eGiniWN', 'dmLsE', 'dmLsPY'];
const keep = k => KEYS.indexOf(k) >= 0 || /^rt/.test(k) || /^wt/.test(k) || /^cr/.test(k) || /^dm(Wt1|Wt10|Wb50|Yt1|Yt10|Yb50|Fd|Dm|Di)[SE]$/.test(k) || /^dmWp(10|25|50|75|90|99)[SE]$/.test(k) || /^dmYp(50|90|99)[SE]$/.test(k);
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function boot(x, y, B){  /* paired bootstrap of the mean difference over seeds (fixed generator, so the interval is reproducible) */
  const n = x.length, d = Array.from(x, (v, i) => v - y[i]), m = d.reduce((s, v) => s + v, 0)/n, r = H.mulberry32(20261112), b = [];
  for (let j = 0; j < B; j++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; b.push(s/n); }
  return {m, lo: q(b, 0.025), hi: q(b, 0.975)}; }
const r6 = v => +(+v).toPrecision(8), kf = (o, d, k) => (o.mean[d][k] === undefined ? NaN : o.mean[d][k]);
const out = {_meta: {what: 'S71: the creditor side pilot (research-update prereg/2026-11-s71-creditor-side.md)', creditor: H.RT_CR, env, seeds: N, years: YRS, rows: ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0),
  designs: ['none', 'rls', 'c22'], defaults: H.RT_DEFAULTS, tailDefaults: H.WT_DEFAULTS, tailCuts: H.WT_CUTS, frozen: H.FROZEN, manifest: H.runManifest(), command: 'node dev/tools/s71_creditors.js ' + process.argv.slice(2).join(' ')}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS, nAgents: 500}), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY, {dm: true, rep52: true, wtm: true});
  const pair = () => H.relMainCfgs(H.tbPresets(P)).map(c => Object.assign(c, {sc: H.SPEND_SOURCED, sn: SN, lt: JSON.parse(JSON.stringify(LT))})).map(c => H.frozenRow(c));
  ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0).forEach(function (row) {
    const cf = [pair()[0], pair()[1], H.c22Design(pair()[1])]; cf.forEach(c => { if (row[1]) c.rt = JSON.parse(JSON.stringify(row[1])); if (row[2]) c.wt = JSON.parse(JSON.stringify(row[2])); if (row[3] && c.sp) c.sp = Object.assign({}, c.sp, row[3]); });
    const R = H.tbStudy(cf, N, P, so), o = {label: row[4], rt: row[1], wt: row[2], sp: row[3], mean: {}, effect: {}, seeds: {}};
    ['none', 'rls', 'c22'].forEach((d, i) => { o.mean[d] = {}; o.seeds[d] = {};
      Object.keys(R[i]._s).filter(keep).forEach(k => { o.mean[d][k] = r6(R[i][k]); o.seeds[d][k] = Array.from(R[i]._s[k], r6); });
      if (i){ o.effect[d] = {}; Object.keys(R[i]._s).filter(keep).forEach(k => { if (R[0]._s[k]){ const b = boot(R[i]._s[k], R[0]._s[k], 2000); o.effect[d][k] = {m: r6(b.m), lo: r6(b.lo), hi: r6(b.hi)}; } }); } });
    out.rows[row[0]] = o;
    console.log(env, row[0], 'weighted wealth-poverty effect rls', o.effect.rls.wtPovE.m.toFixed(2), 'c22', o.effect.c22.wtPovE.m.toFixed(2), '| top 1% share effect rls', o.effect.rls.wtT1E.m.toFixed(2), 'c22', o.effect.c22.wtT1E.m.toFixed(2), '| relief, new charges, gap (rls)', kf(o, 'rls', 'crRel').toFixed(0), (kf(o, 'rls', 'crNom') + kf(o, 'rls', 'crEq')).toFixed(0), kf(o, 'rls', 'crGap').toExponential(1), ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's71-creditors', 's71-creditors-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
