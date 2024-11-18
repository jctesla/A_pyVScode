def miF(x):
   return (x%2!=0 and x%3!=0)	# devuelve solo nros q no son pares ni divisibles x 3

rslt = filter(miF, range(1,100))	# el resultdo lo apila en un arreglo, q no tiene iteration x eso list.
print(f'rslt = {list(rslt)} \n\n')

print("---------------------------\n")
arry1=range(8)			# arry1 = [0,1,2,3,4,5,6,7].............. 7 elementos
arry2=range(8,15)			# arry2 = [8,9,10,11,12,13,14].........6 elementos
print(f'arry1={arry1}/arry2={arry2}\n')

def suma(x,y):
   return(x+y)

rslt = map(suma,arry1,arry2)
print(f'rslt de arry1 + arry2 = {list(rslt)} \n')
