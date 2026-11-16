#!/usr/bin/env node
/* S74 part 3 (prereg Amendment 2): the reporting rerun must reproduce every figure the pilot saved. Compares, for each environment, design, arm, row,
 * key and seed, the pilot's file with the rerun's; prints the count of values compared and every difference (exit 1 if any).
 * Usage: node dev/tools/s74_repro.js PILOT_DIR RERUN_DIR */
'use strict';
const fs = require('fs'), path = require('path'), [A, B] = process.argv.slice(2);
let n = 0, bad = [], keysNew = new Set();
['hx', 'adv', 'st', 'ref'].forEach(env => { const fa = path.join(A, 's74-pilot-' + env + '.json'), fb = path.join(B, 's74-pilot-' + env + '.json');
  if (!fs.existsSync(fa) || !fs.existsSync(fb)){ bad.push(env + ': file missing'); return; }
  const P = JSON.parse(fs.readFileSync(fa, 'utf8')), Q = JSON.parse(fs.readFileSync(fb, 'utf8'));
  P._meta.designs.forEach(d => P._meta.arms.forEach(arm => P[d][arm].forEach((row, i) => { const q = Q[d] && Q[d][arm] && Q[d][arm][i];
    if (!q){ bad.push(env + ' ' + d + ' ' + arm + ' row ' + i + ' missing'); return; }
    Object.keys(q).forEach(k => { if (!(k in row)) keysNew.add(k); });
    Object.keys(row).forEach(k => { if (!q[k]){ bad.push(env + ' ' + d + ' ' + arm + ' ' + i + ' ' + k + ' missing'); return; }
      row[k].forEach((v, s) => { n++; if (v !== q[k][s]) bad.push(env + ' ' + d + ' ' + arm + ' ' + i + ' ' + k + ' seed ' + (s + 1) + ': ' + v + ' vs ' + q[k][s]); }); }); }))); });
console.log('compared ' + n + ' values; ' + bad.length + ' differ; ' + keysNew.size + ' new keys in the rerun');
bad.slice(0, 20).forEach(x => console.log('  ' + x)); process.exit(bad.length ? 1 : 0);
