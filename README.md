# FilterData API

Normalize and QC-score contact data (phone, email, name) before you write it to CRM / lead DB / marketing tools.

Languages: [RU](README.ru.md) | [EN](README.en.md)

Links: [Website](https://filterdata.ru) | [Demo Swagger](https://filterdata.ru/docs) | Email: info@filterdata.ru

> This repository is the public API contract + examples for the hosted service. The server code runs on filterdata.ru.

## Quick Start (no API key, Demo)

Demo endpoint (100 requests/day per IP):

```bash
curl -sS -X POST 'https://filterdata.ru/demo/normalize' \
  -H 'Content-Type: application/json' \
  -d '{"phone":"8 (999) 123-45-67","name":"иван иванов","email":"user@agmil.com"}'
```

Note: Demo Swagger UI is available at `https://filterdata.ru/docs`. If Swagger "Try it out" returns `404`, use the stable demo endpoint above.

## Production API

Base URL: `https://filterdata.ru/api/v1/`

Endpoints:
- `POST /normalize` (single record)
- `POST /batch` (up to 1000 records per request)

Auth: `X-API-Key: <your key>`

Billing unit: **1 contact = 1 unit**. Batch is billed by `len(contacts)`.

### cURL (single)

```bash
curl -sS -X POST 'https://filterdata.ru/api/v1/normalize' \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: YOUR_API_KEY' \
  -d '{"phone":"8 (999) 123-45-67","name":"Иванov","email":"EXAMPLE@gmail.com"}'
```

### cURL (batch)

```bash
curl -sS -X POST 'https://filterdata.ru/api/v1/batch' \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: YOUR_API_KEY' \
  -d '{"contacts":[{"phone":"8 (999) 123-45-67","name":"иван иванов","email":"EXAMPLE@gmail.com"}]}'
```

## QC Levels (0-4)

| QC | Level | Meaning |
|---:|---|---|
| 0 | VALID | Clean, ready to use |
| 1 | ACCEPTABLE | Usable, but not perfect |
| 2 | RISK | Fraud/search-bypass patterns (e.g. mixed alphabets) or email domain typo |
| 3 | PARTIAL | Incomplete/invalid input |
| 4 | MISSING | Field not provided |

## Performance Notes

- Core normalization engine (isolated): ~700-800 RPS
- Production contour (auth + billing + SQLite): stable baseline validated

## Pricing (monthly limits)

| Plan | Limit | RPS | Batch | Price |
|---|---:|---:|---:|---:|
| FREE | 5k | 2 | - | 0 |
| START | 100k | 20 | 100 | 2,990 RUB |
| STANDARD | 500k | 50 | 300 | 7,990 RUB |
| BUSINESS | 1.5M | 100 | 500 | 14,990 RUB |

## Files in this repo

- [`README.ru.md`](README.ru.md) / [`README.en.md`](README.en.md)
- [`openapi/filterdata.openapi.yaml`](openapi/filterdata.openapi.yaml) (public contract)
- [`postman/filterdata.postman_collection.json`](postman/filterdata.postman_collection.json)
- [`examples/`](examples/)
