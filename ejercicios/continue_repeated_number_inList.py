# permite saber cunatas veces se repite un nº en una lista siempre y cuando sea continuo.
import itertools
import sys                                      
x = [1,1,1,2,2,2,2,2,3,3,1,1,0,0,0,5]

# cuantas veces se repite un nº pero de forma continua.
y = [{n:len(list(nn))} for n,nn in itertools.groupby(x)]
print(f'version python = {sys.version} ',f'\n resultado = {y} \n')

# version python = 3.7.13 (default, Mar 28 2022, 08:03:21) [MSC v.1916 64 bit (AMD64)]  
# 1º crea esto = [{1: '[1, 1, 1]'}, {2: '[2, 2, 2, 2, 2]'}, {3: '[3, 3]'}, {1: '[1, 1]'}, {0: '[0, 0, 0]'}, {5: '[5]'}]
# resultado = [{1: 3}, {2: 5}, {3: 2}, {1: 2}, {0: 3}, {5: 1}]


#Otra forma de hacerlo: pero sin que sea necesarimente continuo
import numpy as np

# genero un arreglo de 50 Nºs Aleatorios 
# norma inicial = 60 y varioan de +/-20 unidades
L = np.round( np.random.normal(60, 20, 50))     # con numeros enteros sin decimal
L = np.round( np.random.normal(60, 20, 50),2)   # con numeros enteros con 2 decimales

#----------------------------------------------------------------
# CUANTAS VECES SE REPITE un NUMERO DE LA LISTA?
L = [ 37.,  40.,  56.,  77.,  82.,  38.,  46.,  65.,  62.,  45.,  56.,
        57.,  30.,  58.,  48.,  96.,  71.,  58.,  49.,  51.,  57.,  47.,
       110.,  56.,  87.,   6.,  62.,  29.,  71.,  62.,  93.,  48.,  51.,
        48.,  75.,  40.,  53.,  35.,  50.,  76.,  98.,  45.,  72.,  28.,
        68.,  57.,  71.,  68.,  52.,  80.]

# creo un arreglo donde no se repitan (frec) ls notas:
# set oermite copiar todo los elementos pero sin repeticiones
M = list(set(L))

# SOLUCION 01:
# 1º creamos un diccionario(key;val) de la misma dimension q el 'L'
# luego buscamos cuantas veces se repite una nota(nº) de 'M' en 'L'
# de tal forma q vamos agregando en 'val' el nº de veces q se repite
# la nota de M en L:
dic = {n:0 for n in M}
for m in M:
  for l in L:
    if m==l:
      dic[m] += 1

print("1. ",f"dic= {dic}\n")
      
# Result:
# {37.0: 1, 40.0: 2, 56.0: 3, 77.0: 1, 82.0: 1, 38.0: 1, 46.0: 1, 65.0: 1,
# 62.0: 3, 45.0: 2, 57.0: 3, 30.0: 1, 58.0: 2, 48.0: 3, 96.0: 1, 71.0: 3,
# 49.0: 1, 51.0: 2, 47.0: 1, 110.0: 1, 87.0: 1, 6.0: 1, 29.0: 1, 93.0: 1,
# 75.0: 1, 53.0: 1, 35.0: 1, 50.0: 1, 76.0: 1, 98.0: 1, 72.0: 1, 28.0: 1,
# 68.0: 2, 52.0: 1, 80.0: 1}

# SOLUCION 02:
dic ={n:1 for n in M}
for m in M:
  dic[m] = L.count(m)

print("2. ",f"dic= {dic}\n")  

# Result:
# dic= {6.0: 1, 28.0: 1, 29.0: 1, 30.0: 1, 35.0: 1, 37.0: 1, 38.0: 1, 40.0: 2,
# 45.0: 2, 46.0: 1, 47.0: 1, 48.0: 3, 49.0: 1, 50.0: 1, 51.0: 2, 52.0: 1,
# 53.0: 1, 56.0: 3, 57.0: 3, 58.0: 2, 62.0: 3, 65.0: 1, 68.0: 2, 71.0: 3, 72.0: 1,
# 75.0: 1, 76.0: 1, 77.0: 1, 80.0: 1, 82.0: 1, 87.0: 1, 93.0: 1, 96.0: 1, 98.0: 1, 110.0: 1}

# SOLUCION 03:
dic ={n:L.count(n)  for n in M}
print("3. ",f"dic= {dic}\n")

# Result:
# dic= {6.0: 1, 28.0: 1, 29.0: 1, 30.0: 1, 35.0: 1, 37.0: 1, 38.0: 1, 40.0: 2,
# 45.0: 2, 46.0: 1, 47.0: 1, 48.0: 3, 49.0: 1, 50.0: 1, 51.0: 2, 52.0: 1,
# 53.0: 1, 56.0: 3, 57.0: 3, 58.0: 2, 62.0: 3, 65.0: 1, 68.0: 2, 71.0: 3, 72.0: 1,
# 75.0: 1, 76.0: 1, 77.0: 1, 80.0: 1, 82.0: 1, 87.0: 1, 93.0: 1, 96.0: 1, 98.0: 1, 110.0: 1}


# using -zip-
a = [1,2,3,4]
b = [10,11,12,13]
L = list(zip(a,b))
print('1. L=',L)
 
c = [20,30,40,50]
L = list(zip(a,b,c))
print('2. L=',L)
 
  
  

#lista = [1,2,3,1,2]
#dict(zip(lista,map(lambda x: lista.count(x),lista)))
           
           
     