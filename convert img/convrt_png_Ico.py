import os
from PIL import Image

# Dir Actual, donde se encuentra este file
print(f'Dir Actual = {os.getcwd()}, verifying dir Icons...')



# 1º VERIFY AND OPEN IMAGE FILE DIRECTORY
dirExist = False
PATH_Dir = 'G:\\iconos\\tmp'                                        # dir de imagenes .png 
if os.path.isdir(PATH_Dir) and os.access(PATH_Dir, os.R_OK):
   os.chdir('G:\\iconos\\tmp')                                      # el cursor lo cambiamos al Directorio indicado.
   print(f'...Dir Encontrado = {os.getcwd()}')                      # ruta de las imagenes .png origen para convertir.
   lstfiles = os.listdir(os.getcwd())
   for idx,filename in enumerate(lstfiles):
      print(f'{idx}.- {filename}')                                  # vizualizo ruta de c/imagen .png    
   
   dirExist = True
else:
   print(f'No existe el Dir = {PATH_Dir}')



# 2º Si dirExist = True,
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
      

