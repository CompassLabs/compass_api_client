#!/bin/bash
set -eou pipefail

PACKAGE_JSON_URL="https://pypi.org/pypi/${1}/json"

curl -L -s "$PACKAGE_JSON_URL" \
    | jq  -r '.releases | keys | .[]' \
    | sort -V \
    | tail -n1

