#!/bin/bash
# Usage: dev/tools/s137b_jobs.sh WORKTREE OUTDIR [--max-hours=H]   (WORKTREE: a clean worktree of the commit; OUTDIR outside it)
# Ledger step s137, follow-up (dev/DECISIONS.md, Session 2f): the s137 Morris run named inputs in Stress that the first Sobol left out (tax, eps,
# pthUptake, maxMult, ptfOther), so Sobol in Stress on the union of Stress's Morris leaders (11 inputs), N=128 base points, 32 paired seeds in 16 blocks
# of 2 (one per core; JOBS=N overrides), joined with gsa.js sobjoin (bootstrap intervals). A finished block (its file in OUT) is skipped on a rerun.
# --max-hours=H: launch nothing new after H hours and stop the running blocks then. ON_DONE=CMD: run "CMD FILE..." after each finished block.
W=$1; OUT=$2; MAXH=; for a in "${@:3}"; do case $a in --max-hours=*) MAXH=${a#--max-hours=};; esac; done
cd "$W" || exit 1; P=${JOBS:-$(nproc)}; END=; [ -n "$MAXH" ] && END=$(( $(date +%s) + $(awk "BEGIN{print int($MAXH*3600)}") ))
PAR=part,bu,rho,spend,payCut,bleiBonus,tax,eps,pthUptake,maxMult,ptfOther; N=128; B=2; J=()
for i in $(seq 0 15); do J+=("$((i*B+1))"); done
run(){ local lo=$1 f=$OUT/gsa-sobol-st-lo$1.json r; [ -s $f ] && return
  node dev/tools/gsa.js sobol st $N $B --params=$PAR --lo=$lo --out=s137b-sobol-st-lo$lo > $OUT/sobol-st-lo$lo.log 2>&1 && mv dev/runs/v54/s137b-sobol-st-lo$lo.json $f
  r=$?; echo "sobol st lo$lo done $(date -u +%FT%TZ) exit $r" >> $OUT/status.txt
  [ $r = 0 ] && [ -n "$ON_DONE" ] && $ON_DONE "$f"; }
late(){ [ -n "$END" ] && [ $(date +%s) -ge $END ]; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD), $P at a time${MAXH:+, max $MAXH h}, ${#J[@]} pieces" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge $P ]; do late && break 2; sleep 5; done; late && break; run "$j" & done
while [ $(jobs -rp | wc -l) -gt 0 ]; do late && { pkill -f "dev/tools/gsa.js"; echo "stopped at max-hours $(date -u +%FT%TZ)" >> $OUT/status.txt; break; }; sleep 5; done
wait; n=$(ls $OUT/gsa-sobol-st-lo*.json 2>/dev/null | wc -l)
if [ $n != ${#J[@]} ]; then echo "$n of ${#J[@]} pieces saved $(date -u +%FT%TZ)" >> $OUT/status.txt; exit 1; fi
ok=0; node dev/tools/gsa.js sobjoin st $(ls $OUT/gsa-sobol-st-lo*.json | paste -sd,) --out=s137b-sobol-st > $OUT/sobjoin-st.log 2>&1 && mv dev/runs/v54/s137b-sobol-st.json $OUT/gsa-sobol-st.json || ok=1
( cd $OUT && sha256sum *.json > SHA256SUMS )
[ $ok = 0 ] && echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt || echo "pieces done, the join failed $(date -u +%FT%TZ)" >> $OUT/status.txt
[ -n "$ON_DONE" ] && $ON_DONE $OUT/gsa-sobol-st.json $OUT/SHA256SUMS
exit $ok
