#!/usr/bin/env python3
"""S62 (Nov 14, 2026; research-update prereg/2026-11-s62-ptf-realism.md): the sources of PTF_OPS (row option po), PTF realism, and the readings derived
from them. Every figure below was read in the opened source on Nov 14, 2026 (the downloaded file's SHA-256 where a file was downloaded); nothing is fitted
and no engine run is involved. Writes sources/s62_ptf_ops.json.

The EIA ratio is recomputed here from the per-utility rows when the file is given (python3 sources/s62_ptf_ops.py --eia PATH/table_6.xlsx, needs
openpyxl); otherwise the figure as read is used.

Usage: python3 sources/s62_ptf_ops.py [--eia PATH]
"""
import json, os, sys

SRC = {
  'aies': {'cite': 'US Census Bureau, Annual Integrated Economic Survey 2024, national tables AIES00BASIC and AIES00EXP02 (released Sep 2026), United States, all establishments',
           'url': ['https://www2.census.gov/programs-surveys/aies/data/2024/AIES00BASIC.zip', 'https://www2.census.gov/programs-surveys/aies/data/2024/AIES00EXP02.zip'],
           'sha256': ['39c4235026672e7bffdbc36292ed976726df368f2ca435219aef1c84e8e4faa6', '568874267bbeb7687eeb6a2fcb16860212ed40a494fe0fe038490736c2ffa6f7'],
           'read': {  # $ thousands; employees in number (pay period including March 12)
             '445 food and beverage stores': {'revenue': 982152009, 'payroll': 101653223, 'employees': 3395400, 'operating_expenses': 255664944},
             '4451 grocery stores': {'revenue': 885740445, 'payroll': 92002595, 'employees': 3037443, 'operating_expenses': 227568598},
             '22 utilities': {'revenue': 790488295, 'payroll': 89920406, 'fringe_benefits': 26781411, 'employees': 716627, 'operating_expenses': 581352215},
             '6244 child day care, all': {'revenue': 65546955, 'payroll': 32143542, 'employees': 1089087, 'operating_expenses': 60760890},
             '6244 child day care, exempt from federal income tax': {'revenue': 20651715, 'payroll': 11043938, 'employees': 331492, 'operating_expenses': 20027614}},
           'note': 'operating expenses exclude the cost of goods resold (retail); for utilities they include purchased fuel and power'},
  'census_gm': {'cite': "Census, grocers' gross margin 28.8% (Annual Retail Trade Survey; the engine's figure since plan step 5)", 'read': {'gross_margin': 0.288}},
  'bea_nos': {'cite': "BEA 2025, net operating surplus less depreciation as a share of sales (the engine's plan step 5 figures, COST_DEFAULTS)",
              'read': {'food_share_of_food_sales': 0.0494, 'utilities_share_of_housing_component': 0.0260, 'utilities_share_of_housing_PTFS_UTIL': 487.685/(3326.284 + 487.685)}},
  'fmi': {'cite': 'FMI (The Food Industry Association), 2025 food-retail net margin', 'read': {'net_margin': 0.017}, 'note': "FMI's own release; confirmed by S56 (audits/2026-11-s39-s55-review-triage.md, A3)"},
  'nga': {'cite': 'NGA/FMS Independent Grocers Financial Survey, fiscal 2024', 'read': {'net_margin': 0.019}, 'note': 'trade-press summary only; not used for a figure'},
  'eia861': {'cite': 'EIA, Electric Sales, Revenue, and Average Price 2024, Table 6 (residential bundled retail sales by utility; forms EIA-861 schedules 4A and 4D and EIA-861S)',
             'url': 'https://www.eia.gov/electricity/sales_revenue_price/xls/table_6.xlsx', 'sha256': '925e336bb8fb88982f8428e17de752fe7279546c1dd36c9e157f2a041a7dca9e',
             'read': {'public_over_iou_within_state': 0.8385, 'states_public': 45, 'coop_over_iou_within_state': 0.9419, 'states_coop': 43,
                      'national_cents_per_kWh': {'investor_owned': 16.922, 'cooperative': 13.465, 'municipal': 13.526, 'political_subdivision': 12.923, 'state': 21.895, 'federal': 12.4}},
             'note': "public power = municipal, state, political subdivision and federal utilities; within each state, public power's average residential price over investor-owned utilities', weighted by public power's residential sales"},
  'appa': {'cite': 'American Public Power Association, What is public power? (publicpower.org/public-power)', 'read': {'payments_to_community_share_of_revenue': 0.051},
           'note': 'public power pays on average 5.1% of electric operating revenues to the community (taxes, fees, services); its prices cover that'},
  'crs': {'cite': 'Congressional Research Service, R48252 (2024), child care', 'read': {'profit_most_providers_below': 0.01}, 'note': 'personnel "often the largest share" of a centre\'s budget; confirmed by S56'},
  'ncg': {'cite': 'National Co+op Grocers, About us (ncg.coop/about-us)', 'read': {'coops': 169, 'stores': 241, 'sales_billion': 2.8}, 'note': 'no margin figures are published there; none is used'},
  'ces': {'cite': 'BLS Current Employment Statistics, 2024 annual averages of monthly figures (FRED series PAYEMS, CES4244500001, CES4422000001; thousands of jobs)',
          'url': 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=PAYEMS&cosd=2024-01-01&coed=2024-12-01 (and the two others)',
          'sha256': ['cb6f1f5824631d8d5263b2f6f6d2feee727d6698a012b0b840b17b062c871f75', '448adf6a7121dc5c4cefdf4b77c1b904dfa91238364e48aae1e804bb3c519880', 'f0230bd716ac864f9be283cd4f6fc1215327b2887980e213de0ea126d95d0ae2'],
          'read': {'all_nonfarm': 157693.8333, 'food_and_beverage_stores': 3228.2917, 'utilities': 592.4583}},
  'blei': {'cite': 'Duke Johnson, Basic Living Economic Index, Research Hub (bettertobest.github.io/research-hub/basic-living-economic-index.html), section 3.3 and 6.1',
           'read': {'eps_base': 2.64, 'cost_share_base': 0.378, 'eps_conservative_early': 2.22, 'eps_establishment': [1.5, 2.0], 'eps_low_density': [1.5, 1.8], 'density_test': 0.40},
           'note': '"PTF prices are set to cover direct costs plus minimal cooperative overhead"; "Below approximately 40% PTF merchant participation in a given zone, epsilon falls toward 1.5-1.8x"'},
}

def eia_ratio(path):
    import openpyxl
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True).active
    rows = [r for r in ws.iter_rows(values_only=True) if r and isinstance(r[3], (int, float)) and r[4]]
    pub, st = {'Municipal', 'State', 'Political Subdivision', 'Federal'}, {}
    for r in rows:
        k = 'iou' if r[2] == 'Investor Owned' else 'pub' if r[2] in pub else 'coop' if r[2] == 'Cooperative' else None
        if k: s = st.setdefault(r[1], {'iou': [0, 0], 'pub': [0, 0], 'coop': [0, 0]}); s[k][0] += r[4]; s[k][1] += r[5]
    out = {}
    for g in ('pub', 'coop'):
        num = den = 0
        for v in st.values():
            if v['iou'][0] > 0 and v[g][0] > 0: num += v[g][0]*(v[g][1]/v[g][0])/(v['iou'][1]/v['iou'][0]); den += v[g][0]
        out[g] = num/den
    return out

def main():
    if '--eia' in sys.argv:
        r = eia_ratio(sys.argv[sys.argv.index('--eia') + 1]); SRC['eia861']['read']['public_over_iou_within_state'] = round(r['pub'], 4); SRC['eia861']['read']['coop_over_iou_within_state'] = round(r['coop'], 4)
    A, U = SRC['aies']['read']['445 food and beverage stores'], SRC['aies']['read']['22 utilities']
    pu, res = SRC['bea_nos']['read']['utilities_share_of_housing_PTFS_UTIL'], SRC['fmi']['read']['net_margin']
    nos_f, nos_u = SRC['bea_nos']['read']['food_share_of_food_sales'], SRC['bea_nos']['read']['utilities_share_of_housing_component']/pu
    C = SRC['ces']['read']
    D = {
      'full_food': 1 - nos_f + res, 'full_utilities': 1 - nos_u + res, 'full_no_reserve_food': 1 - nos_f, 'full_no_reserve_utilities': 1 - nos_u,
      'sector_food': 1 - SRC['census_gm']['read']['gross_margin'] + A['operating_expenses']/A['revenue'], 'sector_utilities': 0.839,
      'utilities_operating_expenses_over_revenue': U['operating_expenses']/U['revenue'],
      'child_care_tax_exempt_cost_over_revenue': SRC['aies']['read']['6244 child day care, exempt from federal income tax']['operating_expenses']/SRC['aies']['read']['6244 child day care, exempt from federal income tax']['revenue'],
      'hub_food_cost_share_mature': 1/2.64, 'hub_food_cost_share_low': 1/1.65, 'hub_utilities_cost_share': 1/1.80,
      'payroll_share_food': A['payroll']/A['revenue'], 'payroll_share_utilities': U['payroll']/U['revenue'],
      'ptf_jobs_share_k': (C['food_and_beverage_stores'] + C['utilities'])/C['all_nonfarm'],
      'employees_per_million_revenue_food': A['employees']/(A['revenue']/1000), 'employees_per_million_revenue_utilities': U['employees']/(U['revenue']/1000),
    }
    D['price_reading_cut_food'] = 1 - D['full_food']; D['price_reading_cut_utilities'] = 1 - D['full_utilities']
    D['hub_price_over_full_cost_food'] = D['hub_food_cost_share_mature']/D['full_food']; D['hub_price_over_full_cost_utilities'] = D['hub_utilities_cost_share']/D['full_utilities']
    out = {'sources': SRC, 'derived': {k: round(v, 6) for k, v in D.items()}}
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's62_ptf_ops.json')
    json.dump(out, open(p, 'w'), indent=1); [print(k, round(v, 4)) for k, v in D.items()]; print('wrote', p)

if __name__ == '__main__':
    main()
