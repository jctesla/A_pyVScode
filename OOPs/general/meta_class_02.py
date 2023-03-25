class Student:
  	pass

# Print type of Student class
print("Type of Student class is:", type(Student))

#----------------------------------------
# Because Classes are also an object, they can be modified in the same way.
# We can add or subtract fields or methods in class in the same way we did with other objects

# class methods and variables
class atest:
  x=0
  foo=""
  pass

# Defining method variables
atest.x = 45

# Defining class methods
atest.foo = lambda self: print('aHello')      # lambda es callable Ej: f = lambda x : x**2 + x + 1    :. peint(f(3))
# test.foo = print('Hello')                 # no es call able.


# creating object
myobj = atest()

print(myobj.x)
myobj.foo()


#-------------------------------------
# es lo mismo :

class btest:
  pass

# Defining method variables
btest.x = 46

# Defining class methods
btest.foo = lambda self: print('bHello')      # lambda es callable Ej: f = lambda x : x**2 + x + 1    :. peint(f(3))

# creating object
myobj = btest()

print(myobj.x)
myobj.foo()

#---------------------------------------


