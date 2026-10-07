# Children's lives and estates: families that live through the 20 years

Oct 7, 2026 · v5.3, plan items B4 and B5 · Claude · 500 paired runs in each of the three environments · a labelled reading being built; nothing on the live page changes until the v5.3 release

## What was asked

The household reading (the last report) kept each family exactly as first drawn: children never grew older and no one was born. The plan asks for children's lives when the model's ageing is on: children who age, are born, grow up and leave home, and who take the place of the unrelated newcomers when they become adults. You decided (on the dashboard) what happens to someone's estate when they die: it goes to the surviving partner, otherwise to the children in equal shares, otherwise it leaves the model, with no inheritance tax.

As a reminder, ageing is itself a labelled reading from v5.2: adults grow older, retire at 67 on Social Security, and when one dies a new 25-year-old takes their place. The main result has no ageing, so nothing here changes the main result.

## What the model now does (households with ageing)

**Ages that fit together.** At the start, ages are drawn within each family so that they make sense together:
- A mother's age is drawn from how many women there are at each age, combined with the 2024 birth rates at the ages she would have had each child (National Center for Health Statistics).
- Her partner's age adds an age gap between spouses taken from the Census Bureau's 2023 tables (on average the husband is about two years older).
- Couples without children and single adults follow the Census figures for their ages.
- Couples are a woman and a man. A single parent is a mother 83% of the time (the Census share of children living with their mother only).

**Each year:**
- Children grow a year older. Childcare stops at 13.
- At 18 a child stops being a dependant and leaves home. From 18 to 24 they are outside the model, as 18-to-24-year-olds always have been: the model's adults start at 25.
- At 25 they can come back as an adult with their own household, taking the place of an adult who has died. If no place is free that year, they leave the model.
- Women up to 49 can give birth, at the 2024 national rate for their age. The rate is a little higher for women with a partner and lower for women without one. The two adjustments come from Census figures (22% of young children live with one parent); they were not tuned to make the model match anything.
- When a household's last adult dies, its children under 18 leave the model (to relatives outside it). This happens to about two children in a run.

**Estates (your decision).** When someone dies, what they owned goes to their partner; if there is no partner, to their children in equal shares; if there are no children, it leaves the model. In more detail:
- Debts are not inherited.
- A child under 18 has a share, but it leaves the model with them.
- A grown child receives their share only if they are an adult in the model.
- Acre Equity stays Acre Equity for an heir who lives in community housing. Otherwise it is paid out at the share members can already take in cash, and the rest stays with the community trust.
- The comparison reading lets every estate leave the model, as in the adult-only model.

## How it was checked

- **Off means off.** With households or ageing switched off, every earlier result is reproduced exactly: every household reading, both adult ageing readings, and the release panels, by fingerprint, in all three environments.
- **Step by step.** Tests follow one family: a child leaves home at 18, can take a place at 25, and childcare stops at 13. A birth happens exactly at the stated rate, and never after 49. Estates go where they should, and what passes plus what leaves always equals the estate.
- **The same families in every design.** Births, deaths, newcomers and children are identical with and without the programme in every run (they use their own random numbers), so every comparison is fair.
- **The books balance.** Every accounting check passes in every run: 15.5 million checks of a person's money and 4.6 million of couples' shared money per reading. In the Adverse environment the check on couples flagged 11 gaps of two billionths of a dollar. They were rounding on couples holding about $8 million in that environment's late, inflated prices: the check had measured its tolerance against the tiny amounts moved between partners rather than against the wealth they share. The check now measures against the wealth, as every other check does; no figure changes.

## What the 500 runs show

Compassionism against no programme, the same families in both, paired run by run. The 95% intervals are narrow: within ±0.8 point for every share below.

**Reference environment**

| Measure | Adults alone, with ageing | Households with ageing |
|---|---|---|
| Adult-years below the cost of living | 63.4% → 25.0% | 55.3% → 17.0% |
| Adults with too little wealth at the end | 59.6% → 51.5% | 50.7% → 29.3% |
| Adult-years below 30 days of basic living | 51.0% → 20.2% | 41.0% → 12.1% |
| Children below the cost of living (all years) | — | 74.2% → 28.2% |
| Children below the cost of living, Year 7 | — | 75.4% → 21.2% |
| Children below 30 days of basic living | — | 62.3% → 14.1% |
| Children in households with too little wealth (last year) | — | 72.8% → 47.9% |
| Single parents below the cost of living | — | 90.6% → 53.3% |
| Couples with children below the cost of living | — | 63.4% → 15.4% |
| Cost per adult a year | $29,168 | $33,743 |
| Price rise a year | 37.2% | 33.9% |

**Adverse and Stress Test environments (households with ageing; adults alone in brackets)**

| Measure | Adverse | Stress Test |
|---|---|---|
| Adult-years below the cost of living | 76.1% → 27.5% (adults alone 81.2% → 41.4%) | 76.1% → 58.4% (81.2% → 70.7%) |
| Adults with too little wealth at the end | 81.0% → 75.0%, better (85.8% → 88.8%, worse) | 81.0% → 89.1%, worse (85.8% → 91.9%, worse) |
| Children below the cost of living | 88.4% → 40.7% | 88.4% → 70.7% |

**What stands out**

1. **The household results hold up when families live through the run.** Children below the cost of living fall from 74% to 28% in Reference (24% when families were kept as drawn), and by about half in Adverse. As before, couples with children gain the most and single parents remain the hardest case.
2. **In the Adverse environment the wealth result is better than no programme for households (−5.9 points) and worse for adults alone (+2.9).** This is the same pattern as with families kept as drawn. In the Stress Test both are worse.
3. **Estates matter, but not much over 20 years.** Passing estates to partners and children lowers the share of adults with too little wealth by about 0.8 point in Reference, with and without the programme alike. With the programme, about two-thirds of what people leave goes to a partner and under 1% to children in the model; about a third leaves the model (people with no partner and no grown child in the model, and the shares of children under 18). Over 40 years, when more children grow up inside the model, this should matter more.
4. **The families drift a great deal over 20 years, and that is a limit of this reading, not a finding about the programme.** The plan keeps couples as first drawn this round: no one forms a new couple and no one separates. With ageing on, that matters. Here is how the families change (an average over the runs, the same with and without the programme):

| | Year 1 | Year 7 | Year 19 |
|---|---|---|---|
| Women up to 49 with a partner (per 500 adults) | 98 | 74 | 12 |
| Women up to 49 without a partner | 62 | 60 | 57 |
| Births a year | 7.3 | 3.6 | 2.0 |
| Share of births to women without a partner | 27% | 42% | 98% |
| Children | 185 | 149 | 55 |

   The starting couples grow past the age of having children, and every newcomer arrives single, so births fall and more of them are to women on their own. Part of this is the ageing reading itself: only deaths are replaced, so the population grows older (average age 45 at the start, 57 at the end; 29% retired by the end).

   So the children's figures for later years describe the families first drawn, followed over time, not a typical American population in those years. The figures for the first years, and those added up over all years, are the more reliable ones. Fixing this needs couples forming and separating at rates from data, which I have recorded as a candidate for a later round.

## Decisions made (full reasons in `dev/DECISIONS.md`, Session 39)

- A child stops being a dependant at 18. From 18 to 24 they are outside the model; at 25 they can enter as an adult. The model has no wages or costs for 18-to-24-year-olds, and by the Census most young adults have left home by their mid-twenties.
- A grown child takes the place of an adult who has died; an unrelated newcomer comes only when no grown child is waiting. The population stays the same size, as in v5.2's ageing reading. A grown child starts with the same chances as any newcomer: the model does not pass earnings from parents to children, a stated limit.
- Birth rates are the 2024 national rates by age, adjusted for having a partner or not from Census figures. Partners' ages use the Census age gap between spouses.
- Children whose last parent dies leave the model.
- Estates follow your decision, with the details above.

## Claude's reading of the design (please check)

- **Acre Equity passes to heirs without being sold.** Your paper says "Inheritance Rights: Intergenerational wealth transfer without market exposure". I read that as: an heir who lives in community housing keeps the equity as equity; an heir outside it receives the part members can take in cash, and the rest stays with the community trust.
- **A child's share of an estate counts even when the child leaves the model.** Equal shares go to every child, so a child under 18 whose last parent dies takes their share with them.

## What you need to do

Nothing yet: this is one step of v5.3, which arrives as one pull request. Please say if either reading above is not what you intend.

The runs and their exact commands are in `dev/runs/life-check-ref.json`, `-adv.json` and `-st.json` (`node dev/tools/life_check.js ENV 500`).
