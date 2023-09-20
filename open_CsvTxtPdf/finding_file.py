# Busca un file especifico en la ruta q le indiquemos, en este caso le pedi q buscara el 
# find file = C:\$mio\phytonSpace\OpenCV\webcame\jpg_opencv.py
# from = c:\$mio\phytonSpace\miBasic\VSCode\ejercicios\finding_file.py
import sys,os
findfile = input('Name file to find:')             # ej : 'jpg_opencv.py'
fromDir = input('From q ruta <ej: C:\$mio> :')
pythonfile = findfile                          # se ubica en C:\$mio\phytonSpace\OpenCV\webcame\
 
# Para sustraer mi ruta actual
pathname = os.path.dirname(sys.argv[0])
print(f'\nIm on path.. = {os.path.abspath(pathname)}')
print(f'From Dir to find file.. = {fromDir}\n')

fn = 0 
for root, dirs, files in os.walk(fromDir):     # antes r'C:\$mio'
    #print(f'ruta={root}      ',end = '\r')
    for name in files:
        fn+=1
        print(f'files examined : {fn}   ',end='\r')
       
        # As we need to get the provided python file,
        # comparing here like this
        if name == pythonfile: 
            print(f'\n\nENCONTRADO = {os.path.abspath(os.path.join(root, name))} \n')
            break