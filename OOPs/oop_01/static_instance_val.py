# Usamos una variable global static p tosas las instancias del Obj 'Persona'
# Person.stc_num = al usar asi define una variable statica( de la Clase Padre),
# pero si asigno con la instancia person1.stc_num = es de la misma instancia

class Person:
  stc_num = -1                                 # variable PUBLICA, lo llamamos 'Atributos de Clase'.
  din_num = -1
  
  def __init__(self, num=stc_num):          # instancia inicial.
    Person.stc_num = num                    # static var 
    self.din_num = num                      # dinamic var (instancia)
 
  def inc_num(self):                        # incrementa static y dinamic var
    Person.stc_num += 1
    self.din_num += 1
    
    
  def rd_add(self):
    return {'static':Person.stc_num, 'dinamic':self.din_num}
  
  
  #------------------------
  @staticmethod
  def dec_num(self):
    self.numpub -= 1
    
  def rd_sub(self):
    return Person.numpub


#--------------------------------------------
#         MAIN
#--------------------------------------------
# Pregunta.-
# si tienes una variable del obj, puedes modificarla desde un metodo static e instanciado?

# STATIC
#Person.numpub = 100
print('1. ',Person.stc_num)                  # -1   SIN INSTANCIA, leo numpub x defecto = -1
print('1. ',Person.din_num)                  # -1   SIN INSTANCIA, leo numpub x defecto = -1

# INSTANT
person1 = Person(10)                         # 1ra INSTANCIA, y asigna stc_num ^ din_num = 10
print('2. ',person1.rd_add())                # {'static': 10, 'dinamic': 10} 

person2 = Person(20)                         # 2da INSTANCIA, y asigna stc_num ^ din_num = 20
print('3. ',person2.rd_add())                # {'static': 20, 'dinamic': 20}

# STATIC
Person.stc_num = 100                         # SIN INSTANCIA, asigna stc_num = 100
print('4. ',person1.rd_add())                #  {'static': 100, 'dinamic': 10}
print('5. ',person2.rd_add())                #  {'static': 100, 'dinamic': 20}

# INSTANT
person1.inc_num()                           # incrementa la var statica(clase padre) y dinamica(de la instancia person1)
person2.inc_num()                           # incrementa la var statica(clase padre) y dinamica(de la instancia person2)  :. en resumen se incrementa +1 person1 y person2, pero Person(padre) +2
print('6. ',person1.rd_add())               # {'static': 102, 'dinamic': 11}     / Person.stc_num = 102
print('7. ',person2.rd_add())               # {'static': 102, 'dinamic': 21}
