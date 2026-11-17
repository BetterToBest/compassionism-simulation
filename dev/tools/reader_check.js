#!/usr/bin/env node
/* Reader-facing wording, as rendered (S80, Nov 17, 2026).
 *
 * Each published page is opened in jsdom with its own scripts and data files, in each view a reader can choose by link (?rel=1 and the
 * default), and the text a reader sees (the body's text, title, alt, aria-label and placeholder attributes, the page title and the
 * description meta tags) is scanned for the project's internal bookkeeping: step and ledger codes, "session 12", "part M", job ids,
 * "round 2", "release 1/2" and "C2.2". dev/tools/reader_codes.py does the same for the Markdown files and for each page's static text.
 * Allowed: results-folder names and file paths inside <code>, which tell a reader where to find something (dev/tools/reader_codes_allow.txt).
 * Usage: node dev/tools/reader_check.js [--list]   (exit 1 on any finding). domtest.js runs it (module.exports.run). */
'use strict';
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..');
const PAGES = [['index.html', ''], ['index.html', '?rel=1'], ['findings.html', ''], ['findings.html', '?rel=1'], ['suite.html', ''], ['suite.html', '?rel=1'],
  ['study.html', ''], ['replication.html', ''], ['earlier-engine.html', ''], ['compare.html', '']];
const PATTERNS = [
  ['step/ledger code', /(?<![\w./#?=&-])(?:N-S\d+|H-S\d+|S\d{1,3}[a-z]?(?:\.\d+)?|D\d{1,3}|I\d{1,2}|i\d{1,2})(?![\w/-]|\.\w)/g],
  ['session number', /\b[Ss]ession \d+[a-z]?\b/g],
  ['part letter', /\b[Pp]art (?![IVX]\b)[A-Z]\b/g],
  ['job id', /(?<![\w./-])(?:job )?X\d\b/g],
  ['round 2', /(?<![\w/-])[Rr]ound[ -]?[12](?![\w.])/g],
  ['release 1/2', /(?<![\w/-])[Rr]elease[ -]?[12](?![\w.])|\b[Rr]eleases? 1 and 2\b/g],
  ['C2.2', /(?<!criterion )\bC2\.2\b/g]];

function allow() {
  const f = path.join(ROOT, 'dev', 'tools', 'reader_codes_allow.txt'), s = new Set();
  if (fs.existsSync(f)) fs.readFileSync(f, 'utf8').split('\n').forEach(l => { l = l.split('#')[0].trim(); if (l) s.add(l); });
  return s;
}

/* The visible text of a document: text nodes outside script, style, code and pre, plus the attributes a reader sees or hears. */
function visible(d) {
  const out = [];
  out.push(d.title || '');
  d.querySelectorAll('meta[name="description"], meta[property="og:description"], meta[property="og:title"], meta[name="twitter:description"]').forEach(m => out.push(m.getAttribute('content') || ''));
  const walk = n => {
    if (n.nodeType === 3) { out.push(n.nodeValue); return; }
    if (n.nodeType !== 1) return;
    const t = n.tagName.toLowerCase();
    if (t === 'script' || t === 'style' || t === 'code' || t === 'pre' || t === 'noscript' && false) return;
    ['title', 'alt', 'aria-label', 'placeholder'].forEach(a => { if (n.hasAttribute(a)) out.push(n.getAttribute(a)); });
    for (const c of n.childNodes) walk(c);
  };
  if (d.body) walk(d.body);
  return out.join('\n');
}

function scanText(txt, where, ok) {
  const hits = [];
  PATTERNS.forEach(([name, rx]) => { rx.lastIndex = 0; let m;
    while ((m = rx.exec(txt))) { if (ok.has(m[0]) || ok.has(where.split('?')[0] + ':' + m[0])) continue;
      const a = Math.max(0, m.index - 60), b = Math.min(txt.length, m.index + m[0].length + 60);
      hits.push(where + '  [' + name + '] ' + m[0] + '  …' + txt.slice(a, b).replace(/\s+/g, ' ') + '…'); } });
  return hits;
}

async function render(file, query) {
  const { JSDOM, VirtualConsole, requestInterceptor } = require('jsdom');
  const local = requestInterceptor(req => {
    const u = new URL(req.url);
    if (u.hostname !== 'bettertobest.github.io') return new Response('', { status: 200 });
    const p = path.join(ROOT, decodeURIComponent(u.pathname.replace(/^\/compassionism-simulation\//, '')));
    const type = /\.js$/.test(p) ? 'application/javascript' : /\.css$/.test(p) ? 'text/css' : /\.json$/.test(p) ? 'application/json' : 'text/plain';
    return fs.existsSync(p) && fs.statSync(p).isFile() ? new Response(fs.readFileSync(p), { headers: { 'Content-Type': type } }) : new Response('', { status: 404 });
  });
  const errs = [], vc = new VirtualConsole(); vc.on('jsdomError', e => errs.push(String(e.message || e).slice(0, 160)));
  const dom = new JSDOM(fs.readFileSync(path.join(ROOT, file), 'utf8'), {
    url: 'https://bettertobest.github.io/compassionism-simulation/' + file + query, runScripts: 'dangerously', resources: { interceptors: [local] }, pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) {
      w.scrollTo = () => {}; w.matchMedia = w.matchMedia || (() => ({ matches: false, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} }));
      w.Chart = function () { return { destroy() {}, update() {}, resize() {}, data: { datasets: [] }, options: {} }; }; w.Chart.register = () => {}; w.Chart.defaults = { font: {}, plugins: { legend: { labels: {} }, tooltip: {} }, scale: { grid: {}, ticks: {} } };
      w.IntersectionObserver = w.IntersectionObserver || class { observe() {} unobserve() {} disconnect() {} };
      w.fetch = url => { const u = String(url).split('?')[0].replace(/^https:\/\/bettertobest\.github\.io\/compassionism-simulation\//, '').replace(/^\.?\//, ''), p = path.join(ROOT, u);
        return fs.existsSync(p) ? Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve(JSON.parse(fs.readFileSync(p, 'utf8'))), text: () => Promise.resolve(fs.readFileSync(p, 'utf8')) })
          : Promise.resolve({ ok: false, status: 404, json: () => Promise.reject(new Error('404 ' + u)), text: () => Promise.resolve('') }); };
    } });
  await new Promise(r => dom.window.addEventListener('load', r));
  await new Promise(r => setTimeout(r, 2500));
  const txt = visible(dom.window.document);
  dom.window.close();
  return { txt, errs };
}

async function run() {
  const ok = allow(), out = [];
  let hits = [], chars = 0;
  for (const [f, q] of PAGES) {
    if (!fs.existsSync(path.join(ROOT, f))) continue;
    const r = await render(f, q); chars += r.txt.length;
    hits = hits.concat(scanText(r.txt, f + q, ok));
  }
  out.push({ name: 'S80: no step or ledger code, session or part label, job id, "round 2", "release 1/2" or "C2.2" in the text a reader sees on any page, rendered with its data in each view',
    pass: hits.length === 0, detail: hits.length ? hits.slice(0, 6).join(' | ') + (hits.length > 6 ? ' (+' + (hits.length - 6) + ')' : '') : PAGES.length + ' views, ' + chars + ' characters of visible text', hits });
  return out;
}

module.exports = { run, render };
if (require.main === module) run().then(out => {
  out.forEach(o => { console.log((o.pass ? 'PASS ' : 'FAIL ') + o.name + '\n  ' + (process.argv.includes('--list') ? o.hits.join('\n  ') || o.detail : o.detail)); });
  process.exit(out.every(o => o.pass) ? 0 : 1);
});
