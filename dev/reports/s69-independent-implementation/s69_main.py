"""S69 phase 1: the candidate main row of round 2 and its no-programme run, written again from the packet.

  python3 -I s69_main.py --env ref --row base --seed 1        one run, prints its keys as JSON
  python3 -I s69_main.py --env ref --row base --seed 1 --cmp  the same, compared key by key with the reference
  python3 -I s69_main.py --env ref --row base --seeds 1-500 --out results/ref-base.json --jobs 4

--row base is the no-programme run (rows[0] of the reference), --row main the candidate main row (rows[1]).
The packet is read from ../../packets/s69-main-row.zip unless --packet names it.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import argparse
import json
import math
import time
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PACKET = os.path.join(HERE, '..', '..', 'packets', 's69-main-row.zip')
# The configuration file captures each tbRun call of seed 1: for each row, the supply-path run (tbBaseS) first, then the row itself.
CAPTURE = {'base': (0, 1), 'main': (2, 3)}

_CFG = None


def load(packet):
    global _CFG
    if _CFG is None:
        with zipfile.ZipFile(packet) as z:
            _CFG = json.loads(z.read('main-row-config.json'))
        with open(os.path.join(HERE, 'code_tables.json')) as f:
            _CFG['_tables'] = json.load(f)
    return _CFG


def state_of(cfg, env, i):
    rows = cfg['envs'][env]['rows']
    e = rows[i]
    st = dict(cfg['atLoad'])
    for k, v in e['switchesDifferentFromLoad'].items():
        if k in ('S3_CACHE', 'HL_GOVREF', 'HHS', 'TB_BLEI_NET'):
            continue
        st[k] = v
    return st, e['preset'], e['options']


def supply_state(cfg, env, row):
    """The supply-path run's settings (tbBaseS, MODEL_SPEC 13.2 fx.sp). Reference and Adverse capture them; Stress's file holds only the two rows'
    own runs, so they are derived by tbBaseS's rule: the no-programme row's settings with the programme-only options at their defaults (here
    rep52 and giniNN1 off), keeping the row's economy-wide settings (for the main row, its pathway setting and noDamp). Checked: in Reference and
    Adverse this derivation gives exactly the captured settings (s69_check_capture.py)."""
    if env != 'st':
        return state_of(cfg, env, CAPTURE[row][0])
    st, p, o = state_of(cfg, env, 0)
    o = dict(o)
    o['rep52'] = False
    o['giniNN1'] = False
    st = dict(st)
    if row == 'main':
        sm, pm, om = state_of(cfg, env, 1)
        st['PATHWAY_OFF'] = sm['PATHWAY_OFF']
        o['noDamp'] = om['noDamp']
    return st, p, o


def row_state(cfg, env, row):
    if env != 'st':
        return state_of(cfg, env, CAPTURE[row][1])
    return state_of(cfg, env, 0 if row == 'base' else 1)


def run_seed(packet, env, row, seed):
    from s69_core import tb_run
    cfg = load(packet)
    tables = cfg['_tables']
    st0, p0, o0 = supply_state(cfg, env, row)
    spd = []
    tb_run(st0, tables, p0, seed, o0, None, spd)
    st, p, o = row_state(cfg, env, row)
    return tb_run(st, tables, p, seed, o, spd)


def ref_rows(packet, env):
    with zipfile.ZipFile(packet) as z:
        return json.loads(z.read('reference/s69-%s-1-500.json' % env))['rows']


def compare(mine, ref, seed, show=40):
    bad = []
    n = 0
    for k, rv in ref.items():
        v = rv[seed - 1]
        if k not in mine:
            bad.append((k, v, None, 'missing'))
            continue
        n += 1
        m = mine[k]
        d = abs(m - v)
        rel = d / max(abs(v), abs(m), 1e-300) if d > 0 else 0
        if rel > 1e-9 and d > 1e-12:
            bad.append((k, v, m, rel))
    extra = [k for k in mine if k not in ref]
    return n, bad, extra


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--env', default='ref')
    ap.add_argument('--row', default='base')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--seeds', default=None)
    ap.add_argument('--out', default=None)
    ap.add_argument('--jobs', type=int, default=1)
    ap.add_argument('--cmp', action='store_true')
    ap.add_argument('--packet', default=DEFAULT_PACKET)
    a = ap.parse_args()
    if a.seeds:
        lo, hi = [int(x) for x in a.seeds.split('-')]
        from s69_batch import batch
        batch(a.packet, a.env, a.row, lo, hi, a.out, a.jobs)
        return
    t0 = time.time()
    r = run_seed(a.packet, a.env, a.row, a.seed)
    dt = time.time() - t0
    if a.cmp:
        rows = ref_rows(a.packet, a.env)
        ref = rows[0 if a.row == 'base' else 1]['seeds']
        n, bad, extra = compare(r, ref, a.seed)
        print('%s %s seed %d: %d keys compared, %d differ (relative > 1e-9), %d of mine not in the reference; %.1f s' % (a.env, a.row, a.seed, n, len(bad), len(extra), dt))
        for b in sorted(bad, key=lambda x: x[0])[:200]:
            print('  %-14s ref %-24r mine %-24r %s' % b)
    else:
        print(json.dumps(r))


if __name__ == '__main__':
    main()
