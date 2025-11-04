import requests
from bs4 import BeautifulSoup
import json

def scrape_quotes(base_url, pages=5):
    all_quotes = []

    for page in range(1, pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"Scraping {url} ...")

        response = requests.get(url)
        if response.status_code != 200:
            print(f" Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]

            all_quotes.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

    return all_quotes


if __name__ == "__main__":
    base_url = "http://quotes.toscrape.com"
    data = scrape_quotes(base_url, pages=3)  # scrape 3 pages

    # Save results into JSON file
    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Scraping complete! Saved {len(data)} quotes into quotes.json")
