import json

with open('country.json') as json_file:
    datas = json.load(json_file)
    
    print(datas[3]['country'])