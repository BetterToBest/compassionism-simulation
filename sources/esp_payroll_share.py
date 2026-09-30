"""Session 18 (s38): the ESP payroll share (lambda) and the ESP workforce share, derived from primary sources.

lambda = the share of an essential service provider's revenue paid as compensation of employees, weighted by the model's
essentials mix (CFG.BASKET: food 0.0901, housing incl. utilities 0.2761, medical 0.0685).
Source: BEA GDP-by-industry, 2024 values. Session 18 read the release of June 25, 2026 (lambda 0.15 / 0.20 / 0.26). BEA's annual
update, published September 30, 2026, revised the industry ratios (grocers 0.396 to 0.378, other real estate 0.070 to 0.076,
utilities 0.161 to 0.171); session 19 re-ran this script on it: lambda 0.152 / 0.203 / 0.263 (2024 values) and 0.149 / 0.203 / 0.263
(2025 values, now published). The central value the harness uses, 0.20, is unchanged. The script reads BEA's current release, so its
per-industry ratios move with BEA's revisions:
  gross output  https://apps.bea.gov/industry/Release/XLS/GDPxInd/GrossOutput.xlsx  sheet TGO105-A
  compensation  https://apps.bea.gov/industry/Release/XLS/GDPxInd/ValueAdded.xlsx   sheet TVA113-A
Caveat: BEA measures retail gross output as the margin, not sales, so the grocer ratio overstates compensation per dollar of
sales; the range below therefore leans high.

ESP workforce: BLS CES Table B-1, August 2026 (preliminary, seasonally adjusted), https://www.bls.gov/news.release/empsit.t17.htm
(read in-session on Sep 30, 2026; the figures are typed in below because the BLS site refuses scripted downloads).
"""
import urllib.request, openpyxl, io

def sheet(url, name):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    wb = openpyxl.load_workbook(io.BytesIO(urllib.request.urlopen(req).read()), read_only=True, data_only=True)
    return list(wb[name].iter_rows(values_only=True))

go_rows = sheet('https://apps.bea.gov/industry/Release/XLS/GDPxInd/GrossOutput.xlsx', 'TGO105-A')
va_rows = sheet('https://apps.bea.gov/industry/Release/XLS/GDPxInd/ValueAdded.xlsx', 'TVA113-A')
gi, ci = list(go_rows[7]).index('2024'), list(va_rows[7]).index('2024')
GO = {str(r[1]).strip(): r[gi] for r in go_rows if r[1]}
COMP = {}
for k, r in enumerate(va_rows[:-1]):
    nxt = va_rows[k + 1]
    if r[1] and nxt[1] and str(nxt[1]).strip() == 'Compensation of employees':
        COMP[str(r[1]).strip()] = nxt[ci]

def ratio(*inds):
    return sum(COMP[i] for i in inds) / sum(GO[i] for i in inds)

r = {k: ratio(k) for k in ['Food and beverage stores', 'Food services and drinking places', 'Housing', 'Other real estate', 'Utilities']}
r['Health care'] = ratio('Ambulatory health care services', 'Hospitals', 'Nursing and residential care facilities')
for k, v in r.items():
    print(f'{k:36s} compensation / gross output, 2024: {v:.3f}')

W = {'food': 0.0901, 'housing': 0.2761, 'medical': 0.0685}
ess = sum(W.values())
def lam(food, housing, medical):
    return (W['food'] * food + W['housing'] * housing + W['medical'] * medical) / ess
lo = lam(r['Food services and drinking places'], r['Housing'], r['Health care'])
mid = lam(r['Food and beverage stores'], r['Other real estate'], r['Health care'])
hi = lam(r['Food and beverage stores'], r['Utilities'], r['Health care'])
print(f'\nlambda: low {lo:.3f} (food services; housing at BEA Housing), central {mid:.3f} (grocers; housing at other real estate), high {hi:.3f} (grocers; housing at utilities)')

# BLS CES Table B-1, Aug 2026 (p), seasonally adjusted, thousands
total = 159075
narrow = {'Food and beverage retailers': 3249.9, 'Utilities': 611.7, 'Real estate': 1843.7, 'Health care': 18520.7}
wide = dict(narrow, **{'Food services and drinking places': 12426.8})
print(f'ESP workforce share: narrow {sum(narrow.values())/total:.4f}, wide {sum(wide.values())/total:.4f}')
