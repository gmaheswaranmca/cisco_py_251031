# Banking Management System (BMS) — Detailed Design & Implementation

> Multi-module Python API for `Account {id, name, number, balance}` with full CRUD, email notification on create, batch total-balance calculation (multi-thread/coroutines), web-scraping module (interest rates / bank info), structured logging, centralized exception handling, unit tests, and PEP 8 compliance.

---

## 1. Abstract

This project builds a production-ready, multi-module Python API (server) and a simple client. The server exposes CRUD endpoints for `Account` objects stored in SQLite. When a new account is created, the system sends an email immediately to the business owner (background task). It supports batch processing to calculate total balances in batches of N (default 10) using either `concurrent.futures` (threads/processes) or `asyncio` coroutines. A separate **web-scraping module** fetches current interest rates or bank metadata to seed or annotate accounts. The codebase includes structured logging (JSON-friendly option), robust exception handling, unit tests with `pytest`.

---

## 2. Key Requirements / Features

* REST API (CRUD) for `Account {id, name, number, balance}`
* SQLite persistence (SQLAlchemy ORM)
* Immediate email notification on account creation (background worker/thread/async task)
* Batch total-balance calculation (batches of N, default 10) using:
  * `concurrent.futures.ThreadPoolExecutor` (or `ProcessPoolExecutor`)
  * `asyncio` coroutine implementation
* Web scraping module using `requests` + `BeautifulSoup` (optional `selenium` fallback)
* Structured logging (optionally JSON output)
* Centralized exception handling and custom exceptions
* PEP 8 compliance; linting with `pylint`/`flake8`
* Unit tests with `pytest`
* Simple CLI client for demonstration + example Postman collection

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
bms/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Configs (DB URL, SMTP, batch size, logging)
│   ├── models.py          # SQLAlchemy models (Account)
│   ├── db.py              # DB session, initialization helpers
│   ├── crud.py            # DB operations (create/read/update/delete)
│   ├── routes.py          # Flask routes (CRUD endpoints)
│   ├── emailer.py         # Email service (synchronous & background wrapper)
│   ├── batch_calc.py      # Batch total-balance calculation (threads + asyncio)
│   ├── scraper.py         # Web scraping functions (interest rates)
│   ├── logger.py          # Logging setup (structured)
│   └── exceptions.py      # Custom exceptions
├── run.py                 # Entry point (create_app + run)
├── client/
│   ├── __init__.py
│   └── cli.py             # minimal CLI client to call API (create/read/list)
├── tests/
│   ├── __init__.py
│   ├── test_crud.py
│   └── test_batch_calc.py
├── requirements.txt
└── README.md
```
