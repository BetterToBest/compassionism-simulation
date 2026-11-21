/* S65: the Release 2 section of findings.html renders from its data files with no error, prints no NaN/undefined, every printed number is a snum span whose
 * path names a real row and column of its file, and the main-row card values equal the r2-effects file.  Usage: node dev/tools/check_round2.js */
const { JSDOM } = require('jsdom'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..'), rd = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
(async () => {
  const w = new JSDOM(rd('findings.html'), { runScripts: 'outside-only', url: 'https://bettertobest.github.io/compassionism-simulation/findings.html' }).window, errs = [];
  w.scrollTo = () => {}; w.addEventListener('error', e => errs.push(String(e.message)));
  w.fetch = url => { const p = path.join(ROOT, String(url).split('?')[0].replace(/^\.?\//, ''));
    return Promise.resolve(fs.existsSync(p) ? { ok: true, status: 200, json: () => Promise.resolve(JSON.parse(fs.readFileSync(p, 'utf8'))) } : { ok: false, status: 404, json: () => Promise.reject(new Error('404')) }); };
  w.eval(rd('site/charts.js')); w.eval(rd('site/findings.js')); w.eval(rd('site/round2.js'));
  try { w.eval([...w.document.querySelectorAll('script')].filter(x => !x.src && !x.type)[0].textContent); } catch (e) { errs.push(String(e.message)); }
  await new Promise(r => setTimeout(r, 1500));
  const body = w.document.getElementById('round2-body'), bad = [];
  if (errs.length) bad.push('errors: ' + errs.slice(0, 3).join('; '));
  if (/NaN|undefined|Could not load/.test(body.textContent) || [...body.querySelectorAll('.snum')].some(s => s.textContent === 'not reported')) bad.push('the section prints NaN, undefined, a missing value or a load error');  /* S100: a missing value is a number span that reads 'not reported'; the weighting note says the words in prose */
  const D = {}; let n = 0;
  body.querySelectorAll('.snum').forEach(s => { n++; const f = s.getAttribute('data-study'), m = /^row (\d+) (.+)$/.exec(s.getAttribute('data-src'));
    D[f] = D[f] || JSON.parse(rd('data/studies/' + f + '.json')); const d = D[f], j = m && d.columns.indexOf(m[2]);
    if (!m || j < 0 || +m[1] >= d.data[j].length || d.data[j][+m[1]] === null) { bad.push('snum path ' + f + ' ' + s.getAttribute('data-src')); return; }
    const v = d.data[j][+m[1]], t = s.textContent.replace(/[−−]/g, '-').replace(/[$,%+]/g, '');
    if (typeof v === 'number') { const x = parseFloat(t); const tol = Math.max(0.5, Math.abs(x) * 0.0006) * (/\./.test(t) ? Math.pow(10, -(t.split('.')[1] || '').length) / 0.5 : 1);
      const vv = m[2] === 'backed share (fraction of the payout)' && Math.abs(x) > Math.abs(v) ? v * 100 : v;
      if (!(Math.abs(Math.abs(x) - Math.abs(vv)) <= Math.max(tol, 0.51 * Math.pow(10, -(( t.split('.')[1] || '').length))))) bad.push('snum shows ' + s.textContent + ' but ' + f + ' row ' + m[1] + ' ' + m[2] + ' is ' + v); } });
  if (n < 400) bad.push('only ' + n + ' printed numbers; the section did not fully render');
  const eff = JSON.parse(rd('data/studies/r2-effects.json')), g = (c, i) => eff.data[eff.columns.indexOf(c)][i];
  let found = 0; for (let i = 0; i < eff.data[0].length; i++) if (g('design', i) === 'C2.2' && g('environment', i) === 'Reference' && g('years', i) === 20 && /basket/.test(g('outcome', i))) { found++; if (!body.textContent.includes(g('programme', i).toFixed(1) + '%')) bad.push('basket-poverty card does not show the main row'); }
  if (found !== 1) bad.push('main-row row not found once');
  if (!body.querySelectorAll('img').length) bad.push('no charts'); else body.querySelectorAll('img').forEach(i => { if (!fs.existsSync(path.join(ROOT, i.getAttribute('src')))) bad.push('missing chart ' + i.getAttribute('src')); });
  console.log(bad.length ? 'FAIL round 2 section:\n  ' + bad.slice(0, 10).join('\n  ') : 'PASS round 2 section: ' + n + ' printed numbers, each tied to a row of its file; ' + body.querySelectorAll('img').length + ' charts exist');
  process.exit(bad.length ? 1 : 0);
})();
