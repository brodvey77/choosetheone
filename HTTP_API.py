import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=xml&starttime=2019-01-01&endtime=2019-01-02&latitude=51.51&longitude=-0.12&maxradius=180'
response = requests.get(url, headers={'Accept':'application/json'})

print(response.json())