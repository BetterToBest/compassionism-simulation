# SOURCES — access date October 13, 2026 (all sources opened)

Coverage: income/reference year 2005 through latest available, which is 2025 (Census P60-290, published September 2026), not 2024. "year" is the income/reference year, not the publication year.

## poverty_official.csv
- U.S. Census Bureau, Historical Poverty Tables: People and Families – 1959 to 2025 — https://www.census.gov/data/tables/time-series/demo/income-poverty/historical-poverty-people.html — Tables 2, 3, 5 (.xlsx): https://www2.census.gov/programs-surveys/cps/tables/time-series/historical-poverty-people/hstpov2.xlsx , hstpov3.xlsx, hstpov5.xlsx
- CPS Historical Poverty Footnotes — https://www.census.gov/topics/income-poverty/poverty/guidance/poverty-footnotes/cps-historic-footnotes.html
- Poverty in the United States: 2024 (P60-287), Table A-1 — https://www2.census.gov/library/publications/2025/demo/p60-287.pdf (source of 2024 value_original cells)
- Census Research Matters, "Using Administrative Data to Evaluate Nonresponse Bias in the 2024 CPS ASEC" — https://www.census.gov/newsroom/blogs/research-matters/2024/09/administrative-data-nonresponse-bias-cps-asec.html

## poverty_spm.csv
- P60-290 Table 8 (SPM rates) — https://www2.census.gov/programs-surveys/demo/tables/p60/290/table_8_spm_hist.xlsx
- P60-290 Table 6 (program-effect counts 2024–2025) — https://www2.census.gov/programs-surveys/demo/tables/p60/290/table_6_spm_program_effect_counts.xlsx
- P60-287 Table B-7 — https://www2.census.gov/programs-surveys/demo/tables/p60/287/tableB-7.xlsx
- P60-283 Table B-7 — https://www2.census.gov/programs-surveys/demo/tables/p60/283/tableB-7.xlsx
- P60-280 Table B-7 — https://www2.census.gov/programs-surveys/demo/tables/p60/280/tableB-7.xlsx
- P60-277 Table B-7 — https://www2.census.gov/programs-surveys/demo/tables/p60/277/tableB-7.xlsx
- P60-272, Figure 8 (2019 program effects) — https://cdn.www.census.gov/content/dam/Census/library/publications/2020/demo/p60-272.pdf
- SPM 2020 press-kit slides — https://cdn.www.census.gov/content/dam/Census/newsroom/press-kits/2021/iphi/20210914-slides-spm-plotpoints.pdf
- Poverty 2022 press-kit slides — https://cdn.www.census.gov/content/dam/Census/newsroom/press-kits/2023/iphi/20230912-iphi-slides-poverty.pdf
- Census America Counts SPM story (2024) — https://www.census.gov/library/stories/2024/09/supplemental-poverty-measure.html (2023 market-income count)
- Census SEHSD-WP2026-17, Revising Supplemental Poverty Measure Estimates from 2019 to 2024 — https://www2.census.gov/library/working-papers/2026/demo/sehsd-wp2026-17.pdf
- BLS corrected thresholds notice — https://www.bls.gov/pir/spm/spm_thresholds_2024_correction.htm

## poverty_spm_history.csv
- Wimer, Fox, Collyer, Garfinkel, Kaushal, Laird, Nam, Nolan, Pac, Vinh & Waldfogel, Historical Supplemental Poverty Measure data 1967–2024, Center on Poverty and Social Policy, Columbia University — https://povertycenter.columbia.edu/sites/povertycenter.columbia.edu/files/content/Data/Historical/Anchored-and-Historical-Poverty-Rates-1967-to-2024_update-09_09_2025.xlsx — "Poverty Rates" sheet; landing: https://povertycenter.columbia.edu/historical-spm-data
- Foundational paper: Wimer, Fox, Garfinkel, Kaushal & Waldfogel (2016), "Progress on Poverty? New Estimates of Historical Trends Using an Anchored Supplemental Poverty Measure," Demography 53(4):1207–1218. Anchored SPM thresholds anchored to 2012 SPM thresholds (inflation-adjusted).

## thresholds.csv
- Official thresholds: Census, Poverty Thresholds by Size of Family and Number of Children — https://www.census.gov/data/tables/time-series/demo/income-poverty/historical-poverty-thresholds.html — annual thresh05.xlsx … thresh25.xlsx (four-person / two-children cell)
- SPM thresholds: P60-290 Table 11 — https://www2.census.gov/programs-surveys/demo/tables/p60/290/table_11_spm_thresh.xlsx ; SEHSD-WP2026-17 Table 1 (2019); P60-287 Table B-1 (2023 as-published); 2022 press-kit slides; SPM 2020 press-kit slides; BLS Research SPM 2021 thresholds — https://www.bls.gov/pir/spm/spm_chart1_2021data.htm ; BLS Garner (Brookings, rev. Oct 14, 2020) — https://www.bls.gov/pir/spm/garner_brookings_changs-_10_14_20.pdf ; BLS Garner & Gudrais (2012) via UNT archive — https://webarchive.library.unt.edu/web/20170125222217mp_/https://www.bls.gov/pir/spm/spm_pap_joint12.pdf

## macro_drivers.csv
- BLS Public API v2 — CPS series LNU04000000 (unemployment) and CPI-U series CUUR0000SA0, period M13 annual averages — https://api.bls.gov/publicAPI/v2/timeseries/data/
- BEA iTable — NIPA Table 1.1.1, Percent Change From Preceding Period in Real GDP, last revised Sept 30, 2026 — https://apps.bea.gov/iTable/?reqid=19&step=3&isuri=1&categories=survey&nipa_table_list=1&Series=A&select_all_years=1
- Census CPS ASEC Table H-6 (h06ar.xlsx), median household income — https://www2.census.gov/programs-surveys/cps/tables/time-series/historical-income-households/h06ar.xlsx
- FHFA HPI master file — https://www.fhfa.gov/hpi/download/monthly/hpi_master.csv
- Federal Reserve Z.1 Financial Accounts, Sept 11, 2026 release, Table S1M.b, series FL152090005.Q — https://www.federalreserve.gov/releases/z1/20260911/z1_csv_files.zip

## snap.csv
- USDA Food and Nutrition Service, SNAP Data Tables, National Level Annual Summary (snap-annualsummary-9.xlsx), data as of Sept 11, 2026 — https://www.fns.usda.gov/sites/default/files/resource-files/snap-annualsummary-9.xlsx

## policy_events.csv
- CRS R43257, Background on the Scheduled Reduction to SNAP Benefits — https://www.congress.gov/crs_external_products/R/PDF/R43257/R43257.5.pdf
- IRS, The Making Work Pay Tax Credit — https://www.irs.gov/newsroom/the-making-work-pay-tax-credit
- CRS RL34340, Extending Unemployment Compensation Benefits During Recessions — https://www.congress.gov/crs-product/RL34340
- IRS SOI, CARES Act statistics — https://www.irs.gov/statistics/soi-tax-stats-coronavirus-aid-relief-and-economic-security-act-cares-act-statistics
- DOL, FPUC $600 guidance — https://www.dol.gov/newsroom/releases/eta/eta20200404?lang=en
- DOL, PUA guidance — https://www.dol.gov/newsroom/releases/eta/eta20200405?lang=ko
- DOL UIPL 14-21 Attachment I — https://www.dol.gov/sites/dolgov/files/ETA/advisories/UIPL/2021/UIPL_14-21_Attachment_1_acc.pdf
- Treasury/IRS, second-round EIPs ($600) — https://home.treasury.gov/news/press-releases/sm1224
- DOL, ARPA UI guidance — https://www.dol.gov/newsroom/releases/eta/eta20210316
- IRS, expanded 2021 Child Tax Credit — https://www.irs.gov/newsroom/how-the-expanded-2021-child-tax-credit-can-help-your-family
- IRS IR-2021-153, advance CTC monthly payments — https://www.irs.gov/newsroom/irs-monthly-child-tax-credit-payments-begin
- Congress.gov, H.R.1 ARRA (Pub. L. No. 111-5) — https://www.congress.gov/bill/111th-congress/house-bill/1/titles

## scf_wealth.csv
- Federal Reserve SCF Historic Tables (nominal dollars), Table 4 — https://www.federalreserve.gov/econres/files/scf2025_tables_internal_nominal_historical.xlsx (linked from https://www.federalreserve.gov/econres/scfindex.htm ; historic tables updated 10/9/2026)
- Federal Reserve Distributional Financial Accounts, dfa-networth-levels.csv — https://www.federalreserve.gov/releases/z1/dataviz/download/zips/dfa.zip (overview: https://www.federalreserve.gov/releases/z1/dataviz/dfa/ ; last update Sep 18, 2026)
