# modos de aprtruar un file ne python con open():
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
from datetime import datetime as dt
import os
import sys
import subprocess

# flags de estados
flgExist = False
PATH_file = './vitacora_at_boot.txt'

# 1º Version de Python y Donde me encuentro?
pyver = sys.version
print(f'Python ver = {pyver}')
print(f'Dir Actual = {os.getcwd()}, {dt.now()}')

# Verificamos si Existe el File .isfile(PATH) y 
# si se puede leer .access(PATH, os.R_OK)
if os.path.isfile(PATH_file) and os.access(PATH_file, os.R_OK):
   print(f'File SI Existe!')
   flgExist = True
else:
   print(f'File NO Existe! we have to creat it')


# Get my Own ip Host, Temp & Voltage
# ip = subprocess.check_output(["hostname","-I"])                     # sino existe este comando saldra ERR: subprocess.CalledProcessError: Command '['hostname', '-I']' returned non-zero exit status 1.
# print(f"La Ip de tu raspBerry es = {ip}")
# tmp = subprocess.check_output(["vcgencmd","measure_temp"])
# print(f"Temp Raspi = {tmp}")
# voltg = subprocess.check_output(["vcgencmd","measure_volts"])
# print(f"Temp Raspi = {voltg}")



# Creamos la Vitacora   a=append, t = text
f=open(PATH_file, 'at')
f.write(f"------------------------------------------------------------\n")
f.write(f"Files del Directorio, {dt.now()}\n")
f.write(f"Python Ver = {pyver}")
#f.write(f"ip={ip}")
#f.write(f"temp={tmp} voltg={voltg}")

lstfiles = os.listdir(os.getcwd())
for idx,filename in enumerate(lstfiles):
  if os.path.isdir(filename):
    f.write(f"{idx}.- {filename} - dir\n")          # es un Directorio
  else:
    f.write(f"{idx}.- {filename}\n")                # es un File

f.close()



