#!/usr/bin/env python3
"""S100 part 2 (Nov 21, 2026): the findings page's data for the study of pay by household type and the child and dependent care credit in the
no-programme yardstick (data/studies/s100-yardstick.json and s100-effects.json), from the tables tool's summary.

  python3 dev/tools/s100_page_data.py <compassionism-sim-results>/s100-tables-e50a3b3/s100-summary.json

Research-update prereg/2026-11-s100-part-time-dcc.md. The page (site/round2.js) prints every figure from these files; no figure is typed there.
Copied as dev/tools/s100_tables.py computed them: means over seeds 1-500; 95% paired-bootstrap intervals (2,000 resamples, generator seed 9001);
Holm across the five primary outcomes within each design, environment and horizon for the change.

- s100-yardstick.json: the no-programme rows' tax-credit reach (overall and by household type), the care credit's reach and mean, and the levels of
  four primary outcomes, for every reading, environment and horizon, beside the US figure fixed in the preregistration and the gap rule's verdict
  (a share more than 3 points from the US figure, a dollar amount outside 0.80-1.25 times it; shares that the US measures at full take-up are judged
  only in the full take-up rows). Plus decision rule 2's summed gap of the four household types (Reference, 20 years, full take-up).
- s100-effects.json: per design, environment, horizon and reading, the programme's effect (programme row minus its no-programme row) and the change
  against today's main row (paired difference in differences) on the five primary and nine secondary outcomes, and the interaction
  (both - credit) - (pay by type - today's) on the five primary outcomes.
Standard library only."""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ENVS = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress'}
DES = {'c22': 'full coverage', 'rel': 'opt-in'}
READL = {'off': "today's main row", 'eh': 'pay by household type', 'cdc': 'the care credit', 'both': 'both',
         'pc0': 'both, partners independent', 'call': 'both, credit for every family', 'bound': 'both, credit in the no-programme run only',
         'off.full': "today's main row, full take-up", 'both.full': 'both, full take-up'}
PRIM = [('bNAPy', 'below 30 days of basic living (points)'), ('fgt0PY', 'basket poverty (points)'), ('ppovA', 'too little wealth, yearly average (points)'),
        ('wtMedE', 'median real wealth, weighted (year-0 $)'), ('endoAnn', 'programme inflation (points a year)')]
SEC = [('fgt2PY', 'poverty severity (squared gap)'), ('Er', 'real wage earnings per adult-year ($)'), ('dmYp50E', 'median real disposable income, last year, weighted ($)'),
       ('cost', 'programme cost per adult-year ($)'), ('wtF0E', 'basket poverty, last year, weighted (points)'), ('wtPovE', 'too little wealth, last year, weighted (points)'),
       ('snCdcM', 'care credit per adult-year ($)'), ('snEitcM', 'EITC per adult-year ($)'), ('snCtcM', 'refundable child tax credit per adult-year ($)')]
YM = [('snEitc', 'EITC reach, all adults (%)'), ('snEitcSg', 'EITC reach, single adults (%)'), ('snEitcSp', 'EITC reach, single parents (%)'),
      ('snEitcCn', 'EITC reach, couples without children (%)'), ('snEitcCk', 'EITC reach, couples with children (%)'),
      ('snCtc', 'refundable child tax credit reach, all adults (%)'), ('snCtcSp', 'refundable child tax credit reach, single parents (%)'),
      ('snCtcCk', 'refundable child tax credit reach, couples with children (%)'),
      ('snCdcK', 'care credit reach, families with a child under 13 (%)'), ('snCdcR', 'care credit per receiving family ($)'),
      ('fgt0PY', 'basket poverty (%)'), ('bNAPy', 'below 30 days of basic living (%)'), ('ppovA', 'too little wealth, yearly average (%)'),
      ('wtMedE', 'median real wealth, weighted (year-0 $)')]
US = {'snEitc': 11.77, 'snEitcSg': 8.62, 'snEitcSp': 49.77, 'snEitcCn': 4.55, 'snEitcCk': 16.54, 'snCtcSp': 45.31, 'snCtcCk': 19.00, 'snCdcK': 21.37, 'snCdcR': 606.0}
CDC = ('snCdcK', 'snCdcR')


def r(x):
    return None if x is None else round(x, 6)


def write(name, meta, cols, rows):
    obj = {'meta': dict(meta, id=name, n=len(rows)), 'columns': cols, 'data': [list(c) for c in zip(*rows)]}
    p = os.path.join(ROOT, 'data', 'studies', name + '.json')
    with open(p, 'w') as fh:
        json.dump(obj, fh, ensure_ascii=False, separators=(',', ':'))
    print('wrote %s: %d rows' % (os.path.relpath(p, ROOT), len(rows)))


def gap(k, read, v):
    """the gap rule's verdict, or None where the row cannot be compared (no US figure; a share the US measures at full take-up, outside a full
    take-up row; the care credit in a row without it)"""
    if k not in US:
        return None
    if k in CDC:
        if v == 0:
            return None
    elif not read.endswith('.full'):
        return None
    u = US[k]
    bad = not (0.8 <= v / u <= 1.25) if k == 'snCdcR' else abs(v - u) > 3
    return 'gap' if bad else 'within the rule'


def main():
    src = sys.argv[1]
    S = json.load(open(src))
    base = {'prereg': 'prereg/2026-11-s100-part-time-dcc.md (research-update)', 'report': 'dev/reports/s100-part-time-dcc.md', 'engine': S['engine'],
            'seeds': 500, 'resultsFolder': 's100-tables-' + S['engine'], 'resultsRepo': 'BetterToBest/compassionism-sim-results',
            'command': 'python3 dev/tools/s100_page_data.py s100-tables-%s/s100-summary.json' % S['engine'],
            'intervals': '95%% paired-bootstrap intervals over seeds 1-500 (%d resamples); the model\'s randomness only' % S['reps']}
    rows = []
    for cell, Y in S['yardstick'].items():
        e, y = cell.split('-')
        for read, vals in Y.items():
            for k, lab in YM:
                v = vals[k]
                rows.append((ENVS[e], int(y), READL[read], lab, r(v), US.get(k), gap(k, read, v)))
    R2 = S['rule2']
    rows.append(('Reference', 20, READL['off.full'], "sum of the four household types' EITC gaps (points)", r(R2['sumGapOff']), None, None))
    rows.append(('Reference', 20, READL['both.full'], "sum of the four household types' EITC gaps (points)", r(R2['sumGapBoth']), None, None))
    write('s100-yardstick', dict(base, title='The no-programme run against US data: tax-credit reach by household type, the care credit, and poverty levels, under each reading',
                                 terms="model: the no-programme run's mean over seeds; US: the figure fixed in the preregistration (CPS ASEC 2026, own tax unit, full take-up; the care credit: IRS Statistics of Income, tax year 2023); gap: the preregistered rule, more than 3 points away, or a dollar amount outside 0.80-1.25 times the US figure",
                                 rule2='holds' if R2['holds'] else 'does not hold'),
          ['environment', 'years', 'reading', 'measure', 'model', 'US', 'gap rule'], rows)
    rows = []
    for c in S['cells']:
        env, yrs, des = ENVS[c['env']], c['years'], DES[c['design']]
        for read, E in c['effect'].items():
            for k, lab in PRIM:
                o = E[k]
                rows.append((env, yrs, des, READL[read], 'effect', lab, r(o['est']), r(o['lo']), r(o['hi']), None))
        for read, E in c['change'].items():
            for k, lab in PRIM:
                o = E[k]
                rows.append((env, yrs, des, READL[read], 'change', lab, r(o['est']), r(o['lo']), r(o['hi']), 'excludes zero' if o['star'] else 'includes zero'))
            for k, lab in SEC:
                o = c['secondary'][read][k]
                rows.append((env, yrs, des, READL[read], 'change', lab, r(o['est']), r(o['lo']), r(o['hi']), None))
        for k, lab in PRIM:
            o = c['interaction'][k]
            rows.append((env, yrs, des, 'interaction', 'interaction', lab, r(o['est']), r(o['lo']), r(o['hi']),
                         'excludes zero' if (o['lo'] > 0 or o['hi'] < 0) else 'includes zero'))
    write('s100-effects', dict(base, title="The programme's effect under each reading of the yardstick, its change against today's main row, and the two additions' interaction",
                               terms="effect: programme row minus its no-programme row; change: the effect under the reading minus the effect in today's main row, paired by seed; interaction: (both minus the credit alone) minus (pay by type alone minus today's); interval: Holm-adjusted across the five primary outcomes for the change (unadjusted for the interaction and the secondary outcomes)"),
          ['environment', 'years', 'design', 'reading', 'kind', 'outcome', 'est', 'lo95', 'hi95', 'interval'], rows)


if __name__ == '__main__':
    main()
