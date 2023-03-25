h = 'esto va para todos'      
sp=h.split(' ')             # ['esto', 'va', 'para', 'todos']
hh = ' '.join(sp)
print(hh)                   # esto va para todos


nrs = [n for n in range(0,100)]
for n in  nrs:
   print(n,end= ' ')
   if n%4 == 3:
      print()


n = [n  for n in range(1,50,2)]
print(n)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# n = nro de spcs , b=nro de balls.
def steps(n,b):
  spc=""
  balls=""
  for s in range(n-(b//2)):
	   spc = ' ' + spc
  for ss in range(b):
	   balls=balls + '0'
  print(spc+balls)
  
   
for p in n:
	steps(len(n),p)


# creo una medida que es de 0-->360  como lo llevo a una escala de 1..5 ?
med= 360
for i in range(med):
  print('{0:.03f}'.format((i*4)/360 + 1), end=' ')

# Out:
# 1.000 1.011 1.022 1.033 1.044... 4.956 4.967 4.978 4.989     

# 1.00 1.01 1.02 1.03 1.04 1.05 ... 1.94 1.95 1.96 1.97 1.98 1.99 

num = 123.4567
print('\n {0:.2f}'.format(num))
	