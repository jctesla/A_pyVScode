# calculo de la serie de fibonacci
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n-1) + fibonacci(n-2)

# genero la secuencia empezando si solo empieza en 1:
for i in range(1,10+1):
   print(fibonacci(i),end=", ")
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55,