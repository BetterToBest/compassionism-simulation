#!/usr/bin/env node
/* S77 (S75 preregistration Amendment 5): the check before S75's corrected part 2 is read. With the same start as dev/tools/s75_eras.js (the release's
 * global settings), the frozen round-2 main pair in Reference at 20 years, both designs, seeds 1..N (2), must equal release 2's published rows
 * (compassionism-sim-results r2-m-ref-20-104691f) per seed on basket poverty, wealth poverty and median real wealth. Exit 1 on any difference.
 * Usage: node dev/tools/s77_check_start.js R2_DIR [N] [--engine=E7]
 * S93 part 3 (Nov 23, 2026): --engine=E7 names the part M folder's engine (r2-m-ref-20-E7; default 104691f), for the check against the release rerun. */
'use strict';
const fs = require('fs'), path = require('path'), zlib = require('zlib');
const H = require(path.join(__dirname, '..', '..', 'harness.js'));
const svS = H.startRelease();  /* the same two lines as s75_eras.js */
const pa = process.argv.slice(2).filter(x => !x.startsWith('--')), E7 = (process.argv.find(x => x.startsWith('--engine=')) || '--engine=104691f').slice(9);
const dir = pa[0], N = +(pa[1] || 2);
const R = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(dir, 'r2-m-ref-20-' + E7, 'shard-0000.json.gz'))).toString('utf8')).rows;
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
console.log('check passed: with s75_eras.js\'s start, the main pair equals r2-m-ref-20-' + E7 + ' in Reference per seed (' + n + ' values, seeds 1-' + N + ', both designs, both runs)');
