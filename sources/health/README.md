# Health coverage: sources (session 2a, setting A)

These figures feed `CFG.HL_*` in `index.html` (the health-coverage block, grep `HL_KEYS`). They were read on Oct 13, 2026. Figures marked "design" have no source. They are labelled in the code and swept.

| Figure | Value | Source |
|---|---|---|
| Personal health care spending per person by age, 2020 | 0-18 $4,217; 19-44 $6,669; 45-64 $12,577; 65-84 $20,503; 85+ $35,995; working age (19-64) $9,154 | CMS, National Health Expenditure Accounts, Age and Sex tables (`cms_nhe_age_sex_percap.csv` in this folder, row "Total Personal Health Care"; the 19-64 figure is from the CMS NHE fact sheet / Age and Sex highlights, 2020) |
| Raising 2020 dollars to the model's year 0 | x 15,474 / 12,530 | CMS NHE fact sheet: national health spending per person, 2024 $15,474; 2020 $12,530 |
| Multiple chronic conditions | 25.9% of adults; 57.0% of spending | AHRQ, MEPS Statistical Brief 485 (2012 data) |
| Concentration of spending (the fit target for the spread) | top 1% 21.9%; top 5% 50.1%; bottom 50% 2.9% | AHRQ, MEPS Statistical Brief 528 (2017 data) |
| Poverty guideline | $15,650 for one person, plus $5,500 for each added person (48 states) | HHS poverty guidelines, 2025 |
| Medicaid income limits (share of the guideline) | expansion states 138% (adults); children (Medicaid and CHIP) 255%; parents in the ten non-expansion states: AL 18%, FL 26%, GA 100%, KS 38%, MS 21%, SC 67%, TN 105%, TX 15%, WI 100%, WY 43% (median 40.5%); adults without children in non-expansion states 0 (Wisconsin 100% is the exception) | KFF State Health Facts, "Medicaid income eligibility limits for parents" and "... for children", January 2026 |
| Employer coverage | premium $9,325 single, $26,993 family; worker's share $1,440 and $6,850; single deductible $1,886 | KFF, 2025 Employer Health Benefits Survey |
| ACA out-of-pocket limit | $9,200 self-only (2025); $3,050 with cost-sharing reductions under 200% of poverty | HHS, 2025 Notice of Benefit and Payment Parameters |
| Marketplace | benchmark silver premium for a 40-year-old $497 a month (2025); average deductible $2,759 (2025) | KFF marketplace premium and deductible analyses |
| Premium tax credit schedule (share of income, 2026) | 2.10% under 133% of poverty; 3.14-4.19% at 133-150%; 4.19-6.60% at 150-200%; 6.60-8.44% at 200-250%; 8.44-9.96% at 250-300%; 9.96% at 300-400%; none above 400% (the enhanced credits ended in 2025) | IRS Rev. Proc. 2025-25 |
| Medicare | Part B premium $185 a month, deductible $257 (2025); Medicare Advantage in-network out-of-pocket limit $9,350 (2025) | CMS |
| Coverage shares (checks, not inputs, apart from the two calibrated take-up figures) | whole population 2024: employer 53.8%, Medicaid 17.6%, Medicare 19.1%, direct purchase 10.7%, uninsured about 8%; ages 19-64: private 74.0%, uninsured 11% | Census Bureau, *Health Insurance Coverage in the United States: 2024* (P60-288, CPS ASEC) |
| Underinsured (definition used, and a check) | insured all year, out-of-pocket cost (not premiums) of 10% of income or more, 5% under 200% of poverty, or a deductible of 5% of income or more; 23% of adults 19-64 in 2024 | Commonwealth Fund, 2024 Biennial Health Insurance Survey |
| Medical debt (a check) | about 1 in 12 adults owe more than $250 (2021) | Peterson-KFF Health System Tracker, "The burden of medical debt in the United States" (SIPP 2021) |
| Care skipped for cost (a check) | could not get care when needed because of cost, 2024: uninsured 43.3%; other coverage types 5.7-17.3% | SHADAC State Health Compare (BRFSS 2024) |

Design parameters (no source; swept): employer offer and take-up (20% at the lowest pay to 80% at the highest) and marketplace take-up (0.60), set so the model's coverage shares come close to the Census shares above; Medicaid take-up 0.80 (children 0.90); 20% coinsurance; a child's marketplace premium at half an adult's; the acute event (8% a year, 30% of mean spending); the chronic state's persistence (0.9 a year); the share of non-acute care a burdened household skips (0.5).
