# Campbell, Giglio and Pathak, "Forced Sales and House Prices" (AER 101(5): 2108-2131, 2011)

File: `Campbell-Giglio-Pathak-forced-sales.pdf`, the author's open-access manuscript (version of July 2010, 34 pages) from Harvard DASH (https://dash.harvard.edu/entities/publication/73120378-a7ef-6bd4-e053-0100007fdf3b); the same manuscript is at MIT DSpace, http://hdl.handle.net/1721.1/61687. Published version: https://doi.org/10.1257/aer.101.5.2108. SHA-256 of the PDF: 6a6e557b74c8e3d28ed6704fdaca74c765865bcff4e43da2d3a4619ed9adc959.

## What S74 item 5 can take from it (section 3.1, Table 2, equation 1)
Data: every Massachusetts house transaction, 1987 to March 2009 (1,831,393 after cleaning); single-family, multi-family and condominiums. Forced sales are identified by a seller's death or bankruptcy near the sale, or a foreclosure. Method: hedonic regression of log price with census tract-by-year effects and house characteristics. The authors caution that the coefficients are not causal.

Coefficients on log price (all housing types, Table 2 panel B) and the implied discount, 1 - exp(coefficient):
| Forced sale type | Coefficient | Discount |
|---|---|---|
| Death of a seller under 70 | -0.053 | 5.2% |
| Death of a seller 70 or over | -0.069 | 6.7% |
| Bankruptcy-related | -0.035 | 3.4% |
| Foreclosure | -0.314 | 26.9% (the paper says 27%) |
| Any forced sale (panel A) | -0.197 | 18% |

One seller against two (panel C): death -0.083 / -0.097 (young / old) against -0.038 / -0.053; bankruptcy -0.064 against -0.017.

## How the paper reads them (so the engine does not over-read them)
- Death-related discounts look like poor maintenance by older sellers, not urgency (they do not depend on how soon after the death the sale happens, and rise with seller age).
- Bankruptcy-related discounts are the ones the authors read as closest to a true liquidity effect.
- Foreclosure discounts are tied to urgency and to vandalism or damage (larger for low-priced houses in low-priced neighbourhoods), so part of the 27% is lower house quality, not only a quick-sale price.
- Forced-sale prices are mean-reverting; unforced prices are close to a random walk.
