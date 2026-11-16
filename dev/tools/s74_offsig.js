#!/usr/bin/env node
/* S74: an off-identity signature of the round-2 main pair (both designs), for comparing two engine copies (guardrail 1 beside guard_test.js, which
 * runs the v5.4 rows only and so never reaches the asset classes). Every testbed output of every seed, as raw numbers, hashed per environment.
 * Usage: node dev/tools/s74_offsig.js [HARNESS] [SEEDS]   (HARNESS defaults to this repository's harness.js; SEEDS 2) */
'use strict';
const path = require('path'), crypto = require('crypto');
const H = require(path.resolve(process.argv[2] || path.join(__dirname, '..', '..', 'harness.js'))), N = +(process.argv[3] || 2);
const E = {ref:H.FULL_INTEGRATION, adv:H.ADVERSE_REFERENCE, st:H.STRESS_TEST};
Object.keys(E).forEach(env => { ['c22', 'rel'].forEach(d => {
  const P = Object.assign({}, E[env], {years:20, nAgents:500}), R = H.tbStudy(H.r2MainPair(P, d), N, P, H.r2MainStudy());
  const sig = R.map(r => Object.keys(r._s).sort().map(k => k + ':' + Array.prototype.join.call(r._s[k], ',')).join(';')).join('\n');
  console.log(env, d, crypto.createHash('sha256').update(sig).digest('hex').slice(0, 16), 'fgt0PY', R.map(r => r.fgt0PY).join(' '), 'pov', R.map(r => r.pov).join(' ')); }); });
