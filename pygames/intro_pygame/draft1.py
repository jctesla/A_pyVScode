 # rotate matriz simetrica 90º
matriz = [
           [10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]
         ]
mresult = [
           [10, 20, 30],
           [40, 50, 60],
           [70, 80, 90]
         ]



rows=3
cols=3

# secuencia Gira derecha 90º
ruta=[[rows-r-1,c]  for c in range(cols) for r in range(rows)]
print(ruta)

# asignacion segun secuencia
cont=0
for r in range(rows):
  for c in range(cols):
    mresult[r][c] = matriz[ruta[cont][0]][ruta[cont][1]]
    cont+=1

print(mresult)  
