/* S93 part 4 (Nov 23, 2026): item F1 of the release checklist (research-update prereg/2026-11-s90-private-price-at-sale.md, Amendment 2 F1 with
 * Amendment 3), the page part: every figure the findings page prints from a release data file, published against release.
 *
 *   node dev/tools/s93_page_check.js PUBLISHED_ROOT OUT.md [OUT.json]
 *
 * PUBLISHED_ROOT is a tree holding the published page and data (git archive origin/main findings.html site data | tar -x -C DIR); the release is this
 * checkout. The tool renders the v5.9 section of findings.html (site/round2.js, which has no switches) and the central-bank section (site/cb.js, every
 * design and environment its switches offer) from each tree, exactly as check_round2.js renders the page, and reads every printed number span (class
 * snum, with its file, row and column). The two renders use the same scripts, so the spans pair one to one; the tool stops if they do not, or if a
 * row's labels differ between the two files (row i must mean the same thing in both). It extends dev/tools/s90_page_check.py (the main rows only,
 * against the at-sale folders) to every release data file the page reads.
 *
 * For each file it counts: figures printed; figures whose printed text changes (the last printed digit or more); figures whose sign changes; and, from
 * the files themselves, rows whose release estimate falls outside the published printed range (the 95% interval the page prints beside it, and for
 * the specification curves the range across readings), and rows whose printed category changes (robust or fragile, improves or worsens, material,
 * the break-even word, the gap rule). Every changed figure is listed with its section heading and its row's labels. A third part lists every number
 * typed in the section's own words (outside a number span), for the statements to be read against the release figures by hand. */
const { JSDOM } = require('jsdom'), fs = require('fs'), path = require('path');
const REL = path.join(__dirname, '..', '..');

async function render(ROOT) {
  const rd = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
  const w = new JSDOM(rd('findings.html'), { runScripts: 'outside-only', url: 'https://bettertobest.github.io/compassionism-simulation/findings.html' }).window, errs = [];
  w.scrollTo = () => {}; w.addEventListener('error', e => errs.push(String(e.message)));
  w.fetch = url => { const p = path.join(ROOT, String(url).split('?')[0].replace(/^\.?\//, ''));
    return Promise.resolve(fs.existsSync(p) ? { ok: true, status: 200, json: () => Promise.resolve(JSON.parse(fs.readFileSync(p, 'utf8'))) } : { ok: false, status: 404, json: () => Promise.reject(new Error('404')) }); };
  for (const s of ['site/charts.js', 'site/findings.js', 'site/round2.js', 'site/cb.js']) w.eval(rd(s));
  try { w.eval([...w.document.querySelectorAll('script')].filter(x => !x.src && !x.type)[0].textContent); } catch (e) { errs.push(String(e.message)); }
  await new Promise(r => setTimeout(r, 2500));
  if (errs.length) throw new Error(ROOT + ': ' + errs.slice(0, 3).join('; '));
  const spans = [], typed = [];
  const read = (host, view) => {
    let sec = '';
    host.querySelectorAll('h2,h3,h4,.snum').forEach(el => {
      if (el.tagName[0] === 'H') { sec = el.textContent.trim(); return; }
      spans.push({ view, sec, file: el.getAttribute('data-study'), src: el.getAttribute('data-src'), text: el.textContent });
    });
  };
  const words = (host, view) => {  // numbers typed in the words: text outside number spans, code and tables' header cells excluded
    const walk = (n, sec) => {
      for (const c of n.childNodes) {
        if (c.nodeType === 1) {
          if (/^H[234]$/.test(c.tagName)) { sec.v = c.textContent.trim(); continue; }
          if (c.classList.contains('snum') || /^(CODE|PRE|SCRIPT|STYLE|SVG|IMG|TH)$/i.test(c.tagName)) continue;
          walk(c, sec);
        } else if (c.nodeType === 3 && /\d/.test(c.textContent)) {
          const t = c.textContent.replace(/\s+/g, ' ').trim();
          const m = t.match(/[^.;:]*\d[^.;:]*/g) || [];
          for (const s of m) if (/\d/.test(s.replace(/\b(19|20)\d\d\b|\b(Nov|Oct|Sep)\w* \d+|seeds? \d+-\d+|\d+-year|year \d+|\b[0-9a-f]{7}\b/g, ''))) typed.push({ view, sec: sec.v, text: s.trim() });
        }
      }
    };
    walk(host, { v: '' });
  };
  const r2 = w.document.getElementById('round2-body');
  read(r2, 'v5.9 section'); words(r2, 'v5.9 section');
  const cb = w.document.getElementById('cb');
  if (cb) {
    read(cb.querySelector('#cb-words'), 'central bank, summary'); words(cb.querySelector('#cb-words'), 'central bank, summary');
    const groups = [...cb.querySelectorAll('#cb-sw > *')];
    const btn = g => [...groups[g].querySelectorAll('button')];
    const nd = btn(0).length, ne = btn(1).length;
    for (let i = 0; i < nd; i++) for (let j = 0; j < ne; j++) {
      btn(0)[i].click(); btn(1)[j].click();
      const v = 'central bank, ' + btn(0)[i].textContent + ', ' + btn(1)[j].textContent;
      read(cb.querySelector('#cb-table'), v);
    }
  }
  return { spans, typed };
}

const num = t => { const x = parseFloat(t.replace(/[−–]/g, '-').replace(/[$,%+×x ]/g, '')); return isNaN(x) ? null : x; };
const load = (root, f) => JSON.parse(fs.readFileSync(path.join(root, 'data', 'studies', f + '.json'), 'utf8'));
const EST = ['effect', 'est', 'change', 'estimate', 'interaction', 'value', 'main row', 'offset share (%)', 'produced share (%)', 'break-even share', 'model'];
const CAT = ['class', 'category', 'material', 'word', 'gap rule', 'interval excludes zero', 'interval'];

(async () => {
  const [PUB, OUTF, OUTJ] = process.argv.slice(2);
  if (!PUB || !OUTF) { console.log(fs.readFileSync(__filename, 'utf8').split('*/')[0]); process.exit(1); }
  const A = await render(PUB), B = await render(REL);
  // the files: row labels (the columns that name a row), so that a row is paired by what it is, not by its place (a file may hold a row only when it
  // meets a rule, such as the cost per point where the fund lowers basket poverty)
  const NUMLAB = ['years', 'backed share (fraction of the payout)', 'backed share', 'displaced (%)', 'm', 'gain'];
  const loadT = (root, f) => { const [a, b] = f.split('.'), d = load(root, a); return b ? d[b] : d; };
  const T = {};
  const tab = f => {
    if (T[f]) return T[f];
    const P = loadT(PUB, f), R = loadT(REL, f);
    if (!P || !P.columns || JSON.stringify(P.columns) !== JSON.stringify(R.columns)) throw new Error(f + ': columns differ');
    const lab = P.columns.filter((c, j) => !CAT.includes(c) && (NUMLAB.includes(c) || P.data[j].every(v => typeof v === 'string' || v === null)));
    const g = (D, c, i) => D.data[D.columns.indexOf(c)][i];
    const labels = D => { const seen = {}; return D.data[0].map((_, i) => { const k = lab.map(c => g(D, c, i)).join(', '); seen[k] = (seen[k] || 0) + 1; return seen[k] > 1 ? k + ' #' + seen[k] : k; }); };
    const LP = labels(P), LR = labels(R), IR = new Map(LR.map((k, i) => [k, i]));
    return (T[f] = { P, R, g, lab, LP, LR, IR, IP: new Map(LP.map((k, i) => [k, i])) });
  };
  const where = s => { const m = /^row (\d+) (.+)$/.exec(s.src); if (!m) return { lab: '', col: s.src }; const t = tab(s.file), L = s === undefined ? null : null;
    return { lab: s.side === 'R' ? t.LR[+m[1]] : t.LP[+m[1]], col: m[2] }; };
  // pair by where it is printed and what it prints (view, file, row label and column, and the occurrence of that): some lists print a row only when
  // the row meets a rule (a reading that passes, a cell where an interval excludes zero), so the renders need not print the same figures
  const keyed = (S, side) => { const seen = {}; return S.map(s => { s.side = side; const w = where(s); const k = s.view + '|' + s.file + '|' + w.lab + '|' + w.col; seen[k] = (seen[k] || 0) + 1;
    return Object.assign({ key: k + '|' + seen[k], lab: w.lab, col: w.col }, s); }); };
  const KA = keyed(A.spans, 'P'), KB = keyed(B.spans, 'R'), MB = new Map(KB.map(s => [s.key, s])), MA = new Map(KA.map(s => [s.key, s]));
  const onlyPub = KA.filter(s => !MB.has(s.key)), onlyRel = KB.filter(s => !MA.has(s.key));
  const files = {}, changed = [];
  KA.filter(s => MB.has(s.key)).forEach(a => {
    const b = MB.get(a.key);
    const F = files[a.file] = files[a.file] || { n: 0, ch: 0, sg: 0 };
    F.n++;
    const x = num(a.text), y = num(b.text), ch = a.text !== b.text, sg = x !== null && y !== null && x * y < 0;
    F.ch += ch; F.sg += sg;
    if (ch) changed.push({ view: a.view, sec: a.sec, file: a.file, lab: a.lab, col: a.col, pub: a.text, rel: b.text, sign: sg });
  });
  // the files themselves: printed ranges and categories, row by row label
  const data = {};
  for (const f of Object.keys(files).filter(f => !f.includes('.'))) {
    const t = tab(f), P = t.P, R = t.R, g = t.g;
    const est = EST.find(c => P.columns.includes(c));
    const lo = P.columns.includes('main lo95') ? 'main lo95' : 'lo95', hi = lo === 'main lo95' ? 'main hi95' : 'hi95';
    const out = [], rng = [], cat = [];
    t.LP.forEach((L, i) => {
      const j = t.IR.get(L); if (j === undefined) return;
      if (est && P.columns.includes(lo) && P.columns.includes(hi)) {
        const e = g(R, est, j), l = g(P, lo, i), h = g(P, hi, i);
        if (e !== null && l !== null && h !== null && (e < l || e > h)) out.push({ L, est, pub: [g(P, est, i), l, h], rel: [e, g(R, lo, j), g(R, hi, j)] });
      }
      if (f === 'r2-curves') {
        const e = g(R, 'main row', j), l = g(P, 'lowest reading', i), h = g(P, 'highest reading', i);
        if (e < l || e > h) rng.push({ L, pub: [l, h], rel: e });
      }
      for (const c of CAT) if (P.columns.includes(c) && g(P, c, i) !== g(R, c, j)) cat.push({ L, col: c, pub: g(P, c, i), rel: g(R, c, j) });
    });
    const gone = t.LP.filter(L => !t.IR.has(L)), added = t.LR.filter(L => !t.IP.has(L));
    data[f] = { rows: P.data[0].length + (P.data[0].length === R.data[0].length ? '' : ' / ' + R.data[0].length), est, out, rng, cat, gone, added };
  }
  const rowLabel = (f, lab) => lab;
  // the typed numbers in the words, published and release (the words are the same script; they may print a count computed from a file)
  const tyA = A.typed.map(t => t.view + ' | ' + t.sec + ' | ' + t.text), tyB = B.typed.map(t => t.view + ' | ' + t.sec + ' | ' + t.text);
  const md = ['# The findings page, published against the release: every printed figure', '',
    'Item F1 of the release checklist (the page part). The findings page’s v5.9 section and its central-bank section (every switch position) rendered from the published data files and from the release data files (engine 50bc51d, v5.9.23), with the same scripts; every printed number paired with its counterpart. ' +
    'Command: `node dev/tools/s93_page_check.js <published tree> ' + path.basename(OUTF) + '`, the published tree from `git archive origin/main findings.html site data`.', '',
    '## 1. Counts by data file', '',
    '| Data file | Figures printed in both | Printed figure changes | Sign changes | Rows | Release estimate outside the published 95% interval | Main row outside the published range across readings | Category changes |',
    '|---|---|---|---|---|---|---|---|'];
  const tot = [0, 0, 0, 0, 0, 0];
  for (const f of Object.keys(files).sort()) {
    const F = files[f], d = data[f.split('.')[0]], isSub = f.includes('.');
    const o = isSub ? '' : (d.est ? d.out.length : 'no interval'), r = isSub ? '' : (f === 'r2-curves' ? d.rng.length : ''), c = isSub ? '' : d.cat.length;
    md.push('| `' + f + '` | ' + F.n + ' | ' + F.ch + ' | ' + F.sg + ' | ' + (isSub ? '' : d.rows) + ' | ' + o + ' | ' + r + ' | ' + c + ' |');
    tot[0] += F.n; tot[1] += F.ch; tot[2] += F.sg;
    if (!isSub) { tot[3] += d.out.length; tot[4] += d.rng.length; tot[5] += d.cat.length; }
  }
  md.push('| all | ' + tot[0] + ' | ' + tot[1] + ' | ' + tot[2] + ' | | ' + tot[3] + ' | ' + tot[4] + ' | ' + tot[5] + ' |', '',
    'A printed figure changes when its printed text differs (the last printed digit or more). The intervals and ranges are the published ones the page prints; the estimate is the release one.', '',
    '## 2. Every printed figure that changes sign', '', '| Where | Section | File | Row | Column | Published | Release |', '|---|---|---|---|---|---|---|');
  for (const c of changed.filter(c => c.sign)) md.push('| ' + [c.view, c.sec, '`' + c.file + '`', c.lab, c.col, c.pub, c.rel].join(' | ') + ' |');
  md.push('', '## 3. Rows whose category changes', '', '| File | Row | Column | Published | Release |', '|---|---|---|---|---|');
  for (const f of Object.keys(data).sort()) for (const c of data[f].cat) md.push('| `' + f + '` | ' + c.L + ' | ' + c.col + ' | ' + c.pub + ' | ' + c.rel + ' |');
  md.push('', 'Rows held in only one of the two files (a row the file holds only when it meets a rule):', '');
  for (const f of Object.keys(data).sort()) { const d = data[f]; if (d.gone.length || d.added.length) md.push('- `' + f + '`: published only: ' + (d.gone.join('; ') || 'none') + '. Release only: ' + (d.added.join('; ') || 'none') + '.'); }
  md.push('', '## 4. The main row outside the published range across readings (specification curves)', '', '| Row | Published range | Release main row |', '|---|---|---|');
  for (const c of data['r2-curves'].rng) md.push('| ' + c.L + ' | ' + c.pub.map(v => +v.toFixed(4)).join(' to ') + ' | ' + (+c.rel.toFixed(4)) + ' |');
  md.push('', '## 5. Release estimates outside the published 95% interval', '', '| File | Row | Estimate | Published (estimate, interval) | Release (estimate, interval) |', '|---|---|---|---|---|');
  for (const f of Object.keys(data).sort()) for (const c of data[f].out) md.push('| `' + f + '` | ' + c.L + ' | ' + c.est + ' | ' + c.pub.map(v => +(+v).toPrecision(4)).join(', ') + ' | ' + c.rel.map(v => +(+v).toPrecision(4)).join(', ') + ' |');
  md.push('', '## 6. Numbers typed in the words', '',
    'Every number in the sections’ own words (outside a number span; years, dates, seed ranges and commits left out). These are not read from a data file, so each is read by hand against the release figures. ' +
    (JSON.stringify(tyA) === JSON.stringify(tyB) ? 'They are the same in both renders.' : 'They differ between the renders (counts computed from a file).'), '',
    '| Where | Section | Text |', '|---|---|---|');
  B.typed.forEach(t => md.push('| ' + t.view + ' | ' + t.sec + ' | ' + t.text.replace(/\|/g, '/') + ' |'));
  md.push('', '## 7. Figures printed in only one of the two renders', '',
    'A list that prints a row only when it meets a rule prints a different set of rows when the data change: ' + onlyPub.length + ' figures are printed from the published data only and ' + onlyRel.length + ' from the release data only.', '',
    '| Render | Where | Section | File | Row | Column | Printed |', '|---|---|---|---|---|---|---|');
  for (const [w, S] of [['published only', onlyPub], ['release only', onlyRel]]) for (const c of S) md.push('| ' + [w, c.view, c.sec, '`' + c.file + '`', c.lab, c.col, c.text].join(' | ') + ' |');
  md.push('', '## 8. Every printed figure that changes', '', '| Where | Section | File | Row | Column | Published | Release |', '|---|---|---|---|---|---|---|');
  for (const c of changed) md.push('| ' + [c.view, c.sec, '`' + c.file + '`', c.lab, c.col, c.pub, c.rel].join(' | ') + ' |');
  fs.writeFileSync(OUTF, md.join('\n') + '\n');
  if (OUTJ) fs.writeFileSync(OUTJ, JSON.stringify({ totals: { printed: tot[0], changed: tot[1], sign: tot[2], outsideInterval: tot[3], outsideRange: tot[4], category: tot[5] }, files,
    changed, category: Object.fromEntries(Object.entries(data).map(([f, d]) => [f, d.cat])), outsideInterval: Object.fromEntries(Object.entries(data).map(([f, d]) => [f, d.out])),
    outsideRange: data['r2-curves'].rng, onlyPublished: onlyPub, onlyRelease: onlyRel, typed: B.typed }, null, 1) + '\n');
  console.log('s93_page_check: %d published-only, %d release-only', onlyPub.length, onlyRel.length);
  console.log('s93_page_check: %d figures printed in both, %d change as printed, %d change sign; %d rows outside the published interval, %d outside the range across readings, %d category changes; %d typed numbers in the words',
    tot[0], tot[1], tot[2], tot[3], tot[4], tot[5], B.typed.length);
})().catch(e => { console.error(e.message); process.exit(1); });
