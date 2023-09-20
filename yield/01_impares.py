def numeros(n):
  for i in range(n):
    yield i


# Uso del generador y almacenamiento en una lista
generador = numeros(10)

for num2 in generador:                # aqui ya genero un step
    print(next(generador))            # aqui genera el sgnt step, x lo que genera posicion impares.

"""
1
3
5
7
9
"""
 