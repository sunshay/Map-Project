import json
Person = dict(Name = "Allan Smith",man=True, age=45, siblings=["Yae","Samuel","Liz","Ammon"],Pet=None)
# print(Person)
print("Datatype before conversion: ",type(Person))
json_string = json.dumps(Person)
print("Datatype after conversion: ",type(json_string))
# print(Person.keys()) 
# for i in Person.keys():
#print(i)

# print(Person.items()) 
# for k in Person.items():
    # print(k)

# for j in Person.values():
    # print(j)