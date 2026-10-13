#!/bin/bash
# Usage: dev/tools/s137_jobs.sh WORKTREE OUTDIR [--max-hours=H]   (WORKTREE: a clean worktree of the commit; OUTDIR outside it)
# Ledger step s137 (dev/reports/v5-29-outside-audit.md): the Runpod study in resumable pieces, one per core (JOBS=N overrides), longest first; a finished
# piece (its file in OUT) is skipped on a rerun. --max-hours=H: launch nothing new after H hours and stop the running pieces then.
# ON_DONE=CMD: run "CMD FILE..." after each finished piece. When every piece is in, the health pieces are merged (health_check.js --merge).
#  - sensitivity: Morris (20 trajectories) in each environment on two seed blocks (1-10, 11-20), joined with the noise check; Sobol in Stress on v5.4's leaders
#  - the health financing table: the grid with today's safety net plus the audit's rows, 500 seeds in 20 pieces per environment
#  - the safety net's price channel: the grid with prices flat and with every price response 1.5 times, 500 seeds in 4 pieces per environment
W=$1; OUT=$2; MAXH=; for a in "${@:3}"; do case $a in --max-hours=*) MAXH=${a#--max-hours=};; esac; done
cd "$W" || exit 1; P=${JOBS:-$(nproc)}; END=; [ -n "$MAXH" ] && END=$(( $(date +%s) + $(awk "BEGIN{print int($MAXH*3600)}") ))
TROWS=SN,BSNfl,CSNfl,ASNpv,BSNpv,CSNpv,BSNcau,BSNhigh,CSNcau,CSNhigh,CSNp25,CSNp75,CSNx0,CSNg8,CSNx26,ASNtLo,ASNtHi
J=("sobol st")
for e in ref adv st; do for lo in 1 11; do J+=("morris $e $lo"); done; done
for e in ref adv st; do for lo in 1 126 251 376; do J+=("hc flat $e $lo 125" "hc thx $e $lo 125"); done; done
for e in ref adv st; do for i in $(seq 0 19); do J+=("hc table $e $((i*25+1)) 25"); done; done
run(){ set -- $1; local f r
  case $1 in
    sobol) f=$OUT/gsa-sobol-$2.json; [ -s $f ] && return
      node dev/tools/gsa.js sobol $2 64 10 --params=part,bu,rho,spend,payCut,bleiBonus --out=s137-sobol-$2 > $OUT/sobol-$2.log 2>&1 && mv dev/runs/v54/s137-sobol-$2.json $f;;
    morris) f=$OUT/gsa-morris-$2-lo$3.json; [ -s $f ] && return
      node dev/tools/gsa.js morris $2 20 10 --lo=$3 --out=s137-morris-$2-lo$3 > $OUT/morris-$2-lo$3.log 2>&1 && mv dev/runs/v54/s137-morris-$2-lo$3.json $f;;
    hc) local n=s137$2-p$4 hi=$(( $4 + $5 - 1 )) x=; f=$OUT/$n-$3.seeds.json; [ -s $f ] && return
      case $2 in flat) x=--flat;; thx) x=--thetaX=1.5;; table) x=--rows=$TROWS;; esac
      node dev/tools/health_check.js $3 $hi --grid $x --lo=$4 --out=$n --dump > $OUT/$n-$3.log 2>&1 && mv dev/runs/health/$n-$3.json $OUT/ && mv dev/runs/health/$n-$3.seeds.json $f;;
  esac; r=$?; echo "$* done $(date -u +%FT%TZ) exit $r" >> $OUT/status.txt
  [ $r = 0 ] && [ -n "$ON_DONE" ] && $ON_DONE "$f"; }
late(){ [ -n "$END" ] && [ $(date +%s) -ge $END ]; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD), $P at a time${MAXH:+, max $MAXH h}, ${#J[@]} pieces" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge $P ]; do late && break 2; sleep 5; done; late && break; run "$j" & done
while [ $(jobs -rp | wc -l) -gt 0 ]; do late && { pkill -f "dev/tools/(gsa|health_check).js"; echo "stopped at max-hours $(date -u +%FT%TZ)" >> $OUT/status.txt; break; }; sleep 5; done
wait; n=$(ls $OUT/gsa-sobol-*.json $OUT/gsa-morris-*-lo*.json $OUT/s137*-p*.seeds.json 2>/dev/null | wc -l)
if [ $n != ${#J[@]} ]; then echo "$n of ${#J[@]} pieces saved $(date -u +%FT%TZ)" >> $OUT/status.txt; exit 1; fi
ok=0   # every piece is in: join the Morris blocks and merge the health pieces (quick, one process each)
for e in ref adv st; do
  node dev/tools/gsa.js morrisjoin $e $OUT/gsa-morris-$e-lo1.json,$OUT/gsa-morris-$e-lo11.json --out=s137-morris-$e > $OUT/morrisjoin-$e.log 2>&1 && mv dev/runs/v54/s137-morris-$e.json $OUT/gsa-morris-$e.json || ok=1
  for k in flat thx table; do x=; case $k in flat) x=--flat;; thx) x=--thetaX=1.5;; table) x=--rows=$TROWS;; esac
    node dev/tools/health_check.js $e 500 --grid $x --merge=$(ls $OUT/s137$k-p*-$e.seeds.json | paste -sd,) --out=s137$k > $OUT/merge-$k-$e.log 2>&1 && mv dev/runs/health/s137$k-$e.json $OUT/ || ok=1; done
done
( cd $OUT && sha256sum *.json > SHA256SUMS )
[ $ok = 0 ] && echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt || echo "pieces done, a join or merge failed $(date -u +%FT%TZ)" >> $OUT/status.txt
[ -n "$ON_DONE" ] && $ON_DONE $OUT/gsa-morris-*.json $OUT/s137flat-*.json $OUT/s137thx-*.json $OUT/s137table-*.json $OUT/SHA256SUMS
exit $ok
