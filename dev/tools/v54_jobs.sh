#!/bin/bash
# Usage: dev/tools/v54_jobs.sh WORKTREE OUTDIR [--max-hours=H]   (WORKTREE: a clean worktree of the commit; OUTDIR outside it)
# v5.4 step 9: the 500-seed batch in resumable pieces, one per core (JOBS=N overrides); a finished piece (its file in OUT) is skipped on a rerun.
# --max-hours=H: launch nothing new after H hours and stop the running pieces then (a rerun redoes them). ON_DONE=CMD: run "CMD FILE" after each finished piece.
W=$1; OUT=$2; MAXH=; for a in "${@:3}"; do case $a in --max-hours=*) MAXH=${a#--max-hours=};; esac; done
cd "$W" || exit 1; P=${JOBS:-$(nproc)}; END=; [ -n "$MAXH" ] && END=$(( $(date +%s) + $(awk "BEGIN{print int($MAXH*3600)}") ))
J=()
for e in ref adv st; do for i in 0 1 2 3 4 5; do J+=("p40 $e $i 6"); done; done
for e in ref adv st; do for i in 0 1 2 3; do J+=("p20 $e $i 4"); done; done
for e in ref adv st; do J+=("bk $e"); done
run(){ set -- $1
  if [ $1 = bk ]; then f=$OUT/backing-share-$2.json; [ -s $f ] && return; node harness.js testbed 500 backing $2 --v54 --json=$f.tmp > $OUT/bk-$2.log 2>&1 && mv $f.tmp $f
  else y=; s=; [ $1 = p40 ] && { y=--years=40; s=-40; }; f=$OUT/release-panel$s-$2.part$3.json; [ -s $f ] && return
    node harness.js testbed 500 release $2 --v54 $y --part=$3/$4 --json=$f.tmp > $OUT/$1-$2-$3.log 2>&1 && mv $f.tmp $f; fi
  r=$?; echo "$* done $(date -u +%FT%TZ) exit $r" >> $OUT/status.txt
  [ $r = 0 ] && [ -n "$ON_DONE" ] && $ON_DONE "$f"; }
late(){ [ -n "$END" ] && [ $(date +%s) -ge $END ]; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD), $P at a time${MAXH:+, max $MAXH h}" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge $P ]; do late && break 2; sleep 5; done; late && break; run "$j" & done
while [ $(jobs -rp | wc -l) -gt 0 ]; do late && { pkill -f "harness.js testbed 500"; echo "stopped at max-hours $(date -u +%FT%TZ)" >> $OUT/status.txt; break; }; sleep 5; done
wait; n=$(ls $OUT/release-panel*.part*.json $OUT/backing-share-*.json 2>/dev/null | grep -vc '\.tmp$')
[ $n = ${#J[@]} ] && echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt || echo "$n of ${#J[@]} pieces saved $(date -u +%FT%TZ)" >> $OUT/status.txt
[ $n = ${#J[@]} ]
