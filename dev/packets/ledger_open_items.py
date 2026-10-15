"""Writes the open items of the project ledger (decisions not confirmed, open issues, steps not done) as one plain-text file, for chats that
cannot read the ledger. Usage: python3 -I dev/packets/ledger_open_items.py <sim.json> <out.md>   (sim.json: the "sim" project document of the ledger)"""
import json, sys
d = json.load(open(sys.argv[1])); d = d.get('data', d)
o = ['# Simulation project: open items from the ledger (saved Oct 15, 2026)', '',
     'The ledger is the claude.ai artifact the project owner keeps; this file is a copy of what is still open, for chats that cannot open it. Decisions show the default that applies if the owner does not answer.', '']
o += ['## Next action', '', d.get('next', ''), '', '## Open decisions', '']
for x in d['decisions']:
    if not x.get('confirmed'):
        o += ['- **%s** %s' % (x['id'], x['q'])] + ['    - %s%s' % (op, ' (default)' if i == x.get('def') else '') for i, op in enumerate(x['options'])] + ([('    - Why the default: ' + x['why'])] if x.get('why') else [])
o += ['', '## Open issues', '']
for x in d['issues']:
    if x.get('open'):
        o.append('- **%s** [%s] %s' % (x['id'], x.get('sev', ''), x['title']))
        if x.get('note'): o.append('    - ' + x['note'][:600].replace('\n', ' '))
        o += ['    - [%s] %s' % ('x' if s.get('done') else ' ', s['text']) for s in x.get('subs', [])]
o += ['', '## Steps not done', '']
for x in d['steps']:
    if x['status'] != 'done':
        o.append('- **%s** (%s%s) %s' % (x['id'], x['status'], ', ' + x['priority'] + ' priority' if x.get('priority') else '', x['title'].split(' · ', 1)[-1]))
        if x.get('note'): o.append('    - ' + x['note'][:500].replace('\n', ' '))
open(sys.argv[2], 'w').write('\n'.join(o) + '\n')
