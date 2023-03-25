import sys
import msvcrt

print("python ver=", sys.version)
print("Cual es tu Nombre?")

busKey = ""
while True:
  
  if msvcrt.kbhit():
    byteKey = msvcrt.getch()                    				     # lo Lee en formato de Bytes b''
    tecla = byteKey.decode('UTF-8')         
    if tecla == chr(27):
      print("Hasta luego....")
      break
    else:
      busKey = busKey + tecla
      if tecla == chr(13):
        print(" " + busKey + " ")       #,end= chr(10) + chr(13))
        print("Listo presiones ESC o continue escribiendo")
        busKey = ""
      else:
        print(busKey + u"\u2593" ,end=chr(13))

# salida:
# (base) D:\>python make_question_01.py
# python ver= 3.7.13 (default, Mar 28 2022, 08:03:21) [MSC v.1916 64 bit (AMD64)]
# Cual es tu Nombre?
# Juan carlos
# Listo presiones ESC o continue escribiendo
# Hasta luego....

# (base) D:\>_          
