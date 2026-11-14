"""S68 part 2: tables of the on-together tests and the 10,000-adult checks (dev/runs/s68-pairs/*.json -> tables.md).
Usage: python3 dev/tools/s68_pairs_table.py [DIR]"""
import json, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'runs', 's68-pairs')
out = ['# S68 part 2: on-together tests of the round-2 switches, and the 10,000-adult checks', '',
       'Written by `python3 dev/tools/s68_pairs_table.py`. A test, not a study: no figure here is a result.', '']
envs = [e for e in ('ref', 'adv', 'st') if os.path.exists(os.path.join(D, 's68-pairs-%s.json' % e))]
P = {e: json.load(open(os.path.join(D, 's68-pairs-%s.json' % e))) for e in envs}
if P:
    m = P[envs[0]]['manifest']
    out += ['## 1. The on-together tests', '', 'Engine commit %s (dirty %s); %d seeds; design %s. Every row is the candidate main row (`r2MainRow`) with the readings named; both runs of each pair are checked.' % (m['commit'], m['dirty'], P[envs[0]]['seeds'], P[envs[0]]['design']), '',
            '| Environment | Rows | Pass | Failed | Run order (main pair; no programme alone) | Seconds |', '|---|---|---|---|---|---|']
    for e in envs:
        s = P[e]['summary']; ro = P[e]['runOrder']
        out.append('| %s | %d | %d | %s | %s; %s | %.0f |' % (e, s['rows'], s['pass'], ', '.join(s['fail'] + s['threw']) or 'none', 'identical' if ro['mainSame'] else 'DIFFERS', 'identical' if ro['noneSame'] else 'DIFFERS', P[e]['secs']))
    out += ['', 'The other readings (`R2_ALT`):', '']
    out += ['- `%s`: %s' % (a[0], a[1]) for a in P[envs[0]]['alts']]
    out += ['', '### Checks per row (Reference first; identities checked, draws counted, failures)', '', '| Row | Identity checks | Identity failures | Runs counted | Draw-count failures | Non-finite keys | Own-check failures |', '|---|---|---|---|---|---|---|']
    for e in envs:
        for x in P[e]['rows']:
            n = sum((x.get('acct') or {}).get('n', {}).values()) if isinstance((x.get('acct') or {}).get('n'), dict) else (x.get('acct') or {}).get('n', 0)
            out.append('| %s %s | %s | %s | %s | %s | %s | %s |' % (e, x['id'], n, (x.get('acct') or {}).get('nFail', '-'), (x.get('draws') or {}).get('runs', '-'), (x.get('draws') or {}).get('bad', '-'), len(x.get('nonFinite') or []), '; '.join(x.get('own') or []) or (x.get('threw') or '0')))
B = {e: json.load(open(os.path.join(D, 's68-big-%s.json' % e))) for e in ('ref', 'adv', 'st') if os.path.exists(os.path.join(D, 's68-big-%s.json' % e))}
if B:
    out += ['', '## 2. The 10,000-adult checks (the tail and the creditor totals)', '', 'Candidate main row, C2.2 design, %d seeds; each cell is no programme / programme, the mean over seeds.' % list(B.values())[0]['seeds'], '']
    ids = ['500 tail', '500 no tail', '10000 tail', '10000 no tail']
    for e, b in B.items():
        out += ['### %s' % e, '', '| Key | ' + ' | '.join(ids) + ' |', '|---|' + '---|'*len(ids)]
        for k in b['keys']:
            cells = []
            for i in ids:
                r = b['runs'][i]; f = lambda v: '-' if v is None else ('%.6g' % v)
                cells.append('%s / %s' % (f(r['none'].get(k)), f(r['prog'].get(k))))
            out.append('| `%s` | ' % k + ' | '.join(cells) + ' |')
        out.append('')
open(os.path.join(D, 'tables.md'), 'w').write('\n'.join(out) + '\n')
print(os.path.join(D, 'tables.md'))
