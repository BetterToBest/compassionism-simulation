#!/usr/bin/env node
/* S58 (Nov 9, 2026; research-update prereg/2026-11-s58-price-rule.md, Amendment 1): the capacity price rule pilot. On the frozen yardstick (frozenRow, CPS
 * earnings, today's safety net) with the money-flow table on every row (study option mf, reporting only): the no-programme run under today's rule and the
 * capacity rule, the release row and the C2.2 design under both rules, and the C2.2 design over the preregistered sweep, same seeds, one environment per
 * call. Writes every run's per-seed values of the outcome keys, PR_KEYS and MF_KEYS as JSON; dev/tools/s58_table.py makes the tables and the paired bootstrap.
 * Usage: node dev/tools/s58_price.js ENV [SEEDS] [YEARS] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const Y = {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}};
/* name, programme (0 none, 1 release, 2 C2.2), price rule (undefined = today's) */
const ROWS = [['np', 0], ['np-cap', 0, true], ['rel', 1], ['rel-cap', 1, true], ['rel-k25', 1, {k: 0.25}],
  ['c22', 2], ['c22-cap', 2, true], ['c22-k25', 2, {k: 0.25}], ['c22-k1', 2, {k: 1}], ['c22-r0', 2, {r: 0}], ['c22-r45', 2, {r: 0.45}], ['c22-a0', 2, {a: 0}],
  ['c22-h', 2, {h: {gen: 0.0446}}], ['c22-k2z', 2, {k2: 0}], ['c22-k2h', 2, {k2: 0.657}], ['c22-nest', 2, {k: 1, r: 0, a: 0, h: 0}]];
const OUTK = ['endoAnn', 'endoMax', 'pLev10', 'pLev20', 'pov', 'fgt0PY', 'hhCostPY', 'bOAPy', 'medWealthReal', 'srcPay', 'srcM', 'srcTax', 'cost', 'eGiniW', 'eGiniWN', 'hhDebt20']
  .concat(H.TB_PLV_KEYS || []).concat(H.PR_KEYS, H.MF_KEYS);
const out = {_meta: {what: 'S58: the capacity price rule pilot (research-update prereg/2026-11-s58-price-rule.md, Amendment 1)', env, seeds: N, years: YRS, yardstick: Y, frozen: H.FROZEN,
  defaults: H.PR_DEFAULTS, manifest: H.runManifest(), command: 'node dev/tools/s58_price.js ' + process.argv.slice(2).join(' '), rows: ROWS.map(r => ({name: r[0], prog: r[1], pr: r[2] || 'qt'}))}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED, mf: true}, H.REL_V52_STUDY);
  const mk = r => { const c = H.frozenRow(Object.assign(H.relMainCfgs(PR)[r[1] ? 1 : 0], JSON.parse(JSON.stringify(Y)), r[2] ? {pr: JSON.parse(JSON.stringify(r[2]))} : {})); return r[1] === 2 ? H.c22Design(c) : c; };
  const R = H.tbStudy(ROWS.map(mk), N, P, so);
  ROWS.forEach((r, i) => { out.rows[r[0]] = {}; OUTK.forEach(k => { if (R[i]._s[k]) out.rows[r[0]][k] = Array.from(R[i]._s[k]); }); });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's58-price', 's58-price-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out));
const m = (r, k) => { const v = out.rows[r][k]; return v ? v.reduce((s, x) => s + x, 0)/v.length : NaN; };
console.log(env, 'programme inflation (points a year): C2.2 today ' + (100*m('c22', 'endoAnn')).toFixed(1) + ', capacity ' + (100*m('c22-cap', 'endoAnn')).toFixed(1) +
  '; pass-through after 19 years ' + m('c22-cap', 'prPT19').toFixed(3) + '; wrote ' + file + ' (' + out._meta.seconds + ' s)');
