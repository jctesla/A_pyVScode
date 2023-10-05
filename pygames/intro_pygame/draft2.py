import numpy as np
import random
'''

# gen = 2x3 (nºs aleatorio entre 10 y 100)
m1 = np.random.randint(10,100,(2,3), dtype='int32')
print(f'Matriz m1 =\n {m1}')

# rotate 90º 2x3
m2 = np.rot90(m1)
print(f'Matriz 90º m2 =\n {m2}')

m3 = np.rot90(m2)
print(f'Matriz 90º m2 =\n {m3}')

m4 = np.rot90(m3)
print(f'Matriz 90º m2 =\n {m4}')

m5 = np.rot90(m4)
print(f'Matriz 90º m2 =\n {m5}')
'''
#-----------------------------
matriz = [
           [10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]
         ]
print(f'Matriz cnp =\n {type(matriz)}')

cnp = np.array(matriz)

print(f'Matriz cnp =\n {type(cnp)}\n { cnp}')  
