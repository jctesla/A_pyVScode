# https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html

import numpy as np

def rowcol(val):
  return [val+1,val+2,val+3]
  
m = np.array([rowcol(v) for v in range(10,100,10)])  
print(f'm={m}\n')
#m=np.zero((3,4),dtype='int32')

# Jugamos con la Matriz creada
# devuelve = 32,42,52
print(m[2:5,1])

# devuelve = 41,42,51,52
print(m[3:5,0:2])

# devuelve = 41,42,51,52 y 82,83,92,93
m1 = m[3:5,0:2]
m2 = m[7:9,1:3]
m3 = np.append(m1,m2,axis=0)
print(m3)

# devuelve = 32,33,42,43
print(m[2:4,1:])