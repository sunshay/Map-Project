import json

with open('zipcode.json') as json_file:
    datas = json.load(json_file)
    
    print(datas[0]['country'])
    print(datas['places'][0]['post code'])
    print(datas['places'][1]['post code'])

    adress = 