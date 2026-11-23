#!/usr/bin/env python3
"""S93 part 3 (Nov 23, 2026): section C3 of research-update prereg/2026-11-s90-private-price-at-sale.md (Amendment 2, with Amendment 3): the paired
change, release minus published, on the supply study's base rows at backed shares 0, 0.25, 0.5, 0.75 and 1. Written before any figure of the rerun
supply study was read.

  python3 dev/tools/s93_belowfull_change.py RESULTS_DIR OUT_DIR [--engine 50bc51d] [--pub aa2a4e0] [--reps 2000]

Reads s82-v6-<env>-<years>-<engine> (the rerun on the release engine) and s82-v6-<env>-<years>-<pub> (published) of compassionism-sim-results, rows
base.none and base.a<share>. A cell is one base row (one backed share) in one environment and horizon: 5 x 3 x 2 = 30 cells per outcome.

Reading (Claude's, the cautious one, stated before any figure): C3 compares "the base rows", and was written when the no-programme rows were expected
to equal the published ones (its validity condition, check D2). Amendment 3 put pay by household type and the care credit in both runs of the release
main row, so the release base.none is expected to differ from the published one by design; the condition is then replaced by Amendment 3's D2 (engine
proofs A1-A2 and the dry run), and the change is read on the programme's effect (base.a<share> minus base.none, paired by seed): release effect minus
published effect, a paired difference in differences. The change in the programme row's level is printed beside it, and whether base.none equals the
published one (keys and seeds that differ, counted).
Outcomes: the five primary outcomes of the preregistration (bNAPy, fgt0PY, ppovA, wtMedE, endoAnn x 100). Estimate: mean over seeds 1-500; 95%
interval: paired bootstrap, 2,000 resamples, numpy default_rng(9001), the same resample for every cell. Published whichever way it moves; no threshold.
Standard library and numpy; helpers from dev/tools/s90_tables.py (unchanged)."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s90_tables import shards, check2, est, ci, ENVS, ENVL, YEARS, LAB, SCALE, SEED, REPS, opt  # noqa: E402

PRIM = ['bNAPy', 'fgt0PY', 'ppovA', 'wtMedE', 'endoAnn']
SHARES = ['0', '0.25', '0.5', '0.75', '1']


def rows_of(folder, eng):
    bad, rows = check2(folder, eng)
    out = {}
    for r, v in (rows or {}).items():
        p = r.split('.')
        out['.'.join(p[2:]) if len(p) > 2 and p[1].isdigit() else r.split('.', 1)[1]] = v  # strip the environment and the row index
    return bad, out


def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    R, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
    eng, pubE, reps = opt('engine', '50bc51d'), opt('pub', 'aa2a4e0'), int(opt('reps', REPS))
    BS = np.random.default_rng(SEED).integers(0, 500, size=(reps, 500))
    md = ['# Below full backing: the paired change on the supply study\'s base rows (release minus published)\n',
          'Release `s82-v6-*-%s`; published `s82-v6-*-%s`; seeds 1-500; 95%% intervals by paired bootstrap (%d resamples, generator seed %d).\n' % (eng, pubE, reps, SEED),
          '## Checks\n']
    S = {'engine': eng, 'published': pubE, 'reps': reps, 'seed': SEED, 'checks': {}, 'cells': []}
    D, fail = {}, False
    for e in ENVS:
        for y in YEARS:
            bN, N = rows_of(os.path.join(R, 's82-v6-%s-%d-%s' % (e, y, eng)), eng)
            bP, P = rows_of(os.path.join(R, 's82-v6-%s-%d-%s' % (e, y, pubE)), pubE)
            need = ['base.none'] + ['base.a' + s for s in SHARES]
            miss = [r for r in need if r not in N or r not in P]
            nd = {'keys': 0, 'keysDiffer': 0, 'seedsDiffer': 0}
            if not miss:
                for k in P['base.none']:
                    if k not in N['base.none']: continue
                    a, b = N['base.none'][k], P['base.none'][k]; nd['keys'] += 1
                    s = (a == b) | (np.isnan(a) & np.isnan(b))
                    if not s.all(): nd['keysDiffer'] += 1; nd['seedsDiffer'] += int((~s).sum())
            S['checks']['%s-%d' % (e, y)] = {'release': bN, 'published': bP, 'missing': miss, 'noProgramme': nd}
            ok = lambda x: 'passes' if not x else 'FAILS: ' + '; '.join(x[:4])
            md.append('- %s, %d years: release folder %s; published folder %s; rows %s; no-programme row against the published one: %d of %d keys differ '
                      '(expected by design, Amendment 3)' % (ENVL[e], y, ok(bN), ok(bP), 'present' if not miss else 'MISSING ' + ', '.join(miss), nd['keysDiffer'], nd['keys']))
            if bN or bP or miss: fail = True
            else: D[(e, y)] = (N, P)
    md.append('')
    if fail:
        open(os.path.join(OUT, 's93-belowfull-change.md'), 'w').write('\n'.join(md) + '\nA check failed: no outcome is read.\n')
        json.dump(S, open(os.path.join(OUT, 's93-belowfull-change.json'), 'w'), indent=1)
        print('\n'.join(md)); sys.exit('a check failed: stopped before any outcome')
    md.append('## The change, per outcome\n')
    md.append('Effect: base row at the backed share minus base.none, paired by seed. Change in the effect: release effect minus published effect. Level: '
              'the base row itself, release minus published.\n')
    for k in PRIM:
        md.append('### %s\n' % LAB[k])
        md.append('| Environment | Years | Backed share | Published effect | Release effect | Change in the effect | Change in the level |')
        md.append('|---|---|---|---|---|---|---|')
        sc = SCALE.get(k, 1.0)
        for e in ENVS:
            for y in YEARS:
                N, P = D[(e, y)]
                for s in SHARES:
                    r = 'base.a' + s
                    eN, eP = (N[r][k] - N['base.none'][k])*sc, (P[r][k] - P['base.none'][k])*sc
                    o = {'key': k, 'env': e, 'years': y, 'share': float(s), 'published': est(eP, BS), 'release': est(eN, BS),
                         'change': est(eN - eP, BS), 'level': est((N[r][k] - P[r][k])*sc, BS)}
                    S['cells'].append(o)
                    md.append('| %s | %d | %s | %s | %s | %s | %s |' % (ENVL[e], y, s, ci(o['published'], k), ci(o['release'], k), ci(o['change'], k), ci(o['level'], k)))
        md.append('')
    open(os.path.join(OUT, 's93-belowfull-change.md'), 'w').write('\n'.join(md) + '\n')
    json.dump(S, open(os.path.join(OUT, 's93-belowfull-change.json'), 'w'), indent=1)
    print('wrote %s/s93-belowfull-change.md and s93-belowfull-change.json' % OUT)


if __name__ == '__main__':
    main()
