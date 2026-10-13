#!/usr/bin/env node
/* Session 2a (Oct 13, 2026; dev/reports/v5-25-health-today.md): the health settings' paired check. For each variant, the v5.4 release row and its no-programme
 * run, both with the variant's health setting, paired by seed. Reports both runs' levels, the programme's paired effect, and, against the variant 'off'
 * (no health setting: the released model), how far the setting moves that effect (the difference of the paired effects, seed by seed, with a 95% interval).
 * Setting B rows are compared against setting A (the health and Compassionism interaction: how much the programme's effect changes when single payer replaces
 * today's system), setting A rows against 'off'.
 * Usage: node dev/tools/health_check.js ref|adv|st [SEEDS] [--rows=off,A,Anx,B,...] [--out=NAME] [--theta=X] [--flat]
 * --theta=X sets the medical price response to extra demand (PM_DEFAULTS.theta.medical, 0.5 as released) in every row; --flat holds prices flat (pass-through 0,
 * every essentials' response 0): the difference between a run with prices free and one with --flat is the part that comes through prices.
 * Output: dev/runs/health/NAME-ENV.json (NAME defaults to 'check'). */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : null; };
const pos = process.argv.slice(2).filter(x => !x.startsWith('--'));
const env = pos[0] || 'ref', N = +(pos[1] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME || !(N >= 2)) { console.error('usage: health_check.js ref|adv|st [SEEDS >= 2] [--rows=off,A,...]'); process.exit(1); }
/* The variants: the row option hl (undefined = the health setting off). */
const VAR = {off: undefined, A: {}, Anx: {exp: false}, Askip25: {skip: 0.25}, Askip75: {skip: 0.75}, Apers80: {persist: 0.8}, Apers95: {persist: 0.95},
  B: {set: 'B'}, Bcau: {set: 'B', cs: 'cautious'}, Bhigh: {set: 'B', cs: 'high'}, Bnx: {set: 'B', exp: false}, Bcap25: {set: 'B', cap: 0.25}, Bcap100: {set: 'B', cap: 1}, Badm0: {set: 'B', adm: 0}, Badm2: {set: 'B', adm: 0.02}, Bind0: {set: 'B', induce: 0}};
const REF = v => VAR[v] && VAR[v].set === 'B' ? (VAR[v].exp === false ? 'Anx' : 'A') : 'off';
const rows = (arg('rows') || 'off,A,Anx').split(',');
rows.forEach(v => { if (!(v in VAR)) { console.error('unknown variant ' + v + ' (known: ' + Object.keys(VAR).join(', ') + ')'); process.exit(1); } });
if (rows.some(v => REF(v) === 'Anx') && rows.indexOf('Anx') < 0) rows.unshift('Anx');
if (rows.some(v => REF(v) === 'A') && rows.indexOf('A') < 0) rows.unshift('A');
if (rows.indexOf('off') < 0) rows.unshift('off'); else if (rows[0] !== 'off'){ rows.splice(rows.indexOf('off'), 1); rows.unshift('off'); }
const ROOT = path.join(__dirname, '..', '..'), t0 = Date.now(), SC = H.SPEND_SOURCED, C = H.CFG;
const K = ['fgt0PY', 'fgt2PY', 'pov', 'bOAPy', 'cost', 'medWealthReal', 'pLev20', 'giniD', 'hrs'];
const KH = H.HL_KEYS;
const FLAT = process.argv.includes('--flat'), PMX = FLAT ? {lamG: 0, theta: {food: 0, housing: 0, medical: 0}} : arg('theta') !== null ? {theta: {medical: +arg('theta')}} : {};
const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
const cmd = 'node dev/tools/health_check.js ' + env + ' ' + N + ' --rows=' + rows.join(',') + (arg('out') ? ' --out=' + arg('out') : '') + (FLAT ? ' --flat' : PMX.theta ? ' --theta=' + arg('theta') : '');
const out = {_meta: {what: 'health settings: the v5.4 release row and its no-programme run under each variant, paired by seed; vsRef: the change in the programme\'s paired effect against the reference setting (A against off, B against A)', env, seeds: N, manifest: H.runManifest(), command: cmd, health: H.HEALTH_DEFAULTS}, rows: {}};
const r3 = x => +(+x).toFixed(3);
function pd(a, b, k){ const n = a._s[k].length; let m = 0, v = 0; const d = []; for (let i = 0; i < n; i++) d.push(a._s[k][i] - b._s[k][i]); d.forEach(x => { m += x/n; }); d.forEach(x => { v += (x - m)*(x - m)/(n - 1); }); const h = 1.96*Math.sqrt(v/n); return {m, lo: m - h, hi: m + h, d}; }
try {
  const P = Object.assign({}, H[NAME]), PR = H.tbPresets(P), cfg = [];
  rows.forEach(v => { const M = H.relMainCfgs(PR), hl = VAR[v]; cfg.push(Object.assign(M[0], hl ? {hl} : {}), Object.assign(M[1], {sc: SC}, hl ? {hl} : {})); });
  const R = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: SC}, H.REL_V52_STUDY, PMX));
  const at = {}; rows.forEach((v, i) => { at[v] = {B: R[2*i], M: R[2*i + 1]}; });
  rows.forEach((v, i) => { const B = R[2*i], M = R[2*i + 1], o = out.rows[v] = {hl: VAR[v] || null, ref: v === 'off' ? null : REF(v), base: {}, prog: {}, d: {}, vsRef: {}};
    K.concat(v === 'off' ? [] : KH).forEach(k => { if (B[k] === undefined) return; const q = pd(M, B, k); o.base[k] = r3(B[k]); o.prog[k] = r3(M[k]); o.d[k] = [r3(q.m), r3(q.lo), r3(q.hi)];
      if (v !== 'off' && K.indexOf(k) >= 0){ const q0 = pd(at[REF(v)].M, at[REF(v)].B, k), n = q.d.length; let m = 0, s = 0; const dd = q.d.map((x, j) => x - q0.d[j]); dd.forEach(x => { m += x/n; }); dd.forEach(x => { s += (x - m)*(x - m)/(n - 1); }); const h = 1.96*Math.sqrt(s/n); o.vsRef[k] = [r3(m), r3(m - h), r3(m + h)]; } }); });
} finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const dir = path.join(ROOT, 'dev', 'runs', 'health'); fs.mkdirSync(dir, {recursive: true});
const file = path.join(dir, (arg('out') || 'check') + '-' + env + '.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
const f = x => (x >= 0 ? '+' : '') + (Math.abs(x) >= 100 ? x.toFixed(0) : x.toFixed(2));
console.log('health check, ' + env + ', seeds 1-' + N + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
rows.forEach(v => { const o = out.rows[v]; console.log('[' + v + ']');
  Object.keys(o.base).forEach(k => console.log('  ' + k.padEnd(14) + String(o.base[k]).padStart(10) + ' -> ' + String(o.prog[k]).padEnd(10) + ' ' + f(o.d[k][0]) + ' [' + f(o.d[k][1]) + ', ' + f(o.d[k][2]) + ']' + (o.vsRef[k] ? '   vs ' + o.ref + ': ' + f(o.vsRef[k][0]) + ' [' + f(o.vsRef[k][1]) + ', ' + f(o.vsRef[k][2]) + ']' : ''))); });
