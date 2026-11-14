#!/usr/bin/env node
/* S72 (Nov 14, 2026): the pilot preregistered in research-update prereg/2026-11-s72-government-budget.md (with Amendment 1).
 * (A) The government account and the readings of who pays the part a contribution does not raise, both designs: the Source (main, gv {}), the Source
 *     with gv {wb: false} (the size of the weighted books), and the flat contribution on wages, cap 0.9, share 1 with fx.fin 'money', 'debt' (fixed rate),
 *     'debt' (the policy-rate rule), 'cap' (0.99). (B) The C2.2 flat contribution with 'debt': each reading moved alone from the main values.
 * The candidate main row (r2MainRow, r2MainStudy) in both runs, 500 adults, 20 years.
 * Usage: node dev/tools/s72_pilot.js ENV SEEDS [OUTDIR]     ENV ref | adv | st; writes OUTDIR/s72-pilot-ENV.json (per-seed values of every key read) */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const E = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}, env = process.argv[2] || 'ref', N = +(process.argv[3] || 100);
const OUT = process.argv[4] || path.join(__dirname, '..', 'runs', 's72-government');
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
try {
  const P = Object.assign({}, H[E[env]], {years: 20, nAgents: 500});
  const row = (d, fin, f, gv) => { const c = H.r2MainPair(P, d === 'none' ? 'c22' : d)[d === 'none' ? 0 : 1]; if (fin) c.o = Object.assign({}, c.o, {fin}); if (f) c.fx.fin = f; c.gv = Object.assign({}, gv || {}); return c; };
  const L = [['none', row('none')]];
  ['rel', 'c22'].forEach(d => { L.push([d + ' source', row(d)], [d + ' source wb0', row(d, null, null, {wb: false})], [d + ' tax money', row(d, 'tax', 'money')],
    [d + ' tax debt', row(d, 'tax', 'debt')], [d + ' tax debt rule', row(d, 'tax', 'debt', {r: 'rule'})], [d + ' tax cap', row(d, 'tax', 'cap')]); });
  [['rule a0.25', {r: 'rule', a: 0.25}], ['rule a1', {r: 'rule', a: 1}], ['rule b0', {r: 'rule', b: 0}], ['rule b1', {r: 'rule', b: 1}], ['rule rs0', {r: 'rule', rs: 0}], ['rule rs0.02', {r: 'rule', rs: 0.02}],
   ['rr0', {rr: 0}], ['rr0.0196', {rr: 0.0196}], ['dk0', {dk: 0}], ['dk0.021', {dk: 0.021}], ['ip borrow', {ip: 'borrow'}]].forEach(x => L.push(['c22 tax debt ' + x[0], row('c22', 'tax', 'debt', x[1])]));
  L.push(['c22 tax cap 0.95', row('c22', 'tax', 'cap', {capHi: 0.95})]);
  const K = H.GV_KEYS.concat(['finPay', 'finTax', 'finMoney', 'finMatch', 'finGap', 'finGapM', 'finGapSh', 'finCapYrs', 'tauMean', 'tauLast', 'endoAnn', 'fgt0PY', 'pov', 'hrs', 'cost',
    'snAll', 'crOutG', 'crRel', 'wtF0E', 'wtPovE', 'wtF0S', 'wtPovS'], Array.from({length: 20}, (_, t) => 'ppov_' + t));
  const R = H.tbStudy(L.map(x => x[1]), N, P, H.r2MainStudy());
  fs.mkdirSync(OUT, {recursive: true});
  const res = {env, seeds: N, manifest: H.runManifest(), secs: (Date.now() - t0) / 1000,
    rows: L.map((x, i) => ({row: x[0], s: Object.fromEntries(K.map(k => [k, R[i]._s[k] ? Array.from(R[i]._s[k]) : null]))}))};
  fs.writeFileSync(path.join(OUT, 's72-pilot-' + env + '.json'), JSON.stringify(res));
  console.log(env + ': done in ' + res.secs.toFixed(0) + ' s');
} finally { H.resetNR6(svN); H.tbSetG(svG); }
