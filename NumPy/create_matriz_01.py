import numpy as np
a1 = np.full((2,3),1,dtype='int8')      # Gen una matriz de 2rows x 3 cols con el valor de 1 del tipo int8= 1 byte.
print(a1)

a2 = np.zeros(5)                        # Gen arry de ZEROS de 5u.
a3 = np.ones(5)                         # Gen arry de UNOS de 5u.
a4 = np.random.random(5)                # Gen arry de random de 10u solo numrs positivos.
a5 = np.random.randn(3)                 # Gen arry de random de 10u entre numrs negativos y positivos.
a6 = np.linspace(0,1,5)                 # ajusta 5 partes iguales con valores entre 0 y 1 = [0. 0.25 0.5 0.75 1.]
                                        # Gen arry de nºs espaciados uniformemente en el intervalo de 0 a 1
a7 = np.arange(0,5,1)                   # Gen arry 5 nºs con: begin=0, hasta=5, step=1  : rslt=[0 1 2 3 4]
a8 = np.arange(2,8,1)                   # Gen arry [2 3 4 5 6 7]  , crea una sumatoria + step=1 hasta < limit-->8
a9 = np.arange(2,8.01,1)                # Gen arry [2. 3. 4. 5. 6. 7. 8.], y se ve en float, x q se coloco 8,01
a10 = np.arange(0,2,0.7)                # Gen arry [0.  0.7  1.4], begin=0, maxRange sum + step=0,7

