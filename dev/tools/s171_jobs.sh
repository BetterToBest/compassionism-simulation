#!/bin/bash
# Usage: dev/tools/s171_jobs.sh WORKTREE OUTDIR [--max-hours=H] [--estimate]   (WORKTREE: a clean worktree of the engine commit; OUTDIR outside it)
# Study s171 (Oct 15, 2026): ONE Runpod study that carries everything the open work needs, so a chat without code access can finish it from the results alone.
#   A. ledger s117 (community-project hours): the release panel on the current engine with today's safety net, SNAP's work rule and the slope in every run
#      (as the v5.6 panel) plus --hours, which adds pjHrs, pjWork and pjDisp (with 95% intervals) to every row. Reference, Adverse, Stress; 20 and 40 years;
#      seeds 1-500, in resumable pieces (40 years in 6, 20 in 4, per environment). Merged afterwards by dev/tools/merge_parts.py (needs python3).
#   B. ledger s95 / s171 (the like-for-like re-run of the compare page's six designs on the current engine): node harness.js testbed 500 match ENV --snab --slope,
#      Compassionism (the Hub-specification model, the released main row) beside UBI, NIT and asset endowment matched to its cost, X-Cents and public grocery,
#      with today's safety net in every arm; two financing rules (money = the Source's reading, v5.0 and later; tax = the old flat wage contribution).
#      Text tables, one file per environment, horizon and financing rule.
#   C. ledger s118 (the second implementation): the real engine's runScenario output for the five validation presets, seeds 1-500 (the packet carries seeds 1-30
#      and 42), so a Python version can be checked on 500-seed means as well as on single seeds.
# A piece whose file is in OUTDIR is skipped on a rerun; seeds are paired, so splitting changes no figure.
# --max-hours=H: launch nothing new after H hours and stop the running pieces then (a rerun redoes them). ON_DONE=CMD: run "CMD FILE" after each saved file.
# --estimate: print the time estimate and exit.   SEEDS=2 runs the whole script on two seeds (dry run).
R=$(cd "$(dirname "$0")/../.." && pwd)
W=$1; OUT=$2; MAXH=; EST=; for a in "${@:3}"; do case $a in --max-hours=*) MAXH=${a#--max-hours=};; --estimate) EST=1;; esac; done
P=${JOBS:-$(nproc)}; N=${SEEDS:-500}
if [ -n "$EST" ]; then
  # A: v5.4 batch timing (48 s a seed at 40 years and 25 s at 20 years per environment, one core) plus 10%; B: about 25 s a seed per piece at 20 years and 50 s at 40
  # (a 2-seed run of the whole match section took 51 s with 60-seed pilots; this is an upper-side guess, say so if it is wrong); C: under 1 s a seed.
  awk -v p=$P 'BEGIN{ a=500*3*(48+25)*1.10/3600; b=500*3*2*(25+50)/3600; c=500*5*0.5/3600; t=a+b+c;
    printf "core-hours (guess for B): panel %.1f, comparison %.1f, python reference %.1f, total %.1f\n", a, b, c, t;
    w=t/p; if (w < 500*50/3600) w = 500*50/3600; printf "on %d vCPU: about %.1f hours (longest single piece about %.1f h)\n", p, w + 0.3, 500*50/3600 }'
  exit 0
fi
cd "$W" || exit 1; END=; [ -n "$MAXH" ] && END=$(( $(date +%s) + $(awk "BEGIN{print int($MAXH*3600)}") ))
done_(){ [ -n "$ON_DONE" ] && $ON_DONE "$@"; return 0; }
cp $R/dev/tools/s171_README.md $OUT/README.md 2> /dev/null && done_ $OUT/README.md
J=()
for e in ref adv st; do for f in money tax; do for y in 40 20; do J+=("cmp $e $y $f"); done; done; done   # the long pieces first
for e in ref adv st; do for i in 0 1 2 3 4 5; do J+=("p40 $e $i 6"); done; done
for e in ref adv st; do for i in 0 1 2 3; do J+=("p20 $e $i 4"); done; done
J+=("py")
merged(){ local e=$1 y=$2 s= k=4; [ $y = 40 ] && { s=-40; k=6; }; local f=$OUT/release-panel$s-$e.json; [ -s $f ] && return 0
  for i in $(seq 0 $((k - 1))); do [ -s $OUT/release-panel$s-$e.part$i.json ] || return 1; done
  python3 dev/tools/merge_parts.py $OUT $e $y $k $f.tmp > $OUT/merge-$e-$y.log 2>&1 && mv $f.tmp $f && done_ $f; }
run(){ set -- $1; local f r
  case $1 in
    cmp) local yf=; [ $3 = 40 ] && yf=--years=40; f=$OUT/match-$2-$3-$4.txt; [ -s $f ] && return
      { echo "# s171 comparison: engine $(git rev-parse --short HEAD); node harness.js testbed $N match $2 --models=framework --fin=$4 --v54 --snab --slope $yf; $(date -u +%FT%TZ)"
        NODE_OPTIONS=--max-old-space-size=6144 node harness.js testbed $N match $2 --models=framework --fin=$4 --v54 --snab --slope $yf; } > $f.tmp 2> $OUT/cmp-$2-$3-$4.log && mv $f.tmp $f;;
    py) f=$OUT/python-reference-$N.json; [ -s $f ] && return
      S118_SEEDS=$N node $R/dev/packets/make_s118_reference.js > $f.tmp 2> $OUT/py.log && mv $f.tmp $f;;
    *) local y= s=; [ $1 = p40 ] && { y=--years=40; s=-40; }; f=$OUT/release-panel$s-$2.part$3.json; [ -s $f ] && return
      node harness.js testbed $N release $2 --v54 --snab --slope --hours $y --part=$3/$4 --json=$f.tmp > $OUT/$1-$2-$3.log 2>&1 && mv $f.tmp $f;;
  esac
  r=$?; echo "$* done $(date -u +%FT%TZ) exit $r" >> $OUT/status.txt
  if [ $r = 0 ]; then done_ "$f"; case $1 in p40) merged $2 40;; p20) merged $2 20;; esac; fi; }
late(){ [ -n "$END" ] && [ $(date +%s) -ge $END ]; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD), $P at a time${MAXH:+, max $MAXH h}" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge $P ]; do late && break 2; sleep 5; done; late && break; run "$j" & done
while [ $(jobs -rp | wc -l) -gt 0 ]; do late && { pkill -f "harness.js testbed $N"; pkill -f make_s118_reference.js; echo "stopped at max-hours $(date -u +%FT%TZ)" >> $OUT/status.txt; break; }; sleep 5; done
wait
n=0; for j in "${J[@]}"; do set -- $j; case $1 in cmp) [ -s $OUT/match-$2-$3-$4.txt ] && n=$((n + 1));; py) [ -s $OUT/python-reference-$N.json ] && n=$((n + 1));;
  p40) [ -s $OUT/release-panel-40-$2.part$3.json ] && n=$((n + 1));; p20) [ -s $OUT/release-panel-$2.part$3.json ] && n=$((n + 1));; esac; done
( cd $OUT && sha256sum *.json *.txt > SHA256SUMS 2> /dev/null )
[ $n = ${#J[@]} ] && echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt || echo "$n of ${#J[@]} pieces saved $(date -u +%FT%TZ)" >> $OUT/status.txt
[ $n = ${#J[@]} ]
