import requests
from bs4 import BeautifulSoup

def scrap_gt86_checker(data, context):
    result = requests.get('http://www.dewsburyautosalvage.com/catalogsearch/result/index/?limit=all&q=gt86&x=0&y=0')
    soup = BeautifulSoup(result.content, 'lxml')

    number = int(soup.find("p", {"class": "amount"}).strong.text.split()[0])

    for products_grid in soup.find_all('ul', {'class': 'products-grid'}):
        for item in products_grid.find_all('li'):
            car = item.h2.a
            # print(car.attrs['title'])
            # print (car.attrs['href'])
