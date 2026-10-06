#!/usr/bin/env node
/* v5.2.2 (Oct 6, 2026; audit A2, Muse F2): retired claims must not come back to a public page.
 *
 * Each entry below is a claim that was once true (or once written) and has since been retired: its pattern, the version that made it untrue, the version
 * that took it off the pages, and what is true now. The check fails if any pattern appears in what a reader of a public page can see:
 *   - HTML pages: the text of the markup (scripts, styles and comments removed; regions that are labelled history, listed in HISTORY below, skipped),
 *     and the inline scripts with their comments removed (string literals stay: the simulation page builds its sentences in them);
 *   - JavaScript files the pages load: the code with its comments removed;
 *   - Markdown (README.md): the whole text;
 *   - the release data files (data/releases/*.json): every string in them;
 *   - the walk-through script (walkthrough/tour.json): every string in it.
 * A claim can be limited to some files (`files`), for instance one that is still true of the earlier engine, whose page describes v4.22.
 * Code comments are not scanned: they record the history of the code on purpose.
 *
 * To retire a claim: add an entry (id, re, retired, removed, now), fix the pages, and run this file. domtest runs it (module.exports.run).
 * Usage: node dev/tools/check_stale_claims.js   (exit 1 on any hit; --list prints the claims) */
'use strict';
const fs = require('fs'), path = require('path');
let ROOT = path.join(__dirname, '..', '..');  /* --root=DIR checks another copy of the site (to show the check fails on the old pages) */

const CLAIMS = [
  {id: 'nine-in-ten', re: /\bnine (?:runs )?in ten\b(?! adults)/i, retired: 'v5.1', removed: 'v5.2.2',
   was: '"nine runs in ten" for the 10th to 90th percentile band', now: 'that band holds eight runs in ten (Muse audit F1); the page builds the words from the percentile pair it prints'},
  {id: 'automation-uniform', re: /automation[_ ]?risk\W{0,16}(?:∈|in|is drawn|drawn)[^.]{0,60}\buniform|automationRisk uniform distribution/i, retired: 'v4.3', removed: 'v5.2.2',
   was: 'automationRisk is drawn uniform on [0.2, 1.0]', now: 'a 63%/37% Beta(6,1)/Beta(1,6) mixture since v4.20 (47%/53% from v4.3); not yet tied to occupation (Muse audit F2)'},
  {id: 'rng-variable-draws', re: /still consumes a variable number of RNG calls/i, retired: 'v4.3', removed: 'v5.2.2',
   was: 'runYear() draws a variable number of random numbers per agent', now: 'eight draws per adult-year in a fixed order since v4.3; new processes use their own streams'},
  {id: 'headline-v44', re: /Headline large-N figures on this page are current as of v4\.4/i, retired: 'v5.0', removed: 'v5.2.2',
   was: 'the page\'s headline figures are the v4.4 large-N study', now: 'the release engine\'s 500 paired runs since v5.0; the v4.4 study is labelled history'},
  {id: 'wealth-loop-units', re: /keeps its pre-v4\.0 unit simplification/i, retired: 'v4.3', removed: 'v5.2.2',
   was: 'the wealth update keeps its pre-v4.0 wage units', now: 'WAGE_TO_USD in the wealth update since v4.3'},
  {id: 'conversion-unconstrained', re: /conversion proceeds are tracked but not production-constrained/i, retired: 'v5.0', removed: 'v5.2.2', files: ['replication.html', 'index.html', 'findings.html', 'README.md'],
   was: 'conversion is credited without a treasury or production account', now: 'the Source pays conversions, new output backs part of the payout, the price module turns the rest into prices (release engine)'},
  {id: 'ptf-cap-unresolved', re: /Initial PTF share is not a hard cap \(relabell?ed v3\.6, unresolved\)/i, retired: 'v4.6', removed: 'v5.2.2',
   was: 'nothing limits PTF membership', now: 'an opt-in cap since v4.6 (earlier engine); PTF capacity limits membership in the release engine'},
  {id: 'no-per-adult-history', re: /per-agent poverty spells tracked over time, which the engine does not keep/i, retired: 'v5.2', removed: 'v5.2.2', files: ['replication.html', 'index.html', 'findings.html', 'README.md'],
   was: 'the engine keeps no per-adult history', now: 'the release engine records each adult\'s yearly poverty status and measures spells (v5.2)'},
  {id: 'oat-only', re: /\bOAT sensitivity only\b/i, retired: 'v4.6', removed: 'v5.2.2',
   was: 'one-at-a-time sensitivity is the only sensitivity tool', now: 'the earlier engine also exports a Latin-hypercube design (v4.6); the release engine has no global analysis yet (planned for v5.4)'},
  {id: 'wealth-line-savings', re: /less than (?:\$[\d,]+|\{\{inputs\.wealthLine\|usd\}\}) of savings|\bsavings under (?:\$[\d,]+|\{\{inputs\.wealthLine)/i, retired: 'v5.0', removed: 'v5.2.2',
   was: '"too little wealth" described as savings', now: 'it counts net wealth, what someone owns minus what they owe (Muse audit nit)'}
];

/* Regions of a page that are labelled as history and quote the old engine on purpose (each says so on the page): the replication page's version history
 * (each release's own notes, as written at the time) and the notes moved from the simulation page, headed as describing the engine through v4.22. */
const HISTORY = {
  'replication.html': ['#history', '#page-assumptions']
};

const PUBLIC = ['index.html', 'earlier-engine.html', 'replication.html', 'findings.html', 'README.md', 'site/findings.js', 'site/simpage.js', 'site/charts.js', 'walkthrough/tour.json'];

/* JavaScript without its comments (strings, template literals and regular-expression literals are kept as they are). */
function stripJS(src) {
  let out = '', i = 0, n = src.length, last = '';
  while (i < n) {
    const c = src[i], d = src[i + 1];
    if (c === '/' && d === '/') { while (i < n && src[i] !== '\n') i++; continue; }
    if (c === '/' && d === '*') { const j = src.indexOf('*/', i + 2); i = j < 0 ? n : j + 2; out += ' '; continue; }
    if (c === '"' || c === "'" || c === '`') { let j = i + 1; while (j < n && src[j] !== c) { if (src[j] === '\\') j++; j++; } out += src.slice(i, j + 1); i = j + 1; last = c; continue; }
    if (c === '/' && /[(,=:[!&|?{};+\-*%<>~^]|^$/.test(last)) {  /* a regular-expression literal */
      let j = i + 1, cls = false; while (j < n && (cls || src[j] !== '/') && src[j] !== '\n') { if (src[j] === '\\') j++; else if (src[j] === '[') cls = true; else if (src[j] === ']') cls = false; j++; }
      out += src.slice(i, j + 1); i = j + 1; last = '/'; continue; }
    out += c; if (!/\s/.test(c)) last = c; i++;
  }
  return out;
}
function strings(o, acc) { if (typeof o === 'string') acc.push(o); else if (o && typeof o === 'object') Object.values(o).forEach(v => strings(v, acc)); return acc; }

function textsOf(rel, JSDOM) {
  const p = path.join(ROOT, rel); if (!fs.existsSync(p)) return [];
  const src = fs.readFileSync(p, 'utf8');
  if (rel.endsWith('.md')) return [['text', src]];
  if (rel.endsWith('.json')) return [['strings', strings(JSON.parse(src), []).join('\n')]];
  if (rel.endsWith('.js')) return [['code', stripJS(src)]];
  const doc = new JSDOM(src).window.document, scripts = [];
  doc.querySelectorAll('script').forEach(s => { if (!s.src && (!s.type || /javascript/.test(s.type))) scripts.push(stripJS(s.textContent)); s.remove(); });
  doc.querySelectorAll('style, noscript').forEach(s => s.remove());
  (HISTORY[rel] || []).forEach(sel => doc.querySelectorAll(sel).forEach(el => el.remove()));
  return [['text', doc.body ? doc.body.textContent : ''], ['script', scripts.join('\n')]];
}

function run() {
  const { JSDOM } = require('jsdom');
  const files = PUBLIC.concat(fs.readdirSync(path.join(ROOT, 'data', 'releases')).filter(f => f.endsWith('.json')).map(f => 'data/releases/' + f));
  const hits = [];
  files.forEach(rel => textsOf(rel, JSDOM).forEach(([kind, t]) => CLAIMS.forEach(c => {
    if (c.files && !c.files.includes(rel)) return;
    const m = t.match(c.re); if (m) { const k = t.indexOf(m[0]); hits.push(rel + ' (' + kind + '): ' + c.id + ' [retired ' + c.retired + '] "…' + t.slice(Math.max(0, k - 40), k + m[0].length + 40).replace(/\s+/g, ' ') + '…"'); }
  })));
  return {pass: hits.length === 0, hits, claims: CLAIMS.length, files: files.length};
}

module.exports = {run, CLAIMS, stripJS};
if (require.main === module) {
  const ra = process.argv.find(a => a.startsWith('--root=')); if (ra) ROOT = path.resolve(ra.slice(7));
  if (process.argv.includes('--list')) { CLAIMS.forEach(c => console.log(c.id + ' (retired ' + c.retired + ', off the pages ' + c.removed + '): was ' + c.was + '; now ' + c.now)); process.exit(0); }
  const r = run();
  console.log(r.pass ? 'no retired claim on a public page (' + r.claims + ' claims, ' + r.files + ' files)' : 'RETIRED CLAIMS FOUND:\n  ' + r.hits.join('\n  '));
  process.exit(r.pass ? 0 : 1);
}
