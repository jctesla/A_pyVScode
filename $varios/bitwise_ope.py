
from enum import Enum

class Constants(Enum):
  WIDTH = 1024
  HEIGHT = 256

  
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1
  


print(Constants.WIDTH.value)
print(Constants.HEIGHT.value)

entr = int(input("Ingrese 1/0:"))
if entr==State.ACTIVE.value:
  print("Encendido")
else:
  print("Apagado")    


