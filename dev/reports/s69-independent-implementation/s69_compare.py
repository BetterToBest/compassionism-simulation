"""S69: compare this program's 500-seed results with the packet's reference, as 00-START-HERE.md asks.

1. Exact: a key of a seed matches if its relative difference is under 1e-9 (or both are within 1e-12 of each other). Two keys are
   identity residues, zero to rounding by definition (crGap, the creditor ledger's gap; mfChk, the money-flow check; spCarry, the split's
   carry, pool less what is used): they are compared against the size of the ledger they close (crRel; mfPay; spPool), at the same 1e-9.
2. Statistical: a key matches if |mean_mine - mean_ref| <= 2 sqrt(sd_mine^2/500 + sd_ref^2/500); the same for the programme's effect
   (candidate main row minus no programme, seed by seed). A difference within rounding (relative 1e-9) also matches: a few keys hardly
   vary across seeds (the price level of a year in Adverse is 1.02^t times 1), so two standard errors are smaller than the last binary
   digit, and the two languages' power functions round 1.02^12 differently.

  python3 -I s69_compare.py RESULTS_DIR [PACKET]      writes RESULTS_DIR/compare-*.csv and prints the markdown tables
"""
import os
import sys
import json
import math
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
RESIDUE = {'crGap': 'crRel', 'mfChk': 'mfPay', 'spCarry': 'spPool'}
HEADLINE = ['y0F0', 'y0Pov', 'y0BO', 'y0BN', 'y0Fpl', 'y0GiniW', 'y0Ep', 'fgt0PY', 'fgt2PY', 'pov', 'bOAPy', 'bNAPy', 'medWealthReal', 'giniD', 'giniX', 'epPY',
            'cost', 'tauMean', 'endoAnn', 'pLev20', 'hrs', 'jnP19', 'emUrate', 'snAll', 'wtPovE', 'wtF0E', 'wtGnE', 'paSh', 'poSub', 'finGapSh', 'crRel', 'lfShare', 'drHit']
ENVS = ('ref', 'adv', 'st')
ROWS = ('base', 'main')


def close(a, b, scale=None):
    if a is None or b is None:
        return False
    d = abs(a - b)
    if d <= 1e-12:
        return True
    s = max(abs(a), abs(b))
    if scale is not None:
        s = max(s, abs(scale))
    return d / s <= 1e-9


def mean_sd(x):
    n = len(x)
    m = math.fsum(x) / n
    v = math.fsum((y - m) ** 2 for y in x) / (n - 1) if n > 1 else 0
    return m, math.sqrt(v)


def two_se(x, y):
    mx, sx = mean_sd(x)
    my, sy = mean_sd(y)
    n = len(x)
    lim = 2 * math.sqrt(sx * sx / n + sy * sy / n)
    d = mx - my
    ok = abs(d) <= lim or abs(d) <= 1e-9 * max(abs(mx), abs(my)) or abs(d) <= 1e-12
    return mx, my, d, lim, ok


def load_ref(packet, env):
    with zipfile.ZipFile(packet) as z:
        return json.loads(z.read('reference/s69-%s-1-500.json' % env))['rows']


def mine_path(res, env, row):
    p = os.path.join(res, '%s-%s-1-500.json' % (env, row))
    return p if os.path.exists(p) else p + '.gz'


def load_mine(res, env, row):
    p = mine_path(res, env, row)
    if p.endswith('.gz'):
        import gzip
        with gzip.open(p, 'rt') as f:
            return json.load(f)
    with open(p) as f:
        return json.load(f)


def fmt(v):
    if v is None:
        return ''
    a = abs(v)
    if a == 0:
        return '0'
    if a >= 1000:
        return '%.1f' % v
    if a >= 1:
        return '%.4f' % v
    return '%.4g' % v


def main():
    res = sys.argv[1]
    packet = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, '..', '..', 'packets', 's69-main-row.zip')
    out = []
    summary = []
    effects = []
    head_rows = []
    nonexact_all = []
    for env in ENVS:
        refs = load_ref(packet, env)
        mine = {}
        for ri, row in enumerate(ROWS):
            p = mine_path(res, env, row)
            if not os.path.exists(p):
                summary.append((env, row, None))
                continue
            M = load_mine(res, env, row)
            mine[row] = M
            R = refs[ri]['seeds']
            ms = M['seeds']
            tiny = ms.get('_tinyEarn')
            keys = sorted(R)
            nk = len(keys)
            n_exact_all = 0
            n_fail = 0
            missing = [k for k in keys if k not in ms]
            rows_csv = []
            for k in keys:
                if k not in ms:
                    continue
                r = R[k]
                m = ms[k]
                sc = R.get(RESIDUE[k]) if k in RESIDUE else None
                bad = [i for i in range(len(r)) if not close(m[i], r[i], abs(sc[i]) if sc else None)]
                if not bad:
                    n_exact_all += 1
                else:
                    tb = sum(1 for i in bad if tiny and tiny[i])
                    nonexact_all.append((env, row, k, len(bad), tb, bad[:5]))
                mx, my, d, lim, ok = two_se(m, r)
                if not ok:
                    n_fail += 1
                rows_csv.append((k, len(r) - len(bad), my, mx, d, lim, ok))
                if k in HEADLINE:
                    head_rows.append((env, row, k, my, mx, d, lim, ok, len(r) - len(bad)))
            with open(os.path.join(res, 'compare-%s-%s.csv' % (env, row)), 'w') as f:
                f.write('key,seeds_exact_of_500,ref_mean,my_mean,difference,two_se,match_2se\n')
                for q in rows_csv:
                    f.write('%s,%d,%r,%r,%r,%r,%s\n' % q)
            summary.append((env, row, dict(keys=nk, exact=n_exact_all, fail=n_fail, missing=len(missing), seconds=M.get('seconds'), errors=len(M.get('errors') or {}))))
        if 'base' in mine and 'main' in mine:
            Rb = refs[0]['seeds']
            Rm = refs[1]['seeds']
            Mb = mine['base']['seeds']
            Mm = mine['main']['seeds']
            nk = nf = 0
            rows_csv = []
            for k in sorted(set(Rb) & set(Rm)):
                if k not in Mb or k not in Mm:
                    continue
                er = [Rm[k][i] - Rb[k][i] for i in range(len(Rb[k]))]
                em = [Mm[k][i] - Mb[k][i] for i in range(len(Mb[k]))]
                mx, my, d, lim, ok = two_se(em, er)
                nk += 1
                if not ok:
                    nf += 1
                rows_csv.append((k, my, mx, d, lim, ok))
                if k in HEADLINE:
                    head_rows.append((env, 'effect', k, my, mx, d, lim, ok, None))
            with open(os.path.join(res, 'compare-%s-effect.csv' % env), 'w') as f:
                f.write('key,ref_effect,my_effect,difference,two_se,match_2se\n')
                for q in rows_csv:
                    f.write('%s,%r,%r,%r,%r,%s\n' % q)
            effects.append((env, nk, nf))
    out.append('## Summary\n')
    out.append('| Environment | Run | Keys | Keys exact in all 500 seeds | Keys failing the 2-SE test | Keys missing | Seconds | Seeds that failed to run |')
    out.append('|---|---|---|---|---|---|---|---|')
    for env, row, s in summary:
        if s is None:
            out.append('| %s | %s | not run | | | | | |' % (env, row))
        else:
            out.append('| %s | %s | %d | %d | %d | %d | %s | %d |' % (env, row, s['keys'], s['exact'], s['fail'], s['missing'], s['seconds'], s['errors']))
    out.append('\n| Environment | Effect keys compared (main row minus no programme) | Failing the 2-SE test |')
    out.append('|---|---|---|')
    for env, nk, nf in effects:
        out.append('| %s | %d | %d |' % (env, nk, nf))
    out.append('\n## Keys not exact in every seed\n')
    out.append('Why: "zero earnings" = every such seed has an adult-year whose earnings are zero in exact arithmetic, so rounding decides whether it was worked (GAPS.md item 22); "ties" = a weighted distribution measure whose order of near-tied adults at the borrowing limit is set by rounding (item 24); "not explained" = neither.\n')
    out.append('| Environment | Run | Key | Seeds not exact | Of them, seeds with a zero-earnings adult-year | Why | First seeds |')
    out.append('|---|---|---|---|---|---|---|')
    for env, row, k, nb, tb, first in nonexact_all:
        why = 'zero earnings' if tb == nb else ('ties' if k.startswith('dm') else 'not explained')
        out.append('| %s | %s | %s | %d | %d | %s | %s |' % (env, row, k, nb, tb, why, ', '.join(str(i + 1) for i in first)))
    out.append('\n## Headline keys\n')
    out.append('| Environment | Run | Key | Reference mean | My mean | Difference | 2 SE | Match (2 SE) | Seeds exact |')
    out.append('|---|---|---|---|---|---|---|---|---|')
    for env, row, k, my, mx, d, lim, ok, ne in head_rows:
        out.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (env, row, k, fmt(my), fmt(mx), fmt(d), fmt(lim), 'yes' if ok else 'NO', '' if ne is None else ne))
    txt = '\n'.join(out) + '\n'
    with open(os.path.join(res, 'compare.md'), 'w') as f:
        f.write(txt)
    print(txt)


if __name__ == '__main__':
    main()
