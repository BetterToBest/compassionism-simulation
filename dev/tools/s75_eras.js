#!/usr/bin/env node
/* S75 part 2 (research-update prereg/2026-11-s75-deep-history.md, Part B, and Amendment 4): the engine readings. The frozen round-2 main pair
 * (r2FreezePair: no programme, programme) under one era's settings, both designs, seeds 1..N, 500 adults, with the stability measures (study
 * option stab). Arms: P the era's path, the actual rate (central bank off); R the path and the era's fitted rule (cb with HXE[era].R); S the path
 * and S74's rule (cb at its main values); T the path and the era's tax schedule (hx.T, revenue-neutral); H the path and the era's health cost
 * growth (hx.H); A R, T and H together. Readings (not in the main tables): Tn arm T with nothing returned (hx.Tr false).
 * Usage: node dev/tools/s75_eras.js ERA [SEEDS] [--design=c22,rel] [--arms=P,R,S,T,H,A,Tn] [--out=DIR]   (ERA e1 | e2 | e3 | e4; SEEDS 100)
 * Writes DIR/s75-eras-ERA.json (default DIR dev/runs/s75-eras): per design, arm and row, every saved key's per-seed values. */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
/* S77 (prereg Amendment 5): the release's global settings, as the round-2 runner sets them (compassionism-sim-results runner/jobs/r2.js) and as the
 * corrected S74 tools do; without them the main row's switches run under the engine's older defaults, not release 2's main row. */
H.applyNR6(); H.tbSetG(H.TB_PROFILE_G);
const ARG = process.argv.slice(2).filter(a => !/^--/.test(a)), opt = k => (process.argv.filter(a => a.indexOf('--' + k + '=') === 0)[0] || '').slice(k.length + 3);
const era = ARG[0], N = +(ARG[1] || 100), designs = (opt('design') || 'c22,rel').split(','), arms = (opt('arms') || 'P,R,S,T,H,A,Tn').split(','),
  dir = opt('out') || path.join(__dirname, '..', 'runs', 's75-eras'), t0 = Date.now();
const E = H.HXE && H.HXE[era]; if (!E) { console.error('ERA must be e1, e2, e3 or e4'); process.exit(1); }
const ARM = {P: {hx: {}}, R: {hx: {}, cb: E.R}, S: {hx: {}, cb: {}}, T: {hx: {T: true}}, H: {hx: {H: true}}, A: {hx: {T: true, H: true}, cb: E.R}, Tn: {hx: {T: true, Tr: false}}};
const KEEP = /^(fgt0PY|fgt0|pov|ppov_\d+|pmedW_\d+|medWealthReal|endoAnn|cost|st[A-Z]|rk[A-Z]|cb[A-Z]|fs[A-Z]|hxT)/;
const out = {_meta: {what: 'S75 engine readings: the frozen round-2 main pair under one era\'s settings, with the stability measures', era, years: E.n, eraYears: E.y0 + '-' + (E.y0 + E.n - 1),
  seeds: N, designs, arms, command: 'node dev/tools/s75_eras.js ' + process.argv.slice(2).join(' '), manifest: H.runManifest(), started: new Date().toISOString()}};
designs.forEach(d => { out[d] = {}; arms.forEach(arm => {
  const a = ARM[arm]; if (!a) throw new Error('unknown arm ' + arm);
  const t = Date.now(), P = Object.assign({}, H.HISTORY_ENV, {years: E.n, nAgents: 500, hx: Object.assign({era}, a.hx)});
  const cf = H.r2FreezePair(P, d); if (a.cb) cf.forEach(c => { c.cb = Object.assign({}, a.cb); });
  const R = H.tbStudy(cf, N, P, Object.assign(H.r2MainStudy(), {stab: true}));
  out[d][arm] = R.map(r => { const o = {}; Object.keys(r._s).filter(k => KEEP.test(k)).forEach(k => { o[k] = Array.from(r._s[k]); }); return o; });
  process.stderr.write(era + ' ' + d + ' ' + arm + ' ' + ((Date.now() - t)/1000).toFixed(0) + ' s\n'); }); });
out._meta.secs = (Date.now() - t0)/1000;
fs.mkdirSync(dir, {recursive: true}); fs.writeFileSync(path.join(dir, 's75-eras-' + era + '.json'), JSON.stringify(out));
console.log(era + ': ' + designs.length + ' designs x ' + arms.length + ' arms x ' + N + ' seeds, ' + out._meta.secs.toFixed(0) + ' s');
