#!/usr/bin/env node
/* S61 (Nov 9, 2026; research-update prereg/2026-11-s61-baseline-scope.md): the baseline-scope pilot. The frozen yardstick (frozenRow, CPS earnings,
 * today's safety net) with the debt reading's cap and floor readings and LF_SCOPE (adults outside the labour force), against S34's outside figures.
 * Per seed, at Year 0 and the last year, from the adults and their households (reporting hook only; nothing any rule reads): the S34 statistics
 * (dev/tools/baseline_realism.js), with adults outside the labour force counted among working-age adults (no earnings), plus, by reason, their own
 * official poverty, median net worth of their families and the share in debt. And the engine's own measures (fgt0PY, pov, hhCostPY, drHit, drCut, LF_KEYS).
 * --prog adds the C2.2 design on rows F0, DC, DF, L, LC (each paired with its own no-programme row) and writes the paired effects on fgt0PY, pov and
 * hhCostPY with the 2.5th-97.5th percentile interval of 2,000 paired bootstrap replicates over seeds (criterion C4; a mechanism check, not a result).
 * Usage: node dev/tools/s61_scope.js ENV [SEEDS] [YEARS] [--prog] [--rows=A,B] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years;
 *        writes dev/runs/s61-scope/s61-scope-ENV[-prog].json) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const PROG = process.argv.indexOf('--prog') >= 0, C = H.CFG, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const Y = {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}}, CAP = {lim: 2500}, FLR = {lim: 2500, fl: 'fpl'};
const ROWS = [['F0', {}], ['DC', {dr: CAP}], ['DF', {dr: FLR}], ['DC0', {dr: {lim: 0}}], ['DC5', {dr: {lim: 5000}}], ['DC87', {dr: {lim: 8700}}], ['DC10', {dr: {lim: 10000}}],
  ['DCL', {dr: {lim: 2500, liq: 0.046}}], ['L', {lf: {}}], ['LC', {lf: {}, dr: CAP}], ['LF', {lf: {}, dr: FLR}], ['LCn', {lf: {conv: 'none'}, dr: CAP}],
  ['F0age', {ag: {}}], ['LCage', {lf: {}, dr: CAP, ag: {}}]];
const PROW = ['F0', 'DC', 'DF', 'L', 'LC'], ONLY = opt('rows') ? opt('rows').split(',') : null;
const TYPES = {sg: 'single adult', sp: 'single parent', cn: 'couple without children', ck: 'couple with children'};
function q(a, p){ if (!a.length) return null; const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function gini(a){ const v = a.map(x => Math.max(0, x)).sort((x, y) => x - y), n = v.length; let t = 0, w = 0; for (let i = 0; i < n; i++){ t += v[i]; w += (i + 1)*v[i]; } return t > 0 ? (2*w/(n*t) - (n + 1)/n)*n/(n - 1) : 0; }
function pc(a, f){ return a.length ? a.filter(f).length/a.length*100 : null; }
function typeOf(Hh){ return Hh.a.length > 1 ? (Hh.kids.length ? 'ck' : 'cn') : (Hh.kids.length ? 'sp' : 'sg'); }
function snap(agents, lf){  /* one seed's statistics for one year (S34's, with adults outside the labour force among the working-age adults) */
  const work = agents.filter(a => !a._ret || a._lf), earn = work.map(a => a._lf ? 0 : (+a.yrWageUSD || 0)/lf), earners = earn.filter(x => x > 0), o = {};
  o.earnShare = pc(earn, x => x > 0); o.earnP10 = q(earners, 0.1); o.earnP25 = q(earners, 0.25); o.earnMed = q(earners, 0.5); o.earnP75 = q(earners, 0.75); o.earnP90 = q(earners, 0.9);
  o.earnGini = gini(earners);
  const seen = new Set(), hh = [];
  agents.forEach(a => { const Hh = a._hh; if (!Hh || seen.has(Hh)) return; seen.add(Hh);
    const inc = Hh.a.reduce((s, b) => s + H.tbCashIncome(b), 0)/lf, nw = Hh.a.reduce((s, b) => s + b.wealth, 0)/lf, k = Hh.a.length + 'a' + Math.min(4, Hh.kids.length) + 'k';
    hh.push({t: typeOf(Hh), nA: Hh.a.length, nK: Hh.kids.length, inc, nw, poor: inc < C.HH_FPL[k], lf: Hh.a.map(b => b._lf || null)}); });
  const per = (l, f, w) => { let n = 0, d = 0; l.forEach(h => { const m = w(h); d += m; if (f(h)) n += m; }); return d ? n/d*100 : null; };
  o.fplAdult = per(hh, h => h.poor, h => h.nA); o.fplKid = per(hh, h => h.poor, h => h.nK); o.fplAll = per(hh, h => h.poor, h => h.nA + h.nK);
  o.hhIncMed = q(hh.map(h => h.inc), 0.5); o.hhIncGini = gini(hh.map(h => h.inc));
  const W = l => ({n: l.length, median: q(l.map(h => h.nw), 0.5), neg: pc(l, h => h.nw < 0), below25k: pc(l, h => h.nw < 25000)});
  o.wealth = {all: W(hh)}; Object.keys(TYPES).forEach(t => { o.wealth[t] = W(hh.filter(h => h.t === t)); });
  o.lf = {share: pc(work, a => !!a._lf)};  /* adults outside the labour force, by reason: their own official poverty (the household's), family net worth, in debt */
  ['dis', 'ret', 'care', 'sch', null].forEach(r => { const l = []; hh.forEach(h => h.lf.forEach(x => { if (x === r) l.push(h); }));
    o.lf[r || 'inLF'] = {n: l.length, fpl: l.length ? pc(l, h => h.poor) : null, nwMed: q(l.map(h => h.nw), 0.5), neg: l.length ? pc(l, h => h.nw < 0) : null}; });
  return o; }
function summ(list){ const o = {}; Object.keys(list[0]).forEach(k => { const v = list.map(x => x[k]);
    if (v[0] !== null && typeof v[0] === 'object') { o[k] = summ(v); return; }
    const z = v.filter(x => typeof x === 'number' && isFinite(x)); o[k] = z.length ? {mean: z.reduce((s, x) => s + x, 0)/z.length, lo: q(z, 0.025), hi: q(z, 0.975)} : null; });
  return o; }
function boot(x, y, B){  /* paired bootstrap of the mean difference over seeds (fixed generator, so the interval is reproducible) */
  const n = x.length, d = Array.from(x, (v, i) => v - y[i]), m = d.reduce((s, v) => s + v, 0)/n, r = H.mulberry32(20261109), b = [];
  for (let j = 0; j < B; j++){ let s = 0; for (let i = 0; i < n; i++) s += d[Math.floor(r()*n)]; b.push(s/n); }
  return {m, lo: q(b, 0.025), hi: q(b, 0.975)}; }
const ENGK = ['fgt0PY', 'pov', 'bOAPy', 'hhCostPY', 'fgt2PY', 'giniD', 'emUrate', 'hhDebt20', 'drHit', 'drCut'].concat(H.LF_KEYS || []);
const out = {_meta: {what: 'S61: baseline scope pilot (research-update prereg/2026-11-s61-baseline-scope.md)', env, seeds: N, years: YRS, prog: PROG,
  rows: ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0).map(r => [r[0], r[1]]), yardstick: Y, frozen: H.FROZEN, manifest: H.runManifest(),
  command: 'node dev/tools/s61_scope.js ' + process.argv.slice(2).join(' ')}, rows: {}, prog: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY);
  const mk = (v, prog) => { const c = H.frozenRow(Object.assign(H.relMainCfgs(PR)[prog ? 1 : 0], Y, JSON.parse(JSON.stringify(v)))); return prog ? H.c22Design(c) : c; };
  ROWS.filter(r => !ONLY || ONLY.indexOf(r[0]) >= 0).forEach(function (row) {
    const S = {y0: [], end: []}, both = PROG && PROW.indexOf(row[0]) >= 0;
    H.setRepHook(function (agents, yr, T, lf) { const k = yr === 0 ? 'y0' : yr === T - 1 ? 'end' : null; if (k) S[k].push(snap(agents, lf)); });
    let R; try { R = H.tbStudy(both ? [mk(row[1], false), mk(row[1], true)] : [mk(row[1], false)], N, P, so); } finally { H.setRepHook(null); }
    const eng = {}; ENGK.forEach(k => { if (R[0][k] !== undefined) eng[k] = R[0][k]; });
    const pick = l => both ? l.filter((x, i) => i % 2 === 0) : l;  /* with --prog the hook sees the no-programme run, then the programme run, of each seed */
    out.rows[row[0]] = {engine: eng, y0: summ(pick(S.y0)), end: summ(pick(S.end)), seedsSeen: [pick(S.y0).length, pick(S.end).length]};
    if (both){ const e = {}; ['fgt0PY', 'pov', 'hhCostPY', 'bOAPy'].forEach(k => { if (R[0]._s[k]) e[k] = boot(R[1]._s[k], R[0]._s[k], 2000); }); out.prog[row[0]] = {effect: e, prog: Object.fromEntries(ENGK.filter(k => R[1][k] !== undefined).map(k => [k, R[1][k]]))}; }
    const r0 = out.rows[row[0]];
    console.log(env, row[0], 'debt y0/end', r0.y0.wealth.all.neg.mean.toFixed(1), r0.end.wealth.all.neg.mean.toFixed(1), 'earnShare', r0.y0.earnShare.mean.toFixed(1), 'fplAll', r0.y0.fplAll.mean.toFixed(1),
      both ? 'C2.2 fgt0PY ' + out.prog[row[0]].effect.fgt0PY.m.toFixed(2) : '', ((Date.now() - t0)/1000).toFixed(0) + ' s');
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's61-scope', 's61-scope-' + env + (PROG ? '-prog' : '') + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out, null, 1));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
