#!/usr/bin/env node
/* S62 (Nov 14, 2026; research-update prereg/2026-11-s62-ptf-realism.md): the pilot of PTF_OPS (row option po), PTF realism: sourced running costs and
 * who pays the gap (D19), PTF jobs and the conversion bonus on PTF workers, PTF wages by S60's wage setting, a hiring limit, and the density tests
 * (smooth curve, D20; what the tests read).
 * The frozen release row and the C2.2 design, each against its own no-programme run on the same seeds, on S60's rows (S71's rows: frozenRow, today's
 * safety net, CPS earnings, wealth by asset class with owners, capital income and the creditor side, the tail; adults outside the labour force) with
 * S60's wage setting at its main reading (bg pass-through 0) and S55's open access with growth (pa 'open').
 * Readings: open (no po); hub0 (po at the step-5 accounting, the bonus on members, the step, the tests on sales: must equal open); main (po main); hubSt
 * (the Hub's costs as stated); price (prices rise to running cost); sector (observed sector costs); res0 (no reserve); members (bonus on members); step
 * (the papers' wording); w10, w40 (the smooth band's half-width); tMem, tCap (what the tests read); hire5, hire2 (hiring limits); bg03 (main, pass-through
 * 0.03). Per reading it keeps, per seed and row, the poverty, wealth, price and cost measures, the weighted measures (wt*), PA_KEYS and PO_KEYS, and writes
 * the paired effects (programme minus no programme) with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates over seeds.
 * A pilot is a mechanism check at 100 seeds, not a result.
 * Usage: node dev/tools/s62_ptf_ops.js ENV [SEEDS] [YEARS] [--rows=A,B] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years;
 *        writes dev/runs/s62-ptf-ops/s62-ptf-ops-ENV.json, per-seed values included) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now(), SN = {abawd: true, slope: true}, LT = {s: 'all', m: 'all'};
const RT = {bo: true, ci: true, ng: 'base', cr: true}, MD = 1/1.21, BG = {pi: 0, m: MD};
const ID = {cost: 'full', res: 0, bonus: 'members', curve: 'step', test: 'sales'};
const ROWS = [['open', null, null, 'open access, no po (S55 main readings)'], ['hub0', ID, null, 'po at the step-5 accounting, bonus on members, the step, tests on sales: must equal open'],
  ['main', true, null, 'po main: full cost with the reserve, the Source pays the gap, bonus on PTF workers, smooth curve w 0.20, tests on sales'],
  ['hubSt', {cost: 'hub'}, null, 'the Hub\'s costs as stated (no gap)'], ['price', {pay: 'price'}, null, 'prices rise to full cost (no subsidy)'],
  ['sector', {cost: 'sector'}, null, 'observed sector costs'], ['res0', {res: 0}, null, 'no reserve'], ['members', {bonus: 'members'}, null, 'bonus on members (S55)'],
  ['step', {curve: 'step'}, null, 'the step at 40% (the papers\' wording)'], ['w10', {w: 0.10}, null, 'smooth band half-width 0.10'], ['w40', {w: 0.40}, null, 'smooth band half-width 0.40'],
  ['tMem', {test: 'members'}, null, 'tests read members\' share of adults'], ['tCap', {test: 'capacity'}, null, 'tests read the share of demand capacity can serve'],
  ['hire5', {hire: 0.05}, null, 'hiring limit 5 points a year (stress)'], ['hire2', {hire: 0.02}, null, 'hiring limit 2 points a year (stress)'],
  ['bg03', true, {pi: 0.03, m: MD}, 'po main with bargaining pass-through 0.03']];
const ONLY = opt('rows') ? opt('rows').split(',') : null;
const KEYS = ['pov', 'fgt0PY', 'hhCostPY', 'endoAnn', 'pLev20', 'hhDebt20', 'giniD', 'eGiniW', 'E', 'hrs', 'emp', 'medWealthReal', 'cost', 'cCut', 'csFree', 'cConv', 'cBU', 'pfCut', 'pfMem'];
const keep = k => KEYS.indexOf(k) >= 0 || /^po/.test(k) || /^pa/.test(k) || /^wt/.test(k) || /^bg/.test(k);
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function boot(x, y, B){ const n = x.length, d = Array.from(x, (v, i) => v - y[i]), m = d.reduce((s, v) => s + v, 0)/n, r = H.mulberry32(20261114), b = [];
  for (let j = 0; j < B; j++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; b.push(s/n); } return {m, lo: q(b, 0.025), hi: q(b, 0.975)}; }
const r6 = v => +(+v).toPrecision(8), kf = (o, d, k) => (o.mean[d][k] === undefined ? NaN : o.mean[d][k]);
const out = {_meta: {what: 'S62: PTF realism pilot (research-update prereg/2026-11-s62-ptf-realism.md)', env, seeds: N, years: YRS, rows: ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0),
  base: {rt: RT, wt: true, lf: {}, sn: SN, lt: LT, bg: BG, pa: 'open'}, defaults: H.PO_DEFAULTS, frozen: H.FROZEN, manifest: H.runManifest(), command: 'node dev/tools/s62_ptf_ops.js ' + process.argv.slice(2).join(' ')}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS, nAgents: 500}), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY, {dm: true, rep52: true, wtm: true});
  const base = c => { c.sc = H.SPEND_SOURCED; c.sn = SN; c.lt = JSON.parse(JSON.stringify(LT)); c.rt = JSON.parse(JSON.stringify(RT)); c.wt = true; c.lf = {}; c.bg = Object.assign({}, BG); c.pa = 'open'; return H.frozenRow(c); };
  const pair = () => H.relMainCfgs(H.tbPresets(P)).map(base);
  ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0).forEach(function (row) {
    const cf = [pair()[0], pair()[1], H.c22Design(pair()[1])]; cf.forEach(c => { if (row[1]) c.po = row[1] === true ? true : Object.assign({}, row[1]); if (row[2]) c.bg = Object.assign({}, row[2]); });
    const R = H.tbStudy(cf, N, P, so), o = {label: row[3], po: row[1], bg: row[2] || BG, mean: {}, effect: {}, seeds: {}};
    ['none', 'rls', 'c22'].forEach((d, i) => { o.mean[d] = {}; o.seeds[d] = {};
      Object.keys(R[i]._s).filter(keep).forEach(k => { o.mean[d][k] = r6(R[i][k]); o.seeds[d][k] = Array.from(R[i]._s[k], r6); });
      if (i){ o.effect[d] = {}; Object.keys(R[i]._s).filter(keep).forEach(k => { if (R[0]._s[k]){ const b = boot(R[i]._s[k], R[0]._s[k], 2000); o.effect[d][k] = {m: r6(b.m), lo: r6(b.lo), hi: r6(b.hi)}; } }); } });
    out.rows[row[0]] = o;
    console.log(env, row[0], 'wealth poverty rls', o.effect.rls.wtPovE.m.toFixed(2), 'c22', o.effect.c22.wtPovE.m.toFixed(2), '| basket poverty rls', o.effect.rls.fgt0PY.m.toFixed(2), 'c22', o.effect.c22.fgt0PY.m.toFixed(2),
      '| cost rls', kf(o, 'rls', 'cost').toFixed(0), '| subsidy rls', (kf(o, 'rls', 'poSub') || 0).toFixed(0), '(' + (kf(o, 'rls', 'poSubSh') || 0).toFixed(1) + '%) | PTF share', kf(o, 'rls', 'paSh').toFixed(1), '| eps', (kf(o, 'rls', 'poEpsF') || 0).toFixed(3), ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's62-ptf-ops', 's62-ptf-ops-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file + '.tmp', JSON.stringify(out)); fs.renameSync(file + '.tmp', file);
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
