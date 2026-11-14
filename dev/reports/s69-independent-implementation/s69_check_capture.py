"""Checks that the supply-path settings derived by tbBaseS's rule equal the captured ones in Reference and Adverse (so the Stress derivation is sound)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s69_main as M
cfg = M.load(sys.argv[1] if len(sys.argv) > 1 else M.DEFAULT_PACKET)
RUN_STATE = {'DR_ACC', 'EMS', 'LFS', 'SNS', 'SPD', 'DR_PL', 'BGS', 'FWS', 'PJS', 'ESS', 'SPS', 'MLS', 'PDS', 'JNS', 'THETA_DENS'}
for env in ('ref', 'adv'):
    st0, p0, o0 = M.state_of(cfg, env, 1)
    for row, (iS, iR) in M.CAPTURE.items():
        cs, cp, co = M.state_of(cfg, env, iS)
        ds, dp, do = st0, p0, dict(o0, rep52=False, giniNN1=False)
        ds = dict(ds)
        if row == 'main':
            sm, pm, om = M.state_of(cfg, env, 3)
            ds['PATHWAY_OFF'] = sm['PATHWAY_OFF']
            do['noDamp'] = om['noDamp']
        bad = [k for k in set(cs) | set(ds) if k not in RUN_STATE and cs.get(k) != ds.get(k)] + [k for k in set(co) | set(do) if co.get(k) != do.get(k)] + (['preset'] if cp != dp else [])
        print(env, row, 'derived supply-path settings equal the captured ones' if not bad else 'differ: %s' % bad)
