# https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_normal.html
import numpy as np
r = np.random.uniform(0,1.0, size=(3,2))
print(f"\n{'0:.3f'.format(r)}\n")
# Out:
# array([[0.44569835, 0.8583457 ],
#        [0.10367002, 0.4006943 ],
#        [0.74625541, 0.04878518]])


r = np.random.random_sample((5,))                               # esto es en NumPy vs List es random.sample(10,100)
print(r)
# Out:
# [0.16054031 0.85660984 0.50009946 0.55788519 0.24332357]


# crea arrys de n elementos en base al arry [1,2,..9]
import random
def lista(n):
  return random.sample([1,2,3,4,5,6,7,8,9],n)

n = np.array([lista(3),lista(3),lista(3),lista(3)])
print(f'\n {n} \n')
# Out:
#  [[4 9 6]
#   [2 7 3]
#   [8 7 6]
#   [1 8 3]]


arr = np.arange(10)                                             #  Baraja : input= [1,2,3,4,5,6,7,8,9]
np.random.shuffle(arr)
print(arr)
# Out:
# [3 4 6 0 1 5 9 8 7 2]


s = np.random.standard_normal(size=(3, 4, 2))
print(f'\n{s}\n')
# [
#  [[ 0.85152869 -0.6716254 ]
#   [-0.11190777  0.94570109]
#   [ 0.48884648 -0.19919231]
#   [ 1.23579999 -1.96264771]]
#
#  [[-0.28619622  0.6875425 ]
#   [-2.01446507 -1.01466365]
#   [-0.1985092  -1.4791122 ]
#   [-0.75213028 -0.59483954]]
#
#  [[-0.34779417  1.03175232]
#   [ 1.18772108  0.43156941]
#   [ 1.21185672  1.25300734]
#   [-1.39104349 -0.40754999]]
# ]

