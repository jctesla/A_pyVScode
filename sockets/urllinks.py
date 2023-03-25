# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup       #BeautifulStoneSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://' + input('Enter Url:')
print(f'Url Ingresado = {url}\n')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# esto signif q va jalar todos los tags <a... href
# Ej si encuentra en la url:
# <a aria-label="Microsoft Teams para Educaci&#243;n Educaci&#243;n" class="c-uhff-link" href="https://www.microsoft.com/education/products/teams" data-
# jala : https://www.microsoft.com/education/products/teams
tags = soup('a')
print(f'Se hizo un -Web Scraping-, criterio= tag href :')
for tag in tags:
    print(tag.get('href', None))
    
 