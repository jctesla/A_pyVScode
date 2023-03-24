print("---------------List.append() modo 00--------------")
e = []
for i in range(5):
	if i % 2 == 0:
		e.append(i)
print(f'Los pares de e = {e}')										# el valor de e = [0, 2, 4]
print()


print("-----------Asignar Variable modo 01----------------")
a,b,*c = 0,1,2,3,4																# al asignar de forma grupal los valores se reparten segun el orden.
print(f'los valores de a={a}, b={b}, c={c}\n')		# quedaria asi = valores de a=0, b=1, c[2, 3, 4]


print("-----------Asignar Variable modo 02----------------")
a,*b,c = 0,1,2,3,4															# al asignar a un grupo de variables un grupo de valores de esta forma
print(f'los valores de a={a}, b={b}, c={c}\n')		# quedarin asi los valores de a=0, b=[1, 2, 3], c=4


print("-----------Using set & frozenset 03----------------")
"""
UN Conjunto de elementos se define en python entre llaves {}, o mediante el comando 'Set',
Al definir un conjunto, podemos hacer intersecciones, uniones de conjuntos de sus elementos.
En el sngt Ej, Si no usara la sentencia "set", saldria error en la operacion A & B
NOTA: set a su vez no deja q se repitan los elementos por q es un conjunto matematico.
"""
A = set([0,1,2,3,4])														# de un List ---> Conjunto.												
B = set([7,6,5,4,3])
print(f'Conjunto A = {A}')											# A = {0, 1, 2, 3, 4}		lo ordna a demás
print(f'Conjunto B = {B}')											# B = {3, 4, 5, 6, 7}
print(f'Interseccion de A & B = {A & B} \n')		# A & B = {3, 4}

# Frozenset Convierte a un Conjunto en inmutable.
A.add(6)
print(f'agrego un nuevo elemento al conjunto A = {A}')
tmpA = frozenset(A)															# crea y Convierte a un Conjunto en inmutable.
# tmpA.add(7)	
print(f'No Puedo agregar mas elementos al conjunto tmpA = {tmpA}\n')

print("-----------Forma de Crear un Conjunto 04----------------")
#The range() function is used to generate a sequence of numbers.
A = {x*2 for x in range(5)}											# puedo crear una serie con ecuacion.
print(f'El conjunto A = {A}')										# El conjunto A = {0, 2, 4, 6, 8}
M = [range(5)]																	# la asignacion de M = range(0,5), por si solo no se generan los elementos
print(f'Range(1,5)={M}\n')											# ERR no se genera un list, solo una expresion "range(0,5)"


print("---------Diccionario key<int):val<int> 05----------")
sq = {}																						# declaro un dictionary vacio.
for x in range(10):
	sq[x] = x + 1																		# genero una <key:value>, ya que key=[x] y value= x+1
print(f'El valor de sq={sq}\n')										# El valor de sq={0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:10}

print("---------Diccionario key<str):val<int> 06------------")
# None  = es una palabra reservada
sq = {str(x):None  for x in range(10)}						# { <key> : <value=funcion(None)>} 
print(f'El valor de sq={sq}\n')										# El valor de sq={'0':None, '1':None, '2':None, '3':None, '4':None, '5':None, '6':None, '7':None, '8':None, '9':None}

print("---------Diccionario key<str):val<int> 07------------")
sq = {str(x):x+1  for x in range(10)}							# es equivalnete a un diccionario con key:value { <key> : <value=funcion()> }
print(f'El valor de sq={sq}')											# El valor de sq={'0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10}
print()


print("---------Diccionario con elemento variable 08-------------")
sq = {x:x+1  for x in range(10)}									# { <int> : funcion() }

print(f'El valor de sq={sq}')											# El valor de sq={0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
print(f'los keys de sq = {sq.keys()}')						# los keys de sq = dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'los valores de sq = {sq.values()}')				# los valores de sq = dict_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f'los items key value = {sq.items()}')			# los items key value = dict_items([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)])
print(f'dame el valor de key(2) = {sq[2]}')				# dame el valor de key(2) = 3
print()


print("-----------------Objetos ITERABLES 09--------------------")
"""
Los iteradores están en bucles, comprensiones, generadores, etc. pero están ocultos a la vista.
Iterator en Python es simplemente un objeto sobre el que se puede iterar devolverá datos, un elemento a la vez.
un objeto iterador debe implementar dos métodos '__iter__()' y  '__next__()', llamado protocolo iterador .
La mayoría de los contenedores integrados en Python como: list , tuple , string , etc. son iterables.
• __next__: This returns the next item of the container 
• __iter__: This returns the iterator itself

'next(obj)' es lo mismo 'obj.__next__()'
"""
myit=iter('abcd')
#arry = list(myit)
#print(f'Valor de obj = {arry}')												# Valor de obj = ['a', 'b', 'c', 'd']
print(f'Valor de next(obj) = {next(myit)}')							# a implementa naturalmente el metodo __next__
print(f'Valor de next(obj) = {next(myit)}')							# b
print(f'Valor de next(obj) = {next(myit)}')							# c
print(f'Valor de next(obj) = {myit.__next__()}')				# d
print(f'Valor de next(obj) = {myit.__iter__()}')				# <str_iterator object at 0x0000000002987388>
#print(f'Valor de next(obj) = {next(obj)}')							# Si llamo despues del ultimo elemento, saldra ERR
print()


print("---------Implemtando Clase con Potocolo ITERABLE 10-------------")
# La Clase debe implentar los metodos Iterables;
class iterCount:
	def __init__(self,step):															# asi se declara el metodo de Instanciamiento de la clase
		self.step = step																		# selft es de la propia clase q sirve como transportador de valor en toda la clase.
	
	def __next__(self):																		# metodo next para el protocolo Iterable
		if self.step <= 0:
			print('fin de Iteracion- ERR')
			raise StopIteration																# comando como break, o deterner iteraccion.
		else:
			self.step -= 1
		return self.step

	def __iter__(self):																		# metodo iter para el protocolo Iterable
		return self


obj = iterCount(4)																	# asigno una clase de Objeto, q Implementa el Protocolo Iterable
try:
    while True:
        print(next(obj))
except:
    print('termino interaccion')
print()


print("---------YIELD(rendimiento) Statement generator 11-------------")
print()
"""
Los generadores de Python son una forma simple de crear iteradores. Todo el trabajo que mencionamos anteriormente es manejado automáticamente por los generadores en Python.
Simplemente hablando, un generador es una función que devuelve un objeto (iterador) sobre el que podemos iterar (un valor a la vez).
"""

print("---------------List and Dict 12--------------------")
fruits = [
					{'name':'apple', 'price':20},
					{'name':'orange', 'price':10},
					{'name':'banana', 'price':15},
				 ]

for fruit in fruits:
  	print(	[fruit['name'] ])																									# por cada interaccion imprime.
print()
print(	[fruit['name']  for fruit in fruits ]	)																# = ['apple', 'orange', 'banana'] 	, exp:1ro llena el arreglo [] y luego lo imprime, x eso sale asi.
print(	[fruit['name']  for fruit in fruits 	if fruit['name'][0] == 'a'] )		# = ['apple']	, 	exp: lee todo los items q tengan la 1ra letra = 'a', si esto es TRUE, agrega el resultado = fruit['name'], llena solo lo q cumpla la condicion.
print()


print("---------------lambda es una funcion tambien 13--------------------")
'''
>>>add = lambda x,y : x + Y 																											# solo debe usarse en tu shell interactivo, pero p un programa en un file nop.
add(1,2)
3
'''
lista = [1,2,3,4]
e = lambda x: x > 2
numeros = filter(e, lista)																										# solo filter es decir evaluaciones, no modificiaciones.
print(list(numeros))																													# [3, 4]


print("---------------lambda es una funcion tambien 14--------------------")
# busco de un conjunto de nros los valores pares
d = [x for x in range(10) if x%2 == 0]
print(d)																																				# = [0, 2, 4, 6, 8]


print("---------------lambda es una funcion tambien 15--------------------")
# busco los puntos pares(y) de una ecuacion de curva positiva: y = x^2 + 1

# Genero los puntos X q cumplan con el criterio de y = par
pX = [x for x in range(10) if (x**2+1)%2 == 0]																	# Solo es verdadero si x^2+1 = es un Nro Par
pY = [y**2+1 for y in pX]																												# Con el Resultado de pX solo calculo Y, por q la condicion ya esta efectuada en X	
# pY = [x**2+1 for x in range(10) if (x**2+1)%2 == 0]														# esta seri otra forma, da el mismo resultado.	
print(f'pX= {pX}')
print(f'pY= {pY}')

# lo Graficamos
#Line and Scatter Plots
from pylab import plot, show
import matplotlib.pyplot as plt
#import plotly.express as plt
plt.scatter(pX, pY)
show()

print("---------------Convert String to Bytes 16--------------------")
def strInBits(frase):
    byte = ''
    for i in frase:
        byte = byte + bin(ord(i)) + ' '																					# bin, convierte un Int en una representacion string de byte.
    return byte
        
print(strInBits('Hola'))																												# 'Hola' = 0b1001000 0b1101111 0b1101100 0b1100001