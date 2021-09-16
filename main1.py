KEYWORDS = {'дизайн', 'фото', 'web', 'python*', 'c*', 'javascript*'}

import requests
from bs4 import BeautifulSoup

req = requests.get('https://habr.com/ru/all/')

soup = BeautifulSoup(req.text, 'html.parser')
articles = soup.find_all('article')
url_list = []

for article in articles:
    hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
    hubs_text = set()
    for hub in hubs:
        hubs_text.add(hub.text.lower().strip())

    if KEYWORDS & hubs_text:
        time = article.find('span', class_='tm-article-snippet__datetime-published')
        title = article.find('h2')
        link = title.find('a').attrs.get('href')
        url = 'https://habr.com' + link
        url_list.append(url)
        print(f"{time.text} - {title.text} - {url}")


for url in url_list:
    article_read = requests.get(url)
    soup2 = BeautifulSoup(article_read.text, 'html.parser')
    text2 = article_read
    print(text2.text)