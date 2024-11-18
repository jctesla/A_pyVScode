# Cadena de caracteres
cadena = "jcdergan-https://api.wheretheiss.at/v1/satellites/25544"

# Convertir a valores ASCII
ascii_chars = [ord(char)+1 for char in cadena]

letras =[chr(l) for l in ascii_chars]


# Mostrar los valores ASCII
print(ascii_chars)
print(letras)
palabra = ''.join(letras)
print("Encripted:" , palabra)

adrrs = ""
for c in palabra:
  n = ord(c)-1
  l = chr(n)
  adrrs += l
  
print('------------------------\n')  
print("Descencripted:" , adrrs)  

print('------------------------\n')  

print("Descencripted just URL:" , adrrs[9:])  

'''
Encripted: kdefshbo.iuuqt;00bqj/xifsfuifjtt/bu0w20tbufmmjuft036655
------------------------

Descencripted: jcdergan-https://api.wheretheiss.at/v1/satellites/25544
------------------------

Descencripted just URL: https://api.wheretheiss.at/v1/satellites/25544
'''