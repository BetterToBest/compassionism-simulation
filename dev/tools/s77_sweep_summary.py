#!/usr/bin/env python3
"""S77: the figures the S74 report's "forward sweep" section quotes, read from a sweep-tables.json (dev/tools/s74_sweep_table.js). Run on the first
sweep's tables it prints the figures as first published (a check that each is read from the right cell); run on the corrected sweep it prints the
corrected ones. Nothing is run here. Usage: python3 dev/tools/s77_sweep_summary.py DIR   (DIR holds sweep-tables.json)"""
import json, os, sys

T = json.load(open(os.path.join(sys.argv[1], 'sweep-tables.json')))
KEYS = ['stP1', 'stP2', 'stP3', 'rkRecM', 'stP5', 'fgt0PY', 'pov']
CB = lambda n: n not in ('off', 'actual', 'actual-sp1.5', 'actual-sp4.5')
m = lambda c: None if c is None else c['m']

print('1. sign of the programme effect E against the main rule, central-bank settings')
for e in ('hx', 'adv', 'st', 'ref'):
    for d in ('c22', 'rel'):
        R = T[e][d]['rows']; names = [n for n in R if CB(n)]
        for k in KEYS:
            base = R['main']['E'][k]['m']
            flips = [(n, round(R[n]['E'][k]['m'], 2)) for n in names if R[n]['E'][k]['m'] * base < 0]
            if flips: print('  %s %s %s main %.2f; flips in %d of %d: %s' % (e, d, k, base, len(flips), len(names), flips))
        if d == 'c22': print('  %s %s settings %d' % (e, d, len(names)))
print('2. C2.2 cut in basket poverty (fgt0PY) and wealth poverty (pov) across central-bank settings')
for e in ('hx', 'adv', 'st', 'ref'):
    R = T[e]['c22']['rows']; names = [n for n in R if CB(n)]
    for k in ('fgt0PY', 'pov'):
        v = [R[n]['E'][k]['m'] for n in names]; print('  %s %s %.1f to %.1f' % (e, k, min(v), max(v)))
print('3. largest |X| on P1 over all settings: %.4f' % max(abs(T[e][d]['rows'][n]['X']['m']) for e in T if e != '_meta' for d in ('c22', 'rel') for n in T[e][d]['rows']))
print('4. the central bank\'s effect on wealth poverty without the programme (C pov0) and basket poverty (C fgt0PY0), points; cbU; cbFloor; cbQmax')
for e, ns in (('hx', ['main', 'nofs', 'sp1.5', 'sp4.5', 'fd0.1', 'fd0.27', 'fd0.034', 'fd0.062', 'actual', 'actual-sp1.5', 'actual-sp4.5', 'reg2022', 'a2', 'reg2008', 'reg2020']),
              ('adv', ['main', 'b0', 'b1', 'reg2008', 'reg2020', 'reg2022']), ('st', ['main']), ('ref', ['main', 'b0', 'b1'])):
    for d in ('c22',):
        R = T[e][d]['rows']
        for n in ns:
            if n not in R: continue
            r = R[n]; C = r.get('C') or {}
            print('  %s %-13s pov0 %6s fgt0PY0 %6s | cbU %s cbFloor %s cbQmax %s' % (e, n, None if C.get('pov0') is None else round(C['pov0']['m'], 2),
                  None if C.get('fgt0PY0') is None else round(C['fgt0PY0']['m'], 2), *(None if r.get(k) is None else round(r[k]['m'], 2) for k in ('cbU', 'cbFloor', 'cbQmax'))))
print('5. programme runs: cbFloor and cbQmax (max over designs) in History and Adverse')
for e in ('hx', 'adv'):
    for n in ('main', 'a2', 'reg2008', 'reg2020'):
        f = [T[e][d]['rows'][n] for d in ('c22', 'rel')]
        print('  %s %-8s floor %s qmax %s' % (e, n, [round(x['cbFloor']['m'], 1) for x in f], [round(x['cbQmax']['m'], 1) for x in f]))
print('6. dm: the rule\'s effect on the release design\'s wealth poverty (C pov1), main against dm0.5 and dm1')
for e in ('hx', 'adv', 'st', 'ref'):
    R = T[e]['rel']['rows']; print('  %s main %.2f dm0.5 %.2f dm1 %.2f' % (e, R['main']['C']['pov1']['m'], R['dm0.5']['C']['pov1']['m'], R['dm1']['C']['pov1']['m']))
print('7. endoAnn max over settings: %.4f' % max(T[e][d]['rows'][n]['endoAnn']['m'] for e in T if e != '_meta' for d in ('c22', 'rel') for n in T[e][d]['rows']))
