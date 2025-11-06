import requests 
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/'

response = requests.get(url) 
#print(response.text)
#print('\n\n\n\n\n')

soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
articles = []

article_elements = soup.find_all("div", attrs={"data-testid":'card-text-wrapper'})
for article_element in article_elements:
    try: 
        headline_element = article_element.find('h2')#, attrs={"data-testid":'card-headline'})
        description_element = article_element.find('p')#, attrs={"data-testid":'card-description'})
        #if headline_element and description_element:
        news_dict = {'headline' : headline_element.get_text(strip=True),
                    'description' : description_element.get_text(strip=True)
                    }
        articles.append(news_dict)
    except:
        pass 

print(articles)