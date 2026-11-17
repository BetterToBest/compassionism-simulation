#!/usr/bin/env node
/* S74 part 3: the forward sweep (research-update prereg/2026-11-s74-central-bank.md, "What is built" item 3, and Amendments 1 and 2). The frozen
 * round-2 main pair (r2FreezePair: no programme, programme) in each setting of one environment, both designs, seeds 1..N (20), 500 adults, with
 * the stability measures (study option stab). One setting is varied at a time from the rule's main values (CB_DEFAULTS); three named regimes;
 * the design parameters' readings. Descriptive: fans and ranges, no claims of significance.
 * Usage: node dev/tools/s74_sweep.js ENV [SEEDS] [--design=c22,rel] [--only=name,name] [--out=DIR]   (ENV ref | adv | st | hx; SEEDS 20)
 * Writes DIR/s74-sweep-ENV.json (default DIR dev/runs/s74-sweep): per design, setting and row, every saved key's per-seed values (6 significant
 * digits). */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
/* S76 (prereg Amendment 4): the release's global settings, as the round-2 runner sets them (compassionism-sim-results runner/jobs/r2.js); without them
 * the main row's switches run under the engine's older defaults, not release 2's main row. */
const svS = H.startRelease({baseline: true});  /* S84: and the no-programme arm must equal the release per seed (data/baseline.json), or the run stops */
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const env = ARG[0], N = +(ARG[1] || 20), designs = (opt('design') || 'c22,rel').split(','), dir = opt('out') || path.join(__dirname, '..', 'runs', 's74-sweep'), t0 = Date.now();
const ENV = {ref: H.FULL_INTEGRATION, adv: H.ADVERSE_REFERENCE, st: H.STRESS_TEST, hx: H.HISTORY_ENV}[env];
if (!ENV) { console.error('ENV must be ref, adv, st or hx'); process.exit(1); }
/* name: [cb options or null (no central bank), hx options in History]. 'off' in History is hx.rp 'infl' (no central bank, Amendment 1). */
const S = {
  off: [null, {rp: 'infl'}], main: [{}],
  a1: [{a: 1}], 'a1.5': [{a: 1.5}], a2: [{a: 2}],
  b0: [{b: 0}], b1: [{b: 1}],
  pt3: [{pt: 0.03}],
  r0: [{r: 0}], 'r1.5': [{r: 0.015}],
  'bL0.25': [{bL: 0.25}], bL1: [{bL: 1}], noqe: [{qe: false}],
  lag1: [{lag: 1}], lag2: [{lag: 2}],
  'th0.25': [{th: 0.25}], th1: [{th: 1}],
  'dm0.5': [{dm: 0.5}], dm1: [{dm: 1}],
  reg2008: [{a: 1.5, b: 1, bL: 1}], reg2020: [{b: 1, bL: 1, lag: 0}], reg2022: [{lag: 2, a: 2}],
  'sp1.5': [{sp: 0.015}], 'sp4.5': [{sp: 0.045}], 'mm0.75': [{mm: 0.75}], D4: [{D: 4}], D10: [{D: 10}], 'k0.25': [{k: 0.25}], k1: [{k: 1}],
  'fd0.1': [{fd: 0.1}], 'fd0.27': [{fd: 0.27}], 'fd0.034': [{fd: 0.034}], 'fd0.062': [{fd: 0.062}], 'ok1.5': [{ok: 1.5}], nofs: [{fs: false}]  /* fd0.034, fd0.062: Amendment 3, Campbell, Giglio and Pathak 2011's bankruptcy-related discounts (all sales; one seller) */
};
if (env === 'hx'){ Object.assign(S, {actual: [null, {rp: 'actual'}], 'actual-sp1.5': [null, {rp: 'actual', sp: 0.015}], 'actual-sp4.5': [null, {rp: 'actual', sp: 0.045}]});
  delete S['ok1.5']; }  /* Okun's reading acts only outside History (History reads CBO's gap) */
const only = opt('only') ? opt('only').split(',') : null, names = Object.keys(S).filter(n => !only || only.indexOf(n) >= 0);
const KEEP = /^(fgt0PY|fgt0|pov|pf0_\d+|ppov_\d+|endoAnn|endoMax|medWealthReal|cost|st[A-Z]|rk[A-Z]|cb[A-Z]|fs[A-Z]|wg[A-Z]|wt(T1|T10|B50|Mean|Med)[SE]$)/;
const r6 = v => (v === 0 || !isFinite(v)) ? v : +v.toPrecision(6);
const out = {_meta: {what: 'S74 forward sweep: the frozen round-2 main pair in each setting, with the stability measures', env, seeds: N, designs, settings: {},
  command: 'node dev/tools/s74_sweep.js ' + process.argv.slice(2).join(' '), manifest: H.runManifest(), started: new Date().toISOString()}};
names.forEach(n => { out._meta.settings[n] = {cb: S[n][0], hx: env === 'hx' ? (S[n][1] || {rp: 'actual'}) : undefined}; });
designs.forEach(d => { out[d] = {}; names.forEach(n => {
  const t = Date.now(), P = Object.assign({}, ENV, {years: env === 'hx' ? H.HISTORY_ENV.years : 20, nAgents: 500});
  if (env === 'hx') P.hx = S[n][1] || {rp: 'actual'};
  const cf = H.r2FreezePair(P, d); if (S[n][0]) cf.forEach(c => { c.cb = Object.assign({}, S[n][0]); });
  const R = H.tbStudy(cf, N, P, Object.assign(H.r2MainStudy(), {stab: true}));
  out[d][n] = R.map(r => { const o = {}; Object.keys(r._s).filter(k => KEEP.test(k)).forEach(k => { o[k] = Array.from(r._s[k], r6); }); return o; });
  process.stderr.write(env + ' ' + d + ' ' + n + ' ' + ((Date.now() - t)/1000).toFixed(0) + ' s\n'); }); });
out._meta.secs = (Date.now() - t0)/1000;
fs.mkdirSync(dir, {recursive: true}); fs.writeFileSync(path.join(dir, 's74-sweep-' + env + '.json'), JSON.stringify(svS.withSettings(out)));
console.log(env + ': ' + designs.length + ' designs x ' + names.length + ' settings x ' + N + ' seeds, ' + out._meta.secs.toFixed(0) + ' s');
