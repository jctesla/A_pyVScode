class promo(object):
  __ele = []                                                  # variable tipo list() privado
  lbl =""                                                     # var tipo str publico
  __inst=0                                                    # var tipo int publico
  
  def __init__(self,lbl):
    print(f'Nom clase: {type(self).__name__}')                # me da el nombre de la clase = 'promo'.
    promo.__inst += 1                                         #  self.__inst .- represnt la instancia de la clase, ref a var de la 'instancia'.
    self.lbl= lbl                                             # promo.__inst .- represnt la clase em si misma, ref a var de la clase 'static'.  
    
  @staticmethod
  def addName(a):
    promo.__ele.append(a)
    return True
  
  def rdNames(self):
    return {'pro':self.__ele, 'ninst':self.__inst}
  
#  def __init__(self) -> None:
#    pass
# sustraigo nombre de clase

# Instancia 01
prm1 = promo("Promo 85")
promo.addName('Obama')
promo.addName('Biden')
datos = prm1.rdNames()
print(f"Instancias={datos['ninst']}   Promo={prm1.lbl}  Nombres={datos['pro']}")    # Instancias=1   Promo=Promo 85  Nombres=['Obama', 'Biden']


# Instancia 02
prm2 = promo("Promo 86")
promo.addName('Coollin')
datos = prm2.rdNames()
print(f"Instancias={datos['ninst']}   Promo={prm2.lbl}  Nombres={datos['pro']}")    # Instancias=2   Promo=Promo 86  Nombres=['Obama', 'Biden', 'Coollin']
