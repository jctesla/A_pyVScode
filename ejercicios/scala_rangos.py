
# Este metodo sirve p crear scalas dentro de un rango de una serie de numeros:
# en este caso si la serie=0..100, y quiero rangos de scala de 0..3 :. div=4
# Evalua el Residuo de la div de 0..99 respecto al divisor
# si div=2 :. imprime 50 '0's  y  50 '1's
# si div=3 :. imprime 34 '0's  y  33 '1's  y  33 '2's   
# si div=4 :. imprime 25 '0's  y  25 '1's  y  25 '2's  y  25 '3's 

div = 5
for x in range(100):
  print(x%div,end='-')        
  
#------------------------------------------------------------------------------  
# si quiero q en 360 grados tenga una salida en el rango de 0..15grados
for x in range(360):
   print(f'{(x%15):.2f}',end='-')

# en una serie de 0--360 grados, solo qiero una scala de salida de 1.00...4.59
for x in range(360):
   print(f'{(x/100 + 1):.2f}',end='-')

