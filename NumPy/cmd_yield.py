# experiment w 'yield'
# To understand what yield does, you must understand what generators are. And before you can understand generators, you must understand iterables.

# Iterables
# When you create a list, you can read its items one by one. Reading its items one by one is called iteration:
# mylist = [1, 2, 3]
# for i in mylist:
#    print(i)

# NOTE: 'yield' not allowed outside of a function or lambda, and just excecuted one time to get data

import time

def sumador(max):
    print("Begin Sumador():")
    n=0
    lst = []
    while n < max:
        lst.append(n)
        n=n+10
    print("Fin Sumador():")
    return lst


def contador(max):
    print("Begin Contador():")
    n=0
    while n < max:
        yield n
        n=n+10
    print("Fin Contador():")

#------------------------------
print("IniCreate 2 CaLLs to Contador()\n") 
cnt = contador(40)              # No Salta a desarrollar la funcion solo asigna al parecer una ref.
smd = sumador(30)               # Si Salta a desarrollar la funcion y devuelve un resultado

# A continuacion hay 3 formas de jalar la info de 'yield'

#-----CASO 1----------
# in this case each next(cnt) Retrieve 1 item 
# from the funct iterator by calling __next__() method
# in this case we dont use memory
#print(next(cnt))
#print(next(cnt))          
#print(next(cnt))
#print(next(cnt))

print(smd)


#-----CASO 2----------
# In this case excute all the function complete
# and give a list to memory
L = list(cnt)                 # ejecuta toda la funcion
if len(L):
  print(f'cnt={L[2]}')
  print(f'cnt={L[1]} \n')

L = list(smd)
if len(L):
  print(f'cnt={L[2]}')
  print(f'cnt={L[1]} \n')


#-----CASO 3----------
# al igual q el caso anterior el for ya jala todo la info
# a memoria.
for i in cnt:
    print(f"from Main() i={i}") 


for i in smd:
    print(f"from Main() i={i}") 
