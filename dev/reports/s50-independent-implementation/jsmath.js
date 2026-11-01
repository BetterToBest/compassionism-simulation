// S50 phase 2: Node's own Math functions, served to s50_release.py --js-math.
// Python's math module and Node's Math can differ in the last binary digit of log, exp, pow, cos and
// tan (they use different C libraries). This server answers one call per line, "op x [y]", with the
// result printed so that Python reads back the exact same double. It runs no part of the engine.
'use strict';
const rl = require('readline').createInterface({input: process.stdin, terminal: false});
const F = {l: Math.log, e: Math.exp, c: Math.cos, t: Math.tan};
rl.on('line', function(line){
  const s = line.split(' ');
  let r;
  if (s[0] === 'p') r = Math.pow(Number(s[1]), Number(s[2]));
  else r = F[s[0]](Number(s[1]));
  process.stdout.write(String(r) + '\n');
});
