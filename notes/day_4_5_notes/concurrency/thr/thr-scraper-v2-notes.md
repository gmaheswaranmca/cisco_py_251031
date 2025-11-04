## 🔑 Concepts in This Multi-Threaded Scraper

### 1. **ThreadPoolExecutor**

```python
with ThreadPoolExecutor(max_workers=5) as executor:
```

* `ThreadPoolExecutor` manages a **pool of worker threads**.
* Instead of manually creating and starting `threading.Thread` objects, you just “submit” tasks, and the executor handles scheduling them across available threads.
* `max_workers=5` → at most 5 pages will be fetched in parallel.

---

### 2. **Submitting Tasks**

```python
future_to_url = {executor.submit(scraper_func, url): url for url in urls}
```

* `executor.submit(func, arg)` schedules a function (`scraper_func`) to run in a separate thread.
* It returns a **Future object**, which represents the eventual result of the function.
* A dict `future_to_url` is used to keep track of which future belongs to which URL (handy for logging).

---

### 3. **as\_completed**

```python
for future in as_completed(future_to_url):
```

* `as_completed` yields futures **as soon as they finish** (not in submission order).
* This means you can process results as they arrive, instead of waiting for all threads to complete sequentially.

---

### 4. **Future.result()**

```python
data = future.result()
```

* `.result()` retrieves the return value from the thread’s function (e.g., list of quotes or books).
* If the function raised an exception, `.result()` will re-raise it → which is why you wrapped it in `try/except`.

---

### 5. **Scraping Functions**

Two scrapers handle different sites:

* **Quotes Site (`scrape_quotes_page`)**

  * Extracts text, author, and tags.
  * Returns a list of dicts → `[{"quote": "...", "author": "...", "tags": [...]}, ...]`.

* **Books Site (`scrape_books_page`)**

  * Extracts title and price of each book.
  * Returns `[{"title": "...", "price": "..."}, ...]`.

Each scraper is **stateless** (no shared variables), so no locks are needed.

---

### 6. **Dynamic URL Generation**

```python
if 'quotes' in base_url:
    urls = [f"{base_url}/page/{i}/" for i in range(1, pages + 1)]
else:
    urls = [f"{base_url}/page-{i}.html" for i in range(1, pages + 1)]
```

* Different websites have different page URL patterns.
* This logic ensures correct URLs are generated for both quotes and books sites.

---

### 7. **Collecting Results**

```python
results.extend(data)
```

* Each page returns its own list of items.
* These are appended to the main `results` list.
* Since all thread results are joined in the main thread, no lock is needed here.

---

### 8. **Saving Data to JSON**

```python
with open("scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False, indent=4)
```

* Saves structured results in **readable JSON format**.
* `ensure_ascii=False` → preserves Unicode characters.
* `indent=4` → makes the file pretty-printed.

---

## ⚖️ Why This is Better Than Manual Threads

* No need for `lock` → each thread just returns results.
* No manual `start()` / `join()` management.
* Cleaner error handling with `.result()`.
* Easier to scale — just adjust `max_workers`.

---

✅ **In short**:
This program demonstrates **concurrent I/O with ThreadPoolExecutor**, uses **Futures** to collect results, applies **BeautifulSoup parsing**, dynamically builds URLs, and saves structured results into JSON. It’s a textbook example of a clean, production-style Python multi-threaded scraper.
