/* S47 (Nov 6, 2026): how far the re-derived spending share moves the frozen model's figures (research-update prereg/run-manifest.md section 6 item 4:
 * "if it differs, that is a dated amendment before the freeze, and the measured effect is recorded"). Re-derivation: dev/tools/s47_spend.js,
 * dev/runs/s47-spend/rederive.json.
 *
 * Rows (each environment, CPS earnings yardstick, 500 adults, 20 years, seeds paired), all on the frozen engine (harness.js frozenRow):
 *   three designs: none, the release design, the C2.2 design (harness.js c22Design);
 *   three spending shares, each set study-wide as the method sets it (the supply path and every row): 0.593 (today's SPEND_SOURCED), the share re-derived
 *   by the method's own formula (saving over wages) and the share re-derived on saving over disposable income.
 * Every row carries the runner's reference settings (relMainCfgs, today's safety net with the work rule and slope, REL_V52_STUDY).
 *
 *   node dev/tools/s47_spend_effect.js --env=ref|adv|st --seeds=1-50 --shares=0.593,0.779,0.877 --out=FILE.json
 *   node dev/tools/s47_spend_effect.js --table FILE_ref.json FILE_adv.json FILE_st.json
 * Measurement only: no figure here is a target and nothing is tuned to it. */
'use strict';
const fs = require('fs'), path = require('path');
const ENVN = {ref: 'FULL_INTEGRATION', adv: 'ADVERSE_REFERENCE', st: 'STRESS_TEST'}, ENVL = {ref: 'Reference', adv: 'Adverse', st: 'Stress'};
const DES = ['none', 'release', 'c22'];
const KEYS = ['fgt0PY', 'pov', 'bNAPy', 'nbleiPov', 'fgt2PY', 'endoAnn', 'pLev20', 'medWealthReal', 'cost', 'emp', 'giniD', 'hhDebt20'];
const KL = {fgt0PY: 'basket poverty (% of person-years)', pov: 'wealth poverty, year 20 (%)', bNAPy: 'design-neutral BLEI below 30 days (% of person-years)',
  nbleiPov: 'design-neutral BLEI below 30 days, year 20 (%)', fgt2PY: 'basket poverty severity (FGT2 x100)', endoAnn: 'programme inflation (yearly rate, %)',
  pLev20: 'price level, year 20', medWealthReal: 'median real wealth, year 20 ($)', cost: 'programme cost per adult-year ($)', emp: 'employment (%)',
  giniD: 'Gini, disposable income', hhDebt20: 'families with net worth below zero, year 20 (%)'};

function run(env, lo, hi, shares, file) {
  const H = require(path.join(__dirname, '..', '..', 'harness.js')), svN = H.applyNR6(), svG = H.tbSetG(H.TB_PROFILE_G), t0 = Date.now(), out = {env, seeds: [lo, hi], shares, rows: {}};
  try {
    const P = Object.assign({}, H[ENVN[env]], {years: 20, nAgents: 500});
    shares.forEach(s => {
      const R0 = DES.map(d => { const c = H.relMainCfgs(H.tbPresets(P)).map(x => Object.assign(x, {sc: s, sn: {abawd: true, slope: true}}))[d === 'none' ? 0 : 1];
        c.lt = {s: 'all', m: 'all'}; if (d === 'c22') H.c22Design(c); H.frozenRow(c); return [s + '.' + d, c]; });
      const so = Object.assign({fin: 'tax', aT: 0, a: 0, X: 0, sc: s}, H.REL_V52_STUDY), R = H.tbStudy(R0.map(r => r[1]), hi, P, so, lo);
      R0.forEach((r, i) => { out.rows[r[0]] = {}; KEYS.forEach(k => { out.rows[r[0]][k] = Array.from(R[i]._s[k]); }); });
    });
    out.seconds = (Date.now() - t0)/1000;
    fs.writeFileSync(file, JSON.stringify(out));
    console.log(env + ': seeds ' + lo + '-' + hi + ', shares ' + shares.join(', ') + ', ' + out.seconds.toFixed(0) + ' s -> ' + file);
  } finally { H.resetNR6(svN); H.tbSetG(svG); }
}
function diff(x, y) { const n = x.length, d = x.map((v, i) => v - y[i]), m = d.reduce((a, b) => a + b, 0)/n;
  const sd = Math.sqrt(d.reduce((a, b) => a + (b - m)*(b - m), 0)/Math.max(1, n - 1)); return [m, 1.96*sd/Math.sqrt(n)]; }
function mean(x) { return x.reduce((a, b) => a + b, 0)/x.length; }
function f(v, k) { const x = v*(k === 'endoAnn' ? 100 : 1), a = Math.abs(x); return x.toFixed(k === 'pLev20' || k === 'giniD' ? 4 : a >= 100 ? 0 : 2); }
function table(files) {
  const L = [];
  files.forEach(file => {
    const D = JSON.parse(fs.readFileSync(file, 'utf8')), R = D.rows, S = D.shares, b = S[0], n = D.seeds[1] - D.seeds[0] + 1;
    L.push('### ' + ENVL[D.env] + ' (seeds ' + D.seeds[0] + '-' + D.seeds[1] + ', ' + n + ' paired)', '');
    DES.forEach(d => {
      L.push('**' + {none: 'No programme', release: 'Release design', c22: 'C2.2 design'}[d] + '** (frozen engine)', '');
      L.push('| Measure | share ' + b + ' | ' + S.slice(1).map(s => 'share ' + s + ' | change').join(' | ') + ' |', '|---|---|' + S.slice(1).map(() => '---|---|').join(''));
      KEYS.forEach(k => { const g = s => R[s + '.' + d][k];
        L.push('| ' + KL[k] + ' | ' + f(mean(g(b)), k) + ' | ' + S.slice(1).map(s => { const [m, h] = diff(g(s), g(b)); return f(mean(g(s)), k) + ' | ' + f(m, k) + ' ± ' + f(h, k); }).join(' | ') + ' |'); });
      L.push('');
    });
    L.push('**Programme effects (design minus no programme at the same share, paired)**', '');
    L.push('| Design | Measure | ' + S.map(s => 'share ' + s).join(' | ') + ' | ' + S.slice(1).map(s => s + ' - ' + b).join(' | ') + ' |', '|---|---|' + S.map(() => '---|').join('') + S.slice(1).map(() => '---|').join(''));
    ['release', 'c22'].forEach(d => ['fgt0PY', 'pov', 'bNAPy', 'endoAnn', 'medWealthReal'].forEach(k => {
      const e = s => R[s + '.' + d][k].map((v, i) => v - R[s + '.none'][k][i]);
      L.push('| ' + d + ' | ' + KL[k] + ' | ' + S.map(s => f(mean(e(s)), k)).join(' | ') + ' | ' + S.slice(1).map(s => { const [m, h] = diff(e(s), e(b)); return f(m, k) + ' ± ' + f(h, k); }).join(' | ') + ' |'); }));
    L.push('');
  });
  console.log(L.join('\n'));
}
const A = process.argv.slice(2), arg = k => { const a = A.find(x => x.startsWith('--' + k + '=')); return a ? a.slice(k.length + 3) : null; };
if (A[0] === '--table') table(A.slice(1));
else { const s = (arg('seeds') || '1-50').split('-').map(Number), env = arg('env') || 'ref';
  run(env, s[0], s[1], (arg('shares') || '0.593,0.779,0.877').split(',').map(Number), arg('out') || 's47-spend-effect-' + env + '.json'); }
