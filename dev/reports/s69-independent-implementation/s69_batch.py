"""S69: run seeds lo..hi of one environment and row in parallel, write per-seed results, and compare them with the reference
(exact, then the 500-seed two-standard-error test of 00-START-HERE.md)."""
import os
import sys
import json
import math
import time
import multiprocessing as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _one(args):
    packet, env, row, seed = args
    import s69_main as M
    try:
        return seed, M.run_seed(packet, env, row, seed), None
    except Exception as e:  # report and go on: a seed that fails is a finding
        import traceback
        return seed, None, traceback.format_exc()


def batch(packet, env, row, lo, hi, out, jobs):
    t0 = time.time()
    seeds = list(range(lo, hi + 1))
    res = {}
    errs = {}
    with mp.Pool(jobs) as pool:
        for seed, r, err in pool.imap_unordered(_one, [(packet, env, row, s) for s in seeds], chunksize=2):
            if err:
                errs[seed] = err
            else:
                res[seed] = r
    keys = sorted(set(k for r in res.values() for k in r))
    data = {'env': env, 'row': row, 'lo': lo, 'hi': hi, 'seconds': round(time.time() - t0, 1), 'errors': {str(k): v for k, v in errs.items()},
            'seeds': {k: [res[s].get(k) if s in res else None for s in seeds] for k in keys}}
    if out:
        with open(out, 'w') as f:
            json.dump(data, f)
    print('%s %s seeds %d-%d: %d ran, %d failed, %.0f s' % (env, row, lo, hi, len(res), len(errs), time.time() - t0))
    return data
