def numeros_pares(n):
    for i in range(n):
        yield ('palabra larga' + str(i))

# Uso del generador
generador = numeros_pares(20)                  # yield sirve mas que todo para leer una secuencia muy grande de valores
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
    if (cntr==10):
        print('break = 10')
        break
    cntr+=1
    print(num2)
    
    
print('\nContinuamos con la secuencia\n')


while True:
    try:
        v = next(generador)
        print(v)
    except Exception:
        print("Termino")
        break    
    
"""
demostramos como se mantiene la secuencia almacenada en memoria.
palabra larga0
palabra larga1
palabra larga2
palabra larga3
palabra larga4
break = 5

Continuamos con la secuencia

palabra larga6
palabra larga7
palabra larga8
palabra larga9
palabra larga10
break = 10

Continuamos con la secuencia

palabra larga12
palabra larga13
palabra larga14
palabra larga15
palabra larga16
palabra larga17
palabra larga18
palabra larga19
Termino
    
"""