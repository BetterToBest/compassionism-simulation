#!/usr/bin/env node
/* S68 part 2 (Nov 14, 2026; research-update PLAN S68 item 7): the 10,000-adult checks of the weighted tail (wt; S59 report, limit 2) and the creditor side's
 * weighted totals (rt.cr; S71 report, limit 9). The candidate main row and its no-programme run (harness.js r2MainPair), C2.2 design, at 500 and 10,000
 * adults, with the tail on and off. The tail's weights enter measures only, but the model economy holds about three times as many very wealthy households
 * as the population: the check is that the tail moves prices and poverty negligibly, and that the creditor side's totals (the one rule that reads weights)
 * agree per adult between 500 and 10,000 adults. A test, not a study.
 * Usage: node dev/tools/s68_big.js ENV [SEEDS]   (default 2 seeds); writes dev/runs/s68-pairs/s68-big-ENV.json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const env = process.argv[2] || 'ref', N = +(process.argv[3] || 2), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env], t0 = Date.now();
const K = ['fgt0PY', 'pov', 'endoAnn', 'pLev20', 'cost', 'hrs', 'medWealthReal', 'wtPovE', 'wtT1E', 'wtT10E', 'wtB50E', 'wtGnE', 'wtW', 'wtTailW', 'crRel', 'crBook', 'crNom', 'crEq', 'crGap', 'crUn', 'crOutG', 'crOutF', 'crOutH', 'crOutS'];
const out = {env, seeds: N, keys: K, manifest: H.runManifest(), command: 'node dev/tools/s68_big.js ' + process.argv.slice(2).join(' '), runs: {}};
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
try {
  [500, 10000].forEach(n => [true, false].forEach(wt => {
    const P = Object.assign({}, H[NAME], {years: 20, nAgents: n}), cf = H.r2MainPair(P, 'c22');
    if (!wt) cf.forEach(c => { delete c.wt; });
    const so = H.r2MainStudy(); if (!wt) delete so.wtm;
    const t = Date.now(), R = H.tbStudy(cf, N, P, so), id = n + (wt ? ' tail' : ' no tail');
    out.runs[id] = {secs: (Date.now() - t)/1000, none: {}, prog: {}, seedsNone: {}, seedsProg: {}};
    K.forEach(k => { out.runs[id].none[k] = R[0][k]; out.runs[id].prog[k] = R[1][k]; if (R[0]._s[k]) { out.runs[id].seedsNone[k] = Array.from(R[0]._s[k]); out.runs[id].seedsProg[k] = Array.from(R[1]._s[k]); } });
    process.stderr.write(env + ' ' + id + ' ' + out.runs[id].secs.toFixed(0) + ' s\n'); }));
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out.secs = (Date.now() - t0)/1000;
fs.mkdirSync(path.join(__dirname, '..', 'runs', 's68-pairs'), {recursive: true});
fs.writeFileSync(path.join(__dirname, '..', 'runs', 's68-pairs', 's68-big-' + env + '.json'), JSON.stringify(out, null, 1));
console.log(env + ': done in ' + out.secs.toFixed(0) + ' s');
