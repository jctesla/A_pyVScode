# create a list suing []
palabra = "HOLA"
numbers = [4, 15, 8, 16, 42, 20]                # List of Numbers
friends = ["kevin", "Karen", "Jim", "Juan"]     # List of String
print("Get element form index friends = " + palabra[0])     # devuelve el elemtno H index=0
palabra[0] = "p"
print("Get element form index friends = " + palabra[0])     # devuelve el elemtno H index=0

print("Print all List friends(Arrays) = " + str(friends))
print("Get index of element 'karen' from friends = " + str(friends.index("Karen")))
print("Get Element of List friends = " + str(friends[1:4])) # sustraer d la lista los elementos de index1=1 to index2=4 (index1 begin = 0  / index2 begin =1)

print("Lista (Arreglo) numbers = " + str(numbers))
numbers.sort()
print("Lista (Arreglo) Ordenado = " + str(numbers))

# copy from One Array to Another new Array
friends2 = friends.copy()
print("Copia Lista o Arreglo from friends to friends2 = " + str(friends2))

friends.clear()
print("Borro el arreglo friends" + str(friends))

# using TUPLES, is the same as a List array, different is you can't save a different type of data
# create tuple, tuple is inmutable.
# inmutable = can't change or modify his contain elements (String, Integer, Boolean,etc)
# mutable = suelen ser las estructuras de datos como: dict, list, etc
coordinates = (4, 5)
print("Print Tuple Array = " + str(coordinates))
print("Print Element index=0 : " + str(coordinates[0]))
# Tuple is inmutable, used for data that not gone change.
# coordinates[1] = 10  # can't assign new value

# create list of TUPLES using ()
coordinates = [(4, 5), (6, 7), (80, 34)]













