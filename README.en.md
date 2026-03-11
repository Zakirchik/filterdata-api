# FilterData API

Hosted API to normalize and QC-score contact data before writing it into CRM / lead DB / marketing tools.

Website: https://filterdata.ru  
Get an API key: info@filterdata.ru  

> This repository contains the public API contract and integration examples for the hosted service at `filterdata.ru`.

## What it does

- Phone normalization (RU): strips non-digits, `8...` -> `+7...`, outputs `E.164`.
- Email normalization: trim + lowercase + basic syntax validation.
- Name normalization: cleanup + capitalization + structure.
- QC score (0–4) per field and per record.
- Risk detection:
  - mixed Cyrillic/Latin alphabet (fraud/search-bypass pattern)
  - common email domain typos (Levenshtein against popular providers)

## What it does NOT do

- Phone existence checks (HLR)
- Fraud scoring / enrichment
- External data sources

## QC levels (0–4)

| QC | Level | Meaning |
|---:|---|---|
| 0 | VALID | Clean data |
| 1 | ACCEPTABLE | Usable, but not perfect |
| 2 | RISK | Mixed alphabets / domain typo / suspicious patterns |
| 3 | PARTIAL | Incomplete/invalid |
| 4 | MISSING | Field not provided |

## Endpoints

### Demo (no key)

`POST https://filterdata.ru/demo/normalize`

Limits:
- 100 requests/day per IP
- simplified phone mode

```bash
curl -sS -X POST 'https://filterdata.ru/demo/normalize' \
  -H 'Content-Type: application/json' \
  -d '{"phone":"8 (999) 123-45-67","name":"ivanov ivan","email":"user@agmil.com"}'
```

### Production (API key)

Base URL: `https://filterdata.ru/api/v1/`

Header:

`X-API-Key: <your key>`

Endpoints:
- `POST /normalize` (single record)
- `POST /batch` (up to 1000 records)

Billing unit: **1 record = 1 unit**. Batch is billed by `len(contacts)`.

## Request/Response formats

### Single normalize

```json
{
  "phone": "8 (999) 123-45-67",
  "name": "Ivanov Ivan",
  "email": "EXAMPLE@gmail.com"
}
```

```json
{
  "phone": "+79991234567",
  "name": "Ivanov Ivan",
  "email": "example@gmail.com",
  "qc": 0,
  "qc_breakdown": {"phone": 0, "name": 0, "email": 0},
  "warnings": []
}
```

### Batch normalize

```json
{
  "contacts": [
    {"phone":"8 (999) 123-45-67","name":"Ivanov Ivan","email":"EXAMPLE@gmail.com"},
    {"phone":"+7 912 000-00-00","name":"Иванov","email":"user@agmil.com"}
  ]
}
```

```json
{
  "results": [
    {
      "phone": "+79991234567",
      "name": "Ivanov Ivan",
      "email": "example@mail.com",
      "qc": 0,
      "qc_breakdown": {"phone": 0, "name": 0, "email": 0},
      "warnings": []
    }
  ]
}
```

## Warnings (production)

Common values:
- `name_mixed_alphabet_risk`
- `email_domain_typo`
- `phone_invalid`
- `email_invalid`
- `name_invalid`
- `name_acceptable`

## HTTP status codes (production)

- `200` OK
- `400` bad request (e.g. no fields provided)
- `401` missing `X-API-Key`
- `403` invalid/inactive key
- `402` monthly hard limit exceeded
- `429` rate limit (gateway/nginx)
- `422` validation error (Pydantic)

## Docs & examples

- Swagger (Demo): https://filterdata.ru/docs
- If Swagger "Try it out" returns `404`, use the stable demo endpoint `POST /demo/normalize` (see above).
- OpenAPI contract (in this repo): `openapi/filterdata.openapi.yaml`
- Postman collection: `postman/filterdata.postman_collection.json`
