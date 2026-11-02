#!/usr/bin/env python3
"""S52 (Nov 2, 2026): the analysis of the outside supply-shock study (study O), exactly as preregistered (research-update
prereg/2026-11-supply-shock-addendum.md, Analysis and Decision rules). Reads the shard files of a run-study folder (compassionism-sim-results
s52-shock-<engine>/) and writes the tables in Markdown.

  python3 dev/tools/s52_shock.py RESULTS_FOLDER [--out FILE] [--reps 2000]

R_g, the share of the shock reaching group g: [sxC(shocked) - sxC(off)] / [sxM(shocked) - sxM(off)], seed means of each difference, then the ratio,
against the same design's off row (programme rows) or off none row (none rows). Intervals: paired bootstrap over seeds (2,000 replicates, resampler
seed 52, the same resample for every row). Standard library only."""
import json, os, sys, glob, random, math

ENVS = ['ref', 'adv', 'st']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
DES = ['rel', 'c22']; DESL = {'rel': 'release row (released wages)', 'c22': 'C2.2 design (CPS yardstick)'}
GRPS = [('A', 'all adults'), ('F', 'PTF members'), ('H', 'PTH members (not PTF)'), ('P', 'other CCO participants'), ('N', 'in none of the three'),
        ('X', 'chose not to take part')]
PATHS = ['main', 'e246', 'e373', 'e655', 'k51', 'k100']
PATHL = {'main': 'main shock (rise 32.8%, 88% kept)', 'e246': 'rise 24.6%', 'e373': 'rise 37.3%', 'e655': 'rise 65.5% (beyond history)',
         'k51': '51% kept', 'k100': 'all kept'}
MAIN = 'm25.s0.k50.p1'; NOPTF = 'm0.s0.k50.p1'


def load(folder):
    files = sorted(f for f in glob.glob(os.path.join(folder, 'shard-*.json')) if not f.endswith('.timing.json'))
    if not files: sys.exit('no shard files in ' + folder)
    D = [json.load(open(f)) for f in files]
    D.sort(key=lambda d: d['_meta']['seeds'][0])
    rows = {}
    for d in D:
        for r, v in d['rows'].items():
            t = rows.setdefault(r, {})
            for k, x in v.items(): t.setdefault(k, []).extend(x)
    return rows, D[0]['_meta']


def pct(v, q):
    if not v: return float('nan')
    v = sorted(v); i = q*(len(v) - 1); lo = int(math.floor(i)); hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo])*(i - lo)


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    folder = a[0]; out = a[a.index('--out') + 1] if '--out' in a else None; reps = int(a[a.index('--reps') + 1]) if '--reps' in a else 2000
    rows, meta = load(folder)
    n = len(next(iter(rows.values()))['fgt0PY'])
    rnd = random.Random(52); BS = [[rnd.randrange(n) for _ in range(n)] for _ in range(reps)]
    envs = [e for e in ENVS if any(r.startswith(e + '.') for r in rows)]
    L = []; w = L.append

    def ratio(S, Z, g, win, idx):
        num = sum(S['sxC' + win + g][i] - Z['sxC' + win + g][i] for i in idx); den = sum(S['sxM' + win + g][i] - Z['sxM' + win + g][i] for i in idx)
        return num/den if den else float('nan')

    def R(S, Z, g, win='D'):
        v = ratio(S, Z, g, win, range(n)); bs = [ratio(S, Z, g, win, b) for b in BS]; bs = [x for x in bs if x == x]
        return v, (pct(bs, 0.025), pct(bs, 0.975)) if bs else (float('nan'), float('nan'))

    def Rdiff(S1, S2, Z, g1, g2, win='D'):  # R(S1, g1) - R(S2, g2), paired
        f = lambda idx: ratio(S1, Z, g1, win, idx) - ratio(S2, Z, g2, win, idx)
        v = f(range(n)); bs = [f(b) for b in BS]; bs = [x for x in bs if x == x]
        return v, (pct(bs, 0.025), pct(bs, 0.975))

    def D(S, Z, k):  # mean paired difference shocked - off, with interval
        f = lambda idx: sum(S[k][i] - Z[k][i] for i in idx)/len(idx)
        v = f(range(n)); bs = [f(b) for b in BS]
        return v, (pct(bs, 0.025), pct(bs, 0.975))

    def DD(S, Z, S0, Z0, k):  # (S - Z) - (S0 - Z0)
        f = lambda idx: sum((S[k][i] - Z[k][i]) - (S0[k][i] - Z0[k][i]) for i in idx)/len(idx)
        v = f(range(n)); bs = [f(b) for b in BS]
        return v, (pct(bs, 0.025), pct(bs, 0.975))

    P = lambda x: '%.1f%%' % (x*100)
    I = lambda c: '(%.1f to %.1f)' % (c[0]*100, c[1]*100)
    Pp = lambda x, c: '%+.2f (%+.2f to %+.2f)' % (x, c[0], c[1])
    w('# Study O (S52): the outside supply shock, every preregistered table')
    w('')
    w('PILOT: seeds 1-%d, labelled pilot throughout; not figures of the model. Engine %s. Analysis: `dev/tools/s52_shock.py` (prereg/2026-11-supply-shock-addendum.md).' % (n, meta['manifest'].get('commit', '?')[:7]))
    w('')
    w('Share of the shock reaching a group: the rise in its own money costs over the rise in the same basket at market prices, against the same run without the shock (same seed). 1 = the whole rise; 0 = none of it. 95% intervals: paired bootstrap over seeds.')
    for e in envs:
        for d in DES:
            Zp = rows[e + '.' + d + '.off.prog']; Zn = rows[e + '.' + d + '.off.none']
            w(''); w('## %s, %s' % (ENVL[e], DESL[d])); w('')
            w('### Q14 (primary): share of the main shock reaching each group, during the shock (years 5-8), main reading (markup 25%, no local sourcing)')
            w(''); w('| Group | No programme | Programme | Programme, after the shock (years 9-19) |'); w('|---|---|---|---|')
            Sp = rows[e + '.' + d + '.main.' + MAIN]; Sn = rows[e + '.' + d + '.main.none']
            for g, gl in GRPS:
                c = []
                for (S, Z) in [(Sn, Zn), (Sp, Zp)]:
                    if sum(S['sxMD' + g]) == 0: c.append('no adults'); continue
                    v, ci = R(S, Z, g); c.append(P(v) + ' ' + I(ci))
                va, ca = R(Sp, Zp, g, 'A'); w('| %s | %s | %s | %s |' % (gl, c[0], c[1], P(va) + ' ' + I(ca)))
            w(''); w('### Q15: PTF members (F) by markup share and local sourcing, during the main shock (local supply half as exposed; no pooling)')
            w(''); w('| Markup share | no local sourcing | 25% local | 50% local | all local |'); w('|---|---|---|---|---|')
            for m in [0, 25, 50]:
                c = []
                for s in [0, 25, 50, 100]:
                    v, ci = R(rows['%s.%s.main.m%d.s%d.k50.p1' % (e, d, m, s)], Zp, 'F'); c.append(P(v) + ' ' + I(ci))
                w('| %d%% | %s |' % (m, ' | '.join(c)))
            w(''); w('Sensitivities (markup 25%): local supply fully protected (kap 0), and a three-year price reserve (pool 3).'); w('')
            w('| Row | PTF members | all adults |'); w('|---|---|---|')
            for r in ['m25.s25.k0.p1', 'm25.s50.k0.p1', 'm25.s100.k0.p1', 'm25.s0.k50.p3', 'm25.s50.k50.p3']:
                S = rows['%s.%s.main.%s' % (e, d, r)]; v, ci = R(S, Zp, 'F'); va, ca = R(S, Zp, 'A')
                w('| %s | %s | %s |' % (r, P(v) + ' ' + I(ci), P(va) + ' ' + I(ca)))
            w(''); w('### Protection by part of the design (Analysis; decision rules 1, 3)')
            w('')
            S0 = rows['%s.%s.main.%s' % (e, d, NOPTF)]
            v, ci = Rdiff(S0, Sp, Zp, 'F', 'F'); w('- PTF (markup removal, main reading): PTF members\' share without markup removal less with it: %s %s (rule 1: protects if the interval is above zero).' % (P(v), I(ci)))
            v, ci = Rdiff(Sp, Sp, Zp, 'N', 'P'); w('- BU: adults in none of the three less other CCO participants: %s %s.' % (P(v), I(ci)))
            if sum(Sp['sxMDH']) > 0:
                v, ci = Rdiff(Sp, Sp, Zp, 'P', 'H'); w('- PTH: other CCO participants less PTH members (not PTF): %s %s (rule 3: protects if the interval is above zero; the groups differ in who they are).' % (P(v), I(ci)))
            w(''); w('### Q16: basket poverty and volatility, main shock, main reading: shocked less unshocked (points), and for the programme against no programme')
            w(''); w('| Measure | No programme | Programme | Programme less no programme |'); w('|---|---|---|---|')
            for k, kl in [('sxPDA', 'basket poverty during the shock, all'), ('sxPAA', 'basket poverty after the shock, all'), ('sxPDX', 'basket poverty during, chose not to take part (no harm, rule 4)'),
                          ('sxPAX', 'basket poverty after, chose not to take part'), ('sxPDF', 'basket poverty during, PTF members'), ('fgt0PY', 'basket poverty over the run'),
                          ('pov', 'too little wealth at year 20'), ('sxVA', 'volatility of costs, all (points of yearly change)'), ('sxVX', 'volatility, chose not to take part'),
                          ('cBU', 'BU cost a person-year ($)'), ('endoAnn', 'programme inflation a year')]:
                if sum(Sp[k]) == 0 and sum(Sn[k]) == 0 and k.endswith('F'): continue
                a0, c0 = D(Sn, Zn, k); a1, c1 = D(Sp, Zp, k); a2, c2 = DD(Sp, Zp, Sn, Zn, k)
                w('| %s | %s | %s | %s |' % (kl, Pp(a0, c0), Pp(a1, c1), Pp(a2, c2)))
            w(''); w('### Other shock paths (programme rows: main reading and 50% local sourcing)')
            w(''); w('| Path | No programme, all adults | Programme, all | PTF members, main reading | PTF members, 50% local | basket poverty during, programme less no programme (points) |'); w('|---|---|---|---|---|---|')
            for q in PATHS:
                Sn2 = rows['%s.%s.%s.none' % (e, d, q)]; S1 = rows['%s.%s.%s.%s' % (e, d, q, MAIN)]; S2 = rows['%s.%s.%s.m25.s50.k50.p1' % (e, d, q)]
                c = [R(Sn2, Zn, 'A'), R(S1, Zp, 'A'), R(S1, Zp, 'F'), R(S2, Zp, 'F')]
                dd, cd = DD(S1, Zp, Sn2, Zn, 'sxPDA')
                w('| %s | %s | %s |' % (PATHL[q], ' | '.join(P(v) + ' ' + I(ci) for v, ci in c), Pp(dd, cd)))
    txt = '\n'.join(L) + '\n'
    if out: open(out, 'w').write(txt)
    else: sys.stdout.write(txt)


if __name__ == '__main__':
    main()
