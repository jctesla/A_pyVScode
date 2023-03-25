# En esta clase se ref a la variable Global,
# y se usa una Herencia 'list' a la clase 'List'

# var Global
cnt = 0

#-----------------------------------
class miList(list):                               # miList hereda de la clase 'list'
   def __init__(self, lbini='nc'):
      global cnt
      cnt += 1
      self.append(lbini)
      pass   
   
   def push(self,x):
      self.append(x)
   
      
#--------------- MAIN () -----------
s = miList('Contructed step 01')
s.push(10)
s.push('A')
print(s)                                           # ['Contructed step 01', 10, 'A']

p = miList('Contructed step 02')
p.push(20)
p.push('B')
print(p)
 
k = miList('Contructed step 03')
k.push(30)
k.push('C')
print(k)

