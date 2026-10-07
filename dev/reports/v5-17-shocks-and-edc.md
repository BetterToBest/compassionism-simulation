# Partners' incomes, and the extractive drain measured from the money

Oct 7, 2026 · v5.3, plan item B6 · Claude · 500 paired runs in each of the three environments · reporting and a labelled reading; nothing on the live page changes until the v5.3 release

## What was asked

Two things. First, with households, partners' incomes should be able to move together: when one has a bad year, the other may too. Second, the Extractive Drain Coefficient (EDC, the share of income lost to rent, interest and fees) should be measured from the money people actually pay. The figure the earlier engine shows comes from a formula set to the BLEI paper's target bands; it should be labelled as what it is, a "design target proxy".

## Partners' incomes

**What the model does.** Each year, everyone's income can rise or fall: by a shared amount in a recession, and by each person's own swing of up to 10% either way. With households, a couple's two swings can now share a part, so they move together as much as the data say.

**What the data say.** Shore (2010, *Review of Economics and Statistics*) measured how American couples' incomes change together. They move together very little: about +0.10 in good years, and slightly in opposite directions (−0.10) in bad years, because when one partner loses income the other often works more. The model uses those figures. It also has a stress reading in which partners' swings move together strongly (0.5). Losing a job together is a different risk and arrives with employment in v5.4.

**What the 500 runs show.** No headline figure moves by more than 0.06 point, with either setting, in any environment. The swing this reshapes is small (±10%), and recessions, which already hit everyone together, matter far more.

## The extractive drain, measured

**What the model measures.** I followed the glossary on the page: "Share of income captured by contracts that build zero household wealth (rent, interest, fees). PTH payments have EDC = 0."
- **What counts as drain:** rent paid to a landlord, plus interest on debt (only where a reading charges it). The model has no fees. Payments for community housing count as zero.
- **What it is measured against:** all income, including the BU allowance at face value, since BU can pay rent too.
- **For families:** it is the household's figure, counted for every person in it.

**What the 500 runs show** (average share of income, no programme → Compassionism):

| | Measured from payments | Design target proxy (the formula) |
|---|---|---|
| Reference, adults alone | 33.7% → 19.3% | 48.5% → 10.4% |
| Reference, households | 25.8% → 12.9% | 48.5% → 10.1% |
| Adverse, adults alone | 50.6% → 25.5% | 51.6% → 10.2% |
| Stress Test, adults alone | 50.6% → 38.6% | 51.6% → 19.5% |

**What this means.** Measured from the money, the drain falls by roughly half with the programme in Reference and Adverse. The formula says it falls by about four-fifths. The formula gives every participant a much lower drain by assumption. The payments show what happens: members of community housing pay none, but most participants are not members and still pay market rent. The BU help them pay it, so it takes a smaller share of their income, but it does not go away. The proxy assumes most of the drain disappears; the payments show it halves. Both figures will be reported side by side in v5.3; the proxy's results are conditional on its target being met, and the replication page now says so where the formula's 0.025 appears.

## How it was checked

- **Off means off.** With either switched off, every earlier result is reproduced exactly.
- **The partners' setting does what it says.** In the tests, couples' swings correlate 0.51 when set to 0.5, and +0.11 in good years and −0.09 in recessions under Shore's figures. Each person's own swing keeps its size.
- **Measuring changes nothing.** Switching the measured EDC on changes no result.
- **The books balance.** Every accounting check passes in every run.

## What changed on the pages (with the v5.3 release)

- The earlier engine page's EDC tile, its comparison table, its notes and its export now say "design target proxy".
- The glossary on both pages explains the difference.
- The replication page's formula for advancing an octave notes that results using the 0.025 figure are conditional on community housing reaching it.

## Claude's reading of the design (please check)

- **A community-housing payment is not extractive.** That is what the page's glossary says. The trust's running costs are part of the payment, so it is a reading of your definition, not a calculation.

## What you need to do

Nothing yet. Please say if counting community-housing payments as zero drain is not what you intend.

The runs and their exact commands are in `dev/runs/shock-edc-check-ref.json`, `-adv.json` and `-st.json` (`node dev/tools/shock_edc_check.js ENV 500`).
