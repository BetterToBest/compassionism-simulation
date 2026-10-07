# The model now checks its own books

Oct 6, 2026 · v5.3, plan item B2 · Claude · every release row, three environments; the effect of two corrections on 500 paired seeds · nothing on the live page changes until the v5.3 release

## What was asked

Before households and children go in (the next steps), the plan asks that the model's accounting be made exact and checked automatically: every dollar and every Basic Unit (BU) has a source and a destination, and a check fails if anything appears from nowhere or disappears. Where a check fails, that is a finding, and the model is corrected; the check is never made looser to let it pass.

## What the check does

The model can now audit itself while it runs (it is switched off unless asked for, so ordinary runs are unchanged, and switching it on changes no result: the tests compare over 20,000 results with and without it, and every one is identical). Every simulated year it checks:

1. **Each person's money.** What a person owns at the end of the year equals what they owned at the start, plus their wages, conversion income, Social Security and any cash transfer, plus interest and the cash paid out from their community-housing equity, minus their living costs, what they put into that equity and what they consume from their surplus, plus any debt written off at the floor. Each of these is the same yearly record the poverty measures read, so the check also proves the poverty measures see every dollar that reaches a person.
2. **Each community-housing member's Acre Equity.** The equity at the end of the year equals the equity at the start, plus what the member put in, plus its growth, minus the part of the growth paid out in cash.
3. **Every BU.** BU issued (the monthly allowance and the launch gift) end up spent at a business, converted (by a person or by the business), destroyed (expired BU that are not directed to projects, BU above a cap), or still held (the pools waiting to be paid out next year, BU a person holds for later conversion). Nothing else.
4. **The essential businesses' conversion premium.** What the businesses pay out each year from last year's premium (as lower prices, as dollars to workers, as reinvestment, as capital charges) plus what they carry to next year equals what they had.
5. **The Source's books against the households' books.** What the Source pays for BU at face value equals the BU people spent; what it pays at conversion equals the conversion income people received plus the price cuts, reinvestment and capital charges; the BU it issued equal the allowances; and the money it puts into the economy (what the price model reads) agrees.
6. **How the Source pays.** What it pays out equals the new money it creates plus the part backed by new output.

The tolerance is a billionth of the amounts being balanced; ordinary rounding in a computer is about a million times smaller than that, and the two real problems found are about ten million times larger.

## What it found

All of the checks pass on every one of the 49 rows of the release (the main result, every labelled reading and their no-programme comparisons), in all three environments, except in two places. Both are mistakes in how the model kept its books, and both are now corrected for v5.3.

**1. Community-housing equity growth was counted twice.** Each year a community-housing member's Acre Equity grows (by 3 to 6%), and part of that growth is paid to the member in cash (15% in the first year, rising to 85% after five years). The model paid the cash *and* left the whole growth in the equity, so the cash part was counted in both places, and the extra equity grew again the next year. This had been listed as an open question since v4.16; the check shows it is simply a double count. Corrected: the cash part now leaves the equity when it is paid.

*What the correction changes* (500 paired runs in each environment, the main result): the cash paid out from community-housing equity falls by about a tenth (in the Reference environment from $21.91 to $19.89 per adult a year, in today's money; Adverse $17.97 to $16.66; Stress Test $13.83 to $12.29). Every headline figure moves by less than one hundredth of a percentage point: below the cost of living by −0.002 to −0.003 points, too little wealth by −0.002 to 0.000 points (within the run-to-run noise), below 30 days of basic living by −0.001 points; the cost falls by $1 to $2 per adult a year. Against no programme, every change on the page is the same to two decimals. The double count was real but small, because few members hold equity long enough for its growth to compound much in 20 years.

**2. In the two "landlords raise rents" readings, the businesses handed out more than they had.** Those readings (labelled sensitivity tests, not the main result) let landlords raise the rent of tenants paying with BU. The essential businesses share their premium as one percentage cut on each customer's essentials; the cut was worked out on rents before the landlords' increase but applied to rents after it, so up to 4% more was handed out in a year than the businesses had. Corrected: the cut is worked out on the same bill it is applied to.

*What the correction changes* (500 paired runs, the first rent reading): the extra money had made that reading look a little better than it should. With it removed, in the Reference environment 0.25 points more adult-years are below the cost of living, 0.56 points more adults end with too little wealth, 0.18 points more adult-years fall below 30 days of basic living, and the programme costs $166 less per adult a year (the handed-out money no longer counts as spending). In the Adverse environment the same three figures move by +0.24, 0.00 and +0.16 points (cost −$132); in the Stress Test by +0.01, −0.01 and 0.00 points. Nothing outside the two rent readings changes.

## Two things the check cannot cover (stated, not hidden)

- **The community-housing organisation's own books.** The plan asks that a member's housing payment be split into running costs, equity, community surplus and financing costs. The model does not keep accounts for the housing organisation itself, only for the member (the 35% cut in housing costs, a quarter of that saving put into equity, and the equity's growth). Those books arrive with the community-housing balance sheet planned for v5.4, and the check will cover them then.
- **What the equity contribution is a quarter of.** The quarter of the housing saving that goes into equity is worked out on the BLEI paper's daily cost of living ($68.33 a day) rather than on the cost of living the model uses for everything else (MIT's $49,370 a year), so in practice a member puts 12.6% of their actual saving into equity, not 25%. No money is lost either way. The 25% is the model's own choice (no source gives it), so I have not changed it now; changing it would be retuning a setting without evidence. It is listed for the v5.4 sensitivity study, which will show what happens across a range.

## What this means for the figures

Nothing on the live page changes now. The two corrections are switches that stay off until the v5.3 restudy, so the release commands still reproduce the published v5.2 figures exactly (checked again this step, by fingerprint, in all three environments over 20 and 40 years). At the v5.3 restudy the corrections are on for every row, together with households and children, and the v5.3 report will show the combined effect. From the measurements above, the main result will move by less than a hundredth of a point from the corrections themselves; the two rent readings will read about a quarter to half a point worse in Reference and Adverse.

Every identity also held over all 500 runs in each environment for the main result, the first rent reading and the ageing reading with the corrections on (47.2 million checks of a person's money, 7.9 million of community-housing equity, and 94,500 of each of the yearly totals; the largest gap anywhere was eight parts in a thousand trillion). The runs and the exact commands are in `dev/runs/acct-check-ref.json`, `-adv.json` and `-st.json` (`node dev/tools/acct_check.js ENV 500`).

## Decisions made (full reasons in `dev/DECISIONS.md`, Session 39)

- The check lives inside the model (so it sees every person, every year), is off by default, and counts problems rather than stopping a run.
- Both mistakes are corrected (the plan's rule: an identity that fails is corrected, not shown as an option). The plan had listed the equity reading as an option for v5.4; the check showed it is a mistake, so the correction comes forward to v5.3.
- The equity contribution's base is kept for now and tested in v5.4.
- BU a person was holding for later conversion when they die lapse, as unspent BU do (in the main result there are none: project BU are converted the year they are received).
- Each change to the model's code between releases is now recorded with proof that it changes no published result (`dev/runs/engine-lineage.json`), so the page's check that its figures come from its own engine keeps working during the round.

## Does anything here misrepresent your vision?

One reading of yours is involved: that part of a community-housing member's equity growth is paid out in cash, rising with the years of membership (the BLEI paper's Table 1a). The correction keeps that and only stops the same dollars being counted twice. Please say if the cash payout is not what you intend.

## What you need to do

Nothing yet: this is one step of v5.3, which arrives as one pull request when households and children are done. You can read this note and say if anything reads wrong.
