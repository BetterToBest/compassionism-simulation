# The reference keys: which to compare first, and what they measure

Each reference file holds, for each run (`rows[0]` no programme, `rows[1]` the release row), `seeds[key]`: a list of 500 values, seeds 1 to 500 in order, unrounded, exactly as the engine's study function (`tbStudy`) keeps them. There are 631 keys. Definitions are in `MODEL_SPEC.md` section 9; the code that computes each is the result object `tbRunCore` returns at its end (`code/release-row-code.js`). Keys for years past the run (`_20` to `_39` in these 20-year runs) are 0 by construction: never read a 0 there as a value.

## 1. The starting population (year 0; checks the draws before any rule acts)

| Key | Meaning |
|---|---|
| `y0F0` | % of adults below the cost of living in year 0 |
| `y0Pov` | % of adults with too little wealth in year 0 |
| `y0BO`, `y0BN` | % of adults below 30 days of basic living in year 0 (BLEI paper's reading, design-neutral) |
| `y0Fpl` | % of adults below the official poverty line in year 0 |
| `y0GiniW` | Gini of wealth (debts as zero) in year 0, × n/(n − 1) |
| `y0Ep` | % of people unhoused in year 0 (the extreme-poverty overlay) |

## 2. The headline measures

| Key | Meaning |
|---|---|
| `fgt0PY` | % of adult-years below the cost of living (basket poverty) |
| `fgt2PY` | poverty severity: mean squared shortfall of cash income below own cost, as a share of it, × 100 |
| `pov` | % of adults with too little wealth at the last year |
| `bOAPy`, `bNAPy` | % of adult-years below 30 days of basic living (the BLEI paper's reading; design-neutral) |
| `medWealthReal` | median wealth at the last year, year-0 dollars |
| `giniD`, `giniX` | Gini of disposable income, and of income plus in-kind cuts, at the last year |
| `epPY` | % of person-years unhoused |
| `cost` | programme cost per adult-year, year-0 dollars (0 with no programme) |
| `tauMean` | the flat contribution's mean rate (share of earnings; 0 with no programme) |
| `endoAnn`, `pLev20` | programme inflation a year; the price level at the last year |
| `hrs` | change in hours from the labour response (share) |
| `jnP19` | % of adults taking part in year 19 |
| `emUrate` | % of adult-years out of work (weeks out / 52) |
| `snAll` | today's safety net, dollars per adult-year (year-0 dollars) |

## 3. Year by year (t = 0 to 19)

`plv_t` price level, `ppov_t` % with too little wealth, `pmedW_t` median wealth (year-0 $), `pwageR_t` the real wage (year-0 dollars a month; the code says which statistic). The snapshot families `y7…` (Year 7) and `e…` (the last year) repeat section 1's measures at those years.

## 4. Everything else

Every other key is a part's own report (project hiring `pj…`, ESP payroll `es…`, the surplus split `sp…`, the production side `pd…`, the Source's ledger `src…`, joining `jn…`, job loss `em…`, PTH's books `pb…`, PTF by sector `pf…`, the safety net `sn…`, households `hh…`, BLEI by reading and group `b…`, risk `rk…`). Compare them once the headline matches; a part's key that disagrees while the headline agrees still marks a difference worth reporting.
