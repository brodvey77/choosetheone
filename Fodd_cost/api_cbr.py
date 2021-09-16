import requests
from math import ceil

url ='https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)
if response.status_code == 200:
    text = response.json()

cource_of_eur = ceil(text['Valute']['EUR']['Value'])


