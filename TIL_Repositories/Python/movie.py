import requests

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'language' : 'ko_KR',
    'region' : 'KR'
}

response = requests.get(BASE_URL+path, params=params).json()
# print(response)
print(response.get('results')[0])