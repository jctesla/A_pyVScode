# como usar una clase estatica

class apellido(object):
  elemento = []
  totales=0
  
  def __init__(self, lbl):
    self.lbl = lbl
    
  def edad(self,edad):
    self.totales += edad
    return(apellido.totales)
  
  def total(self):
    return self.totales    
  
  @staticmethod
  def addApellido(x):
    apellido.elemento.append(x)
    return True
  
  def readElemento():
     return  apellido.elemento
 
 
print('LLenado de datos del Alumnos:')

# instancia 1  
ape1 = apellido('Promocion 85-1')
apellido.addApellido('Obama')
ape1.edad(18)
apellido.addApellido('Biden')
ape1.edad(16)
apellido.addApellido('Jhonns')
ape1.edad(16)
apellido.addApellido('Millen')
print(f'Lee los Apellidos= {apellido.readElemento()} / edades total: {ape1.total()} años')

# instancia 2  
ape2 = apellido('Promocion 85-2')
apellido.addApellido('coollin')
ape2.edad(18)
apellido.addApellido('tyson')
ape2.edad(16)
print(f'Lee los Apellidos= {apellido.readElemento()} / edades total: {ape2.total()} años')





