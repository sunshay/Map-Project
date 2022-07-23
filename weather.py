import json
# weather = urllib2.urlopen('url')
with open('weather.json') as file:
    weather = json.load(file)

print(weather)
#wjson = weather.read()
# wjdata = json.loads(wjson)
# print weather['data']['current_condition'][0]['temp_C']