#!/usr/bin/env python3
"""S47 (Nov 6, 2026): the loader of the study batch's programme-job folders (compassionism-sim-results runner/jobs/program.js: studies A to J
and R), for the consumers that read them after the batch (S36 synergy tables, S38 community layer, S5 participation, S7 release panel, S39).

  python3 dev/tools/batch_load.py FOLDER [FOLDER ...] [--check]

FOLDER is a run-study folder (prog-<study>-<engine>/ or the dry run's dry-<study>-<engine>/). load() returns, per row, a dict key -> numpy
array over seeds (seeds in order across shards), with `null` read as NaN. Row names are `ENV.nN.yY.DESIGN.YARD.ROW[.READING]` (DESIGN `c22`
or `rls`) for studies A to J and `ENV.n500.yY.YARD.ENGINE.DESIGN[.READING]` for R. by_design() returns one design's rows under the pilots'
names (`ENV.nN.yY.YARD.ROW...`), so the pilot scripts' tables (pilot_studies.py, main_table's prefix) read the batch with only a folder change.

--check confirms what the consumers rely on, and exits 1 if any fails:
- the shards cover one contiguous seed range, every shard records the same engine commit, every row has every seed;
- every environment holds the same row list (paired rows);
- every row name parses, and its horizon is 20 or 40;
- the primary outcomes of the study programme (prereg/2026-11-study-program.md: bNAPy, bOAPy, fgt0PY, cost, ppov_19 and plv_19, and
  ppov_39 and plv_39 in 40-year rows) are present and finite in every row;
- keys past a row's horizon are null (S35 report section 9 item 2: never 0).
It prints, per folder, the row counts and the keys that hold nulls (allowed where the job writes them: participation keys on no-programme
rows, ageing keys without ageing, octMean without CCO, keys a row's switches do not report).
"""
import glob, gzip, json, os, re, sys
import numpy as np

PRIMARY = ['bNAPy', 'bOAPy', 'fgt0PY', 'cost', 'ppov_19', 'plv_19']
PRIMARY40 = ['ppov_39', 'plv_39']
NAME = re.compile(r'^(ref|adv|st)\.n(\d+)\.y(\d+)\.(.+)$')


def load(folder):
    # S48: shards over 100 MB are stored gzip-compressed (shard-NNNN.json.gz)
    fs = sorted(f for f in glob.glob(os.path.join(folder, 'shard-*.json')) + glob.glob(os.path.join(folder, 'shard-*.json.gz')) if not f.endswith('.timing.json'))
    if not fs: sys.exit('no shard files in ' + folder)
    parts = sorted((json.load(gzip.open(f, 'rt') if f.endswith('.gz') else open(f)) for f in fs), key=lambda p: p['_meta']['seeds'][0])
    prob, seeds = [], []
    for p in parts:
        lo, hi = p['_meta']['seeds']
        if seeds and lo != seeds[-1] + 1: prob.append('seed gap before %d' % lo)
        seeds += list(range(lo, hi + 1))
    eng = {json.dumps(p['_meta'].get('manifest', {}).get('commit', p['_meta'].get('engine'))) for p in parts}
    if len(eng) != 1: prob.append('shards from %d engine commits' % len(eng))
    rows = {}
    for r in parts[0]['rows']:
        if any(r not in p['rows'] for p in parts): prob.append('row %s missing from a shard' % r); continue
        rows[r] = {k: np.array([np.nan if x is None else x for x in sum((p['rows'][r].get(k, [None]*(p['_meta']['seeds'][1] - p['_meta']['seeds'][0] + 1)) for p in parts), [])], dtype=float)
                   for k in parts[0]['rows'][r]}
    meta = dict(parts[0]['_meta']); meta['seedList'] = seeds; meta['_problems'] = prob
    return rows, meta


def horizon(r):
    m = NAME.match(r)
    return int(m.group(3)) if m else None


def by_design(rows, design):
    """One design's rows (`c22` or `rls`) under the pilots' names: ENV.nN.yY.DESIGN.REST -> ENV.nN.yY.REST (studies A to J)."""
    out = {}
    for r, v in rows.items():
        p = r.split('.')
        if len(p) > 4 and p[3] == design: out['.'.join(p[:3] + p[4:])] = v
    return out


def check(folder, rows, meta):
    prob = list(meta['_problems'])
    n = len(meta['seedList'])
    lens = {len(x) for v in rows.values() for x in v.values()}
    if lens != {n}: prob.append('seed counts %s, expected %d' % (sorted(lens), n))
    envs = {}
    for r in rows:
        m = NAME.match(r)
        if not m: prob.append('row name does not parse: ' + r); continue
        envs.setdefault(m.group(1), set()).add(r.split('.', 1)[1])
    if len({frozenset(s) for s in envs.values()}) > 1: prob.append('environments hold different row lists')
    bad, past = [], []
    for r, v in rows.items():
        y = horizon(r)
        if y not in (20, 40): prob.append('row %s: horizon %s' % (r, y)); continue
        for k in PRIMARY + (PRIMARY40 if y == 40 else []):
            if k not in v or not np.all(np.isfinite(v[k])): bad.append((r, k))
        for k, x in v.items():
            t = re.search(r'_(\d+)$', k)
            if t and int(t.group(1)) >= y and k[:-len(t.group(0))] in ('ppov', 'plv') and not np.all(np.isnan(x)): past.append((r, k))
    if bad: prob.append('%d primary cells missing or not finite (%s)' % (len(bad), ', '.join('%s %s' % b for b in bad[:4])))
    if past: prob.append('%d keys past the horizon are not null (%s)' % (len(past), ', '.join('%s %s' % b for b in past[:4])))
    nulls = sorted({k for v in rows.values() for k, x in v.items() if np.any(np.isnan(x))})
    per = {e: len(s) for e, s in sorted(envs.items())}
    print(('PASS' if not prob else 'FAIL') + '  batch_load.py %s: %s rows per environment, seeds %d-%d, %d keys with nulls%s' % (
        os.path.basename(os.path.normpath(folder)), '/'.join('%s %d' % kv for kv in per.items()), meta['seedList'][0], meta['seedList'][-1], len(nulls),
        ('; ' + '; '.join(prob)) if prob else ''))
    return not prob


def main():
    a = sys.argv[1:]
    folders = [x for x in a if not x.startswith('--')]
    if not folders: sys.exit(__doc__)
    ok = True
    for f in folders:
        rows, meta = load(f)
        if '--check' in a: ok &= check(f, rows, meta)
        else: print('%s: %d rows, seeds %d-%d' % (f, len(rows), meta['seedList'][0], meta['seedList'][-1]))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
