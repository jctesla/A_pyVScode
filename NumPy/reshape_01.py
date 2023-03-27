import numpy as np
b = np.arange(12).reshape(4, 3)     # 2d array
print(b)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#   [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

# The product operator * operates elementwise in NumPy arrays. 
# The matrix product can be performed using the @ operator (ver Py >=3.5)
# or the dot function or method:

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])

A * B                       # Elementwise product
# array([[2, 0],
#        [0, 4]])

A @ B                       # Matrix product
# array([[5, 4],
#        [3, 4]])

A.dot(B)                    # Another matrix product
# array([[5, 4],
#        [3, 4]])