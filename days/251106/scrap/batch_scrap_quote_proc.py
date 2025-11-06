import multiprocessing
import requests 
from bs4 import BeautifulSoup

def scrap_quote_page(url, quotes):
    response = requests.get(url) 

    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
    for quote_element in soup.find_all("div", class_="quote"):
        text = quote_element.find("span", class_="text").get_text(strip=True)
        author = quote_element.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote_element.find_all("a", class_="tag")]

        quotes.append({
            "quote": text,
            "author": author,
            "tags": tags})
        

def batch_quote_scraper():
    urls = [ 'http://quotes.toscrape.com/', 
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/']
    manager = multiprocessing.Manager()
    quotes = manager.list()  # shared list across processes
    processes = []

    # Start a process for each URL
    for url in urls:
        p = multiprocessing.Process(target=scrap_quote_page, args=(url, quotes))
        processes.append(p)
        p.start()

    # Wait for all processes
    for p in processes:
        p.join()
        
    results = list(quotes)
    return results

if __name__ == "__main__":
    print(batch_quote_scraper())