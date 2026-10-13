#!/usr/bin/env node
/* Session 2a (Oct 13, 2026; dev/DECISIONS.md Session 2a, d-guard): the guard test. It reruns 20 fixed seeds (1-20) of a set of v5.4 release-panel rows
 * (the main row, its no-programme run, and the readings that turn each of the model's parts on or off) in the Reference, Adverse and Stress
 * environments, and fails if any figure changes. "Any figure" means every testbed output (TB_KEYS) for every seed, compared as raw 64-bit
 * numbers through a SHA-256 hash per row; a handful of headline means are stored beside each hash so a failure says what moved.
 * The reference (dev/runs/guard/guard-ENV.json) was made on main 0f2e42e (v5.4.1; the engine is v5.4's) before any engine edit. A new mechanism
 * behind a switch must leave it unchanged with the switch off; a deliberate change to released figures must re-write it (--write) and say why.
 * Usage: node dev/tools/guard_test.js [--write] [--env=ref,adv,st] [--seeds=20]
 * Without --env the three environments run as three child processes at once (about 3 minutes on 4 cores). Exit code 1 on any difference. */
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto'), cp = require('child_process');
const arg = k => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.split('=')[1] : null; };
const WRITE = process.argv.includes('--write'), N = +(arg('seeds') || 20), ENVS = (arg('env') || 'ref,adv,st').split(',');
const ROOT = path.join(__dirname, '..', '..'), DIR = path.join(ROOT, 'dev', 'runs', 'guard');
/* The rows (by their panel names, harness.js releaseRowsV54 / releaseBasesV54): every v5.4 part on and off, ageing, households off, savings that
 * keep up with prices, the other financing readings. Each no-programme pair a row needs is listed too. */
const ROWS = ['v422', 'release', 'v53', 'cut0', 'autopay', 'pthbold', 'ptfs25', 'dis', 'h1', 'tax', 'progtax', 'age', 'indiv', 'adults', 'sav', 'fbs50'];
const BASES = ['b53', 'bcut0', 'bautopay', 'bdis', 'ag', 'bindiv', 'badults', 'sv'];
const HEAD = ['fgt0PY', 'fgt2PY', 'pov', 'bOAPy', 'cost', 'medWealthReal', 'pLev20', 'giniD', 'hrs', 'emp'];

if (ENVS.length > 1){
  let bad = 0, left = ENVS.length;
  ENVS.forEach(e => { const c = cp.fork(__filename, process.argv.slice(2).filter(a => !a.startsWith('--env=')).concat('--env=' + e), {stdio: 'inherit'});
    c.on('exit', code => { if (code) bad++; if (--left === 0){ console.log(bad ? 'GUARD TEST FAILED (' + bad + ' environment' + (bad > 1 ? 's' : '') + ')' : (WRITE ? 'guard references written' : 'guard test passed: every figure identical')); process.exit(bad ? 1 : 0); } }); });
} else run(ENVS[0]);

function run(env){
  const H = require(path.join(ROOT, 'harness.js')), C = H.CFG, SC = H.SPEND_SOURCED, t0 = Date.now(), file = path.join(DIR, 'guard-' + env + '.json');
  /* The outputs compared are the reference's own list, so an output added later (a new mechanism's figures) does not count as a change. */
  const ref = WRITE ? null : JSON.parse(fs.readFileSync(file, 'utf8')), KEYS = ref ? ref._meta.keyList : H.TB_KEYS.slice();
  const lost = KEYS.filter(k => H.TB_KEYS.indexOf(k) < 0);
  if (lost.length){ console.log('[' + env + '] FAILED: outputs no longer produced: ' + lost.join(', ')); process.exit(1); }
  const P0 = {ref: H.FULL_INTEGRATION, adv: H.ADVERSE_REFERENCE, st: H.STRESS_TEST}[env];
  if (!P0){ console.error('unknown environment ' + env + ' (ref, adv, st)'); process.exit(2); }
  const R = H.releaseRowsV54(SC), B = H.releaseBasesV54(SC), pick = (L, j) => { const x = L.filter(r => r.j === j)[0]; if (!x) throw new Error('no panel row ' + j); return x; };
  /* As the testbed's release section builds them (harness.js stepSection): the debt floor, the NR6 profile and TB_PROFILE_G; the no-programme
   * run with the panel's shared settings; each programme row through n1Row (framework model); the study options of the v5.4 panel. */
  const wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000; const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), out = {};
  try {
    const P = Object.assign({}, P0), PR = H.tbPresets(P), base = {sc: SC, so: H.REL_V52_STUDY, hh: H.REL_V53.hh, sg: true, g: H.ACCT_V53, em: true, fb: true, v54: H.REL_V54.v54};
    const names = ['base'], cfg = [Object.assign({p: PR.baseline()}, base)];
    ROWS.forEach(j => { const r = pick(R, j), c = H.n1Row(PR, 'framework', r.v); if (r.v.o) Object.assign(c.o || (c.o = {}), r.v.o); names.push(j); cfg.push(c); });
    BASES.forEach(j => { names.push(j); cfg.push(Object.assign({p: PR.baseline()}, pick(B, j).v)); });
    const S = H.tbStudy(cfg, N, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0}, H.REL_V52_STUDY, {sc: SC}));
    S.forEach((r, i) => { const h = crypto.createHash('sha256');
      KEYS.forEach(k => { h.update(k); h.update(Buffer.from(r._s[k].buffer, r._s[k].byteOffset, r._s[k].byteLength)); });
      const m = {}; HEAD.forEach(k => { m[k] = r[k]; }); out[names[i]] = {hash: h.digest('hex'), mean: m}; });
  } finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; }
  const secs = Math.round((Date.now() - t0)/1000);
  if (WRITE){ fs.mkdirSync(DIR, {recursive: true});
    fs.writeFileSync(file, JSON.stringify({_meta: {what: 'guard test reference: every testbed output of these rows, seeds 1-' + N + ', hashed per row (dev/tools/guard_test.js)', env, seeds: N, keyList: KEYS, manifest: H.runManifest(), written: new Date().toISOString().slice(0, 10)}, rows: out}, null, 1) + '\n');
    console.log('[' + env + '] wrote ' + path.relative(ROOT, file) + ' (' + Object.keys(out).length + ' rows, ' + secs + ' s)'); return; }
  if (ref._meta.seeds !== N){ console.error('[' + env + '] the reference has ' + ref._meta.seeds + ' seeds; run with --seeds=' + ref._meta.seeds); process.exit(2); }
  const bad = [];
  Object.keys(ref.rows).forEach(j => { const a = ref.rows[j], b = out[j];
    if (!b){ bad.push(j + ': missing'); return; }
    if (a.hash !== b.hash){ const mv = HEAD.filter(k => a.mean[k] !== b.mean[k] && !(Number.isNaN(a.mean[k]) && Number.isNaN(b.mean[k]))).map(k => k + ' ' + a.mean[k] + ' -> ' + b.mean[k]);
      bad.push(j + ': ' + (mv.length ? mv.join('; ') : 'per-seed outputs differ (headline means unchanged)')); } });
  if (bad.length){ console.log('[' + env + '] FAILED (' + secs + ' s):\n  ' + bad.join('\n  ')); process.exit(1); }
  console.log('[' + env + '] identical: ' + Object.keys(ref.rows).length + ' rows x ' + N + ' seeds x ' + KEYS.length + ' outputs (' + secs + ' s)');
}
