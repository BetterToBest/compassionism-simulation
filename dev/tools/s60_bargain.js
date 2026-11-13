#!/usr/bin/env node
/* S60 (Nov 13, 2026; research-update prereg/2026-11-s60-bargaining-power.md): the pilot of BARGAIN (row option bg), a worker's outside option and an
 * employer markdown, in reduced form.
 * The frozen release row and the C2.2 design, each against its own no-programme run on the same seeds, on S71's rows (frozenRow with today's safety net
 * and CPS earnings; wealth by asset class with owners, capital income and the creditor side; the tail) with adults outside the labour force (lf).
 * Readings: off (no bg); bg0 (pi 0, m 1/1.21: must equal off); bg03 (pi 0.03, Jager et al.'s bound); bg10 (0.10, Vivalt et al.'s bound); nash24 and nash48
 * (the Nash benchmarks the evidence rejects); nash48y (0.48 with Yeh et al.'s markdown, m 1/1.53); nash48n (0.48 with no markdown, m 1: must equal off).
 * Per reading it keeps, per seed and row, the poverty, wealth, labour and price measures, the weighted measures (wt*) and BG_KEYS, and writes the paired
 * effects (programme minus no programme) with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates over seeds.
 * --validate: the check against Vivalt et al. (no programme; $12,000 a year to every adult, unfinanced, against nothing; 3 years; the same base row):
 *   rows base (no transfer), ubi (bg off), and ubi under each pass-through.
 * A pilot is a mechanism check at 100 seeds, not a result.
 * Usage: node dev/tools/s60_bargain.js ENV [SEEDS] [YEARS] [--rows=A,B] [--out=FILE] [--validate]   (ENV ref, adv or st; default 100 seeds, 20 years;
 *        writes dev/runs/s60-bargain/s60-bargain-ENV.json, or s60-validate-ENV.json, per-seed values included) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const VAL = process.argv.indexOf('--validate') >= 0;
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || (VAL ? 3 : 20)), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now(), SN = {abawd: true, slope: true}, LT = {s: 'all', m: 'all'};  /* today's safety net and CPS earnings, as S71's rows */
const RT = {bo: true, ci: true, ng: 'base', cr: true}, MD = 1/1.21, MY = 1/1.53;
const ROWS = [['off', null, 'no bargaining (S71 main row with adults outside the labour force)'], ['bg0', {pi: 0, m: MD}, 'pass-through 0 (the central estimate): must equal off'],
  ['bg03', {pi: 0.03, m: MD}, 'pass-through 0.03 (Jager et al.: larger ruled out)'], ['bg10', {pi: 0.10, m: MD}, 'pass-through 0.10 (Vivalt et al.: hourly pay above +$0.58 ruled out)'],
  ['nash24', {pi: 0.24, m: MD}, 'pass-through 0.24 (Nash benchmark with finite benefits; rejected by the evidence)'], ['nash48', {pi: 0.48, m: MD}, 'pass-through 0.48 (basic Nash benchmark; rejected by the evidence)'],
  ['nash48y', {pi: 0.48, m: MY}, 'pass-through 0.48, markdown 1.53 (Yeh et al.)'], ['nash48n', {pi: 0.48, m: 1}, 'pass-through 0.48, no markdown: must equal off']];
const VROWS = [['base', null, null, 'no transfer'], ['ubi', 12000, null, '$12,000 a year to every adult, no bargaining'], ['ubi03', 12000, {pi: 0.03, m: MD}, 'with pass-through 0.03'],
  ['ubi10', 12000, {pi: 0.10, m: MD}, 'with pass-through 0.10'], ['ubi24', 12000, {pi: 0.24, m: MD}, 'with pass-through 0.24'], ['ubi48', 12000, {pi: 0.48, m: MD}, 'with pass-through 0.48']];
const ONLY = opt('rows') ? opt('rows').split(',') : null;
const KEYS = ['pov', 'fgt0PY', 'hhCostPY', 'endoAnn', 'pLev20', 'hhDebt20', 'giniD', 'eGiniW', 'eGiniWN', 'E', 'E0', 'Er', 'dE', 'hrs', 'emp', 'zero', 'medWealthReal', 'dmLsE', 'dmLsPY', 'cost'];
const keep = k => KEYS.indexOf(k) >= 0 || /^bg/.test(k) || /^wt/.test(k) || /^lf/.test(k) || /^dm(Wt1|Wt10|Wb50|Yt1|Yt10|Yb50)[SE]$/.test(k) || /^dmYp(10|50|90)[SE]$/.test(k);
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function boot(x, y, B){  /* paired bootstrap of the mean difference over seeds (fixed generator, so the interval is reproducible) */
  const n = x.length, d = Array.from(x, (v, i) => v - y[i]), m = d.reduce((s, v) => s + v, 0)/n, r = H.mulberry32(20261113), b = [];
  for (let j = 0; j < B; j++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; b.push(s/n); }
  return {m, lo: q(b, 0.025), hi: q(b, 0.975)}; }
const r6 = v => +(+v).toPrecision(8), kf = (o, d, k) => (o.mean[d][k] === undefined ? NaN : o.mean[d][k]);
const out = {_meta: {what: 'S60: bargaining power pilot (research-update prereg/2026-11-s60-bargaining-power.md)' + (VAL ? ', validation against Vivalt et al.' : ''), env, seeds: N, years: YRS,
  rows: (VAL ? VROWS : ROWS).filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0), base: {rt: RT, wt: true, lf: {}, sn: SN, lt: LT}, defaults: H.BG_DEFAULTS, frozen: H.FROZEN, manifest: H.runManifest(),
  command: 'node dev/tools/s60_bargain.js ' + process.argv.slice(2).join(' ')}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS, nAgents: 500}), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY, {dm: true, rep52: true, wtm: true});
  const base = c => { c.sc = H.SPEND_SOURCED; c.sn = SN; c.lt = JSON.parse(JSON.stringify(LT)); c.rt = JSON.parse(JSON.stringify(RT)); c.wt = true; c.lf = {}; return H.frozenRow(c); };
  const pair = () => H.relMainCfgs(H.tbPresets(P)).map(base);
  if (VAL){
    const sv = Object.assign({}, so, {fin: 'none'}), PR = H.tbPresets(P), rows = VROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0);
    const cf = rows.map(r => { const c = pair()[0]; if (r[1]) c.p = PR.ubi(r[1]); if (r[2]) c.bg = Object.assign({}, r[2]); return c; }), R = H.tbStudy(cf, N, P, sv);
    rows.forEach((r, i) => { const o = {label: r[3], ubi: r[1], bg: r[2], mean: {}, seeds: {}, effect: {}};
      Object.keys(R[i]._s).filter(keep).forEach(k => { o.mean[k] = r6(R[i][k]); o.seeds[k] = Array.from(R[i]._s[k], r6); if (i && R[0]._s[k]){ const b = boot(R[i]._s[k], R[0]._s[k], 2000); o.effect[k] = {m: r6(b.m), lo: r6(b.lo), hi: r6(b.hi)}; } });
      out.rows[r[0]] = o; if (i) console.log(env, r[0], 'earnings per adult-year', o.effect.E.m.toFixed(0), 'per dollar', (o.effect.E.m/r[1]).toFixed(3), '| adults with earnings (points)', o.effect.emp.m.toFixed(2), '| hours', o.effect.hrs.m.toFixed(4), '| bargained raise a year', (o.mean.bgR || 0).toFixed(0), ((Date.now() - t0)/1000).toFixed(0) + ' s'); });
  } else ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0).forEach(function (row) {
    const cf = [pair()[0], pair()[1], H.c22Design(pair()[1])]; cf.forEach(c => { if (row[1]) c.bg = Object.assign({}, row[1]); });
    const R = H.tbStudy(cf, N, P, so), o = {label: row[2], bg: row[1], mean: {}, effect: {}, seeds: {}};
    ['none', 'rls', 'c22'].forEach((d, i) => { o.mean[d] = {}; o.seeds[d] = {};
      Object.keys(R[i]._s).filter(keep).forEach(k => { o.mean[d][k] = r6(R[i][k]); o.seeds[d][k] = Array.from(R[i]._s[k], r6); });
      if (i){ o.effect[d] = {}; Object.keys(R[i]._s).filter(keep).forEach(k => { if (R[0]._s[k]){ const b = boot(R[i]._s[k], R[0]._s[k], 2000); o.effect[d][k] = {m: r6(b.m), lo: r6(b.lo), hi: r6(b.hi)}; } }); } });
    out.rows[row[0]] = o;
    console.log(env, row[0], 'weighted wealth-poverty effect rls', o.effect.rls.wtPovE.m.toFixed(2), 'c22', o.effect.c22.wtPovE.m.toFixed(2), '| basket poverty rls', o.effect.rls.fgt0PY.m.toFixed(2), 'c22', o.effect.c22.fgt0PY.m.toFixed(2),
      '| bargained raise per worker-year rls', kf(o, 'rls', 'bgR').toFixed(0), 'c22', kf(o, 'c22', 'bgR').toFixed(0), '| share of raises', kf(o, 'rls', 'bgSh').toFixed(1), kf(o, 'c22', 'bgSh').toFixed(1), ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's60-bargain', (VAL ? 's60-validate-' : 's60-bargain-') + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file + '.tmp', JSON.stringify(out)); fs.renameSync(file + '.tmp', file);
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
