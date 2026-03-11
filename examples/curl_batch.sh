#!/usr/bin/env bash
set -euo pipefail

: "${FILTERDATA_API_KEY:?Set FILTERDATA_API_KEY env var}"

curl -sS -X POST 'https://filterdata.ru/api/v1/batch' \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: ${FILTERDATA_API_KEY}" \
  -d '{"contacts":[{"phone":"8 (999) 123-45-67","name":"иван иванов","email":"EXAMPLE@gmail.com"},{"phone":"+7 912 000-00-00","name":"Иванov","email":"user@agmil.com"}]}'
