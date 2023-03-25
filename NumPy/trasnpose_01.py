import numpy as np
# A transpose makes the array non-contiguous
m = np.arange(0, 5, 0.5, dtype=float)             # crea una arry [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]

m = np.array([[1,2,3],[4,5,6]])                   # Fila x Cols
y = m.T                                           # Cols-->Fila x Fila-->Cols
print(f'm:\n{m}')
print(f'Trasnpuesta de m.T :\n{y}\n')

# numpy.empty / numpy.zeros : empty no escribe los valores de c/elemnt del Array
a = m[0:2,0:2]
print(f'm[0:2] :\n{a}\n')

z = np.reshape(a,4)
print(f'np.reshape :\n {z}')