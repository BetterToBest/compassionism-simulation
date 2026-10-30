"""S34 (Oct 30, 2026; preregistration research-update prereg/s34-baseline-realism.md, Q5): PolicyEngine-US's SNAP, EITC and refundable Child Tax Credit
for the six households of dev/tools/sn_households.js, beside the engine's.

PolicyEngine-US (https://github.com/PolicyEngine/policyengine-us, AGPL-3.0; installed with `pip install policyengine-us`, not vendored here; its version
is recorded in the output). Each household lives in Florida (SNAP's gross income limit at 200% of the poverty guideline under broad-based categorical
eligibility, and no state income tax, so no state credit enters); the adults are 30 and 32, the couple is married filing jointly, children are dependants.
Rent: the engine's housing line (MIT's HUD rent with utilities), entered as pre-subsidy rent on the head; no separate utility expense is entered, so no
standard utility allowance applies (the engine's housing line already holds utilities). Childcare: the engine's line, entered as pre-subsidy childcare
expenses on the children under 13, youngest first, at the engine's first, second and third-child amounts. The tax credits are for tax year 2025; SNAP is the
January 2026 monthly benefit (fiscal year 2026, the allotments the engine holds) times 12, and, beside it, PolicyEngine's calendar-2025 total.

Usage: python dev/tools/pe_households.py ENGINE_JSON OUT_JSON   (ENGINE_JSON from `node dev/tools/sn_households.js --out=...`)
"""
import json, sys
from importlib.metadata import version
from policyengine_us import Simulation
E = json.load(open(sys.argv[1]))
SNAP_STEPS = ['snap_gross_income', 'snap_earned_income_deduction', 'snap_standard_deduction', 'snap_dependent_care_deduction',
              'snap_excess_shelter_expense_deduction', 'snap_net_income', 'snap_max_allotment', 'meets_snap_gross_income_test', 'is_snap_eligible']
def situation(h):
    people, kids = {}, sorted(h['kids'])
    names = ['adult1', 'adult2'][:h['nA']]
    for i, n in enumerate(names):
        people[n] = {'age': {'2025': 30 + 2*i, '2026': 31 + 2*i}, 'employment_income': {'2025': h['earn']/h['nA'], '2026': h['earn']/h['nA']}}
    people['adult1']['pre_subsidy_rent'] = {'2025': h['rent'], '2026': h['rent']}
    cc = [12913.68, 11637.65, 7823.75]; nc = 0
    for j, age in enumerate(kids):
        k = 'child%d' % (j + 1); c = 0.0
        if age < 13: c = cc[min(nc, 2)]; nc += 1
        people[k] = {'age': {'2025': age, '2026': age}, 'is_tax_unit_dependent': {'2025': True, '2026': True},
                     'pre_subsidy_childcare_expenses': {'2025': c, '2026': c}}
    m = list(people)
    s = {'people': people, 'tax_units': {'tu': {'members': m}}, 'spm_units': {'su': {'members': m}}, 'families': {'f': {'members': m}},
         'households': {'hh': {'members': m, 'state_code': {'2025': 'FL', '2026': 'FL'}}}}
    s['marital_units'] = {'mu': {'members': names}} if h['nA'] == 2 else {'mu': {'members': names}}
    for j in range(len(kids)): s['marital_units']['muk%d' % j] = {'members': ['child%d' % (j + 1)]}
    return s
rows = []
for h in E['households']:
    sim = Simulation(situation=situation(h))
    snapJan = float(sim.calculate('snap', '2026-01')[0])*12
    pe = {'snap': snapJan, 'snap2025': float(sim.calculate('snap', 2025).sum()), 'eitc': float(sim.calculate('eitc', 2025)[0]),
          'ctc': float(sim.calculate('refundable_ctc', 2025)[0]), 'filingStatus': str(sim.calculate('filing_status', 2025)[0])}
    steps = {}
    for v in SNAP_STEPS:
        try: steps[v] = float(sim.calculate(v, '2026-01')[0])*(1 if v.startswith(('meets', 'is_')) else 12)
        except Exception as ex: steps[v] = 'n/a (%s)' % type(ex).__name__
    pe['snapSteps'] = steps
    diff = {k: h['engine'][k] - pe[k] for k in ('snap', 'eitc', 'ctc')}
    gap = {k: abs(diff[k]) > max(100, 0.05*max(abs(pe[k]), abs(h['engine'][k]))) for k in diff}
    rows.append(dict(h, policyengine=pe, diff=diff, gap=gap))
    print(h['id'], h['label'], {k: round(h['engine'][k]) for k in diff}, {k: round(pe[k]) for k in diff}, {k: round(v) for k, v in diff.items()}, gap)
out = {'_meta': {'what': 'S34 Q5: engine against PolicyEngine-US, six households', 'policyengine_us': version('policyengine-us'),
                 'policyengine_core': version('policyengine-core'), 'command': 'python dev/tools/pe_households.py ' + ' '.join(sys.argv[1:]),
                 'gapRule': 'a difference above the larger of $100 a year and 5% (prereg)', 'engineMeta': E['_meta']}, 'households': rows}
json.dump(out, open(sys.argv[2], 'w'), indent=1)
