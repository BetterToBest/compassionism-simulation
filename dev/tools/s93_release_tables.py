#!/usr/bin/env python3
"""S93 part 3 (Nov 23, 2026): the release's main-row table of published against release values, with the change split in two
(research-update prereg/2026-11-s90-private-price-at-sale.md, Amendment 2 item F1 as Amendment 3 changes it). Written before any figure of the rerun
part M was read.

  python3 dev/tools/s93_release_tables.py RESULTS_DIR OUT_DIR [--engine 50bc51d] [--pub 104691f] [--sale b8ccd8d] [--reps 2000]

Reads, per environment (Reference, Adverse, Stress) and horizon (20, 40 years), from compassionism-sim-results:
  published  r2-m-<env>-<years>-<pub>      the frozen model's main rows (private price paid a year late; rows none, c22, rel)
  at sale    s90-sale-<env>-<years>-<sale> the same rows with the private price at the sale (rows none, c22.sale, rel.sale)
  release    r2-m-<env>-<years>-<engine>   the rerun part M on the release engine (private price at the sale, pay by household type, care credit)
  yardstick  s100-<env>-<years>-<engine>   the yardstick study rerun on the release engine (rows *.off and *.both), for the checks only

The change from published to release goes in two steps, each a paired difference in differences over seeds 1-500:
  price      (at-sale effect) - (published effect): the private price at the sale alone
  readings   (release effect) - (at-sale effect): pay by household type and the care credit, on the at-sale row
  total      (release effect) - (published effect) = price + readings, exactly (the same seeds; no remainder)
where an effect is the programme row minus its own no-programme row (the no-programme row changes with the readings, so it is paired too).

Checks first; the script stops before any outcome if one fails:
  1. every folder: DONE, run.txt, SHA256SUMS (each sum verified), shards covering seeds 1-500 once, its engine commit and a clean engine in every shard,
     500 values per key (s90_tables.check2);
  2. the at-sale no-programme row equals the published one per seed on every key the published row holds (it does not read the price rule);
  3. the yardstick's none.off, c22.off, rel.off equal the at-sale rows none, c22.sale, rel.sale per seed on every key both hold (so the readings step is
     the yardstick's both against off on the release engine), and its none.both, c22.both, rel.both equal the release rows none, c22, rel (check D3).
Then per design (c22 full coverage, rel opt-in), environment and horizon, for the primary and secondary outcomes of s90_tables.py: the published, at-sale
and release effects, and the three changes, each with its 95% interval (paired bootstrap, 2,000 resamples, numpy default_rng seed 9001, the same
resample for every row and step); Holm across the five primary outcomes within each cell, for "the total change is not zero". Each primary row is
marked: the direction of the total change (for the programme: lower poverty, lower inflation, higher wealth), and whether the effect's sign or its
value at REPRODUCE.md's rounding (2 decimals; whole dollars) changes. Pages are read against these in the pre-publish check (F1's page part).
Standard library and numpy. Helpers are imported from dev/tools/s90_tables.py (unchanged)."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s90_tables import shards, join, derive, check2, est, holm, ci, rnd, ENVS, ENVL, YEARS, DES, DESL, PRIM, SEC, LAB, SCALE, SEED, REPS, opt  # noqa: E402

GOOD_UP = {'wtMedE', 'Er', 'dmYp50E'}  # outcomes where a larger programme effect is in the programme's favour; for the others smaller is
STEPS = [('price', 'Private price at the sale'), ('readings', 'Pay by household type and the care credit'), ('total', 'Total')]


def strip(rows):
    """row names without the environment prefix (ref., adv., st., str.)"""
    return {r.split('.', 1)[1]: v for r, v in rows.items()} if rows else rows


def equal(a, b, pairs, keys_of='b'):
    bad, n = [], 0
    for x_, y_ in pairs:
        x, y = a.get(x_), b.get(y_)
        if x is None or y is None: bad.append('row %s or %s missing' % (x_, y_)); continue
        ks = [k for k in (y if keys_of == 'b' else x) if k in x and k in y] if keys_of == 'both' else list(y)
        if not ks: bad.append('%s / %s: no key in common' % (x_, y_)); continue
        for k in ks:
            if k not in x: bad.append('%s: key %s missing' % (x_, k)); continue
            u, v = x[k], y[k]; n += len(v)
            s = (u == v) | (np.isnan(u) & np.isnan(v))
            if not s.all(): bad.append('%s/%s %s: %d seeds differ' % (x_, y_, k, int((~s).sum())))
    return bad, n


def direction(k, ch):
    if ch['lo'] <= 0 <= ch['hi']: return 'interval includes 0'
    fav = ch['est'] > 0 if k in GOOD_UP else ch['est'] < 0
    return "programme's favour" if fav else 'AGAINST the programme'


def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    R, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
    eng, pubE, saleE, reps = opt('engine', '50bc51d'), opt('pub', '104691f'), opt('sale', 'b8ccd8d'), int(opt('reps', REPS))
    BS = np.random.default_rng(SEED).integers(0, 500, size=(reps, 500))
    md = ['# The release main rows against the published main rows: the change, split\n',
          'Published `r2-m-*-%s`; at the sale `s90-sale-*-%s`; release `r2-m-*-%s`; yardstick (checks) `s100-*-%s`. Effects paired over seeds 1-500; '
          '95%% intervals by paired bootstrap (%d resamples, generator seed %d, the same resample for every row and step).\n' % (pubE, saleE, eng, eng, reps, SEED),
          '## Checks\n']
    S = {'engine': eng, 'published': pubE, 'sale': saleE, 'reps': reps, 'seed': SEED, 'checks': {}, 'cells': []}
    data, fail = {}, False
    for e in ENVS:
        for y in YEARS:
            F = {n: os.path.join(R, '%s-%s-%d-%s' % (p, e, y, c)) for n, p, c in (('pub', 'r2-m', pubE), ('sale', 's90-sale', saleE), ('rel', 'r2-m', eng), ('yd', 's100', eng))}
            b, rows = [], {}
            for n, f in F.items():
                if not os.path.isdir(f): b.append(os.path.basename(f) + ' missing'); continue
                bb, rr = check2(f, {'pub': pubE, 'sale': saleE}.get(n, eng)); b += [os.path.basename(f) + ': ' + x for x in bb]; rows[n] = strip(rr)
            b2 = b3 = []; n2 = n3 = 0
            if len(rows) == 4:
                b2, n2 = equal(rows['sale'], rows['pub'], [('none', 'none')])
                b3a, n3a = equal(rows['yd'], rows['sale'], [('none.off', 'none'), ('c22.off', 'c22.sale'), ('rel.off', 'rel.sale')], 'both')
                b3b, n3b = equal(rows['yd'], rows['rel'], [('none.both', 'none'), ('c22.both', 'c22'), ('rel.both', 'rel')], 'both')
                b3, n3 = b3a + b3b, n3a + n3b
            S['checks']['%s-%d' % (e, y)] = {'check1': b, 'check2': b2, 'check2Values': n2, 'check3': b3, 'check3Values': n3}
            ok = lambda x: 'passes' if not x else 'FAILS: ' + '; '.join(x[:4])
            md.append('- %s, %d years: check 1 %s; check 2 %s (%s values); check 3 %s (%s values)' % (ENVL[e], y, ok(b), ok(b2), '{:,}'.format(n2), ok(b3), '{:,}'.format(n3)))
            if b or b2 or b3: fail = True
            if not fail: data[(e, y)] = {n: {r: derive(v, y) for r, v in rows[n].items()} for n in ('pub', 'sale', 'rel')}
    md.append('')
    if fail:
        open(os.path.join(OUT, 's93-release-tables.md'), 'w').write('\n'.join(md) + '\nA check failed: no outcome is read.\n')
        json.dump(S, open(os.path.join(OUT, 's93-release-summary.json'), 'w'), indent=1)
        print('\n'.join(md)); sys.exit('a check failed: stopped before any outcome')
    md.append('## The change from the published main rows to the release, per design, environment and horizon\n')
    md.append('Effect: programme row minus its no-programme row. Steps: the private price at the sale (at-sale effect minus published effect), then pay by '
              'household type and the care credit (release effect minus at-sale effect); their sum is the total. p (Holm): the total change, across the '
              'five primary outcomes of the cell. Marks: direction of the total change for the programme; whether the effect changes sign or its rounded '
              'value (2 decimals, whole dollars).\n')
    count = {'cells': 0, 'sign': 0, 'rounding': 0, 'against': 0, 'favour': 0, 'zero': 0}
    for d in DES:
        for e in ENVS:
            for y in YEARS:
                P, A, L = data[(e, y)]['pub'], data[(e, y)]['sale'], data[(e, y)]['rel']
                rows = {'pub': (P[d], P['none']), 'sale': (A[d + '.sale'], A['none']), 'rel': (L[d], L['none'])}
                md.append('### %s, %s, %d years\n' % (DESL[d], ENVL[e], y))
                md.append('| Outcome | Published effect | Release effect | Price at the sale | The two readings | Total change | p (Holm) | Direction | Sign or rounding |')
                md.append('|---|---|---|---|---|---|---|---|---|')
                cell, ps = [], []
                for k in PRIM + SEC:
                    if any(k not in r or k not in b for r, b in rows.values()): md.append('| %s | not stored | | | | | | | |' % LAB[k]); continue
                    sc = SCALE.get(k, 1.0)
                    eff = {n: (r[k] - b[k])*sc for n, (r, b) in rows.items()}
                    o = {'key': k, 'primary': k in PRIM, 'published': est(eff['pub'], BS), 'sale': est(eff['sale'], BS), 'release': est(eff['rel'], BS),
                         'price': est(eff['sale'] - eff['pub'], BS), 'readings': est(eff['rel'] - eff['sale'], BS), 'total': est(eff['rel'] - eff['pub'], BS)}
                    if k in PRIM:
                        ps.append(o['total']['p']); o['direction'] = direction(k, o['total'])
                        pe, re_ = o['published']['est'], o['release']['est']
                        o['mark'] = 'sign' if (pe > 0) != (re_ > 0) else 'rounding' if rnd(pe, k) != rnd(re_, k) else 'no'
                    cell.append(o)
                H = holm(ps); j = 0
                for o in cell:
                    if o['primary']:
                        o['total']['pHolm'] = H[j]; j += 1; count['cells'] += 1
                        count['sign'] += o['mark'] == 'sign'; count['rounding'] += o['mark'] == 'rounding'
                        count['against'] += o['direction'].startswith('AGAINST'); count['favour'] += o['direction'].startswith('programme'); count['zero'] += o['direction'].startswith('interval')
                    ph = '%.2g' % o['total']['pHolm'] if o['primary'] else '%.2g (unadjusted)' % o['total']['p']
                    md.append('| %s%s | %s | %s | %s | %s | %s | %s | %s | %s |' % (LAB[o['key']], '' if o['primary'] else ' (secondary)', ci(o['published'], o['key']), ci(o['release'], o['key']),
                              ci(o['price'], o['key']), ci(o['readings'], o['key']), ci(o['total'], o['key']), ph, o.get('direction', '–'), o.get('mark', '–')))
                md.append('')
                S['cells'].append({'design': d, 'env': e, 'years': y, 'outcomes': cell})
    S['count'] = count
    md.insert(md.index('## The change from the published main rows to the release, per design, environment and horizon\n') + 1,
              'Over the %d primary effects (2 designs x 3 environments x 2 horizons x 5 outcomes): total change in the programme\'s favour %d, against it %d, '
              'interval including 0 %d; effect changes sign %d, changes at its rounding %d.\n' % (count['cells'], count['favour'], count['against'], count['zero'], count['sign'], count['rounding']))
    open(os.path.join(OUT, 's93-release-tables.md'), 'w').write('\n'.join(md) + '\n')
    json.dump(S, open(os.path.join(OUT, 's93-release-summary.json'), 'w'), indent=1)
    print('wrote %s/s93-release-tables.md and s93-release-summary.json' % OUT)


if __name__ == '__main__':
    main()
