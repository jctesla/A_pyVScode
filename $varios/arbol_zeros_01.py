n=30 #cuantos zeros como max

# func() permite colocar
# pre-spaces zeros pos-spaces
def spcZero(nSpc,nZero):
  print(' '*(nSpc//2),end='')
  print('0'*nZero,end='')
  print(' '*(nSpc//2),end='\n')
  
# generar linea de zeros impar
for i in range(n):
  if i%2 !=0:
    spcZero(n-i,i)