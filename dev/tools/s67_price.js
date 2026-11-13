#!/usr/bin/env node
/* S67 (Nov 13, 2026; research-update prereg/2026-11-s67-price-rule-derivation.md, Part C and Amendment 1): the pilot of the price rule's new readings. On S58's
 * yardstick (frozenRow, CPS earnings, today's safety net, the money-flow table on every row): the no-programme run under today's rule and the capacity rule; the
 * release row and the C2.2 design under both (these six reproduce S58's rows); then the within-year readings (wy: four sub-steps with values fitted on quarterly
 * data; wyroot: four sub-steps with the yearly rule's roots; qt4: today's rule in four sub-steps), the velocity response (vel, velh; qtvel on today's rule) and the
 * velocity drift (drift; qtdrift on today's rule). Same seeds, one environment per call. Writes every run's per-seed values of the outcome keys, the yearly path
 * keys, PR_KEYS and MF_KEYS as JSON; dev/tools/s67_table.py makes the tables and the paired bootstrap.
 * Usage: node dev/tools/s67_price.js ENV [SEEDS] [YEARS] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const Y = {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}};
/* name, programme (0 none, 1 release, 2 C2.2), price rule (undefined = today's) */
const QT = {k: 1, r: 0, a: 0, h: 0, rs: false}, WY = {q: 4, k: 0.0788, k2: 0, r: 0.2333};
const ROWS = [['np', 0], ['np-cap', 0, true], ['rel', 1], ['rel-cap', 1, true], ['c22', 2], ['c22-cap', 2, true],
  ['c22-wy', 2, WY], ['c22-wyroot', 2, {q: 4, a: 0, r: 0.9406, k: 0.0317, k2: 0.0036}], ['c22-qt4', 2, Object.assign({q: 4}, QT)],
  ['c22-vel', 2, {bv: 0.0043}], ['c22-velh', 2, {bv: 0.0022}], ['c22-qtvel', 2, Object.assign({k2: 1, bv: 0.0043}, QT)],
  ['c22-drift', 2, {bd: 0.132}], ['c22-qtdrift', 2, Object.assign({bd: 0.132}, QT)], ['rel-wy', 1, WY], ['rel-vel', 1, {bv: 0.0043}], ['rel-drift', 1, {bd: 0.132}]];
const OUTK = ['endoAnn', 'endoMax', 'pLev10', 'pLev20', 'pov', 'fgt0PY', 'hhCostPY', 'bOAPy', 'medWealthReal', 'srcPay', 'srcM', 'srcTax', 'cost', 'eGiniW', 'eGiniWN', 'hhDebt20']
  .concat(H.TB_PLV_KEYS || []).concat(H.PR_KEYS, H.MF_KEYS)
  .concat(['f0', 'pov', 'medW'].reduce((r, m) => r.concat(Array.from({length: YRS}, (_, t) => 'p' + m + '_' + t)), []));
const out = {_meta: {what: 'S67: the price rule's new readings, pilot (research-update prereg/2026-11-s67-price-rule-derivation.md, Amendment 1)', env, seeds: N, years: YRS, yardstick: Y, frozen: H.FROZEN,
  defaults: H.PR_DEFAULTS, manifest: H.runManifest(), command: 'node dev/tools/s67_price.js ' + process.argv.slice(2).join(' '), rows: ROWS.map(r => ({name: r[0], prog: r[1], pr: r[2] || 'qt'}))}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED, mf: true}, H.REL_V52_STUDY);
  const mk = r => { const c = H.frozenRow(Object.assign(H.relMainCfgs(PR)[r[1] ? 1 : 0], JSON.parse(JSON.stringify(Y)), r[2] ? {pr: JSON.parse(JSON.stringify(r[2]))} : {})); return r[1] === 2 ? H.c22Design(c) : c; };
  const R = H.tbStudy(ROWS.map(mk), N, P, so);
  ROWS.forEach((r, i) => { out.rows[r[0]] = {}; OUTK.forEach(k => { if (R[i]._s[k]) out.rows[r[0]][k] = Array.from(R[i]._s[k]); }); });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's67-price', 's67-price-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out));
const m = (r, k) => { const v = out.rows[r][k]; return v ? v.reduce((s, x) => s + x, 0)/v.length : NaN; };
console.log(env, 'programme inflation (points a year): C2.2 today ' + (100*m('c22', 'endoAnn')).toFixed(1) + ', capacity ' + (100*m('c22-cap', 'endoAnn')).toFixed(1) + ', within-year ' + (100*m('c22-wy', 'endoAnn')).toFixed(1) +
  ', drift ' + (100*m('c22-drift', 'endoAnn')).toFixed(1) + '; wrote ' + file + ' (' + out._meta.seconds + ' s)');
