# {"author": "Me", "time":"9:00", "date": "today"}
# print_dict, permite atravez de ** crear un dictiroanry

def print_dict(**kDict):
  for key in kDict:
    print(key + ": " + kDict[key])
  return kDict  

   
print_dict(author="Me", time="9:00", date="today")
print()
print_dict(author="Someone", text="My example text")
print('.........')

miDictionary = print_dict(author="JuanCalos", text="Buscando mi Destino")
for key in miDictionary:
    print(key + ": " + miDictionary[key])


# salida: 
# author: Me
# time: 9:00
# date: today
#
# author: Someone
# text: My example text







