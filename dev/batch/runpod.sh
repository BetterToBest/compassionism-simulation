#!/bin/bash
# The v5.4 500-seed batch on a Runpod CPU pod. Each finished piece is pushed at once to BetterToBest/compassionism-sim-results
# (branch main, folder v54-<engine commit>/); a file DONE there means every piece is in. The pod then terminates itself
# (stops itself if terminating is refused). A restarted pod resumes: pieces already in the results repository are skipped.
# Pod start command (RUNNER = the commit of this repository that holds this file; the image needs bash, git, curl):
#   bash -c 'git clone -q https://github.com/BetterToBest/compassionism-simulation /w/sim && cd /w/sim && git checkout -q RUNNER && bash dev/batch/runpod.sh'
# Pod env: GH_TOKEN = {{ RUNPOD_SECRET_github_results_token }}; MAX_HOURS (default 10); MODE=smoke for the smoke test
# (token expiry, one small file pushed, then terminate); STUDY=s137 for ledger step s137 (dev/tools/s137_jobs.sh), s137b for its follow-up Sobol
# (dev/tools/s137b_jobs.sh), s165 for the v5.6 study (dev/tools/s165_jobs.sh; about 2.6 hours on 16 vCPU, --estimate); default v54, the v5.4 batch.
# The token is never printed or written to disk. The engine commit is pinned below; the batch refuses to start if its worktree is not clean,
# and run.txt records the engine, runner, Node version and command; SHA256SUMS (s137) records every output's hash.
STUDY=${STUDY:-v54}
case $STUDY in
  v54)  ENGINE=fe88599f9d2f4d26651f6e01370454206257beab; JOBSH=dev/tools/v54_jobs.sh;;   # head of pull request #13's branch: the v5.4 engine, pinned
  s137) ENGINE=a3582e2ad2489619151b295d037cf99cb272fdd8; JOBSH=dev/tools/s137_jobs.sh;;                     # the outside-audit fixes' commit (engine unchanged since 57e00367e58f)
  s137b) ENGINE=41f236124d27ac282e4241acc0b916c24d036c49; JOBSH=dev/tools/s137b_jobs.sh;;                  # s137's follow-up Sobol (gsa.js sobjoin; engine unchanged since 57e00367e58f)
  s165) ENGINE=c88c1e096e74380341996f3953407bd9d701622b; JOBSH=dev/tools/s165_jobs.sh;;                   # ledger s165: the panel with today's safety net and SNAP's work rule, the rule's own effect, the visual-suite export (s166, s164)
  *) echo "unknown STUDY $STUDY"; exit 1;;
esac
NODEV=22.22.0                                      # the Node version of the earlier local runs
RES=BetterToBest/compassionism-sim-results; D=$STUDY-${ENGINE:0:7}; W=/w
log(){ echo "[runpod.sh $(date -u +%FT%TZ)] $*"; }
git config --global credential.helper '!f() { echo username=x-access-token; echo "password=$GH_TOKEN"; }; f'
git config --global user.name "compassionism batch pod"; git config --global user.email "noreply@users.noreply.github.com"

if [ "${1:-}" = push ]; then   # ON_DONE hook from v54_jobs.sh: push one finished piece (and the logs) to the results repository
  ( flock 9; cd $W/res || exit 1; git add "${@:2}" $D/status.txt $D/run.txt $D/*.log || exit 1; git commit -qm "$STUDY batch: $(basename "$2")" || exit 1
    for t in 1 2 3 4 5; do git push -q origin HEAD:main && exit 0; sleep $((t * 10)); git pull -q --rebase origin main; done; exit 1
  ) 9> $W/push.lock || log "push of $2 failed (it stays on the pod; the next push retries it)"
  exit 0
fi

bye(){  # terminate this pod, else stop it; never fall through to a container restart loop
  log "ending: $1"
  if command -v runpodctl > /dev/null; then runpodctl pod delete "$RUNPOD_POD_ID" && exit 0; runpodctl remove pod "$RUNPOD_POD_ID" && exit 0; fi
  for u in https://rest.runpod.io/v1/pods/$RUNPOD_POD_ID https://api.runpod.io/v2/pods/$RUNPOD_POD_ID; do
    curl -fsS -X DELETE -H "Authorization: Bearer $RUNPOD_API_KEY" "$u" > /dev/null && { log "terminate requested ($u)"; sleep 600; }; done
  if command -v runpodctl > /dev/null; then runpodctl pod stop "$RUNPOD_POD_ID" || runpodctl stop pod "$RUNPOD_POD_ID"; fi
  curl -fsS -X POST -H "Authorization: Bearer $RUNPOD_API_KEY" https://rest.runpod.io/v1/pods/$RUNPOD_POD_ID/stop > /dev/null && log "stop requested"
  log "could not terminate or stop the pod: stop it in the Runpod console"; sleep infinity; }

h=$(curl -sS -o /dev/null -D - -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/repos/$RES)
log "results repository: $(echo "$h" | head -1 | tr -d '\r'); token expiry: $(echo "$h" | grep -i '^github-authentication-token-expiration:' | cut -d' ' -f2- | tr -d '\r')"
git clone -q https://github.com/$RES $W/res || bye "cannot clone the results repository"

if [ "${MODE:-}" = smoke ]; then
  f=smoke-$(date -u +%Y%m%dT%H%M%SZ).txt; echo "smoke test from pod $RUNPOD_POD_ID, $(nproc) vCPU, $(date -u +%FT%TZ)" > $W/res/$f
  cd $W/res && git add $f && git commit -qm "smoke test: $f" && git push -q origin HEAD:main && log "pushed $f" || log "PUSH REFUSED for $f"
  bye "smoke test finished"
fi

[ -f $W/res/$D/DONE ] && bye "DONE already in the results repository"
if [ "$(node -v 2>/dev/null)" != v$NODEV ]; then
  curl -fsSL https://nodejs.org/dist/v$NODEV/node-v$NODEV-linux-x64.tar.gz | tar -xz -C /usr/local --strip-components=1 || bye "Node install failed"; fi
git -C $W/sim worktree add -q --detach $W/engine $ENGINE || bye "engine commit $ENGINE not found"
[ -z "$(git -C $W/engine status --porcelain)" ] || bye "engine worktree not clean"
RUNNER=$(git -C $W/sim rev-parse HEAD); mkdir -p $W/res/$D
echo "study $STUDY; engine $ENGINE; runner $RUNNER; node $(node -v); $(nproc) vCPU; pod $RUNPOD_POD_ID; start $(date -u +%FT%TZ); command: ON_DONE=... $JOBSH $W/engine $W/res/$D --max-hours=${MAX_HOURS:-10}" >> $W/res/$D/run.txt
STUDY=$STUDY ON_DONE="bash $W/sim/dev/batch/runpod.sh push" bash $W/sim/$JOBSH $W/engine $W/res/$D --max-hours=${MAX_HOURS:-10}; ok=$?
cd $W/res; [ $ok = 0 ] && { tail -1 $D/status.txt > $D/DONE; git add $D/DONE; }
git add $D/status.txt $D/run.txt $D/*.log $D/*.json $D/SHA256SUMS 2> /dev/null; git commit -qm "$STUDY batch: $([ $ok = 0 ] && echo DONE || echo 'stopped before the end')"
for t in 1 2 3 4 5; do git push -q origin HEAD:main && break; sleep $((t * 10)); git pull -q --rebase origin main; done
bye "batch $([ $ok = 0 ] && echo finished || echo 'stopped at max-hours')"
