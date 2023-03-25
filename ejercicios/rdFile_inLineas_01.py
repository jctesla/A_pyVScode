from logging import exception
from datetime import datetime as d
from msilib.schema import Error
import os

# Verificamos si Existe el File/Dir
PATH = './resumen.txt'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
   print(f'Si el File existe pero no se sabe si tiene Datos')
else:
   print(f'No existe este File o Directorio')   

# Aqui probamos como se comporta si no/si existe el file
cnt = 0
mif = None
try:
   mif = open('resumen.txt','r')
   for linea in mif:
      linea = linea.rstrip()	                     # quita del 'linea' el 'LF' o \n de la linea leida del txt.
      cnt += 1	
      print(linea)
   
   print(f'Se leyo Documento de ={cnt} Lineas')
      
except FileNotFoundError  as  ex:
         #mif.close()
         r = input(f'No se Encontro el File! err={ex}, desea Crearlo?')
         if r.upper()=='Y' or r.upper()=='YES' or r.upper()=='SI':
            mif = open('resumen.txt','w')
            mif.write(f"file Creado fecha={d.now()}")
            print(f'File Creado!')
            mif.close()
         else:
            print(f'Fin no se Creo el File que no se Ubico!')
                  

