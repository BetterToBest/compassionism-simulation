"""S82 part 2 (Nov 17, 2026; research-update prereg/2026-11-s82-v6-supply-indexing.md, Amendment 2): the supply limit's headroom values, SL_SRC in
index.html, for housing, medical care and food. Each value is a share of the sector's no-programme NEEDS consumption (Amendment 1, item 1), not of
the sector's output: e, the excess the limit answers, is measured on the needs baskets (the engine's essD).
  v    idle capacity: capacity unused beyond the sector's normal use, met at once;
  m    above-needs consumption: what households consume of the sector beyond the needs baskets, over the needs baskets (the engine scales the part
       given up by eta x theta x e, theta the engine's own relative price rise, so m only matters where theta > 0: housing and medical care);
  eta  the price elasticity of that consumption;
  lam  the share of the lasting unmet excess that new capacity answers each year.

Sources (each opened Nov 17, 2026; FRED files are saved in the directory given and hashed in the output):
- FRED (Federal Reserve Bank of St. Louis), fredgraph.csv?id=<series>:
    DHUTRC1A027NBEA  BEA, personal consumption expenditures (PCE): housing and utilities, $bn, annual (NIPA table 2.4.5; rent and the imputed rent of
                     owner-occupied housing at market value, with household utilities: the housing services the economy produces);
    DFXARC1A027NBEA  PCE: food and beverages purchased for off-premises consumption, $bn (recorded, not used);
    DHLCRC1A027NBEA  PCE: health care, $bn (every payer; recorded, not used: MIT's medical line counts what the household pays);
    TTLHH            Census, total households, thousands (CPS/HVS);
    CXUHEALTHLB0101M, CXUFOODHOMELB0101M, CXUFOODTOTLLB0101M, CXUSHELTERLB0101M, CXUUTILSLB0101M, CXU980010LB0101M
                     BLS Consumer Expenditure Survey (CE), all consumer units: health care, food at home, food, shelter, utilities ($ a unit a year)
                     and persons per unit (BLS refuses scripted downloads from the build environment; FRED republishes the series);
    RRVRUSQ156N, RHVRUSQ156N  Census Housing Vacancy Survey: rental and homeowner vacancy rates, %, quarterly;
    CAPUTLG311S      Federal Reserve G.17: capacity utilisation, food manufacturing (NAICS 311), %, monthly.
- Albouy, D., G. Ehrlich and Y. Liu (2016), "Housing Demand, Cost-of-Living Inequality, and the Affordability Crisis", NBER Working Paper 22816,
  Table 2, column 3 (their preferred estimate, renters, metro level): uncompensated own-price elasticity of housing demand -0.697 (s.e. 0.042);
  "roughly -2/3" in the text; the table's other columns -0.49 to -0.83 (w22816.pdf sha256 c89055bbd3e4e260b3ba2beed62dd7d81188ef701cf43690b41c4442946b7cfb).
- Aron-Dine, A., L. Einav and A. Finkelstein (2013), "The RAND Health Insurance Experiment, Three Decades Later", NBER Working Paper 18642: the
  elasticity of medical spending with respect to its out-of-pocket price is -0.2 (Keeler and Rolph 1988; Manning et al. 1987) (w18642.pdf sha256
  564bc5edbf41d52e2cf3341f386b7164cdd2b4f47849bac6b086c9110d828daa).
- Leuchter, R. K. et al. (2025), "Health Care Staffing Shortages and Potential National Hospital Bed Shortage", JAMA Network Open 8(2): e2460645
  (Europe PMC PMC11840646, full text): mean US hospital occupancy 63.9% in 2009-2019 against 75.3% from May 2023 to April 2024 (staffed beds fell
  from 802,000 to 674,000; the daily census stayed near 510,000).
- Wheaton, W. C., S. Chervachidze and G. Nechayev (2014), "Error Correction Models of MSA Housing 'Supply' Elasticities: Implications for Price
  Recovery", MIT Department of Economics, second draft Dec 30, 2014, 68 metro areas: "Adjustment speeds back to the underlying cointegrating
  relationship average about 5% per quarter or 20% per annum" (the price equation; the authors find the stock equation itself rarely corrects:
  the generous side for building) (pdf sha256 4e3a007985f4a767fc01fcac67390a3f691cf08aed96df2a9112f4f387bc4986).
- The engine's own needs baskets (index.html, transcribed below): CFG.LIVING_WAGE_ANNUAL, CFG.BASKET, CFG.HH_RATIO, CFG.HH_COMP, CFG.HH_KIDS. The
  needs per household are the model population's (adults 25-64, CPS ASEC 2023), while the spending is every US household's: older households have
  fewer children and lower needs, so m is if anything understated (the cautious side).

Derived (year 2025, the last complete year and the year of the engine's other inputs; 2026 quarters printed beside):
- v: max(0, normal use - this year's use) for the sector's own measure, the normal being the series' long-run mean (as the price-rule study,
  sources/s58_price_rule.py, measured slack): housing, the rental and homeowner vacancy rates against their 1956-2025 means (weighted by renters'
  and owners' shares of occupied units, here 0.35 and 0.65); food, food-manufacturing utilisation against its 1972-2025 mean; medical care,
  hospital occupancy against its 2009-2019 mean. Converted to needs consumption by x (1 + m). Each is 0 in 2025: every sector runs at or above
  its normal use. The headroom to a practical maximum (85% hospital occupancy, Leuchter et al.'s shortage line; the lowest rental vacancy since
  1980) is printed, not used: drawing on it is a price-driven supply response, which the engine's form does not have, and the cautious reading
  leaves it out.
- m: max(0, the sector's spending per household / the model's needs per household - 1), on matching coverage: housing, PCE housing and utilities
  per household against MIT's housing line (HUD fair-market rents, gross of utilities); the CE's shelter and utilities (owners' outlays, not the
  rental value of their homes) printed as the low end. Medical care, the CE's health care per unit (premiums the household pays, services, drugs)
  against MIT's medical line (the household's premium share and out-of-pocket costs). Food, the CE's food at home against MIT's food plan (not
  used: theta food is 0).
- eta: housing 0.697 (Albouy et al.); medical care 0.2 (RAND); food 0.5, the preregistration's design middle (no source opened; not used, theta
  food is 0).
- lam: housing 0.2 (Wheaton et al.); medical care and food 0.25, the preregistration's design middle (no source opened on how fast either
  sector's capacity answers a lasting excess; labelled design parameters).

Usage: python3 sources/s82_supply.py sources/s82_fred [--fetch] > sources/s82_supply.json   (standard library only)
"""
import csv, hashlib, json, os, statistics as st, sys, urllib.request

SERIES = ['DHUTRC1A027NBEA', 'DFXARC1A027NBEA', 'DHLCRC1A027NBEA', 'TTLHH', 'CXUHEALTHLB0101M', 'CXUFOODHOMELB0101M', 'CXUFOODTOTLLB0101M',
          'CXUSHELTERLB0101M', 'CXUUTILSLB0101M', 'CXU980010LB0101M', 'RRVRUSQ156N', 'RHVRUSQ156N', 'CAPUTLG311S']
YEAR = '2025'
# index.html (v5.9.16): CFG.LIVING_WAGE_ANNUAL, CFG.BASKET (three sectors), CFG.HH_RATIO (three sectors), CFG.HH_COMP, CFG.HH_KIDS
L = 49369.82
BASKET = {'food': 0.0901, 'housing': 0.2761, 'medical': 0.0685}
RATIO = {'1a0k': {'food': 1, 'housing': 1, 'medical': 1}, '1a1k': {'food': 1.46685, 'housing': 1.357341, 'medical': 2.842683},
         '1a2k': {'food': 2.197896, 'housing': 1.357341, 'medical': 2.890464}, '1a3k': {'food': 2.925225, 'housing': 1.765906, 'medical': 2.942673},
         '2a0k': {'food': 1.833247, 'housing': 1.100935, 'medical': 2.147724}, '2a1k': {'food': 2.275206, 'housing': 1.357341, 'medical': 3.142813},
         '2a2k': {'food': 2.926551, 'housing': 1.357341, 'medical': 3.240001}, '2a3k': {'food': 3.570563, 'housing': 1.765906, 'medical': 3.348802}}
COMP = {'coupleKids': 0.3163, 'coupleNoKids': 0.3291, 'singleParent': 0.0495, 'single': 0.3050}   # adults 25-64 by household type
KIDS = {'couple': [0.4063, 0.3838, 0.1462, 0.0637], 'single': [0.5651, 0.2785, 0.1101, 0.0463]}  # 1, 2, 3, 4+ children (4+ costed as 3, as the engine)
RENT_SHARE = 0.35   # renters' share of occupied housing units (HVS, about 35% in 2025); owners 0.65
LEUCHTER = {'pre2009_2019': 63.9, 'post2023_2024': 75.3, 'shortageLine': 85.0}
SECT = ['food', 'housing', 'medical']

D = sys.argv[1]
if '--fetch' in sys.argv:
    os.makedirs(D, exist_ok=True)
    for s in SERIES: urllib.request.urlretrieve('https://fred.stlouisfed.org/graph/fredgraph.csv?id=' + s, os.path.join(D, s + '.csv'))
def rd(s):
    out = {}
    with open(os.path.join(D, s + '.csv')) as f:
        for r in csv.DictReader(f):
            k = list(r.keys()); v = r[k[1]]
            if v not in ('', '.'): out[r[k[0]]] = float(v)
    return out
def sha(s): return hashlib.sha256(open(os.path.join(D, s + '.csv'), 'rb').read()).hexdigest()
def annual(x, y): return x[y + '-01-01']
def year_mean(x, y, n):
    v = [x[d] for d in x if d[:4] == y]
    if len(v) != n: raise SystemExit('%s: %d observations in %s, expected %d' % (y, len(v), y, n))
    return st.mean(v)
def span_mean(x, a, b, n):
    return st.mean([year_mean(x, str(t), n) for t in range(a, b + 1)])

# Needs per household in the model population (dollars a year at the line), by sector.
hh = {'couple0': COMP['coupleNoKids']/2, 'couple': COMP['coupleKids']/2, 'single1': COMP['singleParent'], 'single0': COMP['single']}
nH = sum(hh.values())
need = {}
for k in SECT:
    tot = hh['couple0']*RATIO['2a0k'][k] + hh['single0']*RATIO['1a0k'][k]
    for i, p in enumerate(KIDS['couple']): tot += hh['couple']*p*RATIO['2a%dk' % min(3, i + 1)][k]
    for i, p in enumerate(KIDS['single']): tot += hh['single1']*p*RATIO['1a%dk' % min(3, i + 1)][k]
    need[k] = L*BASKET[k]*tot/nH

H = annual(rd('TTLHH'), YEAR)*1000
spend = {'housing': annual(rd('DHUTRC1A027NBEA'), YEAR)*1e9/H, 'medical': annual(rd('CXUHEALTHLB0101M'), YEAR), 'food': annual(rd('CXUFOODHOMELB0101M'), YEAR)}
lowH = annual(rd('CXUSHELTERLB0101M'), YEAR) + annual(rd('CXUUTILSLB0101M'), YEAR)
m = {k: max(0.0, spend[k]/need[k] - 1) for k in SECT}

rv, hv, fu = rd('RRVRUSQ156N'), rd('RHVRUSQ156N'), rd('CAPUTLG311S')
rv25, hv25, fu25 = year_mean(rv, YEAR, 4), year_mean(hv, YEAR, 4), year_mean(fu, YEAR, 12)
rvLR, hvLR, fuLR = span_mean(rv, 1956, 2025, 4), span_mean(hv, 1956, 2025, 4), span_mean(fu, 1972, 2025, 12)
rvMin = min(year_mean(rv, str(t), 4) for t in range(1980, 2026))
idleH = RENT_SHARE*max(0.0, (rv25 - rvLR)/100) + (1 - RENT_SHARE)*max(0.0, (hv25 - hvLR)/100)
idleF = max(0.0, (fuLR - fu25)/100)
idleM = max(0.0, (LEUCHTER['pre2009_2019'] - LEUCHTER['post2023_2024'])/100)
v = {'housing': idleH*(1 + m['housing']), 'food': idleF*(1 + m['food']), 'medical': idleM*(1 + m['medical'])}

eta = {'housing': 0.697, 'medical': 0.2, 'food': 0.5}
lam = {'housing': 0.2, 'medical': 0.25, 'food': 0.25}
basis = {'housing': {'v': 'sourced (HVS vacancy against its 1956-2025 mean)', 'm': 'sourced (BEA PCE against MIT housing)', 'eta': 'sourced (Albouy et al. 2016)',
                     'lam': 'sourced (Wheaton et al. 2014; the generous side for the stock)'},
         'medical': {'v': 'sourced (hospital occupancy against its 2009-2019 mean, Leuchter et al. 2025)', 'm': 'sourced (CE health care against MIT medical)',
                     'eta': 'sourced (RAND HIE)', 'lam': 'design parameter (no source opened)'},
         'food': {'v': 'sourced (food-manufacturing utilisation against its 1972-2025 mean)', 'm': 'sourced (CE food at home against MIT food; not used, theta food 0)',
                  'eta': 'design parameter (not used, theta food 0)', 'lam': 'design parameter (no source opened)'}}
r4 = lambda x: round(x, 4)
out = {'files': {s: sha(s) for s in SERIES}, 'year': int(YEAR),
       'SL_SRC': {k: {'v': r4(v[k]), 'm': r4(m[k]), 'eta': eta[k], 'lam': lam[k]} for k in SECT},
       'basis': basis,
       'needsPerHousehold': {k: round(need[k], 2) for k in SECT}, 'householdsPerAdult': r4(nH),
       'spendPerHousehold': {k: round(spend[k], 2) for k in SECT},
       'housingLowEnd': {'ceShelterUtilities': lowH, 'm': r4(max(0.0, lowH/need['housing'] - 1))},
       'recorded': {'pceFoodOffPremisesPerHousehold': round(annual(rd('DFXARC1A027NBEA'), YEAR)*1e9/H, 2),
                    'pceHealthPerHousehold': round(annual(rd('DHLCRC1A027NBEA'), YEAR)*1e9/H, 2),
                    'ceFoodPerUnit': annual(rd('CXUFOODTOTLLB0101M'), YEAR), 'cePersonsPerUnit': annual(rd('CXU980010LB0101M'), YEAR), 'households': H},
       'slack': {'rentalVacancy2025': r4(rv25), 'rentalVacancyMean1956_2025': r4(rvLR), 'rentalVacancyMin1980_2025': r4(rvMin),
                 'homeownerVacancy2025': r4(hv25), 'homeownerVacancyMean1956_2025': r4(hvLR),
                 'foodUtilisation2025': r4(fu25), 'foodUtilisationMean1972_2025': r4(fuLR), 'hospitalOccupancy': LEUCHTER,
                 'notUsed_headroomToPracticalMax': {'housingRental': r4(max(0.0, (rv25 - rvMin)/100)),
                                                    'medicalTo85': r4(max(0.0, (LEUCHTER['shortageLine'] - LEUCHTER['post2023_2024'])/LEUCHTER['post2023_2024']))},
                 'latest2026': {'rentalVacancy': {d: rv[d] for d in sorted(rv) if d[:4] == '2026'}, 'foodUtilisationMean2026': r4(st.mean([fu[d] for d in fu if d[:4] == '2026']))}},
       'restricted': {k: {'v': r4(v[k]/2), 'm': r4(m[k]/2), 'eta': r4(eta[k]/2), 'lam': r4(lam[k]/2)} for k in SECT}}
print(json.dumps(out, indent=1))
