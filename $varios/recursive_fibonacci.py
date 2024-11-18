'''
Lo mas importante en la serie de fibonacci es que cada nro es la suma de los dos nros anteriores!
Ahora pueden darte un N° de inicio != 0 o 1 :. la regla de ORO es:
1° el primer Nro de inicio seria el mismo N°, el siguiente seria la suma del mismo numer, 
Ej: inicio=5 cuales son los 3 sgnts numeros?
5,5+5=10,5+10=15,10+15=25  :. 5,10,15,25

Pero si no te dicen desde que N° empieza :. el N° inicial = 1.
1,1+1=2,1+2=3,2+3=5,3+5=8,5+8=13,8+13=21,13+21=34,21+34=55 :. 1,2,3,5,8,13,21,34,55 

En este Ejmplo presentamos una Func() recusriva y una serie Fibinacci:
Ej: si busco la serie de los 1ros 10 numeros de Fibonacci empezando por el N°1, serian : 
0+1=1,seria: 1,1,2,3,5,8,13,21,34,55

Ej: si busco la serie fibonacci de los 10 numeros sgnts, empezando por el N° 5, serian :
[5, 10, 15, 25, 40, 65, 105, 170, 275, 445]

'''
def fibonacci(n,idx,arry=[]):
   if idx < 1:
       return arry
   else:
       if len(arry)==0:
           arry=[n,n+n]
           idx-=2
       else:
           arry.append(n)
           idx-=1
   return fibonacci(arry[-1]+arry[-2],idx,arry)   
       

# Cacular la secuencia de fibonacci desde un N° inicial hasta los siguientes 10 nros.
r = fibonacci(1,10)
print(r)
# [5, 10, 15, 25, 40, 65, 105, 170, 275, 445]
