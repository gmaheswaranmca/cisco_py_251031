# Hospital Management System (HMS) — Detailed Design & Implementation

> Multi-module Python API for `Patient {id, name, age, disease}` with full CRUD, email notification on create, batch patient average-age calculation (multi-thread/coroutines), web-scraping module (hospital/disease info), structured logging, centralized exception handling, unit tests, and PEP 8 compliance.

---

## 1. Abstract

This project develops a production-ready, multi-module Python API (server) with a client component. The server exposes CRUD endpoints for `Patient` objects stored in SQLite. When a new patient record is created, the system sends an immediate email notification to the hospital admin (as a background task). The system supports batch processing to calculate average patient age in batches of N (default 10) using either threads/processes or `asyncio` coroutines. A dedicated **web-scraping module** fetches hospital information (e.g., locations, departments) or disease-related metadata to enrich the system. The codebase follows PEP 8 standards, includes structured logging, robust exception handling, unit tests with `pytest`.

---

## 2. Key Requirements / Features

* REST API (CRUD) for `Patient {id, name, age, disease}`
* SQLite persistence (SQLAlchemy ORM)
* Immediate email notification on patient record creation
* Batch average-age calculation (batches of N, default 10) using:
  * `concurrent.futures.ThreadPoolExecutor` (or `ProcessPoolExecutor`)
  * `asyncio` coroutine implementation
* Web scraping module using `requests` + `BeautifulSoup` (optional Selenium for JS-heavy pages)
* Structured logging (JSON-friendly option)
* Centralized exception handling and custom exceptions
* PEP 8 compliance, linting with `pylint` / `flake8`
* Unit tests with `pytest`
* Simple CLI client to demonstrate functionality

---

## 3. High-level Architecture

```
+----------------+        +-------------------------+       +------------------+
| Client (React)  | <----> |  API Server (FlaskAPI)   | <-->  | SQLite Database  |
| or CLI / script |        |  - CRUD endpoints       |       | (file: db.sqlite)|
| (web client)    |        |  - email notifier       |       +------------------+
+----------------+        |  - batch calc module    |       +------------------+
                          |  - scraper module       | <--> | SMTP / Mailtrap  |
                          +-------------------------+       +------------------+
```

---

## 4. Folder / Module Layout

```
hms/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Configs (DB URL, SMTP, logging, batch size)
│   ├── models.py          # SQLAlchemy models (Patient)
│   ├── db.py              # DB session and initialization
│   ├── crud.py            # CRUD operations
│   ├── routes.py          # Flask routes (CRUD endpoints)
│   ├── emailer.py         # Email service (sync + background)
│   ├── batch_calc.py      # Batch average-age calculation (threads + asyncio)
│   ├── scraper.py         # Web scraping functions (hospital/disease info)
│   ├── logger.py          # Logging setup
│   └── exceptions.py      # Custom exceptions
├── run.py                 # Entry point
├── client/
│   ├── __init__.py
│   └── cli.py             # Minimal CLI client to call API
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_crud.py
│   └── test_batch_calc.py
├── requirements.txt
└── README.md
```
