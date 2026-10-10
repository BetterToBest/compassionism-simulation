"""v5.4 step 9 (Oct 8, 2026; dev/DECISIONS.md Session 41): join the pieces of one environment's release panel run with `--part=I/K` into the whole panel.

Every row of the panel is its own run on the same seeds (common random numbers), so a row's figures do not depend on which other rows ran beside it; each
piece also runs the main and today rows and the no-programme runs its readings are paired with. This checks that the pieces come from one build, that every
row and no-programme run appears, and that a row appearing in more than one piece is identical in each, then writes the panel in the order the whole run
would have written it.

Usage: python3 dev/tools/merge_parts.py IN_DIR ENV YEARS K OUT
       (reads IN_DIR/release-panel[-40]-ENV.partI.json for I = 0..K-1; YEARS 20 or 40; writes OUT)
"""
import json, sys

def main(d, env, years, k, out):
    suf = '-40' if years == '40' else ''
    P = [json.load(open('%s/release-panel%s-%s.part%d.json' % (d, suf, env, i))) for i in range(k)]
    m0 = P[0]['_meta']
    for i, p in enumerate(P):
        m = p['_meta']
        if m['manifest'] != m0['manifest']: sys.exit('merge_parts: piece %d comes from another build' % i)
        if m['part']['k'] != k or m['part']['i'] != i: sys.exit('merge_parts: piece %d is %s' % (i, m['part']))
        if m['part']['rows'] != m0['part']['rows'] or m['part']['bases'] != m0['part']['bases']: sys.exit('merge_parts: piece %d has another row list' % i)
        if json.dumps(p['envs'][env]['base'], sort_keys=True) != json.dumps(P[0]['envs'][env]['base'], sort_keys=True): sys.exit('merge_parts: the no-programme run differs in piece %d' % i)
    order, border = m0['part']['rows'], m0['part']['bases']
    rows, bases = {}, {}
    for p in P:
        E = p['envs'][env]
        for j, r in E['rows'].items():
            if j in rows and json.dumps(rows[j], sort_keys=True) != json.dumps(r, sort_keys=True): sys.exit('merge_parts: row %s differs between pieces' % j)
            rows[j] = r
        for j, b in (E.get('bases') or {}).items():
            if j in bases and json.dumps(bases[j], sort_keys=True) != json.dumps(b, sort_keys=True): sys.exit('merge_parts: no-programme run %s differs between pieces' % j)
            bases[j] = b
    want = [j for j in order if j not in border]
    miss = [j for j in want if j not in rows] + [j for j in border if j not in bases]
    if miss: sys.exit('merge_parts: missing ' + ', '.join(miss))
    E0 = P[0]['envs'][env]
    E = {'name': E0['name'], 'base': E0['base'], 'rows': {j: rows[j] for j in want}}
    if border: E['bases'] = {j: bases[j] for j in border}
    meta = {k2: v for k2, v in m0.items() if k2 != 'part'}
    meta['command'] = meta['command'] + ' (run in %d pieces with --part=I/%d; python3 dev/tools/merge_parts.py)' % (k, k)
    json.dump({'_meta': meta, 'envs': {env: E}}, open(out, 'w'), indent=1)
    print('merged %d pieces: %d rows, %d no-programme pairs -> %s' % (k, len(want), len(border), out))

if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) != 5: sys.exit(__doc__)
    main(a[0], a[1], a[2], int(a[3]), a[4])
