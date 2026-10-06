# US births: national figures (input for v5.3 children, plan item B4)

Given by Duke Johnson on Oct 6, 2026 (pasted from CDC/NCHS FastStats, "Births and Natality"). FastStats cites them to *Births: Final Data for 2024* (National Vital Statistics Reports, vol. 75, no. 2, June 9, 2026), so the data year is 2024. cdc.gov refused connections from the build environment earlier on Oct 6 (HTTP 403) and answered later the same day, so the report itself was read (below).

| Measure | Value |
|---|---|
| Number of births | 3,628,934 |
| Birth rate | 10.7 per 1,000 population |
| General fertility rate | 53.8 births per 1,000 women aged 15-44 |
| Born low birthweight | 8.52% |
| Born preterm | 10.41% |
| Births to unmarried mothers | 39.5% |
| Mean age of the mother at first birth | 27.6 |

How v5.3 uses them: as checks on the model's births (the general fertility rate, the mean age at first birth, the share of births to unmarried mothers, which bears on single-parent households). Low birthweight and preterm births are not modelled.

## Births by the mother's age, 2024 (what the model draws from)

Source: Osterman, Hamilton, Martin, Driscoll and Valenzuela, *Births: Final Data for 2024*, National Vital Statistics Reports vol. 75 no. 2 (NCHS, June 9, 2026), Table 2, "Birth rates, by age of mother: United States, 2010-2024", row 2024, all races and origins. https://www.cdc.gov/nchs/data/nvsr/nvsr75/nvsr75-02.pdf (read Oct 6, 2026). Births per 1,000 women in the age group a year.

| Age of mother | 10-14 | 15-19 | 20-24 | 25-29 | 30-34 | 35-39 | 40-44 | 45-49 |
|---|---|---|---|---|---|---|---|---|
| Births per 1,000 women | 0.2 | 12.6 | 55.8 | 89.5 | 93.7 | 54.3 | 12.7 | 1.1 |

The total fertility rate, 1,599.5 per 1,000 women (the sum of the rates × 5), is in the same row. The 45-49 rate includes births to women 50 and over (the report's note 1).
