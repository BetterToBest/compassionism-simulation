"""v5.4 item 2 (Oct 7, 2026; dev/reports/v5-21-v54-design.md, 1.1): the job-loss constants of the EMPL switch (harness.js CFG.EMPL_*).

Sources (BLS Current Population Survey, monthly, seasonally adjusted, via FRED; retrieved Oct 7, 2026 from fred.stlouisfed.org/graph/fredgraph.csv?id=...):
  UNEMPLOY      unemployed (thousands)                 UEMPLT5, UEMP5TO14, UEMP15T26, UEMP27OV   unemployed by weeks out of work so far
  CE16OV        employed (thousands)                   LNS13023621 job losers, LNS13023705 job leavers, LNS13026638 permanent job losers
  CCSA          continued claims for unemployment insurance (weekly)
and the Department of Labor's UI Data Summary (oui.doleta.gov/unemploy/data_summary/SummaryTables.pdf, the four quarters to 2026 Q2): average weekly benefit
$500.61; covered wages $3,138,452,945 thousand and covered employment 155,046 thousand for 2025 Q4 (the summary's wage table), so an average weekly wage of
3,138,452,945 / 155,046 / 13 = $1,557 and a replacement of 500.61 / 1,557 = 0.321.

Method (steady state, each period's monthly averages):
  - Inflow: people out of work fewer than 5 weeks are the last 5 weeks' entrants, so weekly inflow = UEMPLT5 / 5. Only job losers and job leavers come
    from a job (re-entrants and new entrants come from outside the labour force, which the model does not have): inflow x (losers + leavers) / unemployed.
    The yearly chance of entering = 1 - exp(-52 x weekly inflow / employed).
  - Spell lengths: in a steady state the number out of work for d weeks so far is the inflow times the share of spells lasting at least d weeks, S(d).
    So the stock per week of each duration band, over the inflow, reads S at the band's middle (2.5, 9.5, 20.5 weeks); S is linear between those points
    log-linear between those points (S = 1 up to 2.5 weeks), and beyond 20.5 weeks the spells end at a constant rate set so the
    27-weeks-and-over stock matches.
  - Permanent losses: permanent job losers / (losers + leavers): those who come back at lower pay (temporary layoffs and quits do not).
  - UI recipiency: continued claims / unemployed.
Periods: 'normal' = 2015-2019 and 2022-2025 (the pandemic years left out); 'recession' = 2009-2010 (the Great Recession's high-unemployment years).

Usage: python3 sources/unemp_flows.py   (downloads nine small CSV files; needs only the standard library)
"""
import csv, io, math, urllib.request
S = ['UNEMPLOY', 'CE16OV', 'UEMPLT5', 'UEMP5TO14', 'UEMP15T26', 'UEMP27OV', 'LNS13023621', 'LNS13023705', 'LNS13026638', 'CCSA']
def get(s):
    u = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s&cosd=2000-01-01&coed=2025-12-31' % s
    r = csv.reader(io.StringIO(urllib.request.urlopen(u, timeout=60).read().decode())); next(r)
    out = {}
    for d, v in r:
        try: x = float(v)
        except ValueError: continue
        out.setdefault(d[:7], []).append(x)
    return {k: sum(v)/len(v) for k, v in out.items()}  # monthly (CCSA is weekly: the month's mean)
D = {s: get(s) for s in S}
PER = {'normal': [y for y in range(2015, 2026) if y not in (2020, 2021)], 'recession': [2009, 2010]}
def avg(s, yrs):
    v = [x for k, x in D[s].items() if int(k[:4]) in yrs]; return sum(v)/len(v)
res = {}
for name, yrs in PER.items():
    U, E = avg('UNEMPLOY', yrs), avg('CE16OV', yrs)
    b = [avg(s, yrs) for s in ('UEMPLT5', 'UEMP5TO14', 'UEMP15T26', 'UEMP27OV')]
    ll = avg('LNS13023621', yrs) + avg('LNS13023705', yrs)
    inflow = b[0]/5                                   # all entrants a week
    S1, S2 = (b[1]/10)/inflow, (b[2]/12)/inflow        # S at 9.5 and 20.5 weeks
    # S is log-linear between (2.5, 1), (9.5, S1) and (20.5, S2), and beyond 20.5 falls at a constant rate 1/tau, with tau set so the stock out of work
    # 27 weeks or more matches: stock27 / inflow = integral of S from 26.5 on = S2 x exp(-6/tau) x tau (solved by bisection).
    def Sat(d):
        if d <= 2.5: return 1.0
        if d <= 9.5: return math.exp(math.log(S1)*(d - 2.5)/7)
        return math.exp(math.log(S1) + (math.log(S2) - math.log(S1))*(d - 9.5)/11)
    tgt, lo, hi = b[3]/inflow, 0.1, 500.0
    for _ in range(200):
        tau = (lo + hi)/2
        if S2*math.exp(-6/tau)*tau < tgt: lo = tau
        else: hi = tau
    S5, S15, S27 = Sat(5), Sat(15), S2*math.exp(-6/tau)
    tailMean = tau                                     # mean weeks beyond 26.5 (constant rate)
    pEnter = 1 - math.exp(-52*inflow*ll/U/E)
    print('%-9s CFG: S(9.5) %.4f, S(20.5) %.4f, tau %.2f weeks' % (name, S1, S2, tau))
    res[name] = dict(pEnter=pEnter, S5=S5, S15=S15, S27=S27, tailMean=tailMean, perm=avg('LNS13026638', yrs)/ll,
                     recip=avg('CCSA', yrs)/1000/U, urate=U/(U + E), meanSpell=U/inflow)
    print('%-9s yearly chance of losing or leaving a job into unemployment %.4f; share of spells lasting 5+ weeks %.3f, 15+ %.3f, 27+ %.3f; '
          'mean weeks beyond 26.5 %.1f; permanent share %.3f; UI recipiency %.3f; (check: unemployment rate %.3f, mean spell %.1f weeks)'
          % (name, pEnter, S5, S15, S27, tailMean, res[name]['perm'], res[name]['recip'], res[name]['urate'], res[name]['meanSpell']))
print('UI replacement (DOL, average weekly benefit / average weekly covered wage): %.3f' % (500.61/(3138452945/155046/13)))
