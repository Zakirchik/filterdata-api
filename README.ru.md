# FilterData API

API-сервис для технической очистки и нормализации контактных данных перед записью в CRM / базы лидов / маркетинговые системы.

Сайт: https://filterdata.ru  
Почта (получить API-ключ): info@filterdata.ru  

> Этот репозиторий содержит публичный контракт API и примеры для hosted-сервиса `filterdata.ru`.

## Что сервис делает

- Нормализация телефонов (RU): удаление лишних символов, `8...` -> `+7...`, формат `E.164`.
- Нормализация email: trim + lowercase + базовая проверка синтаксиса.
- Нормализация имени/ФИО: очистка, исправление регистра, приведение структуры.
- QC (0–4): техническая оценка качества данных.
- Детект рисков:
  - смешение кириллицы и латиницы (антифрод/обход поиска дублей)
  - вероятная опечатка домена email (Levenshtein по популярным доменам)

## Что сервис НЕ делает

- Проверку существования телефона (HLR)
- Антифрод-скоринг (0–100) и внешние источники
- Data enrichment

## QC (0–4)

| QC | Уровень | Смысл |
|---:|---|---|
| 0 | VALID | Данные корректны |
| 1 | ACCEPTABLE | Допустимо, но не идеально |
| 2 | RISK | Риск: смесь алфавитов / опечатка домена / подозрительные паттерны |
| 3 | PARTIAL | Технически неполные/невалидные |
| 4 | MISSING | Поле отсутствует |

## Endpoints

### Demo (без ключа)

`POST https://filterdata.ru/demo/normalize`

Ограничения:
- до 100 запросов/день на IP
- упрощенный режим для телефонов

Пример:

```bash
curl -sS -X POST 'https://filterdata.ru/demo/normalize' \
  -H 'Content-Type: application/json' \
  -d '{"phone":"8 (999) 123-45-67","name":"иван иванов","email":"user@agmil.com"}'
```

### Production (по API-ключу)

Base URL: `https://filterdata.ru/api/v1/`

Заголовок:

`X-API-Key: <ваш ключ>`

Endpoints:
- `POST /normalize` (одна запись)
- `POST /batch` (до 1000 записей)

Единица биллинга: **1 запись = 1 unit** (в batch списание по количеству элементов `contacts`).

## Форматы запросов/ответов

### 1) Single normalize

Request:

```json
{
  "phone": "8 (999) 123-45-67",
  "name": "иван иванов",
  "email": "EXAMPLE@gmail.com"
}
```

Response (production):

```json
{
  "phone": "+79991234567",
  "name": "Иванов Иван",
  "email": "example@gmail.com",
  "qc": 0,
  "qc_breakdown": {
    "phone": 0,
    "name": 0,
    "email": 0
  },
  "warnings": []
}
```

### 2) Batch normalize

Request:

```json
{
  "contacts": [
    {"phone":"8 (999) 123-45-67","name":"иван иванов","email":"EXAMPLE@gmail.com"},
    {"phone":"+7 912 000-00-00","name":"Иванov","email":"user@agmil.com"}
  ]
}
```

Response:

```json
{
  "results": [
    {
      "phone": "+79991234567",
      "name": "Иванов Иван",
      "email": "example@gmail.com",
      "qc": 0,
      "qc_breakdown": {"phone": 0, "name": 0, "email": 0},
      "warnings": []
    },
    {
      "phone": "+79120000000",
      "name": "Иванov",
      "email": "user@agmil.com",
      "qc": 2,
      "qc_breakdown": {"phone": 0, "name": 2, "email": 2},
      "warnings": ["name_mixed_alphabet_risk", "email_domain_typo"]
    }
  ]
}
```

## Warnings (production)

Типовые флаги:
- `name_mixed_alphabet_risk`
- `email_domain_typo`
- `phone_invalid`
- `email_invalid`
- `name_invalid`
- `name_acceptable`

## HTTP статусы (production)

- `200` OK
- `400` некорректный запрос (например, не передано ни одного поля)
- `401` отсутствует `X-API-Key`
- `403` ключ неверный/неактивный
- `402` превышен месячный лимит
- `429` rate limit (на уровне gateway/nginx)
- `422` validation error (Pydantic)

## Быстрые примеры

### Смешение алфавитов

`"Иванov"` -> `QC=2 (RISK)`

### Опечатка домена email

`user@agmil.com` -> `QC=2 (RISK)`, warning `email_domain_typo`  
Важно: домен **не исправляется автоматически**, только помечается.

## Документация и примеры

- Swagger (Demo): https://filterdata.ru/docs
- Если в Swagger `Try it out` возвращает `404`, используйте стабильный демо-эндпоинт `POST /demo/normalize` (см. выше).
- OpenAPI контракт (в репозитории): `openapi/filterdata.openapi.yaml`
- Postman коллекция: `postman/filterdata.postman_collection.json`
