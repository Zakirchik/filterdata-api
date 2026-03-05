# filterdata-api
API for normalization and QC scoring of phone numbers, emails and names before loading data into CRM systems.
FilterData

FilterData — API нормализации и QC-оценки контактных данных.

Приводит телефоны, email и имена к единому формату и помогает выявлять проблемные записи до загрузки в CRM, маркетинговые системы и базы лидов.

Типичные задачи:

очистка лидов перед загрузкой в CRM

нормализация телефонных номеров

приведение email к стандартному виду

снижение количества дублей

улучшение качества контактных баз

Что делает API

FilterData принимает контактные данные и возвращает:

нормализованные значения

техническую оценку качества данных (QC)

человекочитаемое объяснение результата

Поддерживаемые поля:

phone
name
email
Пример запроса

POST

https://filterdata.ru/demo/api/v1/demo/normalize

Body:

{
  "phone": "8 (999) 123-45-67",
  "name": "иван иванов",
  "email": "EXAMPLE@mail.com"
}
Пример ответа
{
  "phone": "+79991234567",
  "name": "Иванов Иван",
  "email": "ivanov@example.com",
  "qc": 0,
  "explanation": "Данные корректны и готовы к использованию."
}
Уровни качества данных (QC)

QC показывает техническое качество записи.

QC	Значение	Описание
0	VALID	Данные корректны
1	ACCEPTABLE	Допустимо, но не идеально
2	RISK	Подозрительные данные
3	PARTIAL	Неполные данные
4	MISSING	Поле отсутствует

Пример риска:

Иванов Ivan

Смешение кириллицы и латиницы.

Demo API

Доступен открытый демо-endpoint для тестирования.

POST https://filterdata.ru/demo/api/v1/demo/normalize

Ограничения демо:

до 100 запросов в день с одного IP

API-ключ не требуется

телефоны обрабатываются в упрощённом режиме

Тарифы
FREE (тестовый)

Для разработки и первичной интеграции.

5 000 записей / месяц

RPS: 2

Batch: не поддерживается

Payload: до 0.2 MB

Жёсткий лимит

START — 2 990

Для малого и растущего бизнеса.

100 000 записей / месяц

RPS: 20

Batch: до 100

Payload: до 1 MB

Soft limit

Поддержка: email

STANDARD — 7 990

Для интеграторов и регулярных нагрузок.

500 000 записей / месяц

RPS: 50

Batch: до 300

Payload: до 3 MB

Soft limit

Очереди при перегрузке

Поддержка: email + чат

BUSINESS — 14 990

Для систем с большим объёмом данных.

1 500 000 записей / месяц

RPS: 100

Batch: до 500

Payload: до 5 MB

Приоритетная очередь

Поддержка: приоритетная

Типичные применения

CRM интеграции
Email-маркетинг
Call-центры
E-commerce
Lead-generation платформы

FilterData помогает очистить данные до того, как они попадут в бизнес-процессы.

Быстрый тест через curl
curl -X POST https://filterdata.ru/demo/api/v1/demo/normalize \
-H "Content-Type: application/json" \
-d '{
  "phone":"8 (999) 123-45-67",
  "name":"иван иванов",
  "email":"EXAMPLE@mail.com"
}'
Roadmap

Планируемые возможности:

дедупликация контактов

отчёт качества базы

batch-нормализация больших файлов

расширенная проверка email

Контакты

Website
https://filterdata.ru

Demo API
https://filterdata.ru/docs

Contact:
info@filterdata.ru
