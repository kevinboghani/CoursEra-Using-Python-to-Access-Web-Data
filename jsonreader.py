import urllib.request, urllib.error, urllib.parse
import json

url = input('Enter URL: ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_751384.json'
data = urllib.request.urlopen(url).read()
js = json.loads(data)
print('Retrieving',url)
i = 0
sum = 0
for item in js['comments']:
    x = js['comments'][i]['count']
    i = i + 1
    sum = sum + x

print(sum)
