# Este ejemplo trata de una pagina q devuelve un JSON file del GCP de goole api map
import urllib.request, urllib.parse, urllib.error      
import json
import ssl

#-------------------------------------------------------------------
# Consulto con API_KEY
api_key = 42

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# api_key = 'AIzaSyDdUhlhpndbEoNtusY2MHFSunk36p8zsMA'                     # key generado desdr mi cuenta juancarlos.dergan@gmail.com
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key == 42:
    mapurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    mapurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

print(f'Seleccion : {mapurl}')


#-------------------------------------------------------------------
# Retreive info from Server in JSON format. 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #----------------------------------------------------
    # 1º Creo un Dictionary. *
    parms = dict()                                                     
    parms['address'] = address                                          # existe header--> key:val :. Key='address' val=<address>       NOTA INPORTANTE: el Key='address' esta declarado en la API, si cambiar sy nomre no saldra nada.
    if api_key is not False: parms['key'] = api_key                     # key:val :. Key='key'     val=<apli_key>
    print(f'parms = {parms} \n')                                        # formato : parms = {'address': <'lima, peru'>, 'key': <42>}

    #--------------------------------------------------
    # 2º parser from dataIn = Dictionary
    url = mapurl + urllib.parse.urlencode(parms)                        # from dataIn = Dictionaey to format Request URL Dictionary --> .urlencode()  *
    print(f'MapUrl = {url}\n')                                          # MapUrl = 'http://py4e-data.dr-chuck.net/json?address=lima%2C+peru&key=42'

    #----------------------------------------------------
    # 3º Me Conecto y Le Consulto al Sevidor. *
    conn = urllib.request.urlopen(url, context=ctx)                     
    data = conn.read().decode()                                         # decode from stream of bits to stram of chars, data decodificada
    print(f'Retrieved Size: {len(data)} characters')
    print(f'Retrieved data: {data}')                                    # Data formateada p Leer, pero no esta en JSON Obj.

    #----------------------------------------------------
    # 4º de chars .txt to json obj
    try:
        js = json.loads(data)                                           
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':            # el serv devuelve = { "results": [...], "status": "OK"}
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    #----------------------------------------------------
    # 5º read all propeties from json obj
    lat = js['results'][0]['geometry']['location']['lat']           # el serv devuelve = { "results": { [ { "geometry":{...}}, "location":{...} }, "status": "OK"}
    lng = js['results'][0]['geometry']['location']['lng']
    print(f'lat={lat} / lng={lng}')                                 # lat -12.0463731 lng -77.042754
                                                                    
    location = js['results'][0]['formatted_address']
    print(location)                                                 # Lima, Peru        



# Resultado:
# Enter location: lima, peru
# Valor parms = {'address': 'lima, peru', 'key': 42}
# 
# Retrieving http://py4e-data.dr-chuck.net/json?address=lima%2C+peru&key=42
# Retrieved 1599 characters
# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "Lima",
#                     "short_name": "Lima",
#                     "types": [
#                         "colloquial_area",
#                         "locality",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Callao Region",
#                     "short_name": "Callao Region",
#                     "types": [
#                         "administrative_area_level_1",
#                         "political"
#                     ]
#                 },
#                 {
#                     "long_name": "Peru",
#                     "short_name": "PE",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 }
#             ],
#             "formatted_address": "Lima, Peru",
#             "geometry": {
#                 "bounds": {
#                     "northeast": {
#                         "lat": -11.7999875,
#                         "lng": -76.78833970000001
#                     },
#                     "southwest": {
#                         "lat": -12.2532891,
#                         "lng": -77.1872186
#                     }
#                 },
#                 "location": {
#                     "lat": -12.0463731,
#                     "lng": -77.042754
#                 },
#                 "location_type": "APPROXIMATE",
#                 "viewport": {
#                     "northeast": {
#                         "lat": -11.7999875,
#                         "lng": -76.78833970000001
#                     },
#                     "southwest": {
#                         "lat": -12.2532891,
#                         "lng": -77.1872186
#                     }
#                 }
#             },
#             "place_id": "ChIJxz7uGfbFBZERSi5FzLlsIBQ",
#             "types": [
#                 "colloquial_area",
#                 "locality",
#                 "political"
#             ]
#         }
#     ],
#     "status": "OK"
# }



# SI es Err: <js['status'] != 'OK'>
# Enter location: Lima, Peru
# parms = {'address': 'Lima, Peru', 'key': 'AIzaSyDdUhlhpndbEoNtusY2MHFSunk36p8zsMA'}
# 
# MapUrl = https://maps.googleapis.com/maps/api/geocode/json?address=Lima%2C+Peru&key=AIzaSyDdUhlhpndbEoNtusY2MHFSunk36p8zsMA
# Retrieved Size: 130 characters
# ==== Failure To Retrieve ====
# {
#    "error_message" : "This API project is not authorized to use this API.",
#    "results" : [],
#    "status" : "REQUEST_DENIED"
# }
