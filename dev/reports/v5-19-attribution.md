# What each part of the design does

Oct 7, 2026 · v5.3, plan item B9 · Claude · 500 paired runs in each of the three environments, 20 years · on the v5.3 main result (households and children, the Hub's full list of what BU buy, starting wealth from the survey, spending that follows income)

## What was asked

Until now the page said its readings were "not an attribution": it could show how the result moves when one part is read differently, but not how much of the result each part of the design produces. The plan asked for that: take each part out in turn, on the same 500 runs, and publish what each part adds, with its uncertainty.

## How it was measured

For each part, the model runs the main result twice on the same 500 sets of random draws: once with every part (the main result) and once with that one part taken out. The difference, run by run, is what the part adds. The 95% intervals are narrow (most within ±0.3 point), so the differences below are not luck.

Parts work together, so what they add one at a time does not sum to what the whole programme does. The gap is reported as the interaction. A part that leans on another part (for example, conversion needs BU to convert) shows its effect in both.

## The whole programme (Compassionism against no programme, 20 years)

| | Reference | Adverse | Stress Test |
|---|---|---|---|
| Adult-years below the cost of living | −28.3 points | −38.4 | −15.5 |
| Adults with too little wealth at the end | +5.5 points (worse) | +40.6 (worse) | +37.5 (worse) |
| Children below the cost of living | −43.3 points | −40.0 | −14.8 |
| Programme inflation | 47.9% a year | 61.5% | 28.5% |
| Cost per adult a year (today's dollars) | $31,366 | $29,567 | $12,177 |

## What each part adds (Reference)

Negative means the part lowers the share below the line (it helps); positive means it raises it.

| Part (taken out in turn) | Below the cost of living | Too little wealth | Children below the cost of living | Inflation a year |
|---|---|---|---|---|
| The BU allowance itself (no BU at all) | −26.0 | +6.1 | −40.8 | +47.9 |
| Conversion (BU become dollars at earned rates) | −11.6 | −5.4 | −21.9 | +20.7 |
| The premium split (instead of the premium going to every adult by wages) | +1.9 | +7.0 | −1.0 | +4.6 |
| Joining and leaving (instead of participation fixed as first drawn) | −2.6 | −0.5 | −8.2 | +3.5 |
| Zone coordination and the civic portal (SZH, CIP) | −1.1 | −4.3 | −1.6 | −0.9 |
| The production side (new capacity and creative output counted as backing) | −0.4 | −3.3 | −0.8 | −3.7 |
| Project hiring (instead of the earlier rule for directing expired BU) | −0.6 | −2.9 | −0.9 | −2.1 |
| Octave advancement | −0.1 | −1.9 | −0.5 | 0.0 |
| Community housing (PTH) | −0.3 | −0.2 | −0.4 | −0.3 |
| Community businesses (PTF) | +0.2 | +1.0 | +0.4 | −0.6 |
| The essential businesses' payroll (ESP) | +0.9 | +0.1 | +1.1 | +0.3 |
| The spending layer (jobs from programme spending in recessions) | 0.0 | 0.0 | 0.0 | 0.0 |
| *Interaction (the whole minus the sum of the parts)* | *+11.4* | *+9.9* | *+31.2* | *−21.3* |

**Adverse and Stress Test, in short.** The same two parts lead. The BU allowance accounts for nearly everything (Adverse: −37.5 on the cost of living, +39.1 on too little wealth; Stress: −15.2 and +36.6). Conversion helps on the cost of living in both (−17.8 and −8.4). It lowers too little wealth in Adverse (−5.7) and raises it in the Stress Test (+7.6). The premium split again worsens every adult measure (Adverse +9.5 on too little wealth). The spending layer, which acts only in recessions, now helps a little (Adverse −1.2 on the cost of living).

## What this means

1. **The BU allowance is the programme.** Take it away and almost nothing is left, because the other parts run on BU: businesses convert the BU they accept, and expired BU fund projects. Its effect on the cost of living (−26 points in Reference, −41 for children) is nearly the whole programme's. So is its effect on prices: all the programme's inflation goes with it.
2. **Conversion is the second engine.** It adds about 12 points of the fall in adults below the cost of living, and about 22 of the children's. It causes about 40% of the programme's inflation (20.7 of 47.9 points a year in Reference). Yet in Reference and Adverse it leaves fewer adults with too little wealth, because the dollars it pays become savings.
3. **The premium split is the one part that makes the adults' results worse.** Without it, the premium the essential businesses earn on converting BU goes to every adult in proportion to their wage (the model's earlier rule). With it, the premium goes to lower prices for BU customers, to new capacity and to a profit share for participating workers. In Reference, adults with too little wealth rise by 7 points, prices rise 4.6 points a year faster, and the real resources of adults who do not take part fall by about $9,500 a year: they lose their wage share of the premium and pay the higher prices. Children are a point better off. This is the split as the design describes it. I note it for the next model round, which will look at how the split's price cuts and reinvestment feed into prices.
4. **The small parts do what they say, and little more.** Zones and the civic portal, the production side, project hiring and octave advancement each lower too little wealth by about 2 to 4 points: the production side and project hiring by slowing prices (new output backs part of the Source's payout), zones and octaves by raising what participants earn and keep. Community housing and community businesses move results by about a point or less in this model, which has no places: they are national averages here. The spending layer does nothing in Reference, which has no recessions.
5. **The parts overlap a great deal.** The interaction is large (+31 points for children in Reference): the BU allowance and conversion each claim much of the same effect, since conversion needs BU. Read each row as "what the result loses without this part", not as a share of the whole.

## Who gains (real resources a year against no programme, Reference)

The whole programme: adults who take part +$26,137, adults who do not +$11,072, the poorest third by starting wage +$22,448, the richest third +$23,439. Conversion carries half to two-thirds of each group's gain. The premium split takes about $9,000 a year from adults who do not take part and from the richest third, and $2,900 from participants, compared with paying the premium out by wages.

## Claude's reading of the design (please check)

- **Taking a part out means the model's next-simplest version of it**, not a different design. Without project hiring, expired BU still fund projects by the earlier rule; without the premium split, the premium is paid out by wages; without joining and leaving, participation stays as first drawn. These are modelling choices, labelled where they appear.
- **Three labels were corrected before publishing.** My first wording said "BU only expire and are converted", "expired BU are destroyed" and "businesses keep the premium". Checking each against the engine showed what the switches really do, as described above. The runs did not change; only the words did (recorded in `dev/DECISIONS.md`).

## How it was checked

- Each parts-removed run differs from the main result in that one part only (a unit test checks this).
- The "whole programme" row equals the main result's change against no programme in the separate backing-sweep runs to the last published digit, in all three environments (too little wealth: Reference +5.51, Adverse +40.57, Stress +37.50; inflation 47.9%, 61.5%, 28.5%).
- Each label was checked against what the engine does when the part is taken out (three were corrected, above).

## What you need to do

Read it, and say if any part is described in a way your design does not intend. The figures will appear on the simulation page under "What each part does" and in the findings explorer, once the v5.3 restudy is complete.

The runs and their exact commands: `dev/runs/v53/attrib-check-ref.json`, `-adv.json` and `-st.json` (`node dev/tools/attrib_check.js ENV 500 20`, from commit 289e723).
