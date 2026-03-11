# Changelog

This changelog summarizes major product milestones for the hosted API at `filterdata.ru`.

## 2026-03-10
- Production base URL stabilized: `https://filterdata.ru/api/v1/` (SSL, reverse proxy, routing fixes).
- Batch endpoint validated in production.

## 2026-03-09
- Email domain typo risk detection (Levenshtein against popular providers). QC=RISK, no auto-fix.

## 2026-03-08
- Batch API: `POST /api/v1/batch` (up to 1000 records).
- Billing optimized for batch: one SQLite write per batch (avoid `database is locked`).

## 2026-02-12
- Landing page + demo API integration.
- Stress tests (core engine ~700-800 RPS isolated, production contour baseline established).

## 2026-02-11
- RU phone input compatibility: `8XXXXXXXXXX` -> `+7XXXXXXXXXX`.
- Mixed alphabet detection in name normalization (anti-fraud/search-bypass pattern).

## 2026-01-31
- QC scale fixed (0-4).
- Monthly billing hard limit enforcement (HTTP 402 on exceed).

