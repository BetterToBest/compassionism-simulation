#!/usr/bin/env python3
"""S54 (Nov 5, 2026): the analysis of the policy-levers study (study N), exactly as preregistered (research-update
prereg/2026-11-levers-addendum.md: Outcomes, Analysis, Decision rules). Written and committed before any result of the study was read.

  python3 dev/tools/s54_levers.py --s1 STAGE1 [--s2 STAGE2] [--s3 STAGE3 --list LIST] [--out FILE] [--csv DIR] [--select LIST] [--reps 2000] [--check]

STAGEn is a run-study folder of compassionism-sim-results (s54-levers1-<engine>/, s54-levers2-<engine>/, stage 3's folder) or one shard file.
  --out FILE     the tables in Markdown (default: standard output)
  --csv DIR      every cell as CSV: stage1-effects.csv, stage2-effects.csv (and stage3-effects.csv)
  --select LIST  write stage 3's settings (decision rule 4 and the Pareto front, chosen on these seeds) as JSON, for runner/jobs/levers.js --stage=3
  --list LIST    with --s3: the settings file stage 3 ran (the confirmation tests of decision rule 5)
  --check        only confirm the files are complete: checksums, row counts, every key present, the seeds contiguous and equal; exits

What it computes (the addendum's words, then how):
- Every outcome: a row's seed mean minus its own no-programme row on the same seeds (programme effect), and a lever row minus its design's
  comparison row (lever effect): `base` for the test reading's levers and for `asis` (the joining reading's own effect), `asis` for today's
  rule's tax sweep (`asis.tNN`), and `base.sv` for the `.sv` twins (the second savings reading, against `none.sv`). The protected accounts
  (`sva`, `svc`) are compared with `base` and `none` (ordinary savings): the account is the programme's, the no-programme world has none.
  Programme inflation is `endoAnn`'s change against the no-programme row, shown in points a year (the no-programme row's own level is in the CSV).
  Participation and the Source's keys (`lv*`) exist only on programme rows: the no-programme row counts as 0 there.
- 95% intervals: paired bootstrap over seeds, 2,000 replicates, resampler seed 54 (Python's random.Random(54).randrange, as S53's script),
  the same resample for every cell; percentiles with linear interpolation.
- Decision rule 1 (what a lever does), per design, wage and outcome with a favourable direction: works where the lever effect's interval
  excludes zero in the favourable direction in all three environments; harms where it excludes zero in the unfavourable direction in any
  environment; otherwise does not move.
- Q21 (decision rules 2, 3): the three break-even tax rates per design, wage, environment and joining reading (test: tNN and base; today's
  rule: asis.tNN and asis). Self-funding: the lowest rate at which the seed-mean net new money (lvU) is at or below zero, by linear
  interpolation between grid rates. Lowest basket poverty: the grid rate with the lowest seed-mean basket poverty. Deterrence: the lowest rate
  above the released rate (12%; 18% in Stress) at which mean participation (lvJm) is 5 points or more below its level at the released rate
  (the base or asis row), by linear interpolation from the released rate. Intervals: the 2.5th-97.5th percentiles of the same statistic over
  the replicates, a replicate that never reaches it counting as beyond 40%; with the share of replicates that reach it.
- Morris (descriptive): elementary effects on the [0, 1] factor scale (the change in the seed mean over a step of 2/3, divided by 2/3) of each
  factor on the four objectives, per design and environment, at wages 100%: mean absolute effect (mu*), mean (mu), spread (sd, n - 1).
- Pareto front per design and wage: candidates are every stage-1 programme row under the test reading on ordinary savings (not `asis*`, not
  `.sv`) and every stage-2 programme row; objectives are the mean over the three environments of basket poverty (lower), wealth poverty
  (lower), participation (higher) and programme inflation (lower). Candidates with identical objectives are one point (the first listed
  stands for it). Fronts per environment are published beside it.
- Decision rule 4 (the best setting): among the same candidates, (a) in every environment the mean change against no programme of gNonF0,
  gNonW, secU25X, secM3X and pov is at or below zero; (b) in every environment programme inflation is under 5% a year; (c) the lowest mean
  basket poverty over the three environments (ties: the first listed). If none passes (a) and (b): the five closest, by the sum over
  environments of each failing measure's excess in points, with what fails.
- Decision rule 5 (stage 3): a setting is confirmed if in every environment basket poverty's interval lies below zero, each no-harm measure's
  interval has its upper end at or below +0.5 points, and programme inflation's upper end is under 5% a year (required for the chosen
  setting; reported for Pareto points). The chosen setting's `.sv` twin and today's-rule run are tested and reported the same way.
Needs numpy."""
import json, os, sys, glob, random, math, hashlib
import numpy as np

ENVS = ['ref', 'adv', 'st']; ENVL = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
DES = ['rel', 'c22']; DESL = {'rel': 'release row', 'c22': 'C2.2 design'}; WAGES = [100, 90]
TAX = [0, 4, 8, 12, 16, 20, 25, 30, 40]; TREL = {'ref': 12, 'adv': 12, 'st': 18}   # the released base tax (addendum, Q21 3)
PREREG = {1: 520, 2: 1164}
# key: (plain label, favourable direction: -1 lower is better, +1 higher is better, 0 reported only; display scale)
KEYS = {
    'fgt0PY': ('basket poverty, % of adult-years', -1, 1), 'pov': ('wealth poverty at year 20, %', -1, 1),
    'gNonF0': ("non-participants' basket poverty, %", -1, 1), 'endoAnn': ('programme inflation, points a year', -1, 100),
    'lvJm': ('participation, mean of years 1-19, %', 1, 1), 'lvJ1': ('participation at year 1, %', 1, 1),
    'lvJ7': ('participation at year 7, %', 1, 1), 'lvJ19': ('participation at year 19, %', 1, 1),
    'bOAPy': ('below 30 days of basic living, % of adult-years', -1, 1), 'bNAPy': ('below 30 days of basic living, design-neutral, %', -1, 1),
    'gNonW': ("non-participants' wealth poverty, %", -1, 1), 'gPartF0': ("participants' basket poverty, %", -1, 1),
    'gPartW': ("participants' wealth poverty, %", -1, 1), 'pLev20': ('price level at year 20', 0, 1), 'cost': ('cost per adult', 0, 1),
    'giniD': ('income Gini', -1, 1), 'medWealthReal': ('median real wealth', 1, 1), 'emp': ('employment, %', 0, 1), 'hrs': ('hours (change)', 0, 1),
    'fgt2PY': ('FGT2 (never alone)', -1, 1), 'lvU': ("the Source's net new money, % of earned income", 0, 1),
    'lvP': ("the Source's payout before backing, % of earned income", 0, 1), 'lvBk': ('payout backed or retired, %', 0, 1),
    'lvKp': ('project sales kept, % of earned income', 0, 1), 'lvSv': ('protected-account interest, % of earned income', 0, 1),
    'lvQ': ('mean premium factor (1 = full rates)', 0, 1), 'lvCap': ('years the issuance cap was met, %', 0, 1),
    'secU25A': ('income drop 25%+ with no buffer, all adults, per 100 adult-years', -1, 1),
    'secU25P': ('income drop 25%+ with no buffer, participants, per 100', -1, 1),
    'secU25X': ("non-participants' income drops of 25%+ with no buffer, per 100", -1, 1),
    'secM3A': ('under 3 months of basics covered, all adults, %', -1, 1), 'secM3P': ('under 3 months of basics covered, participants, %', -1, 1),
    'secM3X': ("non-participants under 3 months of basics covered, %", -1, 1)}
PRIMARY = ['fgt0PY', 'pov', 'gNonF0', 'endoAnn', 'lvJm']
MATRIX = PRIMARY + ['gNonW', 'secU25X', 'secM3X', 'bNAPy']
NOHARM = ['gNonF0', 'gNonW', 'secU25X', 'secM3X', 'pov']
OBJ = [('fgt0PY', 'basket poverty', -1), ('pov', 'wealth poverty', -1), ('lvJm', 'participation', 1), ('endoAnn', 'inflation', -1)]
LV0 = lambda k: k.startswith('lv')   # keys absent on no-programme rows (0 there)

# Stage 2's factors, as runner/jobs/levers.js maps u in [0, 1] to a setting (for the plain description of each point)
lvl = lambda u, n: min(n - 1, int(math.floor(u*n)))
FACT = [('tax', 'base tax', lambda u: '%.0f%%' % (40*u)), ('pr', 'progression', lambda u: '%.1f pts' % (8*u)), ('pc', 'cap', lambda u: '%.0f%%' % (50 + 25*u)),
        ('bt', 'business tax', lambda u: '%.0f%%' % (75*u)), ('keep', 'sales kept', lambda u: '%.0f%%' % (50*u)), ('ex', 'recycled', lambda u: '%.0f%%' % (100*u)),
        ('br', 'business rate', lambda u: '%.1fx' % (1 + 2*u)), ('bu', 'BU', lambda u: '%.0f%%' % (60 + 40*u)), ('mm', 'top multiplier', lambda u: '%.1f' % (3 + 6*u)),
        ('oc', 'octave capacity', lambda u: ['not enforced', '100%', '50%', '25%'][lvl(u, 4)]), ('no', 'octaves', lambda u: '%d' % (2 + lvl(u, 5))),
        ('phi', 'Phi tier', lambda u: ['on', 'off'][lvl(u, 2)]), ('ph', 'phase-in', lambda u: '%d y' % int(math.floor(1 + 9*u + 0.5))),
        ('cap', 'issuance cap', lambda u: ['none', '8%', '4%', '2%'][lvl(u, 4)]), ('ix', 'indexation', lambda u: ['surge', 'every year', 'basic needs'][lvl(u, 3)]),
        ('sv', 'protected account', lambda u: ['none', 'first $10,000', 'all savings'][lvl(u, 3)]), ('rc', 'rent cap', lambda u: ['off', 'on'][lvl(u, 2)])]
FACTL = {'tax': 'base conversion tax (0-40%)', 'pr': 'progression (0-8 points)', 'pc': 'progression cap (50-75%)', 'bt': 'business base rate (0-75%)',
         'keep': 'project sales kept (0-50%)', 'ex': 'expired BU recycled (0-100%)', 'br': 'business rate (1-3x)', 'bu': 'BU amount (60-100%)',
         'mm': 'top multiplier (3-9)', 'oc': 'octave capacity (none, 100, 50, 25%)', 'no': 'number of octaves (2-6)', 'phi': 'Phi tier (on, off)',
         'ph': 'phase-in (1-10 years)', 'cap': 'issuance cap (none, 8, 4, 2%)', 'ix': 'indexation (surge, yearly, needs)',
         'sv': 'protected account (none, capped, all)', 'rc': 'rent cap (off, on)'}
S1DESC = {'base': 'the design (test reading)', 'asis': "today's joining rule", 'fprog': 'outside finance: progressive income tax',
          'fland': 'outside finance: land-value tax', 'fflat': 'outside finance: flat wage contribution', 'phi0': 'Phi tier off',
          'ixs': 'indexation: surge protocol (5%)', 'ixy': 'indexation: every year, price level', 'ixn': 'indexation: every year, basic needs',
          'sva': 'protected account, all savings', 'svc': 'protected account, first $10,000', 'rcap': 'rent cap for BU tenants',
          'hc': 'rent risk ($1.41 a BU dollar)', 'hcrc': 'rent risk and rent cap'}


def desc1(n):
    import re
    if n in S1DESC: return S1DESC[n]
    for pat, f in [(r'asis\.t(\d+)$', "tax %s%%, today's rule"), (r't(\d+)$', 'tax %s%%'), (r'bt(\d+)$', 'business tax %s%%'), (r'kp(\d+)$', 'Source keeps %s%% of project sales'),
                   (r'ex(\d+)$', '%s%% of expired BU recycled'), (r'bu(\d+)$', '%s%% of the BU'), (r'mm(\d+)$', 'top multiplier %s'), (r'oc(\d+)$', 'octave capacity %s%%'),
                   (r'no(\d+)$', '%s octaves'), (r'ph(\d+)$', 'phase-in over %s years'), (r'cap(\d+)$', 'issuance cap %s%%')]:
        m = re.match(pat, n)
        if m: return f % m.group(1)
    m = re.match(r'pr(\d+)c(\d+)$', n)
    if m: return 'progression %s pts, cap %s%%' % m.groups()
    m = re.match(r'br(\d+)$', n)
    if m: return 'business rate %sx' % {'1': '1', '15': '1.5', '2': '2'}.get(m.group(1), m.group(1))
    return n


def u_of(name, design):
    """The [0, 1] factor vector of a stage-2 row name (hI or mT.S), from the job's design written in the output."""
    if name.startswith('h'): return design['lhs'][int(name[1:])]
    t, s = name[1:].split('.'); return design['morris'][int(t)]['points'][int(s)]


def desc(name, design):
    if design is not None and (name[:1] == 'h' and name[1:].isdigit() or name[:1] == 'm' and '.' in name):
        return '; '.join('%s %s' % (lab, f(u)) for (k, lab, f), u in zip(FACT, u_of(name, design)))
    return desc1(name)


# ---------- loading ----------
def load(path, check_sums=True):
    files = [path] if path.endswith('.json') else sorted(f for f in glob.glob(os.path.join(path, 'shard-*.json')) if not f.endswith('.timing.json'))
    if not files: sys.exit('no shard files in ' + path)
    bad = []
    sums = os.path.join(os.path.dirname(files[0]) if path.endswith('.json') else path, 'SHA256SUMS')
    if check_sums and os.path.exists(sums):
        for line in open(sums):
            h, f = line.split()
            p = os.path.join(os.path.dirname(sums), f)
            if os.path.exists(p) and hashlib.sha256(open(p, 'rb').read()).hexdigest() != h: bad.append(f)
    D = [json.load(open(f)) for f in files]
    D.sort(key=lambda d: d['_meta']['seeds'][0])
    gaps = [(a['_meta']['seeds'], b['_meta']['seeds']) for a, b in zip(D, D[1:]) if b['_meta']['seeds'][0] != a['_meta']['seeds'][1] + 1]
    rows = {}
    for d in D:
        for r, v in d['rows'].items():
            t = rows.setdefault(r, {})
            for k, x in v.items(): t.setdefault(k, []).extend(x)
    rows = {r: {k: np.array(x, dtype=float) for k, x in v.items()} for r, v in rows.items()}
    meta = dict(D[0]['_meta']); meta['seeds'] = [D[0]['_meta']['seeds'][0], D[-1]['_meta']['seeds'][1]]
    meta['_problems'] = (['checksum differs: ' + ', '.join(bad)] if bad else []) + (['seed ranges not contiguous: %s' % gaps[:3]] if gaps else [])
    return rows, meta


def get(rows, r, k, n):
    v = rows[r].get(k)
    if v is None: return np.zeros(n) if LV0(k) else np.full(n, np.nan)
    return v


def check(rows, meta, expect, label):
    prob = list(meta['_problems'])
    for e in ENVS:
        names = [r for r in rows if r.startswith(e + '.')]
        if expect is not None and len(names) != expect: prob.append('%s: %d rows in %s (expected %d)' % (label, len(names), e, expect))
    keys = meta['keys']; n = {len(v) for r in rows.values() for v in r.values()}
    if len(n) != 1: prob.append('seed counts differ: %s' % sorted(n))
    if meta['seeds'][1] - meta['seeds'][0] + 1 not in n: prob.append('seed range %s does not match the values' % meta['seeds'])
    miss = [(r, k) for r in rows for k in keys if k not in rows[r] and not (LV0(k) and '.none' in r)]
    nonf = [(r, k) for r in rows for k, v in rows[r].items() if not np.all(np.isfinite(v))]
    if miss: prob.append('%d missing keys (%s)' % (len(miss), ', '.join('%s %s' % x for x in miss[:4])))
    if nonf: prob.append('%d non-finite cells (%s)' % (len(nonf), ', '.join('%s %s' % x for x in nonf[:4])))
    print(('PASS' if not prob else 'FAIL') + '  s54_levers.py %s: %d rows, %d keys, seeds %d-%d, engine %s%s' % (
        label, len(rows), len(keys), meta['seeds'][0], meta['seeds'][1], meta.get('manifest', {}).get('commit', '?')[:7], ('; ' + '; '.join(prob)) if prob else ''))
    return not prob


# ---------- statistics ----------
def weights(n, reps):
    rng = random.Random(54); W = np.zeros((reps, n))
    for r in range(reps):
        for _ in range(n): W[r, rng.randrange(n)] += 1
    return W/n


def stats(D, W):
    """D: cells x seeds of paired differences -> seed means, 2.5th and 97.5th bootstrap percentiles (the same resample W for every cell)."""
    m = D.mean(1)
    if D.shape[1] < 2: return m, np.full_like(m, np.nan), np.full_like(m, np.nan)
    lo, hi = np.percentile(D @ W.T, [2.5, 97.5], axis=1)
    return m, lo, hi


def pct(v, q):
    """Percentile with linear interpolation; inf (not reached) sorts last and propagates."""
    v = sorted(v); i = q*(len(v) - 1); a = int(math.floor(i)); b = min(a + 1, len(v) - 1); f = i - a
    if math.isinf(v[a]) or (f > 0 and math.isinf(v[b])): return math.inf
    return v[a] + (v[b] - v[a])*f


def first_down(xs, ys, thr):
    """The lowest x at which the piecewise-linear curve (xs, ys) is at or below thr; None if it never is."""
    if ys[0] <= thr: return xs[0]
    for i in range(1, len(xs)):
        if ys[i] <= thr: return xs[i - 1] + (thr - ys[i - 1])*(xs[i] - xs[i - 1])/(ys[i] - ys[i - 1])
    return None


def verdict(eff, sgn):
    """Decision rule 1 from [(mean, lo, hi)] per environment."""
    if any((sgn < 0 and lo > 0) or (sgn > 0 and hi < 0) for m, lo, hi in eff): return 'harms'
    if all((sgn < 0 and hi < 0) or (sgn > 0 and lo > 0) for m, lo, hi in eff): return 'works'
    return 'does not move'


def fmt(m, lo=float('nan'), hi=float('nan'), dp=2):
    s = ('%+.' + str(dp) + 'f') % m
    return s if math.isnan(lo) else s + (' (%+.' + str(dp) + 'f, %+.' + str(dp) + 'f)') % (lo, hi)


# ---------- stage 1 ----------
def comparator(name):
    sv = name.endswith('.sv'); b = name[:-3] if sv else name
    c = None if b == 'base' else 'base' if b == 'asis' else 'asis' if b.startswith('asis.') else 'base'
    return (c + '.sv' if sv else c) if c else None


def effects(rows, meta, W, stage):
    """Every cell: {(env, design, wage, row): {key: (level, none level, prog m, lo, hi, comparator, lever m, lo, hi)}}."""
    keys = meta['keys']; n = meta['seeds'][1] - meta['seeds'][0] + 1; E = {}
    for e in ENVS:
        for d in DES:
            for w in WAGES:
                pre = '%s.%s.w%d.' % (e, d, w)
                names = [r[len(pre):] for r in rows if r.startswith(pre) and not r[len(pre):].startswith('none')]
                if not names: continue
                for k in keys:
                    P, L, idx = [], [], []
                    for nm in names:
                        none = pre + ('none.sv' if nm.endswith('.sv') and stage != 2 else 'none')
                        x = get(rows, pre + nm, k, n); P.append(x - get(rows, none, k, n))
                        c = comparator(nm) if stage == 1 else None
                        L.append(x - get(rows, pre + c, k, n) if c else np.zeros(n)); idx.append((nm, none, c))
                    pm, plo, phi = stats(np.array(P), W); lm, llo, lhi = stats(np.array(L), W)
                    for j, (nm, none, c) in enumerate(idx):
                        E.setdefault((e, d, w, nm), {})[k] = (float(np.mean(get(rows, pre + nm, k, n))), float(np.mean(get(rows, none, k, n))),
                                                             pm[j], plo[j], phi[j], c, lm[j] if c else np.nan, llo[j] if c else np.nan, lhi[j] if c else np.nan)
    return E


def write_csv(E, path, stage):
    with open(path, 'w') as f:
        f.write('stage,env,design,wage,row,key,level,none,prog,prog_lo,prog_hi,vs,lever,lever_lo,lever_hi\n')
        for (e, d, w, nm), v in E.items():
            for k, (lv, nl, pm, plo, phi, c, lm, llo, lhi) in v.items():
                f.write('%d,%s,%s,%d,%s,%s,%s\n' % (stage, e, d, w, nm, k, ','.join(['%.6g' % lv, '%.6g' % nl, '%.6g' % pm, '%.6g' % plo, '%.6g' % phi, c or '',
                                                                                     '' if not c else '%.6g' % lm, '' if not c else '%.6g' % llo, '' if not c else '%.6g' % lhi])))


def lever_names(E, d, w, sv=False):
    out = []
    for (e, dd, ww, nm) in E:
        if e == 'ref' and dd == d and ww == w and nm != ('base.sv' if sv else 'base') and nm.endswith('.sv') == sv and nm not in out: out.append(nm)
    return out


def stage1_tables(E, n, reps):
    L = ['## Stage 1: each lever on its own (Q20, decision rule 1)', '',
         'Lever effect: the lever row minus its comparison row on the same seeds (the design under the test reading, `base`; for today\'s rule\'s tax sweep, `asis`; '
         'for `asis` itself, `base`, so that row is the effect of the joining reading). A lever **works** on an outcome where the interval excludes zero in the favourable '
         'direction in all three environments, **harms** where it excludes zero in the unfavourable direction in any environment, and otherwise does not move it. '
         'Each cell of the matrices: the verdict and the lever effect\'s mean over the three environments (points; inflation in points a year). '
         'Participation (higher is favourable) is in % of adults.', '']
    L += ['### The designs against no programme (programme effect, seed mean and 95% interval)', '',
          '| Design | Wages | Row | Environment | ' + ' | '.join(KEYS[k][0] for k in MATRIX) + ' |', '|---|---|---|---|' + '---|'*len(MATRIX)]
    for d in DES:
        for w in WAGES:
            for nm in ['base', 'asis', 'base.sv']:
                for e in ENVS:
                    v = E.get((e, d, w, nm))
                    if not v: continue
                    L.append('| %s | %d%% | %s | %s | %s |' % (DESL[d], w, nm, ENVL[e], ' | '.join(fmt(v[k][2]*KEYS[k][2], v[k][3]*KEYS[k][2], v[k][4]*KEYS[k][2]) for k in MATRIX)))
    L.append('')
    for sv in (False, True):
        for d in DES:
            for w in WAGES:
                names = lever_names(E, d, w, sv)
                if not names: continue
                L += ['### Verdicts: %s, wages %d%%%s' % (DESL[d], w, ', savings that keep up with prices (`.sv` twins, against `base.sv`)' if sv else ''), '',
                      '| Row | What it sets | vs | ' + ' | '.join(KEYS[k][0] for k in MATRIX) + ' |', '|---|---|---|' + '---|'*len(MATRIX)]
                for nm in names:
                    cells = []
                    for k in MATRIX:
                        eff = [(E[(e, d, w, nm)][k][6], E[(e, d, w, nm)][k][7], E[(e, d, w, nm)][k][8]) for e in ENVS]
                        v = verdict(eff, KEYS[k][1]); mm = np.mean([x[0] for x in eff])*KEYS[k][2]
                        cells.append(('**%s**' % v if v != 'does not move' else 'no move') + ' %+.2f' % mm)
                    L.append('| %s | %s | %s | %s |' % (nm, desc1(nm[:-3] if sv else nm), E[('ref', d, w, nm)]['fgt0PY'][5], ' | '.join(cells)))
                L.append('')
    for d in DES:
        for w in WAGES:
            names = lever_names(E, d, w)
            for k in PRIMARY:
                L += ['### %s: %s, wages %d%% (lever effect, seed mean and 95%% interval)' % (KEYS[k][0], DESL[d], w), '',
                      '| Row | What it sets | ' + ' | '.join(ENVL[e] for e in ENVS) + ' | Verdict |', '|---|---|' + '---|'*len(ENVS) + '---|']
                for nm in names:
                    eff = [(E[(e, d, w, nm)][k][6], E[(e, d, w, nm)][k][7], E[(e, d, w, nm)][k][8]) for e in ENVS]
                    s = KEYS[k][2]
                    L.append('| %s | %s | %s | %s |' % (nm, desc1(nm), ' | '.join(fmt(m*s, lo*s, hi*s) for m, lo, hi in eff), verdict(eff, KEYS[k][1])))
                L.append('')
    return L


def breakevens(rows, meta, W):
    n = meta['seeds'][1] - meta['seeds'][0] + 1; reps = W.shape[0]; out = []
    for d in DES:
        for w in WAGES:
            for e in ENVS:
                for rd in ('conv', 'asis'):
                    pre = '%s.%s.w%d.' % (e, d, w); tn = [pre + ('t%d' % t if rd == 'conv' else 'asis.t%d' % t) for t in TAX]
                    rel = pre + ('base' if rd == 'conv' else 'asis')
                    if not all(r in rows for r in tn + [rel]): continue
                    U = np.array([get(rows, r, 'lvU', n) for r in tn]); F = np.array([get(rows, r, 'fgt0PY', n) - get(rows, pre + 'none', 'fgt0PY', n) for r in tn])
                    J = np.array([get(rows, r, 'lvJm', n) for r in tn]); J0 = get(rows, rel, 'lvJm', n)
                    up = [i for i, t in enumerate(TAX) if t > TREL[e]]; xs = [TREL[e]] + [TAX[i] for i in up]
                    Ub, Fb, Jb, J0b = U @ W.T, F @ W.T, J @ W.T, W @ J0
                    sf = first_down(TAX, U.mean(1), 0.0); sfb = [first_down(TAX, Ub[:, r], 0.0) for r in range(reps)]
                    lb = TAX[int(np.argmin(F.mean(1)))]; lbb = [TAX[int(np.argmin(Fb[:, r]))] for r in range(reps)]
                    j0 = J0.mean(); de = first_down(xs, [j0] + [J[i].mean() for i in up], j0 - 5)
                    deb = [first_down(xs, [J0b[r]] + [Jb[i, r] for i in up], J0b[r] - 5) for r in range(reps)]
                    inf = lambda v: [math.inf if x is None else x for x in v]
                    out.append(dict(d=d, w=w, e=e, rd=rd, sf=sf, sf_ci=(pct(inf(sfb), .025), pct(inf(sfb), .975)), sf_share=np.mean([x is not None for x in sfb]),
                                    u40=U[-1].mean(), u0=U[0].mean(), urel=get(rows, rel, 'lvU', n).mean(), lb=lb, lb_ci=(pct(lbb, .025), pct(lbb, .975)), f_lb=F.mean(1).min(),
                                    de=de, de_ci=(pct(inf(deb), .025), pct(inf(deb), .975)), de_share=np.mean([x is not None for x in deb]), j0=j0, j40=J[-1].mean(),
                                    curve=[(t, F[i].mean(), U[i].mean(), J[i].mean()) for i, t in enumerate(TAX)]))
    return out


def be_tables(B, rows, meta):
    n = meta['seeds'][1] - meta['seeds'][0] + 1
    rate = lambda x: 'beyond 40%' if math.isinf(x) else '%.1f%%' % x
    L = ['## The conversion tax: three break-even rates (Q21, decision rules 2 and 3)', '',
         'Test reading: joining that sees what joining pays (`tNN`, released rate `base`); today\'s rule: `asis.tNN`, released rate `asis`. '
         'Intervals: 2.5th-97.5th percentiles over the bootstrap replicates; "beyond 40%" where fewer than 2.5% (or 97.5%) of replicates reach it; '
         '"reached" is the share of replicates that do.', '',
         '| Design | Wages | Environment | Joining | Self-funding rate | Net new money at 0% / released / 40% (% of earned income) | Lowest basket poverty at | Deterrence rate (participation 5 points below its level at the released rate) | Participation at released / 40% |',
         '|---|---|---|---|---|---|---|---|---|']
    for b in B:
        sf = ('not reached by 40%' if b['sf'] is None else '%.1f%%' % b['sf']) + ' (%s, %s; reached %.0f%%)' % (rate(b['sf_ci'][0]), rate(b['sf_ci'][1]), 100*b['sf_share'])
        de = ('not reached by 40%' if b['de'] is None else '%.1f%%' % b['de']) + ' (%s, %s; reached %.0f%%)' % (rate(b['de_ci'][0]), rate(b['de_ci'][1]), 100*b['de_share'])
        L.append('| %s | %d%% | %s | %s | %s | %.1f / %.1f / %.1f | %g%% (%g%%, %g%%) | %s | %.1f / %.1f |' % (
            DESL[b['d']], b['w'], ENVL[b['e']], 'test' if b['rd'] == 'conv' else "today's", sf, b['u0'], b['urel'], b['u40'], b['lb'], b['lb_ci'][0], b['lb_ci'][1], de, b['j0'], b['j40']))
    L += ['', '### The tax sweep (seed means; basket poverty as the change against no programme)', '']
    for d in DES:
        for w in WAGES:
            L += ['#### %s, wages %d%%' % (DESL[d], w), '', '| Rate | ' + ' | '.join('%s %s: basket / new money / participation' % (ENVL[e], j) for e in ENVS for j in ('test', "today's")) + ' |',
                  '|---|' + '---|'*6]
            cur = {(b['e'], b['rd']): b['curve'] for b in B if b['d'] == d and b['w'] == w}
            for i, t in enumerate(TAX):
                L.append('| %d%% | %s |' % (t, ' | '.join('%+.2f / %.1f / %.1f' % cur[(e, rd)][i][1:] if (e, rd) in cur else '' for e in ENVS for rd in ('conv', 'asis'))))
            L.append('')
    return L


# ---------- stage 2 ----------
def morris(rows, meta):
    X = meta['design']; delta = X['delta']; n = meta['seeds'][1] - meta['seeds'][0] + 1; R = {}
    for d in DES:
        for e in ENVS:
            pre = '%s.%s.w100.' % (e, d)
            for k, _, _ in OBJ:
                ee = {f: [] for f in X['factors']}
                for t, tr in enumerate(X['morris']):
                    y = [get(rows, pre + 'm%d.%d' % (t, s), k, n).mean()*KEYS[k][2] for s in range(len(tr['points']))]
                    for s in range(1, len(y)): ee[tr['order'][s - 1]].append((y[s] - y[s - 1])/delta)
                for f, v in ee.items():
                    v = np.array(v); R[(d, e, k, f)] = (np.mean(np.abs(v)), np.mean(v), np.std(v, ddof=1) if len(v) > 1 else np.nan)
    return R


def morris_tables(R, meta):
    F = meta['design']['factors']
    L = ['## Stage 2: Morris screening (Q22; descriptive, no claim rests on it)', '',
         'Elementary effects on the [0, 1] factor scale (the change over the full range, in points; inflation in points a year), 10 trajectories, wages 100%: '
         'mu* the mean absolute effect, sd its spread (a large sd beside mu* means the factor\'s effect depends on the others). Sorted by mu* on basket poverty, mean over environments.', '']
    for d in DES:
        order = sorted(F, key=lambda f: -np.mean([R[(d, e, 'fgt0PY', f)][0] for e in ENVS]))
        for e in ENVS:
            L += ['### %s, %s' % (DESL[d], ENVL[e]), '', '| Factor | ' + ' | '.join('%s mu* (mu; sd)' % lab for _, lab, _ in OBJ) + ' |', '|---|' + '---|'*len(OBJ)]
            for f in order:
                L.append('| %s | %s |' % (FACTL.get(f, f), ' | '.join('%.2f (%+.2f; %.2f)' % R[(d, e, k, f)] for k, _, _ in OBJ)))
            L.append('')
    return L


# ---------- the front and the choice ----------
def candidates(E1, E2, d, w):
    """[(name, stage, {env: {key: programme effect mean}})] in candidate order: stage 1 (test reading, ordinary savings), then stage 2."""
    C = []
    for E, st in ((E1, 1), (E2, 2)):
        if E is None: continue
        for (e, dd, ww, nm) in E:
            if e != 'ref' or dd != d or ww != w: continue
            if st == 1 and (nm.endswith('.sv') or nm == 'asis' or nm.startswith('asis.')): continue
            C.append((nm, st, {e2: {k: E[(e2, d, w, nm)][k][2] for k in E[(e2, d, w, nm)]} for e2 in ENVS}))
    return C


def objv(c, envs):
    return tuple(np.mean([c[2][e][k]*KEYS[k][2] for e in envs])*(-s) for k, _, s in OBJ)   # all minimised


def front(C, envs):
    pts, seen, dup = [], {}, {}
    for c in C:
        v = objv(c, envs)
        if not all(math.isfinite(x) for x in v): continue
        key = tuple(round(x, 10) for x in v)
        if key in seen: dup.setdefault(seen[key], []).append(c[0]); continue
        seen[key] = c[0]; pts.append((c, v))
    F = [(c, v) for c, v in pts if not any(all(a <= b for a, b in zip(o, v)) and any(a < b for a, b in zip(o, v)) for _, o in pts)]
    return F, dup


def fails(c):
    out, ex = [], 0.0
    for e in ENVS:
        for k in NOHARM:
            x = c[2][e][k]*KEYS[k][2]
            if not x <= 0: out.append('%s %+.2f in %s' % (k, x, ENVL[e])); ex += x if math.isfinite(x) else math.inf
        x = c[2][e]['endoAnn']*100
        if not x < 5: out.append('inflation %.2f in %s' % (x, ENVL[e])); ex += (x - 5) if math.isfinite(x) else math.inf
    return out, ex


def choose(C):
    a = [c for c in C if all(c[2][e][k] <= 0 for e in ENVS for k in NOHARM)]
    b = [c for c in a if all(c[2][e]['endoAnn'] < 0.05 for e in ENVS)]
    ch = min(b, key=lambda c: np.mean([c[2][e]['fgt0PY'] for e in ENVS])) if b else None   # min keeps the first of ties
    close = sorted(C, key=lambda c: fails(c)[1])[:5] if not b else []
    return ch, len(a), len(b), close


def front_tables(E1, E2, meta2, sel):
    X = meta2['design'] if meta2 else None
    L = ['## The trade-off front and the best setting (Q22, Q23, decision rule 4)', '',
         'Candidates: every stage-1 row under the test reading on ordinary savings and every stage-2 row. Objectives: the mean over the three environments of the change '
         'against no programme in basket poverty and wealth poverty (lower is better), participation (higher) and programme inflation (lower, points a year). '
         'No harm: gNonF0, gNonW, secU25X, secM3X and wealth poverty at or below zero in every environment; inflation under 5 points a year in every environment.', '']
    for d in DES:
        for w in WAGES:
            C = candidates(E1, E2, d, w)
            if not C: continue
            F, dup = front(C, ENVS); ch, na, nb, close = choose(C)
            fr_env = {e: {c[0] for c, _ in front(C, [e])[0]} for e in ENVS}
            sel.append({'design': d, 'wage': w, 'chosen': ch[0] if ch else None, 'pareto': [c[0] for c, _ in sorted(F, key=lambda x: x[1][0])],
                        'closest': [c[0] for c in close], 'candidates': len(C), 'pass_noharm': na, 'pass_both': nb})
            L += ['### %s, wages %d%%' % (DESL[d], w), '',
                  '%d candidates; %d pass no harm in every environment; %d of those keep inflation under 5 points a year. ' % (len(C), na, nb) +
                  ('**Chosen by the rule: `%s`** (%s): basket poverty %+.2f, wealth poverty %+.2f, participation %.1f%%, inflation %.2f points a year (means over the environments).' % (
                      ch[0], desc(ch[0], X), *[x*(-s) for x, (_, _, s) in zip(objv(ch, ENVS), OBJ)]) if ch else
                   '**No setting tested meets the rule.** Closest (by the summed excess of what fails): ' + '; '.join('`%s` (%s: %s)' % (c[0], desc(c[0], X), ', '.join(fails(c)[0][:4]) + (' ...' if len(fails(c)[0]) > 4 else '')) for c in close) + '.'), '',
                  '| Point | What it sets | Basket poverty | Wealth poverty | Participation | Inflation | On the front in | Fails |', '|---|---|---|---|---|---|---|---|']
            for c, v in sorted(F, key=lambda x: x[1][0]):
                fl = fails(c)[0]
                L.append('| %s%s | %s | %+.2f | %+.2f | %.1f | %.2f | %s | %s |' % (c[0], ' (= ' + ', '.join(dup[c[0]]) + ')' if c[0] in dup else '', desc(c[0], X), v[0], v[1], -v[2], v[3],
                         ', '.join(ENVL[e] for e in ENVS if c[0] in fr_env[e]) or 'none', ('%d: ' % len(fl) + '; '.join(fl[:3]) + (' ...' if len(fl) > 3 else '')) if fl else 'nothing'))
            L.append('')
    return L


# ---------- stage 3 ----------
def confirm(rows, meta, W, S):
    n = meta['seeds'][1] - meta['seeds'][0] + 1
    L = ['## Stage 3: confirmation on fresh seeds %d-%d (decision rule 5)' % tuple(meta['seeds']), '',
         'Each cell: the change against no programme, seed mean and 95% interval. Confirmed: basket poverty\'s interval below zero, each no-harm measure\'s upper end at or below '
         '+0.5 points, and inflation\'s upper end under 5 points a year (required for the chosen setting, reported for Pareto points), in every environment.', '']
    ks = ['fgt0PY'] + NOHARM + ['endoAnn', 'lvJm']; res = []
    for s in S['sets']:
        d, w = s['design'], s['wage']; names = ([s['chosen'], s['chosen'] + '.sv', s['chosen'] + '.asis'] if s['chosen'] else []) + [p for p in s['pareto'] if p != s['chosen']]
        L += ['### %s, wages %d%%' % (DESL[d], w), '', '| Setting | Role | Environment | ' + ' | '.join(KEYS[k][0] for k in ks) + ' | Passes |', '|---|---|---|' + '---|'*len(ks) + '---|']
        for nm in names:
            role = 'chosen' if nm == s['chosen'] else 'chosen, savings keep up' if nm.endswith('.sv') else "chosen, today's rule" if nm.endswith('.asis') else 'Pareto point'
            ok_all, okx_all = True, True
            for e in ENVS:
                pre = '%s.%s.w%d.' % (e, d, w); r = pre + nm
                if r not in rows: L.append('| %s | %s | %s | not run |' % (nm, role, ENVL[e])); ok_all = False; continue
                none = pre + ('none.sv' if nm.endswith('.sv') else 'none')
                D = np.array([get(rows, r, k, n) - get(rows, none, k, n) for k in ks]); m, lo, hi = stats(D, W); c = dict(zip(ks, zip(m, lo, hi)))
                ok = c['fgt0PY'][2] < 0 and all(c[k][2]*KEYS[k][2] <= 0.5 for k in NOHARM); okx = c['endoAnn'][2]*100 < 5
                ok_all &= ok; okx_all &= okx
                L.append('| %s | %s | %s | %s | %s |' % (nm, role, ENVL[e], ' | '.join(fmt(*(x*KEYS[k][2] for x in c[k])) for k in ks),
                                                         ('yes' if ok else 'no') + ('' if okx else ' (inflation)')))
            conf = ok_all and okx_all if role == 'chosen' else ok_all
            res.append((d, w, nm, role, conf, okx_all))
        L.append('')
    L += ['### Summary', '', '| Design | Wages | Setting | Role | Confirmed | Inflation under 5 points everywhere |', '|---|---|---|---|---|---|']
    L += ['| %s | %d%% | %s | %s | %s | %s |' % (DESL[d], w, nm, role, 'confirmed' if c else 'not confirmed', 'yes' if x else 'no') for d, w, nm, role, c, x in res]
    return L + ['']


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    opt = lambda k: a[a.index(k) + 1] if k in a else None
    reps = int(opt('--reps') or 2000)
    S1, S2, S3 = [load(p) if p else (None, None) for p in (opt('--s1'), opt('--s2'), opt('--s3'))]
    if '--check' in a:
        ok = True
        for (rows, meta), st in ((S1, 1), (S2, 2), (S3, 3)):
            if rows is not None: ok &= check(rows, meta, PREREG.get(st), 'stage %d' % st)
        sys.exit(0 if ok else 1)
    L = []
    E1 = E2 = None
    if S1[0] is not None:
        rows, meta = S1; n = meta['seeds'][1] - meta['seeds'][0] + 1; W = weights(n, reps)
        L += ['# S54 policy levers: tables (pilot, seeds %d-%d; labelled pilot, not figures of the model)' % tuple(meta['seeds']), '',
              'Engine %s. Written by `dev/tools/s54_levers.py` from compassionism-sim-results (stage 1: %s; stage 2: %s). Paired bootstrap over seeds, %d replicates, '
              'resampler seed 54, the same resample for every cell. research-update `prereg/2026-11-levers-addendum.md` defines every cell.' % (
                  meta.get('manifest', {}).get('commit', '?')[:7], opt('--s1'), opt('--s2') or 'not given', reps), '']
        E1 = effects(rows, meta, W, 1)
        L += stage1_tables(E1, n, reps) + be_tables(breakevens(rows, meta, W), rows, meta)
        if opt('--csv'): os.makedirs(opt('--csv'), exist_ok=True); write_csv(E1, os.path.join(opt('--csv'), 'stage1-effects.csv'), 1)
    if S2[0] is not None:
        rows, meta = S2; n = meta['seeds'][1] - meta['seeds'][0] + 1; W = weights(n, reps)
        E2 = effects(rows, meta, W, 2)
        L += morris_tables(morris(rows, meta), meta)
        if opt('--csv'): os.makedirs(opt('--csv'), exist_ok=True); write_csv(E2, os.path.join(opt('--csv'), 'stage2-effects.csv'), 2)
    if E1 is not None or E2 is not None:
        sel = []; L += front_tables(E1, E2, S2[1], sel)
        if opt('--select'):
            m = (S1[1] or S2[1])
            json.dump({'what': 'S54 stage 3 settings: the best setting by decision rule 4 and every point of the front, chosen on seeds %d-%d by dev/tools/s54_levers.py '
                               '(research-update prereg/2026-11-levers-addendum.md)' % tuple(m['seeds']),
                       'engine': m.get('manifest', {}).get('commit', '?'), 'chosen_on': m['seeds'], 'sets': sel}, open(opt('--select'), 'w'), indent=1)
    if S3[0] is not None:
        rows, meta = S3; n = meta['seeds'][1] - meta['seeds'][0] + 1; W = weights(n, reps)
        L += confirm(rows, meta, W, json.load(open(opt('--list'))))
    out = '\n'.join(L) + '\n'
    if opt('--out'): open(opt('--out'), 'w').write(out)
    else: sys.stdout.write(out)


if __name__ == '__main__':
    main()
