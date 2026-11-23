#!/usr/bin/env node
/* S93 part 4 (Nov 23, 2026): items F4, F5, F6 and F8 of the release's pre-publish checklist (research-update prereg/2026-11-s90-private-price-at-sale.md,
 * Amendment 2 section F, with Amendment 3). Every check reads the rendered pages (jsdom) or the data files they load; nothing is typed in.
 *   F4  qualifiers: every headline card carries the full-backing statement and the opt-in design's figure; the wealth card carries the erosion share;
 *       every v5.9 subsection that prints a figure carries an interval note (the words "interval" or "95%"); the page prints no NaN, undefined or
 *       load error. check_round2.js and the reader-codes check are run separately (both are CI checks).
 *   F5  the visual suite (suite.html, release 2): in every environment, horizon and group view, the page renders with no error, no NaN or undefined,
 *       every chart draws, and every series the BLEI charts and the Five Measures table ask for is present in data/releases/r2/ for every row
 *       (all values finite). With --pub=DIR (a copy of the published page and data), the count of "no one in this group" placeholders is compared.
 *   F6  the charts in data/studies/r2-charts/ equal, byte for byte, what dev/tools/s64_charts.py writes from the release copy of the tables
 *       (dev/runs/s93-round2); the figure captions (alt text and table captions) of the v5.9 section print no number and name no engine.
 *   F8  every data file a release section reads, with its engine (meta.engine; a full hash is cut to 7); a section whose files carry two engines
 *       fails, and so does one whose visible text does not name its engine commit and version.
 * Usage: node dev/tools/s93_checklist.js [--pub=DIR] [--out=FILE.md]   (exit 1 if any check fails) */
'use strict';
const { JSDOM } = require('jsdom'), fs = require('fs'), path = require('path'), os = require('os'), cp = require('child_process');
const ROOT = path.join(__dirname, '..', '..'), arg = (k, d) => { const a = process.argv.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : d; };
const ENGINE = '50bc51d', VERSION = 'v5.9.23', out = arg('out', ''), PUB = arg('pub', '');
const L = [], fails = [];
const say = (ok, item, msg) => { L.push('- ' + (ok ? 'PASS' : 'FAIL') + ' ' + item + ': ' + msg); if (!ok) fails.push(item + ': ' + msg); };
const later = ms => new Promise(r => setTimeout(r, ms));

function open(root, page, query) {
  const rd = f => fs.readFileSync(path.join(root, f), 'utf8'), loaded = [];
  const w = new JSDOM(rd(page), { runScripts: 'outside-only', url: 'https://bettertobest.github.io/compassionism-simulation/' + page + (query || '') }).window, errs = [];
  w.scrollTo = () => {}; w.addEventListener('error', e => errs.push(String(e.message)));
  w.fetch = url => { const u = String(url).split('?')[0].replace(/^\.?\//, ''), p = path.join(root, u); loaded.push(u);
    return Promise.resolve(fs.existsSync(p) ? { ok: true, status: 200, json: () => Promise.resolve(JSON.parse(fs.readFileSync(p, 'utf8'))) } : { ok: false, status: 404, json: () => Promise.reject(new Error('404')) }); };
  w.eval(rd('site/charts.js')); w.eval(rd('site/findings.js'));
  if (page === 'findings.html') ['site/round2.js', 'site/cb.js'].forEach(f => { if (fs.existsSync(path.join(root, f))) w.eval(rd(f)); });
  try { w.eval([...w.document.querySelectorAll('script')].filter(x => !x.src && !x.type)[0].textContent); } catch (e) { errs.push(String(e.message)); }
  return { w, errs, loaded };
}
const engOf = f => { const d = JSON.parse(fs.readFileSync(path.join(ROOT, f), 'utf8')), m = d.meta || d._meta || d;
  const e = m.engine || (d._meta && d._meta.engine) || d.engine; return e ? String(e).slice(0, 7) : null; };
const bad = t => /NaN|undefined|Could not load/.test(t);

(async () => {
  /* ---- the findings page ---- */
  const F = open(ROOT, 'findings.html'); await later(2000);
  const d = F.w.document, body = d.getElementById('round2-body'), cbs = d.getElementById('cb');
  say(!F.errs.length && !bad(body.textContent) && !bad(cbs.textContent), 'F4', 'the v5.9 and central-bank sections render with no error, NaN, undefined or load error' + (F.errs.length ? ' (' + F.errs.slice(0, 2).join('; ') + ')' : ''));
  const cards = [...body.querySelectorAll('.fx-card')];
  say(cards.length === 4 && cards.every(c => /At full backing/.test(c.textContent) && /Opt-in design/.test(c.textContent)), 'F4', cards.length + ' headline cards, each with the full-backing statement and the opt-in design\'s figure');
  const wc = cards.filter(c => /Median real wealth/.test(c.textContent));
  say(wc.length === 1 && /erosion of opening balances/.test(wc[0].textContent) && wc[0].querySelector('.snum[data-src*="erosion share"]'), 'F4', 'the wealth card prints the erosion share from its file');
  /* subsections: each h3 with what follows it up to the next h3 */
  const subs = []; let cur = null;
  [...body.children].forEach(n => { if (n.matches('h3.fx-h3')) { cur = {h: n.textContent.trim(), text: '', nums: 0}; subs.push(cur); } else if (cur) { cur.text += ' ' + n.textContent; cur.nums += n.querySelectorAll('.snum').length; } });
  const withInt = S => S.filter(s => s.nums > 0 && /interval|95%/.test(s.text)).map(s => s.h), mine = withInt(subs);
  const noInt = subs.filter(s => s.nums > 0 && !mine.includes(s.h)).map(s => s.h);
  if (PUB) { const Pf = open(PUB, 'findings.html'); await later(2000); const Ps = []; let pc = null;
    [...Pf.w.document.getElementById('round2-body').children].forEach(n => { if (n.matches('h3.fx-h3')) { pc = {h: n.textContent.trim(), text: '', nums: 0}; Ps.push(pc); } else if (pc) { pc.text += ' ' + n.textContent; pc.nums += n.querySelectorAll('.snum').length; } });
    const lost = withInt(Ps).filter(h => !mine.includes(h));
    say(!lost.length, 'F4', mine.length + ' of ' + subs.filter(s => s.nums > 0).length + ' subsections that print figures carry an interval note (the published page: ' + withInt(Ps).length + '); none lost' + (lost.length ? '; lost: ' + lost.join(' | ') : '')); Pf.w.close(); }
  else say(mine.length > 0, 'F4', mine.length + ' of ' + subs.filter(s => s.nums > 0).length + ' subsections that print figures carry an interval note (run with --pub to compare with the published page)');
  if (noInt.length) L.push('  - for information, the subsections that print figures with no interval note of their own: ' + noInt.join(' | '));

  /* ---- F8: which files each release section reads, and its engine ---- */
  const r2src = fs.readFileSync(path.join(ROOT, 'site/round2.js'), 'utf8'), files = JSON.parse(/var FILES = (\[[^\]]+\])/.exec(r2src)[1].replace(/'/g, '"')).map(f => 'data/studies/' + f + '.json');
  const cbsrc = fs.readFileSync(path.join(ROOT, 'site/cb.js'), 'utf8'), cbFiles = [...new Set((cbsrc.match(/data\/studies\/[a-z0-9-]+\.json/g) || []))];
  const loadedStudies = [...new Set(F.loaded.filter(u => /^data\/studies\//.test(u)))];
  const missed = files.concat(cbFiles).filter(f => !loadedStudies.includes(f));
  say(!missed.length, 'F8', 'every data file the v5.9 and central-bank sections name was loaded by the rendered page' + (missed.length ? '; not loaded: ' + missed.join(', ') : ''));
  const SU = open(ROOT, 'suite.html', '?rel=2&env=ref&years=20'); await later(800);
  const suFiles = [...new Set(SU.loaded.filter(u => /^data\/releases\/r2\//.test(u)))];
  const sections = [['the v5.9 section (findings page)', files, body.textContent], ['the central-bank section (findings page)', cbFiles, cbs.textContent],
    ['the visual suite, release 2 (suite page)', suFiles, SU.w.document.body.textContent]];
  L.push('', '| section | data file | engine |', '|---|---|---|');
  sections.forEach(([n, fl]) => fl.forEach(f => L.push('| ' + n + ' | `' + f + '` | ' + (engOf(f) || 'none recorded') + ' |')));
  L.push('');
  sections.forEach(([n, fl, text]) => { const E = [...new Set(fl.map(engOf))];
    say(E.length === 1 && E[0] === ENGINE, 'F8', n + ': ' + fl.length + ' files, engine' + (E.length > 1 ? 's ' : ' ') + E.join(', '));
    say(text.includes(ENGINE) && text.includes(VERSION.slice(1)), 'F8', n + ': the visible text names the engine ' + ENGINE + ' and the version ' + VERSION); });

  /* ---- F5: the visual suite, release 2, every view ---- */
  const R2 = {}; fs.readdirSync(path.join(ROOT, 'data/releases/r2')).filter(f => /^suite-\d+\.json$/.test(f)).forEach(f => { R2[/\d+/.exec(f)[0]] = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/releases/r2', f), 'utf8')); });
  const suiteSrc = fs.readFileSync(path.join(ROOT, 'suite.html'), 'utf8');
  const asked = new Set(); (suiteSrc.match(/series\([a-z']+, '([a-z0-9_]+)'/g) || []).forEach(s => asked.add(/'([a-z0-9_]+)'$/.exec(s)[1]));
  (suiteSrc.match(/sp\([a-z']+, '([a-z0-9_]+)'/g) || []).forEach(s => asked.add(/'([a-z0-9_]+)'$/.exec(s)[1]));
  asked.delete('tier'); ['all', 'part', 'non'].forEach(g => { for (let i = 0; i < 6; i++) asked.add('tier' + i + '_' + g); });
  const gaps = [];
  Object.keys(R2).forEach(y => Object.keys(R2[y].envs).forEach(e => Object.keys(R2[y].envs[e]).forEach(r => asked.forEach(k => {
    const s = R2[y].envs[e][r][k];
    if (!s) { if (!(r === 'base' && /_part$/.test(k))) gaps.push(y + ' ' + e + ' ' + r + ' ' + k + ' absent'); return; }
    Object.keys(s).forEach(st => { if (Array.isArray(s[st]) && s[st].some(v => v !== null && !Number.isFinite(v))) gaps.push(y + ' ' + e + ' ' + r + ' ' + k + '.' + st + ' not finite'); }); }))));
  say(!gaps.length, 'F5', [...asked].length + ' series the suite draws (' + [...asked].sort().join(', ') + '), present and finite for every row, environment and horizon in data/releases/r2/' + (gaps.length ? '; gaps: ' + gaps.slice(0, 8).join('; ') : ''));
  /* the Five Measures table's series (job X3, data/releases/r2/study-<years>.json); keys the page builds by a prefix ('eppm_', 'up_', 'paid_', 'recv_') are checked for the groups present */
  const askedS = new Set(), sgaps = []; (suiteSrc.match(/sy\([a-z']+, '([a-z0-9_]+)'/g) || []).forEach(x => askedS.add(/'([a-z0-9_]+)'$/.exec(x)[1]));
  ['20', '40'].forEach(y => { const f = path.join(ROOT, 'data/releases/r2/study-' + y + '.json'); if (!fs.existsSync(f)) { sgaps.push('study-' + y + '.json absent'); return; }
    const St = JSON.parse(fs.readFileSync(f, 'utf8')); Object.keys(St.envs).forEach(e => Object.keys(St.envs[e].series).forEach(r => askedS.forEach(k => {
      const ks = /_$/.test(k) ? Object.keys(St.envs[e].series[r]).filter(x => x.startsWith(k)) : [k];
      if (!ks.length || ks.some(x => !St.envs[e].series[r][x])) { if (r !== 'base') sgaps.push(y + ' ' + e + ' ' + r + ' ' + k + ' absent'); return; }
      ks.forEach(x => Object.keys(St.envs[e].series[r][x]).forEach(st => { const a = St.envs[e].series[r][x][st]; if (Array.isArray(a) && a.some(v => v !== null && !Number.isFinite(v))) sgaps.push(y + ' ' + e + ' ' + r + ' ' + x + '.' + st + ' not finite'); })); }))); });
  say(!sgaps.length, 'F5', askedS.size + ' Five Measures series (' + [...askedS].sort().join(', ') + '), present and finite in study-20.json and study-40.json for every programme row and environment' + (sgaps.length ? '; gaps: ' + sgaps.slice(0, 8).join('; ') : ''));
  const views = []; ['ref', 'adv', 'st'].forEach(e => ['20', '40'].forEach(y => ['all', 'part', 'non'].forEach(g => views.push('?rel=2&env=' + e + '&years=' + y + '&grp=' + g))));
  const na = async root => { const o = []; for (const q of views) { const v = open(root, 'suite.html', q); await later(500); const t = v.w.document.getElementById('suite') || v.w.document.body;
    o.push({q, errs: v.errs.length, bad: bad(t.textContent), na: v.w.document.querySelectorAll('.su-na').length, svgs: v.w.document.querySelectorAll('.su-sec svg.fx-svg').length}); v.w.close(); } return o; };
  const V = await na(ROOT);
  say(V.every(v => !v.errs && !v.bad && v.svgs > 0), 'F5', views.length + ' suite views (three environments, two horizons, three groups): no error, no NaN or undefined, charts ' + [...new Set(V.map(v => v.svgs))].join('/') + ' per view');
  if (PUB) { const P = await na(PUB), diff = V.filter((v, i) => v.na !== P[i].na || v.svgs !== P[i].svgs);
    say(!diff.length, 'F5', 'against the published page and data: the same charts and the same "no one in this group" placeholders in every view' + (diff.length ? '; differ: ' + diff.map(v => v.q).join(', ') : '')); }

  /* ---- F6: the charts and captions ---- */
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 's93chk-'));
  fs.cpSync(path.join(ROOT, 'dev/runs/s93-round2'), tmp, {recursive: true, filter: s => !/[\\/]charts([\\/]|$)/.test(path.relative(ROOT, s).replace(/^dev[\\/]runs[\\/]s93-round2/, ''))});
  cp.execFileSync('python3', [path.join(ROOT, 'dev/tools/s64_charts.py'), tmp], {stdio: 'ignore'});
  const pub = fs.readdirSync(path.join(ROOT, 'data/studies/r2-charts')).filter(f => /\.svg$/.test(f));
  const neq = pub.filter(f => !fs.existsSync(path.join(tmp, 'charts', f)) || fs.readFileSync(path.join(tmp, 'charts', f), 'utf8') !== fs.readFileSync(path.join(ROOT, 'data/studies/r2-charts', f), 'utf8'));
  say(pub.length === 24 && !neq.length, 'F6', pub.length + ' charts in data/studies/r2-charts/ equal what s64_charts.py writes from the release tables' + (neq.length ? '; differ: ' + neq.join(', ') : ''));
  fs.rmSync(tmp, {recursive: true, force: true});
  const caps = [...body.querySelectorAll('img')].map(i => i.getAttribute('alt')).concat([...body.querySelectorAll('caption')].map(c => c.textContent));
  const capBad = caps.filter(c => /\b[0-9a-f]{7}\b/.test(c) && /[a-f]/.test((/\b[0-9a-f]{7}\b/.exec(c) || [''])[0]) || /late price|lagged price/i.test(c));
  const capNum = [...body.querySelectorAll('img')].map(i => i.getAttribute('alt')).filter(c => /\d+(\.\d+)?%|\$\d|[+−-]\d+\.\d/.test(c));
  say(!capBad.length && !capNum.length, 'F6', caps.length + ' figure and table captions: none names an engine or the late price, and no chart caption prints a figure' + (capBad.concat(capNum).length ? '; ' + capBad.concat(capNum).slice(0, 3).join(' | ') : ''));

  const head = ['# The release checklist, items F4, F5, F6 and F8', '', 'Written by `node dev/tools/s93_checklist.js' + (PUB ? ' --pub=DIR' : '') + '` (engine ' + ENGINE + ', ' + VERSION + '). ' + (fails.length ? fails.length + ' check(s) fail.' : 'Every check passes.'), ''];
  const txt = head.concat(L).join('\n') + '\n';
  if (out) fs.writeFileSync(out, txt); console.log(txt);
  process.exit(fails.length ? 1 : 0);
})();
