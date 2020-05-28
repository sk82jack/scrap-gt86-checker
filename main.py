import requests
from bs4 import BeautifulSoup
from google.cloud import datastore

def scrap_gt86_checker(data, context):
    result = requests.get('http://www.dewsburyautosalvage.com/catalogsearch/result/index/?limit=all&q=gt86&x=0&y=0')
    soup = BeautifulSoup(result.content, 'lxml')

    client = datastore.Client()
    kind = 'gt86-scrap-checker'

    query = client.query(kind=kind)
    entities = list(query.fetch())

for products_grid in soup.find_all('ul', {'class': 'products-grid'}):
    for item in products_grid.find_all('li'):
        car = item.h2.a
        if not any(x['URL'] == car.attrs['href'] for x in entities):
            entity = datastore.Entity(client.key(kind, car.attrs['href']))
            entity.update({
                'title': car.attrs['title'],
                'URL': car.attrs['href'],
            })
            client.put(entity)
