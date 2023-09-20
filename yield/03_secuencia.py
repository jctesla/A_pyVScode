def numeros_pares(n):
    for i in range(n):
        yield i

# Uso del generador
generador = numeros_pares(10)                   # yield sirve mas que todo para leer una secuencia muy grande de valores
                                                # que puede ocupar mucha memoria, y la idea de 'yield' es que no se usa toda la memoria
                                                # para almacenar esta secuencia, sino genere valor por valor lo que usaria poca memoria.
cntr = 0
for num1 in generador:  
    if (cntr==5):
      print('break = 5')
      break
    cntr+=1
    print(num1)

print('\nContinuamos con la secuencia\n')

for num2 in generador:
    print(num2)