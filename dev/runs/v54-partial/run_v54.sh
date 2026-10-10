#!/bin/bash
# v5.4 step 9: the 500-seed panels from a clean worktree (arg 1). 20-year panel then the backing sweep per env; the 40-year panels in parallel.
cd "$1" || exit 1
mkdir -p dev/runs/v54
st=/tmp/claude-0/-home-user-compassionism-simulation/f7497646-b20f-5809-80e3-4fef3add972f/scratchpad/batch-status.txt
echo "started $(date -u +%FT%TZ) at $(git rev-parse --short HEAD)" >> $st
for e in ref adv st; do
  ( node harness.js testbed 500 release $e --v54 --years=40 --json=dev/runs/v54/release-panel-40-$e.json > dev/runs/v54/release-panel-40-$e.log 2>&1; echo "p40 $e exit $? $(date -u +%FT%TZ)" >> $st ) &
  ( node harness.js testbed 500 release $e --v54 --json=dev/runs/v54/release-panel-$e.json > dev/runs/v54/release-panel-$e.log 2>&1; echo "p20 $e exit $? $(date -u +%FT%TZ)" >> $st
    node harness.js testbed 500 backing $e --v54 --json=dev/runs/v54/backing-share-$e.json > dev/runs/v54/backing-share-$e.log 2>&1; echo "backing $e exit $? $(date -u +%FT%TZ)" >> $st ) &
done
wait
echo "all done $(date -u +%FT%TZ)" >> $st
