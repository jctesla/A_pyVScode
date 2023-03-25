# En este caso hay lib q permiten hacer todo automatico, 
# lo anterior ya es en caso muy particulares, por eso hay librerias ya especializadas p c/caso.
import urllib.request,urllib.parse,urllib.error

url = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#url = urllib.request.urlopen('https://www.google.com')

# line es como una matriz bidimensional
# 1o decoidificamos = line.decode()
# 2p .strip() = lo convertimos a una cadena, es dcir hacemos una tira por eso lo llaman strip()
# solo leo el cuerpo html

#print(url)
for line in url:
    print(line.decode().strip())        # strip() quita los LfCr del dato, tambien puedes quitar los espacios en blanco etc