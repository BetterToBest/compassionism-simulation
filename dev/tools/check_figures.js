#!/usr/bin/env node
/* v5.2.1 (Oct 6, 2026; ledger s90, s94): every figure shown on the pages equals the release data.
 *
 * The pages draw their numbers from one data file per release (data/releases/v<version>.json, written by dev/tools/release_data.py) and print each
 * one in a <span class="num" data-src="<path into that file>" data-f="<format>">. This check:
 *  1. the manifest (data/manifest.json) and the release files agree: one current release, every listed file present with the same version, date and
 *     tag, and the current release shown in the page version (META.VERSION);
 *  2. the current release's two panels are byte-for-byte the merged 500-seed panels in dev/runs/ and the panels embedded in index.html;
 *  3. in every release file, every pointer (tables, texts, figure catalogue) leads to a number, and each catalogue figure's value is the number it points to;
 *  4. the explore files: each year's mean across the runs equals the published year-by-year path, for every environment, horizon and row;
 *  5. every numbered span on the three pages, as written (the static text that shows without JavaScript) and as rendered by site/findings.js and
 *     site/simpage.js (simulation page: every environment and horizon; explorer: every release in the manifest), equals the data under its format;
 *  6. no unmarked percentage, dollar figure or price level inside the new sections (a number typed into the page would show up here);
 *  7. every anchor the replication and simulation pages had at v5.2 still exists (dev/tools/anchors-v5.2.json);
 *  8. the cards' plain meanings in site/findings.js are the release file's;
 *  9. dev/tools/release_data.py --check: the data files, the manifest and the static blocks are what the generator writes from dev/runs/.
 * Usage: node dev/tools/check_figures.js   (exit 1 on any failure). domtest.js runs it as Phase 14 (module.exports.run). */
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.join(__dirname, '..', '..');
const rd = f => fs.readFileSync(path.join(ROOT, f), 'utf8'), rj = f => JSON.parse(rd(f));

async function run(opts) {
  opts = opts || {};
  const { JSDOM } = require('jsdom');
  const out = [], add = (name, pass, detail) => out.push({ name, pass: !!pass, detail });
  const chartsSrc = rd('site/charts.js'), findingsSrc = rd('site/findings.js'), simSrc = rd('site/simpage.js');
  const bare = new JSDOM('', { runScripts: 'outside-only' }).window; bare.eval(findingsSrc);
  const F = bare.CSF;
  const resolve = (R, p) => F.get(R, p);

  /* 1. manifest */
  const M = rj('data/manifest.json'), cur = M.releases.filter(r => r.status === 'current'), mp = [];
  const V = (rd('index.html').match(/var META = \{\s*VERSION:'([^']+)'/) || [])[1];
  if (cur.length !== 1) mp.push(cur.length + ' current releases');
  const REL = {};
  M.releases.forEach(r => { const f = path.join('data', r.file); if (!fs.existsSync(path.join(ROOT, f))) { mp.push('missing ' + f); return; }
    const R = rj(f); REL[r.version] = R; if (R.version !== r.version || R.date !== r.date || R.tag !== r.tag || R.status !== r.status) mp.push(r.version + ': file and manifest differ'); });
  const C = cur[0] && REL[cur[0].version];
  if (C && C.shownIn && C.shownIn !== V && !(V || '').startsWith(C.version)) mp.push('current release shown in v' + C.shownIn + ' but the page is v' + V);
  const order = M.releases.map(r => r.version), sorted = order.slice().sort((a, b) => { const x = a.split('.').map(Number), y = b.split('.').map(Number); for (let i = 0; i < 3; i++) { if ((x[i] || 0) !== (y[i] || 0)) return (y[i] || 0) - (x[i] || 0); } return 0; });
  if (order.join() !== sorted.join()) mp.push('manifest not newest first');
  add('v5.2.1: the list of releases (data/manifest.json) and the release files agree: one current release, every file present with its version, date and tag', mp.length === 0, mp.length ? mp.join('; ') : M.releases.map(r => 'v' + r.version + (r.status === 'current' ? ' (current)' : '')).join(', '));

  /* 2. the current panels are the 500-seed panels */
  const html = rd('index.html'), emb = {}; for (const m of html.matchAll(/<script type="application\/json" id="(rel-data(?:-40)?)">([\s\S]*?)<\/script>/g)) emb[m[1]] = JSON.parse(m[2]);
  const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
  const p20 = rj('dev/runs/release-panel.json'), p40 = rj('dev/runs/release-panel-40.json');
  const pOK = C && same(C.panels['20'], p20) && same(C.panels['40'], p40) && same(emb['rel-data'], p20) && same(emb['rel-data-40'], p40) && (!C.backing || same(C.backing, rj('dev/runs/backing-share.json')));
  add('v5.2.1: the current release file carries the merged 500-seed panels unchanged, the same as the panels embedded in the simulation page', pOK, pOK ? 'v' + C.version + ': 20 and 40 years, three environments; backing-share sweep' + (C.backing ? ' included' : ' absent') : 'DIFFERENT');

  /* 3. every pointer resolves; catalogue values */
  const pb = [];
  Object.values(REL).forEach(R => {
    const isNum = p => { const v = resolve(R, p); return typeof v === 'number' && isFinite(v); };
    (R.tables || []).forEach(t => t.rows.forEach(r => r.forEach(c => (c.p || []).concat(c.s || []).forEach(x => { if (typeof x !== 'string' && !isNum(x.src)) pb.push('v' + R.version + ' ' + t.id + ' ' + x.src); }))));
    Object.entries(R.text || {}).forEach(([k, t]) => { for (const m of t.matchAll(/\{\{([^|}]+)\|([a-z0-9]+)\}\}/g)) if (!isNum(m[1])) pb.push('v' + R.version + ' text ' + k + ' ' + m[1]); });
    (R.figures || []).forEach(f => { if (!isNum(f.src) || resolve(R, f.src) !== f.value || !['simulated', 'derived', 'sourced', 'target'].includes(f.basis) || !f.meaning || !f.unit || ![20, 40].includes(f.years)) pb.push('v' + R.version + ' figure ' + f.id); });
  });
  const nFig = Object.values(REL).reduce((s, R) => s + (R.figures || []).length, 0), nCell = Object.values(REL).reduce((s, R) => s + (R.tables || []).reduce((a, t) => a + t.rows.length, 0), 0);
  add('v5.2.1: in every release file each table cell, text and catalogue figure points to a number in the file, and each catalogue figure carries its value, unit, horizon, basis and meaning', pb.length === 0, pb.length ? pb.slice(0, 5).join('; ') + (pb.length > 5 ? ' (+' + (pb.length - 5) + ')' : '') : nFig + ' catalogue figures and ' + nCell + ' table rows in ' + Object.keys(REL).length + ' releases');

  /* 4. explore files */
  const xp = [], X = { bands: {}, lives: {} };
  if (C && C.explore) {
    Object.entries(C.explore.bands).forEach(([y, f]) => { const B = rj(path.join('data/releases', f)); X.bands[y] = B;
      ['ref', 'adv', 'st'].forEach(e => ['base', 'release', 'h1', 'mid'].forEach(row => ['f0', 'pov', 'bO', 'medW'].forEach(m => { const pub = row === 'base' ? C.panels[y].envs[e].base.path[m] : C.panels[y].envs[e].rows[row].path[m], b = B.envs[e].bands[row][m];
        if (!same(b.mean, pub)) xp.push(y + 'y ' + e + ' ' + row + ' ' + m); if (b.p10.some((v, i) => v > b.p90[i])) xp.push(y + 'y ' + e + ' ' + row + ' ' + m + ' band'); }))); });
    Object.entries(C.explore.lives).forEach(([k, f]) => { const L = rj(path.join('data/releases', f)); X.lives[k] = L; const [e, y] = k.split('-');
      ['base', 'release'].forEach(row => { const fl = L.lives[row].f; if (fl.length !== C.meta.agents || fl.some(s => s.length !== +y || !/^[0-9a-f]+$/.test(s))) xp.push(k + ' ' + row + ' shape'); }); });
  } else xp.push('no explore files listed');
  add('v5.2.1: the explore files (spread across the runs, one run\'s adults) match the release: each year\'s mean across the runs equals the published year-by-year path', xp.length === 0, xp.length ? xp.slice(0, 5).join('; ') : Object.keys(X.bands).length + ' horizons x 3 environments x 4 rows x 4 measures; ' + Object.keys(X.lives).length + ' life files of ' + (C && C.meta.agents) + ' adults');

  /* 5. the numbers on the pages */
  const spanProbs = (doc, R, tag) => { const bad = []; let n = 0;
    doc.querySelectorAll('[data-src][data-f]').forEach(s => { n++; const v = resolve(R, s.getAttribute('data-src')); let want; try { want = F.fmt(v, s.getAttribute('data-f')); } catch (e) { want = '?'; }
      if (typeof v !== 'number' || s.textContent !== want) bad.push(tag + ' ' + s.getAttribute('data-src') + ' shows "' + s.textContent + '", data ' + want); });
    return { bad, n }; };
  const withX = Object.assign({}, C, { x: X });
  // 5a. static text, as served
  const st = []; let stN = 0;
  [['index.html', withX], ['findings.html', withX], ['replication.html', withX]].forEach(([f, R]) => { const d = new JSDOM(rd(f)).window.document, r = spanProbs(d, R, f); stN += r.n; st.push(...r.bad); });
  add('v5.2.1: every number in the pages\' static text (what shows without JavaScript and to search engines) equals the release data', st.length === 0 && stN >= 40, st.length ? st.slice(0, 4).join('; ') : stN + ' numbers on the three pages');

  // a jsdom window with fetch served from the repository, so the lazily loaded files load in the test
  const serve = w => { w.fetch = url => { const u = String(url).split('?')[0].replace(/^\.?\//, ''), p = path.join(ROOT, u);
    return Promise.resolve(fs.existsSync(p) ? { ok: true, status: 200, json: () => Promise.resolve(JSON.parse(fs.readFileSync(p, 'utf8'))) } : { ok: false, status: 404, json: () => Promise.reject(new Error('404')) }); }; };
  const settle = w => new Promise(res => w.setTimeout(res, 60)).then(() => new Promise(res => setTimeout(res, 120)));

  // 5b. the simulation page, rendered, in every environment and horizon
  const sp = []; let spN = 0, scan = [];
  { const dom = new JSDOM(html, { runScripts: 'outside-only', url: 'https://bettertobest.github.io/compassionism-simulation/' }), w = dom.window;
    w.Chart = function () { this.destroy = function () {}; }; w.scrollTo = () => {}; w.HTMLCanvasElement.prototype.getContext = () => ({});
    const addEL = w.addEventListener.bind(w); w.addEventListener = (t, fn, o) => { if (t === 'load' || t === 'DOMContentLoaded') return; return addEL(t, fn, o); };
    serve(w); const inline = [...w.document.querySelectorAll('script')].filter(s => !s.src && !s.type); w.eval(inline[0].textContent); w.addEventListener = addEL;
    w.relInit(); w.eval(chartsSrc); w.eval(findingsSrc); w.eval(simSrc);
    await settle(w); await settle(w);
    for (const [e, y] of [['ref', 20], ['adv', 20], ['st', 20], ['ref', 40], ['adv', 40], ['st', 40]]) {
      w.relSet(e); w.relYears(y); await settle(w); await settle(w);
      const r = spanProbs(w.document, withX, 'index ' + e + ' ' + y + 'y'); spN += r.n; sp.push(...r.bad);
      if (!w.document.querySelector('#fx-people-body .fx-grid500') || !w.document.querySelector('#fx-time-chart svg') || !w.document.querySelector('#fx-who-dec svg')) sp.push('index ' + e + ' ' + y + 'y: a section did not render');
      scan.push(...unmarked(w.document.getElementById('explore'), 'index ' + e + ' ' + y + 'y'));
    }
    w.relSet('ref'); w.relYears(20);
  }
  add('v5.2.1: on the simulation page every number the guided sections show equals the release data, in all three environments at 20 and 40 years', sp.length === 0 && spN > 600, sp.length ? sp.slice(0, 4).join('; ') : spN + ' numbers checked in 6 views');

  // 5c. the explorer, every release
  const ep = []; let epN = 0, edoc = null;
  { const dom = new JSDOM(rd('findings.html'), { runScripts: 'outside-only', url: 'https://bettertobest.github.io/compassionism-simulation/findings.html' }), w = dom.window;
    w.scrollTo = () => {}; serve(w); w.eval(chartsSrc); w.eval(findingsSrc); const inline = [...w.document.querySelectorAll('script')].filter(s => !s.src && !s.type); w.eval(inline[0].textContent);
    await settle(w); await settle(w);
    for (const r of M.releases) { const sel = w.document.getElementById('version'); sel.value = r.version; sel.onchange(); await settle(w); await settle(w);
      for (const [e, y] of [['ref', '20'], ['st', '40']]) { if (!REL[r.version].panels[y]) continue;
        [...w.document.querySelectorAll('#controls button')].filter(b => b.dataset.value === e || b.dataset.value === y).forEach(b => b.click()); await settle(w);
        w.document.querySelectorAll('#all-tables details').forEach(d => { d.open = true; d.dispatchEvent(new w.Event('toggle')); });
        const x = spanProbs(w.document, REL[r.version], 'findings v' + r.version + ' ' + e + ' ' + y + 'y'); epN += x.n; ep.push(...x.bad);
        if (w.document.querySelectorAll('.fx-sec').length < 3) ep.push('v' + r.version + ': sections missing');
        scan.push(...unmarked(w.document.getElementById('content'), 'findings v' + r.version)); } }
    const sel = w.document.getElementById('version'); sel.value = C.version; sel.onchange(); await settle(w); await settle(w); edoc = w.document;
  }
  add('v5.2.1: on the findings explorer every number (cards, charts\' tables, guided reads, every full table) equals its release\'s data, for every release in the list', ep.length === 0 && epN > 2000, ep.length ? ep.slice(0, 4).join('; ') : epN + ' numbers checked across ' + M.releases.length + ' releases');

  /* 6. nothing typed */
  add('v5.2.1: no percentage, dollar figure or price level is typed into the new sections: each one comes from the data', scan.length === 0, scan.length ? [...new Set(scan)].slice(0, 5).join('; ') : 'simulation page in 6 views and the explorer for every release');

  /* 7. anchors */
  const A = rj('dev/tools/anchors-v5.2.json'), miss = [];
  Object.entries(A).forEach(([f, ids]) => { const d = new JSDOM(rd(f)).window.document; ids.forEach(id => { if (!d.getElementById(id)) miss.push(f + '#' + id); }); });
  const dup = []; ['index.html', 'replication.html', 'findings.html'].forEach(f => { const seen = {}; for (const m of rd(f).replace(/<script\b[^>]*>[\s\S]*?<\/script>/g, '').matchAll(/\sid="([^"]+)"/g)) { if (seen[m[1]]) dup.push(f + '#' + m[1]); seen[m[1]] = 1; } });
  add('v5.2.1: every anchor the replication and simulation pages had at v5.2 still exists (outside articles and the OSF record link to them), and no id is used twice', miss.length === 0 && dup.length === 0,
    miss.length || dup.length ? miss.concat(dup.map(x => 'duplicate ' + x)).slice(0, 6).join('; ') : Object.values(A).reduce((s, x) => s + x.length, 0) + ' anchors present');

  /* 8. meanings */
  const mm = ['bO', 'f0', 'pov'].filter(k => { const f = C.figures.find(x => x.id === 'ref.20.' + k + '.with'); return !f || f.meaning !== F.MEANINGS[k]; });
  add('v5.2.1: the cards\' plain meanings in site/findings.js are the release file\'s words', mm.length === 0, mm.length ? 'differ: ' + mm.join(', ') : 'three measures');

  /* 9. the generator */
  let g = { status: 1, stdout: '' }; try { g = { status: 0, stdout: cp.execFileSync('python3', [path.join('dev', 'tools', 'release_data.py'), '--check'], { cwd: ROOT, encoding: 'utf8' }) }; } catch (e) { g = { status: e.status || 1, stdout: String(e.stdout || e.message) }; }
  add('v5.2.1: python3 dev/tools/release_data.py --check: the release data, the manifest and the pages\' static figures are what the generator writes from dev/runs/', g.status === 0, g.stdout.trim().split('\n').pop());
  return out;
}

function unmarked(root, tag) {  /* text with a %, a $ amount or a times sign outside a numbered span, outside chart drawings and outside the page's own results text (checked by Phases 11-13) */
  const bad = []; if (!root) return bad;
  const skip = el => el.closest('[data-src], [data-rel-text], svg, script, style, #rel-out, #rel-tg-out, #rel-path-out, #rel-more, #rel-src, #rel-live, #fd-old, .fd-ctl, .fd-dl, #rel-env-note, .fx-tip, select, option');
  const walk = root.ownerDocument.createTreeWalker(root, 4); let n;
  while ((n = walk.nextNode())) { const t = n.nodeValue.replace(/95% (confidence )?interval/g, 'interval'); if (!/\d/.test(t)) continue; if (skip(n.parentElement)) continue;
    const m = t.match(/\d[\d,.]*\s?%|\$\s?\d|\d\s?×/); if (m) bad.push(tag + ': "' + t.trim().slice(0, 60) + '"'); }
  return bad;
}

module.exports = { run };
if (require.main === module) run().then(r => { let bad = 0; r.forEach(x => { console.log((x.pass ? '  PASS  ' : '  FAIL  ') + x.name + '\n           ' + x.detail); if (!x.pass) bad++; }); console.log(bad ? bad + ' failed' : 'all ' + r.length + ' passed'); process.exit(bad ? 1 : 0); })
  .catch(e => { console.error(e); process.exit(1); });
