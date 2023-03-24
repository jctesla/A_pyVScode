# Como analizar el Nº de personas en una reunion, creadno 3 instancias de una misma clase: 
class Person:
  nper = 0                              # defini esta var como static = Person.nper, seria un 'Atributos de Clase' y es publico.
  __var = 0                     	      # variable PRIVATE, si agrego doble underlying __ la var se vuelve private, uso solo dentro de la clase.

  def __init__(self, name):             
    self.name = name                    # attribute de instancia.
    self.add_nper()                     

  def add_nper(self):                   # para usar una var global debo usar la clase misma
    Person.nper += 1                    # cuenta el Nº de Personas
    self.__var +=1
  
  @staticmethod                         # staticmethod :
  def num_persons():                    # permite q pueda declarar un meth con parentisis vacio y self no es static.
    return Person.nper                  # exportar la var static.

  def read_privar(self):
    return self.__var


#--------------------------------------------
#         MAIN
#--------------------------------------------
Person.nper  = 100                                    # var static, supongamos hay 100 prsonas dentro
pn = Person("Milye")                                  # persona 101  
print(f"Nº Personas = {pn.num_persons()} \n")         # Nº Personas = 101


pnn = Person("Tim")                                   # Nº Personas = 102  
print(f"Nº Personas = {pnn.num_persons()} \n")        # se suma +1 c/vez q instacio la Clase Person = 101

pnnn = Person("Lilly")
print(f"Nº Personas = {pnnn.num_persons()}")          # Nº Personas = 103 
print(f"Nº Personas = {Person.nper}")                 # Nº Personas = 103, Forma 01 de llamar ‘ES UN VERY BAD BEHAVIOR’
print(f"Nº Personas = {pnnn.num_persons()}")          # Nº Personas = 103, no necesito instanciar el metodo.

# Read Variable Public/Private de la Clase.
print(pnnn.nper)                              	      # 103
print(pnnn.read_privar())                       	    # 1  x q es solo su propia instancia de 'Lilly'
# print(Person.__var)                      	  	      # saldrá ERR AttributeError : type object 'Person' has no attribute '__var'

# pero si hago esto: ‘ES UN VERY BAD BEHAVIOR’
pnnn.__var = 100				  	                          # funciona pero realmente creas una nueva var local, no es de la clase Person ‘__var’.
print(pnnn.read_privar())                       	    # 1


