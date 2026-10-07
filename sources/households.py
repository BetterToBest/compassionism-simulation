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
