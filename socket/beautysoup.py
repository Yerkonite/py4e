# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
y = []
for tag in tags:
    # Look at the parts of a tag
    x = tag.contents[0]
    x = x.split()
    #print(type(x))
    if len(x) > 0:
        y = y + x
jiyn = 0
for z in y:
    jiyn = jiyn + int(z)
print(jiyn)