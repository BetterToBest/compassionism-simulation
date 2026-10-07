#!/usr/bin/env node
/* v5.3 B3 (Oct 7, 2026; plan item B3; dev/DECISIONS.md Session 39): the household reading so far (households drawn once and kept as drawn: children do not
 * age, are not born and do not leave home until plan item B4), against the adult-only model, 500 paired seeds. Diagnostic for the B3 report: nothing here
 * feeds a published figure (the v5.3 restudy, plan item B10, publishes the figures).
 *
 * Rows, each with its own no-programme run (paired by seed): the adult-only release row (as `testbed release` builds it); the release row with households
 * (pooled, the child allowance at a quarter of the adult BU: d167, d168); with each adult keeping their own money ('individual'); with no child allowance and
 * with half. Every row carries the two v5.3 accounting corrections (ACCT_V53) and runs under the `testbed` profile (acctProfile); the rows with households also
 * run with the accounting check on (it changes no result), so the file records every identity over all seeds.
 * For each row: the means of the adult measures and of the household measures (HH_KEYS), and the change against its own no-programme run with a 95% interval.
 * Usage: node dev/tools/hh_check.js [ENV] [SEEDS]   (ENV ref, adv or st; default ref, 500 seeds); writes dev/runs/hh-check-ENV.json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 500);
if (['ref', 'adv', 'st'].indexOf(env) < 0 || !(N >= 2)) { console.error('usage: hh_check.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now();
const AK = ['fgt0PY', 'pov', 'bOAPy', 'bNAPy', 'fgt2PY', 'endoAnn', 'cost', 'medWealthReal', 'giniD', 'fplPY'];
const HK = H.HH_KEYS;
const READ = [['adult', null, false], ['hh', {}, true], ['hhInd', {pool: 'individual'}, true], ['hhCb0', {childBU: 0}, true], ['hhCb50', {childBU: 0.5}, true]];
const out = {_meta: {what: 'v5.3 B3: the household reading (composition as drawn; children static until B4) against the adult-only model, paired by seed (diagnostic)', env, seeds: N,
  manifest: H.runManifest(), command: 'node dev/tools/hh_check.js ' + env + ' ' + N, corrections: H.ACCT_V53}, rows: {}, changes: {}, identities: {}};
const S = H.acctRelCfgs(env), pick = j => Object.assign({}, S.cfg.find(c => c.j === j));
H.acctProfile(function () {
  READ.forEach(function ([id, hh, chk]) {
    const pair = ['base', 'release'].map(j => { const c = pick(j); if (hh) c.hh = hh; c.g = Object.assign({}, c.g || {}, H.ACCT_V53); return c; });
    let A = null; if (chk) H.setAcct(H.acctNew());
    try { const R = H.tbStudy(pair, N, S.P, S.o); if (chk) A = H.getAcct();
      const keys = AK.concat(hh ? HK : []);
      out.rows[id] = {base: {}, release: {}}; keys.forEach(k => { out.rows[id].base[k] = R[0][k]; out.rows[id].release[k] = R[1][k]; });
      out.changes[id] = {}; keys.forEach(k => { const d = H.tbDiff(R[1], R[0], k); out.changes[id][k] = [d.m, d.lo, d.hi]; });
      if (A) out.identities[id] = {checks: A.n, failures: A.nFail, worst: A.worst}; }
    finally { H.setAcct(null); }
  });
});
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'hh-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
function f(x) { return Math.abs(x) >= 100 ? x.toFixed(0) : Math.abs(x) >= 1 ? x.toFixed(2) : x.toFixed(4); }
console.log('v5.3 B3 household reading, ' + env + ', seeds 1-' + N + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
Object.keys(out.rows).forEach(id => { const r = out.rows[id], c = out.changes[id];
  console.log('\n' + id + ':'); Object.keys(c).forEach(k => console.log('  ' + k.padEnd(14) + ' ' + f(r.base[k]).padStart(10) + ' -> ' + f(r.release[k]).padStart(10) + '   change ' + f(c[k][0]) + ' [' + f(c[k][1]) + ', ' + f(c[k][2]) + ']')); });
Object.keys(out.identities).forEach(id => { const I = out.identities[id], bad = Object.keys(I.failures);
  console.log('identities, ' + id + ': ' + Object.keys(I.checks).map(q => q + ' ' + I.checks[q]).join(', ') + (bad.length ? '; FAILED ' + JSON.stringify(I.failures) : '; all hold')); });
