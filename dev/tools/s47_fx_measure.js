/* S47 (Nov 5, 2026): how far each correction of the frozen engine moves the figures, before the design freeze.
 * research-update prereg/run-manifest.md section 6 item 1; dev/DECISIONS.md, S47.
 *
 * Rows (each environment, CPS earnings yardstick, 500 adults, 20 years, seeds paired):
 *   three designs: none (no programme), the release design, the C2.2 design (automatic, BU at the cost of food, housing and medical care, indexed);
 *   seven engine settings: published (no correction), au (the outside audit's three corrections), au + each fx part alone (pthb, hb, ab, sp),
 *   frozen (au + every fx part).
 * Every row carries the runner's reference settings (relMainCfgs, sc SPEND_SOURCED, today's safety net with the work rule and slope).
 *
 *   node dev/tools/s47_fx_measure.js --env=ref|adv|st --seeds=1-50 --out=FILE.json
 *   node dev/tools/s47_fx_measure.js --table FILE_ref.json FILE_adv.json FILE_st.json   (prints the markdown tables; .json.gz read too)
 * Results of Nov 5, 2026 (engine of pull request 74): dev/runs/s47-fx/*.json.gz; tables dev/reports/s47-fx-tables.md; report dev/reports/s47-fx.md.
 *
 * Measurement only: no figure here is a target and nothing is tuned to it. */
'use strict';
const fs = require('fs'), path = require('path');
const ENVN = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'};
const ENVL = {ref: 'Reference', adv: 'Adverse', st: 'Stress'};
const SETS = [['published', {}], ['au', {au: true}], ['au+pthb', {au: true, fx: {pthb: true}}], ['au+hb', {au: true, fx: {hb: true}}],
  ['au+ab', {au: true, fx: {ab: true}}], ['au+sp', {au: true, fx: {sp: true}}], ['frozen', {au: true, fx: true}]];
const DES = ['none', 'release', 'c22'];
const KEYS = ['fgt0PY', 'pov', 'bleiPov', 'nbleiPov', 'fgt2PY', 'endoAnn', 'pLev20', 'medWealthReal', 'cost', 'emp', 'giniD', 'snAbN'];
const KL = {fgt0PY: 'basket poverty (% of person-years)', pov: 'wealth poverty, year 20 (%)', bleiPov: 'BLEI below precarious, year 20 (%)',
  nbleiPov: 'design-neutral BLEI below precarious (%)', fgt2PY: 'basket poverty severity (FGT2 x100)', endoAnn: 'programme inflation (yearly rate, %)',
  pLev20: 'price level, year 20', medWealthReal: 'median real wealth, year 20 ($)', cost: 'programme cost per adult-year ($)', emp: 'employment (%)',
  giniD: 'Gini, disposable income', snAbN: 'SNAP work-rule months lost (per adult)'};

function rows(H, P) {
  const SC = H.SPEND_SOURCED, SN = {abawd: true, slope: true}, out = [];
  SETS.forEach(([sn, sw]) => DES.forEach(d => {
    const c = H.relMainCfgs(H.tbPresets(P)).map(x => Object.assign(x, {sc: SC, sn: SN}))[d === 'none' ? 0 : 1];
    c.lt = {s: 'all', m: 'all'};
    if (d === 'c22') { c.c22 = {auto: true, idx: 'needs'}; c.p = Object.assign({}, c.p, {bu: H.c22NeedsBU()}); }
    Object.assign(c, JSON.parse(JSON.stringify(sw)));
    out.push([sn + '.' + d, c]);
  }));
  return out;
}

function run(env, lo, hi, file) {
  const H = require(path.join(__dirname, '..', '..', 'harness.js'));
  const svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now();
  try {
    const P = Object.assign({}, H[ENVN[env]], {years: 20, nAgents: 500}), R0 = rows(H, P);
    const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: H.SPEND_SOURCED}, H.REL_V52_STUDY);
    const R = H.tbStudy(R0.map(r => r[1]), hi, P, so, lo), out = {env, seeds: [lo, hi], rows: {}};
    R0.forEach((r, i) => { out.rows[r[0]] = {}; KEYS.forEach(k => { out.rows[r[0]][k] = Array.from(R[i]._s[k]); }); });
    out.seconds = (Date.now() - t0)/1000;
    fs.writeFileSync(file, JSON.stringify(out));
    console.log(env + ': ' + R0.length + ' rows, seeds ' + lo + '-' + hi + ', ' + out.seconds.toFixed(0) + ' s -> ' + file);
  } finally { H.resetNR6(svN); H.tbSetG(svG); }
}

/* Paired difference x - y over seeds: mean and normal 95% interval. */
function diff(x, y) { const n = x.length, d = x.map((v, i) => v - y[i]), m = d.reduce((a, b) => a + b, 0)/n;
  const sd = Math.sqrt(d.reduce((a, b) => a + (b - m)*(b - m), 0)/Math.max(1, n - 1)); return [m, 1.96*sd/Math.sqrt(n)]; }
function mean(x) { return x.reduce((a, b) => a + b, 0)/x.length; }
function sc(k) { return k === 'endoAnn' ? 100 : 1; }
function f(v, k) { const a = Math.abs(v*sc(k)); return (v*sc(k)).toFixed(k === 'pLev20' || k === 'giniD' ? 4 : a >= 100 ? 0 : 2); }

function table(files) {
  const L = [];
  files.forEach(file => {
    const raw = fs.readFileSync(file), D = JSON.parse((/\.gz$/.test(file) ? require('zlib').gunzipSync(raw) : raw).toString('utf8')), R = D.rows, n = D.seeds[1] - D.seeds[0] + 1;
    L.push('### ' + ENVL[D.env] + ' (seeds ' + D.seeds[0] + '-' + D.seeds[1] + ', ' + n + ' paired; ' + D.seconds.toFixed(0) + ' s on one process)', '');
    L.push('Levels on the published engine, and the change each setting makes against the audit-corrected engine (au); the last column is the frozen engine against the published one. Mean change, with its 95% interval, over the paired seeds.', '');
    DES.forEach(d => {
      L.push('**' + {none: 'No programme', release: 'Release design', c22: 'C2.2 design'}[d] + '**', '');
      L.push('| Measure | published | au - published | pthb | hb | ab | sp | frozen - au | frozen - published |', '|---|---|---|---|---|---|---|---|---|');
      KEYS.forEach(k => { const g = s => R[s + '.' + d][k], cell = (a, b) => { const [m, h] = diff(g(a), g(b)); return f(m, k) + ' ± ' + f(h, k); };
        L.push('| ' + KL[k] + ' | ' + f(mean(g('published')), k) + ' | ' + cell('au', 'published') + ' | ' + ['pthb', 'hb', 'ab', 'sp'].map(p => cell('au+' + p, 'au')).join(' | ') +
          ' | ' + cell('frozen', 'au') + ' | ' + cell('frozen', 'published') + ' |'); });
      L.push('');
    });
    L.push('**Programme effects (design minus no programme, paired): how the corrections move them**', '');
    L.push('| Design | Measure | published | au | frozen | frozen - published |', '|---|---|---|---|---|---|');
    ['release', 'c22'].forEach(d => ['fgt0PY', 'pov', 'bleiPov', 'endoAnn', 'medWealthReal'].forEach(k => {
      const e = s => R[s + '.' + d][k].map((v, i) => v - R[s + '.none'][k][i]), me = s => f(mean(e(s)), k), [m, h] = diff(e('frozen'), e('published'));
      L.push('| ' + d + ' | ' + KL[k] + ' | ' + me('published') + ' | ' + me('au') + ' | ' + me('frozen') + ' | ' + f(m, k) + ' ± ' + f(h, k) + ' |'); }));
    L.push('');
  });
  console.log(L.join('\n'));
}

const A = process.argv.slice(2), arg = k => { const a = A.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : null; };
if (A[0] === '--table') table(A.slice(1));
else { const s = (arg('seeds') || '1-50').split('-').map(Number); run(arg('env') || 'ref', s[0], s[1], arg('out') || 's47-fx-' + (arg('env') || 'ref') + '.json'); }
