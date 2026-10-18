#!/usr/bin/env bash
# Cloud session setup: download LAB and build the decontamination index in the background, so a pilot round finds
# it ready. Plain computer work, no model calls and no tokens; about 35 minutes on a fresh container.
#
# The environment's setup script runs this from the repo folder (see CLAUDE.md). Session start never waits for it
# and never fails because of it: everything runs in the background and reports to $LOG.
#   tail -f /tmp/lab-index.log      # "reference index ready" when done, "SETUP FAILED" otherwise
#
# Settings (environment variables, all optional):
#   BRANCH   branch whose code builds the index (default claude/wonderful-bardeen-ecwx4o; use main once merged)
#   CONFIG   config with gates.reference_dirs, relative to the repo (default configs/pilot_nrp_solver.toml)

REPO="${REPO:-$PWD}"
BRANCH="${BRANCH:-claude/wonderful-bardeen-ecwx4o}"
CONFIG="${CONFIG:-configs/pilot_nrp_solver.toml}"
LAB="$(dirname "$REPO")/harvey-labs"
SRC=/tmp/ltg-index-src
LOG=/tmp/lab-index.log

(
  set -euo pipefail
  echo "setup started $(date -u +%FT%TZ): repo $REPO, code from $BRANCH, LAB at $LAB"
  cd "$REPO"

  # The session's own checkout may be another branch: build with $BRANCH's code, unpacked outside the repo.
  git fetch -q origin "$BRANCH"
  rm -rf "$SRC" && mkdir -p "$SRC" && git archive FETCH_HEAD | tar -x -C "$SRC"

  # Python environment for pilot runs (the Claude Agent SDK is an optional extra).
  [ -x .venv/bin/python ] || python3 -m venv .venv
  .venv/bin/pip install -q -e ".[dev,claude]"

  # LAB, once per container. LFS objects are not needed: the index reads the documents themselves.
  if [ ! -d "$LAB/.git" ]; then
    GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 -q https://github.com/harveyai/harvey-labs "$LAB"
  fi

  # Build from the repo folder so the config's relative paths (../harvey-labs, runs/.decontam_cache) resolve here.
  PYTHONPATH="$SRC" python3 -m ltg index --config "$SRC/$CONFIG"
  echo "setup finished $(date -u +%FT%TZ)"
) > "$LOG" 2>&1 || echo "SETUP FAILED (exit $?), see the lines above" >> "$LOG" &

exit 0
