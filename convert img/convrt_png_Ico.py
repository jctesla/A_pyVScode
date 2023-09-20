# https://pillow.readthedocs.io/
# PIL :  Python Imaging Library (Python3), Pillow es la bifurcación amigable de PIL que mantuvo viva la biblioteca e incluye soporte para Python 3
# PIL vs OPenCV; The beauty of OpenCV is, you can see numerous examples on its website in Python, C++, and Java

import os
from PIL import Image

# Dir Actual, donde se encuentra este file
print(f'Dir Actual = {os.getcwd()}, verifying dir Icons...')



# 1º VERIFY AND OPEN Sources IMAGE FILE DIRECTORY
dirExist = False
PATH_Dir = 'G:\\iconos\\tmp'                                        # dir de imagenes .png 

if os.path.isdir(PATH_Dir) and os.access(PATH_Dir, os.R_OK):        # verifico q exista el Directory y que tenag permiso de lectura minimo. 
   
   os.chdir(PATH_Dir)                                               # c:\>cd PATH_DIR  ; el cursor lo cambiamos al Directorio indicado.
   print(f'files encontrados en Dir = {os.getcwd()}')               # ruta de las imagenes .png origen para convertir.
   lstfiles = os.listdir(os.getcwd())                               # c:\>dir          ; hacemos un listado del directorio actual.
   if len(lstfiles) > 0:
      for idx,filename in enumerate(lstfiles):
         print(f'{idx}.- {filename}')                               # vizualizo ruta de c/imagen .png    
      dirExist = True
      
   else:      
      print(f'NO Hay Files en este Directory')   

else:
   print(f'No existe el Dir = {PATH_Dir}')



# 2º Si Dir File Exist, dirExist = True,
# pasamos a leer los .png files to convert in to .ico   
if dirExist : 
   print()
   for idx,filename in enumerate(lstfiles):
      print(f'{idx}.- File to Convert = {filename}')
      os.path.join(PATH_Dir, filename)
      print(f'la ruta es = {os.path.abspath(filename)}')          # Read the full path of a file python

      icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
      img = Image.open(filename)
      _png = filename.find('.png')
      img.save(filename[:_png] + '.ico',size=1)                   # Crea ub file.png del tipo 32x32 bits


# Dir Actual = D:\phytonSpace\miBasic\A_pyVSCode\convert img, verifying dir Icons...
# files encontrados en Dir = G:\iconos\tmp
# 0.- DataCamp.png
# 1.- localize_telegram.png
# 2.- pair_google.png
# 3.- ytb_rip_dwnloadYoutube.png