import json

# open a json file 
f = open('congo.json')

#return a json file as a dictionnary
datas = json.loads(f.read())

for x in datas['properties']:
    print(datas)
    
print(datas)
f.close()