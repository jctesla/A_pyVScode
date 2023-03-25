import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# La idea es crear el file; where.js, y myData.
cur.execute('SELECT address, geodata FROM Locations')                   # selecciona toda la tbls de la BD,p leer Nombre Univ y JSON data(geodata).
fhand = codecs.open('where.js', 'w', "utf-8")                           # abrimos el file en codec estandar x segurida, utf-8
fhand.write("myData = [\n")                                             # La mayoría de los códecs estándar son codificaciones de texto, que codifican texto en bytes (y decodifican bytes en texto),    

# Recorro todo los reg de la BD.
count = 0
for row in cur :
    data = str(row[1].decode())                                         # [1] es la columna 'geodata' (JSON)   /   [0] son los nombres(text)          
    try: js = json.loads(str(data))                                     # creo el Obj JSON
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue          # dentro del JSON hay un elemento KEY : status 

    lat = js["results"][0]["geometry"]["location"]["lat"]               # si el status existe y = OK :. creo los elementos de myData, lat y lng
    lng = js["results"][0]["geometry"]["location"]["lng"]               # dentro de la estructura del JSON donde se encuentran las latitudes
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']                       # si las las latitudes <> 0, procedo a jalar tambien la direccion exacta.
    where = where.replace("'", "")                                      # quita las comillas del String de la Direccion.
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")                               # a partir del 1era linea escrita coloca un LF
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"             # resumo lo q va escribir al file where.js =>  lat,lng,address
        fhand.write(output)                                             # lo escribe al file    
    except:
        continue

fhand.write("\n];\n")                                                   # al final de todo la lectura delos reg de la BD cierra blakets de elemento dentro json.
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

