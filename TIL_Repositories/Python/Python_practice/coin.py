import requests

URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'
response = requests.get(URL)
# print(response)
# print(type(response))
# print(dir(response))
# pprint.pprint(response.json())
data = response.json()
print(data.get('data').get('BTC').get('prev_closing_price'))