# s119 (with s37): the CoMSES model-library package and the wide-audience fact sheet

Prepared Oct 15, 2026 for a plain chat. Two documents are wanted: (1) the text for a CoMSES Net model-library submission (the owner submits it himself and can ask CoMSES for its peer review of the model, the closest available route to an independent review); (2) a one-page fact sheet for reporters and a general audience (also usable for a Show HN post).

## Facts to use (do not invent others)
- Name: Compassionism Framework Simulation, version 5.6.0, released Oct 14, 2026. Live page: https://bettertobest.github.io/compassionism-simulation/ · code: https://github.com/BetterToBest/compassionism-simulation · archive DOI https://doi.org/10.17605/OSF.IO/QWTE2. Code licence Apache-2.0; text CC BY 4.0.
- What it is: an open, in-browser agent-based model of the Compassionism framework (concepts by Duke Johnson, book *Better To Best*, Research Hub at https://bettertobest.github.io/research-hub/): 500 simulated US adults with households and children, followed for 20 years (and 40) in three environments (Reference, Adverse, Stress Test), once with no program and once with Compassionism, on the same simulated people, averaged over 500 paired runs; today's US safety net (SNAP with its work rule, the earned income tax credit, the refundable child tax credit) is in both arms.
- Attribution (use verbatim): "The math and code of this simulation were engineered by Claude, an AI model made by Anthropic, from the concepts in Duke Johnson's book Better To Best and his related vision for eradicating extreme poverty while enriching cultures and supporting human flourishing. The model has not yet been reviewed by an independent economist; the full code is open for anyone to check, and expert collaborators are welcome."
- Figures: take every number from `release-summary.json` (the release file's headline rows; each carries the file and key it came from). Quote the file and key beside each figure. Report the limits as prominently as the gains: in the safety-net comparison, poverty below the cost of living falls in every environment, but too little wealth at year 20 rises in all three, so there is no confirmed gain on every measure. The model measures poverty, cost and work only; it does not measure culture, creativity or wellbeing.
- Keywords for CoMSES: agent-based model, economic policy, poverty, universal basic income, basic income, social policy, simulation, microsimulation.

## CoMSES text needed
Short description (under 100 words), long description (follow the ODD: purpose, entities, process, design concepts, initialisation, input data, submodels; `ODD.md` is attached and already follows the protocol; shorten it, do not rewrite its claims), keywords, how to run (open `index.html` in a browser, or `node harness.js validate`), how to reproduce the 500-run results (see `REPRODUCE.md`), licence lines, limitations, and the request for peer review.

## Fact sheet needed (one page)
Plain words, no jargon. Sections: what it is; what it found (three to five figures, each with the file/key); what it cannot tell you; who made it and the AI attribution; how to check it yourself; contact (the GitHub issues page). End with a short "How not to misquote this" list.

## Rules
Never state a result the data file does not show. Do not use the words "proves" or "forecast". No bare labels such as step or decision numbers. When a figure is a model output, say "in the model". Mark anything you are unsure of with [CHECK] so the owner or Claude Code can verify it.
