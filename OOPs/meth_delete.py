# Check if a variable is defined in Python
# Python la forma de manejar las variables y su definicion lo hace a travez de un listado.
# declaring and initializing varible in Python
var1 = 23
var2 = 2.333
var3 = 'this is me'
var4 = [1,2,3,4]

print( dir() )                                           # dir() devuelve un list de todas las variables buit-in y variables declaradas.
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'var1', 'var2', 'var3', 'var4']

# Python delete variable
del var1, var2, var3, var4
print( dir() )
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


# -----------------------------------------------------------------------------------------------
# How to know if object had deleted in Python : well looking his list returned by dir(), vars() or Globals()
# https://stackoverflow.com/questions/11328219/how-to-know-if-object-gets-deleted-in-python
#------------------------------------------------------------------------------------------------
# The memory Heap in Python holds the objects and other data structures used in the program.
# Hay formas de borrar el Obj de la memoria.
class MiObjet(object):
    
    def __init__(self):                                   # Initializing/Contructure
        self.value= ""
        print("Initialization called=Instance.")
    
    def __delete__(self, instance):                       # deletes attribute, execute before prog ends
        print("event Deleted Object called!.")

    def __del__(self):                                    # Destructor, execute After prog ends
        print("Inside __del__")



miObj = MiObjet()
#print(type(miObj))                                        # <class '__main__.Example'>
print(dir())                                               # return a list[] of all the names of var declared localy
# Out:
# ['MiObjet', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'miObj']

print("Vars()",vars())                                     # return a dict{} de las vars built-in y declaradas localmente con su valor de origen.
print("Globals()",globals())                               # return a dict{} de las vars built-in y declaradas globalmente con su valor de origen.
# Out:
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000000001E42788>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\phytonSpace\\miBasic\\A_VSCode\\OOPs\\meth_delete.py',
# '__cached__': None, 'MiObjet': <class '__main__.MiObjet'>, 'miObj': <__main__.MiObjet object at 0x00000000029AC348>}

del miObj                                                 # puedo borrar varios Objts y variables a la vez. 'del var1, var2, miObjt'

# if 'del is executed', then 'ff' was totally deleted from system.
# but if you want to use it later, then just set to 'None', this
# remain the pointer to the vriable address memory.
lstObjts = dir()
if 'miObj' in lstObjts:
  print("ff Si existe")   # name 'ff' is not defined
else:
  print("ff No existe")   # name 'ff' is defined  