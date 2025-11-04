import requests
from bs4 import BeautifulSoup
import json
import multiprocessing


# ------------------------------
# Scraper for Quotes Site
# ------------------------------
def scrape_quotes_page(url, results):
    try:
        response = requests.get(url)
        response.encoding = "utf-8"
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, "html.parser")
        page_results = []

        for q in soup.find_all("div", class_="quote"):
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
            page_results.append({"quote": text, "author": author, "tags": tags})

        results.extend(page_results)
        print(f" Scraped {len(page_results)} quotes from {url}")

    except Exception as e:
        print(f" Error scraping {url}: {e}")


# ------------------------------
# Scraper for Books Site
# ------------------------------
def scrape_books_page(url, results):
    try:
        response = requests.get(url)
        response.encoding = "utf-8"
        if response.status_code != 200:
            return

        soup = BeautifulSoup(response.text, "html.parser")
        page_results = []

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").get_text(strip=True)
            page_results.append({"title": title, "price": price})

        results.extend(page_results)
        print(f" Scraped {len(page_results)} books from {url}")

    except Exception as e:
        print(f" Error scraping {url}: {e}")


# ------------------------------
# Multi-processing Scraper
# ------------------------------
def scrape_site(base_url, pages, scraper_func):
    manager = multiprocessing.Manager()
    results = manager.list()  # shared list across processes
    processes = []

    if 'quotes' in base_url:
        urls = [f"{base_url}/page/{i}/" for i in range(1, pages + 1)]
    else:
        urls = [f"{base_url}/page-{i}.html" for i in range(1, pages + 1)]

    # Start a process for each URL
    for url in urls:
        p = multiprocessing.Process(target=scraper_func, args=(url, results))
        processes.append(p)
        p.start()

    # Wait for all processes
    for p in processes:
        p.join()

    return list(results)


if __name__ == "__main__":
    final_data = {}

    # Scrape quotes site
    quotes_data = scrape_site("http://quotes.toscrape.com", 4, scrape_quotes_page)
    final_data["quotes"] = quotes_data

    # Scrape books site
    books_data = scrape_site("http://books.toscrape.com/catalogue", 4, scrape_books_page)
    final_data["books"] = books_data

    # Save results
    with open("scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)

    print(f"\n Done! Saved {len(quotes_data)} quotes and {len(books_data)} books into scraped_data.json")
