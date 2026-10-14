"""v5.5 (Oct 2026; ledger step s133): write the study page's data file from the finished 500-seed study (s137) and its follow-up Sobol (s137b).

Usage: python3 dev/tools/study_data.py           writes data/studies/s137.json
       python3 dev/tools/study_data.py --check   exits 1 if that file is not what this script writes from dev/runs/s137 and dev/runs/s137b

The page (study.html) holds no figure. Every number it shows is a path into the file written here, printed through site/findings.js, and
dev/tools/check_figures.js compares each one with the data. The figures are the study's own (dev/reports/v5-30-s137-results.md), copied, not recomputed;
the only arithmetic here is a sign change (a fall shown as a positive number of points), recorded under "drv".
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(ROOT, 'data', 'studies', 's137.json')


def rj(p):
    with open(os.path.join(ROOT, p)) as f:
        return json.load(f)


ENVS = ['ref', 'adv', 'st']
ENVN = {'ref': 'Reference', 'adv': 'Adverse', 'st': 'Stress'}
ROWS = ['off', 'ASN', 'BSN', 'CSN', 'BSNcau', 'BSNhigh', 'CSNcau', 'CSNhigh', 'SN', 'ASNtLo', 'ASNtHi', 'BSNfl', 'CSNfl']
KEEP = ['fgt0PY', 'fgt2PY', 'bOAPy', 'hhCostKidPY', 'pov', 'pLev20', 'hlTax', 'hlRate', 'hlPaid', 'snAll', 'hlGovB', 'hlSB', 'hlXtra']
SOB_OUT = ['fgt0PY', 'pov', 'bOAPy', 'cost', 'endoAnn']
SOB_IN = ['part', 'bu', 'rho', 'spend', 'payCut', 'bleiBonus', 'tax']
SOB_NAME = {'part': 'Participation', 'bu': 'BU amount', 'rho': 'Income effect on earnings', 'spend': 'Share of extra cash spent',
            'payCut': 'Pay cut after job loss', 'bleiBonus': 'BLEI wage bonus', 'tax': 'Conversion tax'}
IN_NAME = dict(SOB_NAME, eps='Wage elasticity', pthUptake='PTH uptake', maxMult='Top conversion rate', ptfOther='PTF cut outside food and housing',
               ptfShare='PTF membership', pthExit='Chance a PTH member leaves')
OUT_NAME = {'fgt0PY': 'Basket poverty', 'pov': 'Too little wealth', 'bOAPy': 'BLEI poverty', 'cost': 'Programme cost', 'endoAnn': 'Programme inflation'}


def engine_constants():
    """the two inputs with no source, read from the engine in index.html (never typed): CCO cost relief at the reference BU and its cap; PTF and PTH inflation damping"""
    h = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    g = lambda pat: float(re.search(pat, h).group(1))
    return {'ccoRelief': round(100*g(r'CCO_RELIEF_AT_REF:([0-9.]+)'), 6), 'ccoCap': round(100*g(r'CCO_RELIEF_CAP:([0-9.]+)'), 6),  # percent, as the p0 format reads them
            'ptfDamp': g(r'inflRate\*=\(1-ptfAdoptFrac\*([0-9.]+)\)'), 'pthDamp': g(r'inflRate\*=\(1-pthMemberFrac\*([0-9.]+)\)')}


def pick(row):
    o = {k: {m: row[k][m] for m in KEEP if m in row[k]} for k in ('base', 'prog')}
    o['d'] = {m: row['d'][m] for m in KEEP if m in row['d']}
    o['vsRef'] = {m: row['vsRef'][m] for m in ('fgt0PY', 'pov') if m in row.get('vsRef', {})}
    o['costs'] = row['costs']
    return o


def build():
    V, FL, TX = {}, {}, {}
    prov = {}
    for e in ENVS:
        t = rj('dev/runs/s137/s137table-%s.json' % e)
        V[e] = {r: pick(t['rows'][r]) for r in ROWS if r in t['rows']}
        for name, D in (('flat', FL), ('thx', TX)):
            f = rj('dev/runs/s137/s137%s-%s.json' % (name, e))
            D[e] = {r: pick(f['rows'][r]) for r in ('ASN', 'BSN') if r in f['rows']}
        prov[e] = {'commit': t['_meta']['manifest']['commit'], 'command': t['_meta']['command']}
    so = rj('dev/runs/s137b/gsa-sobol-st-sc.json')['result']
    sobol = {o: {i: {'ST': so['indices'][o][i]['ST'], 'Sc': so['indices'][o][i]['Sc'], 'ciST': so['ci'][o][i]['ST'], 'ciSc': so['ci'][o][i]['Sc']}
                 for i in SOB_IN} for o in SOB_OUT}
    mo = rj('dev/runs/s137/gsa-morris-st.json')['result']
    morris = {}
    for o in OUT_NAME:
        lead = mo['leaders'][o]
        morris[o] = {'same': lead['same'], 'top': [{'name': IN_NAME[i], 'muStar': mo['inputs'][i][o]['muStar']} for i in lead['joined']]}
    drv = {'fall': {e: -V[e]['ASN']['d']['fgt0PY'][0] for e in ENVS},
           'fallRefB': -V['ref']['BSN']['d']['fgt0PY'][0], 'flatPovFall': {e: -FL[e]['ASN']['d']['pov'][0] for e in ENVS},
           'ptsLess': {e: V[e]['BSN']['vsRef']['fgt0PY'][0] for e in ENVS}}
    R = {'schema': 'study-1', 'id': 's137', 'version': '5.5', 'date': '2026-10-13', 'tag': 'v5.5.0',
         'title': 'Health financing, prices and what the results depend on',
         'summary': 'The 500-seed study of three health systems with and without Compassionism, the price channel, and which inputs explain the spread.',
         'meta': {'seeds': 500, 'agents': 500, 'years': 20, 'envs': {e: ENVN[e] for e in ENVS}, 'prov': prov,
                  'sobolSeeds': so['seeds'], 'sobolBase': so['N'], 'morrisPaths': mo['R'], 'morrisSeeds': mo['seeds'],
                  'report': 'dev/reports/v5-30-s137-results.md', 'runs': 'dev/runs/s137/ and dev/runs/s137b/'},
         'v': V, 'flat': FL, 'thx': TX, 'sobol': sobol, 'morris': morris, 'drv': drv, 'unsourced': engine_constants(),
         'chart': {'inputs': SOB_IN, 'inputNames': SOB_NAME, 'outcomes': SOB_OUT, 'outcomeNames': OUT_NAME}}
    R.update(content(R))
    return R


# ---- the page's words and tables: every number is a {{path|format}} token or a {src, f} part -------------------------------------------------

def N(src, f):
    return {'src': src, 'f': f}


def rng(path, f='s1'):  # a value with its 95% interval underneath
    return {'p': [N(path + '.0', f)], 's': [N(path + '.1', f), ' to ', N(path + '.2', f)]}


def cell(*ps, s=None):
    c = {'p': list(ps)}
    if s:
        c['s'] = list(s)
    return c


def txt(x):
    return {'p': [x]}


def content(R):
    ROW3 = [('A', 'ASN', 'Today\'s system'), ('B', 'BSN', 'Single payer'), ('C', 'CSN', 'Single payer with a private layer')]
    tables, T = [], {}

    # Table 1. basket poverty
    rows = []
    for k, r, lab in ROW3:
        rows.append([txt(lab + ' (' + k + ')')] + [cell(N('v.%s.%s.base.fgt0PY' % (e, r), 'p1'), ' to ', N('v.%s.%s.prog.fgt0PY' % (e, r), 'p1'),
                                                        s=['effect ', N('v.%s.%s.d.fgt0PY.0' % (e, r), 's1'), ' points (', N('v.%s.%s.d.fgt0PY.1' % (e, r), 's1'), ' to ',
                                                           N('v.%s.%s.d.fgt0PY.2' % (e, r), 's1'), ')']) for e in ENVS])
    rows.append([txt('Reference line: no health setting, no safety net')] + [cell(N('v.%s.off.base.fgt0PY' % e, 'p1'), ' to ', N('v.%s.off.prog.fgt0PY' % e, 'p1'),
                                                                                 s=['effect ', N('v.%s.off.d.fgt0PY.0' % e, 's1'), ' points']) for e in ENVS])
    tables.append({'id': 'basket-poverty', 'title': 'Basket poverty, adult-years: no programme to with Compassionism', 'columns': ['Health setting'] + [ENVN[e] for e in ENVS], 'rows': rows})

    # Table 2. other measures
    meas = [('fgt2PY', 'Poverty depth (FGT2)', 'n1'), ('bOAPy', 'BLEI poverty, adult-years', 'p1'), ('hhCostKidPY', 'Children below the cost of living, child-years', 'p1'),
            ('pov', 'Too little wealth, adults, year 20', 'p1')]
    cases = [('ref', 'ASN', 'Reference, A'), ('ref', 'BSN', 'Reference, B'), ('ref', 'CSN', 'Reference, C'), ('adv', 'ASN', 'Adverse, A'), ('adv', 'BSN', 'Adverse, B'),
             ('st', 'ASN', 'Stress, A'), ('st', 'BSN', 'Stress, B')]
    rows = []
    for e, r, lab in cases:
        row = [txt(lab)]
        for m, _, f in meas:
            b, p = 'v.%s.%s.base.%s' % (e, r, m), 'v.%s.%s.prog.%s' % (e, r, m)
            row.append(cell(N(b, f), ' to ', N(p, f), s=['effect ', N('v.%s.%s.d.%s.0' % (e, r, m), 's1')]))
        rows.append(row)
    tables.append({'id': 'other-measures', 'title': 'Other measures: no programme to with Compassionism, and the paired effect', 'columns': ['Cell'] + [m[1] for m in meas], 'rows': rows})

    # Table 3. costs
    rows = []
    for e in ENVS:
        for k, r, lab in ROW3:
            c = 'v.%s.%s.costs' % (e, r)
            row = [txt('%s, %s' % (ENVN[e], k)), cell(N(c + '.prog.cost', 'usd'))]
            if k == 'A':
                row += [txt('none'), cell(N(c + '.base.hlPaid', 'usd'), ' / ', N(c + '.prog.hlPaid', 'usd')), cell(N(c + '.base.snAll', 'usd'), ' / ', N(c + '.prog.snAll', 'usd')), txt('')]
            else:
                row += [cell(N(c + '.base.hlTax', 'usd'), s=['rate ', N('v.%s.%s.base.hlRate' % (e, r), 'p1')]),
                        cell(N(c + '.base.hlPaid', 'usd'), ' / ', N(c + '.prog.hlPaid', 'usd')), cell(N(c + '.base.snAll', 'usd'), ' / ', N(c + '.prog.snAll', 'usd')),
                        cell(N(c + '.base.hlGovB', 'usd'))]
            row.append(cell(N(c + '.base.hlXtra', 'usd')) if k == 'C' else txt(''))
            rows.append(row)
    tables.append({'id': 'costs', 'title': 'Government\'s costs, beside the results: per adult-year',
                   'columns': ['Cell', 'Programme cost, with Compassionism', 'Health tax, no programme', 'Household health bill, no programme / with', 'Today\'s safety-net outlays (not financed in the model), no programme / with',
                               'Government\'s share of the plan', 'Paid to private plans above their enrollees\' public cost'], 'rows': rows})

    # Table 4. single payer's range (Reference)
    rg = [('A', 'ASN', 'Today\'s system (A, for comparison)'), ('B', 'BSN', 'B, central'), ('Bc', 'BSNcau', 'B, cautious'), ('Bh', 'BSNhigh', 'B, high cost'),
          ('C', 'CSN', 'C, central'), ('Cc', 'CSNcau', 'C, cautious'), ('Ch', 'CSNhigh', 'C, high cost')]
    rows = []
    for k, r, lab in rg:
        p = 'v.ref.%s' % r
        row = [txt(lab), cell(N(p + '.base.hlSB', 'usd')) if k != 'A' else txt('')]
        row.append(cell(N(p + '.base.hlRate', 'p1')) if k != 'A' else txt('none'))
        row.append(cell(N(p + '.base.fgt0PY', 'p1'), ' to ', N(p + '.prog.fgt0PY', 'p1'), s=['effect ', N(p + '.d.fgt0PY.0', 's1')]))
        row.append(cell(N(p + '.vsRef.fgt0PY.0', 's2'), s=[N(p + '.vsRef.fgt0PY.1', 's2'), ' to ', N(p + '.vsRef.fgt0PY.2', 's2')]) if k != 'A' else txt(''))
        rows.append(row)
    tables.append({'id': 'single-payer-range', 'title': 'Single payer\'s range (Reference): the Yale preprint\'s central, cautious and high-cost cases',
                   'columns': ['Cost case', 'Plan spending per person-year, no programme', 'Health tax rate', 'Basket poverty, no programme to with Compassionism', 'Change in Compassionism\'s effect against A'], 'rows': rows})

    # Table 5. the price channel
    prow = []
    def pp(env, row, lab_, tail, f):
        prow.append([txt(lab_)] + [cell(N('%s.%s.%s.%s' % (src, env, row, tail), f)) for src in ('flat', 'v', 'thx')])
    for e in ENVS:
        pp(e, 'ASN', 'Basket poverty, ' + ENVN[e], 'd.fgt0PY.0', 's1')
    for e in ENVS:
        pp(e, 'ASN', 'Too little wealth, ' + ENVN[e], 'd.pov.0', 's1')
    pp('st', 'ASN', 'BLEI poverty, Stress', 'd.bOAPy.0', 's1')
    pp('ref', 'ASN', 'Price level at year 20 with Compassionism, Reference (year 0 = 1)', 'prog.pLev20', 'lev')
    pp('ref', 'ASN', 'Programme cost, Reference', 'costs.prog.cost', 'usd')
    pp('ref', 'BSN', 'B\'s change to the effect on basket poverty, Reference', 'vsRef.fgt0PY.0', 's2')
    tables.append({'id': 'price-channel', 'title': 'Compassionism\'s effect under today\'s system with the safety net, by price rule', 'columns': ['Measure', 'Prices flat', 'Prices as released', 'Price responses 1.5 times'], 'rows': prow})

    # Table 6. Morris leaders in Stress
    rows = []
    for o in OUT_NAME:
        row = [txt(OUT_NAME[o])]
        cellp = []
        for i, t in enumerate(R['morris'][o]['top']):
            if i:
                cellp.append('; ')
            cellp += [t['name'] + ' ', N('morris.%s.top.%d.muStar' % (o, i), 'n1' if o != 'cost' else 'usd')]
        row.append({'p': cellp})
        row.append(txt('Yes' if R['morris'][o]['same'] else 'No'))
        rows.append(row)
    tables.append({'id': 'morris', 'title': 'Screening (Morris), Stress: the six inputs that move each outcome most, with the size of the move over the input\'s range',
                   'columns': ['Outcome', 'Leading inputs, with their effect over the input\'s range (points; dollars for cost; points a year for inflation)', 'Same leaders in both seed blocks?'], 'rows': rows})

    # Table 7. Sobol
    rows = []
    for i in SOB_IN:
        row = [txt(SOB_NAME[i])]
        for o in SOB_OUT:
            s = 'sobol.%s.%s' % (o, i)
            row.append(cell(N(s + '.ST', 'n2'), s=['first-order ', N(s + '.Sc', 'n2')]))
        rows.append(row)
    tables.append({'id': 'sobol', 'title': 'Follow-up Sobol, Stress: share of the spread each input explains (total index; centred first-order index beneath)',
                   'columns': ['Input'] + [OUT_NAME[o] for o in SOB_OUT], 'rows': rows})

    # Table 8. what would have to be true
    def mo(o, name):
        for i, t in enumerate(R['morris'][o]['top']):
            if t['name'] == name:
                return N('morris.%s.top.%d.muStar' % (o, i), 'usd' if o == 'cost' else 'n1')
        raise KeyError((o, name))
    st = lambda o, i: N('sobol.%s.%s.ST' % (o, i), 'n2')
    wt = [
        [txt('Basket poverty falls with Compassionism, in every economy.'),
         txt('Enough adults take part, and the BU amount is as designed: both are choices about the programme\'s size, and they move the answer most. The income effect on earnings (how far people cut paid work when given money) is inside its sourced range and no larger.'),
         {'p': ['Over its range, participation moves it ', mo('fgt0PY', 'Participation'), ' points, the BU amount ', mo('fgt0PY', 'BU amount'), ' and the income effect on earnings ', mo('fgt0PY', 'Income effect on earnings'),
                '. Share of the spread explained: participation ', st('fgt0PY', 'part'), ', BU amount ', st('fgt0PY', 'bu'), ', income effect ', st('fgt0PY', 'rho'), '.']}],
        [txt('"Too little wealth" rises with Compassionism.'),
         txt('Programme spending raises prices the way the model\'s price rule says, and people spend about the share of extra cash the model assumes. If prices did not respond, the result would reverse.'),
         {'p': ['With no price response it falls instead (', N('drv.flatPovFall.ref', 'n1'), ' points lower in Reference). The share of extra cash spent explains ', st('pov', 'spend'), ' of the spread, the income effect ', st('pov', 'rho'),
                ', participation ', st('pov', 'part'), ', the pay cut after job loss ', st('pov', 'payCut'), '.']}],
        [txt('BLEI poverty (the 30-days-of-basic-living measure) falls.'),
         txt('Take-up is high enough: almost all of the spread in this result is how many adults take part.'),
         {'p': ['Share of the spread explained: participation ', st('bOAPy', 'part'), ', BU amount ', st('bOAPy', 'bu'), '. Over its range participation moves it ', mo('bOAPy', 'Participation'), ' points.']}],
        [txt('The programme costs what the study reports.'),
         txt('Take-up and the BU amount stay in the ranges swept. Cost is mostly their product; the conversion tax and the top conversion rate matter much less.'),
         {'p': ['Over its range participation moves yearly cost by ', mo('cost', 'Participation'), ' and the BU amount by ', mo('cost', 'BU amount'), '. Share of the spread explained: participation ', st('cost', 'part'), ', BU amount ', st('cost', 'bu'), '.']}],
        [txt('Programme inflation is as reported.'),
         txt('The model\'s price rule, which links the programme\'s spending to the price level, is right in kind. It is not calibrated to outside evidence on benefit-funded demand.'),
         {'p': ['Participation moves it ', mo('endoAnn', 'Participation'), ' points a year over its range and explains ', st('endoAnn', 'part'), ' of the spread; the BU amount explains ', st('endoAnn', 'bu'), '.']}],
        [txt('Single payer lowers poverty.'),
         txt('The Yale preprint\'s savings (not peer reviewed) are roughly right, or the financing rule alone does the work.'),
         txt('The study ran the preprint\'s central case, a cautious case and a high-cost case with no savings; see the single-payer table above. Poverty still falls in the cautious case; in the high-cost case any gain comes from the financing rule.')],
    ]
    tables.append({'id': 'wwtbt', 'title': 'What would have to be true for each headline result', 'columns': ['The result', 'What would have to be true', 'What the study found when it varied the inputs (Stress)'], 'rows': wt})

    # Table 9. the two constants with no source
    tables.append({'id': 'unsourced', 'title': 'Two constants with no source',
                   'columns': ['Constant', 'Value', 'Source', 'Do the released figures use it?'],
                   'rows': [[txt('CCO (Creative Currency Octaves) cost relief: how far CCO members\' cost of living is cut at the reference BU, and the ceiling on that cut'),
                             {'p': [N('unsourced.ccoRelief', 'p0'), ' of the basket (ceiling ', N('unsourced.ccoCap', 'p0'), ')']},
                             txt('None found. The decision log records the search; the value is a placeholder.'),
                             txt('No. Raising it left every released row unchanged when tested. It belongs to the earlier engine.')],
                            [txt('Inflation damping by community businesses (PTF, which cut prices) and community housing (PTH): how much of outside inflation they absorb, applied to the overall inflation rate'),
                             {'p': ['PTF ', N('unsourced.ptfDamp', 'n1'), ', PTH ', N('unsourced.pthDamp', 'n1'), ' (times the share of people who joined)']},
                             txt('None found. The decision log records the search; no source gives its size.'),
                             txt('Only in one optional row, off by default and labelled "the two former stand-ins on"; no main row. Raising both changed that row and no other.')]]})
    T['tables'] = tables

    X = {}
    X['intro'] = ('The 500-seed study, run on a rented server, ran the same 500 simulated populations (500 adults each, 20 years) with and without Compassionism under three health systems and three economies, '
                  'and then asked which inputs the answer depends on. Every comparison is paired: the same people and the same luck in both runs. Figures are the study\'s, copied from its results report.')
    X['basket'] = ('Compassionism lowers basket poverty in every combination of health system and economy. In Reference under today\'s health system it falls by {{drv.fall.ref|n1}} points '
                   '(Adverse {{drv.fall.adv|n1}}, Stress {{drv.fall.st|n1}}). Single payer lowers poverty before Compassionism starts, so Compassionism\'s own drop is '
                   '{{drv.ptsLess.ref|n1}} points smaller under it in Reference, and the level reached with both is the lowest of the three settings.')
    X['cap.basket'] = ('Basket poverty counts the adult-years spent below the cost of living. Results for B (single payer) and C (single payer with a private layer) depend on single-payer savings taken from the Yale preprint (Galvani, Pandey, Wells and Ye, medRxiv 2026), '
                       'which is not peer reviewed; their range is in the table on single payer. "With Compassionism" is the v5.4 release row. Today\'s safety net is on in both runs of rows A, B and C. Intervals are 95% intervals.')
    X['cap.other'] = ('Poverty depth (FGT2) weighs each person\'s shortfall by its square, so the deepest poverty counts most. "Too little wealth" rises with Compassionism in every combination of health system and economy, as in the v5.4 release: '
                      'people in the programme hold less cash once their basket is covered. The price-channel table shows this rise comes from the model\'s price response, not from health financing. '
                      'In Stress, BLEI poverty (the days-of-basic-living measure) also rises slightly.')
    X['cap.costs'] = ('The safety net\'s outlays are today\'s programmes, paid in both runs; they are not programme cost. The model does not reconcile tax revenue with these outlays: it reports them, '
                      'it does not show that they are financed. Under A the household health bill is premiums and out-of-pocket costs. Under B and C it is the health tax less the employer\'s former premium share. '
                      'Government\'s share of the plan is held at its level in the matching run (same seed) without the programme.')
    X['single'] = ('The single-payer savings are inputs from the Yale preprint, not results of this model. The study ran the preprint\'s central case and two others. In the cautious case, savings are cut; '
                   'in the high-cost case providers are paid near commercial rates, so the savings vanish and only the added care remains. Single payer still lowers poverty with the cautious savings. '
                   'In the high-cost case the plan costs more per person than today\'s system, so any gain there comes from the financing rule, not from savings.')
    X['cap.single'] = 'Reference environment, today\'s safety net on. Adverse and Stress are in the study\'s data files. Cost cases are labelled in the first column.'
    X['price'] = ('The model raises essentials\' prices when more of them are bought, and the programme\'s spending also raises the general price level. With prices as released, "too little wealth" rises with Compassionism '
                  '(Reference: {{v.ref.ASN.d.pov.0|s1}} points). With no price response at all it falls instead ({{drv.flatPovFall.ref|n1}} points lower in Reference), and falls in every environment. '
                  'So the rise comes through the price response: programme inflation erodes cash savings, so more adults end with too little real wealth even though their basket is covered. '
                  'Making the responses stronger changes little, so what matters is whether the programme\'s inflation happens, not its strength. How strongly prices respond to benefit-funded demand is not settled.')
    X['cap.price'] = ('The flat column switches off every price response, including the programme\'s own inflation. It shows what prices do in the model; it is not a scenario anyone proposes. '
                      '"As released" carries the programme inflation the v5.4 release reports. In Adverse and Stress the flat runs keep the environments\' background inflation.')
    X['sens'] = ('Two methods ask which inputs the answer depends on. Screening (the Morris method, 1991) ranks how far each input moves an outcome over its range, on {{meta.morrisPaths|int}} random paths of {{meta.morrisSeeds|int}} paired runs (seeds) each. '
                 'The follow-up Sobol run (the Sobol method, Saltelli et al. 2010) splits the spread of each outcome among the inputs, with {{meta.sobolBase|int}} base points and {{meta.sobolSeeds|int}} paired runs (seeds) per point, in Stress. '
                 'Participation and the amount of BU paid explain most of the spread in poverty, BLEI poverty, cost and inflation. These are design choices about the programme\'s size, not uncertain facts about the world. '
                 'For basket poverty, the income effect on earnings is the one uncertain behavioural constant that matters. "Too little wealth" depends most on the share of extra cash people spend.')
    X['cap.morris'] = ('A noise check was set before the run: an input\'s effect counts as measured only if the two seed blocks agree to within a quarter of it. The leaders hardly differ between environments (Reference and Adverse are in the data files).')
    X['cap.sobol'] = ('The total index counts an input alone and together with others; the first-order index counts it alone. Where the totals add to more than the first-order indices the inputs act together. '
                      'The first Sobol run was too noisy for its first-order figures (several fell outside their range), so only this follow-up\'s are shown. Inputs with a total index of 0.01 or less on every outcome are left out: '
                      'wage elasticity, uptake of community housing (PTH), top conversion rate and the community-business (PTF) cut outside food and housing.')
    X['chart'] = ('Each bar is the share of the spread in one outcome that an input explains, alone and together with the others (the Sobol total index, Stress). A longer bar means the answer depends more on that input. '
                   'The line on each bar is its 95% interval. Pick an outcome to redraw the chart; every number is in the table below it.')
    X['true'] = ('A result holds only if some things are true. For each headline result this panel says what would have to be true, and what the study found when those inputs were varied. '
                 'It does not say they are true. It says where an economist should look first. Two constants have no source at all; they are named after the table.')
    X['cap.true'] = ('The two constants with no source do not enter the released figures: the study could not vary them, because they are not in the model that produced those figures. They are listed so a reviewer can check the claim, '
                     'and so that anyone who wants them to count knows a source is needed first. The check that raised each constant and compared every released row is dev/tools/unsourced_check.py, with its result in dev/runs/unsourced-constants-check.txt.')
    X['limits'] = ('All single-payer results rest on the Yale preprint\'s savings. The model does not reconcile tax revenue with today\'s safety-net outlays or with government\'s share of the plan. '
                   'The price response drives the "too little wealth" result and is not calibrated to outside evidence. The cost-of-living line is the unweighted state average. '
                   'The work rules of SNAP (food stamps) and a separate Child Tax Credit take-up are not modelled. The community businesses\' (PTF) health-sector cut under single payer is an upper reading. '
                   'The model has not yet been reviewed by an independent economist.')
    X['asof'] = 'Study run on a rented server on {{meta.seeds|int}} paired seeds; the follow-up Sobol ran in Stress only.'
    T['text'] = X
    T['sections'] = [
        {'id': 'basket', 'title': 'Basket poverty under three health systems', 'lead': 'basket', 'tables': ['basket-poverty'], 'note': 'cap.basket'},
        {'id': 'other', 'title': 'Other measures', 'lead': None, 'tables': ['other-measures'], 'note': 'cap.other'},
        {'id': 'costs', 'title': 'Government\'s costs, in a separate table', 'lead': None, 'tables': ['costs'], 'note': 'cap.costs'},
        {'id': 'single', 'title': 'Single payer depends on the Yale preprint', 'lead': 'single', 'tables': ['single-payer-range'], 'note': 'cap.single'},
        {'id': 'prices', 'title': 'The price channel', 'lead': 'price', 'tables': ['price-channel'], 'note': 'cap.price'},
        {'id': 'depends', 'title': 'What the results depend on', 'lead': 'sens', 'chart': 'chart', 'tables': ['morris', 'sobol'], 'note': 'cap.sobol'},
        {'id': 'true', 'title': 'What would have to be true', 'lead': 'true', 'tables': ['wwtbt', 'unsourced'], 'note': 'cap.true'},
        {'id': 'limits', 'title': 'Limits and what is still open', 'lead': 'limits', 'tables': [], 'note': None},
    ]
    return T


def main():
    R = build()
    s = json.dumps(R, indent=1, ensure_ascii=False) + '\n'
    if '--check' in sys.argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ''
        if cur != s:
            print('study_data.py --check: data/studies/s137.json is not what the generator writes from dev/runs/')
            sys.exit(1)
        print('study_data.py --check: data/studies/s137.json is what the generator writes (%d tables)' % len(R['tables']))
        return
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w').write(s)
    print('wrote %s (%d bytes, %d tables)' % (os.path.relpath(OUT, ROOT), len(s), len(R['tables'])))


if __name__ == '__main__':
    main()
