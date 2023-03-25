#------------------Clase Principal
class Pet(object):
  def __init__(self, obj):
    if type(obj) == Cat or type(obj) == Dog:
      self.name= obj.name
      self.age = obj.age
    else:
      self.name= "uknow"
      self.age = "uknow"
    self.obj = obj


  def show(self):
    print(f"I am {self.name} and I am {self.age} years old")

  def features(self):
    if type(self.obj) == Cat:
        print(f"Es un GATO se llama = {self.name}, tiene ={self.age}años y hace {self.obj.speak()}")

    elif type(self.obj) == Dog:
        print(f"Es un PERRO se llama = {self.name}, tiene ={self.age}años y hace {self.obj.speak()}")

    else:
        print(f"NO es PERRO ni GATO....")


#------------------Clase CAT
class Cat(Pet):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    return("MIAOOO-MIAOOO")


#------------------Clase DOG
class Dog(Pet):
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def speak(self):
      return("WUAUU-WUAUU")


#-----------------Class Fish
class Fish(Pet):
  def __init__(self, name, age):
    print(f"Clase Fish no implementado....")
    pass                                          # esta sentencia permite pasar el control a la clase superior
                                                  # es decir el control a la Clase madre = 'Pet()'  

#------------------FUNCION UNKNOW
def unknowAnimal():
  print(f"...Animal Desconocido...")
  pass



#--------------------------------------------
#         main program
#--------------------------------------------

cat = Cat("Travis",7)
pet = Pet(cat)                                    #Gato
pet.features()                                    #Es un GATO se llama = Travis, tiene =7años y hace MIAOOO-MIAOOO

dog = Dog("Teza",8)
pett = Pet(dog)
pett.features()                                   #Es un PERRO se llama = Teza, tiene =8años y hace WUAUU-WUAUU

fish = Fish("Buble",2)
pettt = Pet(fish)
pettt.features()

animal = unknowAnimal()                           #...Animal Desconocido...
petttt = Pet(animal)           
petttt.features()                                 #NO es PERRO ni GATO....






