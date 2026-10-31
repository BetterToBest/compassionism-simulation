# The community and zone layer (S37): Claude's reading of the design, and what was built

**Claude's reading of the design.** This note says what the Research Hub's papers make depend on local density, how the simulation now models it, and what it leaves out. Where the papers are silent, the most cautious reading is taken and labelled a modelling assumption. It changes the model of the design, not the design: if anything here misrepresents the framework, that is Duke's call.

## Why this layer exists

The pilot studies (`dev/reports/pilot-studies.md`, section 8) found that three parts of the design barely move any outcome: the community businesses (PTF), community housing (PTH) and zone coordination (SZH). Each part changes every share outcome by between -1.2 and +0.3 percentage points. Part of the framework's case for these parts rests on local density: businesses, housing and zones that work better where they are concentrated. The engine had no notion of place, so a synergy study run on it could only report "no synergy among these parts". That report would come from a missing mechanism, not from a test of the claim. This layer adds the mechanism the papers describe, behind a switch, so that the full study batch can test it.

## What the papers make depend on local density

1. **The PTF food price cut.** The Basic Living Economic Index paper (section 6.1, "Insufficient PTF Network Density"): "Below approximately 40% PTF merchant participation *in a given zone*, ε falls toward 1.5–1.8× as insufficient volume prevents Mondragon-equivalent overhead reduction." (ε is how much further a Basic Unit goes at PTF food prices: 2.64 at full scale.) The engine already had this test (since v5.4: 2.64, or 1.65 below 40%), but read it on the share of *all* adults who are PTF members. That share starts at 18% in the Reference environment, so the test never passed.
2. **The synergy coefficient θ.** The same paragraph: "below 55% participation density, cooperative synergies do not activate", with θ rising to 0.25 at 90% (the paper's Table 6). In the engine θ raises the PTF members' conversion rate, draws adults into PTF through SZH, and adds to the design's own BLEI. It too was read on the share of all adults, and stayed at 0.
3. **Where PTF is placed.** The research summary and glossary: SZH "organizes the geographic deployment of PTF businesses and PTH communities", "defines the geographic zone boundaries and service catchments within which PTF businesses are deployed and scaled". The BLEI paper's answer to low density is "Phase deployment beginning in high-density urban zones; SZH zone activation thresholds".
4. **How zones form.** The glossary: "Zone formation threshold: determined by public survey majority via CIP"; "Minimum zone cohesion: defined by shared governance charter adopted by resident supermajority"; "No fixed geographic size: zones scale from neighborhood to regional". SZH "does not mandate that residents move into matching zones" and "does not prevent cross-zone economic activity".
5. **PTH.** "SZH zone formation creates the community coherence required for PTH democratic governance to function effectively" (no size is given). The PTH financing paper's break-even table: a pay-in PTH needs 30-40 households, a grassroots cooperative 5-10.
6. **Zone dynamics.** The governance paper (section 4.3) writes zone populations as flows of people between zones, with mobility rates and preference and capacity functions that it does not give values for.

## Claude's reading (each a modelling assumption)

1. **The density tests are read in each zone, not across the whole population.** The paper says so for the food price cut; θ is in the same paragraph, about the same network. No constant changes: 40%, 55%, 90%, 0.25, 2.64 and 1.65 are the values the engine already used (design parameters taken from the Hub).
2. **SZH's job in the model is to place the PTF where its members live together.** The model has no map. Placing PTF businesses in a zone, with the residents there joining, is the same in the model as grouping the PTF members into the same community. So with SZH on, the starting members are placed together in zones; without SZH they live wherever the draw puts them. Who is a member does not change: the same random draws decide it in both cases. No one is moved for being a member, in keeping with "does not mandate that residents move".
3. **A zone's member share (f) is a design parameter: 0.5, swept 2/3 and 1.** A zone forms where a majority of its residents want it, read as: in a zone, members are at least half the residents. This is the lower of the Hub's two thresholds (survey majority) and the cautious choice. The zone charter's supermajority (2/3) and a zone of members only (1, the upper bound) are run beside it. If members are already half of all adults, no zones are needed and none form.
4. **A community's size (k) is a resolution, not a population: 100 adults, swept 50 and 250.** The density tests read shares, and a share does not depend on how many people the zone holds. k is how many simulated adults stand for one zone. Smaller k gives finer zones but noisier shares where members are scattered by chance. With one community (k at least the population) the layer gives exactly the engine without it (checked). Limit: at 500 adults there are only five communities, so zones are coarse. The preregistration addendum therefore runs the layer at 2,000 and 10,000 adults as well.
5. **Zones form with SZH whether or not CIP is on (main reading); the Hub's own rule, zones only with CIP, is run beside it.** The Hub forms zones through CIP surveys. Written into the model as a rule, that would make every effect of zones show up as a CIP and SZH synergy, which the study would then "find" because the rule was there. The main reading lets zones form through ordinary local planning, so that any CIP and SZH synergy the study reports comes from a mechanism. The literal reading (`zc: true`) is a preregistered sweep row, and its effect is reported as coming from the design's rule.
6. **Word of mouth is local.** The engine's PTF adoption has an imitation term (Bass 1969: the more members, the more join). With the layer, an adult imitates members in their own community. Keeping the population-wide term (`bass: 'pop'`) is a sweep row, so the report can say how much of any effect comes from local imitation and how much from the density tests.
7. **Not modelled, and why.**
   - *PTH density.* The Hub's only PTH quantity is a count of households (break-even at 30-40), and a sample of a zone's adults cannot show a count: 20 simulated members could stand for 20 households or 2,000. The coherence PTH governance needs has no size. PTH is unchanged.
   - *Moving between zones.* The governance paper's flows have no values, and SZH does not make anyone move. Communities are fixed for the run; an adult who dies is replaced by a new adult in the same community.
   - *Capacity by zone.* The PTF's capacity (how many adults it can serve) stays population-wide: there is no source for where new capacity would go.
   - *Price damping.* The price level is economy-wide, so the PTF's damping of inflation stays population-wide.
   - *Shopping across zones.* A member's price cut is read in the member's own community. A member who shops at another zone's PTF is not modelled.

## What was built

The switch `COMM` (per study row: option `cl`; `{}` for the main values) in `index.html`, off by default. It acts only in runs with PTF.

- At the start of the run, households (each adult alone, without households) are dealt into `round(n/k)` communities, in an order drawn on the layer's own random stream (seed + 600059, one draw per household). Households are never split. The eight random draws per adult and year are untouched.
- With zones (SZH and PTF on; with `zc`, CIP on too), communities are filled in turn with member households until members are a share `f` of the community, then with non-member households up to its size. The last zone takes the members left over. The other communities are dealt as above.
- Each year, each community's member share replaces the share of all adults in the food price cut's test, in θ (the rate bonus, SZH induction and the design's BLEI term) and in the imitation term. Each share is taken at the point in the year where the population share was taken before, which is why one community reproduces the engine exactly.
- Parameters: `k` 100, `f` 0.5, `zc` false, `bass` 'local' (`COMM_DEFAULTS`). All four are design parameters, and the preregistration addendum sweeps each.
- Reported (`CL_KEYS`): `clN` communities; `clZ` zones formed at the start; `clSd` how much the member share varies between communities (standard deviation, points, mean over years); `clHi` the share of members living where the share is at least 40% (mean over years); `clTh` the same where θ is above zero.

## Checks (before any study run; `research-update/prereg/checks/s37_layer_checks.js`)

In all three environments, at 2 seeds:
- One community (60 adults, k 100) equals the layer off on every measure, at 20 years, and at 40 years with ageing.
- The no-programme row, and a row with CCO but no PTF (k 10), are identical with the layer on and off.
- At 400 adults the layer changes the release row, runs with every swept setting, and gives identical results when run twice.
- Zones form with SZH and PTF on. With `zc: true` and CIP off, none form; with SZH off, none form.
- With the layer off, the guard test (every earlier output bit-identical) and the validate, unit and page tests pass.

The checks print the layer's own placement figures (communities, zones, where members live) and no outcome value. Those figures show the coarseness limit above: at 400 adults with k 100, about half the members live where the share reaches 40% over the run, and three quarters with k 50.

## What it can and cannot show

It can show whether concentrating the PTF, as the Hub says SZH does, lets the density tests the Hub itself sets pass where the members live, and what that does to basic living, the cost of living, wealth, cost and prices. It also shows whether SZH and PTF then do more together than apart. It cannot show whether real zones would reach these densities, or whether the Hub's thresholds and price cuts are right: those are the Hub's figures, used as given and labelled as such. The layer has not been reviewed by an independent economist.
