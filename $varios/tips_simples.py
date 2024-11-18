# devuelve un DICT y LIST
def function(key, value=0):
    d = {key: value}
    l = [key, value]
    return d, l
print("1.- ", function('llave',300),'\n')                             # ({'llave': 300}, ['llave', 300]) 

#-------------------------
user =['Jan', 'Gomez', '+1-888-222-1546']
name, title, phone = user
print("2.- ", "name:" + name,"  Titulo: ",      
    title, "  Telf:", phone ,'\n')                                    # name:Jan   Titulo: Gomez   Telf: +1-888-222-1546 

jan, (gname, gtitle, gphone) = "maria",user
print("3.- ", "n:", jan, "  datos:",gname, gtitle, gphone ,'\n')     # n: maria    datos: Jan Gomez +1-888-222-1546 

print("4.- \n")
people = [user, ['German', 'GBT', 'unlisted']]
for (name, title, phone) in people:
      print (name, phone)

#-------------------------
#datos
colors = ['red', 'blue', 'green', 'yellow']

# concatenation:
unir  = ''.join(colors)
print("5.- ", unir, "\n")                                           # redbluegreenyellow

# concatenacion con coma:
unir  = ', '.join(colors)
print("6.- ", unir, "\n")                                           # red, blue, green, yellow 
#-------------------------
# Not this :
# if len(items) != 0:
#    pass	

# Do this : 
# if items:
#    pass

#-------------------------
#Use enumerate when it’s possible(index, item)
lista = ['zero', 'one', 'two', 'three']
print ("7.- ",  list( enumerate(lista)), "\n" )               # [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three')]

#-------------------------
# With a list comprehension :
total = sum([num * num for num in range(1, 5)])
print("8.- total=",total)                                     # total= 30