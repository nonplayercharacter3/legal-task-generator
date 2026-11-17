#!/bin/bash
# Autopilot loop for legal-task-generator. Each iteration starts a fresh `claude -p` session with the autopilot prompt;
# the session reads docs/autopilot/STATE.md, does one bounded slice of work, checkpoints, and exits.
#
# Start ONCE, from the main checkout, in a normal terminal where `claude` is logged in to your Max plan:
#   nohup caffeinate -i bash scripts/autopilot.sh >/dev/null 2>&1 &
# Watch:  tail -f runs/.autopilot/loop.log        Where things stand: docs/autopilot/STATE.md
# Stop:   touch runs/.autopilot/stop               (takes effect between iterations; a running session finishes first)
# Knobs:  AUTOPILOT_MODEL (default opus), AUTOPILOT_MAX_ITER (default 300), AUTOPILOT_BUDGET_USD per session (default 25,
#         a client-side estimate that ends a session that runs long; it is not money spent on a Max plan)
#
# No waiting session burns tokens: while a job the autopilot started is running (runs/.autopilot/wait says
# "pid <n>" and/or "until <unix time>"), this loop only sleeps. On a Claude usage limit it sleeps 30 minutes and retries.
set -u
REPO="$HOME/Projects/legal-task-generator"
cd "$REPO" || exit 1
[ -f "$HOME/.zshenv" ] && eval "$(grep -E '^export ' "$HOME/.zshenv")"
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

D=runs/.autopilot
mkdir -p "$D"
LOG="$D/loop.log"; LOCK="$D/lock"; STOP="$D/stop"; WAIT="$D/wait"
MODEL="${AUTOPILOT_MODEL:-opus}"
MAX_ITER="${AUTOPILOT_MAX_ITER:-300}"
BUDGET="${AUTOPILOT_BUDGET_USD:-25}"
log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $*" >> "$LOG"; }

if ! mkdir "$LOCK" 2>/dev/null; then log "another loop holds $LOCK; exiting"; exit 4; fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT
command -v claude >/dev/null || { log "claude CLI not found on PATH; exiting"; exit 3; }
log "loop start (model $MODEL, claude $(claude --version 2>/dev/null | head -1))"

fails=0
i=0
while [ "$i" -lt "$MAX_ITER" ]; do
  if [ -f "$STOP" ]; then log "stop file found; exiting"; break; fi
  if grep -q '^STATUS: DONE' docs/autopilot/STATE.md 2>/dev/null; then log "STATE says DONE; exiting"; break; fi

  # Sleep without a session while a recorded job runs or a wait time has not passed.
  if [ -f "$WAIT" ]; then
    pid=$(awk '/^pid /{print $2}' "$WAIT"); until=$(awk '/^until /{print $2}' "$WAIT"); now=$(date +%s)
    if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && [ "$now" -lt "${until:-9999999999}" ]; then sleep 600; continue; fi
    if [ -z "$pid" ] && [ -n "$until" ] && [ "$now" -lt "$until" ]; then sleep 600; continue; fi
    log "wait over ($(tr '\n' ' ' < "$WAIT"))"; rm -f "$WAIT"
  fi

  # Prompt: the committed copy once M0 has moved it into the repo, else the bootstrap copy.
  P=docs/autopilot/PROMPT.md; [ -f "$P" ] || P=.inbox/2026-11-17-autopilot/PROMPT.md
  i=$((i + 1))
  out="$D/iter-$(date +%Y%m%d-%H%M%S).json"
  log "iteration $i start"
  claude -p "$(cat "$P")" --model "$MODEL" --permission-mode auto --permission-prompts none \
    --max-budget-usd "$BUDGET" --output-format json > "$out" 2>&1
  rc=$?
  summary=$(python3 -c "import json,sys
try:
    d=json.load(open(sys.argv[1])); print(('ERROR ' if d.get('is_error') else '')+str(d.get('result',''))[:300].replace(chr(10),' '))
except Exception as e:
    print('unparsed: '+open(sys.argv[1]).read()[-300:].replace(chr(10),' '))" "$out")
  log "iteration $i end rc=$rc: $summary"

  if echo "$summary" | grep -qiE "unknown option|unrecognized"; then
    log "this claude version lacks a flag the loop uses (needs 2.1.259 or later); update Claude Code. Exiting."; exit 2; fi
  if echo "$summary" | grep -qiE "hit your .*limit|usage limit|limit reached|rate.?limit|resets [0-9]"; then
    log "usage limit; sleeping 30 min"; sleep 1800; continue; fi
  if [ "$rc" -ne 0 ]; then
    fails=$((fails + 1)); log "failure $fails in a row"
    if [ "$fails" -ge 5 ]; then log "5 failures in a row; exiting (see $out)"; exit 1; fi
    sleep 900; continue
  fi
  fails=0
  sleep 60
done
log "loop end"
