"""S72 (Nov 14, 2026): the figures behind the government account (index.html GV_US, GV_DEFAULTS; research-update prereg/2026-11-s72-government-budget.md).

Opened Nov 14, 2026:
- Treasury, Monthly Statement of the Public Debt, table 1, Sept 30, 2025 (fiscaldata.treasury.gov API, v1/debt/mspd/mspd_table_1): debt held by the public
  $30,277.8 billion; bills 6,396.6, notes 15,387.4, bonds 5,133.1, TIPS 2,087.4, floating-rate notes 690.5, non-marketable 582.8. The fixed-coupon part,
  which inflation erodes until it matures (notes, bonds, non-marketable): 69.7%.
- FRED FYGDP (GDP, fiscal year 2025): $30,322.8 billion. FRED FYOINT (federal interest outlays, FY2025): $1,215.6 billion (context only).
- Census Bureau, Vintage 2024 national population estimates by single year of age (nc-est2024-agesex-res.csv): adults 18 and over, July 1, 2024,
  266,978,268.
- Per adult (year-0 = 2025 dollars): debt held by the public $113,410 (GV_US.D0); GDP $113,579 (GV_US.Y0).
- The real borrowing rate: the 10-year TIPS yield, FRED DFII10, mean 0.97% 2003-2025 (sources/tips_real_rate.py; GV_DEFAULTS.rr, .rs); 2025 alone 1.96%.
- Taylor (1993) as written on the Federal Reserve's page "Policy Rules and How Policymakers Use Them"
  (federalreserve.gov/monetarypolicy/policy-rules-and-how-policymakers-use-them.htm): R = r_LR + pi + 0.5(pi - pi*) + 0.5(y - y_P), pi* = 2%
  (GV_DEFAULTS.a, .b, .pt).
- Laubach (2003), "New Evidence on the Interest Rate Effects of Budget Deficits and Debt", Federal Reserve FEDS 2003-12
  (federalreserve.gov/pubs/feds/2003/200312/200312pap.pdf): "interest rates rise ... by about 4 basis points in response to a percentage point increase in
  the projected debt-to-GDP ratio" (conclusions); 2.1 basis points in his model-based estimate, which he calls conservative (GV_DEFAULTS.dk 0.04; reading
  0.021).
Not opened: CBO's projections (cbo.gov refused the session's requests); no figure depends on them.

Usage: python3 sources/s72_government.py   (downloads the files and prints the figures above; needs network access)
"""
import csv, io, json, urllib.request

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode()

m = json.loads(get('https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_1?filter=record_date:eq:2025-09-30&page%5Bsize%5D=50'))['data']
pub = {(r['security_type_desc'], r['security_class_desc']): float(r['debt_held_public_mil_amt']) for r in m}
tot = pub[('Total Public Debt Outstanding', '_')]
fixed = pub[('Marketable', 'Notes')] + pub[('Marketable', 'Bonds')] + pub[('Total Nonmarketable', '_')]
for k in ('Bills', 'Notes', 'Bonds', 'Treasury Inflation-Protected Securities', 'Floating Rate Notes'):
    print('%-42s %10.1f bn  %5.1f%%' % (k, pub[('Marketable', k)] / 1e3, 100 * pub[('Marketable', k)] / tot))
print('%-42s %10.1f bn  %5.1f%%' % ('Non-marketable', pub[('Total Nonmarketable', '_')] / 1e3, 100 * pub[('Total Nonmarketable', '_')] / tot))
print('debt held by the public, Sept 30, 2025: %.1f bn; fixed-coupon share %.1f%%' % (tot / 1e3, 100 * fixed / tot))

def fred(sid, date):
    for r in csv.DictReader(io.StringIO(get('https://fred.stlouisfed.org/graph/fredgraph.csv?id=' + sid))):
        if r['observation_date'] == date:
            return float(r[sid])
gdp = fred('FYGDP', '2025-09-30') * 1e3          # billions -> millions
intr = fred('FYOINT', '2025-09-30')              # millions
print('GDP FY2025 %.1f bn; interest outlays FY2025 %.1f bn' % (gdp / 1e3, intr / 1e3))

rows = list(csv.DictReader(io.StringIO(get('https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/national/asrh/nc-est2024-agesex-res.csv'))))
adults = sum(int(r['POPESTIMATE2024']) for r in rows if r['SEX'] == '0' and r['AGE'] != '999' and int(r['AGE']) >= 18)
print('adults 18+, July 1, 2024: %d' % adults)
print('per adult: debt held by the public $%.0f; GDP $%.0f; ratio %.1f%%' % (tot * 1e6 / adults, gdp * 1e6 / adults, 100 * tot / gdp))
