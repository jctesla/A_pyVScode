# Lo que hace este codigo es crear un BD con el nombre de la institucion (Universidades) y en un record al costado un json que contiene todo las ubic geolatlong de c/alumno.
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
import os

api_key = False

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"                     # Mr Duck = this url is the rule to retrieve a JSON data from MrsDuck Server
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"      # My GoogleApi = this url is the rule to retrieve a JSON data from GoogleApi.

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

# Create Conn to BD
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute(f'CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')

# we Ignore SSL certificate errors from web page https://
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Now opwn a file & read line by line each record, HOW?
# el line in fh, lee una linea hasta econtrar LF or CR

# Verificamos si Existe el File/Dir    before dir './where.data'
print(f'...path actual = {os.getcwd()}')
PATH = './where.data'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
   print(f'Si el File existe pero no se sabe si tiene Datos')
   
   fh = open("where.data")
   count = 0

   for line in fh:                                 
       if count > 10 :
           print(f'Retrieved 5 locations, restart to retrieve more')
           break
       
       # evaluate if 'address' exist or not in DB.
       # strip() qita espacios de los extremos del string  
       address = line.strip()                       
       # SELECT geodata FROM Locations WHERE address = <memory at 0x0000000002DC8588>
       # cur.execute(f'SELECT geodata FROM Locations WHERE address = { memoryview(address.encode()) }')
       cur.execute(f'SELECT geodata FROM Locations WHERE address = "{address}"')
       print(f'SELECT geodata FROM Locations WHERE address = {address} ')
       
       try:
           data = cur.fetchone()[0]                  # busca si hay un reg devuelto por el SELECT, sino existe 'genera una exception'
           print("Found in database ",address)
           continue                                  # si existe en la BD :. goto the next sentence in 'for line in fh:' 
       except:
           pass                                      # continue the next sentence from this point.
   
   
       # build a dictionary needed for requesting to GoogleAPI connection: Ej
       # Ej Rqst un dir donde vivo = https://py4e-data.dr-chuck.net/json?address=Jiron+Jose+Nicolas+Rodrigo+Santiago+de+Surco+Lima+Peru&key=42
       # Ej Rqst un dir de una Universidad = http://py4e-data.dr-chuck.net/json?address=AGH+University+of+Science+and+Technology&key=42   
       parms = dict()
       
       parms["address"] = address
       if api_key is not False: 
           parms['key'] = api_key
           
       url = serviceurl + urllib.parse.urlencode(parms)
       # dict ={'address':address, 'key':api_key}
   
       # we espect to retrieve a JSON string
       print(f'Retrieve url from GoogleApi ={url}')
       uh = urllib.request.urlopen(url, context=ctx)                                 # retrieve a json GoogleAPi link.
       data = uh.read().decode()                                                     # format json data from GoogleServer.
       
       print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
       count = count + 1
   
       # With data retreived, we Try to Create a JSON Objt
       try:
           js = json.loads(data)
       except:
           print(data)  # We print in case unicode causes an error
           continue
   
       # Read if connection data of JSON Obj was good or bad.  
       if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
           print('==== Failure To Retrieve ====')
           print(data)
           break
   
       # If all ready ok, them, Insert addrss and json string to BD.
       cur.execute('''INSERT INTO Locations (address, geodata)
               VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
       
       # Close Connec to DB.
       conn.commit()
       
       # a Delay
       if count % 10 == 0 :
           print('Pausing for a bit...')
           time.sleep(5)
else:
    print(f'No existe este File o Directorio')

    
print("NOTE: Run geodump.py to read the data from the database so you can vizualize it on a map.")
