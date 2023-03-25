#------------------Clase Principal
class Pet(object):
  def __init__(self, name, age):
      self.name= name
      self.age = age

  def speak(self):
    print(f"No se que Sonido hace este Ser...")

  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

  

#------------------Clase CAT
class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color
    self.name = name
    self.age = age

  def speak(self):
    print("MIAOOO-MIAOOO")


#------------------Clase DOG
class Dog(Pet):
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def speak(self):
      print("WUAUU-WUAUU")


#-----------------Class Fish
class Fish(Pet):
    pass                                          #como no esta implemnetado el Metodo de 'speack()', en esta clase le pasamos la
                                                  #pelota es decir el control a la Clase madre = 'Pet().speak'  



#--------------------------------------------
#         main program
#--------------------------------------------
#En este Ejemplo, es similar cuando se tienes la clase superior 'Person' y las clases 'Child', Administradores y Empleados, lo 2dos
#  tienen las mismas propiedades de name, pero ambos tienen diferecias cocmo el nivel de acceso por ejemplo.
cat = Cat("Lolis",8,"BLANCO")
cat.speak()                                   # MIAOOO-MIAOOO
print()

dog = Dog("Teza",7)
dog.speak()                                   # WUAUU-WUAUU
print()

fish = Fish("bubleee",2)
fish.speak()                                  # NO TIENE IMPLEMENTADO NADA; No se que Sonido hace este Ser...




