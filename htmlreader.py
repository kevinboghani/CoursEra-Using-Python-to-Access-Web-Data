import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_751381.html'
html = urllib.request.urlopen(url, context=ctx).read()
x = BeautifulSoup(html,'html.parser')

counts = 0
sum = 0
tags = x('span')
for tag in tags:
    for nums in tag.contents:
        num = int(nums)
        counts += 1
        sum = sum + num
print('Counts =',counts)
print('Sum =',sum)

