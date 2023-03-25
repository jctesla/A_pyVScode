# En este caso hay lib q permiten hacer todo automatico, 
# lo anterior ya es en caso muy particulares, por eso hay librerias ya especializadas p c/caso.
# en este ejemplo creamos un contador de palabras cuantas eces se repite una palabra.
import urllib.request,urllib.parse,urllib.error
url = 'http://data.pr4e.org/romeo.txt'              # devuelve una .txt
#url = 'https://www.google.com'

miUrl = urllib.request.urlopen(url)

cntr = dict()                                       # creo un Diccionario vacio.            
for linea in miUrl:
    words = linea.decode().split()                  # Leo una Linea del .TXT; decode() permite decodificar y llevar el dato a un string  strip() permite quitar lo LF CR
    for w in words:
        cntr[w] = cntr.get(w,0) + 1                 # agrego datos a mis Diccionario, con la sgnt sentencia p evito repetir las palabras, p luego poderlas contar.
print(cntr)                                         # si el key q lee no existe :. devuelve = 0 :. crea un elemento nuevo con key = w y val = 0 + 1 = 1        
