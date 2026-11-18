#!/usr/bin/env python3
"""S82 part 3b (Nov 18, 2026): the findings page's data for the S82 study (data/studies/s82-supply.json and s82-breakeven.json), from the tables tool's summary.

  python3 dev/tools/s82_page_data.py <compassionism-sim-results>/s82-tables-aa2a4e0/s82-summary.json

Decision rule 5 of research-update prereg/2026-11-s82-v6-supply-indexing.md: the findings page's dated note on "the poverty effects barely depend on
backing" is replaced by the curve under the sourced readings, with the restricted and strict readings beside them and the break-even shares under each.
The page (site/round2.js) prints every figure from this file; no figure is typed there. Copied as the tables tool computed them (effects: programme
minus its own no-programme run, mean over seeds 1-500; 95% paired-bootstrap intervals, 10,000 replicates). Rows: the curve (no limit; the three
supply readings with each sharing rule; the wage and BU-delay readings) for basket poverty, wealth poverty (yearly average), median real wealth
(weighted) and programme inflation, every environment and horizon; and the break-even backed shares of each reading. Standard library only."""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')]
OUTS = [('fgt0PY', 'basket poverty (points)', 1.0), ('ppovA', 'wealth poverty, yearly average (points)', 1.0),
        ('wtMedE', 'median real wealth, weighted (year-0 $)', 1.0), ('endoAnn', 'programme inflation (points a year)', 100.0)]
RULES = [('pay', "the market's rule"), ('even', 'even'), ('bu', "the design's rule")]
RDS = [('sourced', 'sourced'), ('restricted', 'restricted'), ('strict', 'strictest case')]
WAGES = [('B.w0.5.c0', 'wages follow half of programme inflation, never made up'), ('B.w0.75.c0', 'wages follow three quarters, never made up'),
         ('B.w0.5.c1', 'wages follow half, made up a year later'), ('B.w0.75.c1', 'wages follow three quarters, made up a year later')]
LAGS = [('C.L0.125', 'the BU a month behind'), ('C.L0.25', 'the BU a quarter behind'), ('C.L1', 'the BU a year behind'), ('C.L2', 'the BU two years behind (a bound)')]
SHARES = ['0', '0.25', '0.5', '0.75', '1']


def rnd(x, k):
    return None if x is None else round(x * k, 6)


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: s82_page_data.py <path to s82-summary.json>')
    S = json.load(open(sys.argv[1]))
    rows, be = [], []
    for e, en in ENVS:
        for yrs in (20, 40):
            R = S['results'][e + '-' + str(yrs)]

            def add(reading, share, eff):
                for k, lab, sc in OUTS:
                    c = eff[k]
                    rows.append([en, yrs, reading, float(share), lab, rnd(c['est'], sc), rnd(c['lo'], sc), rnd(c['hi'], sc)])

            def addbe(reading, b):
                for k, lab, sc in OUTS:
                    c = b['inflation5' if k == 'endoAnn' else k]
                    be.append([en, yrs, reading, 'inflation reaches 5 points a year' if k == 'endoAnn' else lab,
                               c['est'], c['lo'], c['hi'], 'none on the grid' if c['word'] == 'below 0' else (c['word'] or '')])
            for s in SHARES:
                add('no limit', s, R['base'][s])
            addbe('no limit', R['breakeven']['base'])
            for rd, rl in RDS:
                for sh, sl in RULES:
                    lab = rl + ', ' + sl
                    for s in SHARES[:4]:
                        add(lab, s, R['A']['A.%s.%s.a%s' % (rd, sh, s)]['eff'])
                    add(lab, '1', R['base']['1'])  # at full backing nothing is cut under any reading (check 3): the main row
                    addbe(lab, R['breakeven']['A.%s.%s' % (rd, sh)])
            for key, lab in WAGES + LAGS:
                part = R['B'] if key.startswith('B') else R['C']
                for s in SHARES:
                    add(lab, s, part[key + '.a' + s]['eff'])
                addbe(lab, R['breakeven'][key])
    cols = ['environment', 'years', 'reading', 'backed share', 'outcome', 'effect', 'lo95', 'hi95']
    bcols = ['environment', 'years', 'reading', 'outcome', 'break-even share', 'lo95', 'hi95', 'word']
    out = {'meta': {'id': 's82-supply', 'title': 'Limits on supply, wages that lag prices and a delayed BU (S82), along the backing curve',
                    'prereg': 'prereg/2026-11-s82-v6-supply-indexing.md (research-update; Amendments 1-6)', 'report': 'dev/reports/s82-supply-indexing.md',
                    'engine': S['engine'], 'seeds': 500, 'resultsFolder': 's82-tables-aa2a4e0', 'resultsRepo': 'BetterToBest/compassionism-sim-results',
                    'command': 'python3 dev/tools/s82_page_data.py s82-tables-aa2a4e0/s82-summary.json',
                    'intervals': '95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model\'s randomness only',
                    'limit': 'the supply limit cuts only the housing, care and food households receive; the money left over goes to other goods and the cut moves no price, '
                             'so wealth, basic living and inflation are the same with and without it',
                    'n': len(rows)},
           'columns': cols, 'data': [list(c) for c in zip(*rows)]}
    bout = {'meta': dict(out['meta'], id='s82-breakeven', n=len(be), title='Break-even backed shares (S82): scanning down from full backing, where each '
                         'reading\'s effect is no better than no programme, and where programme inflation reaches 5 points a year; "none on the grid" where no '
                         'grid point reaches it (never extrapolated)'),
            'columns': bcols, 'data': [list(c) for c in zip(*be)]}
    for name, obj in (('s82-supply', out), ('s82-breakeven', bout)):
        p = os.path.join(ROOT, 'data', 'studies', name + '.json')
        with open(p, 'w') as fh:
            json.dump(obj, fh, ensure_ascii=False, separators=(',', ':'))
        print('wrote %s: %d rows (engine %s)' % (os.path.relpath(p, ROOT), obj['meta']['n'], S['engine']))


if __name__ == '__main__':
    main()
