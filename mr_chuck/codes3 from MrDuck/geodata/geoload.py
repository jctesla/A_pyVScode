# Lo que hace este codigo es crear un BD con el nombre de la institucion (Universidades) y en un record al costado un json que contiene todo las ubic geolatlong de c/alumno.
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"                     # from Mr Duck = this url is the rule to retrieve a JSON data from MrsDuck Server
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"      # from GoogleApi = this url is the rule to retrieve a JSON data from GoogleApi.

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

# Create Conn to BD
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :  # before 200 instead of 5
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    # SELECT geodata FROM Locations WHERE address= <memory at 0x0000000002B6AB80>
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()), ))
    
    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    # build a string API connection: Ej
    # http://py4e-data.dr-chuck.net/json?address=AGH+University+of+Science+and+Technology&key=42    
    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    # we espect to retriece a JSON string
    print(f'Retrieve url from GoogleApi ={url}')
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    # Try to Create a JSON Objt
    try:
        js = json.loads(data)   
    except:
        # We print in case unicode causes an error
        print(data)
        continue

    # Validate data of JSON Obj retrieved    
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
