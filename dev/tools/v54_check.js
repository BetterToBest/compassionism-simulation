#!/usr/bin/env node
/* v5.4 (Oct 7, 2026; dev/reports/v5-21-v54-design.md): the round's paired check. For each variant (a set of v5.4 switches), the v5.3 main row and its
 * no-programme run, both with the variant's switches, paired by seed; the risk measures are on in every row (reporting only).
 * Usage: node dev/tools/v54_check.js ref|adv|st [SEEDS] [20|40] [--rows=v53,empl,...] [--out=NAME]
 * Output: dev/runs/v54/NAME-ENV[-40].json (NAME defaults to 'check'); levels for both runs and the programme's paired effect with its 95% interval. */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : null; };
const pos = process.argv.slice(2).filter(x => !x.startsWith('--'));
const env = pos[0] || 'ref', N = +(pos[1] || 12), YRS = +(pos[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || !(N >= 2) || (YRS !== 20 && YRS !== 40)) { console.error('usage: v54_check.js ref|adv|st [SEEDS >= 2] [20|40] [--rows=v53,...]'); process.exit(1); }
/* The variants: the v54 row option each one sets (rk, the risk measures, is on in all). */
const VAR = {v53: {}, empl: {empl: {}}, emplPay: {empl: {auto: 'pay'}}, emplCut0: {empl: {cut: 0}}, emplCut20: {empl: {cut: 0.20}}, emplNoUI: {empl: {ui: false}}, emplAdd: {empl: {rec: 'add'}}};
const rows = (arg('rows') || 'v53').split(',');
rows.forEach(v => { if (!VAR[v]) { console.error('unknown variant ' + v + ' (known: ' + Object.keys(VAR).join(', ') + ')'); process.exit(1); } });
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now(), SC = H.SPEND_SOURCED, C = H.CFG;
const K = ['fgt0PY', 'pov', 'bOAPy', 'fgt2PY', 'endoAnn', 'cost', 'giniD', 'medWealthReal', 'hrs'].concat(H.RISK_KEYS, H.EMPL_KEYS);
const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;  /* as the testbed command sets it */
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const cmd = 'node dev/tools/v54_check.js ' + env + ' ' + N + ' ' + YRS + ' --rows=' + rows.join(',') + (arg('out') ? ' --out=' + arg('out') : '');
const out = {_meta: {what: 'v5.4: the v5.3 main row and its no-programme run under each variant, paired by seed', env, seeds: N, years: YRS, manifest: H.runManifest(), command: cmd}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P);
  const cfg = [];
  rows.forEach(v => { const o = Object.assign({rk: true}, VAR[v]), M = H.relMainCfgs(PR);
    cfg.push(Object.assign(M[0], {sc: SC, v54: o}), Object.assign(M[1], {v54: o})); });
  const R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY));
  const r3 = x => +x.toFixed(3);
  rows.forEach((v, i) => { const B = R[2*i], M = R[2*i + 1], o = out.rows[v] = {switches: VAR[v], base: {}, prog: {}, d: {}};
    K.forEach(k => { if (B[k] === undefined) return; const f = k === 'endoAnn' ? 100 : 1, q = H.tbDiff(M, B, k); o.base[k] = r3(B[k]*f); o.prog[k] = r3(M[k]*f); o.d[k] = [r3(q.m*f), r3(q.lo*f), r3(q.hi*f)]; }); });
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const dir = path.join(ROOT, 'dev', 'runs', 'v54'); fs.mkdirSync(dir, {recursive: true});
const file = path.join(dir, (arg('out') || 'check') + '-' + env + (YRS === 40 ? '-40' : '') + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
const f = x => (x >= 0 ? '+' : '') + (Math.abs(x) >= 100 ? x.toFixed(0) : x.toFixed(2));
console.log('v5.4 check, ' + env + ', seeds 1-' + N + ', ' + YRS + ' years (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
rows.forEach(v => { const o = out.rows[v]; console.log('[' + v + ']'); K.filter(k => o.base[k] !== undefined).forEach(k => console.log('  ' + k.padEnd(14) + String(o.base[k]).padStart(10) + ' -> ' + String(o.prog[k]).padEnd(10) + ' ' + f(o.d[k][0]) + ' [' + f(o.d[k][1]) + ', ' + f(o.d[k][2]) + ']')); });
