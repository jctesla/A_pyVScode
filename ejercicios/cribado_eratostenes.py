"""
Implementación del Cribado de Eratóstenes
"""

def cribado_eratostenes(n):
  total=0
  numeros = list(range(2, n+1))           # Creamos una lista con todos los números del 2 al n
                                          # numeros =  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
  # Iniciamos el crifrado                 # en la 1ra vuelta se marcan como None todo los multiplos de 2, excepto el mismo Nro.
  for i in numeros:                       # en la 2da vuelta saldra algo asi: [2, 3, None, 5, None, 7, None, 9   , None, 11, None, 13, None, 15  , None, 17, None, 19, None]
      print('numeros = ', numeros)        # en la 3ra vuelta saldra algo asi: [2, 3, None, 5, None, 7, None, None, None, 11, None, 13, None, None, None, 17, None, 19, None]
                                          
      if i is None:                       # Si el número ya ha sido marcado como no primo, saltamos a la siguiente iteración
          continue
      
      total+=1                            # Si el Nº es primo, marcamos todos sus múltiplos como no primos
      for j in range(i*2, n+1, i):
          numeros[j-2] = None
  
  return total,[num for num in numeros if num is not None]  # Devolvemos una lista con los números primos encontrados



# Encontramos los primeros números primos
total,primos = cribado_eratostenes(20)
# Imprimimos los resultados
print(f"Total de Nºs {total},  Nºs primos= {primos}")               # Total de N�s 8,  N�s primos= [2, 3, 5, 7, 11, 13, 17, 19]