# Usando lib pynput .- 
# Es una libreria q tiene un Listener permanente que escucha los evento de presion del teclado
# tanto press/release.
# Para darle más funcionalidad creamos un sinfin paralelo a Listener del teclado.
# en este ej hay 3 formas de probar esta libreria:
# Forma 01 : permite ver como se puede correr un Hilo base y paralelamente el Hilo del 'pynput'
# Forma 02 y Forma 03 ; son para comparar las diversas formas de usar la sintaxsis de esta libreria

from ast import While
from pynput.keyboard import Key, Listener 
import time

def on_press(key): 
     print(f'pressed = {key}') 
  
def on_release(key): 
     print(f'release = {key}') 
     if key == Key.esc:                                            # al return False, en realidad hace q el Thread termine, finalice.        
         # Stop listener 
         return False 
 
# devuelve:
# pressed = Key.up
# release = Key.up
# pressed = Key.right
# release = Key.right
# pressed = Key.left
# release = Key.left


#---------------- FORMA 01 --------------------------------
contador = 0

# Lanzo el Thread del Listenr de Key Pressed/released
watchKey = Listener(on_press=on_press, on_release=on_release)
watchKey.start()

# creo una rutina sinfin para simular un proceso paralelo
# al Thread Listener el Key
while True:
   #if watchKey.is_alive():                                        # puedes evaluar el estado de watchKey, corriendo en modo debug()   
   #       print(f'Thread watch is running')
   contador = contador + 1            
   time.sleep(0.3)
   print(f'{contador}', end ='\r')
   if contador > 100:
        break


#---------------- FORMA 02 --------------------------------
#watchKey = Listener(on_press=on_press, on_release=on_release)
#   with watchKey:                                                   # el 'with', permite q cuando ya este corriendo el thread se pueda hacer el .join()
#          watchKey.join()


#---------------- FORMA 03 --------------------------------
# Tambien funciona asi:
#with Listener(on_press=on_press, on_release=on_release) as listener: 
#     listener.join()                                        # Wait until the thread terminates.

