import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json


# ------------------------------
# Scraper for Quotes Site
# ------------------------------
async def scrape_quotes_page(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            return []
        text = await response.text()
        soup = BeautifulSoup(text, "html.parser")
        quotes = []

        for q in soup.find_all("div", class_="quote"):
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
            quotes.append({"quote": text, "author": author, "tags": tags})

        print(f" Scraped {len(quotes)} quotes from {url}")
        return quotes


# ------------------------------
# Scraper for Books Site
# ------------------------------
async def scrape_books_page(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            return []
        text = await response.text()
        soup = BeautifulSoup(text, "html.parser")
        books = []

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").get_text(strip=True)
            books.append({"title": title, "price": price})

        print(f" Scraped {len(books)} books from {url}")
        return books


# ------------------------------
# Async Multi-page Scraper
# ------------------------------
async def scrape_site(base_url, pages, scraper_func):
    results = []
    if 'quotes' in base_url:
        urls = [f"{base_url}/page/{i}/" for i in range(1, pages + 1)]
    else:
        urls = [f"{base_url}/page-{i}.html" for i in range(1, pages + 1)]

    async with aiohttp.ClientSession() as session:
        tasks = [scraper_func(session, url) for url in urls]
        pages_data = await asyncio.gather(*tasks, return_exceptions=True)

        for data in pages_data:
            if isinstance(data, list):
                results.extend(data)

    return results


# ------------------------------
# Main entry
# ------------------------------
async def main():
    final_data = {}

    # Scrape quotes
    quotes_data = await scrape_site("http://quotes.toscrape.com", 4, scrape_quotes_page)
    final_data["quotes"] = quotes_data

    # Scrape books
    books_data = await scrape_site("http://books.toscrape.com/catalogue", 4, scrape_books_page)
    final_data["books"] = books_data

    # Save results
    with open("scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)

    print(f"\n Done! Saved {len(quotes_data)} quotes and {len(books_data)} books into scraped_data.json")


if __name__ == "__main__":
    asyncio.run(main())
