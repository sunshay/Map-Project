import json

# open a json file 
f = open('congo.json')

#return a json file as a dictionnary
datas = json.load(f)

print(datas)
f.close()