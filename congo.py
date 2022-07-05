import json

with open('congo.json') as json_file:
    datas = json.load(json_file)
    
    print(datas[0]['properties'])
    # print(datas[0]['geometry'])
   
    
    
    