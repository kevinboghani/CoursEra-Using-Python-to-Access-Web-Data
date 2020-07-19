import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Courtny.html'
pos = int(input('Enter position: '))
count = int(input('Enter count: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for i in range(count):
    newlink = tags[pos-1].get('href')
    html = urllib.request.urlopen(newlink, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print('Retrieving: ',newlink)

