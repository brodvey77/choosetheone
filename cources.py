import requests
from bs4 import BeautifulSoup

url = 'https://cbr.ru/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('div', {'class':'row flex-nowrap'})
table_2 = table.findAll('div', {'class':'indicator_el_value mono-num'})

cource_of_dollar = 0
for sum in table_2[1:]:

    cource_of_dollar = sum.text

print('Курс доллара ' + cource_of_dollar[:7])





# table_2 = table_2.text

#
# print(table_2)



