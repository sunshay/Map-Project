import json
import requests

url = 'https://api.punkapi.com/v2/beers/random'

r= requests.get(url)

data = json.loads(r.text)

print(data[0]['name'])