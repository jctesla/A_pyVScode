L = [74,74,69,70,70,70,70,66,74,67]
p=0
for i in L:
  p+=i

pr = p/len(L)
print("pr=",pr)         # 70.4

p=0
for i in L:
  p+= (i-pr)**2

pr = p/len(L)
print("pr=",pr)           # 7.239999999999999
                          # desv Estandar = SQRT(7,2399) = 2.69

  
