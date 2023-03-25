import random as rndm
L = rndm.sample(list(range(1,21)),20)              # genera 20nrs del 1..20 ordenados de forma aleatoria.
print(L)

import numpy as np
m = np.linspace(0,1,5)                            # genera 5 nrs de partes distantes iguales desde el 0..1 = [0.  0.25  0.5  0.75  1. ]
print(m)

m = np.arange(1,10,2)                             # [1 3 5 7 9]
print(m)

m = np.zeros((2,3))                               # genera una matriz de zeros de 2=rows y 3=cols 
print(m)

m = np.ones((2,3))                               # genera una matriz de unos de 2=rows y 3=cols 
print(m)

m = np.random.rand(3,2)
print(m.round(2))
"""
[[0.19 0.77]
 [0.06 0.89]
 [0.75 0.17]]
""" 

m = np.random.randint(2,10,(2,3),dtype='int8')
print(m)
"""
[[2 5 8]
 [3 6 8]]
"""

m = np.random.uniform(low=0,high=10,size=6)     # genera un array de 6 elmnts aleatorios entre 0..10
print(m)
# [6.90086197 6.49071002 3.03308198 7.6916496  2.26920541 0.18983826]

# En la teoría de probabilidades, existe lo q llamamos distribución norma estándar.
# La distribución normal es la más extendida en estadística, llamado tambien como:
# distribución normal o distribución gaussiana, tiene la forma de una campana.
# una de las distribuciones de probabilidad de variable +s usada.
m = np.random.randn(3,2)                        # ret a sample of 'standard normal' distribution.
print(m.round(2))
"""
[[ 0.78787245  0.44090296]
 [ 0.64093726 -0.17204656]
 [ 1.38184215 -0.80398729]]
""" 


m = np.random.normal(loc=4, scale=0.5,size=10).round(3)           # ret a 10 random samples from a normal (Gaussian) distribution.
print(m)
# [3.908 4.095 4.115 4.35  3.981 3.89  3.719 3.75  3.689 4.843]
m = np.random.normal(loc=4, scale=0.5,size=10)                    # ret a 10 random samples from a normal (Gaussian) distribution.
mm = np.round(m,2)
print(mm)
# [4.03 4.31 3.66 4.84 4.11 4.32 4.47 4.11 3.68 3.44]


m = np.arange(1,10)                                               # [1 2 3 4 5 6 7 8 9]   elementos.
print(m)
mm = np.reshape(m,[3,3])                                          # tienen q ser la misma cantidad de elemts.   
print(mm)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""


m = np.arange(9).reshape(3,3)
print(m)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
""" 
#---------------------------------------------
a = np.random.randint(2,10,(3,2),dtype='int8')
b = np.random.randint(2,10,(2,5),dtype='int8')
print(a)
"""
[[2 4]
 [6 7]
 [4 2]]
""" 
print(b)
"""
[[2 7 4 4 4]
 [9 2 7 9 4]]
"""

# FORMA 01 = FORMA 02
ab = np.matmul(a,b)                     # esta forma 01
print(ab)
"""
[[40 22 36 44 24]
 [75 56 73 87 52]
 [26 32 30 34 24]]
 """
 
print(a@b)                              # esta forma 02        



# estadistica:
m = np.random.randint(65,75,10,dtype='int8')    # [74 74 69 70 70 70 70 66 74 67]
m = np.array([74,74,69,70,70,70,70,66,74,67])
print(m)
mm = np.mean(m)                                 # promedio = 70.4   (a+b+c+d)/4 , la media o media aritmética, media geometrica, media armonica...
print(mm)
mm = np.median(m)                               # promedio = 70.0    (a+b+c+d)/4 , la mediana o mediana estadistica, 1,2,3,4,5 :. rspt=3
print(mm)

mm = np.std(m)                                  # promedio = 2.690724    (74-prom)^2 + (74-prom)^2 + (69-prom)^2 +.../10 = rst --> 'varianza' :. SQRT(rspt) --> 'Desv Estandar'
print(mm)                                       # Compute the standard deviation along the specified axis.

mm = np.percentile(m,90)                        # promedio = 74.0    Compute the q-th percentile of the data along the specified axis.
print(mm)

mm = np.percentile(m,20)                        # promedio = 74.0    Compute the q-th percentile of the data along the specified axis.
print(mm)

