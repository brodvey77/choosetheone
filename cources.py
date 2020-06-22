import requests
from bs4 import BeautifulSoup

url = 'https://cbr.ru/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('div', {'class':'row flex-nowrap'})
table_2 = table.findAll('div', {'class':'indicator_el_value mono-num'})

for sum in table_2:
    print(sum.text)

# table_2 = table_2.text

#
# print(table_2)



