# v5.2.1, the visual suite: a report for Duke

October 6, 2026 · Claude · pull request from `claude/happy-faraday-cdq3ta` into `main` (merging it is the release)

## In one paragraph

Nothing the model says has changed: every figure is exactly the v5.2 figure, and a new check proves it on every page. What changed is how the findings are shown. The simulation page now leads with three plain numbers and walks a reader through eight short sections, from "the answer in ten seconds" to "run it yourself". A new page, the findings explorer, holds every chart and table, release by release, with downloads. The replication page now opens with what is being replicated and how to reproduce it, and keeps only a five-line summary of the findings with a link to the explorer. Behind all three pages sits one data file per release, so the next version (and the compare page) only adds data.

## What to look at first

1. **The simulation page, below the introduction.** The strip under the section menu changes the environment, 20 or 40 years, and whether the big numbers show the run with Compassionism or the run with no programme. Try "Meet the adults": every mark is one of the 500 simulated adults in one run, with and without the programme; drag the year, or click an adult to follow their life.
2. **The findings explorer** (`findings.html`, linked from all three pages). Three cards first, then a guided read of each result (a chart, "how to read this", "what it does not show"), then every table with CSV and JSON downloads. The release menu now also offers v5.1, v5.0.1 and v5.0, because their figures were rebuilt from their tags and came out identical to what was published.
3. **The replication page's top.** "What is being replicated" (the five parts in one line each, the runs, the measures), then "Reproduce the figures", then "Current findings" (five lines and a button to the explorer), then the method sections as before. The version history is now a timeline of collapsed panels, with the v5 releases added. Any old link to a table that moved (for example `replication.html#backing-share`) now opens the same table on the explorer.

## Four choices that change what the pages say (each applied as recommended; you can change any of them)

1. **The three headline numbers** are the three poverty measures the page already led with: below 30 days of basic living, below the cost of living, and too little wealth. The price rise, the cost and the "every dollar backed" result sit on one line directly under them. Where the programme does worse than no programme (too little wealth in the Adverse and Stress environments), the card turns red and says "Worse". *Alternatives:* swap one card for the price rise; four cards.
2. **"What each part does" is not an attribution.** You asked for the attribution chart as an explainer. That chart belongs to the earlier engine; the release has never run "each part removed in turn", and running it now would add new figures to a release that promises none. So each part has a card (what it does, the evidence, its limit) and the readings that already test it, labelled "not an attribution". *Recommended next:* run the attribution study in the next model round. *Alternative:* run it now as new figures.
3. **An old headline strip moved.** The top of the replication page showed the earlier engine's figures (15.3% too little wealth, from a 5,000-agent study) under the heading "Current headline figures, v5.2". They were not the release results. They now sit in the version history with an honest label. *Alternatives:* keep both; leave it.
4. **The five-line summary on the replication page** is written from the numbers: each sentence (which environments do worse on savings, which measures meet the Hub's Year 7 target) is chosen by the data, so a later release that changes a result changes the sentence.

## What did not change

The engine, the main result, every reading, every 500-run figure and the walk-through video (its pictures still show the v5.2 layout; your decision d151 keeps the video for the next model round). The earlier-engine page is unchanged. All your design wording ("What Compassionism is", the attribution paragraph, "Limits, in short", the glossary, the headline sentence) is where it was.

## How it was checked

- The three checks pass: `validate`, `unit` (171 tests) and `domtest` (124 checks, 11 of them new).
- The new check compares every number on the three pages with the data file: the text that shows without JavaScript, the simulation page in all six views (three environments at 20 and 40 years), and the explorer for all four releases, about 16,000 numbers. It also fails if anyone types a percentage or dollar figure into the new sections by hand, and if any of the 178 links into the pages that existed at v5.2 stops working.
- The extra data the sections draw (the spread across the 500 runs, and one run's 500 adults) was read from the same runs with the engine untouched; the tool refuses to write unless its yearly averages equal the published ones, and they did, in every environment and horizon.
- Looked at on a phone width (390 px) and a desktop width (1280 px), in light and dark, with no sideways scrolling; gone through by keyboard alone (every stop shows a focus ring; each chart is one stop, with the arrow keys moving inside it); with reduced motion on (the counters and the "play the years" button do not animate). Colours were checked for colour-blind readers, and every chart also uses shapes, labels and a table, never colour alone.

## Limits worth knowing

- The "spread across runs" band and "Meet the adults" load from the site when their section comes into view. Opened as a file on a computer, the page still shows every result and runs the model, but those two parts need the page served from a website (the live site is fine).
- "Meet the adults" shows one run (the first of the 500) to make the averages concrete; one run varies more than the averages, and the page says so.
- "Who gains" shows how savings shift at each tenth of the adults. In the main reading the top tenths end with less savings in today's money than with no programme, because prices rise and savings in the model earn nothing; the page says this in words, from the numbers.

## Project context box

I cannot see the files in your claude.ai project's context box, so this is the rule to apply: remove anything this round replaces or makes stale, keep the kit.
- **Remove:** the v5.2 round prompt and any older round prompts; copies of `replication.html`, `index.html` or the v5.2 replication tables (the explorer replaces them); older ledger exports (the ledger artifact is the record); any `apply-*.zip` or bundle from earlier sessions.
- **Keep:** `CLAUDE.md`, `dev/PROGRESS.md`, `dev/PLAN.md`, `dev/DECISIONS.md` if you keep them there; and add this round's prompt only if you want a template for the compare page round.

## What is next

The compare page (ledger s95): Compassionism against current US policy and other designs on the same simulated people, built on the same charts and data format. Then children and households.
