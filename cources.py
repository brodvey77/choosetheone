import math
import requests
from bs4 import BeautifulSoup

url = 'https://cbr.ru/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.findAll('div', {'class':'indicator_el_value mono-num'})

cource_of_euro = 0
for sum in table[-1:]:
    cource_of_euro = sum.text

print('Курс евро ' + cource_of_euro[:7])
cource_of_euro_m = cource_of_euro[:7]




cource_of_euro_m = cource_of_euro_m.replace(',', '.')
cource_of_euro_m = (float(cource_of_euro_m))
cource_of_euro_m = math.ceil(cource_of_euro_m)
print(type(cource_of_euro_m))







