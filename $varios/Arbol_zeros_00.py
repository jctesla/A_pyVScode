# Solo Nros Impares:
n = [n  for n in range(1,50,2)]	# out: [1, 3, 5, 7, 9, 11, 13, 15,.., 33, 35, 37, 39, 41, 43, 45, 47, 49]
				
def steps(n,b):		# n:nro de spcs , b:nro de ‘0’.
  spc=""
  balls=""
  for s in range(n-(b//2)):	# los spcs tiene una formula decreciente.
     spc = ' ' + spc
  for ss in range(b):		# los 0s tiene una formula creciente.
     balls=balls + '0'
  print(spc+balls)		# sumados dan la sensacion de un Arbol.
  
for p in n:			# imprime c/linea de ‘0s’
  steps(len(n),p)		# imprime solo la linea de 0s correspondiente a orden de linea.

