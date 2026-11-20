"""Start-up finance for small essential providers, and public operators: the values for the Creative Collectives' lending switch.
Written Nov 20, 2026 for the study of the Collectives' lending to start-ups where banks will not lend (research-update
prereg/2026-11-s94-collectives-lending.md). The engine constants of the switch are set from the figures this file prints.

Sources (all opened Nov 20, 2026):
- Census Bureau, Business Dynamics Statistics 2023 release, tables by sector (bds2023_sec.csv) and by sector and firm age
  (bds2023_sec_fa.csv), www2.census.gov/programs-surveys/bds/tables/time-series/2023/. Rows for utilities (22), retail trade (44-45) and
  accommodation and food services (72), 2014-2023, are saved in s94_lending/; the full downloads' SHA-256 are recorded below.
- BEA, Fixed Assets Table 3.1ESI, current-cost net stock of private fixed assets by industry, yearend 2025 (Section3All_xls.xlsx, file
  created Sep 28, 2026): utilities (line 9) $4,250,891m, food and beverage stores (line 45) $383,164m, food services and drinking places
  (line 95) $454,294m. Their sum, $5,088,349m, is the stock behind the engine's capacity rule ($18,862 per adult).
- Federal Reserve Banks, Small Business Credit Survey, 2025 Report on Employer Firms (survey of 2024): "41% of applicants received all
  the financing they sought, 36% received just some, and 24% received none"; fully approved by firm age: 0-5 years 48%, 6-20 years 48%,
  21+ years 64%; retail 49%. The page is saved in s94_lending/sbcs2025_p_fully_approved.txt.
- Reinvestment Fund, Pennsylvania Fresh Food Financing Initiative (2004-2010): a $30 million state grant leveraged with $145 million;
  "loans and grants for predevelopment, acquisition, equipment and construction costs, as well as for start-up costs such as employee
  recruitment and training", for operators "in communities where infrastructure costs and credit needs were not met by conventional
  financial institutions"; 206 applications, 88 projects financed; $73.2 million in loans and $12.1 million in grants approved.
- American Public Power Association, "Public Power" (publicpower.org): public power utilities "serve 1 in 7 electricity customers".
- EPA, Information about Public Water Systems (updated Mar 16, 2026): public water systems "provide drinking water to 90 percent of
  Americans"; "A public water system may be publicly or privately owned" (no ownership share given).
- BEA, NIPA Table 2.4.5U, personal consumption expenditures by type of product, 2025 (Underlying Section2All_xls.xlsx, opened
  Nov 20, 2026): household utilities (line 165) $487,685m, the engine's utility total; electricity (line 170) $269,938m; natural gas
  (line 171) $77,973m; water supply and sanitation (line 166) $139,774m.
- SIFMA, US Municipal Bonds Statistics (Nov 3, 2026): outstanding $4.5 trillion (2Q26); issuance through October 2026 $521.0 billion.
- BLS, Business Employment Dynamics Table 7, survival of private sector establishments by opening year (read through the fetch tool; only
  the 1994 and 1995 cohorts were read verbatim): all private, 79.6% and 78.8% survive one year, 49.6% and 48.8% five years; retail, 1994
  cohort, 82.8% and 52.4%. A cross-check only: the engine uses the BDS rates below, which cover 2014-2023.

Run: python3 sources/s94_lending.py
"""
import csv, os
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's94_lending')
FULL_SHA256 = {
    'bds2023_sec.csv': '758a263b166167e9557d4fc4ba8cd60229c5e05d341214b7494982c4764cf224',
    'bds2023_sec_fa.csv': '07f3b6c3e34add284c1e5b900605eb6d45b4c22420cc4670ee0a9e0d94661755',
    '2025-report-on-employer-firms.pdf': 'a637b0030a236af2428ab9bbd6b9dfb80d6d72c5ab7f91a13a6e674d8b9ccbac',
    'reinvestment.com FFFI page': '52dabc02cb9c7eeba0c6ebb033ef101730b4d57b1d152e478c69023d6ea3c6d5',
    'Underlying Section2All_xls.xlsx (BEA NIPA)': '7c96d36e8a6e8fcf42385a9d3eed14be90055488e935baf858a4c1adb2c7a1ea',
    'publicpower.org public-power page': '51ed8ea75316f0e4f6335367e6fe29f8e37dec9ece42bb4405fd0755407c0e5f',
}
STOCK = {'22': 4250891, '44-45': 383164, '72': 454294}  # BEA 3.1ESI yearend 2025, $m (food stores and food services weighted at their own lines)
TOT = sum(STOCK.values())
W = {k: v/TOT for k, v in STOCK.items()}

def num(v):
    try:
        return float(v)
    except ValueError:
        return None

sec = list(csv.DictReader(open(os.path.join(HERE, 'bds2023_sec_extract.csv'))))
fa = list(csv.DictReader(open(os.path.join(HERE, 'bds2023_sec_fa_extract.csv'))))

print('Capital weights (BEA 2025 net stock): ' + ', '.join('%s %.4f' % (k, W[k]) for k in W))
print('The engine\'s K: $%.0fm / $18,862 per adult = %.1f million adults (its Census 2025 count of adults 18+, set earlier, not here)' % (TOT, TOT/18862))

# 1. The pace at which new establishments add capacity: jobs created by establishment births over the sector's jobs (BDS
#    job_creation_rate_births), mean of 2014-2023, weighted by the capital each sector holds in the capacity rule.
pace = {}
for s in STOCK:
    v = [num(x['job_creation_rate_births']) for x in sec if x['sector'] == s]
    v = [a for a in v if a is not None]
    pace[s] = sum(v)/len(v)
PACE = sum(W[s]*pace[s] for s in STOCK)
print('New establishments add, per year (% of the sector\'s jobs, 2014-2023 mean): ' + ', '.join('%s %.3f' % (s, pace[s]) for s in STOCK))
print('Capital-weighted pace: %.3f points of the sectors\' capacity a year  -> CL pace main %.4f' % (PACE, PACE/100))

# 2. Exit rates of establishments of young firms, by firm age (BDS estabs_exit_rate), mean of 2014-2023, capital-weighted.
AGES = ['b) 1', 'c) 2', 'd) 3', 'e) 4', 'f) 5', 'g) 6 to 10', 'h) 11 to 15', 'i) 16 to 20', 'j) 21 to 25', 'k) 26+']
def exit_rate(age):
    out = 0
    for s in STOCK:
        v = [num(x['estabs_exit_rate']) for x in fa if x['sector'] == s and x['fage'] == age]
        v = [a for a in v if a is not None]
        out += W[s]*sum(v)/len(v)
    return out/100
EX = [exit_rate(a) for a in AGES]
print('Exit rate by firm age (capital-weighted): ' + ', '.join('%s %.4f' % (a.split(') ')[1], e) for a, e in zip(AGES, EX)))
# The hazard for a unit in its k-th year after opening (k = 1, 2, ...): ages 1-5 one by one, then each band's rate for its years.
haz = EX[:5] + [EX[5]]*5 + [EX[6]]*5 + [EX[7]]*5 + [EX[8]]*5 + [EX[9]]*15
surv = 1
for k in range(5):
    surv *= 1 - haz[k]
print('Survival to 5 years: %.3f (BLS cross-check, all private 1994-95 cohorts: 0.49-0.50; retail 1994: 0.524)' % surv)
s40 = 1
for h in haz[:40]:
    s40 *= 1 - h
print('Survival to 40 years: %.3f' % s40)
print('CL hazard young (main), years 1-40: [' + ', '.join('%.4f' % h for h in haz) + ']')
print('CL hazard mature (other reading): firms 26+ every year %.4f' % EX[9])

# 3. Credit: the share of applicants that banks turn away in full or in part (context; not an engine constant).
print('Small employer firms, 2024: 41% fully funded, 36% in part, 24% none; fully approved 0-5 years 48%, 21+ years 64%.')
# 4. The Pennsylvania programme's mix of loans and grants.
L, G = 73.2, 12.1
print('Pennsylvania FFFI: loans %.1f, grants %.1f ($m): grant share %.4f  -> CL grant share main' % (L, G, G/(L + G)))
# 5. Public operators.
print('Public power: 1 in 7 electricity customers -> CL charter share main %.4f' % (1/7))
EL, UT = 269938, 487685  # BEA 2.4.5U, 2025, $m
print('Electricity over household utilities: %.4f -> the charter acts on this part of the utility cut only (gas and water: no ownership share opened)' % (EL/UT))
print('Municipal bonds outstanding (SIFMA, 2Q26): $4.5 trillion; issuance Jan-Oct 2026: $521.0 billion (context only).')
