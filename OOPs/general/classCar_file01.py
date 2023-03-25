# cualquier forma A o B son validas p declarar una var PRIVADA
# y de la forma 1 y 2 cualier es valida para declara un metodo.
class Car:
  __tipo = "Sport"               	              # declara una var PRIVATE, __ solo para uso de la mísma Clase.<forma A>

  def __init__(self, color):                    # instancia inicial.
    self.__color = color                        # declara una var PRIVATE, __ solo para uso de la mísma Clase.<forma B>

  #--------------------------------------  
  # Forma 1 de exportar las private vars        # creamos methds 'getter/setter'.
  #--------------------------------------
  def get_tipo(self):
    return self.__tipo
  
  def get_color(self):
    return self.__color
  
  def set_color(self, colorin):
    self.__color = colorin
    return self.__color
  
  #--------------------------------------  
  # Forma 2 elegante con setter/getter          # usando 
  #--------------------------------------
  @property
  def color(self):
    return self.__color
  
  @color.setter
  def color(self, colorin):
    self.__color = colorin  
    
    
