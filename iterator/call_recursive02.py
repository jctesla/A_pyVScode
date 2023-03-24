
# usamos la recursividad para crear una func() de fibonacci.
def fib(n,sum=0):
  if n < 1:
    return sum
  sum += n
  f= fib(n-1,sum)
  return f
 
print(fib(3))

print(fib(5)) 