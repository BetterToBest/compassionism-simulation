"""Headline figures of the current release, each with the file and key it comes from, for the CoMSES and fact-sheet packet.
Usage: python3 -I dev/packets/make_release_summary.py data/releases/v5.6.json > release-summary.json"""
import json, sys
f = sys.argv[1]; d = json.load(open(f)); out = {'file': f, 'version': d['version'], 'date': d['date'], 'seeds': d['meta']['seeds'], 'agents': d['meta']['agents'], 'figures': []}
what = {'fgt0PY': 'share of adult-years below the cost of living (%)', 'bOAPy': 'share of adult-years below 30 days of basic living (%)', 'pov': 'share of adults with too little wealth at year 20 (%)',
        'cost': 'programme cost per adult per year (year-0 dollars)', 'hrs': 'change in hours worked (%)', 'part19': 'share of adults enrolled by year 20 (%)',
        'dF0': 'change, below the cost of living (points; negative is better)', 'dBO': 'change, below 30 days of basic living (points)', 'dPov': 'change, too little wealth (points)'}
for env, E in d['panels']['20']['envs'].items():
    for src, row, tag in (('base', E['base'], 'no program'), ('rows.release', E['rows']['release'], 'Compassionism (main reading)')):
        for k, w in what.items():
            if k in row and not isinstance(row[k], (dict, list)):
                out['figures'].append({'environment': env, 'arm': tag, 'what': w, 'value': row[k], 'source': '%s: panels.20.envs.%s.%s.%s' % (f, env, src, k)})
            elif k in row and isinstance(row[k], list):
                out['figures'].append({'environment': env, 'arm': tag, 'what': w + ' [value, low, high of 95% interval]', 'value': row[k], 'source': '%s: panels.20.envs.%s.%s.%s' % (f, env, src, k)})
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
