#!/usr/bin/env node
/* v5.4 item 6 (Oct 7, 2026; dev/reports/v5-21-v54-design.md, 1.7): A TEST OF THE 55% FLOOR. The BLEI paper (section 7, Table 8): "below 55% participation
 * density, cooperative synergies do not activate"; the synergy theta scales from 0 at the floor to 0.25 at 90%. The release reads the density as the share of
 * adults who are PTF members (THETA_GATE 'density', the release profile NR6), and PTF membership is capped by the preset's ptfShare (0.18 in Reference), so
 * theta is zero in every release run. This test raises the cap from 0.2 to 0.9 under floors of 0.40, 0.55 and 0.70 and reports the programme's paired effect
 * and the mean member share at each point, to show whether results jump at the floor (a cliff) or move smoothly, and what the floor means for the design.
 * Configuration: the v5.3 main row with the v5.4 parts (job loss, the PTH balance sheet, PTF by sector), SEEDS paired seeds.
 * Usage: node dev/tools/floor_test.js ref|adv|st [SEEDS]   Output: dev/runs/v54/floor-ENV.json */
'use strict';
const fs = require('fs'), path = require('path');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const C = H.CFG, ROOT = path.join(__dirname, '..', '..');
const env = process.argv[2] || 'ref', S = +(process.argv[3] || 20), NAME = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}[env];
const V54 = {empl: {}, pthb: {}, ptfs: {}}, K = ['fgt0PY', 'pov', 'bOAPy', 'cost', 'endoAnn', 'pfMem'];
const FLOORS = [0.40, 0.55, 0.70], CAPS = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9], t0 = Date.now(), th0 = C.SZH_THETA_THRESHOLD;
const out = {_meta: {what: 'v5.4 item 6: the programme\'s paired effect as the PTF membership cap rises, under three synergy floors', env, seeds: S, floors: FLOORS, caps: CAPS,
  manifest: H.runManifest(), command: 'node dev/tools/floor_test.js ' + env + ' ' + S}, rows: []};
try {
  FLOORS.forEach(fl => { C.SZH_THETA_THRESHOLD = fl;
    CAPS.forEach(cap => { const P = Object.assign({}, H[NAME], {ptfShare: cap}), PR = H.tbPresets(P), M = H.relMainCfgs(PR), wf0 = C.WEALTH_FLOOR; C.WEALTH_FLOOR = -10000;
      const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G);
      try { const R = H.tbStudy([Object.assign(M[0], {sc: H.SPEND_SOURCED, v54: V54}), Object.assign(M[1], {v54: V54})], S, P, Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY));
        const row = {floor: fl, cap};
        K.forEach(k => { const f = k === 'endoAnn' ? 100 : 1, q = H.tbDiff(R[1], R[0], k); row[k] = k === 'pfMem' ? +R[1][k].toFixed(2) : [+(q.m*f).toFixed(3), +(q.lo*f).toFixed(3), +(q.hi*f).toFixed(3)]; });
        out.rows.push(row); process.stderr.write('floor ' + fl + ' cap ' + cap + ' members ' + row.pfMem + '%\n'); }
      finally { H.resetNR6(svN); H.tbSetG(svG); C.WEALTH_FLOOR = wf0; } }); });
} finally { C.SZH_THETA_THRESHOLD = th0; }
out._meta.seconds = Math.round((Date.now() - t0)/1000);
const dir = path.join(ROOT, 'dev', 'runs', 'v54'); fs.mkdirSync(dir, {recursive: true});
const file = path.join(dir, 'floor-' + env + '.json'); fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
console.log('floor test ' + env + ' (' + out._meta.seconds + ' s) -> ' + path.relative(ROOT, file));
out.rows.forEach(r => console.log('floor ' + r.floor + ' cap ' + r.cap + ' members ' + r.pfMem + '%: ' + ['fgt0PY', 'pov', 'bOAPy', 'cost'].map(k => k + ' ' + r[k][0]).join(', ')));
