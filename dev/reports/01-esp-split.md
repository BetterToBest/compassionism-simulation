# Step 1 report: where an essential-service business's earnings go (the ESP split)

Oct 1, 2026 · plan step 1 · Claude · 500 paired seeds, three environments · harness only (the live page is unchanged)

## What this step changes, in plain words

When a grocer, utility or other essential-service business (an "ESP") accepts Basic Units (BU), it converts them to dollars at three times their face value. The extra it earns above face value (the "premium") is large: about $15,900 per adult a year at the reference settings.

Until now the model paid that premium out the following year to every adult in proportion to their wage. That was a stand-in, not the design. This step replaces it with your design:

- **Community-owned businesses (PTFs)** split their premium three ways: lower prices for their customers, reinvestment in new capacity, and profit-sharing with workers. Once there is enough capacity to serve everyone, the split becomes 60% lower prices and 40% profit-sharing.
- **Privately owned businesses** keep all of their premium (your answer of Oct 1). The owners receive it.

## How the model represents it (Claude's reading of the design where the Hub is silent)

- The model has no individual businesses, so it measures the PTFs' share of the premium as the share of last year's BU that PTF members spent (PTF members are treated as the PTFs' customers). Over the run this averages 28% at reference, 30% in the Adverse Environment and 20% in the Stress Test. The other 70-80% is private.
- **Owners** of private businesses are every adult in proportion to their wealth (the model has no shares or firms; wealth is the usual stand-in for ownership). Their dollars count like any dividend: people work a little less when they receive money they did not work for (the same 16 cents per dollar used for every design).
- **The PTFs' price cuts** go to PTF members, the same people counted as their customers. BU then buy the cheaper essentials first, and BU no longer needed expire and go to project hiring, as every expired BU does.
- **The profit share** goes to every essential-service worker (23% of adults), by wage. It counts as a raise.
- **Reinvestment** goes into a capital account. "Enough capacity" means the account reaches $18,862 per adult, the 2025 capital stock per adult of grocers, food services and utilities (US Bureau of Economic Analysis, Fixed Assets Table 3.1ESI; Census adult population). In this step the capital does nothing yet; step 2 gives it a role.
- The split draws no random numbers, so every comparison is between the same simulated people.

## What it does

The measure is poverty severity (how far below the cost of living people fall, with the deepest gaps counting most; the "FGT2" index), averaged over 20 years. Negative numbers mean less poverty. Each change is checked on two other measures too: the share of years people spend below the cost of living ("basket poverty") and the share with too little wealth at year 20 ("wealth poverty").

| | Reference | Adverse | Stress |
|---|---|---|---|
| Today's stand-in, against no program | +4.14 | −0.34 | −0.54 |
| **The split, against no program** | **+15.63** | **+11.41** | **+3.30** |
| The split against today's stand-in: poverty severity | +11.49 | +11.75 | +3.84 |
| … basket poverty (points) | +0.90 | −3.87 | +0.43 |
| … wealth poverty (points) | +2.60 | −4.85 | −0.79 |

Every interval is narrow (within about ±0.1 on poverty severity).

**In everyday words: with your split, poverty is deeper than with today's stand-in in all three environments, and deeper than with no program at all.** In the Adverse Environment fewer people fall below the line, but those who do fall further; the two measures disagree, so this is not a gain.

### Why

1. **Most of the premium goes to private owners.** At reference, $10,951 of the $15,263 premium per adult a year goes to owners in proportion to wealth, so it flows to the richest adults. Today's stand-in spread it by wage instead.
2. **Owners work less, and everyone pays more.** The dividends cut owners' hours (the income effect), and the program is still paid for by a flat contribution on wages in this step. Hours fall 36% against 26% today, and the contribution rises from 80% to 84% of wages at reference. Wage earners who are not owners lose.
3. **PTFs are small for most of the run.** Because PTFs earn only their share, their reinvestment reaches "enough capacity" only in year 16 on average at reference (year 17 in Adverse; never in the Stress Test). So the 60/40 phase barely starts.
4. **Who gains and who loses (against today, per adult a year, reference):** the poorest third by starting wage gains $3,301; participants lose $1,418; adults who chose not to take part lose $6,986; the richest third by wage loses $10,065 (their wage income falls by more than the dividends add). People below the line for basic living (BLEI under 30 days) rise by 3.7 points among participants and 2.3 among non-participants.

### The same split for every business (your earlier default, before Oct 1)

If every ESP split its premium (no private owners keeping theirs), the result is much closer to today: +2.21 against today at reference, +3.20 in Adverse, +1.45 in Stress. Capacity is then reached in year 5 at reference (as the earlier sizing found) and year 12 in Stress. This is still worse than today's stand-in, as the sizing predicted (+1.16 before work responses, expected +1 to +2 after; it came out at +2.21).

### What moves the result (against the split as above, reference)

- **When capacity is reached matters most.** Capacity from year 1: −2.34 (better). Reinvestment spent as price cuts instead: −2.69. Health care included in the capital target: +0.79 (worse).
- **Who gets the PTF price cuts barely matters** (every adult instead of PTF members: +0.54; participants only: +0.99).
- **Each third alone, if every business split and the rest were paid as today:** a third to price cuts is better than today (−0.88 at reference, −1.19 Adverse, −0.07 Stress); a third to reinvestment is worst (+5.46 at reference), because in this step the capital reaches nobody; a third to profit-sharing is worse (+3.22).
- **Financing.** If conversion rewards were new money instead of being paid by the wage contribution ("hybrid" financing), the split still does worse than today by 2.1 points at reference, with prices rising about 26% a year (a = 0); if every reward dollar were backed by new output (H1), by 1.7.

## What it means

Your design sends most essential-service earnings either to community price cuts and capacity (PTFs) or to private owners. In this model both are worse for the poorest than spreading the premium by wage, for two reasons the model can show and one it cannot yet:

- Private owners' share goes to the wealthy.
- Capacity costs money now and helps only once it exists; in this step it helps no one at all.
- What the model cannot show yet: what PTF capacity does for prices and supply (step 2), and how the programme is paid for (step 3). Today every dollar is paid by a flat contribution on wages, which is not your design.

So this is not a final verdict on the split. It is the split's cost, measured before its benefits are modelled.

## Limits

- The model has no individual businesses, so "PTF" versus "private" is measured through PTF members' spending.
- Ownership of private businesses is read as wealth.
- There are no places, so the split cannot vary by location (your charters, S4).

## Exact commands and files

- `node harness.js testbed 500 surp ref`, `… adv`, `… st` (outputs in `dev/runs/step1-surp-500-{ref,adv,st}.txt`; 14 minutes each).
- Code: `SURP` in `harness.js` (off by default; with it off every earlier output is byte-identical). Tests: `surpUnitSuite`, 12 tests, run by `node harness.js unit`.
- Choices made: `dev/DECISIONS.md`, "Step 1".
