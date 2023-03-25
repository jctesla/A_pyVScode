cnt = 0

#---------------------------------------
class List(list):
   def __init__(self,cntIni=0):
      global cnt
      cnt  += cntIni
      print(cnt)	
      pass   
   
   @staticmethod
   def push(self,x):
      self.append(x)
   
      
#--------------- MAIN () ---------------
s = List(1)
s.push(10)
s.push('A')
print(s)

p = List(4)
p.push(20)
p.push('B')
print(p)
 
k = List(8)
k.push(30)
k.push('C')
print(k)


