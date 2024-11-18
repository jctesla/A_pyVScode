class Person:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
      return self.name

class alumno():
    escolar = Person('John')

    
al = alumno()
print(al.escolar)

alu = Person('Johnny')
print(alu.get(alu))
#person2 = object.__init__(Person,'John')




