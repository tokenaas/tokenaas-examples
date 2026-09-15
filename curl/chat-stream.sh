#!/usr/bin/env bash
set -euo pipefail

: "${TOKENAAS_API_KEY:?Set TOKENAAS_API_KEY}"
BASE_URL="${TOKENAAS_BASE_URL:-https://tokenaas.ai/v1}"
MODEL="${TOKENAAS_TEXT_MODEL:-deepseek-v4-flash}"

curl -N -sS "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${TOKENAAS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"stream\": true,
    \"messages\": [{\"role\": \"user\", \"content\": \"Write one short paragraph about APIs.\"}]
  }"
echo
