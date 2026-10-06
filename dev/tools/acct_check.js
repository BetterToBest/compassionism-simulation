#!/usr/bin/env node
/* v5.3 B2 (Oct 6, 2026; plan item B2; dev/DECISIONS.md Session 39): what the two engine corrections the accounting check called for do to the results, and the
 * identities over every seed. Diagnostic for the B2 report: nothing here feeds a published figure (the v5.3 restudy, plan item B10, publishes the figures).
 *
 * The accounting check (ACCT in index.html; acctStudy and acctUnitSuite in harness.js) found two places where money is not conserved in v5.2:
 *  1. PTH appreciation: the whole appreciation is added to the member's Acre Equity and its cash part is also paid into the member's wealth, so the cash
 *     part is counted twice and compounds (PTH_APPR_CONSERVE = true takes the cash part out of the equity; open since v4.16);
 *  2. the ESP surplus split in the two rent mark-up readings: the price cut is sized on essentials before the landlords' mark-up and applied after it, so it
 *     hands out more than the pool holds (SURP_CUT_MARKUP = true sizes it on the same bill).
 * This tool runs, on seeds 1..N, paired, under the `testbed` mode's profile (acctProfile) and with the release rows built as `testbed release` builds them
 * (acctRelCfgs): no programme; the release row as in v5.2 and with both corrections; the first rent mark-up reading as in v5.2 and with both corrections; the
 * ageing reading with both corrections (for the BU that lapse when an adult dies). Rows with the corrections run with the accounting check on (it changes no
 * result: acctUnitSuite), so the file also records every identity over all N seeds. For each row: the means of the headline measures; for each correction,
 * the paired change and its 95% interval; and the change against no programme with and without the corrections.
 * Usage: node dev/tools/acct_check.js [ENV] [SEEDS]   (ENV ref, adv or st; default ref, 500 seeds); writes dev/runs/acct-check-ENV.json */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 500);
if (['ref', 'adv', 'st'].indexOf(env) < 0 || !(N >= 2)) { console.error('usage: acct_check.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now();
const KEYS = ['fgt0PY', 'pov', 'bOAPy', 'bNAPy', 'fgt2PY', 'endoAnn', 'cost', 'cPth', 'medWealthReal', 'giniD', 'pLev20'];
const LBL = {fgt0PY: 'below the cost of living (% of adult-years)', pov: 'too little wealth at the last year (% of adults)', bOAPy: 'below 30 days of basic living, BLEI paper\'s reading (% of adult-years)',
  bNAPy: 'below 30 days, design-neutral reading (% of adult-years)', fgt2PY: 'poverty severity FGT2 (x100, person-years)', endoAnn: 'programme inflation (a year)', cost: 'cost per adult-year (year-0 $)',
  cPth: 'PTH appreciation paid in cash (year-0 $ per adult-year)', medWealthReal: 'median net wealth at the last year (year-0 $)', giniD: 'Gini of disposable income', pLev20: 'price level at the last year'};
const ROWS = [['base', null, false], ['release', null, false], ['release', H.ACCT_V53, true], ['hcap', null, false], ['hcap', H.ACCT_V53, true], ['age', H.ACCT_V53, true]];
const out = {_meta: {what: 'v5.3 B2: the effect of the two accounting corrections (PTH appreciation conserved; the split\'s cut sized on the marked-up rent) and the identities over every seed (diagnostic)',
  env, seeds: N, manifest: H.runManifest(), command: 'node dev/tools/acct_check.js ' + env + ' ' + N, corrections: H.ACCT_V53, labels: LBL}, rows: {}, changes: {}, identities: {}};
const R = H.acctProfile(function () {
  const S = H.acctRelCfgs(env);
  return ROWS.map(function (rw) {
    const c = Object.assign({}, S.cfg.filter(x => x.j === rw[0])[0]); if (rw[1]) c.g = Object.assign({}, c.g || {}, rw[1]);
    let A = null; if (rw[2]) H.setAcct(H.acctNew());
    try { const r = H.tbStudy([c], N, S.P, S.o)[0]; if (rw[2]) A = H.getAcct(); return {id: rw[0] + (rw[1] ? '53' : ''), r, A}; }
    finally { H.setAcct(null); }
  });
});
const by = {}; R.forEach(x => { by[x.id] = x.r; out.rows[x.id] = {}; KEYS.forEach(k => { out.rows[x.id][k] = x.r[k]; });
  if (x.A) out.identities[x.id] = {checks: x.A.n, failures: x.A.nFail, worst: x.A.worst, buLapsedAtDeath: x.A.lostDeath, buIssued: x.A.issued || 0}; });
function d(a, b, k) { const q = H.tbDiff(by[a], by[b], k); return [q.m, q.lo, q.hi]; }
[['release53', 'release', 'PTH appreciation conserved and the cut sized on the marked-up rent, against v5.2 (release row)'], ['hcap53', 'hcap', 'the same, rent mark-up reading'],
 ['release', 'base', 'v5.2 release row against no programme'], ['release53', 'base', 'release row with the corrections against no programme']].forEach(function (p) {
  const o = {what: p[2]}; KEYS.forEach(k => { o[k] = d(p[0], p[1], k); }); out.changes[p[0] + '-' + p[1]] = o; });
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = path.join(ROOT, 'dev', 'runs', 'acct-check-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
function f(x) { return Math.abs(x) >= 100 ? x.toFixed(0) : Math.abs(x) >= 1 ? x.toFixed(2) : x.toFixed(4); }
console.log('v5.3 B2 accounting corrections, ' + env + ', seeds 1-' + N + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
Object.keys(out.changes).forEach(function (k) { const o = out.changes[k]; console.log('\n' + o.what);
  KEYS.forEach(key => console.log('  ' + LBL[key] + ': ' + f(o[key][0]) + ' [' + f(o[key][1]) + ', ' + f(o[key][2]) + ']')); });
Object.keys(out.identities).forEach(function (k) { const I = out.identities[k];
  console.log('\nidentities, ' + k + ': ' + Object.keys(I.checks).map(q => q + ' ' + I.checks[q] + (I.failures[q] ? ' FAILED ' + I.failures[q] : '') + ' (worst ' + (I.worst[q] || 0).toExponential(1) + ')').join(', ') + '; BU lapsed at death: ' + (I.buIssued > 0 ? (I.buLapsedAtDeath/I.buIssued*100).toFixed(3) + '% of BU issued' : 'none')); });
