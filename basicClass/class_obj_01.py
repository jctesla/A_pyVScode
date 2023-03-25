# self representa toda la clase completa como Obj. 
# para crear una representacion propia de si mismo, del obj.
from sqlalchemy import null


class PartyAnimal:
    x = 0
    name = ""

    def __init__(self,name):
        self.name = name
        print(f'name: {self.name} constructed')

    def party(self):
        self.x = self.x + 2
        print(f'name = {self.name} / x: {self.x}')


# clase que se extiende de la clase PartyAnimal()
class FootballFan(PartyAnimal):
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(f'{self.name} points = {self.points}')

   def __del__(self):
       print(f'Clase {self.name} Detructed')

       
#-----------------------------------------------      
s = PartyAnimal("Sally")
s.party()
s.party()

print()

j = FootballFan("Jim")
j.party()
j.touchdown()

j=null

#----------------------------------------------
# OutPut:
#
#// Clase Padre
# name: Sally constructed
# Sally party / count: 2
# Sally party / count: 4
#
#// Clase Hijo/ inherith :
# name: Jim constructed
# Jim party / count: 2
# Jim party / count: 4
# Jim points = 7
# Clase Jim Detructed
