# US births: national figures (input for v5.3 children, plan item B4)

Given by Duke Johnson on Oct 6, 2026 (pasted from CDC/NCHS FastStats, "Births and Natality"; the data year was not in the paste and is to be confirmed against the NCHS release). cdc.gov refuses connections from the build environment (HTTP 403, Oct 6, 2026), so these figures could not be fetched here directly.

| Measure | Value |
|---|---|
| Number of births | 3,628,934 |
| Birth rate | 10.7 per 1,000 population |
| General fertility rate | 53.8 births per 1,000 women aged 15-44 |
| Born low birthweight | 8.52% |
| Born preterm | 10.41% |
| Births to unmarried mothers | 39.5% |
| Mean age of the mother at first birth | 27.6 |

How v5.3 uses them: as checks on the model's births (the general fertility rate, the mean age at first birth, the share of births to unmarried mothers, which bears on single-parent households). The births by the mother's age that the model draws from need an age breakdown; the Census Bureau's API now asks for a key, so the breakdown is to come from the Census Bureau's published fertility tables (CPS June supplement or ACS table B13016, women with a birth in the past 12 months by age) or an NCHS copy Duke uploads. Low birthweight and preterm births are not modelled.
