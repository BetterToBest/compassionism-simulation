"""S7 part 1 (Nov 15, 2026): write one data file per preregistered study of the programme into data/studies/, copied from the study's own tables.

Usage: python3 dev/tools/study_files.py            writes data/studies/<id>.json for every study below
       python3 dev/tools/study_files.py --check    exits 1 if any file is not what this script writes from dev/runs/

Nothing is recomputed: each file holds the study's estimates.csv (S36, S38, S5, S55, S6, S14) or its three per-environment result files (S34) as they are,
as columns (one list per CSV column; an empty CSV cell is null, any other numeric cell is the number the CSV prints). "meta" names the study, the report that
reads it, the engine commit, the seeds, and the SHA-256 of every source file, so a reader can tie the data to the sim-results folder it came from.
The findings page (S7 part 2) prints these figures through site/findings.js; no number is typed into a page.
"""
import csv, hashlib, json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUTDIR = os.path.join(ROOT, 'data', 'studies')

# id: (title, preregistration, report, source folder under dev/runs, engine commit, seeds, what the rows are, results folder in compassionism-sim-results)
CSV_STUDIES = {
    's36-synergy': ('Synergy report (S36): Shapley shares and interactions of the design’s five parts, 20 and 40 years',
                    'prereg/2026-11-study-program.md', 'dev/reports/s36-synergy.md', 's36-synergy', 'ce8d030b8d16a752706c4ea2db71196e11e73831', 500,
                    'full batch, studies B (500 adults) and B10 (10,000 adults)', 'prog-b-ce8d030, prog-b10-ce8d030'),
    's38-layer': ('Community-layer report (S38): what the community and zone layer changes',
                  'prereg/2026-11-community-layer.md', 'dev/reports/s38-community-layer.md', 's38-layer', 'ce8d030b8d16a752706c4ea2db71196e11e73831', 500,
                  'full batch, studies G, G10 and the layer rows', 'prog-g-ce8d030, prog-g10-ce8d030'),
    's5-participation': ('Participation threshold (S5): outcomes by participation level, with each level’s departure from a straight line',
                         'prereg/2026-11-study-program.md', 'dev/reports/s5-participation.md', 's5-participation', 'ce8d030b8d16a752706c4ea2db71196e11e73831', 500,
                         'full batch, studies D (500 adults) and D10 (10,000 adults)', 'prog-d-ce8d030, prog-d10-ce8d030'),
    's55-open-access': ('Open PTF access (S55): anyone may buy at PTF prices, against members only',
                        'prereg/2026-11-ptf-access-addendum.md', 'dev/reports/s55-open-access.md', 's55-open-access', '0c93593e1ea502555387e42215b79f290a60f127', 500,
                        'full 500-seed runs, studies T-Y, paired with the frozen batch', 'prog-t-0c93593, prog-u-0c93593, prog-u10-0c93593, prog-v-0c93593, prog-v10-0c93593, prog-vj-0c93593, prog-w-0c93593, prog-w10-0c93593, prog-y-0c93593'),
    's6-c22-pilot': ('C2.2 coverage and adequacy (S6): pilot cells',
                     'prereg/2026-11-c22-coverage-adequacy.md', 'dev/reports/c22-coverage-adequacy.md', 'c22-pilot', '395dd5b', 100,
                     'PILOT (100 seeds, 500 adults); the frozen C2.2 panel itself is release-panel-frozen.json', 'pilot-k-395dd5b'),
    's14-lw-pilot': ('Cost-of-living line weighted by where people live (S14): pilot cells',
                     'prereg/2026-11-lw-weighted-line.md', 'dev/reports/lw-weighted-line.md', 'lw-pilot', 'f66dc67', None,
                     'PILOT (study L)', 'pilot-l-f66dc67'),
}
S34 = ('The no-program baseline against outside data (S34)', 'prereg/s34-baseline-realism.md', 'dev/reports/baseline-realism.md', 'baseline-realism')
ENVS = ['ref', 'adv', 'st']


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def cell(s):
    if s == '':
        return None
    try:
        return int(s) if s.lstrip('-').isdigit() else float(s)
    except ValueError:
        return s


def csv_file(sid):
    title, pre, rep, folder, eng, seeds, rows, res = CSV_STUDIES[sid]
    p = os.path.join('dev', 'runs', folder, 'estimates.csv')
    with open(os.path.join(ROOT, p), newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        head = next(r)
        cols = [[] for _ in head]
        n = 0
        for row in r:
            if len(row) != len(head):
                sys.exit('study_files: %s row %d has %d cells, expected %d' % (p, n + 2, len(row), len(head)))
            for i, v in enumerate(row):
                cols[i].append(cell(v))
            n += 1
    return {'meta': {'id': sid, 'title': title, 'prereg': pre, 'report': rep, 'engine': eng, 'seeds': seeds, 'rows': rows,
                     'resultsFolders': res, 'resultsRepo': 'BetterToBest/compassionism-sim-results', 'source': {p: sha(os.path.join(ROOT, p))},
                     'intervals': '95% paired-bootstrap intervals over seeds as the report states', 'n': n},
            'columns': head, 'data': cols}


def s34_file():
    title, pre, rep, folder = S34
    src, out = {}, {'meta': None, 'envs': {}}
    for e in ENVS:
        p = os.path.join('dev', 'runs', folder, 'baseline-realism-%s.json' % e)
        with open(os.path.join(ROOT, p), encoding='utf-8') as f:
            d = json.load(f)
        src[p] = sha(os.path.join(ROOT, p))
        out['envs'][e] = {'meta': d['_meta'], 'rows': d['rows']}
    m = out['envs']['ref']['meta']
    out['meta'] = {'id': 's34-baseline', 'title': title, 'prereg': pre, 'report': rep, 'engine': m['manifest']['commit'], 'seeds': m['seeds'],
                   'rows': 'the release no-programme run against outside data, three environments', 'resultsFolders': '(run on the session machine; files here are the record)',
                   'source': src}
    return out


def build():
    out = {sid: csv_file(sid) for sid in CSV_STUDIES}
    out['s34-baseline'] = s34_file()
    return out


def dump(d):
    return json.dumps(d, separators=(',', ':'), ensure_ascii=False) + '\n'


def main():
    files = build()
    bad = 0
    for sid, d in files.items():
        p = os.path.join(OUTDIR, sid + '.json')
        s = dump(d)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != s:
                print('study_files.py --check: %s is not what the generator writes' % p); bad = 1
        else:
            with open(p, 'w', encoding='utf-8') as f:
                f.write(s)
            print('wrote %s (%d bytes)' % (p, len(s.encode())))
    if '--check' in sys.argv:
        if bad: sys.exit(1)
        print('study_files.py --check: all %d files are what the generator writes' % len(files))


main()
