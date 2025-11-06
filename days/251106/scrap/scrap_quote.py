import requests 
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

response = requests.get(url) 
print(response.text)
print('\n\n\n\n\n')

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

print(quotes)