#!/usr/bin/env node
/* S77 (S75 preregistration Amendment 5): the check before S75's corrected part 2 is read. With the same start as dev/tools/s75_eras.js (the release's
 * global settings), the frozen round-2 main pair in Reference at 20 years, both designs, seeds 1..N (2), must equal release 2's published rows
 * (compassionism-sim-results r2-m-ref-20-104691f) per seed on basket poverty, wealth poverty and median real wealth. Exit 1 on any difference.
 * Usage: node dev/tools/s77_check_start.js R2_DIR [N] */
'use strict';
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
H.applyNR6(); H.tbSetG(H.TB_PROFILE_G);  /* the same two lines as s75_eras.js */
const dir = process.argv[2], N = +(process.argv[3] || 2);
const R = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(dir, 'r2-m-ref-20-104691f', 'shard-0000.json.gz'))).toString('utf8')).rows;
let n = 0; const bad = [];
['c22', 'rel'].forEach(d => {
  const P = Object.assign({}, H.FULL_INTEGRATION, {years: 20, nAgents: 500});
  const out = H.tbStudy(H.r2FreezePair(P, d), N, P, H.r2MainStudy());
  [[0, 'none'], [1, d]].forEach(([i, row]) => ['fgt0PY', 'pov', 'wtMedE'].forEach(k => {
    const a = Array.from(out[i]._s[k]), b = R['ref.' + row][k];
    a.forEach((x, s) => { n++; if (Math.abs(x - b[s]) > 1e-9 * Math.max(1, Math.abs(b[s]))) bad.push(d + ' ' + row + ' ' + k + ' seed ' + (s + 1) + ': ' + x + ' against ' + b[s]); });
  }));
});
if (bad.length) { console.log('DIFFERENCES:\n  ' + bad.join('\n  ')); process.exit(1); }
console.log('check passed: with s75_eras.js\'s start, the main pair equals release 2 in Reference per seed (' + n + ' values, seeds 1-' + N + ', both designs, both runs)');
