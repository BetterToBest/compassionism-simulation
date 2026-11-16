#!/usr/bin/env node
/* S74 pilot (research-update prereg/2026-11-s74-central-bank.md, "Pilot", and Amendment 1): the frozen round-2 main pair (r2FreezePair: no programme,
 * programme) in each arm of one environment, both designs, seeds 1..N, 500 adults, with the stability measures (study option stab).
 * Arms: Reference, Adverse, Stress: 'off' (today's engine) and 'cb' (the policy-rate rule at its main values, forced sales on).
 *       History (21 years, 2005-2025): 'infl' (today's reading of rates: no central bank), 'actual' (the actual rate path), 'cb' (the rule).
 * Usage: node dev/tools/s74_pilot.js ENV [SEEDS] [--design=c22,rel] [--out=DIR]   (ENV ref | adv | st | hx; SEEDS 100)
 * Writes DIR/s74-pilot-ENV.json (default DIR dev/runs/s74-pilot): per design, arm and row, every saved key's per-seed values. */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0], N = +(ARG[1] || 100), designs = (opt('design') || 'c22,rel').split(','), dir = opt('out') || path.join(__dirname, '..', 'runs', 's74-pilot'), t0 = Date.now();
const ENV = {ref: H.FULL_INTEGRATION, adv: H.ADVERSE_REFERENCE, st: H.STRESS_TEST, hx: H.HISTORY_ENV}[env];
if (!ENV) { console.error('ENV must be ref, adv, st or hx'); process.exit(1); }
const ARMS = env === 'hx' ? ['infl', 'actual', 'cb'] : ['off', 'cb'];
const KEEP = /^(fgt0PY|fgt0|pov|pf0_\d+|ppov_\d+|endoAnn|endoMax|medWealthReal|cost|st[A-Z]|rk[A-Z]|cb[A-Z]|fs[A-Z]|wg[A-Z]|wt(T1|T10|B50|Mean|Med)[SE]$|gv(Rate|Debt))/;
const out = {_meta: {what: 'S74 pilot: the frozen round-2 main pair in each arm, with the stability measures', env, seeds: N, designs, arms: ARMS,
  command: 'node dev/tools/s74_pilot.js ' + process.argv.slice(2).join(' '), manifest: H.runManifest(), started: new Date().toISOString()}};
designs.forEach(d => { out[d] = {}; ARMS.forEach(arm => {
  const t = Date.now(), P = Object.assign({}, ENV, {years: env === 'hx' ? H.HISTORY_ENV.years : 20, nAgents: 500});
  if (env === 'hx') P.hx = {rp: arm === 'infl' ? 'infl' : 'actual'};
  const cf = H.r2FreezePair(P, d); if (arm === 'cb') cf.forEach(c => { c.cb = {}; });
  const R = H.tbStudy(cf, N, P, Object.assign(H.r2MainStudy(), {stab: true}));
  out[d][arm] = R.map(r => { const o = {}; Object.keys(r._s).filter(k => KEEP.test(k)).forEach(k => { o[k] = Array.from(r._s[k]); }); return o; });
  process.stderr.write(env + ' ' + d + ' ' + arm + ' ' + ((Date.now() - t)/1000).toFixed(0) + ' s\n'); }); });
out._meta.secs = (Date.now() - t0)/1000;
fs.mkdirSync(dir, {recursive: true}); fs.writeFileSync(path.join(dir, 's74-pilot-' + env + '.json'), JSON.stringify(out));
console.log(env + ': ' + designs.length + ' designs x ' + ARMS.length + ' arms x ' + N + ' seeds, ' + out._meta.secs.toFixed(0) + ' s');
