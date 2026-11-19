#!/usr/bin/env python3
"""S92 part 2 (Nov 19, 2026): question 3 of the preregistration on the private price at the sale
(research-update prereg/2026-11-s90-private-price-at-sale.md), read against the findings page itself.

  python3 dev/tools/s90_page_check.py SUMMARY RESULTS OUT.md

SUMMARY is s90-summary.json from dev/tools/s90_tables.py; RESULTS is a checkout of compassionism-sim-results holding the
six folders s90-sale-<env>-<years>-b8ccd8d.

1. Every main-row figure the v5.9 section of findings.html prints (site/round2.js: effects at 1 decimal, median real wealth in
   whole dollars, programme inflation at 2 decimals; the cards' programme levels at 1 decimal), now and at the sale: does the
   printed figure change, does its sign change, does the at-sale main row fall outside the printed range across readings
   (data/studies/r2-curves.json)?
2. An inspection beyond the preregistered outcomes: the distribution and work measures behind the page's "Who gains" and
   "Unfavourable results" prose (the keys of data/studies/r2-distribution.json and r2-work.json), seed means only: does any
   effect change sign at the sale?
"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s90_tables as T

OUT = {'bNAPy': 'basic living (adult-years below 30 days, points)', 'fgt0PY': 'cost of living (basket poverty, adult-years, points)',
       'ppovA': 'wealth poverty, yearly average (points)', 'wtMedE': 'median real wealth (year-0 $)', 'endoAnn': 'programme inflation (points a year)'}
NM = {'bNAPy': 'below 30 days of basic living', 'fgt0PY': 'basket poverty', 'ppovA': 'too little wealth, yearly average',
      'wtMedE': 'median real wealth', 'endoAnn': 'programme inflation'}
DES = {'c22': ('C2.2', 'full coverage'), 'rel': ('release design', 'opt-in')}
ENV = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}
DIST = [('dmWt1E', 'top 1% share of wealth'), ('dmWt10E', 'top 10% share of wealth'), ('dmYt1E', 'top 1% share of income'),
        ('dmYt10E', 'top 10% share of income'), ('dmYpE', 'Palma ratio of income'), ('dmWb50E', 'bottom 50% share of wealth'),
        ('dmYb50E', 'bottom 50% share of income'), ('dmMob00', 'stayed in the lowest wealth fifth'), ('dmMob44', 'stayed in the top wealth fifth'),
        ('dmMob04', 'lowest fifth to top fifth'), ('dmLsPY', "labour's share of money income"), ('dmFdE', 'families in debt'),
        ('emp', 'employment'), ('hrs', 'hours'), ('lfPart', 'participation')]


def table(path):
    d = json.load(open(path))
    return [{c: d['data'][j][i] for j, c in enumerate(d['columns'])} for i in range(len(d['data'][0]))]


def f1(x): return ('−' if x < 0 else '+') + format(abs(x), ',.1f')
def fu(x): return ('−$' if x < 0 else '+$') + format(abs(round(x)), ',')
def f2(x): return format(x, '.2f')


def main():
    if len(sys.argv) < 4: sys.exit(__doc__)
    S, R, OUTF = sys.argv[1], sys.argv[2], sys.argv[3]
    s = json.load(open(S))
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'studies')
    cur, eff = table(os.path.join(here, 'r2-curves.json')), table(os.path.join(here, 'r2-effects.json'))
    md = ['# The findings page read against the rerun with the private price at the sale', '',
          'Question 3 of the preregistration: does any statement on the findings page change in sign or in its printed rounding? '
          'Figures as `site/round2.js` prints them (effects at 1 decimal, median real wealth in whole dollars, programme inflation at 2 decimals). '
          'Mean over seeds 1-500. Command: `python3 dev/tools/s90_page_check.py s90-summary.json <results checkout> page-check.md`.', '',
          '## 1. Every main-row figure in the v5.9 section', '',
          '| Design | Environment | Years | Outcome | Printed now | At the sale | Printed figure changes | Sign changes | Outside the printed range across readings |',
          '|---|---|---|---|---|---|---|---|---|']
    n = [0, 0, 0, 0]
    for c in s['cells']:
        dn, dw = DES[c['design']]
        for o in c['outcomes']:
            k = o['key']
            if k not in OUT: continue
            L, A = o['lagged']['est'], o['sale']['est']
            fm = fu if k == 'wtMedE' else (f2 if k == 'endoAnn' else f1)
            cr = [r for r in cur if r['design'] == dn and r['environment'] == ENV[c['env']] and r['years'] == c['years'] and r['outcome'] == OUT[k]]
            out = 'not shown'
            if cr:
                lo, hi = cr[0]['lowest reading'], cr[0]['highest reading']
                out = 'yes (printed range %s to %s)' % (fm(lo), fm(hi)) if (A < lo or A > hi) else 'no'
            ch, sg = fm(L) != fm(A), L * A < 0
            n[0] += 1; n[1] += ch; n[2] += sg; n[3] += out.startswith('yes')
            md.append('| %s | %s | %d | %s | %s | %s | %s | %s | %s |' % (dw, ENV[c['env']], c['years'], NM[k], fm(L), fm(A),
                      'yes' if ch else 'no', 'yes' if sg else 'no', out))
    md += ['', '%d figures: %d change as printed, %d change sign, %d fall outside the printed range across readings.' % tuple(n), '',
           '## 2. The four cards (full coverage, Reference, 20 years): the programme level', '',
           '| Outcome | No programme | Programme, printed now | Programme, at the sale |', '|---|---|---|---|']
    c0 = [c for c in s['cells'] if c['design'] == 'c22' and c['env'] == 'ref' and c['years'] == 20][0]
    for r in eff:
        if r['design'] == 'C2.2' and r['environment'] == 'Reference' and r['years'] == 20:
            k = [k for k, v in OUT.items() if v == r['outcome']][0]
            lvl = r['no programme'] + [x for x in c0['outcomes'] if x['key'] == k][0]['sale']['est']
            if k == 'wtMedE': cells = ['$' + format(round(v), ',') for v in (r['no programme'], r['programme'], lvl)]
            elif k == 'endoAnn': cells = ['%.2f' % v for v in (r['no programme'], r['programme'], lvl)]
            else: cells = ['%.1f%%' % v for v in (r['no programme'], r['programme'], lvl)]
            md.append('| %s | %s |' % (NM[k], ' | '.join(cells)))
    md += ['', '## 3. Inspection: distribution and work measures (not preregistered; seed means, no intervals)', '',
           'The effect against no programme, lagged and at the sale, for the measures behind the page\'s "Who gains" and "Unfavourable results" prose.', '',
           '| Design | Environment | Years | Measure | Lagged | At the sale | Sign changes |', '|---|---|---|---|---|---|---|']
    flips = 0; cnt = 0
    for e in ['ref', 'adv', 'str']:
        for y in [20, 40]:
            rows = T.join(T.shards(os.path.join(R, 's90-sale-%s-%d-%s' % (e, y, s['engine']))))
            for d in ['c22', 'rel']:
                for k, lab in DIST:
                    if k not in rows[e + '.none']: continue
                    L = float(np.nanmean(rows[e + '.' + d][k] - rows[e + '.none'][k]))
                    A = float(np.nanmean(rows[e + '.' + d + '.sale'][k] - rows[e + '.none'][k]))
                    sg = L * A < 0; flips += sg; cnt += 1
                    md.append('| %s | %s | %d | %s | %+.3f | %+.3f | %s |' % (DES[d][1], ENV[e], y, lab, L, A, 'yes' if sg else 'no'))
    md += ['', '%d effects: %d change sign.' % (cnt, flips), '']
    open(OUTF, 'w').write('\n'.join(md))
    print('wrote %s: %d figures, %d change as printed, %d change sign, %d outside the range; inspection %d effects, %d change sign' % (OUTF, n[0], n[1], n[2], n[3], cnt, flips))


if __name__ == '__main__':
    main()
