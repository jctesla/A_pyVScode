# Nota:
# crea un rango de A..E y luego usa un lambda p generar una secuencia de 30 caracteres usando el rango A..E
list_AZ = [chr(L)  for L in range(ord('A'),ord('E')+1)]
print(list_AZ)                                            # ['A', 'B', 'C', 'D', 'E']
e = lambda L : list_AZ[L%len(list_AZ)] 
#print(e(5))
#d = dict()
for i in range(30):
  print(e(i),end='-')                             # creo un dictionary de keys=A..E  y values=0..30
                                                  # A-B-C-D-E-A-B-C-D-E-A-B-C-D-E-A-B-C-D-E-A-B-C-D-E-A-B-C-D-E-



