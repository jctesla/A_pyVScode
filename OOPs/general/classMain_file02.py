# demuestra como se puede crear un 'Class' o 
# un 'def' en otro file y usarlo en el actual file.

from classCar_file01 import Car

car_a = Car("Aqua")
car_b = Car("Blue")

Car.__type= "Militar"                       # asigno a una var privada de forma static.
car_a.__color = "Pink"                      # crea una var local, no es la ref de la var de la 'class_car.py'
print(car_a.__color,car_a.__tipo)           # Aqui si imprime color y tipo, esto es engañoso.

# usando los getter/setter
print('1. get: ',car_a.get_color())
print('2. set:',car_a.set_color("Yellow"))
print('3. get:',car_a.get_color())

# there are other way more elegant
# use @property/@color.setter               # class_car.py
print('4. get:',car_a.color)                # we dont need to use pareentisis ()
car_a.color='Black'
print('5. set:','Black')
print('6. get:',car_a.color )






