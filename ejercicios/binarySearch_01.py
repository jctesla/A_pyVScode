import random

# Binary Search
def bs(lstNm, nro):

    if not(str(nro).isnumeric()):
       # Valido si el Nro es un numero 
       print(f'Nro={nro} noes un Nro')
       flg=False
            
    else:
       # Recorrido x todo el List        
       lst=lstNm
       size = len(lst)
       mitad = size//2
       flg=True
       
       while (flg and mitad!=0):
          print(f'lst={lst} / mitad nro={lst[mitad]}') 
          
          if lst[mitad] == nro:                                       # siempre el nro buscado va caer en alguna mitad.              
             print(f'Encontrado en Nro={nro} / inx={mitad}')
             flg = False
             
          elif nro < lst[mitad]:
             lst = lst[0:mitad+1]
             mitad = len(lst)//2
          elif nro > lst[mitad]:
             lst = lst[mitad:]
             mitad = len(lst)//2

    return 1

    
# Generador de nrs del 0..100
def ale():
    return(int(random.random()*100))


#------------ MAIN -----------------------------
rng = int(input("Ingrese un rango p generar vlas aleaotorios:"))   
lstNm =  random.sample(range(500),rng)                                        # de un rango de 500 nros elije aleatoriamente sin repetir un List de 'rng' elementos.

# 1ro Ordeno lista asc():
print(f'len = {len(lstNm)} \n{lstNm}')
print(f'Ordenando Lista...')
lstNm.sort()
print(f'{lstNm}\n')

# 2do Busqueda Binaria.
nro= int(input('lija un Nro: '))
bs(lstNm, nro)


# 3ro Busqueda de Indice
# devuelve Indice del elemnt = valor
idx = lstNm.index(nro)
print(f'Nro {lstNm[idx]} se ubica en idx={idx}')


# del Paso 1ro y 2do:
# len = 23
# [387, 63, 317, 75, 318, 172, 314, 297, 40, 89, 405, 477, 120, 390, 78, 104, 7, 478, 397, 265, 133, 17, 0]
# Ordenando Lista...
# [0, 7, 17, 40, 63, 75, 78, 89, 104, 120, 133, 172, 265, 297, 314, 317, 318, 387, 390, 397, 405, 477, 478]
# 
# lija un Nro: 63
# lst=[0, 7, 17, 40, 63, 75, 78, 89, 104, 120, 133, 172, 265, 297, 314, 317, 318, 387, 390, 397, 405, 477, 478] / mitad nro=172
# lst=[0, 7, 17, 40, 63, 75, 78, 89, 104, 120, 133, 172] / mitad nro=78
# lst=[0, 7, 17, 40, 63, 75, 78] / mitad nro=40
# lst=[40, 63, 75, 78] / mitad nro=75
# lst=[40, 63, 75] / mitad nro=63
# Encontrado en Nro=63 / inx=1