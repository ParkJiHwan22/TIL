import requests

students = ['jihwan', 'yoojin']

for name in students:
    URL = f'https://api.nationalize.io/?name={name}'
    response = requests.get(URL).json()
    # print(response)
    # (response.get('country')[0])
    print(name, response.get('country')[0].get('country_id'))