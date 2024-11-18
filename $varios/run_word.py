# Este ej visualiza c/letra de izq-->derech.
import time
palabra = "Hola amigos!"
spc= " "
for id in list(palabra):
    print(spc,id,end='\r')
    spc += ' '
    time.sleep(0.3)
    
#-------------------------------------------
# Este ej corre un mensjae de izq--->derecha
mensaje = "Hola amigos!"
spc = " "
for id in range(40):
    print(spc,mensaje,end='\r')
    spc += ' '
    time.sleep(0.2)

#-------------------------------------------
# Aspa jirando
spc= " "
pos=0
for id in range(40):
    if pos==0:
        print(spc,"|",end='\r')
        pos=1
    elif pos==1:
        print(spc,"/",end='\r')
        pos=2
    elif pos==2:
        print(spc,"--",end='\r')
        pos=3
    elif pos==3:
        print(spc,chr(92),spc,end='\r')   #92 es el ascci de \
        pos=0
    time.sleep(0.1)    

