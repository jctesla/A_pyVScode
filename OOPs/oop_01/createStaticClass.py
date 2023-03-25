# ---------------------------------------------
# Clase q Utiliza una Variable global en el contexto de la clase q no necesita instanciarse p acceder.
class Person:
  numper = 0                          # esta var dentro d la clase, lo llamamos 'Atributos de Clase' y es publico x defecto.
  __privatevar = 0                    # DECLARA la variable como PRIVADA, solo para uso de la misma Clase.

  def __init__(self, name):            # instancia inicial.
    self.name = name
    Person.add_numper()                # llama a sumar mas personas.   

  # @classmethod .- 
  # Convierte una función para que sea un método de clase.
  # Es un método q recibe la clase como primer argumento implícito,
  # al igual que un método de instancia = '__init__' recibe la instancia 'self'.
  # Para declarar un método de clase, use este 'decorator' o 'modismo': @classmethod
  # y cls como entrada. 'num_persons' no necesita una instancia para q actue.
  @classmethod                                 # 'cls' = 'class Person' 
  def add_numper(cls):                         # para usar una var global debo usar la clase misma
    cls.numper += 1                            # Person.numPersonas =  Person.numPersonas + 1
    cls.__privatevar +=1

  
  @classmethod
  def num_persons(cls):                       # devuelvo el valor del atributo de clase, 'glbNumPers'
    return cls.numper                         # si solo escribo  return glbNumPers saldra err: name 'glbNumPers' is not defined

  @classmethod
  def read_privar(cls):
    return cls.__privatevar



# ---------------------------------------------
# @staticmethod.- q no necesita instanciarse p acceder.
class Math:
    
    @staticmethod
    def add5(x):
      Math.n=x                                                    # almacenamos una valor en la clase statica.
      return Math.n + 5

    @staticmethod
    def add10(y):
      return(Math.n + y)                                          # utilizamos el valor almacenado.



#--------------------------------------------
#         MAIN
#--------------------------------------------
prsn = Person("Milye")
print(f"Numero de Personas = {prsn.num_persons()} \n")

Person.numper  = 100                                              # sino declaro q es private puedo usarlo como public y es static
prsnn = Person("Tim")
print(f"Num de Personas = {prsnn.num_persons()} \n")              # se suma +1 c/vez q instacio la Clase Person = 101

prsnnn = Person("Lilly")
print(f"Num de Personas = {prsnnn.num_persons()}")                # = 102
print(f"Num de Personas = {Person.numper} \n")                    # = 102
print(Person.num_persons())                                       # no necesito instanciar el metodo nro d personas = 102

# Read Variable Public/Private de la Clase.
print(Person.numper)                                              # = 102
print(Person.read_privar())                                       # = 3
#print(Person.__privatevar)                                       # ERR Exception has occurred: AttributeError : type object 'Person' has no attribute '__privatevar'


# Clase Statica.
# Podemos asignarlo a una variable como h = Mat(), para luego ser ma facil eliminarla
# o podemos usarla directamente, ahi vemos como almacena una variable que se usa en 2 metodos
print(f"Clase Statica = {Math.add5(10)}")                         # = 15, no necito instanciarla p acceder a ella.
print(f"Clase Statica = {Math.add10(30)}")                        # = 40
print(Math.n)


