#!/usr/bin/env python3
"""S85 part 4 (Nov 20, 2026): the trace of the opt-in worsening, as research-update prereg/2026-11-s85-output-per-hour.md, Amendment 4, fixes it
(written and committed before this tool was run on the 500-seed data).

  python3 dev/tools/s85_trace.py RESULTS_DIR OUT_DIR [--engine 503fa48] [--reps 10000]

Reads the six folders s85-<env>-<years>-<engine> of compassionism-sim-results (keys the batch already stores; no new run) and writes Markdown
tables and a summary JSON. For each cell of block A (design x form x D 0.1-0.7, three environments, 20 and 40 years):

- The all-adult figure is the weighted sum of two groups of latent adults (the same adults in every design and in the no-programme run): those who
  would take part (gPartK) and those who would not (gNonK), with weights s_g = k_g / (k_Part + k_Non), the same in every run of a seed. The tool
  checks that the stored group figures add up to the totals exactly and that the group sizes are equal across the runs it compares.
- For fgt0PY (basket poverty) and fgt2PY (its severity): the harm-signed change from D 0 to D in the programme run (dP_g) and in its no-programme
  partner (dN_g); cost_P = sum_g s_g dP_g, cost_N likewise; the worsening W = cost_P - cost_N (= minus the offset of Amendment 3 item 3), and
  W = W_Part + W_Non with W_g = s_g (dP_g - dN_g). Means over the 500 seeds, paired bootstrap, 10,000 replicates, the one resample shared with
  s85_tables.py (numpy default_rng(20261120)). No p-values and no Holm correction: this splits a difference already tested. A group's share of W is
  given only where W's interval lies wholly above zero.
- Readings (Amendment 4 item 5), per cell where W is wholly above zero: head count (W_Part wholly above zero, severity's W2_Part not) or head count and
  depth (both wholly above zero) among those who would take part; a burden on those who would not take part (W_Non wholly above zero).
- The contribution rate (tauMean, tauLast), the enrolled share (jnP19) and joins and leaves (jnJoin, jnLeave) in the programme run, at D minus at D 0;
  and the last year's basket poverty of the displaced adults (ohDB) and of the rest of those in paid work at the start (ohNB), both runs, with the
  programme's effect on each.
Standard library and numpy."""
import glob, json, math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s85_tables as T  # noqa: E402  (the same loader helpers, categories and bootstrap)

ENVS, ENVL, YEARS = T.ENVS, T.ENVL, T.YEARS
DES, DESL, FORMS, FL = T.DES, T.DESL, T.FORMS, T.FL
DS = ['0.1', '0.3', '0.5', '0.7']
KEYS = ['fgt0PY', 'fgt2PY', 'gPartF0', 'gNonF0', 'gPartF2', 'gNonF2', 'gPartK', 'gNonK', 'tauMean', 'tauLast', 'jnP5', 'jnP10', 'jnP19', 'jnJoin',
        'jnLeave', 'ohDN', 'ohNN', 'ohDB', 'ohNB']
MEAS = [('F0', 'fgt0PY', 'gPartF0', 'gNonF0', 'basket poverty'), ('F2', 'fgt2PY', 'gPartF2', 'gNonF2', 'poverty severity')]
NS = 500


def f2(x): return '%.2f' % x


def ci(s): return '%s (%s to %s)' % (f2(s['est']), f2(s['lo']), f2(s['hi']))


def above(s): return s['lo'] > 0


def load(src, e, y, eng):
    """the rows the trace needs: name (without the environment) -> key -> array over seeds 1-500, and the job's rowSpec"""
    folder = os.path.join(src, 's85-%s-%d-%s' % (e, y, eng))
    D = sorted((T.jload(f) for f in T.shards(folder)), key=lambda d: d['_meta']['seeds'][0])
    spec = {s['name']: s for s in D[0]['_meta']['rowSpec']}
    need = set()
    for des in DES:
        need.add('A.%s.gain.D0' % des)
        for f in FORMS:
            for d in DS: need.add('A.%s.%s.D%s' % (des, f, d))
    need |= {spec[n]['none'] for n in list(need)}
    seeds = [s for d in D for s in range(d['_meta']['seeds'][0], d['_meta']['seeds'][1] + 1)]
    R = {n: {k: np.concatenate([np.array(d['rows']['%s.%s' % (e, n)][k], float) for d in D]) for k in KEYS} for n in sorted(need)}
    return R, spec, seeds, folder


def check(R, spec, seeds):
    """the trace's own checks: seeds 1-500 once; groups add up to totals; group sizes equal across the runs compared"""
    C = [('seeds 1-%d once, in order' % NS, seeds == list(range(1, NS + 1)))]
    worst, same = 0.0, True
    for n, r in R.items():
        kp, kn = r['gPartK'], r['gNonK']
        for _, tot, gp, gn, _ in MEAS:
            worst = max(worst, float(np.abs(r[tot] - (kp * r[gp] + kn * r[gn]) / (kp + kn)).max()))
    ref = R['A.rel.gain.D0']
    for n, r in R.items():
        if not (np.array_equal(r['gPartK'], ref['gPartK']) and np.array_equal(r['gNonK'], ref['gNonK'])): same = False
    C.append(('the stored group figures add up to the totals (largest difference %.3g)' % worst, worst < 1e-9))
    C.append(('group sizes equal in every run compared (%d runs)' % len(R), same))
    return C


def cell(R, spec, des, form, D):
    p, p0 = 'A.%s.%s.D%s' % (des, form, D), 'A.%s.gain.D0' % des
    n, n0 = spec[p]['none'], spec[p0]['none']
    r, r0, q, q0 = R[p], R[p0], R[n], R[n0]
    kp, kn = r['gPartK'], r['gNonK']; sP = kp / (kp + kn)
    out = {}
    for m, tot, gp, gn, lab in MEAS:
        dP = {'Part': r[gp] - r0[gp], 'Non': r[gn] - r0[gn]}; dN = {'Part': q[gp] - q0[gp], 'Non': q[gn] - q0[gn]}
        s = {'Part': sP, 'Non': 1 - sP}
        costP = sum(s[g] * dP[g] for g in s); costN = sum(s[g] * dN[g] for g in s)
        assert np.abs(costP - (r[tot] - r0[tot])).max() < 1e-9 and np.abs(costN - (q[tot] - q0[tot])).max() < 1e-9
        Wt = costP - costN
        out[m] = {'costN': T.est(costN), 'costP': T.est(costP), 'W': T.est(Wt),
                  'W_Part': T.est(s['Part'] * (dP['Part'] - dN['Part'])), 'W_Non': T.est(s['Non'] * (dP['Non'] - dN['Non'])),
                  'dP_Part': T.est(dP['Part']), 'dN_Part': T.est(dN['Part']), 'dP_Non': T.est(dP['Non']), 'dN_Non': T.est(dN['Non'])}
    out['sP'] = T.lev(sP * 100)
    out['tauMean'] = T.est((r['tauMean'] - r0['tauMean']) * 100); out['tauLast'] = T.est((r['tauLast'] - r0['tauLast']) * 100)
    out['tauMeanLev'] = T.lev(r['tauMean'] * 100); out['tauLastLev'] = T.lev(r['tauLast'] * 100)
    for k in ('jnP5', 'jnP10', 'jnP19', 'jnJoin', 'jnLeave'): out[k] = T.est(r[k] - r0[k])
    out['jnP19Lev'] = T.lev(r['jnP19'])
    for k in ('ohDB', 'ohNB'):
        out[k + 'P'] = T.lev(r[k]); out[k + 'N'] = T.lev(q[k]); out[k + 'eff'] = T.est(r[k] - q[k])
    out['ohDNn'] = float(r['ohDN'].mean()); out['ohNNn'] = float(r['ohNN'].mean())
    # shares of W (ratio of means; bootstrap of the ratio), only where W's interval lies wholly above zero
    for m, tot, gp, gn, lab in MEAS:
        if above(out[m]['W']):
            s = {'Part': sP, 'Non': 1 - sP}
            dP = {'Part': r[gp] - r0[gp], 'Non': r[gn] - r0[gn]}; dN = {'Part': q[gp] - q0[gp], 'Non': q[gn] - q0[gn]}
            Wt = sum(s[g] * (dP[g] - dN[g]) for g in s)
            for g in ('Part', 'Non'):
                wg = s[g] * (dP[g] - dN[g]); v = (T.W @ wg) / (T.W @ Wt); lo, hi = np.percentile(v, [2.5, 97.5])
                out[m]['share_' + g] = {'est': float(wg.mean() / Wt.mean()), 'lo': float(lo), 'hi': float(hi)}
    return out


def reading(c):
    """Amendment 4 item 5, per cell"""
    w, w2 = c['F0'], c['F2']
    if not above(w['W']): return 'does not worsen'
    if above(w['W_Part']): a = 'head count and depth among those who would take part' if above(w2['W_Part']) else 'more adults below the line, not further below (those who would take part)'
    else: a = 'not carried by those who would take part'
    b = '; a burden on those who would not take part' if above(w['W_Non']) else ''
    return a + b


def sh(c):
    s = c.get('share_Part'); t = c.get('share_Non')
    return '%d%% / %d%%' % (round(s['est'] * 100), round(t['est'] * 100)) if s and t else '-'


def write(out, ALL, CHK, eng, reps):
    os.makedirs(out, exist_ok=True)
    for y in YEARS:
        sfx = '' if y == 20 else '-40y'
        L = ['# The opt-in worsening, traced: who carries the difference (%d years)' % y, '',
             'Generated by `python3 dev/tools/s85_trace.py` from compassionism-sim-results `s85-<env>-<years>-%s` (keys the batch already stores; no new run; seeds 1-500, 500 adults). Preregistration: research-update `prereg/2026-11-s85-output-per-hour.md`, Amendment 4, written before the figures were computed. Means over seeds with 95%% paired-bootstrap intervals (%d replicates, generator seed 20261120, the resample shared with the other tables). No p-values and no Holm correction: this splits a difference already tested.' % (eng, reps), '',
             'Costs are harm-signed (positive = worse): the level at D minus the level at D 0, in the programme run (cost with the programme) and in its own no-programme run. **Worsening** = cost with the programme minus cost with no programme (positive: the rise is larger with the programme). It is the sum of two parts, one for the adults who would take part and one for those who would not (the same latent adults in every run; the table gives each part in points of all adults). "Share" is each part\'s share of the worsening, given only where the worsening\'s interval lies wholly above zero. Severity counts how far below the line adults fall.', '']
        for e in ENVS:
            for des in DES:
                for form in FORMS:
                    L += ['## %s, %s, %s (%d years)' % (ENVL[e], DESL[des], FL[form], y), '',
                          '| D | basket poverty: cost, no programme | cost, programme | worsening | part: would take part | part: would not | share (take part / not) | severity: worsening | would take part | would not | reading |',
                          '|---|---|---|---|---|---|---|---|---|---|---|']
                    for D in DS:
                        c = ALL['%s-%d' % (e, y)][des][form][D]
                        L.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (D, ci(c['F0']['costN']), ci(c['F0']['costP']), ci(c['F0']['W']), ci(c['F0']['W_Part']), ci(c['F0']['W_Non']), sh(c['F0']),
                                  ci(c['F2']['W']), ci(c['F2']['W_Part']), ci(c['F2']['W_Non']), reading(c)))
                    L += ['', 'Contribution, enrolment and the displaced adults, programme run at D against D 0 (points; the contribution rate in points of pay):', '',
                          '| D | contribution rate, run mean (change) | last year (change) | enrolled in year 19 (level; change) | joins over the run (change) | leaves over the run (change) | displaced adults below the basket, last year: programme / none (effect) | the rest in paid work: programme / none (effect) |',
                          '|---|---|---|---|---|---|---|---|']
                    for D in DS:
                        c = ALL['%s-%d' % (e, y)][des][form][D]
                        L.append('| %s | %s | %s | %s; %s | %s | %s | %s / %s (%s) | %s / %s (%s) |' % (D, ci(c['tauMean']), ci(c['tauLast']), f2(c['jnP19Lev']['est']), ci(c['jnP19']), ci(c['jnJoin']), ci(c['jnLeave']),
                                  f2(c['ohDBP']['est']), f2(c['ohDBN']['est']), ci(c['ohDBeff']), f2(c['ohNBP']['est']), f2(c['ohNBN']['est']), ci(c['ohNBeff'])))
                    L.append('')
        L += ['## Checks', '']
        for e in ENVS:
            for lab, ok in CHK['%s-%d' % (e, y)]: L.append('- %s %s-%d: %s' % ('PASS' if ok else 'FAIL', e, y, lab))
        open(os.path.join(out, 's85-trace%s.md' % sfx), 'w').write('\n'.join(L) + '\n')
    json.dump({'checks': {k: [[a, b] for a, b in v] for k, v in CHK.items()}, 'results': ALL}, open(os.path.join(out, 's85-trace-summary.json'), 'w'), indent=1)


def main():
    src, out = sys.argv[1], sys.argv[2]
    eng = sys.argv[sys.argv.index('--engine') + 1] if '--engine' in sys.argv else '503fa48'
    reps = int(sys.argv[sys.argv.index('--reps') + 1]) if '--reps' in sys.argv else 10000
    rng = np.random.default_rng(20261120); idx = rng.integers(0, NS, size=(reps, NS))
    Wm = np.zeros((reps, NS))
    for b in range(reps): Wm[b] = np.bincount(idx[b], minlength=NS) / NS
    T.W = Wm
    ALL, CHK = {}, {}
    for e in ENVS:
        for y in YEARS:
            R, spec, seeds, folder = load(src, e, y, eng)
            n, bad = T.sha_ok(folder)
            C = [('SHA256SUMS: %d files, all match' % n, not bad)] + check(R, spec, seeds)
            CHK['%s-%d' % (e, y)] = C
            ALL['%s-%d' % (e, y)] = {des: {form: {D: cell(R, spec, des, form, D) for D in DS} for form in FORMS} for des in DES}
            print('done %s %d' % (e, y), file=sys.stderr)
    write(out, ALL, CHK, eng, reps)


if __name__ == '__main__':
    main()
