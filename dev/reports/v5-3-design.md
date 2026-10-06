# v5.3 design note: households and children (written before any code or run)

Oct 6, 2026 · Claude · plan item B0 (`dev/plans/v5.3-plan-prompt.md`) · no code, no runs

This note comes first so that the design is fixed, and the expected results written down, before the model is built or run. Each design point gives the Research Hub's own words (with the page), then **Claude's reading of the design**, then what the model will do. Where the Hub is silent, it says so and names the question for Duke in plain words. Section 3 lists the predictions; the v5.3 report will say which held.

## 1. What the Hub says, and what the model will do

### 1.1 Who receives Basic Units, and how many a child gets

- **The Hub's words.** *Integrated Implementation Roadmap*, Appendix A (the American Economic Renaissance Act), Section 102: "Every citizen and legal resident 18 years or older shall receive 1,200 basic units monthly". *BLEI paper*, section 1: "Basic Units (BU) are allocated monthly at approximately $1,200 per adult". *BLEI paper*, Table 4, Profile B (a median family of four, two adults): "BU allocation (2 adults, EPPM effective) ... $5,004/mo", that is, two adults' allowances and none for the two children. *Risk Mitigation Framework*, section 3.5 (child protection in financially abusive households): "Youth CCO Accounts: Independent financial resources for older children".
- **Duke's answer on the dashboard (Oct 6, decision d167):** a child receives a quarter of the adult allowance ($300 a month at the reference), the same at every age; labelled a design choice and tested from none to half.
- **Claude's reading.** The Hub's written design gives the allowance to adults only; Duke's Oct 6 answer adds a small child allowance, which is the more recent statement of intent, so the model follows it. The Hub's text corresponds to the low end of the sweep (none), which will be shown beside it. "Youth CCO Accounts" read as a safeguard for older children in abusive households, not as an allowance size; abuse is not modelled, so neither are these accounts.
- **What the model does.** Child allowance = s × the adult BU, with s = 0.25 (main reading of the household model), swept over 0, 0.25 and 0.5 (`CHILD_BU_SHARE`, a design parameter). The allowance is indexed like the adult BU and, under pooling (1.4), joins the household's BU budget.
- **Question for Duke (design intent).** The Roadmap's draft Act says 18 or older; on Oct 6 you chose a quarter for children. Should the Act's text change to include the child allowance, or is it a later addition you would like shown as an option? Until you answer, the model uses your Oct 6 choice and shows "no child allowance" beside it.

### 1.2 What Basic Units can buy (childcare and schooling included)

- **The Hub's words.** Glossary, "Basic Units": "restricted to essential expenditures — housing, food, healthcare, education, and transportation", with the example "She uses them to pay rent at PTH housing, buy groceries at a PTF grocer, and cover her transit pass." Act, Section 103: "Permitted: Housing, Food, Transportation (non-luxury), Healthcare, Education, PTF services". Glossary, "Public Trust Foundations": "PTF businesses — grocers, counter-service restaurants, utility providers, transportation services, childcare centers, healthcare ...". *Research Summary*: PTF "provides foundational goods — grocers, utilities, childcare".
- **What the model does today.** Since session 2 (decision N10) BU buy food, housing (with utilities) and medical care only: 43.5% of the basket. Transportation (19.6% of the basket) and education are not BU purchases.
- **Claude's reading.** The Hub is explicit: BU may buy transportation and education too, and childcare is a PTF service, so it is a BU purchase at PTF providers and PTF members' childcare gets the PTF price cut. The present essentials set is narrower than the design. This is a finding about the current model, not only about households.
- **What the model will do.** Childcare and schooling costs enter as their own basket components for households with children (1.3). A switch `BU_SCOPE` with values 'core' (food, housing, medical: today, bit-identical) and 'hub' (adds transportation, education and childcare) is added; 'hub' first appears as a labelled reading, and whether it joins the main result is decided at the v5.3 restudy with everything else. The price module's essentials (which BU demand moves) follow the same set under each value.

### 1.3 Households, their costs and childcare

- **The Hub's words.** *BLEI paper*, section 9: "Demographic heterogeneity — multi-adult households, families with children, older adults, disability status — is partially addressed through the three household profiles but warrants systematic mapping from household size and composition to BLEI tiers." Profile B: daily cash basic cost $104.03 for a family of four (against $68.33 for one adult). Glossary, "Public Trust Housing": a community-owned, opt-in housing model; *PTH Independent Financing*, section 5.1: the pay-in model "serves 44 million renter households".
- **Claude's reading.** The Hub thinks of costs and housing by household; it gives no rule for how a household's needs scale with its size, so the model takes the cost of living from the MIT Living Wage Calculator by household type (the same source as the single-adult basket), with childcare as its own component, and PTH membership as a household's decision.
- **What the model does.** A household's yearly cost is MIT's typical expenses for its type (one or two adults; zero to three children) at the model's price level, with childcare by the children's ages (for children under 13, larger under 5) as a separate component, not a scaled adult basket. All members of a household are in PTH or not together. Results are reported per person and equivalized (the square-root scale, the OECD's current default) side by side, so the v5.2 panels stay comparable.

### 1.4 Pooling within the household

- **The Hub's words.** None on how a household shares its money or its BU.
- **Duke's dashboard decision (d168):** pooled within the household as the main reading; each adult keeping their own as the comparison.
- **What the model does.** `POOL` 'household' (main): earnings, BU (adults' and children's) and conversion income go into one household budget that pays the household's costs; 'individual' (reading): each adult pays their own share of the household's costs from their own income and BU. Pooling changes who counts as poor mechanically, so both are shown.

### 1.5 Inheritance

- **The Hub's words.** *Transforming the US Real Estate Market*, section 2.1 (Acre Equity): "Inheritance Rights: Intergenerational wealth transfer without market exposure"; "Transferability: Accumulated equity transfers between properties within trust networks". No inheritance tax appears anywhere on the Hub (searched every page).
- **Duke's dashboard decision (d169):** with ageing on, an estate passes to a surviving partner, otherwise to the children in equal shares, otherwise it leaves the model as now; no inheritance tax unless the Hub specifies one.
- **Claude's reading.** Acre Equity passes to heirs without being sold; if the heir lives in PTH it stays as Acre Equity, otherwise it is paid out at the liquid share the model already uses. Other wealth passes as money.
- **What the model does.** As above, when ageing and households are both on (estates have no heir in the adult-only model, which keeps today's rule).

### 1.6 Children's lives

- **The Hub's words.** *Economic Modeling and Simulation Analysis*, section 6 (results of an earlier simulation, not a design rule): "Families with children: Maximum benefit from housing security". FAQ: "Non-traditional forms of value creation are recognized — emotional support, childcare, eldercare ... all qualify for conversion at the 1× baseline".
- **Claude's reading.** Children are dependants in the design; nothing on the Hub gives them economic choices. Unpaid care at home could convert expired BU at par under the FAQ's rule; the model has no time use, so in v5.3 this is a stated limit, not a mechanism (a candidate for the later "what money does not capture" step, ledger s117).
- **What the model does.** Children have an age, a childcare need by age, schooling (ages 5-17, no fee in public school; the cost enters only through MIT's basket), a share of household resources, and no choices. They age on the ageing stream; births follow US fertility by the mother's age on their own stream; at a sourced leaving-home age a child forms their own household and enters the adult population in place of the unrelated 25-year-old entrants. Partnerships stay as first drawn (no marriages or separations in v5.3; said on the page).

## 2. The question for Duke

The dashboard's one open question (the child allowance) was answered on Oct 6 (d167: a quarter, flat by age). Two new design questions came up while reading the Hub, both about what the framework is meant to do:

1. **Children and the Act's text** (section 1.1): the draft Act gives BU to adults 18 and older; your Oct 6 answer gives children a quarter. Which is the design? (Until you say: your Oct 6 answer, with "none" beside it.)
2. **What BU buy** (section 1.2): your glossary and the Act include transportation and education; the model has let BU buy only food, housing and medical care since September. Is the glossary's list the design? (Until you say: the glossary's list is added as a labelled reading in v5.3 and its promotion is decided at the restudy; the current main result is unchanged in the meantime.)

## 3. Predictions before running

For each headline measure, the direction expected when households and children are switched on, against no programme with the same households, and why. The v5.3 report will list which held.

| Measure | Expected direction | Why |
|---|---|---|
| Below the cost of living, no programme | Higher than the adult-only run | Families with children face childcare and larger baskets per earner; single parents most |
| Below the cost of living, change with Compassionism | A larger fall in points than adult-only, but a smaller fall in proportion for children than for adults | More people start below the line; a child's allowance ($300) covers less of a child's cost (with childcare) than an adult's BU covers of an adult's |
| Child poverty (new) | Above adult poverty in both runs; reduced by the programme, less in proportion than adult poverty | As above; US data show child poverty above working-age poverty |
| Too little wealth (household, equivalized) | Lower in both runs than adult-only for couples, higher for single parents; the programme's sign by environment unchanged (worse than no programme in Adverse and Stress) | Pooling and shared housing raise savings per couple; the extra BU for children add to the programme's new money, so prices rise a little more |
| Programme inflation | Up by roughly 1 to 3 points a year in Reference | Child allowances add about 7% to the BU issued (about 0.28 children per adult × 0.25), and 'hub' BU scope reduces expiry |
| Cost per adult | Up by roughly 5 to 10% | The child allowance |
| Below 30 days of basic living (BLEI) | Lower in both runs for couples, higher for single parents | Shared costs; a household's daily cost per person falls with size |
| Hours worked | A slightly larger fall | One more income effect per unconditional dollar (the child allowance) |
| Income Gini (equivalized) | Higher in the no-programme run (closer to the US's), cut more by the programme | Household composition adds spread; the allowance rises with children |
| Wealth at 40 years with estates | Less wealth poverty in both runs than the ageing reading, a higher wealth Gini | Estates stay in the model and concentrate |
| Poverty spells (household shocks) | Longer, closer to the PSID | Partners can lose income together |

## 4. Data sources (versions as of Oct 2026)

| What | Source | Version and where |
|---|---|---|
| Household types (adults, children, ages) | Census Bureau, America's Families and Living Arrangements (CPS ASEC) | The 2023 tables are reachable (census.gov/data/tables/2023/demo/families/cps-2023.html); the 2024 and 2025 tables are to be found at their current address in B3 |
| Household wealth | Federal Reserve, Survey of Consumer Finances 2022, summary extract | federalreserve.gov/econres/scfindex.htm (the same extract `sources/scf_singles.py` reads; households by type this time) |
| Costs by household type, with childcare | MIT Living Wage Calculator, typical expenses for 1 and 2 adults with 0 to 3 children | livingwage.mit.edu, Feb 2026 build; read by hand (the site asks not to be scraped), the same eight states as `CFG.BASKET`, components regressed on totals |
| Poverty lines by household size | HHS 2026 poverty guidelines (one person $15,960; two $21,640; three $27,320; four $33,000; $5,680 for each more person) and Census 2025 poverty thresholds by size and number of related children | aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines (read Oct 6, 2026); census.gov historical poverty thresholds page |
| Births by the mother's age | NCHS, Births: Final Data (latest year), age-specific fertility rates | cdc.gov refuses connections from the build environment (403, as ssa.gov did in v5.2); a mirror or a copy Duke uploads may be needed |
| Leaving home | Census, CPS Table AD-1 (young adults living at home, by age) | census.gov families tables |
| Earnings by age | Census, CPS ASEC PINC tables (median earnings by age) | census.gov income tables |
| Equivalence scale | OECD, the square-root scale (household income divided by the square root of household size) | OECD, "What are equivalence scales?" |

## 5. What stays the same

Every new mechanism sits behind a switch (`HOUSEHOLDS`, `POOL`, `CHILD_BU_SHARE`, `BU_SCOPE`, `ESTATES`, household shocks), off by default, and with every switch off the output is bit-identical to v5.2's panels (proved with the panel fingerprints, `dev/tools/panel_hash.py`). The main stream's eight draws per adult-year are untouched: household composition, births, leaving home and household shocks each get their own random stream, registered in one table in the code and in MODEL_SPEC.md. Households appear first as a labelled reading beside the adult-only main result (d170); promotion is decided from the 500-seed restudy.
