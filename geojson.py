import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

loc = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'key':42,'address':loc})

u = urllib.request.urlopen(url)

data = u.read().decode()

info = json.loads(data)

print('Retrieved',len(data),'characters')
print('Place_id', info['results'][0]['place_id'])