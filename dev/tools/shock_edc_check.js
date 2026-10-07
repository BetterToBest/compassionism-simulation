#!/usr/bin/env node
/* v5.3 B6 (Oct 7, 2026; plan item B6; dev/DECISIONS.md Session 39, "B6"): household income shocks and the measured EDC, 500 paired seeds. Diagnostic for the
 * report: nothing here feeds a published figure (the v5.3 restudy, plan item B10, publishes the figures).
 *
 * Rows, each with its own no-programme run (paired by seed), all with the measured EDC on (reporting only): the adult-only release row; the release row with
 * households (pooled, the child allowance at a quarter: d167, d168) and partners' income swings independent (the default); the same with Shore's (2010)
 * correlations ('shore': +0.10 in good years, -0.10 in recession years); and with a correlation of 0.5 (partners lose income together: the stress reading).
 * Every row carries the two v5.3 accounting corrections (ACCT_V53), runs under the `testbed` profile (acctProfile) and with the accounting check on.
 * Usage: node dev/tools/shock_edc_check.js [ENV] [SEEDS]   (ENV ref, adv or st; default ref, 500 seeds); writes dev/runs/shock-edc-check-ENV.json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 500);
if (['ref', 'adv', 'st'].indexOf(env) < 0 || !(N >= 2)) { console.error('usage: shock_edc_check.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now();
const AK = ['fgt0PY', 'pov', 'bOAPy', 'bNAPy', 'fgt2PY', 'endoAnn', 'cost', 'medWealthReal', 'giniD', 'fplPY'].concat(H.EDC_KEYS);
const HK = ['hhCostPY', 'hhCostKidPY', 'hhWlthPY', 'hhWlthEnd', 'hhWlthKidEnd', 'hhBleiPY', 'hhBleiKidPY', 'hhFplPY', 'hhGiniEq', 'hhMedEq'];
const READ = [['adult', null], ['hh', {}], ['hhShore', {shock: 'shore'}], ['hhS50', {shock: 0.5}]];
const out = {_meta: {what: 'v5.3 B6: household income shocks and the measured EDC, paired by seed (diagnostic)', env, seeds: N,
  manifest: H.runManifest(), command: 'node dev/tools/shock_edc_check.js ' + env + ' ' + N, corrections: H.ACCT_V53}, rows: {}, changes: {}, identities: {}};
const S = H.acctRelCfgs(env), pick = j => Object.assign({}, S.cfg.find(c => c.j === j));
H.acctProfile(function () {
  READ.forEach(function ([id, hh]) {
    const pair = ['base', 'release'].map(j => { const c = pick(j); if (hh) c.hh = hh; c.em = true; c.g = Object.assign({}, c.g || {}, H.ACCT_V53); return c; });
    let A = null; H.setAcct(H.acctNew());
    try { const R = H.tbStudy(pair, N, S.P, S.o); A = H.getAcct();
      const keys = AK.concat(hh ? HK : []);
      out.rows[id] = {base: {}, release: {}}; keys.forEach(k => { out.rows[id].base[k] = R[0][k]; out.rows[id].release[k] = R[1][k]; });
      out.changes[id] = {}; keys.forEach(k => { const d = H.tbDiff(R[1], R[0], k); out.changes[id][k] = [d.m, d.lo, d.hi]; });
      out.identities[id] = {checks: A.n, failures: A.nFail, worst: A.worst}; }
    finally { H.setAcct(null); }
  });
});
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'shock-edc-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
function f(x) { return Math.abs(x) >= 100 ? x.toFixed(0) : Math.abs(x) >= 1 ? x.toFixed(2) : x.toFixed(4); }
console.log('v5.3 B6 household shocks and measured EDC, ' + env + ', seeds 1-' + N + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
Object.keys(out.rows).forEach(id => { const r = out.rows[id], c = out.changes[id];
  console.log('\n' + id + ':'); Object.keys(c).forEach(k => console.log('  ' + k.padEnd(14) + ' ' + f(r.base[k]).padStart(10) + ' -> ' + f(r.release[k]).padStart(10) + '   change ' + f(c[k][0]) + ' [' + f(c[k][1]) + ', ' + f(c[k][2]) + ']')); });
Object.keys(out.identities).forEach(id => { const I = out.identities[id], bad = Object.keys(I.failures);
  console.log('identities, ' + id + ': ' + Object.keys(I.checks).map(q => q + ' ' + I.checks[q]).join(', ') + (bad.length ? '; FAILED ' + JSON.stringify(I.failures) : '; all hold')); });
