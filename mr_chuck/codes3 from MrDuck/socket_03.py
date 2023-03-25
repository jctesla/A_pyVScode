# En este caso hay lib q permiten hacer todo automatico, 
# lo anterior ya es en caso muy particulares, por eso hay librerias ya especializadas p c/caso.
import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# line es como una matriz bidimensional
# 1o decoidificamos = line.decode()
# 2p .strip() = lo convertimos a una cadena, es dcir hacemos una tira por eso lo llaman strip()
for line in fhand:
    print(line.decode().strip())