"""v5.3 B7 (Oct 7, 2026; plan item B7, "income-graded spending"): how spending rises with income, from the Consumer Expenditure Survey.

Source: U.S. Bureau of Labor Statistics, Consumer Expenditure Survey, 2024, quintiles of income before taxes (all consumer units), read Oct 7, 2026 from
FRED, Federal Reserve Bank of St. Louis, which republishes the BLS series (bls.gov refuses scripted downloads from the build environment):
  income before taxes   CXUINCBEFTXLB0102M ... LB0106M  (lowest ... highest 20 percent)
  total expenditures    CXUTOTALEXPLB0102M ... LB0106M
  persons per unit      CXU980010LB0102M ... LB0106M
Per equivalent adult (each amount over the square root of the persons per unit, the OECD square-root scale the household measures use), the slope of
log spending on log income is the income elasticity of spending. The lowest quintile spends twice its reported income (transfers, savings drawn down
and under-reported income, which the CE's own documentation notes), so the slope is taken over quintiles 2-5 (CFG.CE_SPEND_ELAST); the slope over all
five is printed beside it.

Usage: python3 sources/ce_spending.py   (prints the inputs and the elasticity; no download: the values are transcribed below with their series)
"""
import math
INCOME = [16658, 42925, 74474, 121548, 264510]   # CXUINCBEFTXLB0102M..LB0106M, 2024
SPEND = [35046, 50054, 66900, 89972, 150342]     # CXUTOTALEXPLB0102M..LB0106M, 2024
PERSONS = [1.6, 2.1, 2.5, 2.9, 3.2]              # CXU980010LB0102M..LB0106M, 2024
def slope(xs, ys):
    mx, my = sum(xs)/len(xs), sum(ys)/len(ys)
    return sum((x - mx)*(y - my) for x, y in zip(xs, ys))/sum((x - mx)**2 for x in xs)
x = [math.log(i/math.sqrt(n)) for i, n in zip(INCOME, PERSONS)]
y = [math.log(s/math.sqrt(n)) for s, n in zip(SPEND, PERSONS)]
for q in range(5):
    print('quintile %d: income %d, spending %d, persons %.1f; per equivalent adult income %.0f, spending %.0f (spending / income %.2f)'
          % (q + 1, INCOME[q], SPEND[q], PERSONS[q], math.exp(x[q]), math.exp(y[q]), SPEND[q]/INCOME[q]))
print('income elasticity of spending, quintiles 2-5: %.4f (CFG.CE_SPEND_ELAST); all five quintiles: %.4f' % (slope(x[1:], y[1:]), slope(x, y)))
