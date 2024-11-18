'''
Por que usar una RAIZ Cuadrada para encontrar si un Nro es primo?
Si quiero saber si No es primo, debo buscar si es divisible por algun numero entre 1 hasta el mismo Nro,
esto puede tomar muchos bucles si es un No Grande, :. una forma de buscar en menos bucles es probar si es
divisible de 1 hasta la raiz cuadrada del Nro.
'''
def esPrimo(n):
    if n < 2:
        return False
    print(f"Va Buscar Divisibles hasta = {int(n**0.5)}")  # al usar la rais cuadrada nos pemite buscar un No divisible en un rango menor de numeros
    for i in range(2, int(n**0.5)+1):                     # es decir si busco el No=16 p saber si es primo, solo basta buscar de 2 hasta 4 p saber si es divisible
        if n%i == 0:                                      # y asi determinar si es primo o no.   
            return False
    return True


# ------------ MAIN -------------------  
import msvcrt
while True:
  e = input("Ing Nro: ")
  if e.isnumeric():
    print(f"Revisando cuantos Nos Primos hay desde 1 hasta {e}")
    P = [n for n in range(int(e)) if esPrimo(n)]
    print(f'Los Numeros primso encontrado =\n{P}')
  elif e.upper() == 'F':
    print("SALISTES..")
    break  
        

  

