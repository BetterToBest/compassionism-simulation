#!/usr/bin/env node
/* Session 2c (Oct 13, 2026; dev/reports/v5-28-safety-net-grid.md, section 2): why does today's safety net raise basket poverty under health setting A?
 * Session 2b's report (v5-27, section 5) read +0.4 points. This tool runs, without the programme and with it, paired by seed: no health setting and setting A,
 * each without and with the safety net, under three engines: as released (work response and prices on), the work response off (every labour coefficient 0),
 * and prices flat. For each it prints the safety net's paired effect on basket poverty (person-years), depth, hours, Medicaid and the household health bill,
 * against the same health setting without the safety net, and, for the setting A rows, against no health setting (the reference session 2b's tool used).
 * Usage: node dev/tools/sn_trace.js ref|adv|st [SEEDS]   Output: dev/runs/health/sntrace-ENV.json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const pos = process.argv.slice(2).filter(x => !x.startsWith('--'));
const env = pos[0] || 'ref', N = +(pos[1] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || !(N >= 2)) { console.error('usage: sn_trace.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const C = H.CFG, SC = H.SPEND_SOURCED, K = ['fgt0PY', 'fgt2PY', 'hrs', 'hlMcaid', 'hlPaid', 'snAll', 'snMtr'];
const ROWS = {off: {}, SN: {sn: {}}, A: {hl: {}}, ASN: {hl: {}, sn: {}}};
const ENG = {released: {}, noWork: {labor: H.LAB_ZERO}, flat: {lamG: 0, theta: {food: 0, housing: 0, medical: 0}}};
const r3 = x => +(+x).toFixed(3);
function ci(d){ const n = d.length; let m = 0, s = 0; d.forEach(x => { m += x/n; }); d.forEach(x => { s += (x - m)*(x - m)/(n - 1); }); const h = 1.96*Math.sqrt(s/n); return [r3(m), r3(m - h), r3(m + h)]; }
const pdiff = (a, b, k) => ci(Array.from(a._s[k]).map((x, j) => x - b._s[k][j]));
const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const out = {_meta: {what: 'today\'s safety net under no health setting and setting A: its paired effect (sn against the same row without it) under three engines, without (base) and with (prog) the programme', env, seeds: N, command: 'node dev/tools/sn_trace.js ' + env + ' ' + N, manifest: H.runManifest()}, eng: {}};
try {
  const P = Object.assign({}, H[NAME]), PR = H.tbPresets(P), names = Object.keys(ROWS), cfg = [];
  names.forEach(v => { const M = H.relMainCfgs(PR); cfg.push(Object.assign(M[0], ROWS[v]), Object.assign(M[1], {sc: SC}, ROWS[v])); });
  Object.keys(ENG).forEach(e => {
    const R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY, ENG[e])), at = {};
    names.forEach((v, i) => { at[v] = {base: R[2*i], prog: R[2*i + 1]}; });
    const o = out.eng[e] = {levels: {}, snNoHealth: {}, snUnderA: {}, ASNvsOff: {}};
    ['base', 'prog'].forEach(w => {
      o.levels[w] = {}; names.forEach(v => { o.levels[w][v] = {}; K.forEach(k => { if (at[v][w][k] !== undefined) o.levels[w][v][k] = r3(at[v][w][k]); }); });
      o.snNoHealth[w] = {}; o.snUnderA[w] = {}; o.ASNvsOff[w] = {};
      K.forEach(k => { if (at.SN[w]._s[k] && at.off[w]._s[k]) o.snNoHealth[w][k] = pdiff(at.SN[w], at.off[w], k);
        if (at.ASN[w]._s[k] && at.A[w]._s[k]) o.snUnderA[w][k] = pdiff(at.ASN[w], at.A[w], k);
        if (at.ASN[w]._s[k] && at.off[w]._s[k]) o.ASNvsOff[w][k] = pdiff(at.ASN[w], at.off[w], k); });
    });
    const f = q => q ? (q[0] >= 0 ? '+' : '') + q[0].toFixed(3) + ' [' + q[1].toFixed(3) + ', ' + q[2].toFixed(3) + ']' : '-';
    console.log('[' + e + ']');
    ['base', 'prog'].forEach(w => console.log('  ' + w + ': basket poverty  sn, no health ' + f(o.snNoHealth[w].fgt0PY) + '; sn under A ' + f(o.snUnderA[w].fgt0PY) + '; A+sn against no health, no sn ' + f(o.ASNvsOff[w].fgt0PY) +
      '\n        depth  sn, no health ' + f(o.snNoHealth[w].fgt2PY) + '; under A ' + f(o.snUnderA[w].fgt2PY) + '   hours ' + f(o.snNoHealth[w].hrs) + ' / ' + f(o.snUnderA[w].hrs) + '   Medicaid under A ' + f(o.snUnderA[w].hlMcaid) + '   bill under A ' + f(o.snUnderA[w].hlPaid)));
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
const dir = path.join(__dirname, '..', 'runs', 'health'); fs.mkdirSync(dir, {recursive: true});
fs.writeFileSync(path.join(dir, 'sntrace-' + env + '.json'), JSON.stringify(out, null, 1) + '\n');
