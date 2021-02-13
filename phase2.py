import requests
import json

file = open('userinput.json', "r")
userdata = json.loads(file.read())
print(userdata)

API_key = 'e3c2904c48b5256e27a53b87e81795ce'

global list_temp
list_temp = []
for city in userdata['City']:
    try:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric' % (city, API_key)
        resp = requests.get(base_url)
        data = resp.json()
        print(data)
        ftemp = data['main']['temp']
        print(ftemp)
        list_temp.append(ftemp)
    except:
        print("%s not available" % city)
        list_temp.append(0)
        continue
