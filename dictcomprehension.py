b = {'four': [4, 4.0], 'two': 'to', 'three': 3.0, 'one': 1}
print(b.keys()) 
print(b.values())
print(b.items()) #access each key-value pair within a dictionary using the items()
#dict_variable = {key:value for (key,value) in dictonary.items()}


print(type(b)) 
b['one'] = 1.0 # append in dictionnary
print(b)
del b['two'] # delete in a dictionnary
print(b)
b.clear() # erase all
print(b)