"""v5.3 B3 (Oct 6, 2026): the household inputs, derived from the Census Bureau's household tables and the MIT Living Wage Calculator's family types.
Standard library only; every input number is transcribed below with its table, and the MIT figures are in sources/mit_household_types.json.

1. Who the model's adults live with. Source: U.S. Census Bureau, Current Population Survey, 2023 Annual Social and Economic Supplement, "America's Families
   and Living Arrangements: 2023" (https://www.census.gov/data/tables/2023/demo/families/cps-2023.html; the 2024 and 2025 table pages were not found on
   Oct 6, 2026), numbers in thousands:
     Table A1 (marital status of people 15 and over, by age): people 25-64 and those married with the spouse present;
     Table UC3 (opposite-sex unmarried couples, by age of each partner): cohabiting partners 25-64 (UC3's top row is "60 and over"; the share of it aged
       60-64 is not published, so an assumed 40% is counted, AGE_60_64: it moves the composition by about 0.3% of adults);
     Table A3 (parents with coresident children under 18, by living arrangement and age of parent, and by number of own children): parents 25 and over.
   The model's adults are 25 to 64 (the working-age population the single-adult calibration describes). Four classes, counted per adult:
     couple with children under 18 (married parents; cohabiting parents with a joint child; cohabiting parents without one, and their partners),
     single parent (no partner present), couple without children under 18 (the rest of the partnered), single without children (the rest).
   "Single without children" includes adults living with parents, adult children or roommates: the model treats them as a one-adult budget (a stated
   simplification; CPS counts about 30% of adults 25-64 in this class).
2. How many children. Table A3, number of own children under 18, by the parent's living arrangement (four or more children are 6% of parents; MIT's
   family types stop at three, so the model's baskets stop at three and count every child for per-person measures).
3. The children's ages. Table C2 (children under 18 by age and living arrangement): under 6, 6-11 and 12-17, children living with both parents and with one.
4. What each household type needs a year. MIT Living Wage Calculator (Feb 2026 build), the eight state pages behind CFG.BASKET (AL, CA, CT, HI, ID, IN, ME,
   WV): each component of each family type regressed on the state's one-adult, no-child pre-tax total and evaluated at the model's $49,369.82
   (CFG.LIVING_WAGE_ANNUAL: the unweighted mean of the 51 state living wages x 2,080), the method behind CFG.BASKET (it reproduces CFG.BASKET's shares).
   Childcare by care type, from MIT's own assignment (first child toddler care, second preschool care, third before/after-school and summer care): the
   first child's childcare, the second's increment and the third's increment.

5. The official poverty line by household. U.S. Census Bureau, "Poverty Thresholds for 2025 by Size of Family and Number of Related Children Under 18 Years"
   (www2.census.gov/programs-surveys/cps/tables/time-series/historical-poverty-thresholds/thresh25.xlsx, read Oct 7, 2026; the one-person figure, $16,749,
   is the model's CFG.POVERTY_THRESHOLD_ONE since v5.2): the thresholds for the model's household types, householder under 65 (THRESH_2025).

6. Ages, sex and births, for households with ageing (v5.3 plan item B4; read Oct 7, 2026):
   - U.S. Census Bureau, CPS ASEC 2023, Table FG3 ("Opposite-Sex Married Couple Family Groups, by Presence of Own Children Under 18, and Age ... of Both
     Spouses: 2023", tabfg3-all.xls, thousands): the wife's age by presence of own children under 18 (FG3_WIFE) and the age difference between the spouses
     (FG3_GAP, husband minus wife). Cohabiting couples are assumed to follow the married couples' figures (FG3 covers married couples only).
   - U.S. Census Bureau, Vintage 2024 national population estimates by single year of age and sex (nc-est2024-agesex-res.csv, the file behind
     CFG.AGE_WEIGHTS; POP_F holds women at each age 25..74 and POP the total, thousands, July 1, 2024): the women's share of adults 25-64 (0.5000) and
     at 25 (0.4910, the share of women among the model's new 25-year-olds), and the within-band spread of the FG3 bands.
   - Table C2 (above): the share of children living with their mother only among children living with one parent (single parents' sex), and the share
     of children under 6 who live with one parent (22.2%), which stands in for the share of births to women without a partner present (the model has
     no separations, so this share also stands in for young families that split).
   - NCHS, Births: Final Data for 2024 (sources/births_us.md): births per 1,000 women a year by the mother's age (ASFR).
   - Fertility by partnership: births to a woman of age x happen at ASFR(x) x K, K_COUPLE for a woman with a partner present and K_SINGLE for one without,
     with K chosen so that the women 25-49 as a whole give birth at ASFR and the share of births to women without a partner equals the C2 share:
     K_COUPLE = (1 - s)/p, K_SINGLE = s/(1 - p), where p is the partnered share of adults 25-49 (Tables A1 and UC3; both sexes stand in for women).
   - Singles' ages: people minus partnered adults minus single parents, by ten-year band (Tables A1, UC3, A3; A3's parents "50 and over" are counted
     in the 45-54 band, an approximation that moves the singles' 45-54 share by under 2%).

Usage: python3 sources/households.py   (prints the derived inputs that index.html holds as CFG.HH_*)
"""
import json, os

# --- 1. Composition (thousands) -------------------------------------------------------------------------------------------------------------------
A1_PEOPLE = {'25-34': 44903, '35-44': 43480, '45-54': 39974, '55-64': 41344}          # Table A1, both sexes, total
A1_MARRIED_SP = {'25-34': 17429, '35-44': 26269, '45-54': 25580, '55-64': 25567}      # Table A1, married spouse present
UC3_MALE = {'25-29': 1738, '30-34': 1534, '35-39': 1080, '40-44': 891, '45-49': 602, '50-54': 613, '55-59': 481, '60+': 1278}    # Table UC3, age of male partner
UC3_FEMALE = {'25-29': 1979, '30-34': 1478, '35-39': 951, '40-44': 795, '45-49': 599, '50-54': 611, '55-59': 435, '60+': 969}   # Table UC3, age of female partner
AGE_60_64 = 0.40   # assumed share of the UC3 "60+" partners who are 60-64 (UC3 does not split 60+; A1 gives 55-64 and 65-74 only). A modelling assumption.
# Table A3, parents with coresident children under 18, parents 25 and over (rows 25-29 ... 50+): married spouse present, cohabiting with a joint
# biological child, cohabiting without one, no partner present
A3_AGE = {'25-29': (3413, 666, 240, 1069), '30-34': (7816, 768, 306, 1575), '35-39': (10194, 631, 307, 1802), '40-44': (10352, 445, 350, 1625),
          '45-49': (8107, 198, 180, 1201), '50+': (7812, 164, 171, 1135)}
# Table A3, number of own children under 18 (all parents): one, two, three, four or more; by arrangement
A3_KIDS = {'married': (19069, 19105, 7155, 3136), 'cohabJoint': (1665, 953, 488, 202), 'cohabOther': (996, 468, 174, 69), 'single': (5106, 2516, 995, 418)}
# Table C2, children under 18 in households: under 6, 6-11, 12-17
C2_BOTH = (16856, 17009, 17555)                      # living with both parents
C2_ONE = (4055 + 750, 5200 + 1029, 5833 + 1275)      # living with mother only + father only

def composition():
    n = sum(A1_PEOPLE.values())
    married = sum(A1_MARRIED_SP.values())
    cohab = sum(v for k, v in UC3_MALE.items() if k != '60+') + AGE_60_64*UC3_MALE['60+'] + sum(v for k, v in UC3_FEMALE.items() if k != '60+') + AGE_60_64*UC3_FEMALE['60+']
    m, cj, co, s = (sum(v[i] for v in A3_AGE.values()) for i in range(4))
    coupleKids = m + cj + 2*co            # married parents (both counted), cohabiting parents with a joint child (both counted), others and their partners
    single = s
    partnered = married + cohab
    shares = {'coupleKids': coupleKids/n, 'singleParent': single/n, 'coupleNoKids': (partnered - coupleKids)/n, 'single': (n - partnered - single)/n}
    return n, married, cohab, shares

def kids_dist():
    def d(t): s = sum(t); return [x/s for x in t]
    couple = [a + b + c for a, b, c in zip(A3_KIDS['married'], A3_KIDS['cohabJoint'], A3_KIDS['cohabOther'])]
    return {'couple': d(couple), 'single': d(A3_KIDS['single'])}

def kid_ages():
    def d(t): s = sum(t); return [x/s for x in t]
    return {'couple': d(C2_BOTH), 'single': d(C2_ONE)}

# --- 5. Census poverty thresholds 2025 (dollars), by adults and related children under 18, householder under 65 -----------------------------------------
THRESH_2025 = {(1, 0): 16749, (1, 1): 22190, (1, 2): 25938, (1, 3): 32762, (1, 4): 37833,   # one adult: 1 person; 2 people, one child; 3, two; 4, three; 5, four
               (2, 0): 21558, (2, 1): 25913, (2, 2): 32649, (2, 3): 38421, (2, 4): 43018}  # two adults: 2 people, none; 3, one; 4, two; 5, three; 6, four

# --- 4. MIT baskets by family type at the model's scale -----------------------------------------------------------------------------------------------
X = 49369.82
KEYS = ['Food', 'Child Care', 'Medical', 'Housing', 'Transportation', 'Civic', 'Internet & Mobile', 'Other', 'Annual taxes']
MODEL = {'Food': 'food', 'Child Care': 'childcare', 'Medical': 'medical', 'Housing': 'housing', 'Transportation': 'transport', 'Civic': 'civic',
         'Internet & Mobile': 'internet', 'Other': 'other', 'Annual taxes': 'taxes'}

def baskets():
    mit = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mit_household_types.json'), encoding='utf-8'))
    states = list(mit['states'].values()); types = mit['types']
    xs = [s['rows']['Required annual income before taxes'][0] for s in states]
    mx = sum(xs)/len(xs); sxx = sum((x - mx)**2 for x in xs)
    def at(col, key):
        ys = [s['rows'][key][col] for s in states]; my = sum(ys)/len(ys)
        b = sum((x - mx)*(y - my) for x, y in zip(xs, ys))/sxx
        return my + b*(X - mx)
    out = {}
    for c, t in enumerate(types):
        comp = {MODEL[k]: at(c, k) for k in KEYS}
        out[t] = {'total': sum(comp.values()), 'comp': comp}
    cc = [out['2A2W1C']['comp']['childcare'], out['2A2W2C']['comp']['childcare'] - out['2A2W1C']['comp']['childcare'], out['2A2W3C']['comp']['childcare'] - out['2A2W2C']['comp']['childcare']]
    return out, cc

# --- 6. Ages, sex and births (B4) -------------------------------------------------------------------------------------------------------------------
FG3_WIFE = {'noKids': {'25-29': 1443, '30-34': 1647, '35-39': 1294, '40-44': 1457, '45-49': 2539, '50-54': 4515, '55-64': 11755, '65-74': 9796},
            'kids': {'25-29': 1988, '30-34': 4235, '35-39': 5373, '40-44': 5277, '45-49': 3756, '50-54': 1955, '55-64': 773, '65-74': 125}}  # FG3, age of wife
# FG3, age difference (husband minus wife), thousands, with and without own children under 18: (lowest gap, highest gap, without, with); "20+" taken as 20-24
FG3_GAP = [(20, 24, 357, 209), (15, 19, 516, 319), (10, 14, 1911, 1016), (6, 9, 4420, 2718), (4, 5, 4834, 2960), (2, 3, 7810, 4979), (-1, 1, 13892, 8748),
           (-3, -2, 2760, 1717), (-5, -4, 1447, 689), (-9, -6, 1139, 437), (-14, -10, 453, 150), (-19, -15, 170, 41), (-24, -20, 122, 58)]
# Census Vintage 2024, July 1, 2024, thousands: total (POP) and women (POP_F) at ages 25..74
POP = [4467, 4459, 4467, 4496, 4571, 4660, 4728, 4826, 4888, 4892, 4747, 4655, 4595, 4594, 4580, 4477, 4531, 4512, 4439, 4411, 4225, 4124, 4066, 3922, 3957,
       3875, 3919, 4099, 4334, 4259, 4095, 4001, 4007, 4055, 4201, 4292, 4283, 4286, 4265, 4176, 4084, 4036, 3949, 3761, 3659, 3513, 3349, 3202, 3028, 2864]
POP_F = [2193, 2194, 2205, 2219, 2257, 2299, 2333, 2386, 2422, 2426, 2352, 2307, 2272, 2270, 2267, 2220, 2249, 2242, 2208, 2196, 2110, 2062, 2039, 1967, 1987,
         1948, 1973, 2060, 2174, 2139, 2060, 2017, 2029, 2058, 2143, 2192, 2195, 2201, 2196, 2155, 2118, 2099, 2064, 1978, 1933, 1866, 1787, 1715, 1634, 1551]
WOMEN_25_64, WOMEN_AT_25 = 0.5000, 0.4910
ASFR = [12.6, 55.8, 89.5, 93.7, 54.3, 12.7, 1.1]   # births per 1,000 women a year, ages 15-19, 20-24, ..., 45-49 (NCHS 2024, Table 2)

def bands_to_ages(counts, pop, lo=25, hi=66):
    """Spread band counts over single ages lo..hi in proportion to the population at each age (a band's ages above hi are dropped)."""
    w = []
    for a in range(lo, hi + 1):
        for k, v in counts.items():
            b0, b1 = (int(x) for x in k.split('-'))
            if b0 <= a <= b1:
                tot = sum(pop[x - 25] for x in range(b0, b1 + 1)); w.append(v*pop[a - 25]/tot); break
        else:
            w.append(0.0)
    return w

def ages_and_births():
    n, married, cohab, sh = composition()
    # singles by ten-year band: people - partnered - single parents
    cohabB = {'25-34': UC3_MALE['25-29'] + UC3_MALE['30-34'] + UC3_FEMALE['25-29'] + UC3_FEMALE['30-34'],
              '35-44': UC3_MALE['35-39'] + UC3_MALE['40-44'] + UC3_FEMALE['35-39'] + UC3_FEMALE['40-44'],
              '45-54': UC3_MALE['45-49'] + UC3_MALE['50-54'] + UC3_FEMALE['45-49'] + UC3_FEMALE['50-54'],
              '55-64': UC3_MALE['55-59'] + UC3_FEMALE['55-59'] + AGE_60_64*(UC3_MALE['60+'] + UC3_FEMALE['60+'])}
    spB = {'25-34': A3_AGE['25-29'][3] + A3_AGE['30-34'][3], '35-44': A3_AGE['35-39'][3] + A3_AGE['40-44'][3], '45-54': A3_AGE['45-49'][3] + A3_AGE['50+'][3], '55-64': 0}
    singleShare = {k: (A1_PEOPLE[k] - A1_MARRIED_SP[k] - cohabB[k] - spB[k])/A1_PEOPLE[k] for k in A1_PEOPLE}
    singleW = [POP[a - 25]*singleShare['25-34' if a < 35 else '35-44' if a < 45 else '45-54' if a < 55 else '55-64'] for a in range(25, 67)]
    wifeNoKids = bands_to_ages(FG3_WIFE['noKids'], POP_F)
    # partnered share of adults 25-49 (45-49: the 45-54 band's rates on its 45-49 population)
    r45 = sum(POP[a - 25] for a in range(45, 50))/sum(POP[a - 25] for a in range(45, 55))
    part = A1_MARRIED_SP['25-34'] + cohabB['25-34'] + A1_MARRIED_SP['35-44'] + cohabB['35-44'] + r45*(A1_MARRIED_SP['45-54'] + cohabB['45-54'])
    ppl = A1_PEOPLE['25-34'] + A1_PEOPLE['35-44'] + r45*A1_PEOPLE['45-54']
    p = part/ppl
    s = (C2_ONE[0])/(C2_ONE[0] + C2_BOTH[0])
    kC, kS = (1 - s)/p, s/(1 - p)
    mothersOnly = (4055 + 5200 + 5833)/sum(C2_ONE)
    womenCouples = 0.5*(sh['coupleKids'] + sh['coupleNoKids'])
    womenSingle = (WOMEN_25_64 - womenCouples - mothersOnly*sh['singleParent'])/sh['single']
    return dict(singleW=singleW, wifeNoKids=wifeNoKids, p=p, s=s, kC=kC, kS=kS, mothersOnly=mothersOnly, womenSingle=womenSingle, singleShare=singleShare)

if __name__ == '__main__':
    n, married, cohab, sh = composition()
    print('Adults 25-64: %.0f thousand; married, spouse present %.0f (%.1f%%); cohabiting about %.0f (%.1f%%)' % (n, married, married/n*100, cohab, cohab/n*100))
    print('Composition, per adult 25-64: ' + ', '.join('%s %.4f' % (k, v) for k, v in sh.items()))
    print('Children (1, 2, 3, 4+), per parent: ' + '; '.join('%s %s' % (k, ' '.join('%.4f' % x for x in v)) for k, v in kids_dist().items()))
    print('Children\'s ages (under 6, 6-11, 12-17): ' + '; '.join('%s %s' % (k, ' '.join('%.4f' % x for x in v)) for k, v in kid_ages().items()))
    b, cc = baskets()
    print('Household baskets at $%.2f (the model\'s one-adult basket), dollars a year:' % X)
    for t, v in b.items():
        print('  %-7s total %8.0f (x%.4f)  ' % (t, v['total'], v['total']/X) + ' '.join('%s %.0f' % (k, x) for k, x in v['comp'].items()))
    print('Childcare by care type (first child, toddler care; second, preschool; third, school-age): ' + ', '.join('%.0f' % x for x in cc))
    print('Official poverty thresholds 2025 (adults, children): ' + ', '.join('%d+%d $%s' % (k[0], k[1], format(v, ',')) for k, v in THRESH_2025.items()))
    B = ages_and_births()
    print('Ages, sex and births (B4):')
    print('  singles\' share of people by band: ' + ', '.join('%s %.4f' % kv for kv in B['singleShare'].items()))
    print('  CFG.HH_AGE_SINGLE = [' + ','.join('%.1f' % x for x in B['singleW']) + '];')
    print('  CFG.HH_AGE_WIFE_NOKIDS = [' + ','.join('%.1f' % x for x in B['wifeNoKids']) + '];')
    print('  partnered share of adults 25-49 %.4f; births to women without a partner (C2, children under 6 with one parent) %.4f' % (B['p'], B['s']))
    print('  CFG.HH_FERT_K = {couple:%.4f, single:%.4f};' % (B['kC'], B['kS']))
    print('  CFG.HH_FEMALE = {single:%.4f, singleParent:%.4f, entrant:%.4f};' % (B['womenSingle'], B['mothersOnly'], WOMEN_AT_25))
    print('  CFG.HH_GAP = ' + str([[g[0], g[1], g[2], g[3]] for g in FG3_GAP]).replace(' ', '') + ';  (husband minus wife: lowest, highest, without children, with)')

