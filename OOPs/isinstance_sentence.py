# isinstance(object, classinfo)
# return "True" si el argumento del objeto es una instancia del argumento classinfo
# o de una subclase (directa, indirecta) del mismo.

# issubclass(class, classinfo)
# return "True" si class es una subclase (directa, indirecta o virtual) de classinfo.
# Una clase se considera una subclase de sí misma.

x = isinstance("Hello", (float, int, list, dict, tuple))
print(x)                 # False

y = isinstance("Hola", (float, int, str,list, dict, tuple))
print(y,"\n")            # True

#----------------------------------
class myObj:
  name = "John"

z = myObj()
r = isinstance(z, myObj)
print(r)                  # True


#----------------------------------
# inherits de clase 'myC' from 'myB' y 'myB' from 'myA'.
class myA:
  name = "John"

class myB(myA):
  lastm = "Charles"

class myC(myB):
  lastp = "Brown"

a = myA()
b = myB()
c = myC()
 
print('1. ', isinstance(a, myA) )     # True
print('2. ', isinstance(b, myA) )     # True
print('3. ', isinstance(c, myB) )     # True
print('4. ', isinstance(c, myA) )     # True

# los arg = argumentos son clases no instancias.
print('5. ', issubclass(myB, myA) )   # True
print('6. ', issubclass(myC, myA) )   # True
print('7. ', issubclass(myA, myB) )   # False
print('8. ', issubclass(myA, myC) )   # False
