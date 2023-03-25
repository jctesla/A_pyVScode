# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# NOTA : FUNCIONA BIEN con python 3.8.3
# pero p eliminar el error que indica source : python 3.7.6 desaparece
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup                               # funciona bien apartir del interprete python 3.8.3 reconoce el path de 'bs4'
import ssl



# Ignore SSL certificate errors for https://
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://' + input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()      # Don't use 'for' to get peaces of the data comming from  server
soup = BeautifulSoup(html, 'html.parser')                   # we can use 'context=ctx' to read all ann put it one read(), ofcourse can be to big-

# Retrieve all of the anchor tags/ recuperamos todo los tag = <a.. de la url
#tags = soup('link')
#for tag in tags:
#    print(tag.get('href', None))                            # 


tags = soup('link')
lstDict = dict()

for tag in tags:
    words = tag.get('href', None).split()
    for w in words:
        lstDict[w] = lstDict.get(w,0) + 1
    
    #print(tag.get('href', None))                            # 
for key,val in lstDict.items():
    print(f'nombre:{key}        Tiene : {val}')    
