## ⚡ Features of `asyncio` used here

### 1. **Coroutines with `async def`**

* In the code, functions like `scrape_quotes_page` and `scrape_books_page` are defined with `async def`.
* These are **coroutines**, meaning they can pause (`await`) while waiting and let other tasks run in the meantime.

Example:

```python
async def scrape_quotes_page(session, url):
    async with session.get(url) as response:
        text = await response.text()
```

🔑 While waiting for the HTTP response (`await response.text()`), the event loop can run other tasks.

---

### 2. **`await` for non-blocking I/O**

* `await` is used whenever we perform a time-consuming I/O operation.
* Instead of blocking the program, `await` suspends the coroutine and gives control back to the **event loop**.
* When the I/O finishes, execution resumes.

Used in:

```python
text = await response.text()
```

---

### 3. **`aiohttp.ClientSession()`**

* This is an **asynchronous HTTP client session** that allows multiple requests without blocking.
* Works like `requests`, but supports `async/await`.
* Inside it, we use:

  ```python
  async with session.get(url) as response:
  ```

  which performs a non-blocking GET request.

---

### 4. **`asyncio.gather()`**

* Runs multiple coroutines **concurrently**.
* Instead of fetching pages one by one, we launch all page requests at once.
* `return_exceptions=True` ensures errors don’t crash the whole program; they are returned as results.

Example:

```python
tasks = [scraper_func(session, url) for url in urls]
pages_data = await asyncio.gather(*tasks, return_exceptions=True)
```

---

### 5. **`asyncio.run(main())`**

* Starts the **event loop**, runs the `main()` coroutine, and shuts down the loop cleanly.
* Without it, coroutines (`async def`) won’t execute.

Used at the bottom:

```python
if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🛠 Functions in the Code

1. **`scrape_quotes_page(session, url)`**

   * Coroutine to scrape one quotes page.
   * Uses `aiohttp` for async HTTP requests.
   * Parses quotes, authors, and tags using BeautifulSoup.
   * Returns a list of quotes.

2. **`scrape_books_page(session, url)`**

   * Coroutine to scrape one books page.
   * Extracts title + price for each book.
   * Returns a list of books.

3. **`scrape_site(base_url, pages, scraper_func)`**

   * Orchestrates scraping multiple pages for a site.
   * Builds all page URLs.
   * Creates tasks (`tasks = [scraper_func(...)]`).
   * Runs them concurrently with `asyncio.gather`.
   * Collects all results into one list.

4. **`main()`**

   * The top-level coroutine.
   * Calls `scrape_site` twice (once for quotes, once for books).
   * Saves the results into JSON.

---

## 📌 Summary

* **async/await** → Makes HTTP requests non-blocking.
* **aiohttp.ClientSession()** → Async HTTP client for concurrent requests.
* **asyncio.gather()** → Runs multiple coroutines concurrently.
* **asyncio.run()** → Starts and manages the event loop.
