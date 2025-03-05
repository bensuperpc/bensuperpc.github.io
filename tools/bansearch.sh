#!/bin/bash
set -euo pipefail
readonly BANWORD_REGEX_FILE=${1:-tools/banwordregex.txt}

if [ ! -f "$BANWORD_REGEX_FILE" ]; then
    echo "Banword regex file not found: $BANWORD_REGEX_FILE"
    exit 1
fi

find . -type d \( -name ".git" -o -name "tools" \) -prune -o -type f -print0 | parallel --null grep -E -i -f "$BANWORD_REGEX_FILE" --color=always -H -n "{}"
