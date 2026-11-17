#!/usr/bin/env python3
"""Release 2's visual-suite series (S11 sub-step 4): data/releases/r2/ from job X2.

    python3 dev/tools/suite_r2.py RESULTS/x4-a60bd3e RESULTS/x2-5b62481   (S81) writes data/releases/r2/suite-20.json, suite-40.json and index.json from job X4,
                                                         after checking that every plain key equals job X2's (the folder named second)
    python3 dev/tools/suite_r2.py --study RESULTS/x3-ENGINE7   (S79) writes data/releases/r2/study-20.json and study-40.json and adds them to index.json
    python3 dev/tools/suite_r2.py --check                checks index.json against data/studies/r2-effects.json and the suite (and study) files

S81 (Nov 17, 2026; research-update prereg/2026-11-x4-weighted-addendum.md, job X4): the suite files now come from job X4, which re-ran release 2's main row at
engine commit a60bd3e (dev/tools/explore_export.js --suite also writes the weighted keys wmean*, wmed*, wtier*, wbO, wbN, wrelPov, wpart: every
adult counted at its population weight, a._w, the 18 top-tail adults at their small weights). Every plain key of X4 equals job X2's (run 125, engine
commit 5b62481, the first source of these files); this tool checks that again when given X2's folder as the second argument.

RESULTS/x4-a60bd3e is the results folder of job X4 in BetterToBest/compassionism-sim-results (run-study run 127: release 2's main row,
engine 104691f, re-run at engine commit a60bd3e with dev/tools/explore_export.js --r2 --suite, every engine key of every row and seed checked equal
to release 2's stored part M). Six shards, one per environment and horizon, 500 seeds each. Nothing is computed here but a re-arrangement:
the series are copied as the shards hold them; index.json adds release 2's published effects (data/studies/r2-effects.json, the file the
findings page reads) so the suite page can quote them beside the series. v5.6's files are not touched.

S79 (Nov 16, 2026; research-update prereg/2026-11-x3-measures-addendum.md, job X3): --study copies job X3's measures study and the BLEI paper's
other measures (EDC, FBS, IPBI's public costs avoided) for the same three rows into study-20.json and study-40.json, in release 1's study-file
layout (envs.ENV.series, envs.ENV.run) plus envs.ENV.measures. Again only a re-arrangement. --check then also checks them, including that each
row's share below the cost of living (person-years) equals release 2's published basket-poverty figure.
SUITE_R2_OUT=DIR writes to DIR instead, and SUITE_R2_TEST=1 accepts a test folder (other seeds or engine commit); both are for testing the tool.
"""
import gzip, hashlib, json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'data', 'releases', 'r2')
EFFECTS = os.path.join(ROOT, 'data', 'studies', 'r2-effects.json')
ENGINE = '104691f3993ac6f37d6ff1b8ccd4690120cfe949'
RERUN = 'a60bd3ecc54743427578ae2d8c81111137ca4133'  # S81: job X4's engine commit (compassionism-simulation PR 144's merge); X2's was 5b62481
X2_RERUN = '5b62481326f3b82cc714e20e4cd4ec3726357dd2'
X2_FOLDER = 'x2-5b62481'
FOLDER = 'x4-a60bd3e'
RUN = 'run-study run 127, Nov 17, 2026 (GitHub Actions)'
WKEYS = ['wmeanSav', 'wmeanInc', 'wmeanBu', 'wmedSav', 'wmedInc', 'wmedBu', 'wbO', 'wbN', 'wrelPov', 'wpart'] + \
    ['wmed_' + g for g in ('all', 'part', 'non')] + ['wtier%d_%s' % (i, g) for g in ('all', 'part', 'non') for i in range(6)]
STUDY_RERUN = '6d095a1eefe71abbb025b82e8942cd80cfe9a34a'  # S79: job X3's engine commit (compassionism-simulation PR 138's merge)
STUDY_FOLDER = 'x3-' + STUDY_RERUN[:7]
STUDY_RUN = 'run-study run 126, Nov 17, 2026 (GitHub Actions)'  # S79: the run-study workflow run that wrote it
TEST = os.environ.get('SUITE_R2_TEST') == '1'
OUT = os.environ.get('SUITE_R2_OUT') or OUT
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


# S79 correction (Nov 17, 2026): release 2's main rows carry the weighted top tail (S59, WEALTH_TAIL): 18 of the 500 adults stand for rare, very rich
# families and carry small weights. The plain per-adult wealth Gini is not valid with the tail on (index.html WT_KEYS; dev/DECISIONS.md S59 part 2);
# release 2 stored the weighted one per seed (wtGzE debts as zero, wtGnE debts kept; the end of the last year). It is copied here from release 2's own
# part M shards, with the paired difference against no programme and its 95% interval as harness.js tbDiff computes it.
PARTM_ENV = {'ref': 'ref', 'adv': 'adv', 'st': 'str'}
PARTM_ROW = {'base': 'none', 'c22': 'c22', 'release': 'rel'}
WGINI = {'gz': 'wtGzE', 'gn': 'wtGnE'}


def quantile(v, q):  # harness.js quantileOf: linear between order statistics
    v = sorted(v); h = (len(v) - 1)*q; lo, hi = math.floor(h), math.ceil(h)
    return v[lo] + (v[hi] - v[lo])*(h - lo)


def tbdiff(x, y):  # harness.js tbDiff: mean paired difference and 1.96 standard errors
    n = len(x); d = [a - b for a, b in zip(x, y)]; m = sum(d)/n
    v = sum((e - m)**2 for e in d)/(n - 1); h = 1.96*math.sqrt(v/n)
    return [round(m, 4), round(m - h, 4), round(m + h, 4)]


def weighted_gini(res, Y):
    out, files = {}, {}
    for e in ENVS:
        f = os.path.join(os.path.dirname(os.path.abspath(res)), 'r2-m-%s-%s-%s' % (PARTM_ENV[e], Y, ENGINE[:7]), 'shard-0000.json.gz')
        with gzip.open(f, 'rt') as g:
            d = json.load(g)
        R = d['rows']; files[e] = {'file': os.path.relpath(f, os.path.dirname(os.path.dirname(os.path.abspath(f)))), 'sha256': sha(f)}
        o = out[e] = {}
        for row in ROWS:
            x = R[PARTM_ENV[e] + '.' + PARTM_ROW[row]]
            if len(x['wtN']) != 500 or not all(n > 0 for n in x['wtN']):
                raise SystemExit('%s %s %s: not the tail rows (wtN)' % (Y, e, row))
            o[row] = {k: {'mean': round(sum(x[c])/len(x[c]), 4), 'p10': round(quantile(x[c], 0.1), 4), 'p90': round(quantile(x[c], 0.9), 4)} for k, c in WGINI.items()}
            if row != 'base':
                b = R[PARTM_ENV[e] + '.none']
                o[row]['d'] = {k: tbdiff(x[c], b[c]) for k, c in WGINI.items()}
    return out, files


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


def index(suite_sha, study_sha=None):
    eff, em = effects()
    X = {
        'about': 'Release 2’s visual-suite series (S11, S81): the main row of release 2 (engine 104691f), re-run at engine commit a60bd3e by job X4 and checked equal to release 2’s stored results, '
                 'value by value. Every plain key equals job X2’s (engine commit 5b62481, the first source of these files); the weighted keys (w…) count each simulated adult at its population weight. '
                 'Written by dev/tools/suite_r2.py from BetterToBest/compassionism-sim-results x4-a60bd3e; release 1’s suite files (v5.6/) are unchanged.',
        'release': '2', 'engine': ENGINE, 'rerunAt': RERUN, 'study': 'x4', 'seeds': 500, 'agents': 500, 'lifeSeed': 1,
        'results': {'repo': 'BetterToBest/compassionism-sim-results', 'folder': FOLDER, 'workflow': RUN},
        'prereg': 'prereg/2026-11-x4-weighted-addendum.md (BetterToBest/research-update)',
        'plainFrom': {'study': 'x2', 'rerunAt': X2_RERUN, 'folder': X2_FOLDER, 'workflow': 'run-study run 125, Nov 16, 2026 (GitHub Actions)', 'prereg': 'prereg/2026-11-x2-series-addendum.md (BetterToBest/research-update)',
                      'about': 'job X4 re-ran job X2’s series with the weighted keys added; every plain key of every row, year and environment equals job X2’s (checked by dev/tools/suite_r2.py and in the results folder’s run notes).'},
        'rows': {'base': 'No programme', 'c22': 'The C2.2 design', 'release': 'The release design'},
        'envs': ENV_TEXT,
        'suite': {'20': 'r2/suite-20.json', '40': 'r2/suite-40.json'},
        'suiteSha256': suite_sha,
        'effectsFrom': {'file': 'data/studies/r2-effects.json', 'engine': em['engine'], 'seeds': em['seeds'], 'intervals': em['intervals'], 'report': em['report']},
        'effects': eff}
    if study_sha:  # S79: job X3
        X['studyFiles'] = {'20': 'r2/study-20.json', '40': 'r2/study-40.json'}
        X['studySha256'] = study_sha
        X['studyFrom'] = {'study': 'x3', 'rerunAt': STUDY_RERUN, 'results': {'repo': 'BetterToBest/compassionism-sim-results', 'folder': STUDY_FOLDER, 'workflow': STUDY_RUN},
                          'prereg': 'prereg/2026-11-x3-measures-addendum.md (BetterToBest/research-update)',
                          'about': 'The measures study and the BLEI paper’s other measures (EDC, FBS, IPBI’s public costs avoided) for release 2’s main row, re-run by job X3 with two reporting '
                                   'switches (the measured EDC and the FBS50 tally) and checked equal to release 2’s stored results, every key, row and seed.'}
    return X


def study_shas():
    ps = [os.path.join(OUT, 'study-%s.json' % Y) for Y in ('20', '40')]
    return {Y: sha(p) for Y, p in zip(('20', '40'), ps)} if all(os.path.exists(p) for p in ps) else None


def plain_equal(res, res2):  # S81, prereg check 3: every plain key of job X4's shard equals job X2's (bands, deciles, lives and every suite key X2 wrote)
    def walk(a, b, path, bad):
        if isinstance(a, dict):
            for k in a:
                if k not in b:
                    bad.append(path + '/' + k)
                else:
                    walk(a[k], b[k], path + '/' + k, bad)
        elif isinstance(a, list):
            if len(a) != len(b):
                bad.append(path)
            else:
                for i, (x, y) in enumerate(zip(a, b)):
                    walk(x, y, '%s[%d]' % (path, i), bad)
        elif a != b:
            bad.append(path)
    for n in range(6):
        a = json.load(open(os.path.join(res2, 'shard-%04d.json' % n)))
        b = json.load(open(os.path.join(res, 'shard-%04d.json' % n)))
        bad = []
        for sec in ('bands', 'deciles', 'lives', 'suite'):
            walk(a[sec], b[sec], sec, bad)
        if bad or any(a['_meta'][k] != b['_meta'][k] for k in ('env', 'years', 'rows', 'seriesSeeds')):
            raise SystemExit('shard %d: job X4 differs from job X2 in %d plain values (first: %s)' % (n, len(bad), bad[:1]))
    print('every plain key of every row, year and environment equals job X2 (%s)' % X2_FOLDER)


def build(res, res2=None):
    if res2:
        plain_equal(res, res2)
    elif not TEST:
        raise SystemExit('give job X2’s folder as the second argument (prereg check 3)')
    by = {}
    for n in range(6):
        p = os.path.join(res, 'shard-%04d.json' % n)
        d = json.load(open(p))
        m = d['_meta']
        if (m['manifest']['commit'] != RERUN and not TEST) or m['manifest']['dirty'] or m['rows'] != ROWS or m['seriesSeeds'] != 500 or 'every engine key of every row equals release 2' not in m['selfCheck'] \
                or m['r2']['panelCheck']['engine'] != ENGINE or any(k not in d['suite'][r] for r in ROWS for k in WKEYS):
            raise SystemExit('shard %d is not job X4 as preregistered' % n)
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
                'results': {e: FOLDER + '/' + envs[e][3] for e in ENVS},
                'resultsSha256': {e: envs[e][2] for e in ENVS},
                'engine': ENGINE, 'rerunAt': RERUN, 'weighted': 'wmeanSav, wmeanInc, wmeanBu, wmedSav, wmedInc, wmedBu, wmed_*, wtier*, wbO, wbN, wrelPov, wpart: every simulated adult counted at its population weight (the top-tail adults of release 2 carry small weights); the keys without w count each adult once'}
        out = {'_meta': meta, 'envs': {e: envs[e][0]['suite'] for e in ENVS}}
        p = os.path.join(OUT, 'suite-%s.json' % Y)
        with open(p, 'w') as f:
            json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
        shas[Y] = sha(p)
    with open(os.path.join(OUT, 'index.json'), 'w') as f:
        json.dump(index(shas, study_shas()), f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote data/releases/r2/ (suite-20.json, suite-40.json, index.json)')


def build_study(res):  # S79: job X3
    by = {}
    for n in range(6):
        p = os.path.join(res, 'shard-%04d.json' % n)
        d = json.load(open(p))
        m = d['_meta']
        if (not TEST and (m['manifest']['commit'] != STUDY_RERUN or m['seriesSeeds'] != 500)) or m['manifest']['dirty'] and not TEST or m['rows'] != ROWS \
                or 'every engine key of every row equals release 2' not in m['selfCheck'] or m['r2']['panelCheck']['engine'] != ENGINE or 'measures' not in d or 'study' not in d:
            raise SystemExit('shard %d is not job X3 as preregistered' % n)
        by.setdefault(str(m['years']), {})[m['env']] = (d, m, sha(p), 'shard-%04d.json' % n)
    os.makedirs(OUT, exist_ok=True)
    for Y, envs in sorted(by.items()):
        if sorted(envs) != sorted(ENVS):
            raise SystemExit('%s years: environments %s' % (Y, sorted(envs)))
        m0 = envs['ref'][1]
        meta = {'seeds': m0['seriesSeeds'], 'rows': ROWS, 'years': int(Y), 'manifest': m0['manifest'],
                'what': 'the measures study and the BLEI paper’s other measures for release 2: for each row (and year), the mean over the runs and the 10th and 90th percentile across them',
                'study': m0['study'], 'measures': m0['measures'], 'r2': {k: m0['r2'][k] for k in ('rows', 'study', 'adults')},
                'added': m0['r2']['panelCheck'].get('added'), 'acct': {e: envs[e][1]['study']['acct'] for e in ENVS},
                'selfCheck': {e: envs[e][1]['selfCheck'] for e in ENVS},
                'commands': {e: envs[e][1]['command'] for e in ENVS},
                'jobCommands': {e: envs[e][1]['jobCommand'] for e in ENVS},
                'results': {e: STUDY_FOLDER + '/' + envs[e][3] for e in ENVS},
                'resultsSha256': {e: envs[e][2] for e in ENVS},
                'engine': ENGINE, 'rerunAt': m0['manifest']['commit']}
        wg, wf = weighted_gini(res, Y)
        meta['wgini'] = {'what': 'the weighted wealth Gini at the end of the last year (gz debts counted as zero, gn debts kept), from release 2’s own stored results; the plain per-adult Gini in series (giniW, giniWnet and their N forms) is not valid with the top tail on, and the page does not show it',
                         'from': wf}
        out = {'_meta': meta, 'envs': {e: {'series': envs[e][0]['study'], 'run': envs[e][0]['studyRun'], 'measures': envs[e][0]['measures'], 'wgini': wg[e]} for e in ENVS}}
        with open(os.path.join(OUT, 'study-%s.json' % Y), 'w') as f:
            json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
    shas = {Y: sha(os.path.join(OUT, 'suite-%s.json' % Y)) for Y in ('20', '40')}
    with open(os.path.join(OUT, 'index.json'), 'w') as f:
        json.dump(index(shas, study_shas()), f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote data/releases/r2/ (study-20.json, study-40.json; index.json)')


def check():
    bad = []
    have = json.load(open(os.path.join(OUT, 'index.json')))
    shas = {Y: sha(os.path.join(OUT, 'suite-%s.json' % Y)) for Y in ('20', '40')}
    ssh = study_shas()
    if have != index(shas, ssh):
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
                for k in WKEYS:
                    if k not in Z or len(Z[k]['mean']) != int(Y):
                        bad.append('%s %s %s: no weighted series %s' % (Y, e, row, k))
                if all(k in Z for k in WKEYS):
                    for t in range(int(Y)):
                        s = sum(Z['wtier%d_all' % k]['mean'][t] for k in range(6))
                        if abs(s - 100) > 0.01:
                            bad.append('%s %s %s year %d: weighted tiers add to %s' % (Y, e, row, t + 1, s))
                        if Z['wmeanSav']['mean'][t] > Z['meanSav']['mean'][t] + 1e-9:
                            bad.append('%s %s %s year %d: weighted average days from savings above the plain one' % (Y, e, row, t + 1))
                if row == 'base' and any(v is not None for v in Z['tier0_part']['mean']):
                    bad.append('%s %s: no programme has participants' % (Y, e))
                # the year-average of the same-rules share under 30 days is release 2's published basic-living figure (adult-years)
                avg = sum(Z['bN']['mean']) / int(Y)
                E = have['effects'][Y][e]['c22' if row == 'base' else row]['bl']
                pub = E['np'] if row == 'base' else E['p']
                if abs(avg - pub) > 0.005:
                    bad.append('%s %s %s: year-average under 30 days %.4f, published %.4f' % (Y, e, row, avg, pub))
    nS = 0
    if ssh:  # S79: job X3's files
        for Y in ('20', '40'):
            S = json.load(open(os.path.join(OUT, 'study-%s.json' % Y)))
            if S['_meta']['rerunAt'] != STUDY_RERUN and not TEST:
                bad.append('study-%s.json is not from job X3' % Y)
            for e in ENVS:
                for row in ROWS:
                    Z, M = S['envs'][e]['series'][row], S['envs'][e]['measures'][row]
                    if len(Z['sur_all']['mean']) != int(Y) or (row != 'base' and len(Z['eppm_all']['mean']) != int(Y)):
                        bad.append('%s %s %s: study series not one value a year' % (Y, e, row))
                    for k in ('edcM', 'fbsAbove', 'cost', 'fgt0PY'):
                        if k not in M:
                            bad.append('%s %s %s: no %s' % (Y, e, row, k))
                    if row == 'base' and (M['cost']['mean'] != 0 or M['fbsAbove']['mean'] != 0):
                        bad.append('%s %s: no programme has a cost or participant-years' % (Y, e))
                    W = S['envs'][e].get('wgini', {}).get(row)
                    if not W or not all(0 < W[k]['p10'] <= W[k]['mean'] <= W[k]['p90'] < 1 for k in WGINI) or (row != 'base' and not all(W['d'][k][1] <= W['d'][k][0] <= W['d'][k][2] for k in WGINI)):
                        bad.append('%s %s %s: no weighted wealth Gini' % (Y, e, row))
                    if row != 'base' and 'ipbi' not in M:
                        bad.append('%s %s %s: no public costs avoided' % (Y, e, row))
                    # each row's share below the cost of living (person-years) is release 2's published basket-poverty figure
                    E = have['effects'][Y][e]['c22' if row == 'base' else row]['bk']
                    pub = E['np'] if row == 'base' else E['p']
                    if abs(M['fgt0PY']['mean'] - pub) > 0.005:
                        bad.append('%s %s %s: below the cost of living %.4f, published %.4f' % (Y, e, row, M['fgt0PY']['mean'], pub))
                    nS += 1
    for b in bad:
        print('  ' + b)
    print('release 2 suite files: ' + ('%d problems' % len(bad) if bad else 'index matches r2-effects and the suite files; tiers add up; no participants without the programme; '
                                       'the year-average share under 30 days (same rules) equals release 2’s published basic-living figure for 3 rows, 3 environments and 2 horizons' +
                                       ('; study files: every measure present (with the weighted wealth Gini), and the share below the cost of living equals release 2’s published basket-poverty figure in all %d cells' % nS if ssh else '')))
    return not bad


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--study':
        build_study(sys.argv[2])
        sys.exit(0)
    if sys.argv[1:] == ['--check']:
        sys.exit(0 if check() else 1)
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    build(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)
