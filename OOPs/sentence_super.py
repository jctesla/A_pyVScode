# Herencia = inherit, la subclass puede usar los methds de la clase padre(super)
# self indica q se refiere a la instancia q los invoco.(The self parameter is a reference to the current instance of the class)
class Person:
  __edad=0                                  # es una var privada
  def __init__(self, fname, lname, edad):
    self.firstname = fname
    self.lastname = lname
    Person.__edad = edad                    # declaramos una : private var static

  def printname(self):
    return [self.firstname, self.lastname]
  
  @staticmethod                             # permite q al llamar el methd no necesite un (arg)
  def printedad():
    return Person.__edad
  
  '''
    ó
  def printedad(v=None):
    return Person.__edad
  '''
  

# super() se ref a la clase de donde hereda :. Person
class Student(Person):
  def __init__(self, fname, lname, edad):
    super().__init__(fname, lname, edad)        # super().
    self.graduationyear = 2019

#---------------------------------
s = Student("Mike", "Olsen",69)
print('1. ',s.graduationyear)
print('2. ',s.printname())                            # ['Mike', 'Olsen']     type(s.printname()) = <class 'list'>
print('3. ',s.printname())                            # si el method printname() tiene 'return' debemos colocar parenticis
print('4. ',Person.printedad())                       # 69
print('5. ',s.printedad())                            # 69

print("\n------------------------")
ss = Student("Niko", "Poison",79)       
#print(Person.__edad)                                 # AttributeError: type object 'Person' has no attribute '__edad', x q es private
print('1. ',Person.printedad())                       # 79
print('2. ',s.printedad())                            # 79  
print('3. ',ss.printedad())                           # 79


