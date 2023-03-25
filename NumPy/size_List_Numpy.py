import sys
import numpy as np
m = range(1000)
print(sys.getsizeof(m)*len(m))

n = np.arange(1000)
print(n.size*n.itemsize)