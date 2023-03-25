import time
import numpy as np
tam = 10
L1 = range(tam)         # list
L2 = range(tam) 
A1 = np.arange(tam)     # lo mismo q list pero p numpy.
A2 = np.arange(tam)

# List() 
start = time.time()                       # inicio
rslt = [(x, y)  for x,y in zip(L1, L2)]   # procesa...
print(rslt)
print((time.time() - start) * 1000)       # termina

# NumPy() 
start = time.time()                       # inicio
rslt = A1*A2                              # procesa...
print(rslt)
print((time.time() - start) * 1000)       # termina

# result:
# 2.0003318786621094
# 0.9999275207519531