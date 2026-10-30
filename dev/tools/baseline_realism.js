#!/usr/bin/env node
/* S34 (Oct 30, 2026; preregistration research-update prereg/s34-baseline-realism.md): the release's no-programme run against outside data.
 * Rows: 'sn', the v5.6 release's no-programme run (relMainCfgs(PR)[0], with today's safety net, SNAP's work rule and the slope reading: the release panel's
 * --v54 --snab --slope); 'none', the same without today's safety net. Run as the release runs them (NR6 profile, TB_PROFILE_G, fin 'tax', v5.2 reporting).
 * At Year 0 and the last year, per seed, from the adults and their households (reporting hook only; nothing any rule reads):
 *  - earnings of working-age adults (pay in the year, today's dollars): share with earnings, percentiles, Gini among earners;
 *  - household money income (the official measure's: pay, conversion, cash transfers, Social Security, unemployment insurance; not SNAP or tax credits):
 *    median and Gini across households;
 *  - official poverty: persons in households whose money income is below the Census 2025 threshold for the household's size and children (CFG.HH_FPL),
 *    moved with the price level: adults, children, everyone;
 *  - household net worth (today's dollars): median, share in debt, share below $25,000, overall and by household type.
 * And from the engine's own results: the share of adult-years out of work (emUrate), the safety net's recipiency and dollars (SN_KEYS), and the release's
 * headline measures (to check that the 'sn' row reproduces the release panel's no-programme figures).
 * Figures are the mean over seeds of each seed's statistic, with the 2.5th and 97.5th percentiles over seeds.
 *
 * --explore adds exploratory rows (the CPS and SCF wage readings, ageing; prereg amendment of Oct 30) and writes ...-ENV-explore.json.
 * Usage: node dev/tools/baseline_realism.js ENV [SEEDS] [YEARS] [--explore] [--out=FILE]   (ENV ref, adv or st; default 500 seeds, 20 years;
 *        writes dev/runs/baseline-realism/baseline-realism-ENV.json unless --out) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), OUTA = process.argv.filter(a => /^--out=/.test(a))[0];
const env = ARG[0] || 'ref', N = +(ARG[1] || 500), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const C = H.CFG, SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const SN = {abawd: true, slope: true};
const EXPLORE = process.argv.indexOf('--explore') >= 0;  /* exploratory rows, added after the first results (prereg amendment, Oct 30): readings that might close the gaps */
const ROWS = [['sn', {sn: SN}], ['none', {}]].concat(EXPLORE ? [['snCpsAll', {sn: SN, lt: {s: 'all', m: 'all'}}], ['snCpsFt', {sn: SN, lt: {s: 'ft', m: 'ft'}}],
  ['snScf', {sn: SN, lt: {s: 1, m: 1}}], ['snAge', {sn: SN, ag: {}}], ['snCpsAllAge', {sn: SN, lt: {s: 'all', m: 'all'}, ag: {}}]] : []);
const TYPES = {sg: 'single adult', sp: 'single parent', cn: 'couple without children', ck: 'couple with children'};
function q(a, p){ if (!a.length) return null; const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function gini(a){ const v = a.map(x => Math.max(0, x)).sort((x, y) => x - y), n = v.length; let t = 0, w = 0; for (let i = 0; i < n; i++){ t += v[i]; w += (i + 1)*v[i]; } return t > 0 ? (2*w/(n*t) - (n + 1)/n)*n/(n - 1) : 0; }
function pc(a, f){ return a.length ? a.filter(f).length/a.length*100 : null; }
function typeOf(Hh){ return Hh.a.length > 1 ? (Hh.kids.length ? 'ck' : 'cn') : (Hh.kids.length ? 'sp' : 'sg'); }
function snap(agents, lf){  /* one seed's statistics for one year */
  const work = agents.filter(a => !a._ret), earn = work.map(a => (+a.yrWageUSD || 0)/lf), earners = earn.filter(x => x > 0), o = {};
  o.earnShare = pc(earn, x => x > 0); o.earnP10 = q(earners, 0.1); o.earnP25 = q(earners, 0.25); o.earnMed = q(earners, 0.5); o.earnP75 = q(earners, 0.75); o.earnP90 = q(earners, 0.9);
  o.earnMean = earners.reduce((s, x) => s + x, 0)/earners.length; o.earnGini = gini(earners);
  const seen = new Set(), hh = [];
  agents.forEach(a => { const Hh = a._hh; if (!Hh || seen.has(Hh)) return; seen.add(Hh);
    const inc = Hh.a.reduce((s, b) => s + H.tbCashIncome(b), 0)/lf, nw = Hh.a.reduce((s, b) => s + b.wealth, 0)/lf, k = Hh.a.length + 'a' + Math.min(4, Hh.kids.length) + 'k';
    hh.push({t: typeOf(Hh), nA: Hh.a.length, nK: Hh.kids.length, inc, nw, poor: inc < C.HH_FPL[k]}); });
  const per = (f, w) => { let n = 0, d = 0; hh.forEach(h => { const m = w(h); d += m; if (f(h)) n += m; }); return d ? n/d*100 : null; };
  o.fplAdult = per(h => h.poor, h => h.nA); o.fplKid = per(h => h.poor, h => h.nK); o.fplAll = per(h => h.poor, h => h.nA + h.nK);
  o.hhIncMed = q(hh.map(h => h.inc), 0.5); o.hhIncGini = gini(hh.map(h => h.inc));
  const W = l => ({n: l.length, median: q(l.map(h => h.nw), 0.5), neg: pc(l, h => h.nw < 0), below25k: pc(l, h => h.nw < 25000)});
  o.wealth = {all: W(hh)}; Object.keys(TYPES).forEach(t => { o.wealth[t] = W(hh.filter(h => h.t === t)); });
  o.hhShare = {}; Object.keys(TYPES).forEach(t => { o.hhShare[t] = pc(hh, h => h.t === t); });
  o.adults = agents.length; o.kids = hh.reduce((s, h) => s + h.nK, 0); return o; }
function summ(list){  /* mean over seeds and the 2.5th-97.5th percentile band, for every numeric leaf */
  const o = {}; Object.keys(list[0]).forEach(k => { const v = list.map(x => x[k]);
    if (v[0] !== null && typeof v[0] === 'object') { o[k] = summ(v); return; }
    const z = v.filter(x => typeof x === 'number' && isFinite(x)); o[k] = z.length ? {mean: z.reduce((s, x) => s + x, 0)/z.length, lo: q(z, 0.025), hi: q(z, 0.975)} : null; });
  return o; }
const out = {_meta: {what: 'S34: the release no-programme run against outside data (prereg/s34-baseline-realism.md in research-update)', env, seeds: N, years: YRS,
  sn: Object.assign({}, H.SNET_DEFAULTS, SN), manifest: H.runManifest(), command: 'node dev/tools/baseline_realism.js ' + env + ' ' + N + ' ' + YRS + (EXPLORE ? ' --explore' : '')}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY);
  ROWS.forEach(function (row) {
    const S = {y0: [], end: []};
    H.setRepHook(function (agents, yr, T, lf) { const k = yr === 0 ? 'y0' : yr === T - 1 ? 'end' : null; if (k) S[k].push(snap(agents, lf)); });
    let R; try { R = H.tbStudy([Object.assign(H.relMainCfgs(PR)[0], {sc: SC}, row[1])], N, P, so)[0]; } finally { H.setRepHook(null); }
    const eng = {}; ['fgt0PY', 'pov', 'bOAPy', 'fgt2PY', 'giniD', 'medWealth', 'emUrate', 'emSpells', 'emWeeks', 'emUI', 'emLong', 'y0Fpl', 'y7Fpl', 'eFpl', 'hhFplPY', 'hhFplKidPY', 'hhFpl7', 'hhFplEnd', 'hhFplKidEnd',
      'hhCostPY', 'hhWlthEnd', 'y0FplX', 'eFplX', 'y0F0', 'eF0', 'y0GiniD', 'eGiniD', 'y0Pov', 'ePov'].concat(H.SN_KEYS, H.SN_AB_KEYS).forEach(k => { if (R[k] !== undefined) eng[k] = R[k]; });
    out.rows[row[0]] = {engine: eng, y0: summ(S.y0), end: summ(S.end), seedsSeen: [S.y0.length, S.end.length]};
    console.log(env, row[0], 'fgt0PY', R.fgt0PY, 'pov', R.pov, 'emUrate', R.emUrate, 'earnMed y0', out.rows[row[0]].y0.earnMed.mean, 'fplAll y0', out.rows[row[0]].y0.fplAll.mean, ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = OUTA ? OUTA.slice(6) : path.join(__dirname, '..', 'runs', 'baseline-realism', 'baseline-realism-' + env + (EXPLORE ? '-explore' : '') + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out, null, 1));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
