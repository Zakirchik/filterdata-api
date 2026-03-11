#!/usr/bin/env bash
set -euo pipefail

curl -sS -X POST 'https://filterdata.ru/demo/normalize' \
  -H 'Content-Type: application/json' \
  -d '{"phone":"8 (999) 123-45-67","name":"иван иванов","email":"user@agmil.com"}'
