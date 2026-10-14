#!/usr/bin/env node
/* Session 9 (Oct 14, 2026; issue i24-1; dev/reports/v5-35-safety-net-poverty.md): why does today's safety net raise basket poverty in the v5.4 main row?
 * Runs the v5.4 main row and its no-programme run (the rows of snap_rule_check.js), paired seeds 1-N, in one environment: without the safety net, with it
 * (row option sn) and with it under SNET.slope (the marginal rate read without SNAP's gross income cliff), under four engines: as released, the
 * work response off (every labour coefficient 0), prices flat (no price response to demand), and both off. Prints the safety net's paired effect (row with sn minus the same row without) on basket poverty,
 * depth, wealth poverty, hours, employment, the benefits and the mean marginal rate, with 95% intervals over seeds.
 * --engines=released,noWork,flat,neither (default all four); --rows=sn,slope (default both); --out=FILE (default dev/runs/sn/v54trace-ENV.json).
 * The s165 study runs it at 500 seeds with --engines=released,noWork,flat --rows=slope (the safety net as the study runs it).
 * Usage: node dev/tools/sn_v54_trace.js ref|adv|st [SEEDS] [--engines=...] [--rows=...] [--out=FILE] */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : null; }, pos = process.argv.slice(2).filter(x => !x.startsWith('--'));
const env = pos[0] || 'ref', N = +(pos[1] || 20), P0 = {ref: H.FULL_INTEGRATION, adv: H.ADVERSE_REFERENCE, st: H.STRESS_TEST}[env];
if (!P0 || !(N >= 2)) { console.error('usage: sn_v54_trace.js ref|adv|st [SEEDS >= 2]'); process.exit(1); }
const C = H.CFG, SC = H.SPEND_SOURCED, K = ['fgt0PY', 'fgt2PY', 'pov', 'bOAPy', 'hrs', 'emp', 'snAll', 'snSnapM', 'snEitcM', 'snMtr', 'pLev20'];
const SN0 = {sn: {sn: {}}, slope: {sn: {slope: true}}}, FLAT = {lamG: 0, theta: {food: 0, housing: 0, medical: 0}}, ENG0 = {released: {}, noWork: {labor: H.LAB_ZERO}, flat: FLAT, neither: Object.assign({labor: H.LAB_ZERO}, FLAT)};
const pick = (O, l) => { const r = {}; (l ? l.split(',') : Object.keys(O)).forEach(k => { if (!O[k]) { console.error('unknown: ' + k); process.exit(1); } r[k] = O[k]; }); return r; };
const SN = pick(SN0, arg('rows')), ENG = pick(ENG0, arg('engines')), OUTF = arg('out');
const r3 = x => +(+x).toFixed(3);
function ci(d){ const n = d.length; let m = 0, s = 0; d.forEach(x => { m += x/n; }); d.forEach(x => { s += (x - m)*(x - m)/(n - 1); }); const h = 1.96*Math.sqrt(s/n); return [r3(m), r3(m - h), r3(m + h)]; }
const pdiff = (a, b, k) => a._s[k] && b._s[k] ? ci(Array.from(a._s[k]).map((x, j) => x - b._s[k][j])) : null;
const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const out = {_meta: {what: 'today\'s safety net in the v5.4 main row and its no-programme run: its paired effect (row with sn minus the same row without), with SNAP\'s cliff in the marginal rate (sn, as released) and without (slope), under four engines (as released, work response off, prices flat, both off)', env, seeds: N, command: 'node dev/tools/sn_v54_trace.js ' + process.argv.slice(2).join(' '), manifest: H.runManifest()}, eng: {}};
try {
  const P = Object.assign({}, P0), PR = H.tbPresets(P), base = {sc: SC, so: H.REL_V52_STUDY, hh: H.REL_V53.hh, sg: true, g: H.ACCT_V53, em: true, fb: true, v54: H.REL_V54.v54};
  const R = H.releaseRowsV54(SC).filter(r => r.j === 'release')[0], main = () => { const m = H.n1Row(PR, 'framework', R.v); if (R.v.o) Object.assign(m.o || (m.o = {}), R.v.o); return m; };
  const arms = {base: () => Object.assign({p: PR.baseline()}, base), prog: main}, names = [], cfg = [];
  Object.keys(arms).forEach(w => { names.push(w + '|off'); cfg.push(arms[w]()); Object.keys(SN).forEach(v => { names.push(w + '|' + v); cfg.push(Object.assign(arms[w](), SN[v])); }); });
  Object.keys(ENG).forEach(e => {
    const S = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0}, H.REL_V52_STUDY, {sc: SC}, ENG[e])), at = {};
    names.forEach((n, i) => { at[n] = S[i]; });
    const o = out.eng[e] = {levels: {}, effect: {}};
    names.forEach(n => { o.levels[n] = {}; K.forEach(k => { if (at[n][k] !== undefined) o.levels[n][k] = r3(at[n][k]); }); });
    const f = q => q ? (q[0] >= 0 ? '+' : '') + q[0].toFixed(3) + ' [' + q[1].toFixed(3) + ', ' + q[2].toFixed(3) + ']' : '-';
    console.log('[' + env + ', ' + e + ']');
    Object.keys(arms).forEach(w => Object.keys(SN).forEach(v => { const d = o.effect[w + '|' + v] = {}; K.forEach(k => { const q = pdiff(at[w + '|' + v], at[w + '|off'], k); if (q) d[k] = q; });
      console.log('  ' + w + ' ' + v + ': basket ' + f(d.fgt0PY) + '  depth ' + f(d.fgt2PY) + '  wealth ' + f(d.pov) + '  hours ' + f(d.hrs) + '  benefits $' + (o.levels[w + '|' + v].snAll || 0).toFixed(0) + '  rate ' + (o.levels[w + '|' + v].snMtr || 0).toFixed(1) + '%'); }));
  });
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = OUTF ? path.resolve(OUTF) : path.join(__dirname, '..', 'runs', 'sn', 'v54trace-' + env + '.json'); fs.mkdirSync(path.dirname(file), {recursive: true});
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
console.log('wrote ' + file + ' (' + out._meta.seconds + ' s)');
