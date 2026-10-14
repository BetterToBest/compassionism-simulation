#!/usr/bin/env python3
# Usage: python3 -I dev/tools/s165_verify.py OUTDIR   (OUTDIR: a copy of the results folder s165-5bf5bcc)
# Matches every output file to the job list of dev/tools/s165_jobs.sh (49 pieces) plus the six merged panels, and checks that each JSON
# records engine commit 5bf5bcc and a clean tree. Prints one line per file; exits 1 on any missing or mismatched file.
import json,os,sys
R=sys.argv[1]
J=[]
for e in 'ref adv st'.split():
  for i in range(6): J.append(('p40',f'release-panel-40-{e}.part{i}.json'))
for e in 'ref adv st'.split():
  for i in range(4): J.append(('p20',f'release-panel-{e}.part{i}.json'))
for e in 'ref adv st'.split():
  J.append(('bk',f'backing-share-{e}.json'))
  for y in (20,40): J.append(('iso',f'snap-iso-{e}-{y}.json'))
J.append(('hist','history-check.json'))
for e in 'ref adv st'.split(): J.append(('snt',f'sn-trace-{e}.json'))
for e in 'ref adv st'.split():
  for y in (40,20): J.append(('ex',f'explore-suite-{e}-{y}-snab.json'))
merges=[f'release-panel{s}-{e}.json' for e in 'ref adv st'.split() for s in ('','-40')]
allj=[f for k,f in J]+merges
print('job pieces',len(J),'+ merged panels',len(merges),'=',len(allj))
bad=0
for f in allj:
  p=os.path.join(R,f)
  if not os.path.isfile(p) or os.path.getsize(p)==0: print('MISSING',f); bad+=1; continue
  d=json.load(open(p)); m=d.get('_meta',{}).get('manifest',{})
  ok=m.get('commit','').startswith('5bf5bcc') and m.get('dirty') is False
  if not ok: print('BAD',f,m.get('commit'),m.get('dirty')); bad+=1
  seeds=d['_meta'].get('seeds') or d['_meta'].get('nSeeds') or d['_meta'].get('N')
  print(f'{f:40s} commit {m.get("commit","")[:7]} dirty={m.get("dirty")} seeds={seeds} args={str(d["_meta"].get("args") or d["_meta"].get("flags") or "")[:70]}')
extra=sorted(set(x for x in os.listdir(R) if x.endswith('.json'))-set(allj))
print('json files not in job list:',extra)
print("problems",bad); sys.exit(1 if bad else 0)
