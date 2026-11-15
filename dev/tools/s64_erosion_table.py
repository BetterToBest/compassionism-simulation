#!/usr/bin/env python3
"""S64 part 3 (Nov 15, 2026; research-update prereg/2026-11-s63-round2-freeze.md, Amendment 4): the tables of the erosion trace.

  python3 dev/tools/s64_erosion_table.py [RAW_DIR] [--out=dev/runs/s64-erosion] [--summary=dev/runs/s64-round2/s64-summary.json]
                                          [--results=../compassionism-sim-results]

Reads dev/tools/s64_erosion.js's files (ero-<env>-40-<seeds>.json.gz; 40-year runs, read at year 20 and year 40) and writes tables.md and summary.json.
Every effect is the programme run minus the no-programme run, paired by seed, as the tables tool computes it; "without erosion" recomputes the programme
run's figure with each adult's real wealth less the erosion term (the adult's opening money claims fare as in the no-programme run). Part that is
erosion = published - without erosion; erosion share = its mean over the published effect's mean. 95% intervals: paired bootstrap over seeds, 2,000
resamples, numpy default_rng(6301), one resample for every row (the tables tool's). The bound column is the same share on S66's all-cash term.
Checks, before anything is printed: (1) seed by seed, the trace's no-programme, C2.2 and release runs equal the batch's part M (compassionism-sim-results
r2-m-<env>-40-104691f and -20-): wealth poverty and median wealth in every year (ppov_t, pmedW_t) and the weighted median at 40 years (wtMedE), and at
year 20 the 20-year run's wtMedE, to the trace's 7 significant digits; (2) with all 500 seeds, the published effects equal the batch's tables
(s64-summary.json, q1) to 1e-6 relative.
Standard library and numpy.
"""
import glob, gzip, json, os, sys
import numpy as np

RAW = next((a for a in sys.argv[1:] if not a.startswith('--')), 'dev/runs/s64-erosion/raw')
OUT = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--out=')), 'dev/runs/s64-erosion')
RES = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--results=')), '../compassionism-sim-results')
SUMM = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--summary=')), 'dev/runs/s64-round2/s64-summary.json')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('str', 'Stress')]
DES = [('c22', 'C2.2'), ('rel', 'release')]
STAT = [('in', 'in the labour force'), ('dis', 'out: disability'), ('ret', 'out: early retirement'), ('care', 'out: care'), ('sch', 'out: school')]
MINUS = '−'


def load(env):
    seeds, meta = {}, []
    for f in sorted(glob.glob(os.path.join(RAW, 'ero-%s-40-*.json.gz' % env))):
        d = json.loads(gzip.open(f).read())
        meta.append(d['_meta'])
        for s, v in d['seeds'].items():
            if s in seeds:
                raise SystemExit('seed %s twice' % s)
            seeds[s] = v
    return [seeds[k] for k in sorted(seeds, key=int)], meta


IDX = None


def boot_idx(n):
    global IDX
    if IDX is None or IDX.shape[1] != n:
        IDX = np.random.default_rng(6301).integers(0, n, size=(2000, n))
    return IDX


def ci(x):
    x = np.asarray(x, float)
    m = x[boot_idx(len(x))].mean(axis=1)
    return {'est': float(x.mean()), 'lo': float(np.percentile(m, 2.5)), 'hi': float(np.percentile(m, 97.5))}


def share(part, pub):
    part, pub = np.asarray(part, float), np.asarray(pub, float)
    I = boot_idx(len(part))
    r = part[I].mean(axis=1) / pub[I].mean(axis=1) * 100
    return {'est': float(part.mean() / pub.mean() * 100), 'lo': float(np.percentile(r, 2.5)), 'hi': float(np.percentile(r, 97.5))}


def fm(c, d=2, unit=''):
    f = lambda v: (MINUS if v < 0 else '') + ('{:,.%df}' % d).format(abs(v))
    return '%s%s (%s to %s)' % (f(c['est']), unit, f(c['lo']), f(c['hi']))


def fs(c):
    f = lambda v: (MINUS if round(v, 1) < 0 else '') + '%.1f' % abs(v)
    return '%s%% (%s to %s)' % (f(c['est']), f(c['lo']), f(c['hi']))


def measures(S, des, H):
    """per seed: published, without erosion, all-cash bound, for each wealth figure at horizon H (years)"""
    out = {}
    yrs = range(1, H)
    def arr(f):
        return np.array([f(s) for s in S], float)
    n = lambda s, k, t: s['none'][k][t]
    p = lambda s, k, t: s[des][k][t]
    out['ppovA'] = [arr(lambda s, k=k: np.mean([p(s, k, t) - n(s, 'pov', t) for t in yrs])) for k in ('pov', 'povN', 'povU')]
    out['ppov'] = [arr(lambda s, k=k: p(s, k, H - 1) - n(s, 'pov', H - 1)) for k in ('pov', 'povN', 'povU')]
    out['pmedWA'] = [arr(lambda s, k=k: np.mean([p(s, k, t) - n(s, 'med', t) for t in yrs])) for k in ('med', 'medN', 'medU')]
    out['pmedW'] = [arr(lambda s, k=k: p(s, k, H - 1) - n(s, 'med', H - 1)) for k in ('med', 'medN', 'medU')]
    y = 'y%d' % H
    out['wtMedE'] = [arr(lambda s, k=k: s[des][y][k] - s['none'][y]['wtMed']) for k in ('wtMed', 'wtMedN', 'wtMedU')]
    return out


LAB = [('ppovA', 'wealth poverty, yearly average (headline)', 'points', 2), ('ppov', 'wealth poverty at the year', 'points', 2),
       ('wtMedE', 'median real wealth, weighted, at the year (headline)', '$', 0), ('pmedWA', 'median real wealth, yearly average', '$', 0),
       ('pmedW', 'median real wealth at the year', '$', 0)]


def main():
    summ = json.load(open(SUMM))
    q1 = {(r['design'], r['env'], r['years'], r['key']): r for r in summ['q1']}
    qb = summ.get('q1beside', [])
    md, res, worst = [], {}, 0.0
    w = md.append
    data = {e: load(e) for e, _ in ENVS}
    # ---- check 1: seed by seed against the batch's part M
    bad, nchk = [], 0
    for e, _ in ENVS:
        S, _m = data[e]
        if not S:
            continue
        seeds = sorted(int(x) for m in _m for x in range(m['seeds'][0], m['seeds'][1] + 1))
        for yrs in (40, 20):
            rows = {}
            for f in sorted(glob.glob(os.path.join(RES, 'r2-m-%s-%d-104691f' % (e, yrs), 'shard-*.json.gz'))):
                d = json.loads(gzip.open(f).read())
                lo = d['_meta']['seeds'][0]
                for r in ('none', 'c22', 'rel'):
                    for k, v in d['rows']['%s.%s' % (e, r)].items():
                        if k.startswith(('ppov_', 'pmedW_')) or k == 'wtMedE':
                            rows.setdefault(r, {}).setdefault(k, {}).update({lo + i: x for i, x in enumerate(v)})
            if not rows:
                raise SystemExit('check 1: no part M files for %s %d years under %s' % (e, yrs, RES))
            for i, sd in enumerate(seeds):
                for r in ('none', 'c22', 'rel'):
                    T = S[i][r]
                    pairs = [(T['y%d' % yrs]['wtMed'], rows[r]['wtMedE'][sd])]
                    if yrs == 40:
                        pairs += [(T['pov'][t], rows[r]['ppov_%d' % t][sd]) for t in range(40)] + [(T['med'][t], rows[r]['pmedW_%d' % t][sd]) for t in range(40)]
                    for a, b in pairs:
                        nchk += 1
                        if abs(a - b) > 5e-7 * max(1.0, abs(b)):
                            bad.append((e, yrs, r, sd, a, b))
    if bad:
        raise SystemExit('check 1 failed: %d of %d values differ, e.g. %s' % (len(bad), nchk, bad[:3]))
    # ---- check 2: the published effects equal the batch's
    for e, _ in ENVS:
        S, _m = data[e]
        if not S:
            continue
        for d, _ in DES:
            for H in (20, 40):
                M = measures(S, d, H)
                for k in ('ppovA', 'wtMedE'):
                    ref = q1.get((d, e, H, k))
                    if ref:
                        got = float(M[k][0].mean())
                        worst = max(worst, abs(got - ref['s']['est']) / max(1.0, abs(ref['s']['est'])))
    full = all(len(data[e][0]) == 500 for e, _ in ENVS)
    if full and worst > 1e-6:
        raise SystemExit('check failed: published effects differ from the batch (largest relative difference %.2e)' % worst)
    nS = {e: len(data[e][0]) for e, _ in ENVS}
    w('# The erosion share of each round-2 wealth figure (S64 part 3)\n')
    w('Generated by `python3 dev/tools/s64_erosion_table.py` from `dev/tools/s64_erosion.js`\'s trace of the frozen main row (harness.js `r2FreezePair`, engine '
      '`104691f`; each row run alone as the batch\'s part M runs it), 40-year runs read at year 20 and year 40, seeds %s. Definitions: research-update '
      '`prereg/2026-11-s63-round2-freeze.md`, Amendment 4.\n' % ', '.join('%s 1-%d' % (n, nS[e]) for e, n in ENVS))
    w('**Checks.** Every traced run reproduced the engine\'s own wealth poverty and median wealth in every year, the weighted median and basket poverty exactly '
      '(the trace stops otherwise). Seed by seed, the three runs equal the batch\'s stored part M (%d values: wealth poverty and median wealth in every year, '
      'the weighted median at 20 and 40 years) to the trace\'s 7 significant digits. The published effects recomputed here equal the batch\'s tables: largest '
      'relative difference %.1e.\n' % (nchk, worst))
    w('**Reading the tables.** *Published*: the effect as the round-2 reports print it. *Without erosion*: the same effect with each adult\'s programme real '
      'wealth less the erosion term, so that the adult\'s opening money claims (deposits, bonds and the non-stock part of funds, less floating- and fixed-rate '
      'debt) fare as in the no-programme run. *Erosion share*: the part that is erosion over the published effect; positive means erosion is part of the '
      'published effect, negative means it works against it. *All-cash bound*: the same share on S66\'s term, which treats all opening wealth as cash; '
      'the frozen row holds wealth by asset class, so this overstates the erosion. Intervals: 95%, paired bootstrap over seeds.\n')
    for H in (20, 40):
        w('## %d years\n' % H)
        w('| Environment | Design | Figure | Published | Without erosion | Part that is erosion | Erosion share | All-cash bound |')
        w('|---|---|---|---|---|---|---|---|')
        for e, en in ENVS:
            S, _m = data[e]
            if not S:
                continue
            for d, dn in DES:
                M = measures(S, d, H)
                for k, kl, unit, dg in LAB:
                    pub, adj, ub = M[k]
                    c_pub, c_adj, c_part = ci(pub), ci(adj), ci(pub - adj)
                    sh, shu = share(pub - adj, pub), share(pub - ub, pub)
                    thr = q1.get((d, e, H, 'ppovA' if k.startswith('ppov') else 'wtMedE'), {}).get('thr')
                    mat = thr is None or abs(c_pub['est']) >= thr
                    u = '' if unit == 'points' else ''
                    res.setdefault(e, {}).setdefault(d, {}).setdefault(str(H), {})[k] = {'pub': c_pub, 'adj': c_adj, 'part': c_part, 'share': sh, 'shareCash': shu, 'material': mat}
                    w('| %s | %s | %s (%s) | %s | %s | %s | %s | %s |' % (en, dn, kl, unit, fm(c_pub, dg), fm(c_adj, dg), fm(c_part, dg if dg else 0),
                                                                        fs(sh) if mat else 'not material', fs(shu) if mat else ''))
        w('')
        w('Mean real wealth per adult present at year 0 in both runs (year-0 dollars): the gap (programme minus no programme), the erosion term, its share of '
          'the gap, the same computation on the opening real holdings (a check: they keep up with prices), and S66\'s all-cash term.\n')
        w('| Environment | Design | Adults | Real-wealth gap | Erosion term | Share of gap | Real holdings (check) | All-cash term |')
        w('|---|---|---|---|---|---|---|---|')
        for e, en in ENVS:
            S, _m = data[e]
            if not S:
                continue
            for d, dn in DES:
                y = 'y%d' % H
                g = np.array([s[d][y]['gap'] for s in S]); eN = np.array([s[d][y]['eN'] for s in S])
                eR = np.array([s[d][y]['eR'] for s in S]); eU = np.array([s[d][y]['eU'] for s in S]); nM = np.mean([s[d][y]['nM'] for s in S])
                res[e][d][str(H)]['gap'] = {'gap': ci(g), 'eN': ci(eN), 'eR': ci(eR), 'eU': ci(eU), 'share': share(eN, g), 'n': float(nM)}
                w('| %s | %s | %.0f | %s | %s | %s | %s | %s |' % (en, dn, nM, fm(ci(g), 0), fm(ci(eN), 0), fs(share(eN, g)), fm(ci(eR), 0), fm(ci(eU), 0)))
        w('')
        w('By fifth of opening net worth (lowest first): mean real-wealth gap / mean erosion term (year-0 dollars).\n')
        w('| Environment | Design | Fifth 1 | Fifth 2 | Fifth 3 | Fifth 4 | Fifth 5 |')
        w('|---|---|---|---|---|---|---|')
        for e, en in ENVS:
            S, _m = data[e]
            if not S:
                continue
            for d, dn in DES:
                y = 'y%d' % H
                F = np.array([s[d][y]['fifth'] for s in S], float)  # seeds x 5 x 3
                m = F.mean(axis=0)
                res[e][d][str(H)]['fifth'] = m.tolist()
                f = lambda v: (MINUS if v < 0 else '+') + '{:,.0f}'.format(abs(v))
                w('| %s | %s | %s |' % (en, dn, ' | '.join('%s / %s' % (f(a[0]), f(a[1])) for a in m)))
        w('')
        w('### Basket poverty by labour-force status (%d years)\n' % H)
        w('Adult-years whose income is below their basket, as a share of the adult-years in each status, years 0 to %d (the definition of `fgt0PY`; the '
          'statuses sum to it exactly). Status is the adult\'s in that year; under S73\'s flows adults move in and out. Effect: programme minus no programme, '
          'points, paired by seed. Descriptive: no rule applies.\n' % (H - 1))
        w('| Environment | Status | Share of adult-years (no programme) | No programme | C2.2 | Effect, C2.2 | Release | Effect, release |')
        w('|---|---|---|---|---|---|---|---|')
        for e, en in ENVS:
            S, _m = data[e]
            if not S:
                continue
            k = 'lr%d' % H
            tot = np.array([sum(c[0] for c in s['none'][k].values()) for s in S], float)
            for st, sl in STAT:
                rate = lambda r: np.array([100.0 * s[r][k][st][1] / s[r][k][st][0] if st in s[r][k] and s[r][k][st][0] else np.nan for s in S])
                rn, rc, rr = rate('none'), rate('c22'), rate('rel')
                ok = ~np.isnan(rn) & ~np.isnan(rc) & ~np.isnan(rr)
                if ok.sum() < 10:
                    continue
                shr = np.mean([s['none'][k][st][0] if st in s['none'][k] else 0 for s in S] / tot) * 100
                ec, er = ci((rc - rn)[ok]), ci((rr - rn)[ok])
                res[e].setdefault('lr', {}).setdefault(str(H), {})[st] = {'share': shr, 'none': float(np.mean(rn[ok])), 'c22': float(np.mean(rc[ok])), 'rel': float(np.mean(rr[ok])),
                                                                          'effC22': ec, 'effRel': er, 'seeds': int(ok.sum())}
                w('| %s | %s | %.1f%% | %.1f%% | %.1f%% | %s | %.1f%% | %s |' % (en, sl, shr, np.mean(rn[ok]), np.mean(rc[ok]), fm(ec, 1), np.mean(rr[ok]), fm(er, 1)))
        w('')
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'tables.md'), 'w').write('\n'.join(md) + '\n')
    json.dump({'check': worst, 'seeds': nS, 'res': res}, open(os.path.join(OUT, 'summary.json'), 'w'), indent=1)
    print('wrote', os.path.join(OUT, 'tables.md'), '(check: largest relative difference %.1e)' % worst)


if __name__ == '__main__':
    main()
