def add_many(*args):
    s = 0
    for n in args:
        s += n
    print(s)

add_many(100, 50, 3)

#----------------------------
class Dog:    
  def woof(self):
     return 'woof!'

t = Dog()
print(t.woof())

#----------------------------------
