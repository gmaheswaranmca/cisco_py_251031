# Product Management System (PMS) — Detailed Design & Implementation

> Multi-module Python API for `Product {id, name, qty, price}` with full CRUD, email notification on create, batch stock calculation (multi-thread/coroutines), web scraping module, logging, exception handling, and PEP 8 compliance.

---

## 1. Abstract

This project builds a production-ready, multi-module Python API (server) and a client application. The server exposes CRUD endpoints for `Product` objects stored in SQLite. When a new product is created, the system sends an email immediately to the business owner (background task). It supports batch processing to calculate total stock in batches of 10 products using either threads/processes or asyncio coroutines. A separate **web-scraping module** extracts product data from e-commerce pages to seed the database. The codebase includes structured logging, robust exception handling, unit tests, PEP 8-compliant formatting.

---

## 2. Key Requirements / Features

* REST API (CRUD) for `Product {id, name, qty, price}`
* SQLite persistence
* Immediate email notification on product creation
* Batch total-stock calculation (batches of 10) using:
  * `concurrent.futures.ThreadPoolExecutor` (or ProcessPool)
  * `asyncio` coroutine approach
* Web scraping module using `requests` + `BeautifulSoup` (optional `selenium` fallback)
* Structured logging (JSON-friendly optional)
* Centralized exception handling
* PEP 8 compliance, pylint
* Unit tests with `pytest`

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
pms/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── config.py          # Configs (DB, SMTP)
│   ├── models.py          # SQLAlchemy models
│   ├── crud.py            # DB operations
│   ├── routes.py          # Flask routes (CRUD endpoints)
│   ├── emailer.py         # Email service
│   ├── batch_calc.py      # Batch stock calculation
│   ├── scraper.py         # Web scraping functions
│   ├── logger.py          # Logging setup
│   └── exceptions.py      # Custom exceptions
├── run.py                 # Entry point
├── client/
│   ├── __init__.py        # Flask app factory
│   └── cli.py                  # minimal CLI client to call API
├── tests/
│   ├── __init__.py        # Flask app factory
│   ├── test_crud.py
│   └── test_batch_calc.py
├── requirements.txt
└── README.md
```

---
