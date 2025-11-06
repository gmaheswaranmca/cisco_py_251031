import requests 
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url) 
print(response.text)
print('\n\n\n\n\n')

soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
books = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text(strip=True)
    books.append({
        "title": title,
        "price": price
    })

print(books)