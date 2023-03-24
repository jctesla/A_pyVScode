
def lista(L):
  lista=[]
  if type(L)== list:
    for ele1 in L:
      if type(ele1) == list:
        for ele2 in ele1:
          lista.append(ele2)
      else:
     		lista.append(ele1)
  else:
     lista=None
  return lista


print(lista([1,2,3,['a','b','c'],10]))

