from concurrent.futures import ThreadPoolExecutor, as_completed
import requests 
from bs4 import BeautifulSoup

def scrap_quote_page(url):
    response = requests.get(url) 

    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
    quotes = []
    for quote_element in soup.find_all("div", class_="quote"):
        text = quote_element.find("span", class_="text").get_text(strip=True)
        author = quote_element.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote_element.find_all("a", class_="tag")]

        quotes.append({
            "quote": text,
            "author": author,
            "tags": tags})
        
    return quotes 

'''
def scrap_quote_pages():
    urls = [ 'http://quotes.toscrape.com/', 
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/']
    result = []
    for url in urls:
        result.extend(scrap_quote_page(url))
    print(result)

scrap_quote_pages()
'''
def batch_quote_scraper():
    urls = [ 'http://quotes.toscrape.com/', 
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/']
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(scrap_quote_page, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                results.extend(data)
                print(f" Scraped {len(data)} items from {url}")
            except Exception as e:
                print(f" Error scraping {url}: {e}")
    return results

batch_quote_scraper()