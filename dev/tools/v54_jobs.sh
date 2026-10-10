#!/bin/bash
# Usage: dev/tools/v54_jobs.sh WORKTREE OUTDIR   (WORKTREE: a clean worktree of the commit; OUTDIR outside it)
# v5.4 step 9: the 500-seed batch in resumable pieces, four at a time; a finished piece (its file in OUT) is skipped on a rerun.
W=$1; OUT=$2; cd "$W" || exit 1
J=()
for e in ref adv st; do for i in 0 1 2 3 4 5; do J+=("p40 $e $i 6"); done; done
for e in ref adv st; do for i in 0 1 2 3; do J+=("p20 $e $i 4"); done; done
for e in ref adv st; do J+=("bk $e"); done
run(){ set -- $1
  if [ $1 = bk ]; then f=$OUT/backing-share-$2.json; [ -s $f ] && return; node harness.js testbed 500 backing $2 --v54 --json=$f.tmp > $OUT/bk-$2.log 2>&1 && mv $f.tmp $f
  else y=; s=; [ $1 = p40 ] && { y=--years=40; s=-40; }; f=$OUT/release-panel$s-$2.part$3.json; [ -s $f ] && return
    node harness.js testbed 500 release $2 --v54 $y --part=$3/$4 --json=$f.tmp > $OUT/$1-$2-$3.log 2>&1 && mv $f.tmp $f; fi
  echo "$* done $(date -u +%FT%TZ) exit $?" >> $OUT/status.txt; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD)" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge 4 ]; do sleep 5; done; run "$j" & done
wait; echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt
