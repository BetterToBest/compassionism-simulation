"""v5.4 item 2 (Oct 7, 2026; dev/reports/v5-21-v54-design.md, 1.1): occupations as the common cause of pay and automation risk (harness.js CFG.EMPL_OCC).

Source: the file sources/fo_risk_wage.py reads (Frey and Osborne's probabilities for 702 occupations with May 2016 BLS OES employment and median annual
wages; plotly/datasets job-automation-probability.csv, retrieved Oct 7, 2026). Occupations with a wage and employment (700, 130.3 million jobs) are sorted
by median wage; the table gives each one's cumulative employment share (the top of its band, 0-1), its probability and its log median wage, so an adult at
employment quantile q of the pay ranking holds the first occupation whose cumulative share reaches q. It also prints the employment-weighted variance of
log median wages across occupations (the between-occupation part of the spread of log pay), which the engine compares with its own population's spread.

Usage: python3 sources/fo_occupations.py   (prints the JavaScript constant; needs pandas and numpy)
"""
import io, json, urllib.request
import numpy as np, pandas as pd
URL = 'https://raw.githubusercontent.com/plotly/datasets/master/job-automation-probability.csv'
d = pd.read_csv(io.BytesIO(urllib.request.urlopen(URL, timeout=60).read()))
for c in ('median_ann_wage', 'employed_may2016', 'prob'):
    d[c] = pd.to_numeric(d[c].astype(str).str.replace(',', ''), errors='coerce')
d = d.dropna(subset=['median_ann_wage', 'employed_may2016', 'prob']); d = d[(d.median_ann_wage > 0) & (d.employed_may2016 > 0)]
d = d.sort_values(['median_ann_wage', 'prob']).reset_index(drop=True)
w = d.employed_may2016.values.astype(float); lw = np.log(d.median_ann_wage.values); cum = np.cumsum(w)/w.sum()
m = (w*lw).sum()/w.sum(); vb = (w*(lw - m)**2).sum()/w.sum()
print('%d occupations, %.1f million jobs; between-occupation variance of log median wage %.4f (sd %.4f); employment-weighted mean probability %.4f'
      % (len(d), w.sum()/1e6, vb, vb**0.5, (w*d.prob.values).sum()/w.sum()))
print('CFG.EMPL_OCC = ' + json.dumps({'vb': round(vb, 5), 'cum': [round(x, 5) for x in cum], 'p': [round(x, 3) for x in d.prob.values]}, separators=(',', ':')) + ';')
