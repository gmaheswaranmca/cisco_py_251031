## ✅ When You *Can* Scrape a Website

1. **The site allows scraping**:

   * Some sites are built specifically for scraping practice (e.g. [quotes.toscrape.com](http://quotes.toscrape.com), [books.toscrape.com](http://books.toscrape.com), [jsonplaceholder](https://jsonplaceholder.typicode.com/)).
   * Many open/public APIs are also free to fetch.

2. **Check the robots.txt file**:

   * Example: `http://example.com/robots.txt`
   * This file tells you what parts of the site can/can’t be crawled by bots.
   * If the section is marked as `Disallow:`, you should avoid scraping it.

3. **Data is public**:

   * Content is visible to anyone without login or payment (e.g. news articles, product listings).

4. **Educational / research purposes**:

   * Some test sites are created **just to teach scraping** (like the `toscrape` family).

---

## ❌ When You *Should Not* Scrape

1. **Login-protected / personal data**:

   * Example: scraping Facebook profiles, Gmail, or banking sites is illegal.

2. **Against Terms of Service (ToS)**:

   * Many big platforms (Amazon, LinkedIn, Instagram, Twitter) explicitly **forbid scraping** in their ToS.

3. **High traffic scraping without permission**:

   * Flooding a server with thousands of requests per second can be treated as a **Denial-of-Service (DoS) attack**.

4. **Commercial use without license**:

   * If you plan to resell or use data for business, you usually need to buy access via their **official API**.

---

## ⚖️ General Rule of Thumb

* **Scraping for learning** → use demo sites like `quotes.toscrape.com`, `books.toscrape.com`, `httpbin.org`.
* **Scraping real sites** → always check **robots.txt** and **Terms of Service**.
* **Large-scale scraping** → ask permission or use official APIs.
