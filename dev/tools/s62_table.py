#!/usr/bin/env python3
"""S62 (Nov 14, 2026; research-update prereg/2026-11-s62-ptf-realism.md): tables of the PTF realism pilot, from the files dev/tools/s62_ptf_ops.js writes.
Usage: python3 dev/tools/s62_table.py DIR [OUT.md]
  DIR holds s62-ptf-ops-ENV.json (or chunks s62-ptf-ops-ENV-1.json, -2.json, ...; merged first: same engine, seeds and rows, so merging changes no figure)
  for ENV = ref, adv, st. Default OUT dev/runs/s62-ptf-ops/tables.md; also writes summary.json beside OUT (means and paired effects, no per-seed values).
Analysis only. Intervals: the 2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds (fixed generator), unadjusted."""
import glob, json, os, sys
import numpy as np
ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]; D = ARGS[0]
OUT = ARGS[1] if len(ARGS) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runs', 's62-ptf-ops', 'tables.md')
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress')]; DES = [('rls', 'release'), ('c22', 'C2.2')]
READ = ['open', 'hub0', 'main', 'hubSt', 'price', 'sector', 'res0', 'members', 'step', 'w10', 'w40', 'tMem', 'tCap', 'hire5', 'hire2', 'bg03']
OUTC = [('fgt0PY', 'basket poverty (points of adult-years)'), ('wtPovE', 'wealth poverty, weighted, last year (points)'), ('hhCostPY', 'household basket poverty (points)'),
        ('pLev20', 'price level, year 20 (index points)'), ('cost', 'programme cost ($ per adult-year)'), ('wtT1E', 'top 1% wealth share, weighted, last year (points)')]
MECH = [('poSub', 'PTF subsidy $/adult-yr', 0), ('poSubSh', 'subsidy % of cost', 1), ('poFree', 'free part $/adult-yr', 0), ('poEpsF', 'food epsilon', 2), ('poCov', 'sales/cost %', 1),
        ('poWk', 'PTF jobs /100 adults', 2), ('poWkH', 'PTF % of workers\' hours', 2), ('poBon', 'mean bonus %', 2), ('poHire', 'hiring limit binds % yrs', 0), ('poG', 'PTF payroll raise %', 2),
        ('paSh', 'PTF share of sales % (mean)', 1), ('paS19', 'share yr 19 %', 1), ('cCut', 'price cuts counted $', 0), ('csFree', 'free part counted $', 0), ('cConv', 'conversion $', 0)]
def load(stem, e):
    f = os.path.join(D, '%s-%s.json' % (stem, e)); ch = sorted(glob.glob(os.path.join(D, '%s-%s-*.json' % (stem, e))), key=lambda p: int(p.rsplit('-', 1)[1][:-5]))
    if ch:
        parts = [json.load(open(p)) for p in ch]; m = dict(parts[0]['_meta']); m['rows'] = [r for q in parts for r in q['_meta']['rows']]; m['chunks'] = [q['_meta']['command'] for q in parts]
        m['seconds'] = sum(q['_meta']['seconds'] for q in parts); m['command'] = 'in chunks: see chunks'
        assert len({json.dumps(q['_meta']['manifest'], sort_keys=True) for q in parts}) == 1, 'chunks from different engines'
        rows = {}
        for q in parts: rows.update(q['rows'])
        return {'_meta': m, 'rows': rows}
    return json.load(open(f)) if os.path.exists(f) else None
R = {e: load('s62-ptf-ops', e) for e, _ in ENVS}; L = []; P = L.append
def boot(d):
    d = np.asarray(d, float); g = np.random.default_rng(20261114); b = d[g.integers(0, len(d), (2000, len(d)))].mean(1); return float(d.mean()), float(np.quantile(b, 0.025)), float(np.quantile(b, 0.975))
def has(e, r): return R[e] and r in R[e]['rows']
def eff(e, r, d, k):
    x = R[e]['rows'][r]['effect'][d].get(k) if has(e, r) else None; return (x['m'], x['lo'], x['hi']) if x else (float('nan'),) * 3
def dd(e, r, d, k, ref='open'):  # the reading's effect less ref's, paired by seed
    A = R[e]['rows'][r]['seeds']; B = R[e]['rows'][ref]['seeds']
    if k not in A[d] or k not in B[d]: return (float('nan'),) * 3
    a = np.asarray(A[d][k]) - np.asarray(A['none'][k]); b = np.asarray(B[d][k]) - np.asarray(B['none'][k]); return boot(a - b)
f1 = lambda t: '%.1f [%.1f, %.1f]' % t; f2 = lambda t: '%.2f [%.2f, %.2f]' % t; f0 = lambda t: '%.0f [%.0f, %.0f]' % t
fmt = lambda k: f0 if k in ('cost',) else f2
S = {'meta': {}, 'checks': {}, 'mech': {}, 'effects': {}, 'diff_open': {}, 'diff_main': {}, 'signs': {}}
P('# S62 pilot tables: PTF realism (running costs and who pays, PTF workers and wages, the density tests)\n')
P('Seeds 1-100, 500 adults, 20 years; the release row and the C2.2 design, each against its own no-programme run on the same seeds; S60\'s rows (S71\'s, adults outside the labour force, `bg` pass-through 0) with open access and growth (`pa: \'open\'`). A pilot is a mechanism check, not a result. Intervals: 2.5th-97.5th percentile of 2,000 paired bootstrap replicates over seeds, unadjusted.\n')
for e, en in ENVS:
    if R[e]: S['meta'][e] = {k: R[e]['_meta'].get(k) for k in ('seeds', 'years', 'seconds', 'command', 'chunks')}; S['meta'][e]['commit'] = R[e]['_meta']['manifest'].get('commit')
P('## 1. Check: `hub0` (the step-5 accounting, the bonus on members, the step, the tests on sales) must equal `open`\n')
P('| environment | series compared | series that differ |'); P('|---|---|---|')
for e, en in ENVS:
    if not (has(e, 'open') and has(e, 'hub0')): continue
    A, B = R[e]['rows']['open']['seeds'], R[e]['rows']['hub0']['seeds']; n = bad = 0; diff = []
    for d in ('none', 'rls', 'c22'):
        for k, v in A[d].items():
            if k.startswith('po') and k != 'pov': continue
            n += 1
            if v != B[d].get(k): bad += 1; diff.append(d + ' ' + k)
    S['checks'][e] = {'compared': n, 'differ': bad, 'which': diff[:10]}; P('| %s | %d | %d%s |' % (en, n, bad, (' (' + ', '.join(diff[:5]) + ')') if bad else ''))
P('')
P('## 2. What each reading does (means over seeds, programme rows; Reference)\n')
for d, dn in DES:
    P('### %s\n' % dn); P('| reading | ' + ' | '.join(m[1] for m in MECH) + ' |'); P('|---|' + '---|' * len(MECH))
    for r in READ:
        if not has('ref', r): continue
        mm = R['ref']['rows'][r]['mean'][d]; S['mech'].setdefault(d, {})[r] = {k: mm.get(k) for k, _, _ in MECH}
        P('| %s | ' % r + ' | '.join(('%.' + str(p) + 'f') % mm[k] if mm.get(k) is not None else '' for k, _, p in MECH) + ' |')
    P('')
P('## 3. Effects against no programme (programme minus no programme, paired)\n')
for k, kn in OUTC:
    P('### %s\n' % kn); P('| reading | ' + ' | '.join('%s %s' % (en, dn) for e, en in ENVS for d, dn in DES) + ' |'); P('|---|' + '---|' * 6)
    for r in READ:
        cells = []
        for e, en in ENVS:
            for d, dn in DES:
                t = eff(e, r, d, k); cells.append(fmt(k)(t)); S['effects'].setdefault(k, {}).setdefault(r, {})[e + '_' + d] = t
        P('| %s | ' % r + ' | '.join(cells) + ' |')
    P('')
P('## 4. Each reading\'s effect less the effect without `po` (`open`), paired by seed\n')
for k, kn in OUTC:
    P('### %s\n' % kn); P('| reading | ' + ' | '.join('%s %s' % (en, dn) for e, en in ENVS for d, dn in DES) + ' |'); P('|---|' + '---|' * 6)
    for r in READ[1:]:
        cells = []
        for e, en in ENVS:
            for d, dn in DES:
                t = dd(e, r, d, k) if has(e, r) and has(e, 'open') else (float('nan'),) * 3; cells.append(fmt(k)(t)); S['diff_open'].setdefault(k, {}).setdefault(r, {})[e + '_' + d] = t
        P('| %s | ' % r + ' | '.join(cells) + ' |')
    P('')
P('## 5. Each reading\'s effect less the main reading\'s, paired by seed\n')
for k, kn in OUTC:
    P('### %s\n' % kn); P('| reading | ' + ' | '.join('%s %s' % (en, dn) for e, en in ENVS for d, dn in DES) + ' |'); P('|---|' + '---|' * 6)
    for r in [x for x in READ if x not in ('main',)]:
        cells = []
        for e, en in ENVS:
            for d, dn in DES:
                t = dd(e, r, d, k, 'main') if has(e, r) and has(e, 'main') else (float('nan'),) * 3; cells.append(fmt(k)(t)); S['diff_main'].setdefault(k, {}).setdefault(r, {})[e + '_' + d] = t
        P('| %s | ' % r + ' | '.join(cells) + ' |')
    P('')
P('## 6. Signs (rule 3): readings whose programme effect has the other sign from `main`\'s (point estimates; "excl." where both intervals exclude zero)\n')
P('| outcome | environment | design | main | reading(s) with the other sign |'); P('|---|---|---|---|---|')
any_ = False
for k, kn in OUTC[:5]:
    for e, en in ENVS:
        for d, dn in DES:
            m = eff(e, 'main', d, k)
            if np.isnan(m[0]): continue
            other = []
            for r in READ:
                if r == 'main': continue
                t = eff(e, r, d, k)
                if not np.isnan(t[0]) and np.sign(t[0]) != np.sign(m[0]) and t[0] != 0: other.append(r + (' (excl.)' if (t[1] > 0 or t[2] < 0) and (m[1] > 0 or m[2] < 0) else ''))
            if other: any_ = True; S['signs'].setdefault(k, []).append([e, d, other]); P('| %s | %s | %s | %s | %s |' % (kn, en, dn, fmt(k)(m), ', '.join(other)))
if not any_: P('| (none) | | | | |')
P('')
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, 'w').write('\n'.join(L) + '\n')
json.dump(S, open(os.path.join(os.path.dirname(os.path.abspath(OUT)), 'summary.json'), 'w'), indent=1, default=lambda x: None)
print('wrote', OUT)
