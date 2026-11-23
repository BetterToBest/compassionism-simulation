"""S65 (Nov 15, 2026): write the data files of release 2 (round 2 of the engine) into data/studies/, copied from the S64 tables.

Usage: python3 dev/tools/r2_study_files.py            writes data/studies/r2-*.json
       python3 dev/tools/r2_study_files.py --check    exits 1 if any file is not what this script writes from dev/runs/s64-round2/ and dev/runs/s64-erosion/
       python3 dev/tools/r2_study_files.py --engine=50bc51d [--check]   the release's files (v5.9.23), from dev/runs/s93-round2/ and dev/runs/s93-erosion/

Nothing is recomputed. Every row is a value that dev/tools/s64_tables.py (summary file s64-summary.json) or dev/tools/s64_erosion.js (summary file) printed.
Files, in the same shape as study_files.py writes (meta, columns, data as one list per column; a missing value is null):
  r2-effects       the preregistered main effects (question 1): five outcomes, two designs, three environments, two horizons, with the erosion share of each wealth figure
  r2-curves        the specification curves (question 2): the 62 preregistered readings of each outcome, summarised (range, how many keep the sign, robust or fragile)
  r2-backing       the backing curve (question 4): the effects at each backed share, the mechanism's own point, the break-even share
  r2-financed      the financed rows (question 5): contribution rate, debt, and the effects when the programme is paid for by a contribution
  r2-distribution  who gains (question 6): shares, percentiles, debt, mobility, labour's share
  r2-work          work (question 7): employment, hours, participation, labour-force exits
  r2-charts/       the 24 chart files of dev/runs/s64-round2/charts/ (dev/tools/s64_charts.py), copied unchanged
The findings page (site/notes.js, round 2) prints these through site/findings.js; no number is typed into a page.
"""
import hashlib, json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUTDIR = os.path.join(ROOT, 'data', 'studies')
SUMMARY = os.path.join('dev', 'runs', 's64-round2', 's64-summary.json')
EROSION = os.path.join('dev', 'runs', 's64-erosion', 'summary.json')
ENGINE = '104691f'
PREREG = 'prereg/2026-11-s63-round2-freeze.md (research-update; registered on OSF, https://osf.io/msdzk/overview; Amendments 1-4)'
RESULTS = 'r2-<part>-<env>-<years>-104691f (parts m, s, f), r2-tables-104691f, r2-erosion-104691f'
CHARTS = os.path.join('dev', 'runs', 's64-round2', 'charts')
# S93 part 4 (Nov 23, 2026): --engine=50bc51d writes the release's files from the reruns on the release engine (v5.9.23), copied from
# compassionism-sim-results r2-tables-50bc51d (s64-summary.json, curves/) into dev/runs/s93-round2/ and r2-erosion-50bc51d/summary.json into
# dev/runs/s93-erosion/; the charts are dev/tools/s64_charts.py run on dev/runs/s93-round2. Without it, the published v5.9 files (unchanged).
REL = {'50bc51d': {'dir': 's93-round2', 'ero': 's93-erosion',
                   'prereg': PREREG + '; the release reruns: prereg/2026-11-s90-private-price-at-sale.md, Amendments 2-6',
                   'results': 'r2-<part>-<env>-<years>-50bc51d (parts m, s, f, b), r2-tables-50bc51d, r2-erosion-50bc51d'}}
_E = [a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--engine=')]
if _E:
    if _E[0] not in REL: sys.exit('r2_study_files.py: unknown --engine %s (known: %s)' % (_E[0], ', '.join(REL)))
    _R = REL[_E[0]]
    SUMMARY = os.path.join('dev', 'runs', _R['dir'], 's64-summary.json')
    EROSION = os.path.join('dev', 'runs', _R['ero'], 'summary.json')
    ENGINE, PREREG, RESULTS = _E[0], _R['prereg'], _R['results']
    CHARTS = os.path.join('dev', 'runs', _R['dir'], 'charts')
ENVN = {'ref': 'Reference', 'adv': 'Adverse', 'str': 'Stress', 'st': 'Stress'}
DESN = {'c22': 'C2.2', 'rel': 'release design'}
OUTN = {'bNAPy': 'basic living (adult-years below 30 days, points)', 'fgt0PY': 'cost of living (basket poverty, adult-years, points)',
        'ppovA': 'wealth poverty, yearly average (points)', 'wtMedE': 'median real wealth (year-0 $)', 'endoAnn': 'programme inflation (points a year)',
        'gvDebtY': 'government debt at the end (points of GDP)', 'gvY100': 'years until debt passes GDP'}


def sha(p):
    h = hashlib.sha256()
    with open(os.path.join(ROOT, p), 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def r(x, d=6):
    return None if x is None else round(x, d)


def meta(fid, title, report, rows, n, extra=None):
    m = {'id': fid, 'title': title, 'prereg': PREREG, 'report': report, 'engine': ENGINE, 'seeds': 500, 'rows': rows, 'resultsFolders': RESULTS,
         'resultsRepo': 'BetterToBest/compassionism-sim-results', 'source': {SUMMARY: sha(SUMMARY), EROSION: sha(EROSION)},
         'intervals': '95% bootstrap intervals over seeds 1-500 (the seed interval: the model\'s randomness only, not the choice of reading)', 'n': n}
    if extra:
        m.update(extra)
    return m


def table(cols, rows):
    return [[row[j] for row in rows] for j in range(len(cols))]


def build():
    S = json.load(open(os.path.join(ROOT, SUMMARY), encoding='utf-8'))
    E = json.load(open(os.path.join(ROOT, EROSION), encoding='utf-8'))
    out = {}

    # r2-effects
    cols = ['design', 'environment', 'years', 'outcome', 'no programme', 'programme', 'effect', 'lo95', 'hi95', 'material', 'Holm p', 'erosion share of the effect', 'erosion share lo95', 'erosion share hi95']
    rows = []
    for q in S['q1']:
        er = E['res'].get(q['env'], {}).get(q['design'], {}).get(str(q['years']), {}).get(q['key'], {}).get('share')
        rows.append([DESN[q['design']], ENVN[q['env']], q['years'], OUTN[q['key']], r(q['none']), r(q['prog']), r(q['s']['est']), r(q['s']['lo']), r(q['s']['hi']),
                     'yes' if q['material'] else 'no', r(q['holm'], 12), r(er['est']) if er else None, r(er['lo']) if er else None, r(er['hi']) if er else None])
    out['r2-effects'] = {'meta': meta('r2-effects', 'Round 2, the main effects (question 1): five outcomes, each design against no programme, main row',
                                      'dev/reports/s64-round2-q1-main-effects.md', 'main row (full backing, a design parameter), part M, three environments, 20 and 40 years', len(rows),
                                      {'thresholdNote': 'material = the interval excludes zero and the effect passes the preregistered threshold (1 point; the wealth threshold in the report)'}),
                         'columns': cols, 'data': table(cols, rows)}

    # r2-curves
    cols = ['design', 'environment', 'years', 'outcome', 'readings', 'readings keeping the sign', 'class', 'lowest reading', 'highest reading', 'main row', 'main lo95', 'main hi95', 'material']
    rows = []
    for k, c in sorted(S['curves'].items()):
        part, des, key, env, yrs = k.split('-')
        if part != 'S':
            continue
        rows.append([DESN[des], ENVN[env], int(yrs), OUTN.get(key, key), c['n'], c['same'], c['class'], r(c['min']), r(c['max']), r(c['main']['est']), r(c['main']['lo']), r(c['main']['hi']), 'yes' if c['material'] else 'no'])
    fin = []
    for k, c in sorted(S['curves'].items()):
        part, des, key, env, yrs = k.split('-')
        if part == 'F':
            fin.append([DESN[des], ENVN[env], int(yrs), OUTN.get(key, key), c['n'], c['same'], c['class'], r(c['min']), r(c['max']), r(c['main']['est']), r(c['main']['lo']), r(c['main']['hi']), 'yes' if c['material'] else 'no'])
    rows += [x[:3] + [x[3] + ' (paid for by a contribution)'] + x[4:] for x in fin]
    out['r2-curves'] = {'meta': meta('r2-curves', 'Round 2, how sure we are (question 2): every outcome across the preregistered readings',
                                     'dev/reports/s64-round2-q2-robustness.md', 'the preregistered readings of each outcome, source rows (part S) and financed rows (part F); a curve is robust when every reading keeps the sign with an interval excluding zero', len(rows)),
                        'columns': cols, 'data': table(cols, rows)}

    # r2-backing
    cols = ['design', 'environment', 'years', 'row', 'backed share (fraction of the payout)', 'outcome', 'effect', 'lo95', 'hi95']
    rows = []
    for k, b in sorted(S['backing'].items()):
        des, env, yrs = k.split('-')
        for g in b['grid']:
            for key, v in g['eff'].items():
                rows.append([DESN[des], ENVN[env], int(yrs), 'grid', g['a'], OUTN[key], r(v['est']), r(v['lo']), r(v['hi'])])
        for nm, m in b['mech'].items():
            lab = 'the model\'s own mechanism' + (', no ceiling' if nm.endswith('Nc') else '')
            for key, v in m['eff'].items():
                rows.append([DESN[des], ENVN[env], int(yrs), lab, r(m['bkA']['est'] / 100.0), OUTN[key], r(v['est']), r(v['lo']), r(v['hi'])])
        i5 = b['inflation5']
        rows.append([DESN[des], ENVN[env], int(yrs), 'break-even: inflation 5% a year', i5['est'] if isinstance(i5['est'], (int, float)) else None, 'backed share at which programme inflation is 5% a year', None, r(i5['lo']), r(i5['hi'])])
    out['r2-backing'] = {'meta': meta('r2-backing', 'Round 2, how much new output backs the payout (question 4): the backing curve, the mechanism\'s own point and the break-even share',
                                      'dev/reports/s64-round2-q4-backing.md', 'part S points on the backing curve (0, 0.25, 0.5, 0.75, 1), the mechanism\'s reading replayed with its backed share, 12 curves', len(rows),
                                      {'note': 'for the "grid" and mechanism rows the backed-share column is the share (the engine key bkA prints percent; divided by 100 here): the part of the payout matched by new output; for the break-even row, the estimate is the share and the interval its ends'}),
                         'columns': cols, 'data': table(cols, rows)}
    # break-even estimate sits in 'backed share'; the est column is empty by construction

    # r2-financed
    cols = ['design', 'environment', 'years', 'measure', 'estimate', 'lo95', 'hi95']
    rows = []
    FM = [('tauMean', 'mean contribution (% of the base)'), ('defShare', 'deficit share of the payout (%)'), ('debt', 'government debt at the end (% of GDP)'), ('y100', 'years until debt passes GDP')]
    for k, f in sorted(S['financed'].items()):
        des, env, yrs = k.split('-')
        for key, lab in FM:
            v = f[key]
            rows.append([DESN[des], ENVN[env], int(yrs), lab, r(v['est']), r(v['lo']), r(v['hi'])])
        for key, v in f['eff'].items():
            rows.append([DESN[des], ENVN[env], int(yrs), OUTN.get(key, key) + ', effect', r(v['est']), r(v['lo']), r(v['hi'])])
    out['r2-financed'] = {'meta': meta('r2-financed', 'Round 2, the programme paid for by a contribution instead (question 5): shown, never led with',
                                       'dev/reports/s64-round2-q5-financed.md', 'financed rows (part F), run without the weighted top tail', len(rows)),
                          'columns': cols, 'data': table(cols, rows)}

    # r2-distribution and r2-work
    for fid, key, q, title in (('r2-distribution', 'dist', 'q6-distribution', 'Round 2, who gains (question 6): wealth and income shares, percentiles, families in debt, mobility, labour\'s share'),
                               ('r2-work', 'work', 'q7-work', 'Round 2, work (question 7): employment, hours, participation, leaving the labour force')):
        cols = ['design', 'environment', 'years', 'measure', 'no programme', 'programme', 'effect', 'lo95', 'hi95', 'Holm p']
        rows = []
        for blk in S[key]:
            for c in blk['cells']:
                rows.append([DESN[blk['design']], ENVN[blk['env']], blk['years'], c['name'], r(c['none']), r(c['prog']), r(c['s']['est']), r(c['s']['lo']), r(c['s']['hi']), r(c.get('holm'), 12)])
        out[fid] = {'meta': meta(fid, title, 'dev/reports/s64-round2-%s.md' % q, 'main row, part M, three environments, 20 and 40 years', len(rows)),
                    'columns': cols, 'data': table(cols, rows)}
    return out


def text(d):
    return json.dumps(d, ensure_ascii=False, separators=(',', ':')) + '\n'


def main():
    check = '--check' in sys.argv
    bad = []
    for fid, d in build().items():
        p = os.path.join(OUTDIR, fid + '.json')
        want = text(d)
        if check:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != want:
                bad.append(fid)
        else:
            os.makedirs(OUTDIR, exist_ok=True)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(want)
            print('wrote', p, d['meta']['n'], 'rows')
    src = os.path.join(ROOT, CHARTS)
    dst = os.path.join(OUTDIR, 'r2-charts')
    for fn in sorted(x for x in os.listdir(src) if x.endswith('.svg')):
        a, b = open(os.path.join(src, fn), 'rb').read(), None
        if os.path.exists(os.path.join(dst, fn)):
            b = open(os.path.join(dst, fn), 'rb').read()
        if check:
            if a != b:
                bad.append('r2-charts/' + fn)
        else:
            os.makedirs(dst, exist_ok=True)
            open(os.path.join(dst, fn), 'wb').write(a)
    if bad:
        print('r2_study_files --check: not what the script writes:', ', '.join(bad))
        sys.exit(1)
    if check:
        print('r2_study_files --check: all files match')


if __name__ == '__main__':
    main()
