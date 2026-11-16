#!/usr/bin/env python3
"""S77 (S74 preregistration Amendment 4): before a rerun of S74's forward sweep or discount readings is read, its "no central bank" arm ('off') must
equal release 2's main row per seed. Compares, for Reference, Adverse and Stress (20 years), both designs and both runs (no programme, programme),
basket poverty (fgt0PY), wealth poverty (pov) and median real wealth (wtMedE) on every seed the sweep ran, against the round-2 batch's shard
(compassionism-sim-results r2-m-<env>-20-104691f). The sweep saves six significant digits, so values must agree to a relative 1e-5.
Usage: python3 dev/tools/s77_check_off.py SWEEP_DIR R2_DIR      (SWEEP_DIR holds s74-sweep-ENV.json; exit 1 on any difference)"""
import gzip, json, os, sys

def main():
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    sdir, rdir = sys.argv[1], sys.argv[2]
    n, bad = 0, []
    for e, re_ in [('ref', 'ref'), ('adv', 'adv'), ('st', 'str')]:
        f = os.path.join(sdir, 's74-sweep-%s.json' % e)
        if not os.path.exists(f): bad.append(e + ': no sweep file'); continue
        S = json.load(open(f))
        R = json.load(gzip.open(os.path.join(rdir, 'r2-m-%s-20-104691f' % re_, 'shard-0000.json.gz')))['rows']
        for d in S['_meta']['designs']:
            for i, row in ((0, 'none'), (1, d)):
                for k in ('fgt0PY', 'pov', 'wtMedE'):
                    a = S[d]['off'][i][k]; b = R['%s.%s' % (re_, row)][k][:len(a)]
                    for s, (x, y) in enumerate(zip(a, b)):
                        n += 1
                        if abs(x - y) > 1e-5 * max(1, abs(y)): bad.append('%s %s %s %s seed %d: %r against %r' % (e, d, row, k, s + 1, x, y))
    if bad: print('DIFFERENCES (%d of %d values):\n  ' % (len(bad), n) + '\n  '.join(bad[:20])); sys.exit(1)
    print('check passed: the no-central-bank arm equals release 2\'s main row per seed (%d values: Reference, Adverse, Stress; both designs; '
          'both runs; basket poverty, wealth poverty, median real wealth)' % n)

if __name__ == '__main__': main()
