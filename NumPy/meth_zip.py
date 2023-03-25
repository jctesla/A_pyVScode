# NOTE: 'zip' just excecuted one time to get data
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
# Holds an iterator object
zipped = zip(numbers, letters)
print(type(zipped))
#print(list(zipped))

#------------------------
for z in list(zipped):
  print(z)
  for zz in z:
    print(zz)
# Out:
# <class 'zip'>
# (1, 'a')
# 1
# a
# (2, 'b')
# 2
# b
# (3, 'c')
# 3
# c
