L = 32 
P = 35
K = 'A'

# how to check if this vars have the same type
print(isinstance(L, int))                         # True
print(isinstance(L, (float, str, list)))          # False, no es de ninugn de estos types.
print(isinstance(L, (float, str, list, int)))     # True, esta en unos de estos types.

# check memory address: using id()
# En Python, puede usar la función id() para obtener el identificador entero único de un objeto,
# se puede usar para determinar la dirección de memoria de un objeto tmbn. Sin embargo, tenga en
# cuenta que el diseño de memoria exacto de un objeto de Python puede ser complejo y específico,
# y las direcciones de memoria devueltas por id() pueden no ser contiguas o comparables  con las
# direcciones de memoria en lenguajes de programación de bajo nivel.

L = [1,2,3,4]                                     # Create an object
print(id(L[0]))                                   # 8791547683232
print(id(L[1]))                                   # 8791547683264 , la dif entre [0] y [1] = 32bytes


#  other way
import ctypes
# Get the memory address of the object
addr1 = ctypes.cast(id(L[0]), ctypes.POINTER(ctypes.c_byte))  # castea id(L[0])) a un puntero en byte.
addr2 = ctypes.cast(id(L[1]), ctypes.POINTER(ctypes.c_byte))
addr3 = ctypes.cast(id(L[2]), ctypes.POINTER(ctypes.c_byte))

# Print the memory address as a hex string
print(hex(addr1.contents.value), hex(addr2.contents.value), hex(addr3.contents.value))

