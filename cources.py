import math
import requests
from bs4 import BeautifulSoup

url = 'https://cbr.ru/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text, 'html.parser')

table = soup.findAll('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})

cource_of_euro = 0
for sum in table[-1:]:
    cource_of_euro = sum.text



cource_of_euro_m = cource_of_euro[:7]
cource_of_euro_m = cource_of_euro_m.replace(',', '.')
cource_of_euro_m = (float(cource_of_euro_m))
print('Официальный курс евро по ЦБ - ', cource_of_euro_m, 'рублей')
cource_of_euro_m = math.ceil(cource_of_euro_m)
print('Официальный курс евро по ЦБ с округлением - ', cource_of_euro_m, 'рублей')


def func_cource_of_euro():
    return cource_of_euro_m
