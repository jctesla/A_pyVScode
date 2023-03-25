import os
import subprocess
print(os.listdir('/ProgramData/'))                    # <class 'list'> 
# ['Application Data', 'BSD', 'Datos de programa', 'Dell', 'Desktop', 'Documentos', 'Documents', 'Escritorio',
# 'Favorites', 'Favoritos', 'Intel', 'Men� Inicio', 'Microsoft', 'ntuser.pol', 'Package Cache', 'Plantillas',
# 'Sprint', 'Start Menu', 'Templates', 'TweakBit']

subprocess.call( ['conda', 'env', 'list'] )

# salida:
# conda environments:
#
# base                     C:\ProgramData\Anaconda3
# OpenCV                   C:\ProgramData\Anaconda3\envs\OpenCV
# miFastApi                C:\ProgramData\Anaconda3\envs\miFastApi
# mifastapi                C:\ProgramData\Anaconda3\envs\mifastapi
# tf                       C:\ProgramData\Anaconda3\envs\tf