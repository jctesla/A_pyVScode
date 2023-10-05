
#--------------- DATOS 2D de FIGURA ---------------------
def get_dim2d(mi_array):
    
  if isinstance(mi_array, list):          # verificamos si el obj es un list
    rows = len(mi_array)
    print(f'este arrya tiene rows={rows}')
    if rows>0:
       cols= len(mi_array[0])  
    else:
       cols= 0
    
    print(f'Esa Matrix rows={rows} cols={cols}')       
    return (rows,cols)


m_simetrica_orig=[]
m_simetrica_dest=[]

        
#--------------- ROTAR FIGURA ---------------------
def rota2d(mi_array,angulo):
  rows,cols = get_dim2d(mi_array)
  print(f'd2arry = {(rows,cols)}')
  ruta=[(r,cols-c-1)  for c in range(cols): for r in range(rows)]  
  rotDer=[]
  if rows == cols:
    for r in range(rows):
      for c in range(cols):
        rotDer[r,c]= mi_array[cols,rows-r-1]
  else:
      
  
  
  return d2arry
  
  
  
    

list_array = [
              [1, 2, 2, 3],
              [1, 2, 2, 3],
              [1, 2, 2, 3],
              [1, 2, 2, 3],
              [1, 2, 2, 3],
              [1, 2, 2, 3]
             ]


dimensions = rota2d(list_array,90)

print(dimensions)


