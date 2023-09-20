# List use [] like a Boxs
unaList = ['Jugo', 'Tomates', 'Papas', 'Platanos', 'Mazanas']
print('1er Item = ', unaList[0])        # Jugo

unaList[0] = 'Jugo Verde'
print('1er Item = ', unaList[0])        # Jugo Verde
print('1er Item = ', unaList[1:3])      # ['Tomates', 'Papas']  [idxBegin=0,idxBegin=1]

# creamos un arreglo de Listas [0,1..]
segundaList = ['vaso peqeno', 'vaso mediano', 'vaso grande']
todoList = [unaList, segundaList]       # [['Jugo Verde', 'Tomates', 'Papas', 'Platanos', 'Mazanas'], ['vaso peqeno', 'vaso mediano', 'vaso grande']]
print(todoList)

sumArry = unaList + segundaList
print("sumArry :", sumArry)             # sumArry : ['Jugo Verde', 'Tomates', 'Papas', 'Platanos', 'Mazanas', 'vaso peqeno', 'vaso mediano', 'vaso grande']

# podemos ubicar un item del arreglo bidimensional
print(todoList[1][1])                   # vaso mediano
todoList.append('vaso extraGrande')     # agregamos un item mas al arreglo List
print(todoList)                         # [['Jugo Verde', 'Tomates', 'Papas', 'Platanos', 'Mazanas'], ['vaso peqeno', 'vaso mediano', 'vaso grande'], 'vaso extraGrande']

todoList.insert(1,'Zanahoria')
print(todoList)                         # [['Jugo Verde', 'Tomates', 'Papas', 'Platanos', 'Mazanas'], 'Zanahoria', ['vaso peqeno', 'vaso mediano', 'vaso grande'], 'vaso extraGrande']

todoList.remove('Zanahoria')
print(todoList)                         # [['Jugo Verde', 'Tomates', 'Papas', 'Platanos', 'Mazanas'], ['vaso peqeno', 'vaso mediano', 'vaso grande'], 'vaso extraGrande']

del todoList[2]                         # borro un Item = 'vaso extraGrande' IndexBegin = 0
print(todoList)                         # [['Jugo Verde', 'Tomates', 'Papas', 'Platanos', 'Mazanas'], ['vaso peqeno', 'vaso mediano', 'vaso grande']]

otraList = unaList + segundaList
print(len(otraList))                    # len = 8 Elementos Items.

