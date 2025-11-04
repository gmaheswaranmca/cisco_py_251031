## 🧩 Key Concepts in the Code

### 1. **Multiprocessing**

* Python’s `multiprocessing` module creates **separate processes**, each with its **own Python interpreter and memory space**.
* Unlike threads, processes **avoid the GIL (Global Interpreter Lock)**, so they can run truly in parallel on multiple CPU cores.
* In this code, each page URL is scraped in its **own process**.

---

### 2. **`multiprocessing.Manager()`**

* Since processes have **separate memory spaces**, they cannot directly share normal Python lists or dicts.
* `multiprocessing.Manager()` creates special **shared objects** (like `list`, `dict`) that multiple processes can safely update.
* Here, we use:

  ```python
  manager = multiprocessing.Manager()
  results = manager.list()
  ```

  → This creates a **shared list** that all processes can write scraped data into.

---

### 3. **`multiprocessing.Process`**

* A `Process` object represents an **independent process**.
* You pass a target function and arguments, and it runs that function in parallel.
* Example:

  ```python
  p = multiprocessing.Process(target=scraper_func, args=(url, results))
  p.start()
  ```

  * `target=scraper_func` → function to run.
  * `args=(url, results)` → parameters passed to the function.
  * `p.start()` → actually starts the process.
  * `p.join()` → waits for the process to finish before moving on.

---

### 4. **Shared Data Flow**

Each process:

1. Fetches a page with `requests.get()`.
2. Parses HTML using BeautifulSoup.
3. Appends data into the **shared `results` list**.

Because `results` is a **managed list**, changes made in child processes are visible in the parent.

---

### 5. **Scraping Logic**

There are **two scraper functions**:

* `scrape_quotes_page(url, results)`
  → Extracts *quotes, authors, tags* from quotes.toscrape.com.
* `scrape_books_page(url, results)`
  → Extracts *book titles and prices* from books.toscrape.com.

Both functions:

* Use `requests` to fetch the page.
* Parse with BeautifulSoup.
* Append extracted results into the **shared list**.

---

### 6. **Orchestration in `scrape_site()`**

* Builds the list of URLs for the first 4 pages.
* Spawns a process for each URL.
* Waits for all processes to complete (`p.join()`).
* Returns the combined results as a **normal list**.

---

### 7. **Main Block**

* Runs both scrapers (quotes + books).
* Saves results into a JSON file.

---

## ⚖️ Why Multiprocessing Here?

* Threads in Python don’t run CPU-heavy code in true parallel (because of the GIL).
* Multiprocessing **does** achieve real parallelism since each process has its own interpreter and memory.
* In this scraper:

  * Work is I/O-bound (HTTP requests), so **threads or asyncio** are usually more efficient.
  * Multiprocessing adds overhead (new processes, inter-process communication).
  * But it’s useful to demonstrate **true parallel execution** and **shared objects**.

---

## 📌 Summary of Concepts

* **Multiprocessing** → true parallel execution using multiple processes.
* **Manager().list()** → shared memory-safe list across processes.
* **Process(target, args)** → runs a function in a new process.
* **start() / join()** → lifecycle control for processes.
* **BeautifulSoup + requests** → HTML parsing for quotes/books.

---

👉 So here, you’ve learned how to:

1. Run multiple scrapers in parallel processes.
2. Share results safely using `multiprocessing.Manager`.
3. Collect structured data and save it into JSON.
