import math
import requests
from bs4 import BeautifulSoup


def func_cource_of_euro():
    url = 'https://cbr.ru/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, 'html.parser')

    table = soup.findAll('div', {'class': 'indicator_el_value mono-num'})

    cource_of_euro = 0
    for sum in table[-1:]:
        cource_of_euro = sum.text

    cource_of_euro_m = cource_of_euro[:7]
    cource_of_euro_m = cource_of_euro_m.replace(',', '.')
    cource_of_euro_m = (float(cource_of_euro_m))
    return str(cource_of_euro_m)
    # cource_of_euro_m_o = math.ceil(cource_of_euro_m)
    # return cource_of_euro_m_o

# print(func_cource_of_euro())