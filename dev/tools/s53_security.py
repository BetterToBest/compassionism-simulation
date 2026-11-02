#!/usr/bin/env python3
"""S53 (Nov 2, 2026): the analysis of the security-outcomes study (study P), exactly as preregistered (research-update
prereg/2026-11-security-addendum.md, Analysis and Decision rules). Reads the shard files of a run-study folder (compassionism-sim-results
s53-security-<engine>/), or one shard file, and writes the tables in Markdown. load() and diff() are also what later consumers (S54's
policy-lever analysis, S47's dry run) call to read the security keys from any job that records them.

  python3 dev/tools/s53_security.py RESULTS_FOLDER_OR_SHARD [--out FILE] [--reps 2000] [--check]

For each environment, design and path: the programme row minus its no-programme row, per measure and group, as seed means of the paired
differences. Intervals: paired bootstrap over seeds (2,000 replicates, resampler seed 53, the same resample for every cell). --check only
confirms every preregistered key and row is present and finite (the consumer check the plan asks for) and exits. Standard library only."""
import json, os, sys, glob, random, math

ENVS = ['ref', 'adv', 'st']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
GRPS = [('A', 'all adults'), ('P', 'took part'), ('X', 'chose not to take part')]
# (key stem, plain label, favourable direction: -1 lower is better, +1 higher is better, 0 accounting only), basis: E emergent, C by construction, M mixed
MEAS = [('U25', 'income drop of 25%+ with no buffer, per 100 adult-years', -1, 'E'),
        ('D25', 'income drop of 25%+ (any buffer), per 100', -1, 'E'),
        ('U50', 'income drop of 50%+ with no buffer, per 100', -1, 'E'),
        ('U25m', 'money-income drop of 25%+ with no buffer, per 100', -1, 'E'),
        ('M3', 'basics covered under 3 months without wages, %', -1, 'M'),
        ('M1', 'basics covered under 1 month without wages, %', -1, 'M'),
        ('M3w', 'under 3 months on all savings, %', -1, 'M'),
        ('Md', 'median months covered (cap 120)', 1, 'M'),
        ('Hr', 'median hours a week to cover the basics', -1, 'C'),
        ('H40', 'needing more than 40 hours a week, %', -1, 'C'),
        ('Hrc', 'median hours, conversion proceeds counted', -1, 'C'),
        ('Ds', 'displaced by price (proxy), per 100 adult-years', -1, 'E'),
        ('Px', 'PTH tenancies ended, per 100 member-years', 0, 'C'),
        ('Xb', 'essentials paid in money, % of the whole budget', -1, 'C'),
        ('Xe', 'essentials paid in money, % of essentials', -1, 'C')]
CONF = [('fgt0PY', 'basket poverty, % of adult-years'), ('pov', 'wealth poverty at year 20, %'), ('gNonF0', 'basket poverty of non-participants, %'),
        ('gNonW', 'wealth poverty of non-participants, %')]
DESIGNS = [('rel', 'off', '', 'release row, no outside shock'), ('c22', 'off', '', 'C2.2 design, no outside shock'),
           ('rel', 'main', '', 'release row, main supply shock'), ('c22', 'main', '', 'C2.2 design, main supply shock'),
           ('rel', 'off', '.sv', 'release row, savings that keep up with prices')]
S19_M = ['f0', 'f1', 'gD', 'gDc', 'dp', 'hd', 'ep', 'n', 'f0X']


def load(path):
    files = [path] if path.endswith('.json') else sorted(f for f in glob.glob(os.path.join(path, 'shard-*.json')) if not f.endswith('.timing.json'))
    if not files: sys.exit('no shard files in ' + path)
    D = [json.load(open(f)) for f in files]
    D.sort(key=lambda d: d['_meta']['seeds'][0])
    rows = {}
    for d in D:
        for r, v in d['rows'].items():
            t = rows.setdefault(r, {})
            for k, x in v.items(): t.setdefault(k, []).extend(x)
    return rows, D[0]['_meta']


def pct(v, q):
    v = sorted(v); i = q*(len(v) - 1); lo = int(math.floor(i)); hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo])*(i - lo)


def diff(a, b, idx):
    """Paired difference a - b: the seed mean and its bootstrap interval over the resamples idx."""
    d = [x - y for x, y in zip(a, b)]; n = len(d)
    m = sum(d)/n
    if n < 2: return m, float('nan'), float('nan')
    bs = [sum(d[i] for i in I)/n for I in idx]
    return m, pct(bs, 0.025), pct(bs, 0.975)


def check(rows, meta):
    keys = ['sec' + m + g for m, *_ in MEAS for g, _ in GRPS] + [k for k, _ in CONF] + ['s19%s_%d' % (m, t) for m in S19_M for t in range(meta.get('years', 20))]
    want = [e + '.' + d + '.' + p + '.' + r + sv for e in ENVS for d, p, sv, _ in DESIGNS for r in ('none', 'prog')]
    want = [w for w in want if w.split('.')[0] in {r.split('.')[0] for r in rows}]
    miss = [w for w in want if w not in rows]
    bad = [(w, k) for w in want if w in rows for k in keys if k not in rows[w] or not all(math.isfinite(x) for x in rows[w][k])]
    n = {len(v) for w in want if w in rows for v in rows[w].values()}
    ok = not miss and not bad and len(n) == 1
    print(('PASS' if ok else 'FAIL') + '  s53_security.py: %d rows, %d keys each, %s seeds%s%s' % (len(want) - len(miss), len(keys), '/'.join(map(str, sorted(n))),
          ('; missing rows: ' + ', '.join(miss[:5])) if miss else '', ('; missing or not finite: ' + ', '.join('%s %s' % x for x in bad[:5])) if bad else ''))
    return ok


def fmt(m, lo, hi, dp=2):
    return ('%+.' + str(dp) + 'f') % m + ('' if math.isnan(lo) else (' (%+.' + str(dp) + 'f, %+.' + str(dp) + 'f)') % (lo, hi))


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    reps = int(a[a.index('--reps') + 1]) if '--reps' in a else 2000
    rows, meta = load(a[0])
    if '--check' in a: sys.exit(0 if check(rows, meta) else 1)
    nseed = len(next(iter(next(iter(rows.values())).values())))
    rng = random.Random(53); idx = [[rng.randrange(nseed) for _ in range(nseed)] for _ in range(reps)]
    L = ['# S53 security outcomes: tables (pilot, %d seeds; labelled pilot, not figures of the model)' % nseed, '',
         'Engine %s. Each cell: the design minus no programme on the same seeds, the seed mean and its 95%% paired bootstrap interval (%d replicates, seed 53). '
         'Basis: E emergent, M mixed, C by construction (accounting: a difference there is the design working as written, not evidence). '
         'Decision rule 1 credits a gain only where the interval excludes zero in the favourable direction on an E or M measure.' % (meta.get('manifest', {}).get('commit', '?')[:7], reps), '']
    for e in ENVS:
        for d, p, sv, lab in DESIGNS:
            pr, no = '%s.%s.%s.prog%s' % (e, d, p, sv), '%s.%s.%s.none%s' % (e, d, p, sv)
            if pr not in rows: continue
            L += ['## %s: %s' % (ENVL[e], lab), '', '| Measure | Basis | No programme (all) | ' + ' | '.join('Change: ' + gl for _, gl in GRPS) + ' |', '|---|---|---|' + '---|'*len(GRPS)]
            for k, lbl, sgn, bas in MEAS:
                base = sum(rows[no]['sec' + k + 'A'])/nseed
                cells = []
                for g, _ in GRPS:
                    m, lo, hi = diff(rows[pr]['sec' + k + g], rows[no]['sec' + k + g], idx)
                    flag = ' **better**' if sgn and bas != 'C' and not math.isnan(lo) and ((sgn < 0 and hi < 0) or (sgn > 0 and lo > 0)) else ' **worse**' if sgn and not math.isnan(lo) and ((sgn < 0 and lo > 0) or (sgn > 0 and hi < 0)) else ''
                    cells.append(fmt(m, lo, hi) + flag)
                L.append('| %s | %s | %.2f | %s |' % (lbl, bas, base, ' | '.join(cells)))
            for k, lbl in CONF:
                m, lo, hi = diff(rows[pr][k], rows[no][k], idx)
                L.append('| %s (guardrail 6) | E | %.2f | %s |' % (lbl, sum(rows[no][k])/nseed, fmt(m, lo, hi) + ' | |'))
            L.append('')
    # Q19 and decision rule 3: (design minus no programme, with savings that keep up with prices) minus (the same without them), release row, no shock;
    # then, descriptively, the same difference for the main supply shock against no shock (both designs). Paired over seeds, the same resample.
    DID = [('Savings that keep up with prices against plain savings (release row, no outside shock; Q19, decision rule 3)',
            lambda e: ('%s.rel.off.prog.sv' % e, '%s.rel.off.none.sv' % e, '%s.rel.off.prog' % e, '%s.rel.off.none' % e))] + \
          [('Main supply shock against no shock (%s; descriptive: how much the change moves under the shock)' % ('release row' if d == 'rel' else 'C2.2 design'),
            (lambda d: lambda e: ('%s.%s.main.prog' % (e, d), '%s.%s.main.none' % (e, d), '%s.%s.off.prog' % (e, d), '%s.%s.off.none' % (e, d)))(d)) for d in ('rel', 'c22')]
    for title, rw in DID:
        L += ['## Difference in differences: ' + title, '',
              'Each cell: the change with the programme in the first reading minus the change in the second, on the same seeds, with its 95% paired bootstrap interval; '
              'an interval that excludes zero means the reading moves the result.', '',
              '| Environment | Measure | Basis | ' + ' | '.join(gl for _, gl in GRPS) + ' |', '|---|---|---|' + '---|'*len(GRPS)]
        for e in ENVS:
            a1, b1, a0, b0 = rw(e)
            if not all(x in rows for x in (a1, b1, a0, b0)): continue
            for k, lbl, sgn, bas in MEAS:
                if bas == 'C' and k not in ('Hr', 'Xb'): continue
                cells = []
                for g, _ in GRPS:
                    K = 'sec' + k + g
                    dd = [(p1 - n1) - (p0 - n0) for p1, n1, p0, n0 in zip(rows[a1][K], rows[b1][K], rows[a0][K], rows[b0][K])]
                    cells.append(fmt(*diff(dd, [0.0]*len(dd), idx)))
                L.append('| %s | %s | %s | %s |' % (ENVL[e], lbl, bas, ' | '.join(cells)))
            for k, lbl in CONF:
                dd = [(p1 - n1) - (p0 - n0) for p1, n1, p0, n0 in zip(rows[a1][k], rows[b1][k], rows[a0][k], rows[b0][k])]
                L.append('| %s | %s | E | %s | | |' % (ENVL[e], lbl, fmt(*diff(dd, [0.0]*len(dd), idx))))
        L.append('')
    out = '\n'.join(L) + '\n'
    if '--out' in a: open(a[a.index('--out') + 1], 'w').write(out)
    else: sys.stdout.write(out)


if __name__ == '__main__':
    main()
