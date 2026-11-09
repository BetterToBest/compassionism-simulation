#!/usr/bin/env node
/* S57 (Nov 9, 2026; research-update prereg/2026-11-s57-distribution-measures.md): the distribution-measures pilot. Study option dm (reporting only) on the frozen
 * yardstick (frozenRow, CPS earnings, today's safety net): the no-programme run, the release row and the C2.2 design, same seeds, one environment per call.
 * Writes every run's per-seed values of every dm key (and eGiniW, eGiniWN) as JSON; dev/tools/s57_table.py makes the tables and the paired bootstrap.
 * Usage: node dev/tools/s57_dm.js ENV [SEEDS] [YEARS] [--out=FILE]   (ENV ref, adv or st; default 100 seeds, 20 years) */
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0] || 'ref', N = +(ARG[1] || 100), YRS = +(ARG[2] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
if (!NAME) { console.error('environment must be ref, adv or st'); process.exit(1); }
const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
const Y = {sn: {abawd: true, slope: true}, lt: {s: 'all', m: 'all'}};
const KEYS = H.DM_KEYS.concat(['eGiniW', 'eGiniWN', 'y0GiniW', 'y0GiniWN', 'hhDebt20', 'fgt0PY', 'pov']);
const out = {_meta: {what: 'S57: distribution measures pilot (research-update prereg/2026-11-s57-distribution-measures.md)', env, seeds: N, years: YRS, yardstick: Y, frozen: H.FROZEN,
  manifest: H.runManifest(), command: 'node dev/tools/s57_dm.js ' + process.argv.slice(2).join(' '), rows: ['np', 'rel', 'c22'], grid: H.DM_GRID}, rows: {}};
try {
  const P = Object.assign({}, H[NAME], {years: YRS}), PR = H.tbPresets(P), so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED, dm: true}, H.REL_V52_STUDY);
  const base = () => H.relMainCfgs(PR), mk = (i, c22) => { const c = H.frozenRow(Object.assign(base()[i], Y)); return c22 ? H.c22Design(c) : c; };
  const R = H.tbStudy([mk(0, false), mk(1, false), mk(1, true)], N, P, so);
  ['np', 'rel', 'c22'].forEach((nm, i) => { out.rows[nm] = {}; KEYS.forEach(k => { if (R[i]._s[k]) out.rows[nm][k] = Array.from(R[i]._s[k]); }); });
} finally { H.resetNR6(svN); H.tbSetG(svG); }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const file = opt('out') || path.join(__dirname, '..', 'runs', 's57-distribution', 's57-dm-' + env + '.json');
fs.mkdirSync(path.dirname(file), {recursive: true}); fs.writeFileSync(file, JSON.stringify(out));
const np = out.rows.np, m = k => (np[k].reduce((s, x) => s + x, 0)/np[k].length).toFixed(2);
console.log(env, 'no programme, start: top 1% ' + m('dmWt1S') + '%, top 10% ' + m('dmWt10S') + '%, bottom 50% ' + m('dmWb50S') + '%; wrote ' + file + ' (' + out._meta.seconds + ' s)');
