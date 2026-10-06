#!/usr/bin/env node
/* v5.2 round, step 5 (Oct 3, 2026; ledger s84): the no-programme run checked against US data. Runs the no-programme row (and the readings that close known gaps:
 * savings from the SCF linked to wages, automation risk linked to wages, the SCF's wage spread, the SCF's wage median, all four, and ageing) on paired seeds,
 * and compares it with:
 *  - poverty rates, Census Bureau, Poverty in the United States: 2025 (P60-290, Sept 2026): official measure, all people 10.2%, ages 18-64 9.2%, unrelated
 *    individuals 19.0%, all workers 4.3%, full-time year-round workers 1.6%; Supplemental Poverty Measure, all 13.1%, 18-64 12.3%, all workers 7.1%;
 *  - income inequality, Census Bureau, Income in the United States: 2025 (P60-289): household money-income Gini 0.490, post-tax 0.448;
 *  - wealth, Federal Reserve 2022 Survey of Consumer Finances, single heads with no children aged 25-66 with wage income (sources/scf_singles.py; 2025 dollars);
 *  - poverty spells, Panel Study of Income Dynamics: Stevens (1994), "The Dynamics of Poverty Spells: Updating Bane and Ellwood", AER Papers and Proceedings
 *    84(2): 34-37: exit probability 0.53 in the first year of a spell, 0.36 in the second, 0.2 or less after five years; probability of returning to poverty
 *    after one year out 0.269 (Table 2).
 * The model's measures: the share of adults whose money income (earnings, conversion proceeds, cash transfers, Social Security where adults age) is below the
 * official threshold for one person, moved with prices; Supplemental-style resources against the same threshold; the Gini of disposable income; the wealth
 * distribution in today's prices; poverty spells from each adult's record (harness.js tbRepSpells). A check of the yardstick, not the release panel.
 *
 * Usage: node dev/tools/us_check.js ENV [SEEDS] [YEARS]   (ENV ref or adv; default 200 seeds, 20 years; writes dev/runs/us-check-ENV.json) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 200), YRS = +(process.argv[4] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const US = {
  official: {all: 10.2, age18to64: 9.2, unrelated: 19.0, workers: 4.3, ftyr: 1.6, source: 'Census Bureau, Poverty in the United States: 2025 (P60-290), Figure 2'},
  spm: {all: 13.1, age18to64: 12.3, workers: 7.1, ftyr: 4.1, source: 'Census Bureau, P60-290, Figure 3'},
  gini: {money: 0.490, postTax: 0.448, source: 'Census Bureau, Income in the United States: 2025 (P60-289)'},
  scf: {median: 74422, p10: -10543, p25: 10218, p75: 296564, p90: 881839, neg: 12.56, below25k: 36.35, giniKept: 0.840, giniZero: 0.812, wageSdLog: 1.049, wageGini: 0.458,
    source: 'Federal Reserve, 2022 Survey of Consumer Finances: single heads, no children, aged 25-66, with wage income (sources/scf_singles.py), 2025 dollars'},
  psid: {exit1: 0.53, exit2: 0.36, exit5: 0.2, reentry1: 0.269, source: 'Stevens (1994), AER Papers and Proceedings 84(2): 34-37, PSID 1970-1987'}};
const SC = H.SPEND_SOURCED, svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const ROWS = [['none', {}], ['ltw', {lt: {w: 1}}], ['ltr', {lt: {r: 1}}], ['lts', {lt: {s: 1}}], ['ltm', {lt: {m: 1}}], ['lta', {lt: {w: 1, r: 1, s: 1, m: 1}}], ['ag', {ag: {}}]];
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
function gini(a, keepNeg){ const v = a.map(x => keepNeg ? x : Math.max(0, x)).sort((x, y) => x - y), n = v.length; let t = 0, w = 0; for (let i = 0; i < n; i++){ t += v[i]; w += (i + 1)*v[i]; } return t > 0 ? (2*w/(n*t) - (n + 1)/n)*n/(n - 1) : 0; }
const out = {_meta: {what: 'the no-programme run against US data', env, seeds: N, years: YRS, manifest: H.runManifest(), command: 'node dev/tools/us_check.js ' + env + ' ' + N + ' ' + YRS}, us: US, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P);
  ROWS.forEach(function (row) {
    const W = {0: [], 6: [], end: []};  /* per seed: the wealth and wage statistics at Year 0, Year 7 and the last year */
    H.setRepHook(function (agents, yr, T, lf) { const k = yr === 0 ? 0 : yr === 6 ? 6 : yr === T - 1 ? 'end' : null; if (k === null) return;
      const w = agents.map(a => a.wealth/lf), wg = agents.filter(a => !a._ret && a.yrWageUSD > 0).map(a => a.yrWageUSD), lw = wg.map(Math.log), m = lw.reduce((s, x) => s + x, 0)/lw.length;
      W[k].push({median: q(w, 0.5), p10: q(w, 0.1), p25: q(w, 0.25), p75: q(w, 0.75), p90: q(w, 0.9), neg: w.filter(x => x < 0).length/w.length*100, below25k: w.filter(x => x < 25000).length/w.length*100,
        giniKept: gini(w, true), giniZero: gini(w, false), wageSdLog: Math.sqrt(lw.reduce((s, x) => s + (x - m)*(x - m), 0)/lw.length), wageGini: gini(wg, false)}); });
    let R; try { R = H.tbStudy([Object.assign({p: PR.baseline(), sc: SC}, row[1])], N, P, {fin: 'tax', aT: 0, a: 0, X: 0, sc: SC, rep52: true, giniNN1: true})[0]; } finally { H.setRepHook(null); }
    const avg = k => { const o = {}; Object.keys(W[k][0]).forEach(f => { o[f] = W[k].reduce((s, x) => s + x[f], 0)/W[k].length; }); return o; };
    const hz = (m, d) => R[m + 'N' + d] > 0 ? R[m + 'X' + d]/R[m + 'N' + d] : null;
    out.rows[row[0]] = {
      fpl: {y0: R.y0Fpl, y7: R.y7Fpl, end: R.eFpl, py: R.fplPY}, spm: {y0: R.y0FplX, y7: R.y7FplX, end: R.eFplX}, giniD: {y0: R.y0GiniD, y7: R.y7GiniD, end: R.eGiniD},
      costOfLiving: {y0: R.y0F0, y7: R.y7F0, end: R.eF0}, wealth: {y0: avg(0), y7: avg(6), end: avg('end')},
      spells: {fpl: {exit1: hz('sf', 1), exit2: hz('sf', 2), exit3: hz('sf', 3), exit4: hz('sf', 4), exit5: hz('sf', 5), reentry1: R.sfRN > 0 ? R.sfR/R.sfRN : null, spellsPerSeed: R.sfN1, everPoor: R.everFpl},
        col: {exit1: hz('sc', 1), exit2: hz('sc', 2), exit3: hz('sc', 3), exit4: hz('sc', 4), exit5: hz('sc', 5), reentry1: R.scRN > 0 ? R.scR/R.scRN : null, spellsPerSeed: R.scN1}},
      retired: R.agRet};
    console.log(env, row[0], JSON.stringify(out.rows[row[0]]));
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(__dirname, '..', 'runs', 'us-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1));
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
