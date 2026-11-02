# What backs the money the programme creates: Claude's reading of the design

Nov 2, 2026 · research-update plan step S51 (ledger D11) · written before any run · Claude

Duke, this note sets out my reading of what your writing says backs the new money, and how the model will now represent it. Please say if it misrepresents your design. Where the text is silent I took the most cautious option and labelled it a modelling assumption.

## Why this matters

In the released model, the Source (the Treasury) pays every conversion, and almost all of that payout is new money. Only the work on projects, counted at the pay for its hours, is treated as output that backs it: about 7.7% of the payout. The rest raises prices through the model's price rule. That is where the release row's programme inflation of about 51% a year comes from. The other end of the published range, "every dollar backed", removes that inflation by assumption. Neither end is worked out inside the model. The audit (S13, item E6) found the headline depends on it: if wages keep up with prices only in part, the gain shrinks fast unless the payout is backed. Your answer to ledger decision D11 says backing is the design's requirement. So the model should make it a mechanism and report how much backing the result needs.

## What the writing says

1. **Your article** ("Harmonize Economics with Creative Currency Octaves", Sept 16, 2024, updated Aug 6, 2025) says basic units "could be the first currency in history backed by publicly-endowed art and creation", and that both currencies "are sourced by the treasury." Expired basic units "either revert back to their source, the treasury, or get converted into primary notes." Conversion rates depend on productivity, efficiency, creativity, quality and beauty, and octave levels depend on "project scope, market forces such as supply and demand" and cost savings. The article says CCO would "mitigate inflation when compared to UBI without CCO." It does not say how the converted money is taken back out of circulation, or how long the work takes to produce anything.
2. **The Hub's dual-currency paper** (section 3.4) writes the money supply as last year's money plus everything converted this year. Its inflation equations (4.1) have two terms: new money as a share of output raises prices, and **growth in output** lowers them (the β × ΔY term). The paper's conversion "transforms basic units into primary currency through productive participation."
3. **The Hub's community development paper** speaks of "community-coordinated investment in local knowledge and productive capacity". It also says CCO contributions can support public services such as education, health care and infrastructure maintenance.
4. **The Hub's research summary** describes the phi rate as "a formal mechanism for recognizing beauty and social harmony as productive economic contributions". The Cultural Value Integration paper calls CCO a currency "backed by 'publicly-endowed art and creation'". That is real value, but most of it is not goods sold in the shops whose prices make up the basket.

## My reading, as rules the model can run

- **B1. Conversions pay for contributions, and part of them build supply.** A share of the Source's net payout (f, a design parameter) pays for work on projects that add to what the economy can supply: food, housing, transport, utilities, repairs, local production. The rest pays for contributions whose value the model does not count as market supply (care, art, culture, learning). The design does not say what share goes to each, so f is swept from a quarter to all of it.
- **B2. Projects take time and wear out.** A funded dollar adds output only after a lag (2 years in the main reading; 1 and 3 swept), and that output wears away a little each year (5% in the main reading; none swept). Both are design parameters. The writing is silent on both.
- **B3. How much output a dollar buys** (rho, output a year per dollar funded, in year-0 prices) is a design parameter, swept from 0.05 to 0.32. The top value, 0.32, is the US economy's whole output per dollar of its fixed capital (2024 GDP of $29,381 billion over a net stock of fixed assets of $91,549 billion; BEA, via FRED, opened Nov 2, 2026). It is an upper end, because it credits capital with all of output, labour's part included.
- **B4. Output cannot grow without limit.** Added output needs people and materials. In the main reading, the projects can add at most what the economy's underused labour could produce: 8% of the year's earned income (BLS U-6, already in the engine). Kenya's measured peak absorption of cash transfers (16%) and no ceiling at all are swept. This ceiling is a modelling assumption. Without it, the most productive settings would have the projects producing more than twice the whole economy's earned income within 20 years. That cannot happen.
- **B5. Only added output absorbs new money (the main reading).** This is the most cautious reading, and the Hub's own inflation equation uses it. The model's price rule is the quantity theory's: prices rise with new money as a share of income, and the new money stays in circulation. So output already there absorbed earlier money; each year, only the output added that year absorbs that year's new money. This is a modelling assumption.
   *The other reading, swept beside it ("proceeds retire the money"):* each year's whole project output is sold, and the proceeds go back to the Source, which retires that much new money. This is how the released model already counts matched project output and the every-dollar-backed reading. It needs an institution the writing does not describe (the Source taking the projects' sales revenue), so it is not the main reading.
- **The backed share is then an outcome**, read from the run, not an input. Wages, conversions, octaves and every household's pay are unchanged. Only the price path moves, and then everything that follows from prices.

## What this means before any run

The release row pays out about 60% of a year's earned income in new money, every year. Under B4 and B5, no plausible project productivity backs more than a small part of that. The study is built to show this honestly. It reports two things:
1. the **break-even backed share**: how much of the payout must be backed for basket poverty to fall when wages keep up with prices only in part (95%, 90%, 75%);
2. **whether the mechanism reaches that share**, and under which settings.

If it does not, the report will say so plainly. The design's other levers (a smaller or slower payout, a higher conversion tax, octave capacity limits) are then the questions to ask. Changing them is a change to the design, so it would be your call (a ledger decision), not mine.

## Not changed

The released figures do not move: the mechanism is behind a switch (row option `bkm`). Essentials capacity through PTF is not used as the channel here. The release row's programme inflation is in the general price level, which also raises essentials prices. The PTF supply channel is part of S52 (the supply-shock environment, PTF local sourcing).
