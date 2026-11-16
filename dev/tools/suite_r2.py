#!/usr/bin/env python3
"""Release 2's visual-suite series (S11 sub-step 4): data/releases/r2/ from job X2.

    python3 dev/tools/suite_r2.py RESULTS/x2-5b62481     writes data/releases/r2/suite-20.json, suite-40.json and index.json
    python3 dev/tools/suite_r2.py --check                checks index.json against data/studies/r2-effects.json and the suite files

RESULTS/x2-5b62481 is the results folder of job X2 in BetterToBest/compassionism-sim-results (run-study run 125: release 2's main row,
engine 104691f, re-run at engine commit 5b62481 with dev/tools/explore_export.js --r2, every engine key of every row and seed checked equal
to release 2's stored part M). Six shards, one per environment and horizon, 500 seeds each. Nothing is computed here but a re-arrangement:
the series are copied as the shards hold them; index.json adds release 2's published effects (data/studies/r2-effects.json, the file the
findings page reads) so the suite page can quote them beside the series. v5.6's files are not touched.
"""
import hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'data', 'releases', 'r2')
EFFECTS = os.path.join(ROOT, 'data', 'studies', 'r2-effects.json')
ENGINE = '104691f3993ac6f37d6ff1b8ccd4690120cfe949'
RERUN = '5b62481326f3b82cc714e20e4cd4ec3726357dd2'
ROWS = ['base', 'c22', 'release']
ENVS = ['ref', 'adv', 'st']
EFF_ENV = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
EFF_DES = {'c22': 'C2.2', 'release': 'release design'}
EFF_OUT = {'bl': 'basic living (adult-years below 30 days, points)', 'bk': 'cost of living (basket poverty, adult-years, points)',
           'wp': 'wealth poverty, yearly average (points)', 'mw': 'median real wealth (year-0 $)', 'inf': 'programme inflation (points a year)'}
EFF_COL = {'np': 'no programme', 'p': 'programme', 'effect': 'effect', 'lo95': 'lo95', 'hi95': 'hi95', 'material': 'material'}
ENV_TEXT = {  # the page's environment notes for release 2 (Reference and Adverse as release 1's; Stress as STRESS_TEST in index.html sets it)
    'ref': {'name': 'Reference', 'about': 'the model’s main settings, with no recessions and no outside inflation'},
    'adv': {'name': 'Adverse', 'about': 'recessions, 2% outside inflation and an automation wave'},
    'st': {'name': 'Stress Test', 'about': 'the Adverse environment with weaker programme settings (for the release design: 40% take part, a smaller allowance and smaller community programmes)'}}


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def effects():
    d = json.load(open(EFFECTS))
    C, D = d['columns'], d['data']
    col = lambda c: D[C.index(c)]
    out = {}
    for i in range(len(D[0])):
        env = [k for k, v in EFF_ENV.items() if v == col('environment')[i]]
        des = [k for k, v in EFF_DES.items() if v == col('design')[i]]
        oc = [k for k, v in EFF_OUT.items() if v == col('outcome')[i]]
        if not (env and des and oc):
            raise SystemExit('r2-effects row %d not understood' % i)
        out.setdefault(str(col('years')[i]), {}).setdefault(env[0], {}).setdefault(des[0], {})[oc[0]] = {k: col(c)[i] for k, c in EFF_COL.items()}
    return out, d['meta']


def index(suite_sha):
    eff, em = effects()
    return {
        'about': 'Release 2’s visual-suite series (S11): the main row of release 2 (engine 104691f), re-run at engine commit 5b62481 by job X2 and checked equal to release 2’s stored results, '
                 'value by value. Written by dev/tools/suite_r2.py from BetterToBest/compassionism-sim-results x2-5b62481; release 1’s suite files (v5.6/) are unchanged.',
        'release': '2', 'engine': ENGINE, 'rerunAt': RERUN, 'study': 'x2', 'seeds': 500, 'agents': 500, 'lifeSeed': 1,
        'results': {'repo': 'BetterToBest/compassionism-sim-results', 'folder': 'x2-5b62481', 'workflow': 'run-study run 125, Nov 16, 2026 (GitHub Actions)'},
        'prereg': 'prereg/2026-11-x2-series-addendum.md (BetterToBest/research-update)',
        'rows': {'base': 'No programme', 'c22': 'The C2.2 design', 'release': 'The release design'},
        'envs': ENV_TEXT,
        'suite': {'20': 'r2/suite-20.json', '40': 'r2/suite-40.json'},
        'suiteSha256': suite_sha,
        'effectsFrom': {'file': 'data/studies/r2-effects.json', 'engine': em['engine'], 'seeds': em['seeds'], 'intervals': em['intervals'], 'report': em['report']},
        'effects': eff}


def build(res):
    by = {}
    for n in range(6):
        p = os.path.join(res, 'shard-%04d.json' % n)
        d = json.load(open(p))
        m = d['_meta']
        if m['manifest']['commit'] != RERUN or m['manifest']['dirty'] or m['rows'] != ROWS or m['seriesSeeds'] != 500 or 'every engine key of every row equals release 2' not in m['selfCheck'] \
                or m['r2']['panelCheck']['engine'] != ENGINE:
            raise SystemExit('shard %d is not job X2 as preregistered' % n)
        by.setdefault(str(m['years']), {})[m['env']] = (d, m, sha(p), 'shard-%04d.json' % n)
    os.makedirs(OUT, exist_ok=True)
    shas = {}
    for Y, envs in sorted(by.items()):
        if sorted(envs) != sorted(ENVS):
            raise SystemExit('%s years: environments %s' % (Y, sorted(envs)))
        m0 = envs['ref'][1]
        meta = {'seeds': 500, 'rows': ROWS, 'years': int(Y), 'manifest': m0['manifest'], 'what': 'the visual suite for release 2: for each row and year, the mean over the runs and the 10th and 90th percentile across them',
                'suite': m0['suite'], 'r2': {k: m0['r2'][k] for k in ('rows', 'study', 'adults')},
                'selfCheck': {e: envs[e][1]['selfCheck'] for e in ENVS},
                'commands': {e: envs[e][1]['command'] for e in ENVS},
                'jobCommands': {e: envs[e][1]['jobCommand'] for e in ENVS},
                'results': {e: 'x2-5b62481/' + envs[e][3] for e in ENVS},
                'resultsSha256': {e: envs[e][2] for e in ENVS},
                'engine': ENGINE, 'rerunAt': RERUN}
        out = {'_meta': meta, 'envs': {e: envs[e][0]['suite'] for e in ENVS}}
        p = os.path.join(OUT, 'suite-%s.json' % Y)
        with open(p, 'w') as f:
            json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
        shas[Y] = sha(p)
    with open(os.path.join(OUT, 'index.json'), 'w') as f:
        json.dump(index(shas), f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote data/releases/r2/ (suite-20.json, suite-40.json, index.json)')


def check():
    bad = []
    have = json.load(open(os.path.join(OUT, 'index.json')))
    shas = {Y: sha(os.path.join(OUT, 'suite-%s.json' % Y)) for Y in ('20', '40')}
    if have != index(shas):
        bad.append('index.json is not what the generator writes from data/studies/r2-effects.json and the suite files')
    for Y in ('20', '40'):
        S = json.load(open(os.path.join(OUT, 'suite-%s.json' % Y)))
        for e in ENVS:
            for row in ROWS:
                Z = S['envs'][e][row]
                if len(Z['bN']['mean']) != int(Y):
                    bad.append('%s %s %s: not one value a year' % (Y, e, row))
                for t in range(int(Y)):
                    s = sum(Z['tier%d_all' % k]['mean'][t] for k in range(6))
                    if abs(s - 100) > 0.01:
                        bad.append('%s %s %s year %d: tiers add to %s' % (Y, e, row, t + 1, s))
                if row == 'base' and any(v is not None for v in Z['tier0_part']['mean']):
                    bad.append('%s %s: no programme has participants' % (Y, e))
                # the year-average of the same-rules share under 30 days is release 2's published basic-living figure (adult-years)
                avg = sum(Z['bN']['mean']) / int(Y)
                E = have['effects'][Y][e]['c22' if row == 'base' else row]['bl']
                pub = E['np'] if row == 'base' else E['p']
                if abs(avg - pub) > 0.005:
                    bad.append('%s %s %s: year-average under 30 days %.4f, published %.4f' % (Y, e, row, avg, pub))
    for b in bad:
        print('  ' + b)
    print('release 2 suite files: ' + ('%d problems' % len(bad) if bad else 'index matches r2-effects and the suite files; tiers add up; no participants without the programme; '
                                       'the year-average share under 30 days (same rules) equals release 2’s published basic-living figure for 3 rows, 3 environments and 2 horizons'))
    return not bad


if __name__ == '__main__':
    if sys.argv[1:] == ['--check']:
        sys.exit(0 if check() else 1)
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    build(sys.argv[1])
