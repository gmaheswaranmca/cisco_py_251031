import requests

url = "http://books.toscrape.com/"
res = requests.get(url)

print("Declared encoding:", res.encoding)          # From headers
print("Apparent encoding:", res.apparent_encoding) # Detected from content

# Force correct encoding
res.encoding = res.apparent_encoding
html = res.text