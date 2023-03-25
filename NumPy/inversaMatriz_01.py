# Tenemos la Matriz 'A', calcular su matriz Inversa:
from scipy.linalg import inv as invMtx
import numpy as np

A = np.array([
              [2,-2,2],
              [2,1,0],
              [3,-2,2]
            ])

Ainv = invMtx(A)                                                # matriz Inversa de A
Ainv = np.round(Ainv,2)                                         # redondeo a 2 decimales. 
print(f'La Inversa de A={Ainv}')

# out:
array([[-1. , -0. ,  1. ],
       [ 2. ,  1. , -2. ],
       [ 3.5,  1. , -3. ]])

# probamos resultado : NOTA
# se sabe q una Matriz A * A^-1 = I
# Matriz (A) por producto punto de su Matriz Inversa (A^-1) = Matriz Identidad(I).

M_Idnt = np.dot(A,Ainv)
print(f'Matriz Identidad = {M_Idnt}')

# Out:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
