"""S14: the cost-of-living line's level and what is fitted at it (research-update prereg/2026-11-lw-weighted-line.md).

CFG.LIVING_WAGE_ANNUAL is one adult's living wage (MIT Living Wage Calculator, Feb 2026 build, one adult, no children): the unweighted mean of the 51
state figures x 2,080 hours, $49,369.82. Three sets of constants are fitted at that level from the eight MIT state pages in mit_household_types.json
(households.py, section 4): the basket shares (CFG.BASKET), the household-type ratios (CFG.HH_RATIO) and the childcare dollars (CFG.HH_CHILDCARE).
A different line moves all three, so a run at another line needs them refitted, by the same method, at that line. This script prints them.

  python3 sources/lw_line.py              the sets for the lines below, as the engine's CFG.LW_SETS
  python3 sources/lw_line.py 51201.28     one line

The lines (dev/reports/lw-weighted-line.md):
  ext  $51,201.28 = $24.6160 an hour x 2,080: the population-weighted mean of MIT's 51 state figures (first reported by an outside AI review,
       v4.11), Census Vintage 2025 weights; re-derived Oct 31, 2026 to the cent by sources/lw_check_ext.py.
  bea  $51,838: the current line x 1.0500, the ratio of the population-weighted to the unweighted mean of a fit of MIT's one-adult pre-tax total on
       BEA's all-items Regional Price Parity (2024) across the eight states, applied to all 51 (Census Vintage 2025 populations). sources/lw_bea.py.
MIT's terms allow web use of at most ten locations; more needs a licence, so the 51 state figures are not pulled here.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import households

LINES = {'ext': 24.6160*2080}
MODEL = {'food': 'food', 'housing': 'housing', 'medical': 'medical', 'transport': 'transport', 'civic': 'civic', 'internet': 'internet',
         'other': 'other', 'taxes': 'taxes'}
TYPES = {'1a0k': '1A0C', '1a1k': '1A1C', '1a2k': '1A2C', '1a3k': '1A3C', '2a0k': '2A2W0C', '2a1k': '2A2W1C', '2a2k': '2A2W2C', '2a3k': '2A2W3C'}

def at(L):
    households.X = L
    b, cc = households.baskets()
    one = b['1A0C']['comp']
    basket = {k: round(one[k]/L, 4) for k in MODEL}
    basket['other'] = round(1 - sum(v for k, v in basket.items() if k != 'other'), 4)  # as CFG.BASKET: 'other' takes the rounding, so the shares sum to 1
    ratio = {t: {k: round(b[m]['comp'][k]/one[k], 6) for k in MODEL} for t, m in TYPES.items()}
    return {'L': round(L, 2), 'basket': basket, 'ratio': ratio, 'care': [round(x, 2) for x in cc]}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(json.dumps(at(float(sys.argv[1])), indent=1)); sys.exit()
    import lw_bea
    LINES['bea'] = lw_bea.line()
    print(json.dumps({'base': at(49369.82)}, indent=1))
    print('CFG.LW_SETS = ' + json.dumps({k: at(v) for k, v in LINES.items()}, separators=(',', ':')) + ';')
