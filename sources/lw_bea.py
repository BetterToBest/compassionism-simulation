"""S14: a licence-free estimate of how much population weighting raises the cost-of-living line (dev/reports/lw-weighted-line.md).

The line is the unweighted mean of MIT's 51 state one-adult living wages. A population-weighted mean needs all 51 figures, and MIT's terms allow web use
of at most ten locations, so this estimates the ratio instead. Fit MIT's one-adult pre-tax total on BEA's all-items Regional Price Parity across the eight
state pages already in mit_household_types.json (within MIT's terms), predict all 51, and take the population-weighted over the unweighted mean of the
predictions. The ratio, not the predicted level, is used: line() = $49,369.82 x ratio.

Sources (both US federal, public domain):
  BEA, Regional Price Parities by state, SARPP table, line 1 "RPPs: All items", 2024 (apps.bea.gov/regional/zip/SARPP.zip, released Feb 11, 2026;
    SARPP_STATE_2008_2024.csv sha256 9c0cbbf81061b6721fc31f580719b1c57489aef75b70e933ed2386b4dff79863).
  Census Bureau, Vintage 2025 state population estimates, POPESTIMATE2025 (www2.census.gov/programs-surveys/popest/datasets/2020-2025/state/totals/
    NST-EST2025-ALLDATA.csv, sha256 92188e29cb0a67dcf95afa7d6c47359409782f086478b70ea4128eb70e223ca9). Puerto Rico left out (MIT covers 50 states + DC).
Read Oct 31, 2026.

  python3 sources/lw_bea.py     the fit, the ratio, the leave-one-state-out range and the other RPP series' ratios are in the report
"""
import json, os

STATES = {
    'Alabama': (88.823, 5193088),
    'Alaska': (102.359, 737270),
    'Arizona': (100.677, 7623818),
    'Arkansas': (86.937, 3114791),
    'California': (110.720, 39355309),
    'Colorado': (103.052, 6012561),
    'Connecticut': (103.610, 3688496),
    'Delaware': (99.808, 1059952),
    'District of Columbia': (109.901, 693645),
    'Florida': (103.414, 23462518),
    'Georgia': (96.293, 11302748),
    'Hawaii': (109.951, 1432820),
    'Idaho': (95.494, 2029733),
    'Illinois': (99.958, 12719141),
    'Indiana': (93.329, 6973333),
    'Iowa': (87.762, 3238387),
    'Kansas': (90.068, 2977220),
    'Kentucky': (90.159, 4606864),
    'Louisiana': (88.207, 4618189),
    'Maine': (97.050, 1414874),
    'Maryland': (104.959, 6265347),
    'Massachusetts': (105.757, 7154084),
    'Michigan': (96.217, 10127884),
    'Minnesota': (98.621, 5830405),
    'Mississippi': (86.953, 2954160),
    'Missouri': (90.817, 6270541),
    'Montana': (94.645, 1144694),
    'Nebraska': (90.103, 2018006),
    'Nevada': (99.979, 3282188),
    'New Hampshire': (104.165, 1415342),
    'New Jersey': (108.805, 9548215),
    'New Mexico': (92.212, 2125498),
    'New York': (107.921, 20002427),
    'North Carolina': (94.326, 11197968),
    'North Dakota': (88.959, 799358),
    'Ohio': (92.774, 11900510),
    'Oklahoma': (87.843, 4123288),
    'Oregon': (103.361, 4273586),
    'Pennsylvania': (97.572, 13059432),
    'Rhode Island': (102.280, 1114521),
    'South Carolina': (93.749, 5570274),
    'South Dakota': (88.586, 935094),
    'Tennessee': (91.870, 7315076),
    'Texas': (97.057, 31709821),
    'Utah': (98.864, 3538904),
    'Vermont': (97.958, 644663),
    'Virginia': (101.104, 8880107),
    'Washington': (107.013, 8001020),
    'West Virginia': (89.497, 1766147),
    'Wisconsin': (94.095, 5972787),
    'Wyoming': (92.691, 588753),
}

LINE = 49369.82

def fit(states=None):
    mit = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mit_household_types.json'), encoding='utf-8'))['states']
    ks = [s for s in mit if states is None or s in states]
    xs = [STATES[s][0] for s in ks]; ys = [mit[s]['rows']['Required annual income before taxes'][0] for s in ks]
    mx, my = sum(xs)/len(xs), sum(ys)/len(ys)
    b = sum((x - mx)*(y - my) for x, y in zip(xs, ys))/sum((x - mx)**2 for x in xs); a = my - b*mx
    r2 = 1 - sum((y - a - b*x)**2 for x, y in zip(xs, ys))/sum((y - my)**2 for y in ys)
    pred = {s: a + b*v[0] for s, v in STATES.items()}; P = sum(v[1] for v in STATES.values())
    uw = sum(pred.values())/len(pred); w = sum(pred[s]*STATES[s][1] for s in STATES)/P
    return {'a': a, 'b': b, 'r2': r2, 'n': len(ks), 'unweighted': uw, 'weighted': w, 'ratio': w/uw}

def line():
    return round(LINE*fit()['ratio'], 2)

if __name__ == '__main__':
    f = fit(); print('fit on %d states: a %.1f, b %.2f a point, R2 %.3f' % (f['n'], f['a'], f['b'], f['r2']))
    print('predicted mean, unweighted %.0f, population-weighted %.0f, ratio %.4f; line $%.2f' % (f['unweighted'], f['weighted'], f['ratio'], line()))
    mit = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mit_household_types.json'), encoding='utf-8'))['states']
    lo = [fit([s for s in mit if s != d])['ratio'] for d in mit]
    print('leaving one state out: ratio %.4f to %.4f, line $%.0f to $%.0f' % (min(lo), max(lo), LINE*min(lo), LINE*max(lo)))
