# S71: the creditor side, pilot tables

Seeds 1-100, 500 adults, 20 years. Engine commit `f7572fd`. Programme minus no programme on the same seeds; 95% intervals from 2,000 paired bootstrap replicates, unadjusted. Weighted measures. A pilot is a mechanism check, not a result.

Coefficients (sources/s71_creditors.py): `{"led": {"dHH": 0.2393, "bHH": 0.0845, "BUS": 0.3242, "GOV": 0.2556, "ROW": 0.0641, "dGOV": 0.0182, "dROW": 0.0141}, "own": {"eH": 0.7313, "eG": 0.071, "eR": 0.1977}, "w": {"wD": 0.6566, "wB": 0.6067, "wE": 0.6233}, "t": [0.3805, 0.392, 0.4977, 0.5883, 0.6648, 0.726, 0.6624], "tAll": 0.6753}`

## 1. The ledger: where a dollar of debt relief is lost (Year-0 dollars per adult, summed over the run; share of relief in brackets)

**Reference, no programme**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 0 | 0 | 0 | 0 | 0 | 0 |
| on the books already | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| new charge, nominal assets | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| new charge, shares | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| outside: government | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| outside: foreigners | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| outside: households not in the model | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| ledger gap | 0.0e+00 of relief at most | 0.0e+00 of relief at most | 0.0e+00 of relief at most | 0.0e+00 of relief at most | 0.0e+00 of relief at most | 0.0e+00 of relief at most |

**Reference, release**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 102,451 | 102,451 | 102,451 | 102,451 | 102,451 | 873,854 |
| on the books already | 11,529 (11.3%) | 11,529 (11.3%) | 11,529 (11.3%) | 17,914 (17.5%) | 27,608 (26.9%) | 98,336 (11.3%) |
| new charge, nominal assets | 2,416 (2.4%) | 9,821 (9.6%) | 2,416 (2.4%) | 3,982 (3.9%) | 6,145 (6.0%) | 20,608 (2.4%) |
| new charge, shares | 20,974 (20.5%) | 15,140 (14.8%) | 0 (0.0%) | 33,650 (32.8%) | 68,661 (67.0%) | 178,900 (20.5%) |
| outside: government | 30,460 (29.7%) | 30,409 (29.7%) | 27,193 (26.5%) | 30,460 (29.7%) | 0 (0.0%) | 259,811 (29.7%) |
| outside: foreigners | 16,444 (16.1%) | 14,578 (14.2%) | 7,347 (7.2%) | 16,444 (16.1%) | 0 (0.0%) | 140,261 (16.1%) |
| outside: households not in the model | 20,627 (20.1%) | 20,974 (20.5%) | 7,951 (7.8%) | 0 (0.0%) | 0 (0.0%) | 175,939 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 46,015 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 36 (0.0%) | 0 (0.0%) |
| ledger gap | 3.4e-15 of relief at most | 2.3e-15 of relief at most | 5.7e-16 of relief at most | 4.1e-15 of relief at most | 1.0e-14 of relief at most | 3.0e-15 of relief at most |

**Reference, C2.2**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 102,779 | 102,779 | 102,779 | 102,779 | 102,779 | 876,605 |
| on the books already | 11,566 (11.3%) | 11,566 (11.3%) | 11,566 (11.3%) | 17,971 (17.5%) | 27,681 (26.9%) | 98,645 (11.3%) |
| new charge, nominal assets | 2,424 (2.4%) | 9,852 (9.6%) | 2,424 (2.4%) | 3,995 (3.9%) | 6,165 (6.0%) | 20,672 (2.4%) |
| new charge, shares | 21,041 (20.5%) | 15,188 (14.8%) | 0 (0.0%) | 33,758 (32.8%) | 68,881 (67.0%) | 179,463 (20.5%) |
| outside: government | 30,558 (29.7%) | 30,507 (29.7%) | 27,280 (26.5%) | 30,558 (29.7%) | 0 (0.0%) | 260,629 (29.7%) |
| outside: foreigners | 16,497 (16.1%) | 14,625 (14.2%) | 7,371 (7.2%) | 16,497 (16.1%) | 0 (0.0%) | 140,702 (16.1%) |
| outside: households not in the model | 20,693 (20.1%) | 21,041 (20.5%) | 7,977 (7.8%) | 0 (0.0%) | 0 (0.0%) | 176,493 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 46,162 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 52 (0.1%) | 0 (0.0%) |
| ledger gap | 3.6e-15 of relief at most | 2.2e-15 of relief at most | 8.1e-16 of relief at most | 3.4e-15 of relief at most | 1.2e-14 of relief at most | 2.8e-15 of relief at most |

**Adverse, no programme**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 32,307 | 32,307 | 32,307 | 32,307 | 32,307 | 275,542 |
| on the books already | 3,635 (11.3%) | 3,635 (11.3%) | 3,635 (11.3%) | 5,649 (17.5%) | 8,706 (26.9%) | 31,007 (11.3%) |
| new charge, nominal assets | 762 (2.4%) | 3,097 (9.6%) | 762 (2.4%) | 1,256 (3.9%) | 1,938 (6.0%) | 6,498 (2.4%) |
| new charge, shares | 6,614 (20.5%) | 4,774 (14.8%) | 0 (0.0%) | 10,611 (32.8%) | 21,651 (67.0%) | 56,410 (20.5%) |
| outside: government | 9,605 (29.7%) | 9,589 (29.7%) | 8,575 (26.5%) | 9,605 (29.7%) | 0 (0.0%) | 81,923 (29.7%) |
| outside: foreigners | 5,185 (16.1%) | 4,597 (14.2%) | 2,317 (7.2%) | 5,185 (16.1%) | 0 (0.0%) | 44,227 (16.1%) |
| outside: households not in the model | 6,505 (20.1%) | 6,614 (20.5%) | 2,507 (7.8%) | 0 (0.0%) | 0 (0.0%) | 55,477 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 14,510 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 11 (0.0%) | 0 (0.0%) |
| ledger gap | 1.6e-15 of relief at most | 1.8e-15 of relief at most | 4.3e-16 of relief at most | 3.8e-15 of relief at most | 9.5e-15 of relief at most | 2.6e-15 of relief at most |

**Adverse, release**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 102,860 | 102,860 | 102,860 | 102,860 | 102,860 | 877,307 |
| on the books already | 11,575 (11.3%) | 11,575 (11.3%) | 11,575 (11.3%) | 17,985 (17.5%) | 27,714 (26.9%) | 98,724 (11.3%) |
| new charge, nominal assets | 2,426 (2.4%) | 9,860 (9.6%) | 2,426 (2.4%) | 3,998 (3.9%) | 6,170 (6.0%) | 20,689 (2.4%) |
| new charge, shares | 21,058 (20.5%) | 15,200 (14.8%) | 0 (0.0%) | 33,785 (32.8%) | 68,935 (67.0%) | 179,606 (20.5%) |
| outside: government | 30,582 (29.7%) | 30,531 (29.7%) | 27,302 (26.5%) | 30,582 (29.7%) | 0 (0.0%) | 260,838 (29.7%) |
| outside: foreigners | 16,510 (16.1%) | 14,636 (14.2%) | 7,377 (7.2%) | 16,510 (16.1%) | 0 (0.0%) | 140,815 (16.1%) |
| outside: households not in the model | 20,710 (20.1%) | 21,058 (20.5%) | 7,983 (7.8%) | 0 (0.0%) | 0 (0.0%) | 176,634 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 46,198 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 41 (0.0%) | 0 (0.0%) |
| ledger gap | 2.9e-15 of relief at most | 1.7e-15 of relief at most | 6.2e-16 of relief at most | 4.7e-15 of relief at most | 1.2e-14 of relief at most | 2.9e-15 of relief at most |

**Adverse, C2.2**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 102,957 | 102,957 | 102,957 | 102,957 | 102,957 | 878,122 |
| on the books already | 11,586 (11.3%) | 11,586 (11.3%) | 11,586 (11.3%) | 18,002 (17.5%) | 27,726 (26.9%) | 98,816 (11.3%) |
| new charge, nominal assets | 2,428 (2.4%) | 9,869 (9.6%) | 2,428 (2.4%) | 4,002 (3.9%) | 6,176 (6.0%) | 20,708 (2.4%) |
| new charge, shares | 21,078 (20.5%) | 15,215 (14.8%) | 0 (0.0%) | 33,817 (32.8%) | 69,000 (67.0%) | 179,773 (20.5%) |
| outside: government | 30,611 (29.7%) | 30,560 (29.7%) | 27,328 (26.5%) | 30,611 (29.7%) | 0 (0.0%) | 261,080 (29.7%) |
| outside: foreigners | 16,525 (16.1%) | 14,650 (14.2%) | 7,383 (7.2%) | 16,525 (16.1%) | 0 (0.0%) | 140,946 (16.1%) |
| outside: households not in the model | 20,729 (20.1%) | 21,077 (20.5%) | 7,990 (7.8%) | 0 (0.0%) | 0 (0.0%) | 176,798 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 46,242 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 56 (0.1%) | 0 (0.0%) |
| ledger gap | 3.7e-15 of relief at most | 2.6e-15 of relief at most | 6.7e-16 of relief at most | 4.2e-15 of relief at most | 9.9e-15 of relief at most | 3.5e-15 of relief at most |

**Stress, no programme**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 32,307 | 32,307 | 32,307 | 32,307 | 32,307 | 275,542 |
| on the books already | 3,635 (11.3%) | 3,635 (11.3%) | 3,635 (11.3%) | 5,649 (17.5%) | 8,706 (26.9%) | 31,007 (11.3%) |
| new charge, nominal assets | 762 (2.4%) | 3,097 (9.6%) | 762 (2.4%) | 1,256 (3.9%) | 1,938 (6.0%) | 6,498 (2.4%) |
| new charge, shares | 6,614 (20.5%) | 4,774 (14.8%) | 0 (0.0%) | 10,611 (32.8%) | 21,651 (67.0%) | 56,410 (20.5%) |
| outside: government | 9,605 (29.7%) | 9,589 (29.7%) | 8,575 (26.5%) | 9,605 (29.7%) | 0 (0.0%) | 81,923 (29.7%) |
| outside: foreigners | 5,185 (16.1%) | 4,597 (14.2%) | 2,317 (7.2%) | 5,185 (16.1%) | 0 (0.0%) | 44,227 (16.1%) |
| outside: households not in the model | 6,505 (20.1%) | 6,614 (20.5%) | 2,507 (7.8%) | 0 (0.0%) | 0 (0.0%) | 55,477 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 14,510 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 11 (0.0%) | 0 (0.0%) |
| ledger gap | 1.6e-15 of relief at most | 1.8e-15 of relief at most | 4.3e-16 of relief at most | 3.8e-15 of relief at most | 9.5e-15 of relief at most | 2.6e-15 of relief at most |

**Stress, release**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 99,034 | 99,034 | 99,034 | 99,034 | 99,033 | 844,888 |
| on the books already | 11,144 (11.3%) | 11,144 (11.3%) | 11,144 (11.3%) | 17,316 (17.5%) | 26,692 (27.0%) | 95,076 (11.3%) |
| new charge, nominal assets | 2,335 (2.4%) | 9,493 (9.6%) | 2,335 (2.4%) | 3,849 (3.9%) | 5,940 (6.0%) | 19,925 (2.4%) |
| new charge, shares | 20,275 (20.5%) | 14,635 (14.8%) | 0 (0.0%) | 32,528 (32.8%) | 66,370 (67.0%) | 172,970 (20.5%) |
| outside: government | 29,444 (29.7%) | 29,395 (29.7%) | 26,286 (26.5%) | 29,444 (29.7%) | 0 (0.0%) | 251,199 (29.7%) |
| outside: foreigners | 15,896 (16.1%) | 14,092 (14.2%) | 7,102 (7.2%) | 15,896 (16.1%) | 0 (0.0%) | 135,611 (16.1%) |
| outside: households not in the model | 19,939 (20.1%) | 20,274 (20.5%) | 7,686 (7.8%) | 0 (0.0%) | 0 (0.0%) | 170,107 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 44,480 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 30 (0.0%) | 0 (0.0%) |
| ledger gap | 3.1e-15 of relief at most | 2.6e-15 of relief at most | 7.3e-16 of relief at most | 4.1e-15 of relief at most | 7.9e-15 of relief at most | 2.7e-15 of relief at most |

**Stress, C2.2**

| | main: pass | holders of record | shareholders not charged | model = all households | nothing outside | unweighted totals |
|---|---|---|---|---|---|---|
| debt inflated away | 102,973 | 102,973 | 102,973 | 102,973 | 102,973 | 878,253 |
| on the books already | 11,588 (11.3%) | 11,588 (11.3%) | 11,588 (11.3%) | 18,005 (17.5%) | 27,730 (26.9%) | 98,831 (11.3%) |
| new charge, nominal assets | 2,428 (2.4%) | 9,871 (9.6%) | 2,428 (2.4%) | 4,003 (3.9%) | 6,177 (6.0%) | 20,711 (2.4%) |
| new charge, shares | 21,081 (20.5%) | 15,217 (14.8%) | 0 (0.0%) | 33,822 (32.8%) | 69,010 (67.0%) | 179,800 (20.5%) |
| outside: government | 30,615 (29.7%) | 30,564 (29.7%) | 27,332 (26.5%) | 30,615 (29.7%) | 0 (0.0%) | 261,119 (29.7%) |
| outside: foreigners | 16,528 (16.1%) | 14,652 (14.2%) | 7,385 (7.2%) | 16,528 (16.1%) | 0 (0.0%) | 140,967 (16.1%) |
| outside: households not in the model | 20,732 (20.1%) | 21,081 (20.5%) | 7,992 (7.8%) | 0 (0.0%) | 0 (0.0%) | 176,825 (20.1%) |
| outside: lenders' shareholders, not charged | 0 (0.0%) | 0 (0.0%) | 46,249 (44.9%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| unplaced | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 56 (0.1%) | 0 (0.0%) |
| ledger gap | 3.7e-15 of relief at most | 2.4e-15 of relief at most | 6.6e-16 of relief at most | 6.3e-15 of relief at most | 1.2e-14 of relief at most | 3.7e-15 of relief at most |

## 2. Who bears the new charges, and who gets the relief (Year-0 dollars per adult in each fifth of starting wealth, summed over the run; main creditor reading)

**Reference**

| | Poorest fifth | 2nd | 3rd | 4th | Richest fifth | Top 1%'s share of new charges |
|---|---|---|---|---|---|---|
| no programme: relief | 0 | 0 | 0 | 0 | 0 | |
| no programme: new charges | 0 | 0 | 0 | 0 | 0 | 0.0% |
| release: relief | 40,908 | 53,539 | 93,565 | 112,761 | 211,260 | |
| release: new charges | 578 | 1,135 | 3,149 | 9,657 | 102,280 | 26.3% |
| C2.2: relief | 41,039 | 53,710 | 93,864 | 113,121 | 211,937 | |
| C2.2: new charges | 623 | 1,177 | 3,188 | 9,702 | 102,483 | 26.3% |

**Adverse**

| | Poorest fifth | 2nd | 3rd | 4th | Richest fifth | Top 1%'s share of new charges |
|---|---|---|---|---|---|---|
| no programme: relief | 12,900 | 16,883 | 29,504 | 35,557 | 66,618 | |
| no programme: new charges | 160 | 331 | 959 | 3,013 | 32,369 | 26.5% |
| release: relief | 41,071 | 53,753 | 93,938 | 113,210 | 212,104 | |
| release: new charges | 562 | 1,106 | 3,122 | 9,659 | 102,816 | 26.4% |
| C2.2: relief | 41,110 | 53,804 | 94,026 | 113,317 | 212,305 | |
| C2.2: new charges | 607 | 1,151 | 3,162 | 9,690 | 102,766 | 26.3% |

**Stress**

| | Poorest fifth | 2nd | 3rd | 4th | Richest fifth | Top 1%'s share of new charges |
|---|---|---|---|---|---|---|
| no programme: relief | 12,900 | 16,883 | 29,504 | 35,557 | 66,618 | |
| no programme: new charges | 160 | 331 | 959 | 3,013 | 32,369 | 26.5% |
| release: relief | 39,539 | 51,754 | 90,446 | 108,998 | 204,215 | |
| release: new charges | 509 | 1,051 | 2,990 | 9,289 | 99,064 | 26.4% |
| C2.2: relief | 41,116 | 53,812 | 94,040 | 113,334 | 212,336 | |
| C2.2: new charges | 596 | 1,135 | 3,146 | 9,678 | 102,838 | 26.3% |

Top 1%'s share of new charges (by starting wealth), each reading, release design: Reference cr 26.3%, crhold 23.9%, crhedge 20.5%, crpop 26.3%, crall 26.4%, cru 26.1%; Adverse cr 26.4%, crhold 24.1%, crhedge 20.9%, crpop 26.3%, crall 26.5%, cru 26.2%; Stress cr 26.4%, crhold 24.4%, crhedge 21.4%, crpop 26.4%, crall 26.5%, cru 26.3%

## 3. The programme's effect under each reading

**Wealth poverty, year 20 (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -12.53 (-12.82 to -12.24) | -18.13 (-18.44 to -17.81) | -12.96 (-13.28 to -12.64) | -20.15 (-20.52 to -19.78) | -7.01 (-7.30 to -6.73) | -18.63 (-18.99 to -18.27) |
| no debt relief (bound 2) | -6.65 (-6.93 to -6.36) | -13.33 (-13.67 to -12.99) | -7.78 (-8.11 to -7.45) | -15.59 (-15.94 to -15.22) | -2.77 (-3.03 to -2.52) | -13.26 (-13.61 to -12.90) |
| creditor side, main: pass | -12.48 (-12.76 to -12.18) | -18.12 (-18.43 to -17.80) | -12.94 (-13.26 to -12.62) | -20.16 (-20.54 to -19.79) | -6.98 (-7.27 to -6.71) | -18.63 (-19.00 to -18.28) |
| creditor side, holders of record | -12.47 (-12.75 to -12.17) | -18.11 (-18.41 to -17.78) | -12.95 (-13.28 to -12.63) | -20.18 (-20.56 to -19.81) | -6.99 (-7.28 to -6.71) | -18.66 (-19.03 to -18.30) |
| creditor side, shareholders not charged | -12.53 (-12.82 to -12.24) | -18.13 (-18.44 to -17.81) | -12.97 (-13.28 to -12.65) | -20.15 (-20.53 to -19.78) | -7.00 (-7.30 to -6.73) | -18.63 (-18.99 to -18.27) |
| creditor side, model = all households | -12.46 (-12.74 to -12.16) | -18.10 (-18.41 to -17.78) | -12.94 (-13.27 to -12.62) | -20.18 (-20.57 to -19.82) | -6.98 (-7.27 to -6.71) | -18.66 (-19.04 to -18.31) |
| creditor side, nothing outside | -12.38 (-12.67 to -12.09) | -18.08 (-18.38 to -17.75) | -12.90 (-13.22 to -12.58) | -20.21 (-20.59 to -19.85) | -6.89 (-7.19 to -6.62) | -18.65 (-19.03 to -18.30) |
| creditor side, unweighted totals | -12.53 (-12.82 to -12.24) | -18.13 (-18.43 to -17.81) | -12.95 (-13.27 to -12.63) | -20.15 (-20.53 to -19.77) | -7.00 (-7.30 to -6.73) | -18.62 (-18.99 to -18.26) |
| no tail, no creditor side | -12.50 (-12.79 to -12.20) | -18.05 (-18.35 to -17.73) | -12.91 (-13.23 to -12.58) | -20.05 (-20.43 to -19.69) | -6.94 (-7.22 to -6.67) | -18.54 (-18.91 to -18.17) |
| no tail, creditor side | -12.43 (-12.73 to -12.12) | -18.02 (-18.32 to -17.70) | -12.89 (-13.20 to -12.57) | -20.09 (-20.46 to -19.73) | -6.92 (-7.19 to -6.66) | -18.56 (-18.93 to -18.20) |

**Top 0.1% share of wealth (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -0.47 (-0.51 to -0.42) | -0.73 (-0.79 to -0.67) | -0.46 (-0.50 to -0.41) | -0.71 (-0.77 to -0.65) | -0.37 (-0.40 to -0.33) | -0.61 (-0.66 to -0.56) |
| no debt relief (bound 2) | +0.61 (+0.54 to +0.67) | +0.33 (+0.28 to +0.37) | +0.38 (+0.34 to +0.43) | +0.11 (+0.08 to +0.14) | +0.38 (+0.34 to +0.42) | +0.23 (+0.19 to +0.27) |
| creditor side, main: pass | -0.38 (-0.43 to -0.34) | -0.65 (-0.71 to -0.59) | -0.38 (-0.43 to -0.34) | -0.65 (-0.71 to -0.59) | -0.30 (-0.34 to -0.27) | -0.54 (-0.60 to -0.49) |
| creditor side, holders of record | -0.40 (-0.45 to -0.35) | -0.67 (-0.73 to -0.61) | -0.41 (-0.45 to -0.37) | -0.67 (-0.73 to -0.62) | -0.31 (-0.35 to -0.28) | -0.57 (-0.62 to -0.52) |
| creditor side, shareholders not charged | -0.47 (-0.51 to -0.42) | -0.73 (-0.79 to -0.66) | -0.46 (-0.50 to -0.42) | -0.71 (-0.77 to -0.65) | -0.36 (-0.40 to -0.33) | -0.61 (-0.67 to -0.56) |
| creditor side, model = all households | -0.32 (-0.38 to -0.27) | -0.60 (-0.66 to -0.54) | -0.33 (-0.38 to -0.29) | -0.60 (-0.67 to -0.55) | -0.25 (-0.30 to -0.22) | -0.49 (-0.55 to -0.44) |
| creditor side, nothing outside | -0.15 (-0.23 to -0.08) | -0.44 (-0.53 to -0.37) | -0.17 (-0.24 to -0.11) | -0.46 (-0.54 to -0.40) | -0.12 (-0.17 to -0.07) | -0.34 (-0.41 to -0.28) |
| creditor side, unweighted totals | -0.45 (-0.50 to -0.41) | -0.71 (-0.77 to -0.65) | -0.44 (-0.49 to -0.40) | -0.70 (-0.76 to -0.64) | -0.35 (-0.39 to -0.32) | -0.60 (-0.65 to -0.55) |
| no tail, no creditor side | -0.11 (-0.13 to -0.10) | -0.18 (-0.19 to -0.17) | -0.11 (-0.12 to -0.10) | -0.18 (-0.19 to -0.16) | -0.09 (-0.10 to -0.08) | -0.15 (-0.16 to -0.14) |
| no tail, creditor side | -0.09 (-0.11 to -0.07) | -0.16 (-0.17 to -0.14) | -0.09 (-0.10 to -0.08) | -0.16 (-0.17 to -0.14) | -0.07 (-0.08 to -0.06) | -0.13 (-0.15 to -0.12) |

**Top 1% share of wealth (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -1.14 (-1.23 to -1.06) | -1.75 (-1.84 to -1.66) | -1.11 (-1.19 to -1.04) | -1.70 (-1.79 to -1.62) | -0.88 (-0.94 to -0.82) | -1.47 (-1.56 to -1.39) |
| no debt relief (bound 2) | +1.23 (+1.13 to +1.33) | +0.59 (+0.49 to +0.68) | +0.74 (+0.66 to +0.82) | +0.12 (+0.04 to +0.20) | +0.76 (+0.70 to +0.83) | +0.39 (+0.31 to +0.47) |
| creditor side, main: pass | -1.02 (-1.13 to -0.91) | -1.64 (-1.75 to -1.53) | -1.00 (-1.09 to -0.90) | -1.61 (-1.71 to -1.51) | -0.77 (-0.85 to -0.70) | -1.37 (-1.47 to -1.27) |
| creditor side, holders of record | -1.04 (-1.14 to -0.94) | -1.66 (-1.77 to -1.56) | -1.04 (-1.13 to -0.96) | -1.65 (-1.75 to -1.56) | -0.79 (-0.87 to -0.73) | -1.42 (-1.51 to -1.33) |
| creditor side, shareholders not charged | -1.14 (-1.23 to -1.06) | -1.74 (-1.84 to -1.65) | -1.11 (-1.19 to -1.04) | -1.71 (-1.79 to -1.62) | -0.87 (-0.94 to -0.82) | -1.48 (-1.56 to -1.40) |
| creditor side, model = all households | -0.93 (-1.06 to -0.81) | -1.57 (-1.70 to -1.44) | -0.92 (-1.03 to -0.82) | -1.55 (-1.66 to -1.44) | -0.70 (-0.79 to -0.62) | -1.30 (-1.41 to -1.19) |
| creditor side, nothing outside | -0.67 (-0.86 to -0.49) | -1.35 (-1.53 to -1.17) | -0.67 (-0.82 to -0.52) | -1.34 (-1.50 to -1.18) | -0.48 (-0.61 to -0.36) | -1.07 (-1.23 to -0.92) |
| creditor side, unweighted totals | -1.12 (-1.21 to -1.04) | -1.73 (-1.83 to -1.63) | -1.09 (-1.17 to -1.01) | -1.69 (-1.77 to -1.60) | -0.86 (-0.93 to -0.80) | -1.46 (-1.54 to -1.37) |
| no tail, no creditor side | -0.98 (-1.04 to -0.92) | -1.49 (-1.56 to -1.42) | -0.96 (-1.02 to -0.91) | -1.47 (-1.53 to -1.41) | -0.76 (-0.81 to -0.71) | -1.28 (-1.34 to -1.22) |
| no tail, creditor side | -0.86 (-0.95 to -0.78) | -1.39 (-1.48 to -1.30) | -0.85 (-0.93 to -0.78) | -1.38 (-1.46 to -1.31) | -0.66 (-0.72 to -0.60) | -1.18 (-1.26 to -1.10) |

**Top 10% share (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -3.28 (-3.41 to -3.15) | -4.56 (-4.72 to -4.41) | -3.14 (-3.26 to -3.01) | -4.39 (-4.54 to -4.23) | -2.38 (-2.47 to -2.29) | -3.95 (-4.09 to -3.80) |
| no debt relief (bound 2) | +0.81 (+0.74 to +0.89) | -0.54 (-0.64 to -0.44) | +0.04 (-0.04 to +0.12) | -1.25 (-1.36 to -1.15) | +0.42 (+0.37 to +0.48) | -0.74 (-0.83 to -0.64) |
| creditor side, main: pass | -3.63 (-3.79 to -3.46) | -4.96 (-5.15 to -4.77) | -3.40 (-3.54 to -3.24) | -4.71 (-4.88 to -4.52) | -2.58 (-2.69 to -2.46) | -4.25 (-4.41 to -4.07) |
| creditor side, holders of record | -3.50 (-3.66 to -3.35) | -4.83 (-5.01 to -4.65) | -3.34 (-3.48 to -3.19) | -4.64 (-4.81 to -4.46) | -2.51 (-2.61 to -2.39) | -4.19 (-4.35 to -4.01) |
| creditor side, shareholders not charged | -3.28 (-3.40 to -3.15) | -4.56 (-4.71 to -4.40) | -3.14 (-3.26 to -3.01) | -4.39 (-4.54 to -4.24) | -2.38 (-2.47 to -2.28) | -3.95 (-4.09 to -3.80) |
| creditor side, model = all households | -3.85 (-4.03 to -3.66) | -5.22 (-5.43 to -4.99) | -3.57 (-3.73 to -3.39) | -4.91 (-5.11 to -4.70) | -2.70 (-2.83 to -2.57) | -4.44 (-4.63 to -4.24) |
| creditor side, nothing outside | -4.50 (-4.76 to -4.24) | -5.98 (-6.27 to -5.68) | -4.07 (-4.29 to -3.83) | -5.51 (-5.77 to -5.24) | -3.08 (-3.26 to -2.90) | -5.01 (-5.27 to -4.75) |
| creditor side, unweighted totals | -3.34 (-3.47 to -3.20) | -4.63 (-4.79 to -4.47) | -3.18 (-3.30 to -3.05) | -4.45 (-4.60 to -4.28) | -2.41 (-2.51 to -2.32) | -4.00 (-4.14 to -3.84) |
| no tail, no creditor side | -3.65 (-3.72 to -3.58) | -5.03 (-5.10 to -4.96) | -3.52 (-3.60 to -3.45) | -4.89 (-4.97 to -4.81) | -2.68 (-2.73 to -2.62) | -4.41 (-4.48 to -4.33) |
| no tail, creditor side | -4.14 (-4.22 to -4.06) | -5.59 (-5.67 to -5.49) | -3.90 (-3.98 to -3.81) | -5.33 (-5.41 to -5.24) | -2.97 (-3.03 to -2.90) | -4.83 (-4.91 to -4.74) |

**Bottom 50% share (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | +2.61 (+2.50 to +2.71) | +3.68 (+3.53 to +3.81) | +2.45 (+2.34 to +2.54) | +3.47 (+3.33 to +3.61) | +1.61 (+1.54 to +1.68) | +3.16 (+3.03 to +3.29) |
| no debt relief (bound 2) | +0.76 (+0.71 to +0.82) | +1.82 (+1.73 to +1.92) | +1.03 (+0.96 to +1.08) | +1.99 (+1.89 to +2.08) | +0.44 (+0.40 to +0.47) | +1.66 (+1.58 to +1.74) |
| creditor side, main: pass | +2.77 (+2.65 to +2.89) | +3.89 (+3.72 to +4.04) | +2.58 (+2.46 to +2.68) | +3.65 (+3.49 to +3.79) | +1.69 (+1.62 to +1.77) | +3.33 (+3.18 to +3.46) |
| creditor side, holders of record | +2.71 (+2.59 to +2.82) | +3.82 (+3.66 to +3.96) | +2.54 (+2.43 to +2.64) | +3.60 (+3.45 to +3.75) | +1.66 (+1.58 to +1.73) | +3.28 (+3.15 to +3.42) |
| creditor side, shareholders not charged | +2.61 (+2.50 to +2.71) | +3.68 (+3.53 to +3.81) | +2.45 (+2.34 to +2.54) | +3.47 (+3.33 to +3.61) | +1.61 (+1.54 to +1.68) | +3.16 (+3.03 to +3.29) |
| creditor side, model = all households | +2.88 (+2.75 to +3.00) | +4.02 (+3.85 to +4.18) | +2.66 (+2.54 to +2.77) | +3.76 (+3.59 to +3.91) | +1.75 (+1.67 to +1.82) | +3.43 (+3.28 to +3.57) |
| creditor side, nothing outside | +3.21 (+3.05 to +3.35) | +4.43 (+4.23 to +4.63) | +2.92 (+2.78 to +3.05) | +4.10 (+3.91 to +4.28) | +1.91 (+1.82 to +2.00) | +3.75 (+3.58 to +3.92) |
| creditor side, unweighted totals | +2.64 (+2.52 to +2.74) | +3.71 (+3.56 to +3.85) | +2.47 (+2.36 to +2.57) | +3.50 (+3.36 to +3.64) | +1.62 (+1.55 to +1.69) | +3.19 (+3.06 to +3.32) |
| no tail, no creditor side | +3.07 (+3.00 to +3.14) | +4.31 (+4.22 to +4.39) | +2.91 (+2.84 to +2.97) | +4.11 (+4.02 to +4.19) | +1.91 (+1.86 to +1.97) | +3.75 (+3.67 to +3.83) |
| no tail, creditor side | +3.30 (+3.22 to +3.37) | +4.59 (+4.50 to +4.69) | +3.09 (+3.01 to +3.16) | +4.34 (+4.25 to +4.43) | +2.03 (+1.98 to +2.09) | +3.97 (+3.89 to +4.06) |

**Wealth Gini**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -0.043 (-0.044 to -0.041) | -0.061 (-0.063 to -0.059) | -0.039 (-0.041 to -0.038) | -0.057 (-0.059 to -0.055) | -0.027 (-0.028 to -0.026) | -0.052 (-0.053 to -0.050) |
| no debt relief (bound 2) | -0.004 (-0.005 to -0.004) | -0.022 (-0.024 to -0.021) | -0.010 (-0.011 to -0.009) | -0.026 (-0.028 to -0.025) | -0.002 (-0.003 to -0.002) | -0.020 (-0.022 to -0.019) |
| creditor side, main: pass | -0.046 (-0.048 to -0.044) | -0.065 (-0.067 to -0.062) | -0.042 (-0.044 to -0.040) | -0.060 (-0.062 to -0.058) | -0.029 (-0.030 to -0.028) | -0.055 (-0.057 to -0.052) |
| creditor side, holders of record | -0.045 (-0.047 to -0.043) | -0.064 (-0.066 to -0.061) | -0.041 (-0.043 to -0.040) | -0.059 (-0.062 to -0.057) | -0.028 (-0.029 to -0.027) | -0.054 (-0.056 to -0.052) |
| creditor side, shareholders not charged | -0.043 (-0.044 to -0.041) | -0.061 (-0.063 to -0.059) | -0.039 (-0.041 to -0.038) | -0.057 (-0.059 to -0.055) | -0.027 (-0.028 to -0.026) | -0.052 (-0.053 to -0.050) |
| creditor side, model = all households | -0.048 (-0.050 to -0.046) | -0.068 (-0.070 to -0.065) | -0.044 (-0.045 to -0.042) | -0.062 (-0.065 to -0.060) | -0.030 (-0.031 to -0.029) | -0.056 (-0.059 to -0.054) |
| creditor side, nothing outside | -0.054 (-0.057 to -0.052) | -0.075 (-0.079 to -0.072) | -0.049 (-0.051 to -0.046) | -0.069 (-0.072 to -0.066) | -0.033 (-0.035 to -0.032) | -0.062 (-0.065 to -0.060) |
| creditor side, unweighted totals | -0.043 (-0.045 to -0.042) | -0.062 (-0.064 to -0.059) | -0.040 (-0.041 to -0.038) | -0.058 (-0.060 to -0.055) | -0.028 (-0.029 to -0.026) | -0.052 (-0.054 to -0.050) |
| no tail, no creditor side | -0.049 (-0.050 to -0.048) | -0.070 (-0.071 to -0.069) | -0.046 (-0.047 to -0.045) | -0.066 (-0.067 to -0.065) | -0.032 (-0.032 to -0.031) | -0.060 (-0.061 to -0.059) |
| no tail, creditor side | -0.054 (-0.055 to -0.053) | -0.075 (-0.077 to -0.074) | -0.049 (-0.050 to -0.048) | -0.070 (-0.072 to -0.069) | -0.034 (-0.035 to -0.033) | -0.064 (-0.065 to -0.063) |

**Median real wealth (Year-0 dollars)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | +36021 (+33224 to +38815) | +58624 (+55690 to +61501) | +36964 (+33865 to +40036) | +57354 (+54323 to +60350) | +33434 (+30792 to +36058) | +48064 (+45005 to +51156) |
| no debt relief (bound 2) | -45985 (-48417 to -43460) | -25119 (-27660 to -22644) | -19708 (-22501 to -16924) | +516 (-2497 to +3501) | -22074 (-24182 to -19870) | -8484 (-11488 to -5503) |
| creditor side, main: pass | +31461 (+28602 to +34198) | +54128 (+51238 to +56989) | +33812 (+30702 to +36886) | +54027 (+51005 to +56973) | +30612 (+28051 to +33248) | +44565 (+41545 to +47611) |
| creditor side, holders of record | +32038 (+29166 to +34798) | +54917 (+52017 to +57778) | +35240 (+32189 to +38300) | +55655 (+52624 to +58619) | +30960 (+28395 to +33554) | +46227 (+43176 to +49240) |
| creditor side, shareholders not charged | +35880 (+33084 to +38673) | +58519 (+55591 to +61400) | +37044 (+33954 to +40112) | +57459 (+54438 to +60460) | +33350 (+30716 to +35967) | +48179 (+45131 to +51266) |
| creditor side, model = all households | +28742 (+25902 to +31516) | +51382 (+48427 to +54237) | +31903 (+28794 to +34961) | +52025 (+49005 to +54965) | +28785 (+26238 to +31334) | +42617 (+39556 to +45674) |
| creditor side, nothing outside | +21187 (+18286 to +24064) | +43779 (+40781 to +46627) | +26325 (+23367 to +29318) | +46319 (+43280 to +49285) | +23962 (+21438 to +26491) | +37077 (+34005 to +40168) |
| creditor side, unweighted totals | +35170 (+32345 to +37935) | +57795 (+54866 to +60665) | +36422 (+33342 to +39494) | +56770 (+53736 to +59738) | +32898 (+30288 to +35523) | +47427 (+44365 to +50512) |
| no tail, no creditor side | +36211 (+33501 to +39027) | +58924 (+55912 to +61808) | +37932 (+34961 to +40816) | +57418 (+54295 to +60391) | +33140 (+30626 to +35655) | +48574 (+45486 to +51540) |
| no tail, creditor side | +30880 (+28179 to +33702) | +53631 (+50642 to +56484) | +33956 (+31020 to +36873) | +53662 (+50476 to +56627) | +29885 (+27345 to +32394) | +44463 (+41371 to +47475) |

**Mean real wealth (Year-0 dollars)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -57726 (-62984 to -52608) | -37822 (-43342 to -32490) | -49312 (-53952 to -44774) | -29853 (-34657 to -25169) | -35888 (-39623 to -32306) | -39294 (-44097 to -34601) |
| no debt relief (bound 2) | -156757 (-162420 to -151410) | -139183 (-145119 to -133531) | -118485 (-123325 to -113723) | -101748 (-106806 to -96865) | -98625 (-102603 to -94893) | -110847 (-115926 to -105913) |
| creditor side, main: pass | -95960 (-101349 to -90746) | -77208 (-82854 to -71765) | -77342 (-82021 to -72713) | -58882 (-63703 to -54165) | -60268 (-64033 to -56613) | -68359 (-73217 to -63598) |
| creditor side, holders of record | -86540 (-91909 to -81369) | -67087 (-72700 to -61645) | -67994 (-72676 to -63453) | -48999 (-53849 to -44323) | -53839 (-57557 to -50167) | -58419 (-63252 to -53662) |
| creditor side, shareholders not charged | -58086 (-63348 to -52973) | -38071 (-43593 to -32739) | -48837 (-53476 to -44299) | -29306 (-34105 to -24621) | -35983 (-39705 to -32407) | -38733 (-43534 to -34043) |
| creditor side, model = all households | -119083 (-124540 to -113804) | -101022 (-106794 to -95464) | -94263 (-98993 to -89566) | -76403 (-81287 to -71634) | -75006 (-78797 to -71315) | -85900 (-90835 to -81112) |
| creditor side, nothing outside | -182624 (-188402 to -177131) | -166573 (-172663 to -160807) | -141420 (-146360 to -136678) | -125284 (-130470 to -120245) | -115625 (-119693 to -111763) | -134851 (-140080 to -129825) |
| creditor side, unweighted totals | -64879 (-70389 to -59472) | -45187 (-50981 to -39568) | -54524 (-59321 to -49787) | -35249 (-40142 to -30321) | -40447 (-44278 to -36696) | -44695 (-49642 to -39772) |
| no tail, no creditor side | -38207 (-40177 to -36322) | -17738 (-19826 to -15777) | -31722 (-33419 to -29969) | -11924 (-13643 to -10135) | -22212 (-23509 to -20903) | -21201 (-22926 to -19411) |
| no tail, creditor side | -75507 (-77482 to -73571) | -56165 (-58234 to -54187) | -59084 (-60785 to -57319) | -40262 (-41968 to -38474) | -45996 (-47291 to -44675) | -49574 (-51320 to -47771) |

**Real wealth: opening nominal position**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -14356 (-18361 to -10708) | -16990 (-21097 to -13222) | -27161 (-30540 to -24070) | -28738 (-32194 to -25589) | -12959 (-15831 to -10349) | -29082 (-32553 to -25919) |
| no debt relief (bound 2) | -116779 (-121107 to -112704) | -119760 (-124220 to -115597) | -97691 (-101320 to -94293) | -99382 (-103090 to -95929) | -79632 (-82773 to -76783) | -99737 (-103459 to -96275) |
| creditor side, main: pass | -14598 (-18606 to -10948) | -17156 (-21263 to -13387) | -26762 (-30139 to -23672) | -28290 (-31745 to -25141) | -12972 (-15848 to -10364) | -28626 (-32095 to -25463) |
| creditor side, holders of record | -15264 (-19282 to -11607) | -17604 (-21716 to -13833) | -25587 (-28959 to -22512) | -26977 (-30428 to -23829) | -12964 (-15828 to -10362) | -27291 (-30755 to -24129) |
| creditor side, shareholders not charged | -14598 (-18606 to -10948) | -17156 (-21263 to -13387) | -26762 (-30139 to -23672) | -28290 (-31745 to -25141) | -12972 (-15849 to -10364) | -28626 (-32095 to -25463) |
| creditor side, model = all households | -14754 (-18764 to -11103) | -17262 (-21370 to -13493) | -26503 (-29879 to -23416) | -28000 (-31453 to -24851) | -12979 (-15853 to -10373) | -28330 (-31798 to -25167) |
| creditor side, nothing outside | -14969 (-18981 to -11316) | -17409 (-21518 to -13639) | -26144 (-29520 to -23062) | -27599 (-31051 to -24449) | -12988 (-15857 to -10382) | -27922 (-31388 to -24759) |
| creditor side, unweighted totals | -14418 (-18427 to -10767) | -17035 (-21142 to -13266) | -27076 (-30454 to -23988) | -28642 (-32095 to -25497) | -12970 (-15844 to -10361) | -28984 (-32451 to -25825) |
| no tail, no creditor side | -368 (-1922 to +1079) | -2586 (-4185 to -1107) | -15101 (-16414 to -13902) | -16439 (-17771 to -15216) | -3288 (-4370 to -2314) | -16733 (-18069 to -15511) |
| no tail, creditor side | -599 (-2157 to +851) | -2744 (-4344 to -1264) | -14712 (-16025 to -13513) | -16003 (-17335 to -14780) | -3297 (-4380 to -2323) | -16290 (-17625 to -15068) |

**Real wealth: opening real assets**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) |
| no debt relief (bound 2) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) |
| creditor side, main: pass | -37678 (-37956 to -37400) | -38925 (-39212 to -38634) | -28387 (-28598 to -28180) | -29436 (-29652 to -29214) | -24175 (-24374 to -23979) | -29493 (-29710 to -29272) |
| creditor side, holders of record | -27197 (-27398 to -26997) | -28097 (-28305 to -27887) | -20491 (-20643 to -20341) | -21248 (-21404 to -21088) | -17450 (-17594 to -17308) | -21289 (-21445 to -21130) |
| creditor side, shareholders not charged | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) |
| creditor side, model = all households | -60449 (-60896 to -60003) | -62450 (-62911 to -61983) | -45544 (-45881 to -45211) | -47226 (-47573 to -46871) | -38786 (-39105 to -38470) | -47318 (-47665 to -46964) |
| creditor side, nothing outside | -123342 (-124252 to -122432) | -127424 (-128365 to -126472) | -92928 (-93617 to -92248) | -96362 (-97070 to -95636) | -79138 (-79789 to -78494) | -96549 (-97257 to -95825) |
| creditor side, unweighted totals | -7018 (-7394 to -6638) | -7250 (-7640 to -6857) | -5287 (-5570 to -5001) | -5483 (-5777 to -5186) | -4505 (-4746 to -4264) | -5493 (-5789 to -5196) |
| no tail, no creditor side | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) |
| no tail, creditor side | -36787 (-36987 to -36577) | -38004 (-38207 to -37790) | -27716 (-27867 to -27557) | -28740 (-28894 to -28578) | -23604 (-23760 to -23443) | -28796 (-28949 to -28635) |

**Real wealth: saving since**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -43370 (-45257 to -41669) | -20831 (-22844 to -18987) | -22151 (-23975 to -20447) | -1115 (-3046 to +669) | -22929 (-24190 to -21716) | -10212 (-12189 to -8398) |
| no debt relief (bound 2) | -39978 (-41873 to -38268) | -19423 (-21464 to -17604) | -20794 (-22638 to -19079) | -2366 (-4283 to -600) | -18993 (-20293 to -17808) | -11110 (-13054 to -9298) |
| creditor side, main: pass | -43684 (-45581 to -41978) | -21127 (-23146 to -19274) | -22194 (-24018 to -20488) | -1156 (-3085 to +630) | -23121 (-24385 to -21904) | -10239 (-12219 to -8424) |
| creditor side, holders of record | -44078 (-45975 to -42376) | -21385 (-23401 to -19536) | -21916 (-23730 to -20216) | -774 (-2698 to +1008) | -23425 (-24683 to -22210) | -9838 (-11810 to -8030) |
| creditor side, shareholders not charged | -43489 (-45376 to -41788) | -20915 (-22928 to -19070) | -22075 (-23897 to -20373) | -1015 (-2945 to +767) | -23011 (-24271 to -21798) | -10106 (-12084 to -8295) |
| creditor side, model = all households | -43880 (-45782 to -42171) | -21310 (-23333 to -19452) | -22216 (-24040 to -20510) | -1176 (-3105 to +609) | -23242 (-24507 to -22023) | -10252 (-12231 to -8436) |
| creditor side, nothing outside | -44313 (-46232 to -42595) | -21740 (-23774 to -19870) | -22348 (-24173 to -20636) | -1323 (-3251 to +462) | -23499 (-24770 to -22273) | -10380 (-12360 to -8560) |
| creditor side, unweighted totals | -43444 (-45335 to -41739) | -20901 (-22917 to -19052) | -22161 (-23985 to -20456) | -1124 (-3055 to +661) | -22973 (-24236 to -21758) | -10217 (-12196 to -8403) |
| no tail, no creditor side | -37839 (-38651 to -37049) | -15152 (-16002 to -14318) | -16622 (-17587 to -15680) | +4514 (+3568 to +5465) | -18924 (-19561 to -18330) | -4467 (-5438 to -3488) |
| no tail, creditor side | -38120 (-38934 to -37328) | -15418 (-16270 to -14579) | -16656 (-17620 to -15714) | +4481 (+3535 to +5429) | -19095 (-19734 to -18502) | -4488 (-5458 to -3510) |

**Income below the basket, year 20 (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -14.56 (-14.87 to -14.27) | -21.01 (-21.34 to -20.68) | -24.50 (-25.13 to -23.86) | -40.22 (-40.91 to -39.52) | -7.94 (-8.45 to -7.43) | -38.52 (-39.19 to -37.86) |
| no debt relief (bound 2) | -14.46 (-14.77 to -14.16) | -21.00 (-21.34 to -20.67) | -24.55 (-25.17 to -23.94) | -40.32 (-41.01 to -39.63) | -8.02 (-8.53 to -7.51) | -38.57 (-39.24 to -37.91) |
| creditor side, main: pass | -14.55 (-14.86 to -14.27) | -21.00 (-21.33 to -20.67) | -24.49 (-25.13 to -23.87) | -40.25 (-40.93 to -39.55) | -7.95 (-8.45 to -7.43) | -38.54 (-39.22 to -37.89) |
| creditor side, holders of record | -14.55 (-14.86 to -14.27) | -21.00 (-21.33 to -20.67) | -24.50 (-25.14 to -23.88) | -40.25 (-40.93 to -39.55) | -7.96 (-8.46 to -7.44) | -38.55 (-39.22 to -37.90) |
| creditor side, shareholders not charged | -14.56 (-14.87 to -14.27) | -21.01 (-21.34 to -20.68) | -24.50 (-25.13 to -23.86) | -40.22 (-40.91 to -39.52) | -7.94 (-8.45 to -7.43) | -38.53 (-39.20 to -37.87) |
| creditor side, model = all households | -14.55 (-14.86 to -14.26) | -21.00 (-21.33 to -20.67) | -24.47 (-25.10 to -23.86) | -40.25 (-40.93 to -39.55) | -7.93 (-8.43 to -7.42) | -38.54 (-39.21 to -37.89) |
| creditor side, nothing outside | -14.53 (-14.83 to -14.24) | -21.00 (-21.33 to -20.67) | -24.44 (-25.08 to -23.83) | -40.28 (-40.96 to -39.60) | -7.92 (-8.41 to -7.42) | -38.57 (-39.23 to -37.91) |
| creditor side, unweighted totals | -14.56 (-14.87 to -14.27) | -21.00 (-21.33 to -20.67) | -24.50 (-25.14 to -23.87) | -40.23 (-40.92 to -39.53) | -7.95 (-8.45 to -7.43) | -38.53 (-39.20 to -37.87) |
| no tail, no creditor side | -14.46 (-14.76 to -14.17) | -20.83 (-21.16 to -20.51) | -24.45 (-25.07 to -23.80) | -40.10 (-40.79 to -39.41) | -7.94 (-8.45 to -7.43) | -38.43 (-39.10 to -37.77) |
| no tail, creditor side | -14.45 (-14.74 to -14.16) | -20.83 (-21.16 to -20.51) | -24.42 (-25.04 to -23.78) | -40.12 (-40.81 to -39.42) | -7.92 (-8.43 to -7.41) | -38.44 (-39.11 to -37.77) |

**Below the cost of living, adult-years (points; unweighted)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | -15.85 (-16.16 to -15.56) | -23.17 (-23.49 to -22.87) | -21.22 (-21.60 to -20.80) | -32.85 (-33.30 to -32.38) | -8.19 (-8.46 to -7.91) | -32.23 (-32.66 to -31.76) |
| no debt relief (bound 2) | -15.80 (-16.11 to -15.50) | -23.16 (-23.48 to -22.85) | -21.27 (-21.65 to -20.85) | -32.89 (-33.34 to -32.42) | -8.22 (-8.49 to -7.94) | -32.26 (-32.70 to -31.79) |
| creditor side, main: pass | -15.85 (-16.15 to -15.55) | -23.17 (-23.49 to -22.86) | -21.22 (-21.60 to -20.80) | -32.86 (-33.30 to -32.39) | -8.18 (-8.45 to -7.90) | -32.23 (-32.67 to -31.76) |
| creditor side, holders of record | -15.85 (-16.15 to -15.55) | -23.17 (-23.49 to -22.86) | -21.22 (-21.60 to -20.80) | -32.86 (-33.30 to -32.39) | -8.18 (-8.46 to -7.90) | -32.23 (-32.67 to -31.76) |
| creditor side, shareholders not charged | -15.85 (-16.16 to -15.56) | -23.17 (-23.49 to -22.87) | -21.22 (-21.60 to -20.80) | -32.85 (-33.30 to -32.38) | -8.19 (-8.46 to -7.91) | -32.23 (-32.66 to -31.76) |
| creditor side, model = all households | -15.84 (-16.15 to -15.55) | -23.17 (-23.49 to -22.86) | -21.21 (-21.59 to -20.79) | -32.86 (-33.30 to -32.39) | -8.17 (-8.44 to -7.89) | -32.23 (-32.67 to -31.76) |
| creditor side, nothing outside | -15.83 (-16.14 to -15.54) | -23.17 (-23.49 to -22.86) | -21.20 (-21.57 to -20.78) | -32.86 (-33.31 to -32.40) | -8.15 (-8.42 to -7.87) | -32.24 (-32.68 to -31.77) |
| creditor side, unweighted totals | -15.85 (-16.16 to -15.56) | -23.17 (-23.49 to -22.87) | -21.22 (-21.60 to -20.80) | -32.85 (-33.30 to -32.38) | -8.19 (-8.46 to -7.91) | -32.23 (-32.66 to -31.76) |
| no tail, no creditor side | -16.03 (-16.33 to -15.73) | -23.51 (-23.83 to -23.20) | -21.43 (-21.82 to -21.00) | -33.27 (-33.73 to -32.80) | -8.28 (-8.56 to -7.99) | -32.61 (-33.06 to -32.14) |
| no tail, creditor side | -16.02 (-16.33 to -15.72) | -23.51 (-23.83 to -23.20) | -21.42 (-21.81 to -20.99) | -33.28 (-33.73 to -32.81) | -8.27 (-8.55 to -7.98) | -32.62 (-33.06 to -32.15) |

**Yearly inflation (points; unweighted)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| S59 main (bound 1) | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| no debt relief (bound 2) | +0.314 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.375 (+0.372 to +0.378) | +0.439 (+0.436 to +0.442) | +0.165 (+0.162 to +0.167) | +0.458 (+0.455 to +0.461) |
| creditor side, main: pass | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| creditor side, holders of record | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| creditor side, shareholders not charged | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| creditor side, model = all households | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| creditor side, nothing outside | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| creditor side, unweighted totals | +0.315 (+0.312 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| no tail, no creditor side | +0.315 (+0.313 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |
| no tail, creditor side | +0.315 (+0.313 to +0.317) | +0.374 (+0.372 to +0.376) | +0.376 (+0.373 to +0.379) | +0.440 (+0.437 to +0.443) | +0.165 (+0.162 to +0.167) | +0.459 (+0.455 to +0.462) |

## 4. What the creditor side changes: each creditor reading less S59's main reading (difference of paired effects)

**Wealth poverty, year 20 (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | +0.05 (+0.03 to +0.08) | +0.02 (+0.01 to +0.03) | +0.03 (-0.02 to +0.07) | -0.01 (-0.05 to +0.02) | +0.03 (-0.01 to +0.06) | -0.00 (-0.04 to +0.03) |
| holders of record | +0.06 (+0.04 to +0.09) | +0.03 (+0.01 to +0.05) | +0.01 (-0.04 to +0.06) | -0.03 (-0.08 to +0.01) | +0.02 (-0.03 to +0.06) | -0.03 (-0.08 to +0.01) |
| shareholders not charged | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.01 to +0.00) | -0.00 (-0.01 to +0.00) | +0.00 (-0.00 to +0.01) | +0.00 (-0.01 to +0.01) |
| model = all households | +0.08 (+0.05 to +0.11) | +0.03 (+0.02 to +0.05) | +0.02 (-0.03 to +0.07) | -0.03 (-0.09 to +0.02) | +0.03 (-0.02 to +0.08) | -0.04 (-0.09 to +0.01) |
| nothing outside | +0.16 (+0.12 to +0.19) | +0.06 (+0.04 to +0.08) | +0.07 (-0.01 to +0.13) | -0.06 (-0.13 to +0.01) | +0.11 (+0.04 to +0.18) | -0.03 (-0.10 to +0.05) |
| unweighted totals | +0.00 (+0.00 to +0.01) | +0.00 (+0.00 to +0.01) | +0.01 (-0.00 to +0.03) | -0.00 (-0.01 to +0.00) | +0.00 (-0.01 to +0.01) | +0.01 (-0.00 to +0.02) |
| no debt relief (for scale) | +5.88 (+5.67 to +6.10) | +4.80 (+4.62 to +4.99) | +5.18 (+4.89 to +5.46) | +4.56 (+4.29 to +4.83) | +4.23 (+3.97 to +4.51) | +5.37 (+5.11 to +5.64) |
| without the tail (r2cr less r2) | +0.07 (+0.04 to +0.10) | +0.02 (+0.01 to +0.04) | +0.01 (-0.03 to +0.06) | -0.03 (-0.07 to +0.01) | +0.01 (-0.03 to +0.06) | -0.02 (-0.06 to +0.02) |

**Top 0.1% share of wealth (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | +0.09 (+0.07 to +0.10) | +0.08 (+0.06 to +0.09) | +0.08 (+0.06 to +0.09) | +0.07 (+0.05 to +0.08) | +0.07 (+0.06 to +0.08) | +0.07 (+0.06 to +0.08) |
| holders of record | +0.07 (+0.06 to +0.08) | +0.06 (+0.05 to +0.07) | +0.05 (+0.04 to +0.06) | +0.04 (+0.03 to +0.05) | +0.05 (+0.04 to +0.06) | +0.04 (+0.03 to +0.05) |
| shareholders not charged | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.00 to -0.00) |
| model = all households | +0.14 (+0.12 to +0.17) | +0.13 (+0.10 to +0.16) | +0.13 (+0.10 to +0.15) | +0.11 (+0.09 to +0.13) | +0.11 (+0.09 to +0.13) | +0.12 (+0.10 to +0.14) |
| nothing outside | +0.32 (+0.26 to +0.38) | +0.28 (+0.23 to +0.34) | +0.29 (+0.24 to +0.34) | +0.25 (+0.20 to +0.30) | +0.25 (+0.21 to +0.29) | +0.27 (+0.22 to +0.32) |
| unweighted totals | +0.02 (+0.01 to +0.02) | +0.01 (+0.01 to +0.02) | +0.01 (+0.01 to +0.02) | +0.01 (+0.01 to +0.01) | +0.01 (+0.01 to +0.01) | +0.01 (+0.01 to +0.01) |
| no debt relief (for scale) | +1.07 (+0.99 to +1.16) | +1.05 (+0.97 to +1.13) | +0.84 (+0.77 to +0.90) | +0.82 (+0.76 to +0.89) | +0.75 (+0.69 to +0.80) | +0.84 (+0.77 to +0.91) |
| without the tail (r2cr less r2) | +0.03 (+0.02 to +0.03) | +0.02 (+0.02 to +0.03) | +0.02 (+0.02 to +0.03) | +0.02 (+0.01 to +0.02) | +0.02 (+0.01 to +0.02) | +0.02 (+0.02 to +0.03) |

**Top 1% share of wealth (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | +0.13 (+0.09 to +0.16) | +0.11 (+0.07 to +0.14) | +0.11 (+0.08 to +0.14) | +0.09 (+0.06 to +0.12) | +0.10 (+0.08 to +0.12) | +0.10 (+0.07 to +0.13) |
| holders of record | +0.11 (+0.08 to +0.13) | +0.09 (+0.06 to +0.11) | +0.07 (+0.05 to +0.08) | +0.05 (+0.03 to +0.07) | +0.08 (+0.06 to +0.10) | +0.05 (+0.04 to +0.07) |
| shareholders not charged | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.00 to -0.00) |
| model = all households | +0.21 (+0.16 to +0.26) | +0.18 (+0.12 to +0.23) | +0.19 (+0.14 to +0.23) | +0.15 (+0.11 to +0.20) | +0.17 (+0.13 to +0.21) | +0.17 (+0.12 to +0.21) |
| nothing outside | +0.47 (+0.35 to +0.59) | +0.40 (+0.28 to +0.51) | +0.44 (+0.34 to +0.53) | +0.36 (+0.26 to +0.46) | +0.39 (+0.31 to +0.47) | +0.40 (+0.30 to +0.50) |
| unweighted totals | +0.02 (+0.02 to +0.03) | +0.02 (+0.01 to +0.03) | +0.02 (+0.01 to +0.02) | +0.02 (+0.01 to +0.02) | +0.02 (+0.01 to +0.02) | +0.02 (+0.01 to +0.02) |
| no debt relief (for scale) | +2.38 (+2.30 to +2.45) | +2.34 (+2.25 to +2.41) | +1.85 (+1.78 to +1.91) | +1.82 (+1.76 to +1.88) | +1.64 (+1.58 to +1.69) | +1.86 (+1.80 to +1.92) |
| without the tail (r2cr less r2) | +0.12 (+0.08 to +0.15) | +0.10 (+0.06 to +0.13) | +0.11 (+0.08 to +0.14) | +0.09 (+0.06 to +0.11) | +0.10 (+0.07 to +0.12) | +0.10 (+0.07 to +0.13) |

**Top 10% share (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | -0.35 (-0.39 to -0.31) | -0.40 (-0.44 to -0.36) | -0.26 (-0.29 to -0.23) | -0.31 (-0.35 to -0.28) | -0.20 (-0.22 to -0.17) | -0.30 (-0.33 to -0.27) |
| holders of record | -0.22 (-0.25 to -0.20) | -0.27 (-0.30 to -0.24) | -0.20 (-0.23 to -0.18) | -0.25 (-0.27 to -0.22) | -0.13 (-0.14 to -0.11) | -0.24 (-0.26 to -0.21) |
| shareholders not charged | +0.00 (+0.00 to +0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | +0.00 (+0.00 to +0.00) | -0.00 (-0.00 to -0.00) |
| model = all households | -0.57 (-0.63 to -0.50) | -0.66 (-0.72 to -0.59) | -0.43 (-0.48 to -0.38) | -0.51 (-0.57 to -0.46) | -0.32 (-0.36 to -0.28) | -0.49 (-0.55 to -0.44) |
| nothing outside | -1.22 (-1.36 to -1.08) | -1.41 (-1.56 to -1.26) | -0.93 (-1.05 to -0.82) | -1.11 (-1.24 to -0.99) | -0.70 (-0.79 to -0.61) | -1.07 (-1.19 to -0.94) |
| unweighted totals | -0.06 (-0.07 to -0.05) | -0.07 (-0.08 to -0.06) | -0.05 (-0.05 to -0.04) | -0.05 (-0.06 to -0.05) | -0.03 (-0.04 to -0.03) | -0.05 (-0.06 to -0.05) |
| no debt relief (for scale) | +4.09 (+4.00 to +4.18) | +4.02 (+3.94 to +4.10) | +3.17 (+3.09 to +3.24) | +3.14 (+3.07 to +3.20) | +2.80 (+2.73 to +2.87) | +3.21 (+3.14 to +3.27) |
| without the tail (r2cr less r2) | -0.49 (-0.52 to -0.47) | -0.56 (-0.58 to -0.53) | -0.37 (-0.39 to -0.35) | -0.44 (-0.46 to -0.42) | -0.29 (-0.30 to -0.27) | -0.42 (-0.44 to -0.40) |

**Bottom 50% share (points)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | +0.17 (+0.15 to +0.18) | +0.21 (+0.19 to +0.23) | +0.13 (+0.12 to +0.14) | +0.17 (+0.16 to +0.18) | +0.08 (+0.08 to +0.09) | +0.16 (+0.15 to +0.17) |
| holders of record | +0.10 (+0.10 to +0.11) | +0.14 (+0.13 to +0.15) | +0.09 (+0.09 to +0.10) | +0.13 (+0.12 to +0.14) | +0.05 (+0.04 to +0.05) | +0.12 (+0.11 to +0.13) |
| shareholders not charged | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) | -0.00 (-0.00 to -0.00) |
| model = all households | +0.27 (+0.25 to +0.30) | +0.35 (+0.32 to +0.37) | +0.21 (+0.20 to +0.23) | +0.28 (+0.26 to +0.30) | +0.14 (+0.13 to +0.15) | +0.27 (+0.25 to +0.29) |
| nothing outside | +0.60 (+0.55 to +0.65) | +0.76 (+0.70 to +0.82) | +0.47 (+0.44 to +0.51) | +0.62 (+0.58 to +0.67) | +0.30 (+0.28 to +0.33) | +0.59 (+0.54 to +0.64) |
| unweighted totals | +0.03 (+0.03 to +0.03) | +0.04 (+0.03 to +0.04) | +0.02 (+0.02 to +0.02) | +0.03 (+0.03 to +0.03) | +0.01 (+0.01 to +0.02) | +0.03 (+0.03 to +0.03) |
| no debt relief (for scale) | -1.85 (-1.90 to -1.78) | -1.85 (-1.91 to -1.79) | -1.42 (-1.47 to -1.37) | -1.48 (-1.53 to -1.43) | -1.17 (-1.22 to -1.13) | -1.50 (-1.55 to -1.45) |
| without the tail (r2cr less r2) | +0.23 (+0.22 to +0.24) | +0.29 (+0.28 to +0.30) | +0.18 (+0.17 to +0.19) | +0.24 (+0.23 to +0.24) | +0.12 (+0.11 to +0.12) | +0.22 (+0.21 to +0.23) |

**Wealth Gini**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | -0.003 (-0.004 to -0.003) | -0.004 (-0.004 to -0.004) | -0.002 (-0.003 to -0.002) | -0.003 (-0.003 to -0.003) | -0.002 (-0.002 to -0.002) | -0.003 (-0.003 to -0.003) |
| holders of record | -0.002 (-0.002 to -0.002) | -0.003 (-0.003 to -0.002) | -0.002 (-0.002 to -0.002) | -0.002 (-0.003 to -0.002) | -0.001 (-0.001 to -0.001) | -0.002 (-0.003 to -0.002) |
| shareholders not charged | +0.000 (+0.000 to +0.000) | +0.000 (+0.000 to +0.000) | -0.000 (-0.000 to -0.000) | -0.000 (-0.000 to -0.000) | +0.000 (+0.000 to +0.000) | -0.000 (-0.000 to -0.000) |
| model = all households | -0.005 (-0.006 to -0.005) | -0.007 (-0.007 to -0.006) | -0.004 (-0.005 to -0.004) | -0.005 (-0.006 to -0.005) | -0.003 (-0.003 to -0.003) | -0.005 (-0.005 to -0.005) |
| nothing outside | -0.012 (-0.013 to -0.011) | -0.014 (-0.016 to -0.013) | -0.009 (-0.010 to -0.008) | -0.012 (-0.013 to -0.011) | -0.006 (-0.007 to -0.006) | -0.011 (-0.012 to -0.010) |
| unweighted totals | -0.001 (-0.001 to -0.001) | -0.001 (-0.001 to -0.001) | -0.000 (-0.000 to -0.000) | -0.001 (-0.001 to -0.000) | -0.000 (-0.000 to -0.000) | -0.001 (-0.001 to -0.000) |
| no debt relief (for scale) | +0.038 (+0.037 to +0.039) | +0.039 (+0.038 to +0.040) | +0.030 (+0.029 to +0.030) | +0.031 (+0.030 to +0.031) | +0.025 (+0.024 to +0.026) | +0.031 (+0.030 to +0.032) |
| without the tail (r2cr less r2) | -0.005 (-0.005 to -0.004) | -0.006 (-0.006 to -0.005) | -0.004 (-0.004 to -0.003) | -0.004 (-0.005 to -0.004) | -0.003 (-0.003 to -0.002) | -0.004 (-0.004 to -0.004) |

**Median real wealth (Year-0 dollars)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | -4559 (-4832 to -4287) | -4496 (-4772 to -4241) | -3152 (-3433 to -2888) | -3328 (-3644 to -3019) | -2822 (-3089 to -2584) | -3499 (-3798 to -3215) |
| holders of record | -3982 (-4190 to -3790) | -3707 (-3905 to -3513) | -1724 (-1916 to -1536) | -1699 (-1901 to -1505) | -2474 (-2677 to -2289) | -1837 (-2048 to -1638) |
| shareholders not charged | -141 (-152 to -130) | -104 (-111 to -98) | +80 (+63 to +97) | +105 (+89 to +122) | -84 (-114 to -55) | +115 (+98 to +131) |
| model = all households | -7279 (-7699 to -6859) | -7242 (-7670 to -6843) | -5061 (-5471 to -4650) | -5329 (-5812 to -4869) | -4649 (-5030 to -4282) | -5447 (-5911 to -5020) |
| nothing outside | -14834 (-15599 to -14067) | -14844 (-15696 to -14033) | -10639 (-11403 to -9876) | -11035 (-11841 to -10244) | -9472 (-10167 to -8795) | -10987 (-11750 to -10262) |
| unweighted totals | -850 (-908 to -793) | -829 (-889 to -772) | -542 (-598 to -489) | -584 (-646 to -528) | -535 (-590 to -482) | -637 (-698 to -578) |
| no debt relief (for scale) | -82006 (-83636 to -80334) | -83743 (-85558 to -81822) | -56672 (-58471 to -54827) | -56838 (-58502 to -55115) | -55507 (-57231 to -53808) | -56548 (-58295 to -54803) |
| without the tail (r2cr less r2) | -5331 (-5635 to -5038) | -5293 (-5622 to -4991) | -3976 (-4283 to -3678) | -3756 (-4048 to -3458) | -3255 (-3512 to -3005) | -4111 (-4397 to -3842) |

**Mean real wealth (Year-0 dollars)**

| Reading | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| main: pass | -38234 (-38518 to -37949) | -39386 (-39677 to -39091) | -28031 (-28238 to -27825) | -29029 (-29243 to -28812) | -24380 (-24577 to -24183) | -29065 (-29278 to -28848) |
| holders of record | -28814 (-29031 to -28598) | -29265 (-29484 to -29047) | -18682 (-18821 to -18545) | -19146 (-19288 to -19006) | -17951 (-18085 to -17816) | -19125 (-19266 to -18985) |
| shareholders not charged | -361 (-367 to -355) | -249 (-253 to -245) | +475 (+470 to +480) | +547 (+543 to +552) | -95 (-107 to -83) | +561 (+557 to +566) |
| model = all households | -61357 (-61813 to -60899) | -63201 (-63668 to -62727) | -44951 (-45284 to -44621) | -46550 (-46893 to -46202) | -39118 (-39433 to -38803) | -46606 (-46948 to -46259) |
| nothing outside | -124898 (-125825 to -123966) | -128752 (-129704 to -127785) | -92108 (-92793 to -91433) | -95431 (-96135 to -94716) | -79737 (-80389 to -79087) | -95557 (-96257 to -94843) |
| unweighted totals | -7154 (-7537 to -6767) | -7365 (-7761 to -6967) | -5212 (-5491 to -4929) | -5396 (-5687 to -5103) | -4559 (-4803 to -4316) | -5401 (-5691 to -5107) |
| no debt relief (for scale) | -99031 (-99781 to -98296) | -101361 (-102132 to -100612) | -69173 (-69683 to -68665) | -71895 (-72434 to -71364) | -62737 (-63230 to -62257) | -71553 (-72088 to -71022) |
| without the tail (r2cr less r2) | -37299 (-37502 to -37089) | -38426 (-38632 to -38213) | -27362 (-27511 to -27206) | -28338 (-28489 to -28180) | -23783 (-23931 to -23627) | -28373 (-28524 to -28216) |

## 5. Preregistered rules

**Rule 1 (checks).** Largest ledger gap in any seed of any row: 1.2e-14 of the relief (limit 1e-6): pass. Largest unplaced share of relief (row means): 0.0541% (limit 5%): pass.

**Check: the rows without the creditor side equal S59's per-seed files** (main, chi1, r2; every key S59 kept; 3186 series): identical.

**Rule 2 (direction of the effect on the top 1% share).** Established for a design only if the effect has one sign with a 95% interval excluding zero in all five creditor readings in all three environments.

- release: established: the programme lowers the top 1% share in every creditor reading and environment.
- C2.2: established: the programme lowers the top 1% share in every creditor reading and environment.

**Rule 3 (bounds).** Does each creditor reading's effect lie between S59's two readings (means)? Cells list the readings outside.

| Outcome | Reference, release | Reference, C2.2 | Adverse, release | Adverse, C2.2 | Stress, release | Stress, C2.2 |
|---|---|---|---|---|---|---|
| Wealth poverty, year 20 (points) | all inside | all inside | crhedge (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | all inside | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) |
| Top 0.1% share of wealth (points) | all inside | all inside | crhedge (beyond S59 main) | crhedge (beyond S59 main) | all inside | crhedge (beyond S59 main) |
| Top 1% share of wealth (points) | all inside | all inside | crhedge (beyond S59 main) | crhedge (beyond S59 main) | all inside | crhedge (beyond S59 main) |
| Top 10% share (points) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) |
| Bottom 50% share (points) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) |
| Wealth Gini | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) | cr (beyond S59 main), crhold (beyond S59 main), crhedge (beyond S59 main), crpop (beyond S59 main), crall (beyond S59 main) |
| Median real wealth (Year-0 dollars) | all inside | all inside | crhedge (beyond S59 main) | crhedge (beyond S59 main) | all inside | crhedge (beyond S59 main) |
| Mean real wealth (Year-0 dollars) | crall (beyond no debt relief) | crall (beyond no debt relief) | crhedge (beyond S59 main), crall (beyond no debt relief) | crhedge (beyond S59 main), crall (beyond no debt relief) | crall (beyond no debt relief) | crhedge (beyond S59 main), crall (beyond no debt relief) |

