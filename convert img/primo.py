import sys
print("Python Ver = ",sys.version)
n = int(input("Ingrese un Nro y le digo SI/NO es PRIMO :"))
cnt =0
nros=1                                                        # empiezo en 1, no es necesario el ZERO, p evitar la division/Zero
while nros <= n:                                              # evaluo todo los nros que sean menor e igual a 'n'      
  if n%nros == 0:                                             # si es divisible cuento +1
    cnt+=1
  nros+=1  

#---RESULTADO
if cnt==2:
    print("El Nro",n, " = SI es PRIMO")
else:
    print("El Nro",n, " = NO es PRIMO")  
      

print("\n------------------")
#-----------------------------
# rutina forma 1
for n in range(0, 31):
    primo = False
    cnt=0
    for v in range(1, n+1):
        if n % v == 0:
            cnt+=1
    if cnt==2:
      primo = True            
            
    if (primo): 
        print (n, 'es primo')
    else:
        print (n,'no es primo')
        
print("\n------------------")
#-------------------------------
# rutina forma 2
n = int(input("Ingres un Nro :"))
m = 1
while m <= n:                                  # creamos un rango nros: 0...n
  div=0                                        # esta variable va dividir c/nro q le demos, en este caso del rango.
  cnt=0                                        # el nro de veces q es divisible un Nro si = 2 :. es divisible por si mismo y la unidad.
  while div <= m:                              # recorremos el Nro seleccionado y verificamos cuantas veces es divisible.
    if div!=0:                                 # si es = 0 va salir error division x ZERO :. evaitamos este erro, otra forma es usar try exception
      if m%div==0:
        cnt+=1
    div+=1
  
  #-----FINAL----------  
  # si hay +2 de nros divisibles no es primo.
  if cnt==2:
    print("El Nro",m, " = SI es PRIMO")
  else:
    print("El Nro",m, " = NO es PRIMO")  
  
  m+=1                                         # incremento al nro siguiente  
      
    
  
  