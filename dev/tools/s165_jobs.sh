#!/bin/bash
# Usage: dev/tools/s165_jobs.sh WORKTREE OUTDIR [--max-hours=H] [--estimate]   (WORKTREE: a clean worktree of the engine commit; OUTDIR outside it)
# Session 7 (Oct 14, 2026; ledger s164 for s165): the one study for v5.6 and the visual suite, on ONE pod, in resumable pieces (a piece whose file is in
# OUTDIR is skipped on a rerun; seeds are paired, so splitting changes no figure). In this order:
#  1. the full release panel with today's safety net and SNAP's work rule in every run (--v54 --snab): Reference, Adverse and Stress, 20 and 40 years,
#     seeds 1-500, as v5.4's pieces (40 years in 6 pieces, 20 in 4, per environment), and the backing-share sweep; plus the rule's own effect
#     (dev/tools/snap_rule_check.js --on: the main row and its no-programme run with today's safety net, rule off and on, 500 seeds, 20 and 40 years);
#  2. once an environment's panel pieces are in: merge them (dev/tools/merge_parts.py), then the explore export for the visual suite on the same engine
#     and settings (dev/tools/explore_export.js --v54 --suite --snab, checked against that merged panel);
#  3. the history check (ledger s146) only if decision d212 holds (the official poverty series attached) and its tool exists; neither is true on Oct 14.
# --max-hours=H: launch nothing new after H hours and stop the running pieces then (a rerun redoes them). ON_DONE=CMD: run "CMD FILE" after each saved file.
# --estimate: print the time estimate and exit.
W=$1; OUT=$2; MAXH=; EST=; for a in "${@:3}"; do case $a in --max-hours=*) MAXH=${a#--max-hours=};; --estimate) EST=1;; esac; done
P=${JOBS:-$(nproc)}; N=${SEEDS:-500}   # SEEDS=2 for a dry run of the whole script
if [ -n "$EST" ]; then
  # From the v5.4 batch (dev/PROGRESS.md, Oct 12: one core, 48 s a seed for the whole 40-year panel of one environment, 25 s at 20 years, 2 s for
  # backing; 31.4 core-hours), plus 10% for today's safety net, and two-seed timings of this session for the rule check (about 1.5 s a seed at 40
  # years, 0.7 at 20, four rows) and the export (about 3.5 and 1.5 s a seed).
  awk -v p=$P 'BEGIN{ pan=500*3*(48+25+2)*1.10/3600; iso=500*3*(1.5+0.7)/3600; ex=500*3*(3.5+1.5)/3600; piece=500*48/6*1.10/3600; tail=500*3.5/3600;
    t=pan+iso+ex; printf "core-hours: panel %.1f, rule check %.1f, export %.1f, total %.1f\n", pan, iso, ex, t;
    w=t/p; if (w < piece + tail) w = piece + tail; printf "on %d vCPU: about %.1f hours (longest single piece %.1f h, then the longest export %.1f h)\n", p, w + 0.3, piece, tail }'
  exit 0
fi
cd "$W" || exit 1; END=; [ -n "$MAXH" ] && END=$(( $(date +%s) + $(awk "BEGIN{print int($MAXH*3600)}") ))
J=()
for e in ref adv st; do for i in 0 1 2 3 4 5; do J+=("p40 $e $i 6"); done; done
for e in ref adv st; do for i in 0 1 2 3; do J+=("p20 $e $i 4"); done; done
for e in ref adv st; do J+=("bk $e"); for y in 20 40; do J+=("iso $e $y"); done; done
for e in ref adv st; do for y in 40 20; do J+=("ex $e $y"); done; done
done_(){ [ -n "$ON_DONE" ] && $ON_DONE "$@"; return 0; }
merged(){ local e=$1 y=$2 s= k=4; [ $y = 40 ] && { s=-40; k=6; }; local f=$OUT/release-panel$s-$e.json; [ -s $f ] && return 0
  for i in $(seq 0 $((k - 1))); do [ -s $OUT/release-panel$s-$e.part$i.json ] || return 1; done
  python3 dev/tools/merge_parts.py $OUT $e $y $k $f.tmp > $OUT/merge-$e-$y.log 2>&1 && mv $f.tmp $f && done_ $f; }
run(){ set -- $1; local f r
  case $1 in
    bk) f=$OUT/backing-share-$2.json; [ -s $f ] && return; node harness.js testbed $N backing $2 --v54 --snab --json=$f.tmp > $OUT/bk-$2.log 2>&1 && mv $f.tmp $f;;
    iso) f=$OUT/snap-iso-$2-$3.json; [ -s $f ] && return; node dev/tools/snap_rule_check.js --on --env=$2 --seeds=$N --years=$3 --out=$f.tmp > $OUT/iso-$2-$3.log 2>&1 && mv $f.tmp $f;;
    ex) f=$OUT/explore-suite-$2-$3-snab.json; [ -s $f ] && return; s=; [ $3 = 40 ] && s=-40
      while ! merged $2 $3; do late && return; sleep 30; done  # waits for this environment's panel pieces
      node dev/tools/explore_export.js $2 $3 $N 1 --v54 --suite --snab --panel=$OUT/release-panel$s-$2.json --out=$f.tmp > $OUT/ex-$2-$3.log 2>&1 && mv $f.tmp $f;;
    *) local y= s=; [ $1 = p40 ] && { y=--years=40; s=-40; }; f=$OUT/release-panel$s-$2.part$3.json; [ -s $f ] && return
      node harness.js testbed $N release $2 --v54 --snab $y --part=$3/$4 --json=$f.tmp > $OUT/$1-$2-$3.log 2>&1 && mv $f.tmp $f;;
  esac
  r=$?; echo "$* done $(date -u +%FT%TZ) exit $r" >> $OUT/status.txt
  [ $r = 0 ] && done_ "$f"; }
late(){ [ -n "$END" ] && [ $(date +%s) -ge $END ]; }
echo "start $(date -u +%FT%TZ) at $(git rev-parse --short HEAD), $P at a time${MAXH:+, max $MAXH h}" >> $OUT/status.txt
for j in "${J[@]}"; do while [ $(jobs -rp | wc -l) -ge $P ]; do late && break 2; sleep 5; done; late && break; run "$j" & done
while [ $(jobs -rp | wc -l) -gt 0 ]; do late && { pkill -f "harness.js testbed $N"; pkill -f explore_export.js; pkill -f snap_rule_check.js; echo "stopped at max-hours $(date -u +%FT%TZ)" >> $OUT/status.txt; break; }; sleep 5; done
wait
# 3. the history check (s146): only with its tool and the attached series (decision d212); not built as of Oct 14
if [ -f dev/tools/history_check.js ] && [ -f sources/census_poverty_2007.json ]; then node dev/tools/history_check.js > $OUT/history.log 2>&1 && echo "history done $(date -u +%FT%TZ)" >> $OUT/status.txt
else echo "history check skipped: no tool or no attached series (d212)" >> $OUT/status.txt; fi
n=0; for j in "${J[@]}"; do set -- $j; case $1 in bk) f=$OUT/backing-share-$2.json;; iso) f=$OUT/snap-iso-$2-$3.json;; ex) f=$OUT/explore-suite-$2-$3-snab.json;;
  p40) f=$OUT/release-panel-40-$2.part$3.json;; p20) f=$OUT/release-panel-$2.part$3.json;; esac; [ -s $f ] && n=$((n + 1)); done
[ $n = ${#J[@]} ] && echo "all done $(date -u +%FT%TZ)" >> $OUT/status.txt || echo "$n of ${#J[@]} pieces saved $(date -u +%FT%TZ)" >> $OUT/status.txt
[ $n = ${#J[@]} ]
