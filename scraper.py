import requests
from bs4 import BeautifulSoup
import pandas as pd

main_url = "https://indianexpress.com/section/{}/page/{}"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0" }
links = ['india', 'explained', 'opinion', 'business', 'sports', 'political-pulse', 'lifestyle', 'technology']
max_pages = 60

articles = []
categories = []

def findArticle(page_number: int, page_link: str):
    response = requests.get(main_url.format(page_link, page_number), headers=headers)
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            for article in soup.select('.articles .img-context'):
                articles.append(article.select('h2.title a')[0].text.strip() + ' ' + article.select('p')[0].text.strip())
                categories.append(page_link)
            print("page {} completed".format(page_number))
        except:
            print("an exception occured on page {}".format(page_number))
    else:
        print("an error occured on page {}".format(page_number))

def scrapePage(link: str):
    for page in range(1, max_pages + 1):
        findArticle(page, link)

for link in links:
    scrapePage(link)

output_frame = pd.DataFrame({ 'article_text': articles, 'category': categories })
output_frame.to_csv('./dataset.csv', index=None)