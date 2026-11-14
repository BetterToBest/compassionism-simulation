#!/usr/bin/env node
/* S68 (Nov 14, 2026): tables for the pilot (dev/tools/s68_pilot.js). Means over seeds; paired differences with 95% intervals (mean ± 1.96 sd/√n,
 * unadjusted for multiple comparisons). Usage: node dev/tools/s68_table.js [DIR]   reads DIR/s68-{ref,adv,st}.json, writes DIR/tables.md and DIR/summary.json */
'use strict';
const fs = require('fs'), path = require('path');
const DIR = process.argv[2] || path.join(__dirname, '..', 'runs', 's68-financing');
const ENVS = [['ref', 'Reference'], ['adv', 'Adverse'], ['st', 'Stress']];
const mean = v => v.reduce((a, x) => a + x, 0)/v.length;
const ci = v => { const m = mean(v), s = Math.sqrt(v.reduce((a, x) => a + (x - m)*(x - m), 0)/Math.max(1, v.length - 1)); return [m, m - 1.96*s/Math.sqrt(v.length), m + 1.96*s/Math.sqrt(v.length)]; };
const d = (a, b) => a.map((x, i) => x - b[i]);
const f = (x, p) => (x === null || x === undefined || isNaN(x)) ? 'n/a' : x.toFixed(p === undefined ? 1 : p);
const fc = (c, p) => f(c[0], p) + ' (' + f(c[1], p) + ' to ' + f(c[2], p) + ')';
const out = [], sum = {};
out.push('# S68 pilot: the financing identity and costs at the within-year price level (tables)', '',
  'Seeds 1-N per environment as in each file; 500 adults, 20 years; the frozen row (today\'s safety net, CPS earnings), round-2 switches off. Paired differences with 95% intervals, unadjusted. Money in year-0 dollars per adult-year; inflation `endoAnn` in % a year; poverty in % (basket: adult-years below the cost of living; wealth: adults below the line at year 20, all-cash wealth).', '');
ENVS.forEach(([e, name]) => {
  const fl = path.join(DIR, 's68-' + e + '.json'); if (!fs.existsSync(fl)) return;
  const R = JSON.parse(fs.readFileSync(fl, 'utf8')), A = Object.fromEntries(R.A.map(r => [r.row, r.s])), B = Object.fromEntries(R.B.map(r => [r.row, r.s]));
  const S = sum[e] = {seeds: R.seeds, commit: R.manifest && R.manifest.commit, dirty: R.manifest && R.manifest.dirty, A: {}, B: {}};
  out.push('## ' + name + ' (seeds 1-' + R.seeds + '; engine ' + (S.commit || '?').slice(0, 7) + (S.dirty ? ', dirty' : '') + ')', '');
  out.push('### (A) Who pays the programme', '',
    '| Row | Payout | Contribution raised | New money | Matched output | Unpaid (before fx.fin) | Unpaid, % of payout | Mean rate | Years at the cap (of 20) | Inflation | Basket poverty | Wealth poverty | Hours |',
    '|---|---|---|---|---|---|---|---|---|---|---|---|---|');
  R.A.forEach(r => { const s = r.s, m = k => s[k] ? mean(s[k]) : null;
    S.A[r.row] = Object.fromEntries(Object.keys(s).filter(k => s[k]).map(k => [k, mean(s[k])]));
    out.push('| ' + [r.row, f(m('finPay'), 0), f(m('finTax'), 0), f(m('finMoney'), 0), f(m('finMatch'), 0), f(m('finGap'), 0), f(m('finGapSh'), 2), f(100*m('tauMean'), 1) + '%', f(m('finCapYrs'), 1), f(100*m('endoAnn'), 2), f(m('fgt0PY')), f(m('pov')), f(100*m('hrs'), 1) + '%'].join(' | ') + ' |'); });
  out.push('', 'Against the no-programme run (paired):', '', '| Row | Basket poverty | Wealth poverty | Hours, % |', '|---|---|---|---|');
  R.A.slice(1).forEach(r => out.push('| ' + [r.row, fc(ci(d(r.s.fgt0PY, A.none.fgt0PY))), fc(ci(d(r.s.pov, A.none.pov))), fc(ci(d(r.s.hrs, A.none.hrs)).map(x => 100*x))].join(' | ') + ' |'));
  out.push('', 'The gap as new money against the gap unpaid (fx.fin \'money\' less \'report\', paired):', '', '| Design and reading | Inflation, points a year | Basket poverty | Wealth poverty |', '|---|---|---|---|');
  [['c22 tax', 'C2.2, flat contribution'], ['c22 hybrid', 'C2.2, hybrid'], ['rel tax', 'Release design, flat contribution']].forEach(([k, l]) => {
    const a = A[k + ' money'], b = A[k + ' report'], x = {endo: ci(d(a.endoAnn, b.endoAnn)).map(v => 100*v), basket: ci(d(a.fgt0PY, b.fgt0PY)), wealth: ci(d(a.pov, b.pov))}; S.A[k + ' diff'] = x;
    out.push('| ' + [l, fc(x.endo, 2), fc(x.basket), fc(x.wealth)].join(' | ') + ' |'); });
  out.push('', '### (B) Costs at the within-year price level (quarterly count of today\'s rule)', '',
    '| Row | Within-year level over opening | Basket poverty, published | At within-year prices | Depth (FGT1), published | At within-year prices |', '|---|---|---|---|---|---|');
  R.B.forEach(r => { const s = r.s; S.B[r.row] = Object.fromEntries(Object.keys(s).filter(k => s[k]).map(k => [k, mean(s[k])]));
    out.push('| ' + [r.row, f(mean(s.wyAvg), 4), f(mean(s.fgt0PY)), f(mean(s.wyF0PY)), f(mean(s.fgt1PY), 2), f(mean(s.wyF1PY), 2)].join(' | ') + ' |'); });
  out.push('', 'The programme\'s effect on basket poverty (against the no-programme run, paired), published and at within-year prices, and how far the reading moves it:', '',
    '| Design | Effect, published | Effect at within-year prices | Moved by |', '|---|---|---|---|');
  [['rel q4', 'Release design'], ['c22 q4', 'C2.2 (Source)']].forEach(([k, l]) => { const s = B[k], n = B['none q4'];
    const e0 = ci(d(s.fgt0PY, n.fgt0PY)), e1 = ci(d(s.wyF0PY, n.wyF0PY)), mv = ci(d(d(s.wyF0PY, n.wyF0PY), d(s.fgt0PY, n.fgt0PY))); S.B[k + ' effect'] = {pub: e0, wy: e1, moved: mv};
    out.push('| ' + [l, fc(e0), fc(e1), fc(mv)].join(' | ') + ' |'); });
  out.push('');
});
fs.writeFileSync(path.join(DIR, 'tables.md'), out.join('\n') + '\n');
fs.writeFileSync(path.join(DIR, 'summary.json'), JSON.stringify(sum, null, 1));
console.log('wrote ' + path.join(DIR, 'tables.md'));
