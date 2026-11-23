#!/usr/bin/env python3
"""S94 part 5 (Nov 21, 2026): the findings page's data for the Creative Collectives' lending study (data/studies/s94-fund.json, s94-charters.json,
s94-interaction.json and s94-levels.json), from the tables tool's summary.

  python3 dev/tools/s94_page_data.py <compassionism-sim-results>/s94-tables-c5682f9/s94-summary.json

Research-update prereg/2026-11-s94-collectives-lending.md (Amendments 1-2). The page (site/round2.js) prints every figure from these files; no figure
is typed there. Copied as the tables tool computed them: mean of the paired difference over seeds 1-500 (row minus the main row of the same design),
95% paired-bootstrap intervals (10,000 replicates), categories after Holm over the six readings of each row (improves, worsens or no change).

- s94-fund.json: every reading of the fund (the main reading and eight others), each environment, horizon and design: the six readings' change, the
  programme's cost, the contribution, the running-cost subsidy, the fund's net outlay, the community businesses' share of essential sales at years 5,
  10 and 20 (or 40), and the cost per point of basket poverty where the fund lowers it.
- s94-charters.json: charters of public utilities at 1/7, 1/3 and 2/3 (no fund), the same readings, the added subsidy and the cost per point.
- s94-interaction.json: the fund's and charters' interaction (the joint change minus the sum of the two alone) for the six readings and the cost.
- s94-levels.json: the main row's and the fund's levels of the community businesses' share, and the main row's effect against no programme.
Standard library only."""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')]
DES = [('c22', 'full coverage'), ('rel', 'opt-in')]
PRIM = [('fgt0PY', 'basket poverty (points)'), ('ppovA', 'wealth poverty, yearly average (points)'), ('pov', 'wealth poverty, last year (points)'),
        ('wtMedE', 'median real wealth, weighted (year-0 $)'), ('medWealthReal', 'median real wealth, unweighted (year-0 $)'),
        ('secM3A', 'savings under three months of need (points)')]
COST = ('cost', 'programme cost per adult a year ($)')
SEC = [COST, ('tax', 'the contribution that finances the programme, per adult a year ($)'), ('poSub', "community businesses' running-cost subsidy, per adult a year ($)"),
       ('clNet', "the fund's net outlay (outlay less interest), per adult a year ($)"), ('chSub', 'added subsidy from charters, per adult a year ($)')]
SHARES = {5: ('paS5', 'year 5'), 10: ('paS10', 'year 10'), 19: ('paS19', 'year 20'), 39: ('paS39', 'year 40')}
FUND = [('A.main', 'main reading'), ('A.pace0.5', 'half the pace'), ('A.pace2', 'double the pace'), ('A.nolimit', 'no pace limit'),
        ('A.lent', "the pace limits the fund's additions only"), ('A.mature', "mature firms' failure rate"), ('A.haznone', 'no failures'),
        ('A.grant0', 'all loans'), ('A.grant1', 'all grants')]
CHART = [('B.ch1of7', 'charters at 1/7 (public power today)'), ('B.ch1of3', 'charters at 1/3'), ('B.ch2of3', 'charters at 2/3')]
BOTH = ('C.main.ch1of7', 'the fund and charters at 1/7')
CPP = 'cost per point of basket poverty removed ($ per adult a year)'


def r(x, k=1.0):
    return None if x is None else round(x * k, 6)


def write(name, meta, cols, rows):
    obj = {'meta': dict(meta, id=name, n=len(rows)), 'columns': cols, 'data': [list(c) for c in zip(*rows)]}
    p = os.path.join(ROOT, 'data', 'studies', name + '.json')
    with open(p, 'w') as fh:
        json.dump(obj, fh, ensure_ascii=False, separators=(',', ':'))
    print('wrote %s: %d rows' % (os.path.relpath(p, ROOT), len(rows)))


def block(o, rowid, with_share, years):
    """the outcome rows of one reading in one cell: (outcome, est, lo, hi, category)"""
    c, out = o['contrast'][rowid], []
    for k, lab in PRIM:
        out.append((lab, c[k]['est'], c[k]['lo'], c[k]['hi'], c[k]['cat']))
    for k, lab in SEC:
        if k in c:
            out.append((lab, c[k]['est'], c[k]['lo'], c[k]['hi'], None))
        elif k in o['levels'][rowid] and k not in o['levels']['M.main']:  # the main row has no such account, so its level is the change
            lv = o['levels'][rowid][k]
            out.append((lab, lv['est'], lv['lo'], lv['hi'], None))
    if with_share:
        for t, (k, lab) in SHARES.items():
            if (t == 39) == (years == 40) or t in (5, 10):
                if k in c:
                    out.append(('community businesses\' share of essential sales, ' + lab + ' (points)', c[k]['est'], c[k]['lo'], c[k]['hi'], None))
    if rowid in o['q2']:
        q = o['q2'][rowid]
        out.append((CPP, q['est'], q['lo'], q['hi'], None))
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: s94_page_data.py <path to s94-summary.json>')
    S = json.load(open(sys.argv[1]))['results']
    global FOLDER
    FOLDER = os.path.basename(os.path.dirname(os.path.abspath(sys.argv[1])))  # S93 part 4: the tables folder (its name ends in the engine commit)
    F, Ch, I, L = [], [], [], []
    for e, en in ENVS:
        for yrs in (20, 40):
            for d, dn in DES:
                o = S['%s-%d-%s' % (e, yrs, d)]
                for rid, rn in FUND:
                    for out in block(o, rid, True, yrs):
                        F.append([en, yrs, dn, rn] + [r(x) if isinstance(x, float) else x for x in out])
                for rid, rn in CHART + [BOTH]:
                    for out in block(o, rid, False, yrs):
                        Ch.append([en, yrs, dn, rn] + [r(x) if isinstance(x, float) else x for x in out])
                q5 = o['q5']
                for k, lab in PRIM + [COST]:
                    x = q5[k]
                    I.append([en, yrs, dn, lab, r(x['est']), r(x['lo']), r(x['hi']), not x['zero']])
                for rid, rn in (('M.main', 'the main row, no fund'), ('A.main', 'the fund, main reading')):
                    lv = o['levels'][rid]
                    for t, (k, lab) in SHARES.items():
                        if (t == 39) == (yrs == 40) or t in (5, 10):
                            L.append([en, yrs, dn, rn, "community businesses' share of essential sales, " + lab + ' (%)', r(lv[k]['est']), r(lv[k]['lo']), r(lv[k]['hi'])])
                    L.append([en, yrs, dn, rn, 'adult-years where capital limited the share (%)', r(lv['paCap']['est']), r(lv['paCap']['lo']), r(lv['paCap']['hi'])])
                for k, lab in PRIM:
                    x = o['effect']['M.main'][k]
                    L.append([en, yrs, dn, 'the main row against no programme', lab, r(x['est']), r(x['lo']), r(x['hi'])])
    base = {'prereg': 'prereg/2026-11-s94-collectives-lending.md (research-update; Amendments 1-2)', 'report': 'dev/reports/s94-collectives-lending.md',
            'engine': FOLDER.rsplit('-', 1)[1], 'seeds': 500, 'resultsFolder': FOLDER, 'resultsRepo': 'BetterToBest/compassionism-sim-results',
            'command': 'python3 dev/tools/s94_page_data.py %s/s94-summary.json' % FOLDER,
            'intervals': "95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model's randomness only"}
    cols = ['environment', 'years', 'design', 'reading', 'outcome', 'change', 'lo95', 'hi95', 'category']
    write('s94-fund', dict(base, title="The Creative Collectives' fund for community businesses: every reading, each environment, horizon and design",
                           terms='change: the reading minus the main row of the same design, paired by seed (shares and poverty in points, wealth and costs in year-0 dollars); '
                                 'category after Holm over the six readings of a row; the cost per point is the added cost over the fall in basket poverty'), cols, F)
    write('s94-charters', dict(base, title='Charters of public utilities (no fund), and the fund with charters at 1/7',
                               terms='change: the reading minus the main row of the same design, paired by seed; 1/7 is the share public power serves today (APPA), 1/3 and 2/3 are design parameters'),
          cols, Ch)
    write('s94-interaction', dict(base, title='The interaction of the fund and charters at 1/7 (joint change minus the sum of the two alone)'),
          ['environment', 'years', 'design', 'outcome', 'interaction', 'lo95', 'hi95', 'interval excludes zero'], I)
    write('s94-levels', dict(base, title="Community businesses' share of essential sales with and without the fund, and the main row's effect against no programme"),
          ['environment', 'years', 'design', 'row', 'outcome', 'value', 'lo95', 'hi95'], L)


if __name__ == '__main__':
    main()
