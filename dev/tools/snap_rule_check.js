#!/usr/bin/env node
/* Session 7 (Oct 14, 2026; ledger step s166, decision d209): the guard for SNAP's work rule (SNET.abawd, off by default).
 * The guard test (guard_test.js) runs no row with today's safety net, so it cannot see the SNAP block. This runs the v5.4 main row and its
 * no-programme run with today's safety net (row option sn), seeds 1-N, in one environment, and compares every testbed output, as raw 64-bit
 * numbers hashed per row, with a reference made before the rule was added (dev/runs/guard/snap-ENV.json). With the rule off the outputs must be
 * identical. --on also runs both rows with the rule on and prints what moved (no reference is written for that).
 * --out=FILE (with --on and one --env): also write every output's mean for the four rows and, for the headline measures, each seed's value, so the
 * rule's own effect (rule on minus rule off, paired by seed) can be read at 500 seeds (the s165 study; the reference check is skipped). --years=40: 40 years.
 * Usage: node dev/tools/snap_rule_check.js [--write] [--on] [--env=ref|adv|st] [--seeds=20] [--years=40] [--out=FILE]   (no --env: the three environments at once) */
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto'), cp = require('child_process');
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : null; };
const WRITE = process.argv.includes('--write'), ON = process.argv.includes('--on'), N = +(arg('seeds') || 20), ENVS = (arg('env') || 'ref,adv,st').split(','), OUT = arg('out'), YRS = +(arg('years') || 0);
const ROOT = path.join(__dirname, '..', '..'), DIR = path.join(ROOT, 'dev', 'runs', 'guard');
const HEAD = ['fgt0PY', 'fgt2PY', 'pov', 'bOAPy', 'snSnap', 'snSnapM', 'snAll', 'hrs', 'emp', 'snAbN', 'snAbM', 'snAbLost'];

if (ENVS.length > 1){
  let bad = 0, left = ENVS.length;
  ENVS.forEach(e => { const c = cp.fork(__filename, process.argv.slice(2).filter(a => !a.startsWith('--env=')).concat('--env=' + e), {stdio: 'inherit'});
    c.on('exit', code => { if (code) bad++; if (--left === 0){ console.log(bad ? 'SNAP RULE CHECK FAILED (' + bad + ')' : 'snap rule check passed'); process.exit(bad ? 1 : 0); } }); });
} else run(ENVS[0]);

function run(env){
  const H = require(path.join(ROOT, 'harness.js')), C = H.CFG, SC = H.SPEND_SOURCED, t0 = Date.now(), file = path.join(DIR, 'snap-' + env + '.json');
  const ref = WRITE || OUT ? null : JSON.parse(fs.readFileSync(file, 'utf8')), KEYS = ref ? ref._meta.keyList : H.TB_KEYS.slice();
  const P0 = {ref: H.FULL_INTEGRATION, adv: H.ADVERSE_REFERENCE, st: H.STRESS_TEST}[env];
  const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000; const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), out = {};
  let S;
  try {
    const P = Object.assign({}, P0, YRS ? {years: YRS} : {}), PR = H.tbPresets(P), base = {sc: SC, so: H.REL_V52_STUDY, hh: H.REL_V53.hh, sg: true, g: H.ACCT_V53, em: true, fb: true, v54: H.REL_V54.v54};
    const R = H.releaseRowsV54(SC).filter(r => r.j === 'release')[0], main = H.n1Row(PR, 'framework', R.v); if (R.v.o) Object.assign(main.o || (main.o = {}), R.v.o);
    const cfg = [Object.assign({p: PR.baseline()}, base, {sn: {}}), Object.assign({}, main, {sn: {}})], names = ['base+sn', 'release+sn'];
    if (ON){ cfg.push(Object.assign({p: PR.baseline()}, base, {sn: {abawd: true}}), Object.assign({}, main, {sn: {abawd: true}})); names.push('base+sn+rule', 'release+sn+rule'); }
    S = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0}, H.REL_V52_STUDY, {sc: SC}));
    S.forEach((r, i) => { const h = crypto.createHash('sha256');
      KEYS.forEach(k => { h.update(k); h.update(Buffer.from(r._s[k].buffer, r._s[k].byteOffset, r._s[k].byteLength)); });
      const m = {}; HEAD.forEach(k => { m[k] = r[k]; }); out[names[i]] = {hash: h.digest('hex'), mean: m}; });
  } finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
  const secs = Math.round((Date.now() - t0)/1000);
  if (ON) ['base', 'release'].forEach(j => { const a = out[j + '+sn'].mean, b = out[j + '+sn+rule'].mean;
    console.log('[' + env + '] ' + j + ', rule off -> on: ' + HEAD.filter(k => a[k] !== undefined || b[k] !== undefined).map(k => k + ' ' + (+a[k] || 0).toFixed(3) + ' -> ' + (+b[k] || 0).toFixed(3)).join('; ')); });
  if (OUT){ const rows = {}; Object.keys(out).forEach((j, i) => { const r = S[i], m = {}, seeds = {};
      Object.keys(r).filter(k => typeof r[k] === 'number').forEach(k => { m[k] = r[k]; }); HEAD.forEach(k => { if (r._s[k]) seeds[k] = Array.from(r._s[k]); });
      rows[j] = {mean: m, seeds}; });
    fs.writeFileSync(OUT, JSON.stringify({_meta: {what: 'SNAP work rule, its own effect: the v5.4 main row and its no-programme run with today\'s safety net, rule off and on, paired seeds 1-' + N + ' (dev/tools/snap_rule_check.js)',
      env, seeds: N, years: YRS || 20, command: 'node dev/tools/snap_rule_check.js ' + process.argv.slice(2).join(' '), manifest: H.runManifest(), written: new Date().toISOString(), seconds: secs}, rows}));
    console.log('[' + env + '] wrote ' + OUT + ' (' + secs + ' s)'); return; }
  if (WRITE){ fs.mkdirSync(DIR, {recursive: true}); const rows = {}; ['base+sn', 'release+sn'].forEach(j => { rows[j] = out[j]; });
    fs.writeFileSync(file, JSON.stringify({_meta: {what: 'SNAP work rule guard: every testbed output of the v5.4 main row and its no-programme run with today\'s safety net, rule absent, seeds 1-' + N + ' (dev/tools/snap_rule_check.js)', env, seeds: N, keyList: KEYS, manifest: H.runManifest(), written: new Date().toISOString()}, rows}, null, 1));
    console.log('[' + env + '] wrote ' + path.relative(ROOT, file) + ' (' + secs + ' s)'); return; }
  const bad = [];
  Object.keys(ref.rows).forEach(j => { const a = ref.rows[j], b = out[j];
    if (a.hash !== b.hash){ const mv = HEAD.filter(k => a.mean[k] !== b.mean[k] && !(Number.isNaN(a.mean[k]) && Number.isNaN(b.mean[k]))).map(k => k + ' ' + a.mean[k] + ' -> ' + b.mean[k]);
      bad.push(j + ': ' + (mv.length ? mv.join('; ') : 'per-seed outputs differ (headline means unchanged)')); } });
  if (bad.length){ console.log('[' + env + '] FAILED (' + secs + ' s):\n  ' + bad.join('\n  ')); process.exit(1); }
  console.log('[' + env + '] rule off, identical: ' + Object.keys(ref.rows).length + ' rows x ' + N + ' seeds x ' + KEYS.length + ' outputs (' + secs + ' s)');
}
