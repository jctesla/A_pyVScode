import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Subtract 1 from all elements that are greater than 3
arr[arr > 3] -= 1

print(arr)