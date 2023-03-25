# Using type() to compare types with 'is'
arg= "Hola"
lista = list(arg)

if type(lista.__repr__()) is str:               # " <class 'str'>"
  print(lista.__repr__())
  
if type(lista) is list:                         # " <class 'list'>"
  print(lista)

#------------------------------
print('1.- ', type(9) is int)
print('2.- ', type(2.5) is float)
print('3.- ', type('x') is str)
#print('4.- ', type(u'x') is unicode)
print('5.- ', type(2+3j) is complex)

va = None
print('1.- ', va is None)                               # True
print('2.- ', va == 1)                                  # False
print('3.- ', va == 0)                                  # False


#_-------------------------------------------
def curva(x):
    if (x > 2 and x < 7):
        return True
    else:
        return False
lista= [1,2,3,4,5,6,7,8,9,10]
filtro = filter(curva,lista)
print( list(filtro) )


#---------------------------------
class MiClass:
  def __getitem__(self, key):
    """ Determines behavior of `self[key]` """
    l = [10,20,30,40,50]
    return l[key]

  def __pow__(self, num):
    """ Determines behavior of `self ** NUM` """
    return f"Python Like You Mean It {num}"

  def __call__(self):
    return "Look at me!"

miclass = MiClass()
print('1. ', miclass [2])                      		# 30    lo mismo
print('1. ', miclass.__getitem__(2))          		# 30    lo mismo
print('2. ', miclass ** 2 )                  		  # Python Like You Mean It 2
print('3. ', MiClass.__pow__.__doc__)    		      # Determines behavior of `self ** NUM`
print('4. ', miclass.__pow__.__doc__)         		# Determines behavior of `self ** NUM`
print('5. ', miclass())		         		            # Look at me!"



'''
import types
x = "mystring"
print('1. ', isinstance(x, types.StringType))

x = 5
print('2. ', isinstance(x, types.IntType))             # True

x = None
print('3. ', isinstance(x, types.NoneType))            # True
'''