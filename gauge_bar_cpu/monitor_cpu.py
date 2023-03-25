import time
import sys                              		# p sber la version de mi python
import psutil                                   # utilitario del S.O. p leer prop del CPU y MEMORIA
#import keyboard
import msvcrt                                   # permite detect Key Pressed, en 8bits

print(f"Version de Python={sys.version} \n")    # Ver Python=3.7.13 (default, Mar 28 2022, 08:03:21) [MSC v.1916 64 bit (AMD64)]
                                                # no funciona en ver=3.8 debido a no esta instalado el pkg                

# NOTA: 
# Caracter Special = u"\u2593" = ▓
# tipo de chr = https://www.fileformat.info/info/charset/UTF-8/list.htm?start=8192

def display_mon (cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage*0.01)                                                                      # le decimos q este valor esta basado al 100% = cpu * 1/100
    cpu_bar = u"\u2593" * int(cpu_percent * bars) + '-' * (bars-int(cpu_percent * bars))                # pinta cuantos chrs corresponden y el resto lo llena co '-' = total 100%

    mem_percent = (mem_usage*0.01)                                                                      # le decimos q este valor esta basado al 100% 
    mem_bar = u"\u2593" * int(mem_percent * bars) + '-' * (bars-int(mem_percent * bars))

    # .2f --> 2 digitos decimales de float, los labels en una sola linea.
    print(f'CPU:|{cpu_bar}|{cpu_usage:.2f}% ', end='\t')                                                # Label del CPU + 
    print(f'Mem:|{mem_bar}|{mem_usage:.2f}% ', end='\r')                                                # Label del Mem    

print()
while True:
    display_mon(psutil.cpu_percent(), psutil.virtual_memory().percent, 100)
    
    # De esta forma colocamos un Listener de KeyPressed
    if msvcrt.kbhit():
        byteKey = msvcrt.getch()                    # lo Lee en formato de Bytes b''
        txtKey = byteKey.decode('UTF-8')         # lo formateamos a codigo ASCI utf-8 texto
        
        #print(f'Key byte={byteKey} / text={txtKey}')   # will print which key is pressed
        if txtKey.upper() == 'F':
            print('Presiono Salir!')
            break

    time.sleep(0.2)


# out
# CPU:|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓---------------------------------------------------------------|37.30%        Mem:|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓