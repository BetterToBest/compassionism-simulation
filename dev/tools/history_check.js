#!/usr/bin/env node
/* Session 9 (Oct 14, 2026; ledger s146; dev/plans/s146-history-check.md, the rules fixed before any run; dev/reports/v5-34-history-check.md): THE HISTORY CHECK.
 * A rough shape check, not a calibration: the v5.4 no-programme run (Reference Environment), without and with today's safety net, goes through two real
 * shocks, 2008-2012 and 2020-2021, as one scripted recession path (index.html, REC_SCRIPT: the same path for every seed and both arms, no draw added), and
 * each seed is paired with the same run without any recession. The model's figure for a year is "shock minus no shock" in that year's share of adults
 * below the cost-of-living basket (basket poverty); the data's is the change from the year before the shock. Changes are compared, never levels (the start
 * population is built from 2022 data). No constant is fitted to the history.
 * The scripted path (rule (a) of the plan, fixed in writing before any output): in each year after the base year, the income multiplier is the real median
 * household income of that year over the base year's (sources/history/history_series.json, macro.real_median_household_income); the recession flag is on
 * in every year the multiplier is below 1, so the engine's own recession job-loss rates apply then, and (rule 'replace') the income cut is reduced by the
 * extra job loss, so the year's whole loss is the median income's fall. Outside inflation stays the environment's own (0 at Reference).
 * Arms: no safety net (Columbia's rate before taxes and transfers is the comparator; unemployment insurance stays in both arms, as in the engine) and
 * today's safety net (SNAP, EITC, refundable CTC; SNET.slope on, as in the s165 study; SNAP's work rule off: it was suspended nationwide in 2009-2010).
 * Usage: node dev/tools/history_check.js [--seeds=500] [--engine=DIR] [--series=FILE] [--out=FILE]
 *   --engine: the directory whose harness.js runs (default this repository); it must have REC_SCRIPT (harness setRecScript).
 *   --out: default dev/runs/history/history-check.json. Prints the comparison table with the verdicts. */
'use strict';
const fs = require('fs'), path = require('path');
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : null; };
const ROOT = path.join(__dirname, '..', '..'), N = +(arg('seeds') || 500), ENG = path.resolve(arg('engine') || ROOT);
const SER = path.resolve(arg('series') || path.join(ROOT, 'sources', 'history', 'history_series.json')), OUT = path.resolve(arg('out') || path.join(ROOT, 'dev', 'runs', 'history', 'history-check.json'));
const H = require(path.join(ENG, 'harness.js'));
if (typeof H.setRecScript !== 'function'){ console.error('history_check.js: ' + ENG + '/harness.js has no setRecScript (the engine needs REC_SCRIPT)'); process.exit(1); }
const D = JSON.parse(fs.readFileSync(SER, 'utf8')), M = D.macro, inc = M.real_median_household_income;
const off = D.official.rate.all, col = D.spm_columbia_2005_2012, spmC = D.spm_census.rate.all;
const EPIS = {rec: {base: 2007, last: 2012}, c20: {base: 2019, last: 2021}};
const r2 = x => +(+x).toFixed(2), r3 = x => +(+x).toFixed(3);
function script(e){ const s = [{active: false, incomeMultiplier: 1}];
  for (let y = e.base + 1; y <= e.last; y++){ const m = inc[y]/inc[e.base]; s.push({active: m < 1, incomeMultiplier: Math.min(1, m)}); } return s; }
function stat(v){ const n = v.length, s = Array.from(v).sort((a, b) => a - b), q = p => s[Math.min(n - 1, Math.max(0, Math.round(p*(n - 1))))];
  return {mean: r3(v.reduce((a, b) => a + b, 0)/n), p5: r3(q(0.05)), p95: r3(q(0.95))}; }

const C = H.CFG, SC = H.SPEND_SOURCED, t0 = Date.now(), wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), out = {_meta: {what: 'the history check (ledger s146): the v5.4 no-programme run at Reference, without and with today\'s safety net, through a scripted 2008-2012 recession and 2020-2021, each seed paired with the same run without a recession; figures are shock minus no shock, percentage points of adults below the cost-of-living basket', seeds: N, command: 'node dev/tools/history_check.js ' + process.argv.slice(2).join(' '), series: path.relative(ROOT, SER), engine: ENG, manifest: H.runManifest(), rule: 'income multiplier = real median household income / base year; recession flag where below 1'}, episodes: {}};
let sv0 = null;
try {
  Object.keys(EPIS).forEach(k => {
    const e = EPIS[k], T = e.last - e.base + 1, P = Object.assign({}, H.FULL_INTEGRATION, {years: T, shock: true}), PR = H.tbPresets(P);
    const base = {sc: SC, so: H.REL_V52_STUDY, hh: H.REL_V53.hh, sg: true, g: H.ACCT_V53, em: true, fb: true, v54: H.REL_V54.v54};
    const cfg = [Object.assign({p: PR.baseline()}, base), Object.assign({p: PR.baseline()}, base, {sn: {slope: true}})], arms = ['noSN', 'SN'];
    const o = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0}, H.REL_V52_STUDY, {sc: SC}), sc = script(e), R = {};
    sv0 = H.setRecScript(sc); R.shock = H.tbStudy(cfg, N, P, o);
    H.setRecScript([]); R.calm = H.tbStudy(cfg, N, P, o); H.setRecScript(sv0); sv0 = null;
    const E = out.episodes[k] = {years: [], script: sc, model: {}, data: {}};
    for (let t = 0; t < T; t++) E.years.push(e.base + t);
    arms.forEach((a, i) => { const m = E.model[a] = {basket: [], wealth: [], basketLevelCalm: []};
      for (let t = 0; t < T; t++){ const S = R.shock[i]._s, Cm = R.calm[i]._s, d = [], w = [];
        for (let j = 0; j < N; j++){ d.push(S['pf0_' + t][j] - Cm['pf0_' + t][j]); w.push(S['ppov_' + t][j] - Cm['ppov_' + t][j]); }
        m.basket.push(stat(d)); m.wealth.push(stat(w)); m.basketLevelCalm.push(r2(R.calm[i]['pf0_' + t])); }
    });
    const rise = (s, y) => s && s[y] !== undefined && s[e.base] !== undefined ? r2(s[y] - s[e.base]) : null;
    E.years.forEach(y => { E.data[y] = {official: rise(off, y), spmColumbia: rise(col.historical_SPM_rate.all, y), beforeTransfers: rise(col.historical_SPM_rate_before_transfers.all, y), spmCensus: rise(spmC, y), unemployment: M.unemployment_rate_annual_avg[y], incomeMultiplier: r3(inc[y]/inc[e.base])}; });
  });
} finally { if (sv0 !== null) H.setRecScript(sv0); H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }

/* The comparisons of the plan's section 4, with the verdict bands fixed there (comparison 6 as amended there before any run). */
const R1 = out.episodes.rec, Y = R1.years, sn = R1.model.SN.basket.map(x => x.mean), ns = R1.model.noSN.basket.map(x => x.mean), at = y => Y.indexOf(y);
const peak = sn.reduce((b, v, i) => i > 0 && v > sn[b] ? i : b, 1), dPeak = R1.data[2010].official;
const V = [];
V.push({n: 1, what: 'Direction, recession: basket poverty with the safety net higher in 2009 and 2010 than in 2007', model: [sn[at(2009)], sn[at(2010)]].map(r2), data: [R1.data[2009].official, R1.data[2010].official],
  verdict: sn[at(2009)] > 0 && sn[at(2010)] > 0 ? 'matches' : 'does not match'});
V.push({n: 2, what: 'Size, recession: the rise at the model\'s peak between half and double the official rise at its 2010 peak (1.3 to 5.2 points)', model: r2(sn[peak]), modelYear: Y[peak], data: dPeak,
  verdict: sn[peak] <= 0 ? 'does not match' : sn[peak] >= dPeak/2 && sn[peak] <= 2*dPeak ? 'matches' : 'same direction, different size'});
V.push({n: 3, what: 'Timing: the model\'s peak within one year of 2010', model: Y[peak], data: 2010, verdict: Math.abs(Y[peak] - 2010) <= 1 ? 'matches' : 'does not match'});
const k2 = peak + 2 < Y.length ? peak + 2 : null;
V.push({n: 4, what: 'Recovery, two years after the peak: share of the rise gone (reported, no verdict)', model: k2 !== null && sn[peak] > 0 ? r2((sn[peak] - sn[k2])/sn[peak]*100) : null, modelNote: k2 === null ? 'the model\'s peak is less than two years before the end of the window (2012)' : Y[peak] + ' to ' + Y[k2],
  data: r2((R1.data[2010].official - R1.data[2012].official)/R1.data[2010].official*100), verdict: 'reported'});
const a5 = ns[at(2012)] > 0 ? (ns[at(2012)] - sn[at(2012)])/ns[at(2012)]*100 : null, d5 = (R1.data[2012].beforeTransfers - R1.data[2012].spmColumbia)/R1.data[2012].beforeTransfers*100;
V.push({n: 5, what: 'How much the safety net absorbs, 2007 to 2012: (rise without - rise with) / rise without, %; band: within 20 points of the data', model: a5 === null ? null : r2(a5), modelRises: [r2(ns[at(2012)]), r2(sn[at(2012)])], data: r2(d5), dataRises: [R1.data[2012].beforeTransfers, R1.data[2012].spmColumbia],
  verdict: a5 === null || a5 <= 0 ? 'does not match' : Math.abs(a5 - d5) <= 20 ? 'matches' : 'same direction, different size',  /* the safety net absorbing none of the rise, or adding to it, is not the data's direction */
  note: 'the model\'s transfers are SNAP, EITC and the refundable CTC (unemployment insurance is in both arms); Columbia\'s "before transfers" also removes unemployment insurance, Social Security, housing aid and the tax system'});
const R2 = out.episodes.c20, n20 = R2.model.noSN.basket[1].mean, s20 = R2.model.SN.basket[1].mean;
V.push({n: 6, what: '2020, official-style measure (as amended before any run: basket poverty without SNAP and tax credits, which the official measure leaves out): higher in 2020 than in 2019', model: r2(n20), data: R2.data[2020].official, verdict: n20 > 0 ? 'matches' : 'does not match'});
V.push({n: 7, what: '2020, supplemental measure (reported, no verdict: the data fell because of payments the engine does not have)', model: r2(s20), data: R2.data[2020].spmCensus, verdict: 'reported'});
out.comparisons = V; out._meta.seconds = Math.round((Date.now() - t0)/1000);
fs.mkdirSync(path.dirname(OUT), {recursive: true}); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const f = x => x === null || x === undefined ? '-' : Array.isArray(x) ? x.join(' / ') : String(x);
console.log('history check, ' + N + ' seeds, ' + out._meta.seconds + ' s; model = shock minus no shock (points), data = change from the base year');
['rec', 'c20'].forEach(k => { const E = out.episodes[k]; console.log('  ' + k + ': ' + E.years.map((y, t) => y + ' x' + E.script[t].incomeMultiplier.toFixed(3) + ' noSN ' + E.model.noSN.basket[t].mean.toFixed(2) + ' SN ' + E.model.SN.basket[t].mean.toFixed(2) + ' [' + E.model.SN.basket[t].p5.toFixed(2) + ', ' + E.model.SN.basket[t].p95.toFixed(2) + '] off ' + f(E.data[y].official)).join('; ')); });
V.forEach(c => console.log('  ' + c.n + '. ' + c.verdict + ': model ' + f(c.model) + (c.modelYear ? ' (' + c.modelYear + ')' : '') + ', data ' + f(c.data)));
console.log('wrote ' + OUT);
