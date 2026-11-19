# Output per hour, automation and hours: the sources opened

Opened Nov 19, 2026, for the study of output per hour and automation (research-update `prereg/2026-11-s85-output-per-hour.md`; Claude's reading of the design: `dev/reports/s85-output-reading.md`). Each figure below was read on the page or in the paper's own text on that date. A figure marked *as quoted* was read in another opened paper that cites it, because its own page refused the request; it is context only and sets no engine value.

## Hours and output

| Source | What it says (quoted or read) | How the study uses it |
|---|---|---|
| Pencavel, "The Productivity of Working Hours", IZA Discussion Paper 8129 (2014); *Economic Journal* 125 (2015). Read in the paper's text. | Munition workers, most of them women, Britain, First World War. "Below 49 weekly hours, variations in output are proportional to variations in hours"; above 49, "output rises with hours at a decreasing rate and a maximum of output occurs at about 63 hours". | Main reading: shorter weeks below 49 hours bring no gain in output per hour; cutting hours cuts output in proportion. |
| Our World in Data, annual working hours per worker (Huberman and Minns 2005 to 1938; Penn World Table 11.0 from 1950). Full CSV downloaded; US rows in `s85_owid/us_hours.csv`; `s85_hours.py`. | US: 3,096 hours a year (1870), 2,938 (1900), 2,316 (1929), 2,022 (1950), 1,910 (1973), 1,888 (2000), 1,797 (2019), 1,789 (2023). Hours per worker fell 0.53% a year from 1870 to 1950 and 0.17% a year from 1950 to 2023. | Context: since 1950 about 8% of the rise in output per hour was taken as shorter hours, the rest as income. |
| US Bureau of Labor Statistics, Productivity and Costs, third quarter 2026 (preliminary). | Nonfarm business output per hour: "the long-term rate of 2.2 percent since the first quarter of 1947"; 1.5% a year over the 2007-2019 cycle; 2.2% a year since the end of 2019. | Context for the forecasts below; the engine's own baseline wage growth is unchanged. |

## Exposure to automation

| Source | What it says | How the study uses it |
|---|---|---|
| Eloundou, Manning, Mishkin and Rock, "GPTs are GPTs" (arXiv 2303.10130, v5, Aug 2023). Abstract. | "Around 80% of the U.S. workforce could have at least 10% of their work tasks affected"; "approximately 19% of workers may see at least 50% of their tasks impacted"; about 15% of all tasks could be done "significantly faster at the same level of quality", and "between 47 and 56% of all tasks" with software built on the models. | Places the displacement readings: exposure is not loss. |
| Cazzaniga and others, "Gen-AI: Artificial Intelligence and the Future of Work", IMF Staff Discussion Note SDN/2024/001. Full text. | "Almost 40 percent of global employment is exposed to AI"; "about 60 percent of jobs are exposed" in advanced economies, of which "about half may be negatively affected by AI, while the rest could benefit". | About 30% of jobs in advanced economies at risk of being harmed: the 30% reading's anchor. |
| Penn Wharton Budget Model, "The Projected Impact of Generative AI on Future Productivity Growth" (Sept 8, 2025). | "40 percent of current labor income is potentially exposed to automation by generative AI." | Context. |
| Frey and Osborne (2013; already in the engine, `CFG.EMPL_OCC`). | 47% of US employment in occupations with a computerisation probability above 0.7. | The engine's occupations and their automation risk: who is displaced first. |

## Output per hour: the forecasts

| Source | What it says | How the study uses it |
|---|---|---|
| Acemoglu, "The Simple Macroeconomics of AI", NBER Working Paper 32487 (2024); *Economic Policy* 40 (2025). Paper text. | Total factor productivity "no more than a 0.66% increase ... over 10 years" (under 0.53% with hard-to-learn tasks); GDP "around 1.1% over the next 10 years", "a lower estimate of 0.92%". AI "is predicted to widen the gap between capital and labor income". | The low reading of the gain: 0.1 points a year. |
| Penn Wharton Budget Model (Sept 2025). | Productivity and GDP "1.5% by 2035, nearly 3% by 2055, and 3.7% by 2075"; "a peak annual contribution of 0.2 percentage points in 2032". | Agrees with the low reading. |
| Goldman Sachs (Briggs and Kodnani, 2023), *as quoted* in Acemoglu (2024); its page refused the request. | "a 7% increase in global GDP ... and a 1.5% per annum increase in US productivity growth over a 10-year period". | The high reading of the gain: 1.5 points a year. |
| McKinsey Global Institute (2023), *as quoted* in Acemoglu (2024); its pages refused the request. | "the total impact of AI and other automation technologies could produce up to a 1.5 − 3.4 percentage point rise in average annual GDP growth in advanced economies over the coming decade". | Context: beyond the high reading. |
| Brynjolfsson, Li and Raymond, "Generative AI at Work", NBER Working Paper 31161; *Quarterly Journal of Economics* 140 (2025). Abstract. | Issues resolved per hour up "14% on average", "a 34% improvement for novice and low-skilled workers"; 5,179 customer support agents. | Context: one task, not the economy. |
| Humlum and Vestergaard, "Large Language Models, Small Labor Market Effects", NBER Working Paper 33777 (2025). Paper text. | "precise null effects on earnings and recorded hours ... ruling out effects larger than 2% two years after"; "2.8% time savings for the typical user". | Context: early effects in Denmark are near zero. |

## Who gains, and new work

| Source | What it says | How the study uses it |
|---|---|---|
| Acemoglu and Restrepo, "Automation and New Tasks", *Journal of Economic Perspectives* 33(2), 2019. Abstract. | "automation always reduces the labor share in value added and may reduce labor demand even as it raises productivity"; the slower growth of employment in the last three decades reflects stronger displacement and weaker reinstatement. | The dividend of automated work goes to owners in the main reading. |
| Acemoglu and Restrepo, "Robots and Jobs", NBER Working Paper 23285 (2017; *Journal of Political Economy* 2020). Abstract. | One more robot per thousand workers "reduces the employment to population ratio by about 0.18-0.34 percentage points and wages by 0.25-0.5 percent". | Context. |
| Autor, Chin, Salomons and Seegmiller, "New Frontiers: The Origins and Content of New Work, 1940-2018", NBER Working Paper 30389; *Quarterly Journal of Economics* 139 (2024). Paper text. | "The majority of current employment is found in new job specialties ('new work') introduced after 1940." | Why the displacement readings are net of new work, and why a low reading is kept. |
| Stansbury and Summers, "Productivity and Pay: Is the link broken?", NBER Working Paper 24165 (2017). Abstract. | One point more productivity growth goes with "0.7 to 1 percentage points higher median and average compensation growth" and "0.4 to 0.7 percentage points higher production/nonsupervisory compensation growth" (1973-2016). | The pass-through of the gain to wages: 0.7 (where the two ranges meet), with 0 and 1 swept. |

## Not opened yet (to open before any run, by a dated amendment)

- The share of US business and corporate equity held by US households, directly and through funds (the Federal Reserve's Financial Accounts, table B.101 and L.223, or Rosenthal and Burke 2020): the share of the automation dividend the model's households keep. Until then it is a design parameter, 1, swept at 0.5.
- The labour share of the nonfarm business sector (BLS): output per hour of programme work, as an hour's pay over the labour share.
- Output a year per dollar of fixed capital in the essentials industries (BEA fixed assets and value added by industry): PTF capital's yield, capped at the economy-wide 0.32 the backing study used.
