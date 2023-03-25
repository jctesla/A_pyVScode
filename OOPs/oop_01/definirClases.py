
#-------------clase car
#'self' = representa la instancia de la clase. Al usar 'self' podemos acceder a los atributos y métodos de la clase-
class car(): 
      
    # init method or constructor de instancia de la clase.
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 

    #Metodo de Mostrar
    def show_car(self): 
        print("Model is", self.model ) 
        print("color is", self.color ) 

    #Metodo de Get
    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    #Metodo de Set
    def set_model(self, modelo):    
        self.model = modelo 

    def set_color(self, color):    
        self.color = color 


#-----------funcion simple
def funcHello():
  print("hello")


#--------------------------------------------
#         main program
#--------------------------------------------

print(type(funcHello))                 #<class 'function'>

# both objects have different self which contain their attributes. 
car1 = car("audi","blue")
car2 = car("ferrari", "green") 
print(type(car1))                     #<class '__main__.car'>
 
car1.show_car()                       # Model is audi /  color is blue
car2.show_car()                       # Model is ferrari / color is green

print('El Modelo de Carro 01 = ' + car1.get_model() + ' y color = ' + car1.get_color())
print('El Modelo de Carro 02 = {0} y color ={1}'.format(car2.get_model(),car2.get_color()))


#--------------Lista de Objects 'Car'
lista = [car("toyota","blanco"), car("volvo","rojo"), car("ford","marron")]

for i in lista:
  print("-------------------") 
  print("Modelo = " + i.model) 
  print("Color  = " + i.color) 

#-------------------Resultado 
#Modelo = toyota
#Color  = blanco
#-------------------
#Modelo = volvo
#Color  = rojo
#-------------------
#Modelo = ford
#Color  = marron
#-------------------


#-------------Set Value Object 'Car'
#Los elementos de lista son Obj puedo leer/escribir
print("-------------------")
print(lista[1].model)                 #Leo el Modelo = volvo
print(lista[1].color)                 #Leo el Color = rojo

lista[1].set_model("camaro")          #cambia modelo de volvo a camaro
lista[1].set_color("purpura")         #cambia color de rojo a purpura
print(lista[1].model)                 #volvo
print(lista[1].color)                 #volvo
print("-------------------")















