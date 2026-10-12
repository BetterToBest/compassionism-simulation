# v5.4 release: labour and markets

Oct 12, 2026 · Claude · v5.4 · 500 paired runs in each of the three environments, 20 and 40 years (engine fe88599, run on a 16-core cloud machine in 2 h 24 min)

## What v5.4 adds

People now lose jobs and find new ones, as US workers do (unemployment insurance in both runs, lower pay after a lasting loss). Community housing (PTH) keeps its own books, with an enforced identity each year. Community businesses (PTF) cut prices sector by sector and members can leave. New risk measures report how far savings fall, how fast income recovers and how often people slip back into poverty. Each part sits behind a switch; with all switches off the figures equal v5.3.1's.

## The main result against v5.3's (20 years)

Each cell: no programme → Compassionism, and the change in points. The v5.3 column is the same measure on v5.3's rules (no job loss), read from the same runs.

| Measure | Reference, v5.4 | Reference, v5.3 | Adverse, v5.4 | Adverse, v5.3 | Stress Test, v5.4 | Stress Test, v5.3 |
|---|---|---|---|---|---|---|
| Adult-years below 30 days of basic living | 26.5% → 11.6%, −14.9 | −14.9 | 31.5% → 17.3%, −14.2 | −13.4 | 31.5% → 35.0%, +3.4 | +5.5 |
| Adult-years below the cost of living | 49.2% → 19.6%, −29.6 | −28.3 | 66.0% → 31.3%, −34.7 | −38.4 | 66.0% → 52.3%, −13.7 | −15.5 |
| Adults with too little wealth at the end | 32.6% → 43.6%, +11.0 | +5.5 | 45.1% → 80.0%, +34.9 | +40.6 | 45.1% → 75.4%, +30.4 | +37.5 |
| Programme inflation a year | 50.0% | 47.9% | 59.5% | 61.5% | 26.8% | 28.5% |

At 40 years (Reference): below the cost of living 42.1% → 16.2% (−25.9); too little wealth 31.4% → 32.2% (+0.8); programme inflation 48.3%.

## What this means, in plain words

- **The hardship result holds.** In Reference the programme still cuts adult-years below the cost of living by about 30 points, and every one of the 500 runs is better off on that measure. Poverty severity falls slightly more than in v5.3 (−6.0 against −5.1).
- **Job loss changes the no-programme run too**, so the starting points moved (49.2% below the cost of living with no programme, against 45.1% in v5.3). v5.4's figures should be compared within v5.4, not with earlier releases.
- **The wealth result got worse in Reference at 20 years** (+11.0 points of adults with too little wealth, against +5.5), and better in Adverse and Stress Test. In Reference it nearly closes by Year 40 (+0.8). Most of the growth comes from the 10% lower pay people take when they return to work: with no pay cut the gap is +6.6 points (31.3% → 37.9%), with the 10% cut +11.0 and with a 20% cut +15.7, because the cut raises the programme run's share with too little wealth about four times as much as the no-programme run's (about 6 points against 1.4 for each 10% of pay), while the new rules for community housing (PTH) and community businesses (PTF) move it by less than 0.3 points (readings "no pay cut on return to work", "a 20% pay cut", "Acre Equity by the earlier 3-5% rule" and "PTF cutting prices 25%" on the findings page).
- **Stress Test is still the hardest case**: below 30 days of basic living gets worse than no programme (+3.4), as in v5.3 (+5.5), though by less.
- **New measures (Reference):** average unemployment 2.4% of adult-years, unemployment insurance replaces about 6.6% of lost pay across adult-years on average (`emUI`), the typical largest fall in a person's savings is 24%, PTH members leave at 5.8% a year, PTF members at 2.3% a year.

## Claude's reading of the design (please check)

Job loss as a spell that BU soften and PTH makes less dangerous (Hub: *Economic Modeling and Simulation Analysis* 5.3); the trust owns the homes and members' equity grows at most at inflation plus 2%; PTF is several sectors, with price cuts only where the Hub gives a number (food, utilities) and none elsewhere. The three questions for you are on the dashboard (d174–d176). Anything that misrepresents your vision, tell me.

## Limits

No separate behavioural response to BU in job search (one income effect per dollar); emergency employment programmes are not modelled; the model has not been reviewed by an independent economist.

## How it was checked

The 33 pieces were merged by `merge_parts.py`, which refuses mixed builds; every piece's manifest names engine fe88599, clean. Six explore exports (500 seeds each) passed their self-checks against the panels. Validate, unit and page tests: see the pull request.

## What you need to do

Read this; say if anything misrepresents your design; merge pull request #13 when it reads right. The merge is the release.
