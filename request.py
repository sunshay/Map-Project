import json
import requests

url = 'https://api.punkapi.com/v2/beers/random'

r= requests.get(url) # obtain json string 

data = json.loads(r.text) # we can't parse it with index directly,we need convert it to a dictionnary by json.loads first

print(data[0]['name']) #parse it with index