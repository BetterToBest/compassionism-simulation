#!/usr/bin/env node
/* S59, part 2 (Nov 12, 2026; research-update prereg/2026-11-s59-tail-returns.md): the pilot of the weighted top tail (switch WEALTH_TAIL, row option wt),
 * business owners and the income wealth pays (options bo, ci of rt), the returns gradients (ng, rg) and the owners rule (surplus-split option own).
 * The frozen release row and the C2.2 design, each against its own no-programme run on the same seeds (the rows of part 1 and of S66: frozenRow with
 * today's safety net and CPS earnings). Readings: off (all wealth is cash), p1 (part 1's main reading, corrected edges), r2 (p1 with owners and capital
 * income), main (r2 with the tail), and one change at a time from main; the owners readings run without the tail (weights enter measures only).
 * Per reading it keeps, per seed and row, the wealth and poverty measures, S57's distribution measures, RT_KEYS and WT_KEYS (the weighted measures, kept
 * for every row through the study option wtm), and writes the paired effects (programme minus no programme) with the 2.5th-97.5th percentile interval
 * of 2,000 paired bootstrap replicates over seeds. A pilot is a mechanism check at 100 seeds, not a result.
 * Usage: node dev/tools/s59_tail.js ENV [SEEDS] [YEARS] [--rows=A,B] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years;
 *        writes dev/runs/s59-tail/s59-tail-ENV.json, per-seed values included) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now(), SN = {abawd: true, slope: true}, LT = {s: 'all', m: 'all'};  /* today's safety net and CPS earnings, as S66's rows */
const R2 = {bo: true, ci: true}, MN = {bo: true, ci: true, ng: 'base'}, X = (o, x) => Object.assign({}, o, x);
const ROWS = [['off', null, null, null, 'all wealth is one number of dollars'], ['p1', true, null, null, 'part 1: by asset class (corrected group edges)'],
  ['p1chi', {chi: 1}, null, null, 'part 1 with fixed-rate debt repricing (no debt relief)'], ['r2', R2, null, null, 'part 1 with business owners and capital income'],
  ['main', MN, true, null, 'main: owners, capital income and the tail (3 per type, Pareto, cutoff by the rule)'], ['tailonly', true, true, null, 'part 1 with the tail only'],
  ['a135', MN, {a: 1.354}, null, 'tail exponent one standard error lower (1.354: a heavier tail)'], ['a163', MN, {a: 1.626}, null, 'tail exponent one standard error higher (1.626)'],
  ['p99', MN, {cut: 'p99'}, null, 'cutoff at the 99th percentile (exponent 1.576)'], ['gpd', MN, {form: 'gpd'}, null, 'generalised Pareto above the main cutoff'],
  ['gpd90', MN, {form: 'gpd', cut: 'p90'}, null, 'generalised Pareto from the 90th percentile'], ['m1', MN, {m: 1}, null, '1 tail household per type'], ['m6', MN, {m: 6}, null, '6 tail households per type'],
  ['ng0', R2, true, null, 'no interest gradient at the very top'], ['ngall', X(MN, {ng: 'all'}), true, null, 'interest gradient on the inflation pass-through too'],
  ['rg', X(MN, {rg: true}), true, null, 'higher real-estate gains for the top group'], ['bo0', {ci: true, ng: 'base'}, true, null, 'no business-owner split (group averages)'],
  ['ci0', {bo: true, ng: 'base'}, true, null, 'no capital income'], ['chi1', X(MN, {chi: 1}), true, null, 'fixed-rate debt reprices too (no debt relief)'],
  ['ix05', X(MN, {ix: 0.5}), true, null, 'real assets follow half of inflation'], ['ownW', R2, null, {priv: 'owners'}, 'owners keep the private premium, shared by positive wealth (no tail)'],
  ['ownE', R2, null, {priv: 'owners', own: 'eq'}, 'owners keep the private premium, shared by shares and business equity (no tail)'],
  ['flat', true, {flat: true}, null, 'check: the tail with every weight 1 and no change of wealth (must equal p1)']];
const ONLY = opt('rows') ? opt('rows').split(',') : null;
const KEYS = ['pov', 'fgt0PY', 'hhCostPY', 'endoAnn', 'pLev20', 'hhDebt20', 'bOAPy', 'giniD', 'eGiniW', 'eGiniWN', 'dmLsE', 'dmLsPY'];
const keep = k => KEYS.indexOf(k) >= 0 || /^rt/.test(k) || /^wt/.test(k) || /^dm(Wt1|Wt10|Wb50|Yt1|Yt10|Yb50|Fd|Dm|Di)[SE]$/.test(k) || /^dmWp(10|25|50|75|90|99)[SE]$/.test(k) || /^dmYp(50|90|99)[SE]$/.test(k);
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function boot(x, y, B){  /* paired bootstrap of the mean difference over seeds (fixed generator, so the interval is reproducible) */
  const n = x.length, d = Array.from(x, (v, i) => v - y[i]), m = d.reduce((s, v) => s + v, 0)/n, r = H.mulberry32(20261112), b = [];
  for (let j = 0; j < B; j++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; b.push(s/n); }
  return {m, lo: q(b, 0.025), hi: q(b, 0.975)}; }
const r6 = v => +(+v).toPrecision(8);
const out = {_meta: {what: 'S59 part 2: tail, owners and capital income pilot (research-update prereg/2026-11-s59-tail-returns.md)', env, seeds: N, years: YRS, rows: ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0),
  designs: ['none', 'rls', 'c22'], defaults: H.RT_DEFAULTS, tailDefaults: H.WT_DEFAULTS, tailCuts: H.WT_CUTS, frozen: H.FROZEN, manifest: H.runManifest(), command: 'node dev/tools/s59_tail.js ' + process.argv.slice(2).join(' ')}, rows: {}};
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
    console.log(env, row[0], 'weighted wealth-poverty effect rls', o.effect.rls.wtPovE.m.toFixed(2), 'c22', o.effect.c22.wtPovE.m.toFixed(2), '| top 1% share start', o.mean.none.wtT1S.toFixed(1), 'end none/rls/c22', ['none', 'rls', 'c22'].map(d => o.mean[d].wtT1E.toFixed(1)).join(' / '), ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
  if (out.rows.p1 && out.rows.flat){ const bad = []; ['none', 'rls', 'c22'].forEach(d => Object.keys(out.rows.p1.seeds[d]).forEach(k => { const a = out.rows.p1.seeds[d][k], b = out.rows.flat.seeds[d][k]; if (!b || a.some((v, i) => v !== b[i])) bad.push(d + '.' + k); }));
    out._meta.checkEqualsOff = bad.length === 0; out._meta.checkMoved = bad.slice(0, 20); console.log('check row (flat) equals p1 on every kept key: ' + (bad.length === 0)); }
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's59-tail', 's59-tail-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
