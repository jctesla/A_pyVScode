# Object Generator  is a special type of function which does not return a single value,
# instead, it returns an 'Iterator Object' with a sequence of values

def calculo(number):
   return number*number

def miYield(rangeN):
  for i in range(rangeN):
    yield calculo(i)                # similar a 'return', but yield return an Object Generator
                                    # en lugar de devolver un valor o objecto, devuelve un Obj Iterador.
                       
va = 5

#------froma 00-----------
myld = miYield(va)
while True:                         # no way, most create a parallel counter 'c' for Iterator.
  try:
    rs= next(myld)                 # de alguna manera myld devuelve la direcc de memoria del valor.
    print("myld=",rs)
  except StopIteration:
    break

#------froma 01-----------
myld = miYield(va)
c=va
while c > 0:                        # no way, most create a parallel counter 'c' for Iterator.
   rs= next(myld)                   # de alguna manera myld devuelve la direcc de memoria del valor.
   print("myld=",rs)
   c -=1
   
#------froma 02-----------
myld = miYield(va)                  # la func() q contenga el Yield, se convierte en un Obj Iterador, myld no contiene
for idx in myld:                    # aun todo los valores, sino c/vez q invoco a la func(), el pc salta y regresa el valor.
  print("myld=",idx)                
   
#------froma 03-----------   
myld = miYield(va)
print("myld=",next(myld))          # 0      
print("myld=",next(myld))          # 1                 
print("myld=",next(myld))          # 4      
print("myld=",next(myld))          # 9      
print("myld=",next(myld))          # 16      
    
    