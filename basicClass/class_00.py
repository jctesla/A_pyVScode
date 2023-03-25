# en Pytho todo son Objs, en este caso creo una variable global(un Obj global)
# lo uso para saber y llevar una cuenta de cuantas Classes instancio y uso este mismo Obj

msg = {'Desc':'-Hi-', 'Inst':0, 'MeCalled':0}              # Declaro una var/Obj Global inicial = 'msg'
                                                           # que contiene sus elementos: Descripcion, Instancias, Llamdas. 

#----------------------------------------
class anything:
  n = 0

  # Constructor
  def __init__(self, nombre):
    global msg                                            # fuerzo a ref a la var/Obj global 'msg'
    msg['Desc'] = 'Obj Contruido!'                        # Descripcion, modifico el valor del obj global.
    msg['Inst'] = msg['Inst'] + 1                         # Instancia, modifico el valor del obj global.
    msg['MeCalled'] = msg['MeCalled'] + 1                 # Veces he usado este Obj Global.
    print(f'msg = {msg}')
    self.nombre = nombre
  
  # Methodo  
  def getName(self):
    self.n += 1
    msg['Desc'] = f'This Class -{type(self).__name__}-'
    msg['MeCalled'] = msg['MeCalled'] + 1
    return(f'Nombre={self.nombre}  /  Called msg={msg}  /  ThisMet={self.n}')  
  
  
#-----------------------------------------
#               Main()
print(f'Before Call Class w global msg={msg}\n')

print(f'Calling 1st time Class w global msg : ')
cq = anything('Monik')
for i in range(5):
   print(f'{i}.- cq = {cq.getName()}')                    # use 5 times this method of this New Instance

print(f'\nCalling 2nd time Class w global msg: ')
mc = anything('SuMonik')
for i in range(3):
   print(f'{i}.- cq = {mc.getName()}')                    # use 3 times this method of this Other New Instance
   
   
print(f'\nAfter Call Class msg = {msg}')                  # Final result after use Class and Global msg and Methods.