from PIL import Image
import os
from datetime import datetime as dt

# Dir Actual, donde se encuentra este file
print(f'Dir Actual = {os.getcwd()}')

# VERIFY AND OPEN IMAGE FILE DIRECTORY
dirExist = False
PATH_Dir = 'F:\\Imágenes de muestra'                                              # you can use always: C:/mydir' or 'C:\\mydir' you can also try raw string literals: r'C:\mydir'
if os.path.isdir(PATH_Dir) and os.access(PATH_Dir, os.R_OK):
   os.chdir(PATH_Dir)                                                             # nos cambiamos al Directorio indicado.
   print(f'...Dir Encontrado = {os.getcwd()} / Listo algunos Files:')             # vozualizo la ruta en que me ecuentro actualmente ~ $ pwd
   
   lstfiles = os.listdir(os.getcwd())
   for idx,filename in enumerate(lstfiles):
      print(f'{idx}.- {filename}')
      if idx > 5:
        break
   
   dirExist = True
else:
   print(f'No existe el Dir = {PATH_Dir}')



# Si dirExist = True, pasamos a leer los .png files
# to convert in to .ico   
if dirExist : 
   print()
   basewidth = 300
   for idx,filename in enumerate(lstfiles):
      img = Image.open(filename)                                    # abre imagenes del tipo .jpg
      wpercent = (basewidth / float(img.size[0]))
      hsize = int((float(img.size[1]) * float(wpercent)))
      img = img.resize((basewidth, hsize), Image.ANTIALIAS)
      _jpg = filename.find('.jpg')
      img.save(filename[:_jpg] + '_' + str(idx) + '.jpg')
      if idx > 5:
        break