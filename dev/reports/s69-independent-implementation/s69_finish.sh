#!/bin/sh
# S69: after the six batches, write the comparison, compress the per-seed results, and write results/run.txt and results/SHA256SUMS.
set -e
cd "$(dirname "$0")"
PACKET=${1:-../../packets/s69-main-row.zip}
python3 -I s69_compare.py results "$PACKET" > /dev/null
for f in results/*-1-500.json; do [ -f "$f" ] && gzip -9 -n -f "$f"; done
{
  echo "S69 phase 1: a third, independent implementation of the candidate main row of round 2 (Python), and its comparison with the engine's references."
  echo
  echo "Packet: dev/packets/s69-main-row.zip, sha256 $(sha256sum "$PACKET" | cut -d' ' -f1) (built from engine commit 26d9b47cef39785ab40881619945b6ca68d0292c)."
  echo "Program: the files listed in SHA256SUMS (written on top of repository commit $(git rev-parse HEAD)). $(python3 --version), standard library only."
  echo "Machine: $(nproc) processors; seconds per batch are in each results file."
  echo
  echo "Commands (from this folder):"
  for e in ref adv st; do for r in base main; do echo "  python3 -I s69_main.py --env $e --row $r --seeds 1-500 --jobs 4 --out results/$e-$r-1-500.json"; done; done
  echo "  python3 -I s69_compare.py results          (writes results/compare.md and results/compare-*.csv)"
  echo "  python3 -I s69_check_capture.py            (the Stress supply-path settings rule, checked on Reference and Adverse)"
  echo "  node dump_tables.js <packet>/code/main-row-code-full.js tables.json   (code_tables.json: the tables the configuration file lacks)"
  echo "  gzip -9 -n results/*-1-500.json"
  echo
  echo "One seed with a key-by-key comparison: python3 -I s69_main.py --env ref --row main --seed 1 --cmp"
} > results/run.txt
sha256sum s69_*.py dump_tables.js code_tables.json s69_finish.sh GAPS.md REPORT.md results/*.json.gz results/compare*.csv results/compare.md results/batches.log results/run.txt > results/SHA256SUMS
echo done
