'''
Problem Statement
    Build a Python multi-threaded web scraper that:
        Visits multiple websites (e.g., quotes.toscrape.com, books.toscrape.com).
        Scrapes the first 4 pages of each site.
        Extracts structured data (quotes/authors for quotes site, book titles/prices for books site).
        Saves results into JSON.
        Uses threads so each page is fetched concurrently.
'''
import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# ------------------------------
# Scraper for Quotes Site
# ------------------------------
def scrape_quotes_page(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
    quotes = []

    for q in soup.find_all("div", class_="quote"):
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]

        quotes.append({
            "quote": text,
            "author": author,
            "tags": tags
        })
    return quotes


# ------------------------------
# Scraper for Books Site
# ------------------------------
def scrape_books_page(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
    books = []

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").get_text(strip=True)
        books.append({
            "title": title,
            "price": price
        })
    return books


# ------------------------------
# Multi-threaded Scraper
# ------------------------------
def scrape_site(base_url, pages, scraper_func):
    results = []
    if 'quotes' in base_url:
        urls = [f"{base_url}/page/{i}/" for i in range(1, pages + 1)]
    else:
        urls = [f"{base_url}/page-{i}.html" for i in range(1, pages + 1)]

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(scraper_func, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                results.extend(data)
                print(f" Scraped {len(data)} items from {url}")
            except Exception as e:
                print(f" Error scraping {url}: {e}")
    return results


if __name__ == "__main__":
    final_data = {}

    # Scrape quotes.toscrape.com (first 4 pages)
    quotes_data = scrape_site("http://quotes.toscrape.com", 4, scrape_quotes_page)
    final_data["quotes"] = quotes_data

    # Scrape books.toscrape.com (first 4 pages)
    books_data = scrape_site("http://books.toscrape.com/catalogue", 4, scrape_books_page)
    final_data["books"] = books_data

    # Save all results into JSON
    with open("scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)

    print(f"\n Done! Saved {len(quotes_data)} quotes and {len(books_data)} books into scraped_data.json")
