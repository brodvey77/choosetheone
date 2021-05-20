import requests

url ='https://www.cbr-xml-daily.ru/daily_json.js'

# print(requests.get(url))

response = requests.get(url)
if response.status_code == 200:
    text = response.json()

# print(str(text['Date'][:10]))
cource_of_usd = text['Valute']['USD']['Value']
cource_of_eur = text['Valute']['EUR']['Value']

# print('Date: '+ str(text['Date'][:10]))
# print(cource_of_usd)
# print(cource_of_usd)

