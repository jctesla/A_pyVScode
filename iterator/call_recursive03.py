# usamos la recursividad para saber si un Nro es PRIMO.

# sino decalro cnt se asign asi mismo =0
# cntr = nos indica si es divisble x unidad y si mismo cntr=2
# si es dif!= 2 :. no es PRIMO, el concepoto de PRIMO=cntr=2
def n_divs(n,div,cnt=0):
  if div < 1:
    return cnt
  if n%div==0:
    cnt+=1
  f=n_divs(n,div-1,cnt)
  return f

nro = 11
primo = n_divs(nro,nro)
if primo == 2:
  print("Es un Nro PRIMO")
else:
  print("NO Es PRIMO")
