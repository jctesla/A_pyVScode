import random
import msvcrt

def ale():
    n1 = int(random.random()*100)
    n2 = int(random.random()*100)
    print(f"suma {str(n1)} + {str(n2)} = ?")
    return 

while(True):
   if msvcrt.kbhit():
      bytekey = msvcrt.getch()
      tecla = bytekey.decode('UTF-8')
      		
      if tecla == chr(27):
         print("Hasta Luego...")
         break
		
      if tecla == chr(13):
         print("HOLA")
         ale()
	

             	