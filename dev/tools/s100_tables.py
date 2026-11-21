#!/usr/bin/env python3
"""S100 (Nov 21, 2026): the tables of the study of pay by household type and the child and dependent care credit in the no-programme yardstick
(research-update prereg/2026-11-s100-part-time-dcc.md). Written before any result of the six folders was read.

  python3 dev/tools/s100_tables.py RESULTS_DIR OUT_DIR --engine ENGINE7 [--pub b8ccd8d] [--reps 2000]

Reads the six folders s100-<env>-<years>-<engine> of compassionism-sim-results (runner/jobs/s100.js; 22 rows; every key at full precision; seeds 1-500
across shards) and the published at-sale folders s90-sale-<env>-<years>-<pub>.

Checks first (prereg "Checks"; the script stops before any outcome if one fails, decision rule 1):
  1. none.off, c22.off, rel.off equal the published rows none, c22.sale, rel.sale per seed on every key those rows hold;
  2. every folder has DONE, run.txt and SHA256SUMS (each sum verified), shards covering seeds 1-500 once, the engine commit and a clean engine in every
     shard, and 500 values per key in every row.
Then:
  Q1  the yardstick: no-programme rows' EITC, CTC and care-credit reach (overall, by household type, full take-up rows) against the US figures fixed in
      the preregistration, with the gap rule; decision rule 2 at Reference, 20 years.
  Q2  per design, environment, horizon and reading: the programme's effect (programme row minus its no-programme row) and the change against `off`
      (a paired difference in differences) on the five primary outcomes, Holm across the five within each cell; the bound rows pair with none.both.
  Q3  the interaction (both - cdc) - (eh - off) on each primary effect.
  Secondary outcomes: effects and changes, no adjustment.
Estimates: mean over seeds; 95% intervals by paired bootstrap (2,000 resamples, numpy default_rng seed 9001, the same resample for every row);
p: two-sided paired t (s90_tables.tcdf). Helpers are imported from dev/tools/s90_tables.py (unchanged).
Standard library and numpy."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s90_tables import shards, join, derive, check2, est, holm, fmt, ci, ENVS, ENVL, YEARS, DES, DESL, PRIM, LAB, SCALE, DOLLAR, SEED, REPS, opt  # noqa: E402

SEC = ['fgt2PY', 'Er', 'dmYp50E', 'cost', 'wtF0E', 'wtPovE', 'snCdcM', 'snEitcM', 'snCtcM']
LAB = dict(LAB, snCdcM='care credit, $ per adult-year', snEitcM='EITC, $ per adult-year', snCtcM='refundable CTC, $ per adult-year')
DOLLAR = set(DOLLAR) | {'snCdcM', 'snEitcM', 'snCtcM'}
READS = ['off', 'eh', 'cdc', 'both', 'pc0', 'call', 'bound']
READL = {'off': "today's main row", 'eh': 'pay by household type', 'cdc': 'the care credit', 'both': 'both', 'pc0': 'both, partners independent',
         'call': 'both, credit for every family', 'bound': 'both, credit in the no-programme run only'}
US = {'snEitc': 11.77, 'snEitcSg': 8.62, 'snEitcSp': 49.77, 'snEitcCn': 4.55, 'snEitcCk': 16.54, 'snCtcSp': 45.31, 'snCtcCk': 19.00, 'snCdcK': 21.37, 'snCdcR': 606.0}
YK = ['snEitc', 'snEitcSg', 'snEitcSp', 'snEitcCn', 'snEitcCk', 'snCtc', 'snCtcSp', 'snCtcCk', 'snCdcK', 'snCdcR', 'fgt0PY', 'bNAPy', 'ppovA', 'wtMedE']
TYPES = ['snEitcSg', 'snEitcSp', 'snEitcCn', 'snEitcCk']


def check1(new, pub, env):
    bad, n = [], 0
    for a_, b_ in (('none.off', 'none'), ('c22.off', 'c22.sale'), ('rel.off', 'rel.sale')):
        a, b = new.get(env + '.' + a_), pub.get(env + '.' + b_)
        if a is None or b is None: bad.append('row %s or %s missing' % (a_, b_)); continue
        for k, y in b.items():
            if k not in a: bad.append('%s: key %s missing' % (a_, k)); continue
            x = a[k]; n += len(y)
            same = (x == y) | (np.isnan(x) & np.isnan(y))
            if not same.all(): bad.append('%s %s: %d seeds differ' % (a_, k, int((~same).sum())))
    return bad, n


def gap(k, m):
    u = US.get(k)
    if u is None: return ''
    return 'gap' if (k == 'snCdcR' and not 0.8 <= m/u <= 1.25) or (k != 'snCdcR' and abs(m - u) > 3) else '-'


def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    R, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
    eng, pubE, reps = opt('engine', ''), opt('pub', 'b8ccd8d'), int(opt('reps', REPS))
    if not eng: sys.exit('--engine is required')
    BS = np.random.default_rng(SEED).integers(0, 500, size=(reps, 500))
    md, S, data, fail = [], {'engine': eng, 'published': pubE, 'reps': reps, 'seed': SEED, 'checks': {}, 'yardstick': {}, 'cells': []}, {}, False
    md.append('# Pay by household type and the child and dependent care credit in the yardstick: tables\n')
    md.append('Engine `%s`; published at-sale rows `s90-sale-*-%s`; paired over seeds 1-500; 95%% intervals by paired bootstrap (%d resamples, generator seed %d).\n' % (eng, pubE, reps, SEED))
    md.append('## Checks\n')
    for e in ENVS:
        for y in YEARS:
            b2, rows = check2(os.path.join(R, 's100-%s-%d-%s' % (e, y, eng)), eng)
            pd = shards(os.path.join(R, 's90-sale-%s-%d-%s' % (e, y, pubE)))
            b1, n1 = check1(rows, join(pd), e) if rows and pd else (['cannot compare (folder missing)'], 0)
            S['checks']['%s-%d' % (e, y)] = {'check1': b1, 'check1Values': n1, 'check2': b2}
            md.append('- %s, %d years: check 1 %s (%s values); check 2 %s' % (ENVL[e], y, 'passes' if not b1 else 'FAILS: ' + '; '.join(b1[:4]), '{:,}'.format(n1), 'passes' if not b2 else 'FAILS: ' + '; '.join(b2[:4])))
            if b1 or b2: fail = True
            if rows: data[(e, y)] = {r.split('.', 1)[1]: derive(v, y) for r, v in rows.items()}
    md.append('')
    if fail:
        open(os.path.join(OUT, 's100-tables.md'), 'w').write('\n'.join(md) + '\nA check failed: no outcome is read (decision rule 1).\n')
        json.dump(S, open(os.path.join(OUT, 's100-summary.json'), 'w'), indent=1)
        print('\n'.join(md)); sys.exit('a check failed: stopped before any outcome (decision rule 1)')
    # ---- Q1: the yardstick
    md.append('## Question 1: the yardstick (no-programme rows)\n')
    for e in ENVS:
        for y in YEARS:
            D = data[(e, y)]; Y = {}
            md.append('### %s, %d years\n' % (ENVL[e], y))
            md.append('| Measure | US | ' + ' | '.join(['off', 'eh', 'cdc', 'both', 'pc0', 'call', 'off, full take-up', 'both, full take-up']) + ' |')
            md.append('|---|---|' + '---|'*8)
            for k in YK:
                cells = []
                for r in ['off', 'eh', 'cdc', 'both', 'pc0', 'call', 'off.full', 'both.full']:
                    v = D['none.' + r].get(k)
                    if v is None: cells.append('-'); continue
                    m = float(np.nanmean(v)); Y.setdefault(r, {})[k] = m
                    g = gap(k, m) if r.endswith('full') or k in ('snCdcK', 'snCdcR') else ''
                    cells.append(fmt(m, k) + (' (gap)' if g == 'gap' else ''))
                md.append('| %s | %s | %s |' % (k, fmt(US[k], k) if k in US else '', ' | '.join(cells)))
            S['yardstick']['%s-%d' % (e, y)] = Y
            md.append('')
    Y = S['yardstick']['ref-20']; o, b = Y['off.full'], Y['both.full']
    sumGap = lambda z: sum(abs(z[k] - US[k]) for k in TYPES)
    within = sum(1 for k in TYPES if abs(b[k] - US[k]) <= 3)
    rule2 = abs(b['snEitc'] - US['snEitc']) <= 3 and within >= 3 and sumGap(b) < sumGap(o)
    S['rule2'] = {'holds': rule2, 'overallGap': b['snEitc'] - US['snEitc'], 'typesWithin3': within, 'sumGapOff': sumGap(o), 'sumGapBoth': sumGap(b)}
    md.append('Decision rule 2 (Reference, 20 years, full take-up): overall EITC reach %s against %s; %d of 4 household types within 3 points; sum of the types\' gaps %s (both) against %s (off): **%s**.\n'
              % (fmt(b['snEitc'], 'x'), fmt(US['snEitc'], 'x'), within, fmt(sumGap(b), 'x'), fmt(sumGap(o), 'x'), 'holds: both is the recommended yardstick reading' if rule2 else 'does not hold'))
    # ---- Q2 and Q3
    md.append('## Question 2: the programme\'s effect under each reading, and its change against today\'s main row\n')
    md.append('Effect = programme row minus its no-programme row; change = effect under the reading minus effect under `off`, paired by seed. The bound rows pair with the no-programme row of `both`. Holm across the five primary outcomes within each cell, for the change. ✱ = Holm-adjusted 95% interval excludes zero.\n')
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                D = data[(e, y)]
                def eff(r, k):
                    p = D[d + '.' + r][k]; n = D['none.' + ('both' if r == 'bound' else r)][k]; return (p - n)*SCALE.get(k, 1.0)
                md.append('### %s, %s, %d years\n' % (DESL[d], ENVL[e], y))
                md.append('| Reading | ' + ' | '.join(LAB[k] for k in PRIM) + ' |'); md.append('|---|' + '---|'*len(PRIM))
                cell = {'design': d, 'env': e, 'years': y, 'effect': {}, 'change': {}, 'interaction': {}}
                for r in READS:
                    E = {k: est(eff(r, k), BS) for k in PRIM}; cell['effect'][r] = E
                    md.append('| %s: effect | %s |' % (READL[r], ' | '.join(ci(E[k], k) for k in PRIM)))
                    if r == 'off': continue
                    C = {k: est(eff(r, k) - eff('off', k), BS) for k in PRIM}; ha = holm([C[k]['p'] for k in PRIM])
                    for i, k in enumerate(PRIM): C[k]['pHolm'] = ha[i]; C[k]['star'] = ha[i] < 0.05
                    cell['change'][r] = C
                    md.append('| %s: change | %s |' % (READL[r], ' | '.join(ci(C[k], k) + (' ✱' if C[k]['star'] else '') for k in PRIM)))
                I = {k: est((eff('both', k) - eff('cdc', k)) - (eff('eh', k) - eff('off', k)), BS) for k in PRIM}; cell['interaction'] = I
                md.append('| interaction (both − cdc) − (eh − off) | %s |' % ' | '.join(ci(I[k], k) + (' ✱' if I[k]['lo'] > 0 or I[k]['hi'] < 0 else '') for k in PRIM))
                cell['secondary'] = {r: {k: est(eff(r, k) - eff('off', k), BS) for k in SEC if k in D[d + '.' + r] and k in D['none.off']} for r in READS if r != 'off'}
                S['cells'].append(cell); md.append('')
    md.append('## Secondary outcomes (change against `off`, no adjustment)\n')
    for c in S['cells']:
        md.append('- %s, %s, %d years: ' % (DESL[c['design']], ENVL[c['env']], c['years']) + '; '.join('%s %s' % (r, ', '.join('%s %s' % (k, ci(v, k)) for k, v in c['secondary'][r].items())) for r in ('both', 'bound')))
    open(os.path.join(OUT, 's100-tables.md'), 'w').write('\n'.join(md) + '\n')
    json.dump(S, open(os.path.join(OUT, 's100-summary.json'), 'w'), indent=1, default=float)
    print('\n'.join(md[:60]))


if __name__ == '__main__':
    main()
