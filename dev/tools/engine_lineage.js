#!/usr/bin/env node
/* v5.3 B2 (Oct 6, 2026; dev/DECISIONS.md Session 39): the engine's lineage between releases.
 *
 * Each published run file records the SHA-256 of the engine text that made it (`_meta.manifest.engineBlockSha256`), and domtest checks that it equals the page's
 * engine, so a reader knows the published figures come from the engine on the page. During a model round the engine gains code that is off by default (each new
 * mechanism behind a switch, off = bit-identical), so its text, and its hash, change before the round's new figures are made. Rather than remake the published
 * panels after every such change (hours of runs that change no figure), each change is recorded here with its proof: the 12-seed release panels
 * (`node harness.js testbed 12 release ENV`, 20 and 40 years, three environments) made by the new engine have the same fingerprints (dev/tools/panel_hash.py:
 * every result, not the run's own record) as those of the engine that made the published panels. domtest accepts a published file whose engine differs from the
 * page's only when this file links the two by such proofs (reaches()). The round's release (B10) remakes the panels and starts the lineage afresh.
 *
 * Usage:
 *   node dev/tools/engine_lineage.js                 show the chain and whether it reaches the page's engine
 *   node dev/tools/engine_lineage.js prove "WHAT"    run the six 12-seed panels with the page's engine (about 10 minutes on four cores), check their fingerprints
 *                                                    against the base's and add a link from the last engine to this one, described by WHAT
 * File: dev/runs/engine-lineage.json */
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process'), crypto = require('crypto');
const ROOT = path.join(__dirname, '..', '..'), FILE = path.join(ROOT, 'dev', 'runs', 'engine-lineage.json');
const BEGIN = '/* ==== RELEASE ENGINE:', END = '/* ==== END RELEASE ENGINE ==== */';
const PANELS = [['r20-ref', 'ref', 0], ['r20-adv', 'adv', 0], ['r20-st', 'st', 0], ['r40-ref', 'ref', 40], ['r40-adv', 'adv', 40], ['r40-st', 'st', 40]];
function sha(x) { return crypto.createHash('sha256').update(x).digest('hex'); }
/* The page's engine block, exactly as harness.js's pageEngineBlock() cuts it (the BEGIN marker line through the END marker). */
function pageEngineSha(html) {
  html = html || fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
  const a = html.indexOf(BEGIN), b = html.indexOf(END);
  return a >= 0 && b > a ? sha(html.slice(a, b + END.length)) : null;
}
function load() { return JSON.parse(fs.readFileSync(FILE, 'utf8')); }
/* Is there a chain of proven links from engine `from` to engine `to`? (from === to needs none.) */
function reaches(from, to, L) {
  L = L || load(); if (from === to) return {ok: true, links: 0};
  let cur = from, n = 0;
  const same = k => k.equal === true && PANELS.every(([id]) => k.fingerprints && k.fingerprints[id] === L.base.fingerprints[id]);  /* the recorded fingerprints, not only the flag */
  for (const k of L.links) { if (k.from === cur && same(k)) { cur = k.to; n++; if (cur === to) return {ok: true, links: n}; } }
  return {ok: false, links: n};
}
/* The fingerprint panel_hash.py prints (the SHA-256 of the file without _meta, keys sorted, no spaces), through Python so both agree byte for byte. */
function fingerprints(dir) {
  const files = PANELS.map(p => path.join(dir, p[0] + '.json'));
  const out = cp.execFileSync('python3', [path.join(__dirname, 'panel_hash.py')].concat(files), {encoding: 'utf8'});
  const r = {}; out.trim().split('\n').forEach((line, i) => { r[PANELS[i][0]] = line.split(' ')[0]; }); return r;
}
module.exports = {reaches, pageEngineSha, load, PANELS};

if (require.main === module) {
  const L = load(), now = pageEngineSha(), last = L.links.length ? L.links[L.links.length - 1].to : L.base.engineBlockSha256;
  if (process.argv[2] !== 'prove') {
    console.log('base: ' + L.base.engineBlockSha256.slice(0, 12) + ' (' + L.base.what + ')');
    L.links.forEach(k => console.log('  -> ' + k.to.slice(0, 12) + ' ' + k.date + ' ' + (k.equal ? 'reproduces' : 'DIFFERS') + ': ' + k.change));
    const r = reaches(L.base.engineBlockSha256, now, L);
    console.log('page engine ' + now.slice(0, 12) + ': ' + (r.ok ? 'reached (' + r.links + ' link' + (r.links === 1 ? '' : 's') + ')' : 'NOT reached: run `node dev/tools/engine_lineage.js prove "what changed"`'));
    process.exit(r.ok ? 0 : 1);
  }
  const what = process.argv[3]; if (!what) { console.error('usage: engine_lineage.js prove "what changed"'); process.exit(1); }
  if (now === last) { console.log('the page engine is already the last link (' + now.slice(0, 12) + ')'); process.exit(0); }
  const dir = fs.mkdtempSync(path.join(require('os').tmpdir(), 'lineage-')), t0 = Date.now();
  console.log('running the six 12-seed release panels with engine ' + now.slice(0, 12) + ' in ' + dir + ' ...');
  let left = PANELS.length, fail = null;
  PANELS.forEach(([id, env, yrs]) => {
    const args = ['harness.js', 'testbed', '12', 'release', env, '--json=' + path.join(dir, id + '.json')].concat(yrs ? ['--years=' + yrs] : []);
    const ch = cp.spawn(process.execPath, args, {cwd: ROOT, stdio: ['ignore', 'ignore', 'pipe']}); let err = '';
    ch.stderr.on('data', d => { err += d; });
    ch.on('close', code => { if (code !== 0) fail = id + ': exit ' + code + ' ' + err.slice(0, 300); if (--left === 0) finish(); });
  });
  function finish() {
    if (fail) { console.error('FAILED ' + fail); process.exit(1); }
    PANELS.forEach(([id]) => { const m = JSON.parse(fs.readFileSync(path.join(dir, id + '.json'), 'utf8'))._meta.manifest;
      if (m.engineBlockSha256 !== now) { console.error(id + ' was made by engine ' + m.engineBlockSha256.slice(0, 12) + ', not the page\'s'); process.exit(1); } });
    const fp = fingerprints(dir), diff = PANELS.filter(([id]) => fp[id] !== L.base.fingerprints[id]).map(([id]) => id);
    L.links.push({from: last, to: now, date: new Date().toISOString().slice(0, 10), change: what, fingerprints: fp, equal: diff.length === 0, seconds: Math.round((Date.now() - t0)/1000)});
    fs.writeFileSync(FILE, JSON.stringify(L, null, 1) + '\n');
    console.log(diff.length ? 'DIFFERS from the base in ' + diff.join(', ') + ' (link recorded as not reproducing; the published panels must be remade)' : 'all six fingerprints equal the base: link ' + last.slice(0, 12) + ' -> ' + now.slice(0, 12) + ' recorded');
    process.exit(diff.length ? 1 : 0);
  }
}
