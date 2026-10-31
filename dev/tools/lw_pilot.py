#!/usr/bin/env python3
"""S14 study L, the cost-of-living line weighted and current: the pilot's tables (dev/reports/lw-weighted-line.md, section 6).

Usage: python3 dev/tools/lw_pilot.py <results folder, e.g. compassionism-sim-results/pilot-l-ENGINE> <out dir>
Writes <out dir>/tables.md and <out dir>/estimates.csv. Pilot figures (labelled pilot), not headline figures.

Method (research-update prereg/2026-11-lw-weighted-line.md, Analysis and Decision rules): per-seed paired differences,
averaged over seeds; 95% percentile intervals from a paired bootstrap over seeds, 10,000 replicates, random seed 20261101,
one resample of seed indices shared by every row and line (so every contrast is paired). Contrasts:
  (a) none at ext or bea minus none at base (the line's effect on the no-programme world);
  (b) main and c22 minus none, at each line (the programme's effect);
  (c) the difference in differences: (row - none) at ext or bea minus (row - none) at base.
Shares of people below a line are written as reductions in (b) and (c): positive = fewer people below it. In (a) they are
plain differences: positive = more people below it at the higher line.
Rule 1 labels (contrast c, percentage points), applied in the order the preregistration writes them:
  not changed by the line (interval inside +-1), changed by the line (interval excludes 0, |estimate| >= 1),
  small change (interval excludes 0, |estimate| < 1), otherwise unclear.
Cost: (c) is also stated as a percentage of the base row's effect on cost (ratio of seed means, same resample); so is
cumulative inflation. Keys past the run's horizon (year-40 keys in 20-year rows) are never read.
"""
import csv, glob, json, os, sys
import numpy as np

SRC, OUT = sys.argv[1], sys.argv[2]
NB, BSEED = 10000, 20261101
ENVS = [('ref', 'Reference'), ('adv', 'Adverse'), ('st', 'Stress Test')]
LINES = [('base', '$49,370 (current, unweighted mean)'), ('ext', '$51,201 (ext)'), ('bea', '$51,838 (bea)')]
ROWS = [('main', 'release row ($1,200, opt-in)'), ('c22', 'C2.2 design (automatic, all, needs level, needs-indexed)')]
# (label, key per horizon, kind): red = share below a line (points), cost = $ per adult-year, infl = cumulative inflation (points)
PRI = [('Below 30 days of basic living, design-neutral (% adult-years)', {20: 'bNAPy', 40: 'bNAPy'}, 'red'),
       ("Below 30 days of basic living, the design's own reading (% adult-years)", {20: 'bOAPy', 40: 'bOAPy'}, 'red'),
       ('Below the cost of living (% adult-years)', {20: 'fgt0PY', 40: 'fgt0PY'}, 'red'),
       ('Too little wealth at the end, $25,000 line (% adults)', {20: 'ppov_19', 40: 'ppov_39'}, 'red'),
       ('Programme cost ($ per adult-year)', {20: 'cost', 40: 'cost'}, 'cost'),
       ('Cumulative inflation (% to the last year)', {20: 'plv_19', 40: 'plv_39'}, 'infl')]
OWN = [('Too little wealth, household reading (% adult-years)', 'hhWlthPY', 'red'),
       ('Too little wealth at the end, household reading (% households)', 'hhWlthEnd', 'red'),
       ('Households below their cost of living (% household-years)', 'hhCostPY', 'red'),
       ('Children below the cost of living (% child-years)', 'hhCostKidPY', 'red'),
       ('Poverty severity (FGT2)', 'fgt2PY', 'red'),
       ('Below the official poverty line (% household-years)', 'hhFplPY', 'red')]
LEVELS = [('Adult-years receiving the BU (%)', 'buPY'), ('Adult-years the BU covers the C2.2 needs (%)', 'c22PY'),
          ('Mean share of the C2.2 needs covered (%)', 'c22R'), ('Participation in the last year (%)', 'jnP19'),
          ('Non-participants below the cost of living (% of their years)', 'gNonF0'),
          ('Non-participants with too little wealth (%)', 'gNonW'), ('Hours (mean)', 'hrs'),
          ('Gini, disposable income', 'giniD'), ('Gini, wealth', 'eGiniW')]


def load(src):
    rows, meta = {}, None
    for f in sorted(glob.glob(os.path.join(src, 'shard-*.json'))):
        if f.endswith('.timing.json'):
            continue
        d = json.load(open(f))
        meta = meta or d['_meta']
        assert d['_meta']['manifest']['commit'] == meta['manifest']['commit'] and not d['_meta']['manifest']['dirty']
        lo, hi = d['_meta']['seeds']
        for r, v in d['rows'].items():
            for k, a in v.items():
                assert len(a) == hi - lo + 1
                rows.setdefault(r, {}).setdefault(k, {})
                for i, x in enumerate(a):
                    assert lo + i not in rows[r][k], 'seed covered twice'
                    rows[r][k][lo + i] = x
    s = sorted(next(iter(next(iter(rows.values())).values())).keys())
    out = {r: {k: np.array([v[k][q] for q in s], dtype=float) for k in v} for r, v in rows.items()}
    return out, s, meta


R, SEEDS, META = load(SRC)
RUN = open(os.path.join(SRC, 'run.txt')).read().splitlines() if os.path.exists(os.path.join(SRC, 'run.txt')) else []
CMD = next((l.split(': ', 1)[1].split('   (')[0] for l in RUN if l.startswith('command per shard')), META['command'])
N = len(SEEDS)
assert SEEDS == list(range(SEEDS[0], SEEDS[0] + N)), 'seeds are not one contiguous range'
IDX = np.random.default_rng(BSEED).integers(0, N, size=(NB, N))


def est(x):
    m = x[IDX].mean(axis=1)
    return float(x.mean()), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def pct(num, den):
    """100 * mean(num) / mean(den), with its interval from the same resample."""
    b = 100 * num[IDX].mean(axis=1) / den[IDX].mean(axis=1)
    return float(100 * num.mean() / den.mean()), float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))


def val(row, key, kind):
    v = row[key]
    return (v - 1) * 100 if kind == 'infl' else v


def eff(x, none, key, kind):
    """Row minus none, as a reduction for shares below a line."""
    d = val(x, key, kind) - val(none, key, kind)
    return -d if kind == 'red' else d


def label(e):
    m, lo, hi = e
    if lo > -1 and hi < 1:
        return 'not changed'
    if lo > 0 or hi < 0:
        return 'changed' if abs(m) >= 1 else 'small change'
    return 'unclear'


def fmt(e, dp=1, money=False):
    m, lo, hi = e
    if money:
        return '%s (%s to %s)' % tuple(format(round(z), ',') for z in (m, lo, hi))
    return '%.*f (%.*f to %.*f)' % (dp, m, dp, lo, dp, hi)


def big(e):
    """Cumulative inflation runs to millions of points; print it with thousands separators, no decimals."""
    return fmt(e, money=True) if max(abs(z) for z in e) >= 1000 else fmt(e)


def sig(e):
    return e[1] > 0 or e[2] < 0


def ns(e):
    return '' if sig(e) else ' ns'


CSV, MD, SUM = [], [], []
MD.append('# The cost-of-living line, weighted and current: pilot tables (S14, study L)\n')
MD.append('PILOT: seeds %d-%d (%d seeds), 500 adults, CPS earnings yardstick, octave raise off. Engine %s; command per shard `%s` '
          '(compassionism-sim-results `pilot-l-%s`). Written by `dev/tools/lw_pilot.py`. 95%% paired bootstrap intervals in brackets; '
          '"ns": the interval includes zero. Preregistration: research-update `prereg/2026-11-lw-weighted-line.md`.\n'
          % (SEEDS[0], SEEDS[-1], N, META['manifest']['commit'][:7], CMD,
             META['manifest']['commit'][:7]))
MD.append('Lines: ' + '; '.join('%s %s' % (k, l) for k, l in LINES) + '. C2.2 needs level (BU, $ a month): '
          + ', '.join('%s %s' % (x['line'], format(x['needsBU'], ',.2f')) for x in META['lines']) + '.\n')
for yr in (20, 40):
    for e, elab in ENVS:
        pre = '%s.n500.y%d.' % (e, yr)
        g = lambda line, row: R[pre + line + '.' + row]
        headline = (e, yr) == ('ref', 20)
        MD.append('\n## %s, %d years%s\n' % (elab, yr, ' (headline cell)' if headline else ''))
        # levels of the primary outcomes, every row and line
        MD.append('\n### Levels\n\n| Line | Row | ' + ' | '.join(l for l, _, _ in PRI) + ' |\n|' + '---|' * (len(PRI) + 2))
        for line, llab in LINES:
            for row, rlab in [('none', 'no programme')] + ROWS:
                x = g(line, row); cells = []
                for l, kk, kind in PRI:
                    k = kk[yr]; q = est(val(x, k, kind)); CSV.append([e, yr, line, row, 'level', k, *q])
                    cells.append(fmt(q, 0, True) if kind == 'cost' else big(q))
                MD.append('| %s | %s | %s |' % (line, rlab, ' | '.join(cells)))
        MD.append('\n### Levels: this study\'s own and secondary outcomes\n\n| Line | Row | ' + ' | '.join(l for l, _, _ in OWN) + ' |\n|' + '---|' * (len(OWN) + 2))
        for line, llab in LINES:
            for row, rlab in [('none', 'no programme')] + ROWS:
                x = g(line, row); cells = []
                for l, k, kind in OWN:
                    q = est(x[k]); CSV.append([e, yr, line, row, 'level', k, *q]); cells.append(fmt(q, 2 if k == 'fgt2PY' else 1))
                MD.append('| %s | %s | %s |' % (line, rlab, ' | '.join(cells)))
        # (a) the no-programme world at the higher lines
        MD.append('\n### (a) No programme: the higher line minus the current line (positive = more people below the line)\n\n| Line | '
                  + ' | '.join(l for l, _, k in PRI if k != 'cost') + ' | ' + ' | '.join(l for l, _, _ in OWN) + ' |\n|'
                  + '---|' * (len(PRI) + len(OWN)))
        for line, _ in LINES[1:]:
            cells = []
            for l, kk, kind in PRI:
                if kind == 'cost':
                    continue
                k = kk[yr]; q = est(val(g(line, 'none'), k, kind) - val(g('base', 'none'), k, kind))
                CSV.append([e, yr, line, 'none', 'a: vs base', k, *q]); cells.append(big(q) + ns(q))
            for l, k, kind in OWN:
                q = est(g(line, 'none')[k] - g('base', 'none')[k]); CSV.append([e, yr, line, 'none', 'a: vs base', k, *q])
                cells.append(fmt(q, 2 if k == 'fgt2PY' else 1) + ns(q))
            MD.append('| %s | %s |' % (line, ' | '.join(cells)))
        # (b) effects against no programme, at each line
        MD.append('\n### (b) Programme against no programme, at each line (shares: reductions, positive = fewer below)\n\n| Row | Line | '
                  + ' | '.join(l for l, _, _ in PRI) + ' | ' + ' | '.join(l for l, _, _ in OWN) + ' |\n|' + '---|' * (len(PRI) + len(OWN) + 2))
        for row, rlab in ROWS:
            for line, _ in LINES:
                cells = []
                for l, kk, kind in PRI:
                    k = kk[yr]; q = est(eff(g(line, row), g(line, 'none'), k, kind))
                    CSV.append([e, yr, line, row, 'b: vs none', k, *q])
                    cells.append((fmt(q, 0, True) if kind == 'cost' else big(q)) + ns(q))
                for l, k, kind in OWN:
                    q = est(eff(g(line, row), g(line, 'none'), k, kind)); CSV.append([e, yr, line, row, 'b: vs none', k, *q])
                    cells.append(fmt(q, 2 if k == 'fgt2PY' else 1) + ns(q))
                MD.append('| %s | %s | %s |' % (rlab, line, ' | '.join(cells)))
        # (c) difference in differences, with rule 1 labels
        MD.append('\n### (c) Does the effect depend on the line? (row - none) at the higher line minus (row - none) at the current line, rule 1 label\n\n'
                  '| Row | Line | ' + ' | '.join(l for l, _, _ in PRI) + ' | Cost: effect as % of the base effect | Inflation: as % of the base effect |\n|'
                  + '---|' * (len(PRI) + 4))
        for row, rlab in ROWS:
            for line, _ in LINES[1:]:
                cells, labs = [], {}
                for l, kk, kind in PRI:
                    k = kk[yr]
                    d = eff(g(line, row), g(line, 'none'), k, kind) - eff(g('base', row), g('base', 'none'), k, kind)
                    q = est(d); CSV.append([e, yr, line, row, 'c: did vs base', k, *q])
                    if kind == 'cost':
                        cells.append(fmt(q, 0, True) + ns(q))
                    else:
                        lab = label(q); labs[k] = lab; CSV.append([e, yr, line, row, 'c: rule 1', k, lab, '', ''])
                        cells.append('%s, *%s*' % (big(q), lab))
                extra = []
                for kind in ('cost', 'infl'):
                    k = [kk[yr] for _, kk, kd in PRI if kd == kind][0]
                    q = pct(eff(g(line, row), g(line, 'none'), k, kind), eff(g('base', row), g('base', 'none'), k, kind))
                    CSV.append([e, yr, line, row, 'c: %% of base effect', k, *q]); extra.append(fmt(q))
                MD.append('| %s | %s | %s | %s |' % (rlab, line, ' | '.join(cells), ' | '.join(extra)))
                SUM.append((elab, yr, row, line, labs))
        # line-following own outcomes, DiD
        MD.append('\n### (c) for this study\'s own and secondary outcomes (reductions; rule 1 label)\n\n| Row | Line | '
                  + ' | '.join(l for l, _, _ in OWN) + ' |\n|' + '---|' * (len(OWN) + 2))
        for row, rlab in ROWS:
            for line, _ in LINES[1:]:
                cells = []
                for l, k, kind in OWN:
                    q = est(eff(g(line, row), g(line, 'none'), k, kind) - eff(g('base', row), g('base', 'none'), k, kind))
                    CSV.append([e, yr, line, row, 'c: did vs base', k, *q])
                    cells.append('%s, *%s*' % (fmt(q, 2 if k == 'fgt2PY' else 1), label(q)))
                MD.append('| %s | %s | %s |' % (rlab, line, ' | '.join(cells)))
        # coverage, participation, distribution levels
        MD.append('\n### Coverage, participation and distribution (levels)\n\n| Line | Row | ' + ' | '.join(l for l, _ in LEVELS) + ' |\n|' + '---|' * (len(LEVELS) + 2))
        for line, _ in LINES:
            for row, rlab in [('none', 'no programme')] + ROWS:
                x = g(line, row); cells = []
                for l, k in LEVELS:
                    if row == 'none' and k in ('jnP19', 'gNonF0', 'gNonW'):
                        cells.append('n/a'); continue  # 0 by construction with no programme, not a value
                    q = est(x[k]); CSV.append([e, yr, line, row, 'level', k, *q])
                    cells.append(fmt(q, 3 if k.startswith('gini') or k == 'eGiniW' else 1))
                MD.append('| %s | %s | %s |' % (line, rlab, ' | '.join(cells)))

# rule 1 summary over every cell, primary shares and inflation
SHARE = [kk for _, kk, kind in PRI if kind != 'cost']
MD.insert(3, '\n## Rule 1 summary: every cell (primary outcomes, difference in differences)\n\nColumns: basic living (design-neutral, design reading), '
          'cost of living, wealth at the end ($25,000), cumulative inflation.\n\n| Environment | Years | Row | Line | bNAPy | bOAPy | fgt0PY | wealth | inflation |\n|'
          + '---|' * 9 + '\n' + '\n'.join('| %s | %d | %s | %s | %s |' % (el, yr, row, line, ' | '.join(labs[kk[yr]] for kk in SHARE))
                                          for el, yr, row, line, labs in SUM) + '\n')
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'tables.md'), 'w').write('\n'.join(MD) + '\n')
with open(os.path.join(OUT, 'estimates.csv'), 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['env', 'years', 'line', 'row', 'contrast', 'key', 'mean', 'lo95', 'hi95']); w.writerows(CSV)
print('wrote %s (%d estimates, %d seeds)' % (OUT, len(CSV), N))
