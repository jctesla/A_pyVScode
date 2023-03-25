h=0
if h is False:
   print("Falso")
else:
   print("Verdadero")
   
dic = {}
dic['uno']=1
dic['dos']=2
dic['tres']=3
print(f'dic={dic}')
print(f"dic contiene a key=cuatro?, verifiquemos:. dic = {dic.get('cuatro','NO CONTIENE')}")


#---------------------------------

listDic = {'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24}
for k, v in listDic.items():
    print(f'key={k},val={v}', end=' | ')
    
print()
for k,v in enumerate(listDic):
    print(f'key={k},val={v}', end=' | ')
 
