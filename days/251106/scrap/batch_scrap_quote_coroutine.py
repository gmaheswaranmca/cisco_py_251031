import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def scrap_quote_page(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            return []
        text = await response.text()

        soup = BeautifulSoup(text, "html.parser", from_encoding="utf-8")
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
        

async def batch_quote_scraper():
    urls = [ 'http://quotes.toscrape.com/', 
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/']
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [scrap_quote_page(session, url) for url in urls]
        quotes = await asyncio.gather(*tasks, return_exceptions=True)

        for data in quotes:
            if isinstance(data, list):
                results.extend(data)
        
        return results

async def main():
    print(await batch_quote_scraper())

if __name__ == "__main__":
    asyncio.run(main())

