import json


string = '{"name":"Max", "languages": ["English","French"]}'

# string to object 
data = json.loads(string)


# returns json object as dictionnary
print(type(data))
print("JSON string = ", string)
print()