# Tuple are like a () Ball, Tuple = unMutable.
miTuple= (3,1,4,1,5,9)
print("Un Arry Tuple :", miTuple)

#Convertir un Tuple --> List
newList = list(miTuple)
newList[0] = 10
print("List es mutable(se puede cambiar)",newList)

#Convertimos el nuewList  --> Tuple
newTuple = tuple(newList)
print("Tuple es unMutable(no se puede cambiar)",newTuple)
print("Longitus del newTuple : ",len(newTuple))             # = 6 elementos
print("Elemento menor del Tuple : ", min(newTuple))         # = 1 es el Elemento Menor de todos
print("Elemento mayor del Tuple : ", max(newTuple))         # = 10 es el Elemento Mayor de todos

# Dictionary Use {} like a Curly Pages.
frutas = {'Manzana': 'Chilena',
          'Color': 'Rojo',
          'Tamano': 'Mediano',
          'Temporada':'Verano'
        }
# Listamos una Caracteristica
print("Produccion : ", frutas['Temporada'] )

# Borro una Caracteristica
del frutas['Tamano']
print("Borro caracteristica Tamano : ", frutas)

#cambio una Caracteristica
frutas['Temporada'] = 'Primavera'
print("Cambie Caracteristica Temporada : ", frutas['Temporada'])
print("Nro de elementos del Dictionary Frutas : ", len(frutas))
print("Using get para leer un elemento : ",frutas.get("Temporada"))
print("Lee los Keys de Caracteristicas : ", frutas.keys())              # dict_keys(['Manzana', 'Color', 'Temporada'])
print("Leer los values de los Keys : ",frutas.values())                 # (['Chilena', 'Rojo', 'Primavera'])




