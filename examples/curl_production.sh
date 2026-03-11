#!/usr/bin/env bash
set -euo pipefail

: "${FILTERDATA_API_KEY:?Set FILTERDATA_API_KEY env var}"

curl -sS -X POST 'https://filterdata.ru/api/v1/normalize' \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: ${FILTERDATA_API_KEY}" \
  -d '{"phone":"8 (999) 123-45-67","name":"Иванov","email":"EXAMPLE@gmail.com"}'
