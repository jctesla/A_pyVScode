
def numeros(n):
  for i in range(n):
    yield i


# Uso del generador y almacenamiento en una lista
generador = numeros(10)

print("generador type=", type(generador))             # <class 'generator'>
print("  dir(generador)=", dir(generador))            # ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
                                                      # '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', 
                                                      # '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
                                                      # 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']  