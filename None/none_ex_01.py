# uso de None en Python, en otros lenguajes es el equivalente a Null, no exactamente.
class Foo:
    def __eq__(self,other=True):
      return True
    
    @staticmethod
    def eq(other=True):
      return False  
    
    
foo=Foo()
print('----------------')
print('1. ', foo==None)      # True
print('2. ', foo is None)    # False

print('----------------')
# In this case, they are the same. None is a singleton object (there only ever exists one None).
# 'is', checks to see if the object is the same object, while '==' just checks if they are equivalent.
p = [1]
q = [1]
print('1. ', p is q)         # False  because they are not the same actual object
print('2. ', p == q)         # True   because they are equivalent

g = p
print('3. ', p is g)         # True   because they are the same actual object
print('4. ', p == g)         # True   because they are the same actual object

p = None                     # is a singleton
q = None
print('5. ',p is q)          # True   because they are both pointing to the same "None"