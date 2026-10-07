#!/usr/bin/env node
/* v5.3 B4, B5 (Oct 7, 2026; plan items B4, B5; dev/DECISIONS.md Session 39, "B4"): children's lives and estates, households with ageing, against the adult-only
 * ageing reading, 500 paired seeds. Diagnostic for the report: nothing here feeds a published figure (the v5.3 restudy, plan item B10, publishes the figures).
 *
 * Rows, each with its own no-programme run (paired by seed; families live the same lives in both): the adult-only release row with ageing (the v5.2
 * reading: adults age, retire and are replaced when they die); the release row with households and ageing (pooled, the child allowance at a quarter: d167,
 * d168; estates to the partner, else the children: d169); the same with every estate leaving the model (the adult-only rule). Every row carries the two v5.3
 * accounting corrections (ACCT_V53), runs under the `testbed` profile (acctProfile) and with the accounting check on (it changes no result).
 * Besides the means and paired changes, the file records each year's families (women up to 49 with and without a partner, births, children; the same in
 * both runs of a seed), the mean over seeds.
 * Usage: node dev/tools/life_check.js [ENV] [SEEDS]   (ENV ref, adv or st; default ref, 500 seeds); writes dev/runs/life-check-ENV.json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 500);
if (['ref', 'adv', 'st'].indexOf(env) < 0 || !(N >= 2)) { console.error('usage: life_check.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now();
const AK = ['fgt0PY', 'pov', 'bOAPy', 'bNAPy', 'fgt2PY', 'endoAnn', 'cost', 'medWealthReal', 'giniD', 'fplPY', 'pjNet', 'agRet', 'agAge0', 'agAge', 'agDeaths', 'agBorn'];
const HK = H.HH_KEYS.concat(H.HH_LIFE_KEYS);
const READ = [['adultAg', null], ['hhAg', {}], ['hhAgLeave', {estate: 'leave'}]];
const out = {_meta: {what: 'v5.3 B4, B5: children\'s lives and estates (households with ageing) against the adult-only ageing reading, paired by seed (diagnostic)', env, seeds: N,
  manifest: H.runManifest(), command: 'node dev/tools/life_check.js ' + env + ' ' + N, corrections: H.ACCT_V53}, rows: {}, changes: {}, identities: {}, years: null};
const S = H.acctRelCfgs(env), pick = j => Object.assign({}, S.cfg.find(c => c.j === j));
H.acctProfile(function () {
  READ.forEach(function ([id, hh]) {
    const pair = ['base', 'release'].map(j => { const c = pick(j); if (hh) c.hh = hh; c.ag = true; c.g = Object.assign({}, c.g || {}, H.ACCT_V53); return c; });
    const T = id === 'hhAg' ? [] : null; let A = null; H.setAcct(H.acctNew()); H.setHHTrace(T);
    try { const R = H.tbStudy(pair, N, S.P, S.o); A = H.getAcct();
      const keys = AK.concat(hh ? HK : []);
      out.rows[id] = {base: {}, release: {}}; keys.forEach(k => { out.rows[id].base[k] = R[0][k]; out.rows[id].release[k] = R[1][k]; });
      out.changes[id] = {}; keys.forEach(k => { const d = H.tbDiff(R[1], R[0], k); out.changes[id][k] = [d.m, d.lo, d.hi]; });
      out.identities[id] = {checks: A.n, failures: A.nFail, worst: A.worst};
      if (T){ const runs = 2*N, per = T.length/runs, y = [];  /* every run of a seed has the same families: the mean over all runs is the mean over seeds */
        for (let k = 0; k < per; k++){ const m = [0, 0, 0, 0, 0]; for (let r = 0; r < runs; r++) for (let q = 0; q < 5; q++) m[q] += T[r*per + k][q]/runs;
          y.push({year: k + 1, womenPartner: m[0], womenAlone: m[1], births: m[2], birthsAlone: m[3], children: m[4]}); }
        out.years = y; } }
    finally { H.setAcct(null); H.setHHTrace(null); }
  });
});
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'life-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
function f(x) { return Math.abs(x) >= 100 ? x.toFixed(0) : Math.abs(x) >= 1 ? x.toFixed(2) : x.toFixed(4); }
console.log('v5.3 B4, B5 children\'s lives, ' + env + ', seeds 1-' + N + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
Object.keys(out.rows).forEach(id => { const r = out.rows[id], c = out.changes[id];
  console.log('\n' + id + ':'); Object.keys(c).forEach(k => console.log('  ' + k.padEnd(14) + ' ' + f(r.base[k]).padStart(10) + ' -> ' + f(r.release[k]).padStart(10) + '   change ' + f(c[k][0]) + ' [' + f(c[k][1]) + ', ' + f(c[k][2]) + ']')); });
if (out.years) { console.log('\nfamilies by year (mean over seeds): women up to 49 with a partner / without; births (to women without a partner); children');
  out.years.forEach(y => console.log('  year ' + String(y.year).padStart(2) + ': ' + y.womenPartner.toFixed(1) + ' / ' + y.womenAlone.toFixed(1) + '; ' + y.births.toFixed(2) + ' (' + y.birthsAlone.toFixed(2) + '); ' + y.children.toFixed(1))); }
Object.keys(out.identities).forEach(id => { const I = out.identities[id], bad = Object.keys(I.failures);
  console.log('identities, ' + id + ': ' + Object.keys(I.checks).map(q => q + ' ' + I.checks[q]).join(', ') + (bad.length ? '; FAILED ' + JSON.stringify(I.failures) : '; all hold')); });
