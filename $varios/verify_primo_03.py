'''
Por que usar una RAIZ Cuadrada para encontrar si un Nro es primo?
Si quiero saber si No es primo, debo buscar si es divisible por algun numero entre 1 hasta el mismo Nro,
esto puede tomar muchos bucles si es un No Grande, :. una forma de buscar en menos bucles es probar si es
divisible de 1 hasta la raiz cuadrada del Nro.
'''
def esPrimo(n,mprimo=[]):                       # Iniciliacion unica.
    #-----------------------------------------  condicion para Salir (es para generar como un POP)
    if n < 2:
        return mprimo
    #-----------------------------------------  Operacion de Recursividad
    n-=1
    flg=False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
          flg = True
          break                                 # Salir del bucle tan pronto como encuentres un divisor
    
    #-----------------------------------------  Evaluacion de Operacion de Recursividad
    if flg==False:
      mprimo.append(n)
      
    #-----------------------------------------  Necesario para generar una recursividad (es como un Push)
    return esPrimo(n,mprimo)


# ------------ MAIN -------------------  
import msvcrt
e = input("Ing Nro: ")
print(esPrimo(int(e)))

  

