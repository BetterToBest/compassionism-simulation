# GAPS & DOUBTS

## Coverage note
Latest year is 2025 (income year), per Census P60-290 (Sept 2026). The original request assumed 2024 as latest; 2025 is included wherever the source publishes it.

## poverty_official.csv
- 2024 below-50% value_original empty: P60-287 Table A-1 does not publish the official below-50% share, so no originally-published value could be verified.
- 2020 row note wording: the file follows Census's survey-year convention; strictly, income-year-2020 estimates come from the 2021 CPS ASEC (fielded Feb–Apr 2021).
- Nonresponse-bias quantification for income years 2024–2025 was not checked (opened blog covers survey years through 2024 = income year 2023); 2024/2025 rows carry no nonresponse note.
- 2013 choice: value uses the redesigned-questions subsample (forward-comparable); value_original uses the traditional-questions subsample (originally-published headline). Swapping the two columns for 2013 would give the originally-published headline as value.
- Threshold concept (thresholds.csv): official threshold uses the four-person/two-children cell, not Historical Table 1's weighted-average four-person threshold (e.g. 2025 weighted average 32970 vs cell 32649). Choice documented in every threshold row's note.

## poverty_spm.csv
- Corrected SPM thresholds 2020–2023, value empty in thresholds.csv: BLS reissued 2019–2024 thresholds July 2026, but the BLS corrected-thresholds XLSX could not be opened by the researcher (BLS blocks automated download). Fill from BLS "SPM Thresholds (XLSX)" at https://www.bls.gov/pir/spm/spm_thresholds_2024_correction.htm via live browser. value_original holds the as-published values.
- Census "SPM rate before taxes and transfers" is not published as a single series. Only the 2023 market-income count (77800 thousands) is included; the 2019–2023 market-income series in the Census story is an image, not a transcribed table. Columbia "without taxes and transfers" covers 2005–2012.
- Program-effect tables give marginal effects (each element removed in isolation) — do NOT sum marginal lifted counts.
- EITC alone 2019–2023: empty. Not separated pre-P60-290. Do not derive EITC by subtracting refundable CTC from refundable tax credits — components are marginal effects, not additive. EITC alone separated only in P60-290 (2024, 2025).
- Lifted SNAP 2020: empty. 2020 figure combines SNAP + school lunch (3209 thousands); SNAP-alone count not in that figure (only -0.89pp rate effect in P60-277 Table B-7).
- Lifted counts 2021: percentage points only (Table B-7 in that vintage reports rate effects, not counts).
- Lifted counts 2009–2018: not included; earlier SPM reports' program-effect figures were not opened.
- Stimulus rows only 2020–2021 by design.
- 2019 lifted values rounded to nearest 0.1M in the P60-272 source figure (e.g. Social Security 26500) — treat as +/-50 thousands precision.
- 2019–2024 SPM rates restated: BLS corrected SPM thresholds 2019–2024 on July 17, 2026 (coding errors in in-kind-benefit imputations; base rebased from 83% to 82% of median expenditures). Census re-released 2019–2024 SPM estimates in P60-290 (Sept 2026) and SEHSD-WP2026-17. value = latest P60-290; value_original = P60-287 (Sept 2025).
- 2017 main row uses the updated-processing-system row (13.0 all) as the comparable series; prior-processing row (13.9) in notes.

## poverty_spm_history.csv
- Overlap check — Census SPM vs Columbia, all persons: Census 2009 15.1 / 2010 15.9 / 2011 16.1 / 2012 16.0; Columbia historical 15.16 / 15.95 / 16.07 / 15.99; Columbia anchored 14.63 / 15.29 / 15.41 / 15.99. Differences reflect methodology, not error.
- Anchored SPM thresholds anchored to 2012 SPM thresholds (inflation-adjusted); historical SPM uses year-specific thresholds.

## macro_drivers.csv
- value_original empty throughout: original-vintage (as-first-published) values were not retrieved; all values are latest published vintages. In particular, BEA real GDP growth and Z.1 net worth reflect current revisions, not original releases.
- 2025 BLS annual averages rest on 11 months: the BLS API returns "-" for October 2025 for both series, but BLS still publishes 2025 M13 annual averages (unemployment 4.3, CPI-U 321.943) equal to the mean of the 11 published months. The reason for the missing October observation was not verified from a BLS source.
- CPI-U percent change is computed, not taken from a BLS table: percent change in the published M13 annual-average index, rounded to 1 decimal. It matches BLS's published annual-average percent changes.
- FHFA Dec-to-Dec change is computed from published December seasonally adjusted purchase-only index levels. It is the purchase-only index, not FHFA's all-transactions index; current vintage revises history.
- Census income series breaks: 2013 uses the redesigned-questions subsample; 2017 uses the updated processing system. Alternates in notes (2013 old-questions 69470; 2017 old-processing 78900). 2020 uses 2020 Census-based population controls; 2024 uses Vintage 2025 population controls. Income in 2025 dollars (C-CPI-U 2000–2025, R-CPI-U-RS pre-2000).
- Z.1 net worth is the Sept 11, 2026 release vintage, which incorporates revisions; series is households + nonprofit organizations, Q4 year-end, converted from millions to billions by dividing by 1000.

## snap.csv
- SNAP FY2025 is the latest in the FNS annual summary file (data as of Sept 11, 2026). FY2019 participation (35702472) is as published in the file; it is a sharp drop from FY2018 (40775705) and was not independently cross-checked.
- Total benefits only; excludes All Other Costs (e.g. Federal share of State administrative expenses).

## policy_events.csv
- SCF/Policy note: see below.
- EUC08: only the ARRA window (Feb 22–Dec 26, 2009) is listed per scope; EUC08 was repeatedly extended by later laws through Dec 2013 and those later extensions are not listed as separate rows.
- Making Work Pay: phase-out thresholds not included because the opened IRS page does not state them.
- FAC: ARRA row in CRS Table A-4 gives Feb 22–Dec 26, 2009 window, while a later CRS row states FAC expired June 2, 2010; June 2, 2010 is used as end date with the CRS expiry note.
- PUA start date (2020-01-27) is the retroactive coverage start, not the Mar 27, 2020 enactment date; flagged in the amount field.

## scf_wealth.csv
- SCF: median only. The 2025 SCF was released Oct 9, 2026 (median net worth all families 215.9 thousand nominal dollars in the file) but is outside the requested 2007–2022 scope and is not included.
- DFA: year-end (Q4) values only; quarterly values are in the same file but not included. Latest quarter in the downloaded file is 2026:Q2 (Bottom50 net worth 4278.038 billions), which is not a year-end value and is therefore not included.

## Verification
Re-opened 10 randomly chosen values against their sources before delivery; verified 10 of 10, 0 failed:
1. Official poverty rate 2010, all = 15.1 (Historical Table 2)
2. Official threshold 2020, 2 adults 2 children = 26246 (thresh20.xlsx)
3. SPM rate 2021, all = 7.7 (P60-290 Table 8)
4. SPM threshold renters 2024 = 39220 (P60-290 Table 11)
5. Columbia anchored SPM rate 2008, all = 14.64 (Columbia Poverty Rates sheet, 0.14635)
6. Unemployment rate annual avg 2020 = 8.1 (BLS API, LNU04000000 M13)
7. CPI-U annual avg index 2022 = 292.655 (BLS API, CUUR0000SA0 M13)
8. SNAP FY2020 avg monthly participants = 39852778 (FNS file: 39852.778 thousands) and total benefits 73905.39 million dollars
9. SCF median net worth 2007, all families = 120.6 thousands of nominal dollars (SCF Table 4)
10. Expanded Child Tax Credit 2021 = $3600 under 6 / $3000 ages 6–17 (IRS page, re-opened)
