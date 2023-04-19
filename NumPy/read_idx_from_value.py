import numpy as np
L = np.array([10,20,30,40,50,90])
idx = np.where(L==30)
print(idx)

print( L[(L>30) & (L<90)])
