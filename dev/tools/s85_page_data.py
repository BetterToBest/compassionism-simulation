#!/usr/bin/env python3
"""S85 part 5 (Nov 20, 2026): the findings page's data for the automation study (data/studies/s85-automation.json, s85-backing.json and
s85-free-time.json), from the tables tool's summary.

  python3 dev/tools/s85_page_data.py <compassionism-sim-results>/s85-tables2-503fa48/s85-summary.json

Research-update prereg/2026-11-s85-output-per-hour.md (Amendments 1-4). The page (site/round2.js) prints every figure from these files; no figure is
typed there. Copied as the tables tool computed them (mean over paired seeds 1-500; 95% paired-bootstrap intervals, 10,000 replicates; categories
after Holm over the 48 tests of each environment, horizon and design). Shares and costs are scaled for printing only (fractions to percent).

- s85-automation.json: the headline block (displacement in both runs, full backing): for each environment, horizon, design, form and displacement
  level, the six readings' cost with no programme and with it (positive is harm), the offset share with its interval, and the category.
- s85-backing.json: every row of the produced-backing block (nothing assumed backed; displacement as lost jobs): the produced share of the payout
  over the run and programme inflation, each with its interval, and the category against 5 points a year.
- s85-free-time.json: hours a year no longer paid per adult in paid work at the start, mean over the run, split secure and insecure, for the
  no-programme run and each design. Standard library only."""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')]
DES = [('c22', 'full coverage'), ('rel', 'opt-in')]
FORMS = [('jobs', 'lost jobs'), ('hours', 'shorter hours')]
DS = ['0.1', '0.3', '0.5', '0.7']
OUTS = [('fgt0PY', 'basket poverty (points)'), ('ppovA', 'wealth poverty, yearly average (points)'), ('pov', 'wealth poverty, last year (points)'),
        ('wtMedE', 'median real wealth, weighted (year-0 $)'), ('medWealthReal', 'median real wealth, unweighted (year-0 $)'),
        ('secM3A', 'savings under three months of need (points)')]
VARIANTS = {'floor': 'nothing produced (the floor)', 'growth': 'stricter accounting', 'conv': "participants' own conversions",
            'gain': 'the high gain on programme output', 'convgain': 'conversions and the high gain', 'vk': 'the fuller valuation of capital'}


def r(x, k=1.0):
    return None if x is None else round(x * k, 6)


def write(name, meta, cols, rows):
    obj = {'meta': dict(meta, id=name, n=len(rows)), 'columns': cols, 'data': [list(c) for c in zip(*rows)]}
    p = os.path.join(ROOT, 'data', 'studies', name + '.json')
    with open(p, 'w') as fh:
        json.dump(obj, fh, ensure_ascii=False, separators=(',', ':'))
    print('wrote %s: %d rows' % (os.path.relpath(p, ROOT), len(rows)))


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: s85_page_data.py <path to s85-summary.json>')
    S = json.load(open(sys.argv[1]))['results']
    A, B, T = [], [], []
    for e, en in ENVS:
        for yrs in (20, 40):
            R = S['%s-%d' % (e, yrs)]
            assert R['sec'], 'the savings supplement was not read in ' + e
            for d, dn in DES:
                for f, fn in FORMS:
                    for D in DS:
                        c = R['A'][d]['cells'][D + '.' + f]
                        for k, lab in OUTS:
                            x = c[k]
                            A.append([en, yrs, dn, fn, float(D) * 100, lab, r(x['cN']['est']), r(x['cN']['lo']), r(x['cN']['hi']),
                                      r(x['cP']['est']), r(x['cP']['lo']), r(x['cP']['hi']),
                                      r(x['share']['est'], 100), r(x['share']['lo'], 100), r(x['share']['hi'], 100), x['cat']])
                        q = R['Q6'][d]['A.%s.%s.D%s' % (d, f, D)]
                        if d == 'c22':  # the no-programme run is the same for both designs
                            T.append([en, yrs, 'no programme', fn, float(D) * 100, r(q['ohFree']['N']['est']), r(q['ohFreeS']['N']['est']),
                                      r(q['ohFreeI']['N']['est']), r(100 * q['ohFreeI']['N']['est'] / q['ohFree']['N']['est'])])
                        T.append([en, yrs, dn, fn, float(D) * 100, r(q['ohFree']['P']['est']), r(q['ohFreeS']['P']['est']),
                                  r(q['ohFreeI']['P']['est']), r(100 * q['ohFreeI']['P']['est'] / q['ohFree']['P']['est'])])
                for nm, x in sorted(R['Q4'][d]['rows'].items()):
                    p = nm.split('.')  # E.<des>.[variant.]m<m>.g<gain>.D<D>  or  E.<des>.floor.D<D>
                    var = p[2] if not p[2].startswith('m') else 'main'
                    m = next((float(s[1:]) for s in p if s.startswith('m') and s[1:2].isdigit()), None)
                    g = next((s[1:] for s in p if s in ('glow', 'ghigh')), None)
                    Dv = float(nm.split('.D')[-1]) * 100
                    B.append([en, yrs, dn, 'main reading' if var == 'main' else VARIANTS[var], m, g, Dv,
                              r(x['A']['est']), r(x['A']['lo']), r(x['A']['hi']), r(x['infl']['est']), r(x['infl']['lo']), r(x['infl']['hi']), x['cat']])
    base = {'prereg': 'prereg/2026-11-s85-output-per-hour.md (research-update; Amendments 1-4)', 'report': 'dev/reports/s85-output-per-hour.md',
            'engine': '503fa48', 'seeds': 500, 'resultsFolder': 's85-tables2-503fa48', 'resultsRepo': 'BetterToBest/compassionism-sim-results',
            'command': 'python3 dev/tools/s85_page_data.py s85-tables2-503fa48/s85-summary.json',
            'intervals': '95% paired-bootstrap intervals over seeds 1-500 (10,000 replicates); the model\'s randomness only'}
    write('s85-automation', dict(base, title='Automation in both runs (displacement of 10-70% of paid work by year 20, as lost jobs or shorter hours), '
                                 'at full backing: displacement\'s cost with no programme and with it, and the share the programme takes away',
                                 terms='cost: a run at a displacement level minus the same run with none, positive is harm (for wealth, the fall); '
                                       'offset share: the cost with no programme minus the cost with the programme, over the cost with no programme; '
                                       'category after Holm over 48 tests per environment, horizon and design'),
          ['environment', 'years', 'design', 'form', 'displaced (%)', 'outcome', 'cost, no programme', 'lo95 none', 'hi95 none',
           'cost, with the programme', 'lo95 prog', 'hi95 prog', 'offset share (%)', 'lo95', 'hi95', 'category'], A)
    write('s85-backing', dict(base, title='The backing the programme\'s own work produces (nothing assumed backed; displacement as lost jobs): '
                              'produced share of the payout and programme inflation, every row of the block',
                              terms='m: the share of programme work whose output people or businesses would otherwise buy (a design parameter); '
                                    'gain: the automation forecast, low or high; category against 5 points a year of programme inflation'),
          ['environment', 'years', 'design', 'reading', 'm', 'gain', 'displaced (%)', 'produced share (%)', 'lo95', 'hi95',
           'programme inflation (points a year)', 'infl lo95', 'infl hi95', 'category'], B)
    write('s85-free-time', dict(base, title='Free time: hours a year no longer paid per adult in paid work at the start, mean over the run; secure when '
                                'the household is above its cost of living that year (programme runs at full backing)'),
          ['environment', 'years', 'run', 'form', 'displaced (%)', 'freed hours', 'secure hours', 'insecure hours', 'insecure share (%)'], T)


if __name__ == '__main__':
    main()
