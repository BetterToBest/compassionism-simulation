"""The three sourced values of the study of output per hour and automation: own, s_L and y_K.
Written Nov 19, 2026 (research-update prereg/2026-11-s85-output-per-hour.md, Amendment 1 item 5; the values are fixed in Amendment 2,
before the dry run). Each value is computed from the extracts in s85_values/, which were cut from the full downloads named below.

own: the share of US corporate equity held by US households, directly or through funds, pensions, IRAs and annuities.
  Rosenthal and Burke, "Who's Left to Tax? US Taxation of Corporations and Their Shareholders", NYU Tax Policy Colloquium,
  Oct 27, 2020 (Urban-Brookings Tax Policy Center), appendix Table 4 (2019, $ billions, "All US equity" column). The PDF was
  supplied by Duke on Nov 19, 2026; SHA-256 below. Households' share = life insurance separate accounts + DB plans + DC plans
  + IRAs + taxable accounts. Not households: foreigners, government, nonprofits.
s_L: BLS, labour productivity and related measures for major sectors (released Nov 5, 2026), sheet MachineReadable: nonfarm
  business sector, all workers (the self-employed's labour compensation imputed), labor share, percentage, annual. Latest full
  year, 2025. Extract: s85_values/bls_labor_share_nfb.csv.
y_K: capital's share of output per dollar of net capital in the essentials industries, (1 - s_L,ess) x value added / net stock.
  BEA GDP by industry, Components of Value Added by Industry, table TVA113-A (data published Sept 30, 2026), 2024; BEA Fixed
  Assets, Table 3.1ESI (current-cost net stock of private fixed assets by industry) and, for housing, Table 1.1 line 8 (private
  residential fixed assets, owner- and tenant-occupied, matching the value added of the Housing line, which includes
  owner-occupied housing), 2024. Within a sector the industries are pooled (capital-weighted); the sectors are weighted by the
  basket's shares (CFG.BASKET: food 9.0, housing including utilities 27.6, medical 6.9). Extract: s85_values/bea_2024.csv.
  The preregistration caps y_K at 0.32 (the backing study's economy-wide output per dollar of capital); the full-value reading
  (`vk`, value added per dollar of capital) is capped there too.

Run: python3 sources/s85_values.py   (prints the values and writes s85_values.json)
"""
import csv, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
FULL = {  # the full downloads the extracts were cut from (Nov 19, 2026)
    'bea_ValueAdded.xlsx': ('https://apps.bea.gov/industry/Release/XLS/GDPxInd/ValueAdded.xlsx',
                            '737628be9c44bbb49c2a9ec5c9c7c8d843cf849aa6f0e46024a02f0875818b74'),
    'bea_FixedAssets.txt': ('https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt',
                            '486d6b364cfcdf15b6d3779256563b911865920ade7d96566413baa9114b7a93'),
    'bls_labor-productivity-major-sectors.xlsx': ('https://www.bls.gov/web/prod2/labor-productivity-major-sectors.xlsx',
                            '0e81cfa1dd37d6b11de7e61481349151ec156485308b1e9f2b9b87f1ed6f2534'),
    'rosenthal_burke_2020.pdf': ('supplied by Duke (TPC: www.taxpolicycenter.org, "Who\'s Left to Tax?")',
                            '16832d53a179d1b1e9ab86094ca9d8c3d57296ea47733dc3dbf3a4df88ca380a'),
}
# Rosenthal and Burke (2020), appendix Table 4, "All US equity" ($ billions, 2019), read from the PDF's page 16 (printed 14).
RB_T4 = {'Foreigners': 15988, 'Life insurance separate accounts': 1065, 'DB plans': 3102, 'DC plans': 3220, 'IRAs': 4690,
         'Government': 368, 'Nonprofits': 1955, 'Taxable accounts': 9498}
RB_TOTAL = 39886
HOUSEHOLD = ('Life insurance separate accounts', 'DB plans', 'DC plans', 'IRAs', 'Taxable accounts')
BASKET = {'food': 9.0, 'housing': 27.6, 'medical': 6.9}
CAP = 0.32

def main():
    assert sum(RB_T4.values()) == RB_TOTAL, 'Table 4 rows do not sum to its total'
    own = sum(RB_T4[k] for k in HOUSEHOLD)/RB_TOTAL
    with open(os.path.join(HERE, 's85_values', 'bls_labor_share_nfb.csv')) as f:
        ls = {int(r['year']): float(r['labor_share_pct']) for r in csv.DictReader(f)}
    yr = max(ls); s_L = ls[yr]/100
    sec = {}
    with open(os.path.join(HERE, 's85_values', 'bea_2024.csv')) as f:
        for r in csv.DictReader(f):
            a = sec.setdefault(r['basket_sector'], [0.0, 0.0, 0.0])
            a[0] += float(r['value_added_musd']); a[1] += float(r['compensation_musd']); a[2] += float(r['net_stock_musd'])
    W = sum(BASKET.values())
    yK = sum(BASKET[s]/W*(va - c)/k for s, (va, c, k) in sec.items())
    vk = sum(BASKET[s]/W*va/k for s, (va, c, k) in sec.items())
    sLess = sum(BASKET[s]/W*c/va for s, (va, c, k) in sec.items())
    out = {'own': round(own, 4), 's_L': round(s_L, 4), 's_L_year': yr, 'yK': round(min(CAP, yK), 4), 'yK_uncapped': round(yK, 4),
           'vk': round(min(CAP, vk), 4), 'vk_uncapped': round(vk, 4), 's_L_ess': round(sLess, 4),
           'by_sector': {s: {'s_L': round(c/va, 4), 'yK': round((va - c)/k, 4), 'va_per_k': round(va/k, 4), 'weight': round(BASKET[s]/W, 4)}
                         for s, (va, c, k) in sec.items()},
           'yK_sector_capped': round(sum(BASKET[s]/W*min(CAP, (va - c)/k) for s, (va, c, k) in sec.items()), 4),
           'full_downloads': {k: {'url': u, 'sha256': h} for k, (u, h) in FULL.items()}}
    print('own %.4f (US households, 2019)   s_L %.4f (%d)   y_K %.4f (uncapped %.4f; each sector capped %.4f)   vk %.4f (uncapped %.4f)'
          % (out['own'], s_L, yr, out['yK'], yK, out['yK_sector_capped'], out['vk'], vk))
    for s, v in out['by_sector'].items():
        print('  %-8s weight %.4f  labour share %.3f  capital income per $ of capital %.4f  value added per $ %.4f' % (s, v['weight'], v['s_L'], v['yK'], v['va_per_k']))
    with open(os.path.join(HERE, 's85_values.json'), 'w') as f:
        json.dump(out, f, indent=1)

if __name__ == '__main__':
    main()
