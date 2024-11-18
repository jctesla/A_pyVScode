#from decimal import *
#n = int(Decimal(input('Ing un Nro:')))

s = input('Ing un Nro:')
n = int(s.split('.')[0])

# Nro Absoluto (+)
if n < 0:
   n = n*-1
 
ndig=0
r = n

while True:
   if r>10:
      ndig+=1
      r = int(r/10)
   else:
      ndig+=1
      break

#----------------
print(f'El nro:{n} tiene={ndig}digitos')      