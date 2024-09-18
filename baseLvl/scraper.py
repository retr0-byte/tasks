import requests
from bs4 import BeautifulSoup as BS

URL = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='

res = requests.get(URL)
soup = BS(res.text, 'html.parser')

page_count = int(soup.find_all('a', {'class': 'page-link'})[-2].text)

data = {}

goods_count = 1

for page in range(1, page_count + 1):
    new_url = f'{URL}{page}'
    res = requests.get(URL)
    soup = BS(res.text, 'html.parser')

    for laptop in soup.find_all('div', {'class': 'product-wrapper card-body'}):
        image = laptop.find('img', {'class': 'img-fluid card-img-top image img-responsive'}).get('src')
        name = laptop.find('a', {'class': 'title'}).text
        price = laptop.find('h4', {'class': 'price float-end card-title pull-right'}).text
        description = laptop.find('p', {'class': 'description card-text'}).text
        rating = laptop.find('p', {'class': 'review-count float-end'}).text

        laptop_data = {
            'image': image,
            'name': name,
            'price': price,
            'description': description,
            'rating': rating
        }
        data[f'{goods_count}'] = laptop_data
        goods_count += 1

print(data)
