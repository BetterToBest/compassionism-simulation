#!/bin/bash
# Usage: dev/tools/study12_jobs.sh WORKTREE OUTDIR [--max-hours=H] [--estimate]   (WORKTREE: a clean worktree of the engine commit; OUTDIR outside it)
# Session 12 (Oct 14, 2026; dev/plans/next-study-plan.md, Tier A; dev/DECISIONS.md Session 12): the measures study for the visual suite page.
# Six pieces, one per environment and horizon: dev/tools/explore_export.js --v54 --study --snab --slope on seeds 1-500, with the same rows and
# settings as the v5.6 panel (today's safety net, SNAP's work rule, the slope), checked against that merged panel (dev/runs/release-panel[-40]-ENV.json
# in the engine worktree: the yearly means of every row must equal the published path, which also proves the study's switches change no figure).
# Reporting only; the engine block is the v5.6 engine (973e7ce4... at 5bf5bcc). A piece whose file is in OUTDIR is skipped on a rerun.
# --max-hours=H: launch nothing new after H hours and stop the running pieces then (a rerun redoes them). ON_DONE=CMD: run "CMD FILE" after each saved file.
# --estimate: print the time estimate and exit.
W=$1; OUT=$2; MAXH=; EST=; for a in "${@:3}"; do case $a in --max-hours=*) MAXH=${a#--max-hours=};; --estimate) EST=1;; esac; done
P=${JOBS:-$(nproc)}; N=${SEEDS:-500}   # SEEDS=2 for a dry run of the whole script
if [ -n "$EST" ]; then
  # From two-seed timings of this session on one core (about 2.7 s a seed at 20 years and 5.5 s at 40, start-up included), plus 20%.
  awk -v p=$P 'BEGIN{ a=500*2.7*1.2/3600; b=500*5.5*1.2/3600; t=3*(a+b); w=(p >= 6) ? b : t/p; if (w < b) w = b;
    printf "core-hours: %.1f; on %d vCPU: about %.1f hours (the longest piece, 40 years, %.1f h)\n", t, p, w + 0.2, b }'
  exit 0
fi
cd "$W" || exit 1; END=; [ -n "$MAXH" ] && END=$(( $(date +%s) + $(awk "BEGIN{print int($MAXH*3600)}") ))
J=(); for y in 40 20; do for e in ref adv st; do J+=("$e $y"); done; done   # the long pieces first
done_(){ [ -n "$ON_DONE" ] && $ON_DONE "$@"; return 0; }
run(){ set -- $1; local s= f=$OUT/explore-study-$1-$2-snab.json; [ $2 = 40 ] && s=-40; [ -s $f ] && return
  node dev/tools/explore_export.js $1 $2 $N 1 --v54 --study --snab --slope --panel=dev/runs/release-panel$s-$1.json --out=$f.tmp > $OUT/st-$1-$2.log 2>&1 && mv $f.tmp $f
  local r=$?; echo "study $* done $(date -u +%FT%TZ) exit $r" >> $OUT/status.txt; [ $r = 0 ] && done_ "$f"; }
late(){ [ -n "$END" ] && [ $(date +%s) -ge $END ]; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD), $P at a time${MAXH:+, max $MAXH h}" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge $P ]; do late && break 2; sleep 5; done; late && break; run "$j" & done
while [ $(jobs -rp | wc -l) -gt 0 ]; do late && { pkill -f explore_export.js; echo "stopped at max-hours $(date -u +%FT%TZ)" >> $OUT/status.txt; break; }; sleep 5; done
wait
n=0; for j in "${J[@]}"; do set -- $j; [ -s $OUT/explore-study-$1-$2-snab.json ] && n=$((n + 1)); done
( cd $OUT && sha256sum explore-study-*.json > SHA256SUMS 2> /dev/null )
[ $n = ${#J[@]} ] && echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt || echo "$n of ${#J[@]} pieces saved $(date -u +%FT%TZ)" >> $OUT/status.txt
[ $n = ${#J[@]} ]
