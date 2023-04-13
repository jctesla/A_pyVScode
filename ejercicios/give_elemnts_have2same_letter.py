# Devuelve todo los elmentos de un Dictionary q contenga las 2 primeras letras iguales:


# ------ Data
phbook = {
    "John": "3105551212",
    "Bob": "9496667777",
    "Alice": "7144445555",
    "Bobi" : "90909090",
    "Alicia": "28282882",
    "BobLazar":"323232323",
    "Jonny": "3105533333",
    "BobMatrh" : "92222222"
}

# ------ para Un solo elemento de la lista
prefix = "ap"
result = {k:v   for k,v in phbook.items()   if k.startswith(prefix)}
print(result)


# ------- para Todo los elementos de la lista
cpy=[i[:2]   for i in phbook.keys()]                          # hago una copia de los keys pero solo los 2 1ras letras
dictio={}
for k,v in phbook.items():
  try:
    if dictio[k[:2]] in dir():                                # sino existe este elemento, try
      dictio[k[:2]] = cpy.count(k[:2])
      continue
  except:
    dictio[k[:2]] = cpy.count(k[:2])
    
print(dictio,'\n')                                            # {'Jo': 2, 'Bo': 4, 'Al': 2}


# ------- Otra Forma
dictio={}
rep=[k[:2]  for k,v in phbook.items()]
repp = set(rep)
dictio = {i:rep.count(i)   for i in repp}
print(dictio)                                                 # {'Jo': 2, 'Bo': 4, 'Al': 2}