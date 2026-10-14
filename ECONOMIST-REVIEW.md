# Economist review checklist

One page for an independent economist. Each row names one thing to check, where it is in the repository, and what the model does today. Mark each row agree, disagree or cannot tell, with a line of why. You need not do every row. Rows about what the framework means (as opposed to how it is modelled) belong to its author, Duke Johnson; say so in a comment.

Send it by opening an issue with the "Economist review" template (Issues, New issue), or by a comment on the pull request or discussion where you found the model.

| # | Check | Where | What the model does today | Agree / disagree / cannot tell, and why |
|---|---|---|---|---|
| 1 | CCO (Creative Currency Octaves) cost relief has no source (20% of the basket at the reference BU, ceiling 50%) | index.html: CCO_RELIEF_AT_REF, CCO_RELIEF_CAP; dev/runs/unsourced-constants-check.txt | Earlier engine only. Raising it left every released row unchanged. Is that right, and is there a source or a range worth sweeping? |  |
| 2 | Inflation damping by community businesses (PTF, which cut prices) and community housing (PTH) has no source: how much of outside inflation they absorb, applied to the overall inflation rate (0.5 and 0.1 times the share who joined) | index.html: grep "inflRate*=(1-"; dev/runs/unsourced-constants-check.txt | Off in every main row; on only in one optional row. Is a source known for its size? |  |
| 3 | The income effect on earnings (how far people cut paid work when given money; sourced range 0.05 to 0.30) | dev/reports/v5-30-s137-results.md, section 8; dev/DECISIONS.md | The one uncertain behavioural constant that matters for basket poverty. Is the range right for a payment of this size and kind? |  |
| 4 | One wage elasticity for every change in the return to work | dev/DECISIONS.md (fairness rule) | Every change in the return to work uses the same elasticity. Is that the right treatment? |  |
| 5 | The share of extra cash spent (from the range of the US saving rate in recent years) | dev/reports/v5-30-s137-results.md, section 8 | Drives the "too little wealth" result more than any other input. Is the range right? |  |
| 6 | Participation and the amount of BU (Basic Units) paid are design choices, not facts about the world | study.html, "What the results depend on" | They explain most of the spread in poverty, cost and inflation. What take-up should be assumed, and on what evidence? |  |
| 7 | The price rule: how programme spending and extra demand raise prices | dev/reports/v5-30-s137-results.md, section 6; dev/DECISIONS.md | Not calibrated to outside evidence on benefit-funded demand. The "too little wealth" rise comes through it. Which evidence would calibrate it? |  |
| 8 | Single-payer savings come from one preprint that is not peer reviewed | study.html, "Single payer depends on the Yale preprint" | Central, cautious and high-cost cases are run. Are these the right cases? |  |
| 9 | The cost-of-living line is the unweighted state average | dev/reports/v5-30-s137-results.md, section 9 | A population-weighted line is a known later fix. How much would it matter? |  |
| 10 | Every gain is confirmed on basket poverty (below the cost of living) and on wealth poverty (too little wealth), not on one measure | study.html; findings.html | Compassionism lowers basket poverty and raises "too little wealth". Is the way both are reported fair? |  |
| 11 | The no-programme run against US data (poverty, debt, savings) | findings.html; dev/DECISIONS.md | Which gaps with US data would change a conclusion, and which would not? |  |
| 12 | Tax revenue is not reconciled with today's safety-net outlays or government's share of the plan | dev/reports/v5-30-s137-results.md, section 9 | The model reports these costs; it does not show they are financed. Is that an acceptable limit, stated this way? |  |

Everything on the pages comes from files you can run: `node harness.js validate`, `unit`, `domtest`; the 500-seed figures are in `data/`. The study page (`study.html`) names what the results depend on and the two constants with no source.

---

The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book *Better To Best* and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome.
