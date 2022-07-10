import json
# weather = urllib2.urlopen('url')
with open('weather.json') as jsonfile:
    weather = json.loads(jsonfile)

#wjson = weather.read()
# wjdata = json.loads(wjson)
print weather['data']['current_condition'][0]['temp_C']