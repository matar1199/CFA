#!/bin/bash
set -euo pipefail

# Only run in Claude Code on the web (cloud containers reset between sessions)
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
pip install --quiet -r requirements.txt
echo 'export PYTHONPATH="."' >> "$CLAUDE_ENV_FILE"
