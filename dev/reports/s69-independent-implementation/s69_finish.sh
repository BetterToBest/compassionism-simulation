#!/bin/sh
# S69: after the six batches, write the comparison, compress the per-seed results, and write RESULTS/run.txt and RESULTS/SHA256SUMS.
# Usage: sh s69_finish.sh [PACKET] [RESULTS]   (defaults: the candidate main row's packet and results/; S63 part 3: the frozen row's packet and results-frozen/)
set -e
cd "$(dirname "$0")"
PACKET=${1:-../../packets/s69-main-row.zip}
R=${2:-results}
BUILT=$(unzip -p "$PACKET" run.txt | grep -o 'commit [0-9a-f]\{40\}' | head -1 | cut -d' ' -f2)
WHAT=$(unzip -p "$PACKET" run.txt | grep -q 'r2FreezePair' && echo 'the frozen main row of round 2 (full backing, S69 corrections on)' || echo 'the candidate main row of round 2')
python3 -I s69_compare.py "$R" "$PACKET" > /dev/null
for f in "$R"/*-1-500.json; do [ -f "$f" ] && gzip -9 -n -f "$f"; done
{
  echo "S69 phase 1: a third, independent implementation of $WHAT (Python), and its comparison with the engine's references."
  echo
  echo "Packet: $PACKET, sha256 $(sha256sum "$PACKET" | cut -d' ' -f1) (built from engine commit $BUILT)."
  echo "Program: the files listed in SHA256SUMS (written on top of repository commit $(git rev-parse HEAD)). $(python3 --version), standard library only."
  echo "Machine: $(nproc) processors; seconds per batch are in each results file."
  echo
  echo "Commands (from this folder):"
  for e in ref adv st; do for r in base main; do echo "  python3 -I s69_main.py --env $e --row $r --seeds 1-500 --jobs 4 --packet $PACKET --out $R/$e-$r-1-500.json"; done; done
  echo "  python3 -I s69_compare.py $R $PACKET          (writes $R/compare.md and $R/compare-*.csv)"
  echo "  python3 -I s69_check_capture.py            (the Stress supply-path settings rule, checked on Reference and Adverse)"
  echo "  node dump_tables.js <packet>/code/main-row-code-full.js tables.json   (code_tables.json: the tables the configuration file lacks)"
  echo "  gzip -9 -n $R/*-1-500.json"
  echo
  echo "One seed with a key-by-key comparison: python3 -I s69_main.py --env ref --row main --seed 1 --cmp"
} > "$R"/run.txt
sha256sum s69_*.py dump_tables.js code_tables.json s69_finish.sh GAPS.md REPORT.md "$R"/*.json.gz "$R"/compare*.csv "$R"/compare.md "$R"/batches.log "$R"/run.txt > "$R"/SHA256SUMS
echo done
