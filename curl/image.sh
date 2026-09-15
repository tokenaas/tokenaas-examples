#!/usr/bin/env bash
set -euo pipefail

: "${TOKENAAS_API_KEY:?Set TOKENAAS_API_KEY}"
BASE_URL="${TOKENAAS_BASE_URL:-https://tokenaas.ai/v1}"
MODEL="${TOKENAAS_IMAGE_MODEL:-Doubao-Seedream-4.5}"

curl -sS "${BASE_URL}/images/generations" \
  -H "Authorization: Bearer ${TOKENAAS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"prompt\": \"A quiet tropical beach at sunset, realistic photography\",
    \"size\": \"2048x2048\",
    \"n\": 1
  }"
echo
