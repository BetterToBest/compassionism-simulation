#!/usr/bin/env python3
"""S71 (Nov 13, 2026; research-update prereg/2026-11-s71-creditor-side.md): who holds the other side of household fixed-rate debt.

The coefficients of the creditor side (option cr of RETURNS; RT_CR in index.html). Every rule below was fixed in the preregistration before this script
was written; nothing here is fitted or tuned. Method: Doepke and Schneider, "Inflation and the Redistribution of Nominal Wealth", Journal of Political
Economy 114(6), 2006 (opened): every nominal claim is finally owned by households, the government or foreigners; funds that issue only shares of themselves
are looked through to their shareholders; every other business, banks included, is owned through its shares; defined-benefit pension assets belong to the
sponsor; the government includes the central bank, state and local governments and government retirement funds.

Sources (each opened by this script; the SHA-256 of each file used is written to the JSON):
  1. Board of Governors, Financial Accounts of the United States (Z.1), https://www.federalreserve.gov/releases/z1/current/z1_csv_files.zip
     (release of Sep 11, 2026). Levels, $ million, at 2022:Q4 (the year of the survey behind the engine's balance sheets); 2026:Q2 printed as a check.
     Tables: L.218 one-to-four-family residential mortgages (F4_5a_s), L.222 consumer credit (F4_3_s), L.211 agency- and GSE-backed securities (F3_3_s),
     L.110 private depository institutions (S122_s), L.203 checkable deposits and currency (F2_2_s), L.204 time and savings deposits (F2_3_s),
     L.206 money market fund shares (F521_s), L.226 mutual fund shares (F522_1_s), L.224 corporate equities (F51_1_s), L.118.b and L.118.c private
     defined-benefit and defined-contribution pension funds (S129s1_1_s, S129s2_1_s), L.116.g and L.116.s life insurers (S1281_1_s, S1281_2_s).
  2. Survey of Consumer Finances 2022, summary extract (rscfp2022.dta in https://www.federalreserve.gov/econres/files/scfp2022s.zip), all five implicates,
     weight WGT: the engine's families (head aged 25-66 with wage income; sources/s59_portfolio.py) against all families.
  3. Board of Governors, Distributional Financial Accounts (dfa-networth-levels-detail.csv in
     https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip), 2022:Q4: an outside check only, not an input.

One dollar of household fixed-rate debt (home mortgages less home equity loans, times the fixed-rate share; non-revolving consumer credit) is followed to
seven final places: dHH, dGOV, dROW deposit-like claims of households, the government and foreigners (bank deposits that fund the debt; money market
fund shares); bHH bond-like claims of households (direct, mutual funds, defined-contribution pensions, insurers' separate accounts); BUS businesses, for
their shareholders; GOV, ROW direct holdings of the government and of foreigners. Then: eH, eG, eR who owns U.S. shares (households, government,
foreigners); wD, wB, wE the engine families' share of all families' deposit-like assets, bond-like assets and stocks, each over their share of all
families' fixed-rate debt; t the bond-like fraction of nominal assets in each of the engine's seven wealth groups.

Usage: python3 sources/s71_creditors.py [z1_csv_files.zip scfp2022s.zip dfa.zip]   (without paths it downloads the three; needs pandas and numpy)
Prints the tables and writes sources/s71_creditors.json."""
import csv, hashlib, io, json, os, sys, urllib.request, zipfile
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
URLS = ['https://www.federalreserve.gov/releases/z1/current/z1_csv_files.zip', 'https://www.federalreserve.gov/econres/files/scfp2022s.zip',
        'https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip']
def blob(i):
    if len(sys.argv) > 3: return open(sys.argv[1 + i], 'rb').read()
    return urllib.request.urlopen(urllib.request.Request(URLS[i], headers={'User-Agent': 'Mozilla/5.0 (research script)'}), timeout=300).read()
RAW = [blob(i) for i in range(3)]; SHA = [hashlib.sha256(b).hexdigest() for b in RAW]
Z1 = zipfile.ZipFile(io.BytesIO(RAW[0]))
_tab = {}
def tab(name):
    if name not in _tab:
        rows = list(csv.reader(io.TextIOWrapper(Z1.open('csv/' + name + '.csv'), encoding='utf-8-sig'))); h = rows[0]
        _tab[name] = {r[0]: dict(zip(h[1:], r[1:])) for r in rows[1:] if r}
    return _tab[name]
def v(name, code, q):
    x = tab(name)[q][code + '.Q']; return float(x) if x not in ('', 'ND', 'NA') else 0.0
F = ['dHH', 'bHH', 'BUS', 'GOV', 'ROW', 'dGOV', 'dROW']
def unit(k): return {f: (1.0 if f == k else 0.0) for f in F}
def mix(parts):  # parts: [(amount, vector)] -> the amount-weighted vector (sums to 1)
    tot = sum(a for a, _ in parts); return {f: sum(a*x[f] for a, x in parts)/tot for f in F}
ARM = json.load(open(os.path.join(HERE, 's59_portfolio.json')))['arm']  # adjustable-rate share of home mortgage dollars (the engine's families, SCF 2022)

def ledger(q):
    H, B, G, R = unit('bHH'), unit('BUS'), unit('GOV'), unit('ROW')
    # mutual fund shares (L.226): looked through to their holders
    mf = mix([(v('F522_1_s', 'LM153064205', q), H), (v('S129s2_1_s', 'LM573064255', q), H), (v('S129s1_1_s', 'LM573064243', q), B),
              (v('S1281_2_s', 'LM543064385', q), H), (v('S1281_1_s', 'LM543064275', q), B), (v('F522_1_s', 'LM263064203', q), R),
              (v('F522_1_s', 'LM213064203', q) + v('F522_1_s', 'LM223064205', q), G),
              (sum(v('F522_1_s', c, q) for c in ('LM103064203', 'LM763064203', 'LM473064205', 'LM623064203', 'LM513064205')), B)])
    # money market fund shares (L.206): deposit-like claims of their holders; businesses' are their shareholders'
    mm = mix([(v('F521_s', 'FL153034005', q) + v('F521_s', 'FL573034005', q), unit('dHH')), (v('F521_s', 'FL263034003', q), unit('dROW')),
              (v('F521_s', 'FL213034003', q) + v('F521_s', 'FL223034005', q), unit('dGOV')),
              (sum(v('F521_s', c, q) for c in ('FL103034000', 'FL113034003', 'FL513034005', 'FL543034005', 'FL653034003', 'FL563034003', 'FL463034005', 'FL623034003', 'FL443034003', 'FL503034005')), B)])
    # banks and credit unions (L.110): the deposit-funded share passes to depositors (L.203, L.204; foreigners' currency left out), the rest is the banks' own
    dsh = (v('S122_s', 'FL703127005', q) + v('S122_s', 'FL703130005', q))/v('S122_s', 'FL704194005', q)
    dep = mix([(v('F2_2_s', 'FL153020005', q) + v('F2_3_s', 'FL153030005', q), unit('dHH')), (v('F2_2_s', 'FL143020005', q) + v('F2_3_s', 'FL143030005', q), B),
               (v('F2_2_s', 'FL313020005', q) + v('F2_2_s', 'FL213020005', q) + v('F2_3_s', 'FL313030003', q) + v('F2_3_s', 'FL213030000', q), unit('dGOV')),
               (v('F2_2_s', 'FL263027003', q) + v('F2_3_s', 'FL263030005', q), unit('dROW')), (v('F2_2_s', 'FL793020005', q) + v('F2_3_s', 'FL793030005', q), B)])
    bank = mix([(dsh, dep), (1 - dsh, B)])
    # agency- and GSE-backed securities (L.211) by holder
    a = lambda c: v('F3_3_s', c, q)
    ag = mix([(a('LM153061705') + a('LM623061703'), H), (a('LM103061703') + a('LM513061705') + a('LM403061705') + a('LM643061773') + a('LM663061705'), B),
              (a('FL313061703') + a('LM213061703') + a('LM713061705') + a('LM343061705') + a('LM223061743'), G),
              (a('LM763061705') + a('LM743061703') + a('LM473061705') + a('LM733061703'), bank), (a('LM753061703') + a('LM263061705'), R),
              (v('S1281_1_s', 'LM543061775', q), B), (v('S1281_2_s', 'LM543061783', q), H), (v('S129s1_1_s', 'LM573061743', q), B), (v('S129s2_1_s', 'LM573061733', q), H),
              (a('FL633061700'), mm), (a('LM653061703'), mf)])
    # home mortgages (L.218) less home equity loans, by holder
    m = lambda c: v('F4_5a_s', c, q)
    mort_parts = [(m('FL153065103'), H), (m('FL103065105') + m('FL113065103') + m('FL543065105') + m('FL573065103') + m('FL613065105') - m('FL613065123') + m('FL643065173'), B),
                  (m('FL313065105') + m('FL213065103') + m('FL223065143'), G),
                  (m('FL763065105') - m('FL763065125') + m('FL743065103') + m('FL473065100') - m('FL473065125'), bank), (m('FL753065103') - m('FL753065203'), R),
                  (m('FL403065105') + m('FL413065105') + m('FL673065105') - m('FL673065123'), ag)]
    mort = mix(mort_parts); mort_amt = sum(x for x, _ in mort_parts)*m('FL153165105')/m('FL893065105')*(1 - ARM)  # households' part, fixed-rate
    # consumer credit (L.222): the federal government's and nonprofits' holdings are student loans (fixed); other holders' revolving part proportional
    c = lambda k: v('F4_3_s', k, q)
    oth = c('FL763066005') + c('FL473066000') + c('FL673066000') + c('FL613066005'); nrev = c('FL153166000') - c('FL153166100')
    fx = (nrev - c('FL313066220') - c('FL163066223'))/oth
    cc_parts = [(c('FL163066223'), H), (c('FL313066220'), G), ((c('FL763066005') + c('FL473066000'))*fx, bank), (c('FL673066000')*fx, ag), (c('FL613066005')*fx, B)]
    cc = mix(cc_parts); cc_amt = sum(x for x, _ in cc_parts)
    led = mix([(mort_amt, mort), (cc_amt, cc)])
    # who owns U.S. corporate equities (L.224), looked through funds; shares held by other U.S. businesses netted out
    e = lambda k: v('F51_1_s', k, q)
    funds = e('LM653064100') + e('LM563064100') + e('LM553064103'); mfx = {'H': mf['bHH'], 'G': mf['GOV'], 'R': mf['ROW']}
    EH = e('LM153064105') + e('LM623064105') + v('S129s2_1_s', 'LM573064133', q) + v('S1281_2_s', 'LM543064185', q) + funds*mfx['H']
    EG = e('LM313064105') + e('LM213064103') + e('LM343064105') + e('LM223064145') + funds*mfx['G']
    ER = e('LM263064105') + funds*mfx['R']
    own = {'eH': EH/(EH + EG + ER), 'eG': EG/(EH + EG + ER), 'eR': ER/(EH + EG + ER)}
    return {'ledger': led, 'own': own, 'mortgages': mort, 'consumer': cc, 'agency': ag, 'bank': bank, 'deposits': dep, 'mutual': mf, 'money': mm, 'dsh': dsh,
            'amounts': {'mortgages_fixed_households': mort_amt, 'consumer_fixed': cc_amt, 'fixed_share_other_consumer_holders': fx}}

def show(name, x): print('  %-28s ' % name + '  '.join('%s %.4f' % (f, x[f]) for f in F))
out = {'source': 'Z.1 release of Sep 11, 2026 (levels at 2022:Q4); SCF 2022 summary extract; DFA 2022:Q4 (check only); sources/s71_creditors.py',
       'sha256': {'z1_csv_files.zip': SHA[0], 'scfp2022s.zip': SHA[1], 'dfa.zip': SHA[2]}, 'arm': ARM}
for q in ('2022:Q4', '2026:Q2'):
    L = ledger(q); print('== %s: one dollar of household fixed-rate debt, by final holder' % q)
    for k in ('mutual', 'money', 'deposits', 'bank', 'agency', 'mortgages', 'consumer', 'ledger'): show(k, L[k])
    print('  deposit-funded share of banks %.4f; fixed-rate mortgages of households $%.0f bn, fixed consumer credit $%.0f bn (fixed share of other holders\' consumer credit %.4f)'
          % (L['dsh'], L['amounts']['mortgages_fixed_households']/1e3, L['amounts']['consumer_fixed']/1e3, L['amounts']['fixed_share_other_consumer_holders']))
    print('  owners of U.S. shares: households %.4f, government %.4f, foreigners %.4f' % (L['own']['eH'], L['own']['eG'], L['own']['eR']))
    assert abs(sum(L['ledger'].values()) - 1) < 1e-12 and abs(sum(L['own'].values()) - 1) < 1e-12
    out['main' if q == '2022:Q4' else 'check_2026Q2'] = {'ledger': {f: round(L['ledger'][f], 4) for f in F}, 'own': {k: round(x, 4) for k, x in L['own'].items()},
                                                         'dsh': round(L['dsh'], 4), 'amounts': {k: round(x, 4) for k, x in L['amounts'].items()}}
led = out['main']['ledger']; drift = 1 - sum(led.values()); led['BUS'] = round(led['BUS'] + drift, 4)  # the seven rounded shares sum to 1 exactly

# SCF 2022: the engine's families against all families; the bond-like fraction of nominal assets by the engine's wealth group
P = json.load(open(os.path.join(HERE, 's59_portfolio.json'))); CPI22, CPI25, FILE = 292.655, 321.943, 1.09438
zf = zipfile.ZipFile(io.BytesIO(RAW[1])); dta = io.BytesIO(zf.read('rscfp2022.dta'))
cols = ['wgt', 'age', 'married', 'wageinc', 'networth', 'fin', 'equity', 'liq', 'cds', 'install', 'nh_mort', 'resdbt']
r = pd.io.stata.StataReader(dta); names = {c.lower(): c for c in r.variable_labels().keys()}; dta.seek(0)
df = pd.read_stata(dta, columns=[names[c] for c in cols], convert_categoricals=False); df.columns = [c.lower() for c in df.columns]
# nominal assets are FIN - EQUITY, as in the engine; in 338 of 22,975 records EQUITY counts stock held inside transaction accounts, so deposit-like assets
# (LIQ + CDS) are capped at the nominal total (0.35% of the bond-like total)
df['dep'] = np.minimum(df.liq + df.cds, df.fin - df.equity); df['bond'] = df.fin - df.equity - df.dep; df['fix'] = df.install + (1 - ARM)*(df.nh_mort + df.resdbt)
assert (df.bond > -1).all() and (df.dep > -1).all()
eng = (df.age >= 25) & (df.age <= 66) & (df.wageinc > 0) & (df.married > 0)
sh = {c: float((df.wgt*df[c])[eng].sum()/(df.wgt*df[c]).sum()) for c in ('dep', 'bond', 'equity', 'fix')}
om = {'wD': sh['dep']/sh['fix'], 'wB': sh['bond']/sh['fix'], 'wE': sh['equity']/sh['fix']}
print('== SCF 2022: the engine\'s families hold %.1f%% of all families\' fixed-rate debt, %.1f%% of deposit-like assets, %.1f%% of bond-like assets, %.1f%% of stocks (%.1f%% of families)'
      % (sh['fix']*100, sh['dep']*100, sh['bond']*100, sh['equity']*100, float(df.wgt[eng].sum()/df.wgt.sum())*100))
print('  the model\'s share of household-held claims per dollar of its own debt: deposits %.4f, bonds %.4f, shares %.4f' % (om['wD'], om['wB'], om['wE']))
d = df[eng]; w = d.wgt.values.astype(float); nw = d.networth.values*CPI25/CPI22/FILE; grp = np.searchsorted(P['edges'], nw, side='right')
t = [float((w*d.bond.values)[grp == g].sum()/(w*(d.bond.values + d.dep.values))[grp == g].sum()) for g in range(7)]
tall = float((w*d.bond.values).sum()/(w*(d.bond.values + d.dep.values)).sum())
print('  bond-like fraction of nominal assets by wealth group (below zero, to P25, P50, P75, P90, P99, above): ' + ', '.join('%.4f' % x for x in t) + '; all %.4f' % tall)
out['scf'] = {'share': {k: round(x, 4) for k, x in sh.items()}, 'w': {k: round(x, 4) for k, x in om.items()}, 't': [round(x, 4) for x in t], 'tAll': round(tall, 4)}

# DFA 2022:Q4, all households: who would bear the new charges under the main reading (a check, not an input)
rows = list(csv.reader(io.TextIOWrapper(zipfile.ZipFile(io.BytesIO(RAW[2])).open('dfa-networth-levels-detail.csv'), encoding='utf-8-sig'))); hd = rows[0]
D = {x[1]: dict(zip(hd[2:], x[2:])) for x in rows[1:] if x[0] == '2022:Q4'}
GR = [('top 1%', ['TopPt1', 'RemainingTop1']), ('next 9%', ['Next9']), ('next 40%', ['Next40']), ('bottom 50%', ['Bottom50'])]
def dsh_(colsum):
    tot = sum(sum(float(D[c][k]) for k in colsum) for c in D); return [sum(sum(float(D[c][k]) for k in colsum) for c in cs)/tot for _, cs in GR]
inst = {'deposits and money market funds': dsh_(['Deposits', 'Money market fund shares']), 'debt securities and loans': dsh_(['Debt securities', 'Loans (Assets)']),
        'the same with defined-contribution pensions, annuities and life insurance': dsh_(['Debt securities', 'Loans (Assets)', 'DC pension entitlements', 'Annuities', 'Life insurance reserves']),
        'corporate equities and mutual fund shares': dsh_(['Corporate equities and mutual fund shares']), 'home mortgages and consumer credit (the debtors)': dsh_(['Home mortgages', 'Consumer credit'])}
print('== DFA 2022:Q4, all U.S. households: shares held by ' + ', '.join(g for g, _ in GR))
for k, x in inst.items(): print('  %-76s ' % k + '  '.join('%5.1f%%' % (y*100) for y in x))
phi = 0.46; dALL = led['dHH'] + led['dGOV'] + led['dROW']; nb = phi*led['bHH']; ne = (led['BUS'] + phi*dALL)*out['main']['own']['eH']
for lab, key in (('narrow bonds', 'debt securities and loans'), ('wide bonds', 'the same with defined-contribution pensions, annuities and life insurance')):
    mixd = [(nb*a + ne*b)/(nb + ne) for a, b in zip(inst[key], inst['corporate equities and mutual fund shares'])]
    print('  new charges under the main reading (phi 0.46, chi 0), %s: ' % lab + '  '.join('%5.1f%%' % (y*100) for y in mixd))
    out.setdefault('dfa_check', {})[lab] = [round(y, 4) for y in mixd]
out['dfa_check']['groups'] = [g for g, _ in GR]; out['dfa_check']['instruments'] = {k: [round(y, 4) for y in x] for k, x in inst.items()}
json.dump(out, open(os.path.join(HERE, 's71_creditors.json'), 'w'), indent=1)
print('RT_CR = ' + json.dumps({'led': led, 'own': out['main']['own'], 'w': out['scf']['w'], 't': out['scf']['t'], 'tAll': out['scf']['tAll']}))
