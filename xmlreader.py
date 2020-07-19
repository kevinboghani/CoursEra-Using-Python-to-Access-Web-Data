import xml.etree.ElementTree as ET
import urllib.request, urllib.error, urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_751383.xml'
x = urllib.request.urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(x)
nums = tree.findall('.//count')
sum = 0
for num in nums:
    num = int(num.text)
    sum = sum + num
print('Sum:',sum)
