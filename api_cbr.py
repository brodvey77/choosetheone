import requests

url ='https://www.cbr-xml-daily.ru/daily_json.js'

# print(requests.get(url))

response = requests.get(url)
if response.status_code == 200:
    text = response.json()

print(str(text['Date'][:10]))
print(text['Valute']['USD']['Value'])
print(text['Valute']['EUR']['Value'])
