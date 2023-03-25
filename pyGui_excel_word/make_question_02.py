import sys
import msvcrt

print("python ver=", sys.version)
p = input("Cual es tu Nombre?")

busKey = ""
while True:
  print("Listo presiones 'q' y luego ENTER para salir.")
  p = input("Cual es tu Nombre?")
  if p == 'q' or p=='Q':
    print("Hasta luego....")
    break
  
# salida:
# (base) D:\>python make_question_01.py
# python ver= 3.7.13 (default, Mar 28 2022, 08:03:21) [MSC v.1916 64 bit (AMD64)]
# Cual es tu Nombre?
# Juan carlos
# Listo presiones ESC o continue escribiendo
# Hasta luego....

# (base) D:\>_          
