#!/usr/bin/env node
/* v5.3 B7 (Oct 7, 2026; plan item B7; dev/DECISIONS.md Session 39, "B7"): the four calibration readings, 500 paired seeds. Diagnostic for the report: nothing
 * here feeds a published figure (the v5.3 restudy, plan item B10, publishes the figures).
 *
 * Rows, each with its own no-programme run (paired by seed; every reading applies to the no-programme run too): the adult-only release row, and with
 * income-graded spending (sg); the release row with households (pooled, the child allowance at a quarter: d167, d168), with household wealth from the SCF,
 * with income-graded spending, and with both; the adult-only release row with ageing, and with earnings by age (earn 'cps'); the release row with FBS50
 * spread evenly (fb dist 'fbs50') and with FBS50 kept (it only reports). Every row carries the two v5.3 accounting corrections (ACCT_V53), runs under the
 * `testbed` profile (acctProfile) and with the accounting check on (it changes no result).
 * Besides the means and paired changes, the no-programme run of the adult and household rows is checked against the 2022 SCF at Year 7 (sources/
 * scf_singles.py, scf_households.py): the share in debt (net worth below zero) and the median net worth in today's prices, per adult for adults alone and
 * per household for households (its adults' wealth together).
 * Usage: node dev/tools/calib_check.js [ENV] [SEEDS]   (ENV ref, adv or st; default ref, 500 seeds); writes dev/runs/calib-check-ENV.json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 500);
if (['ref', 'adv', 'st'].indexOf(env) < 0 || !(N >= 2)) { console.error('usage: calib_check.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now();
const AK = ['fgt0PY', 'pov', 'bOAPy', 'bNAPy', 'fgt2PY', 'endoAnn', 'cost', 'medWealthReal', 'giniD', 'fplPY', 'y7Pov', 'ePov'];
const HK = ['hhCostPY', 'hhCostKidPY', 'hhWlthPY', 'hhWlthEnd', 'hhWlthKidEnd', 'hhBleiPY', 'hhBleiKidPY', 'hhFplPY', 'hhMedEq'];
const READ = [['rel', {}], ['relSg', {sg: true}], ['hh', {hh: {}}], ['hhScf', {hh: {wealth: 'scf'}}], ['hhSg', {hh: {}, sg: true}], ['hhScfSg', {hh: {wealth: 'scf'}, sg: true}],
  ['ag', {ag: true}], ['agCps', {ag: {earn: 'cps'}}], ['fbF', {fb: {dist: 'fbs50'}}], ['fbL', {fb: true}]];
const US = {adultNeg: 12.56, adultMedian: 74422, hh: {coupleKids: [4.9, 272609], coupleNoKids: [4.4, 357505], singleParent: [16.3, 49503], single: [12.6, 74422]},
  source: 'Federal Reserve, 2022 Survey of Consumer Finances, heads aged 25-66 with wage income (sources/scf_singles.py, scf_households.py), 2025 dollars'};
const out = {_meta: {what: 'v5.3 B7: four calibration readings, paired by seed (diagnostic); the no-programme run against the SCF at Year 7', env, seeds: N,
  manifest: H.runManifest(), command: 'node dev/tools/calib_check.js ' + env + ' ' + N, corrections: H.ACCT_V53}, us: US, rows: {}, changes: {}, identities: {}, year7: {}};
const S = H.acctRelCfgs(env), pick = j => Object.assign({}, S.cfg.find(c => c.j === j));
function q(a, p){ const v = a.slice().sort((x, y) => x - y), h = (v.length - 1)*p, lo = Math.floor(h), hi = Math.ceil(h); return v[lo] + (v[hi] - v[lo])*(h - lo); }
H.acctProfile(function () {
  READ.forEach(function ([id, x]) {
    const mk = j => { const c = Object.assign(pick(j), JSON.parse(JSON.stringify(x))); c.g = Object.assign({}, c.g || {}, H.ACCT_V53); return c; };
    let A = null; H.setAcct(H.acctNew());
    try { const R = H.tbStudy([mk('base'), mk('release')], N, S.P, S.o); A = H.getAcct();
      const keys = AK.concat(x.hh ? HK : [], x.fb ? H.FBS_KEYS : []);
      out.rows[id] = {base: {}, release: {}}; keys.forEach(k => { out.rows[id].base[k] = R[0][k]; out.rows[id].release[k] = R[1][k]; });
      out.changes[id] = {}; keys.forEach(k => { const d = H.tbDiff(R[1], R[0], k); out.changes[id][k] = [d.m, d.lo, d.hi]; });
      out.identities[id] = {checks: A.n, failures: A.nFail, worst: A.worst}; }
    finally { H.setAcct(null); }
    if (['rel', 'relSg', 'hh', 'hhScf', 'hhSg', 'hhScfSg'].indexOf(id) >= 0){  /* the no-programme run at Year 7, against the SCF */
      const Y = {neg: [], med: [], t: {}};
      H.setRepHook(function (agents, yr, T, lf) { if (yr !== 6) return;
        if (!x.hh){ const w = agents.map(a => a.wealth/lf); Y.neg.push(w.filter(v => v < 0).length/w.length*100); Y.med.push(q(w, 0.5)); return; }
        const G = {}, all = [], seen = new Set();
        agents.forEach(a => { const Hh = a._hh; if (!Hh || seen.has(Hh)) return; seen.add(Hh); const w = Hh.a.reduce((s, b) => s + b.wealth, 0)/lf;
          const t = Hh.a.length > 1 ? (Hh.kids.length ? 'coupleKids' : 'coupleNoKids') : (Hh.kids.length ? 'singleParent' : 'single'); (G[t] = G[t] || []).push(w); all.push(w); });
        Y.neg.push(all.filter(v => v < 0).length/all.length*100); Y.med.push(q(all, 0.5));
        Object.keys(G).forEach(t => { (Y.t[t] = Y.t[t] || {neg: [], med: []}); Y.t[t].neg.push(G[t].filter(v => v < 0).length/G[t].length*100); Y.t[t].med.push(q(G[t], 0.5)); }); });
      try { H.tbStudy([mk('base')], N, S.P, S.o); } finally { H.setRepHook(null); }
      const m = v => v.reduce((s, z) => s + z, 0)/v.length;
      out.year7[id] = {unit: x.hh ? 'household' : 'adult', neg: m(Y.neg), median: m(Y.med), byType: Object.fromEntries(Object.keys(Y.t).map(t => [t, {neg: m(Y.t[t].neg), median: m(Y.t[t].med)}]))};
    }
  });
});
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'calib-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
function f(x) { return Math.abs(x) >= 100 ? x.toFixed(0) : Math.abs(x) >= 1 ? x.toFixed(2) : x.toFixed(4); }
console.log('v5.3 B7 calibration readings, ' + env + ', seeds 1-' + N + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
Object.keys(out.rows).forEach(id => { const r = out.rows[id], c = out.changes[id];
  console.log('\n' + id + ':'); Object.keys(c).forEach(k => console.log('  ' + k.padEnd(14) + ' ' + f(r.base[k]).padStart(10) + ' -> ' + f(r.release[k]).padStart(10) + '   change ' + f(c[k][0]) + ' [' + f(c[k][1]) + ', ' + f(c[k][2]) + ']')); });
console.log('\nno programme at Year 7 against the SCF (in debt %, median net worth):');
Object.keys(out.year7).forEach(id => { const y = out.year7[id]; console.log('  ' + id.padEnd(8) + ' per ' + y.unit + ': ' + y.neg.toFixed(1) + '%, $' + Math.round(y.median) +
  Object.keys(y.byType).map(t => '; ' + t + ' ' + y.byType[t].neg.toFixed(1) + '%, $' + Math.round(y.byType[t].median)).join('')); });
Object.keys(out.identities).forEach(id => { const I = out.identities[id], bad = Object.keys(I.failures);
  console.log('identities, ' + id + ': ' + Object.keys(I.checks).map(q => q + ' ' + I.checks[q]).join(', ') + (bad.length ? '; FAILED ' + JSON.stringify(I.failures) : '; all hold')); });
