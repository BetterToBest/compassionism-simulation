"""Do the two constants with no source enter the released figures? (v5.5, study page, "What would have to be true")

Copies harness.js and index.html into three scratch folders, raises one constant in each copy (CCO cost relief at the reference BU; PTF and PTH
inflation damping) and runs the release rows of the Adverse environment (outside inflation is the only place damping can act) on a few seeds.
It then compares every output line with the unchanged copy, ignoring the run-time line.
  CCO relief:  every line must be identical.
  Damping:     only lines of the optional row labelled "the two former stand-ins on" may differ.
Usage: python3 dev/tools/unsourced_check.py [seeds=4] [years=8]   Writes dev/runs/unsourced-constants-check.txt; exit 1 on failure."""
import os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
seeds = sys.argv[1] if len(sys.argv) > 1 else '4'
years = sys.argv[2] if len(sys.argv) > 2 else '8'
OPTIONAL_ROW = 'the two former stand-ins on'


def make(tmp, name, edits):
    d = os.path.join(tmp, name); os.makedirs(d)
    shutil.copy(os.path.join(ROOT, 'harness.js'), d); shutil.copy(os.path.join(ROOT, 'package.json'), d)
    os.symlink(os.path.join(ROOT, 'node_modules'), os.path.join(d, 'node_modules'))
    h = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    for pat, rep in edits:
        h, n = re.subn(pat, rep, h)
        if n == 0: sys.exit('pattern not found: ' + pat)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h)
    return d


def run(d):
    out = subprocess.run(['node', 'harness.js', 'testbed', seeds, 'release', 'adv', '--years=' + years], cwd=d, capture_output=True, text=True).stdout
    return [l for l in out.split('\n') if not re.search(r'\| \d+ s ---|\(\d+(\.\d+)? min\)', l)]


with tempfile.TemporaryDirectory() as tmp:
    base = run(make(tmp, 'base', []))
    relief = run(make(tmp, 'relief', [(r'CCO_RELIEF_AT_REF:0\.20,', 'CCO_RELIEF_AT_REF:0.35,')]))
    damp = run(make(tmp, 'damp', [(r'ptfAdoptFrac\*0\.5\)', 'ptfAdoptFrac*0.9)'), (r'pthMemberFrac\*0\.10\)', 'pthMemberFrac*0.5)')]))
diff_relief = [l for a, l in zip(base, relief) if a != l]
diff_damp = [l for a, l in zip(base, damp) if a != l]
bad_damp = [l for l in diff_damp if OPTIONAL_ROW not in l]
ok = len(base) > 100 and len(base) == len(relief) == len(damp) and not diff_relief and not bad_damp and diff_damp
lines = ['Do the constants with no source enter the released figures? (dev/tools/unsourced_check.py %s %s; Adverse environment, release rows, %s seeds, %s years)' % (seeds, years, seeds, years),
         'output lines compared: %d' % len(base),
         'CCO relief raised from 0.20 to 0.35 at the reference BU: %d lines differ (must be 0)' % len(diff_relief),
         'PTF damping 0.5 -> 0.9 and PTH damping 0.10 -> 0.5: %d lines differ, %d of them outside the optional row "%s" (must be 0; the optional row must differ)' % (len(diff_damp), len(bad_damp), OPTIONAL_ROW),
         'RESULT: ' + ('PASS' if ok else 'FAIL')]
print('\n'.join(lines))
open(os.path.join(ROOT, 'dev', 'runs', 'unsourced-constants-check.txt'), 'w').write('\n'.join(lines) + '\n')
sys.exit(0 if ok else 1)
