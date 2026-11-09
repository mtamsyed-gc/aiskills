#!/bin/bash
# Build the single-file version of a skill: SKILL.md followed by every reference file.
# Usage: tools/bundle.sh insurance-capital-ifrs17
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NAME="$1"; S="$ROOT/skills/$NAME"; O="$ROOT/dist/${NAME}_SINGLE-FILE.md"
{ cat "$S/SKILL.md"
  (cd "$S" && find references -name '*.md' | sort) | while read f; do
    printf '\n\n<!-- ===== FILE: %s ===== -->\n\n' "$f"; cat "$S/$f"; done
} > "$O"
echo "$O ~$(( $(wc -c <"$O")/4 )) tokens"
