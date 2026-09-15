#!/usr/bin/env bash
set -euo pipefail

: "${TOKENAAS_API_KEY:?Set TOKENAAS_API_KEY}"
BASE_URL="${TOKENAAS_BASE_URL:-https://tokenaas.ai/v1}"

curl -sS "${BASE_URL}/models" \
  -H "Authorization: Bearer ${TOKENAAS_API_KEY}"
echo
