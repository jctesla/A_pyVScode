b = b"Lets save: \xf0\x9f\x8d\x95"                        # <class 'bytes'>
s = b.decode('UTF-8')                                     # Now, let's decode/convert them into a string
print(f'De byte a string = {s}')                          # De byte a string = Lets save: 🍕
c= u"\u2593" + " : char especial"                         # ▓ : char especial
print(c)
# NOTA: tipo de chr especial= https://www.fileformat.info/info/charset/UTF-8/list.htm?start=8192

#------------------------------------------
h = 'Hola Mundo'

arryBin = h.encode()                                      # lo obliga a convertirse en un arreglo binario()
print(f'arreglo Binario inmutable = {arryBin}')           # Binary Array = b'Hola Mundo'

for id in arryBin:
  print(f'{id}', end= ' ')                                # Asci = 72 111 108 97 32 77 117 110 100 111

print()
for id in h:                                              # usando el arreflo String() / ord(asci)  / bin(int)
  print(f'{bin(ord(id))}', end= ' ')                      # bin = 0b1001000 0b1101111 0b1101100 0b1100001 0b100000 0b1001101 0b1110101 0b1101110 0b1100100 0b1101111

print()
for id in arryBin:                                        # usando el arreglo ya en binario()
  print(f'{bin(id)}', end= ' ')                           # bin = 0b1001000 0b1101111 0b1101100 0b1100001 0b100000 0b1001101 0b1110101 0b1101110 0b1100100 0b1101111

print()
for id in arryBin:                                        # usando el arreglo ya en binario()
  print(f'{bin(id).replace("0b", "")}', end= ' ')        # bin = 1001000 1101111 1101100 1100001 100000 1001101 1110101 1101110 1100100 1101111

print()  
for id in arryBin:
  print(f'{chr(id)}', end= ' ')                           # Char = H o l a   M u n d o


print(f'\n\nBin to Decimal')
for id in arryBin:                                        # usando el arreglo ya en binario()
  print(f'bin={bin(id)} dec={int(bin(id),2)}')
  
#---------------------- BYTES / BYTEARRAY ------------------  
# bytes(x) = inmutable, crea un arreglo
# con los valores de x
h = 'Hola Mundo'
arryBin = bytes(h,'utf-8')                                # 'initialize' an array of byte’s object and 'encoding' = used only when the source is a string
print(f'arryBin ={arryBin}')                              # b'Hola Mundo'     // c/posicion la convierte en un BYTE la 'b' indica q es un BYTE x c/digito

mibytes = [1,2,3,4,5]                                     # ERROR si nums = ['A','B','C']
array = bytes(mibytes)
print(array)                                              # b'\x01\x02\x03\x04\x05'

num = 10
array = bytes(num)                                        # crea una pos de 10bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(array) 

array = bytes(3)                                          # crea una pos de 10bytes = b'\x00\x00\x00'
print(array) 
print('\n\n')

# BYTEARRAY = mutable
mibytes = [1,2,3,4,5] 
byteArry = bytearray(mibytes)                            # bytearray(b'\x01\x02\x03\x04\x05')
print(byteArry)
print(byteArry[0])                                       # 1
byteArry[0] = 15
print(byteArry)                                          # bytearray(b'\x0f\x02\x03\x04\x05')


#mibytes = ['A','B','C']                                  # ERROR
#byteArry = bytearray(mibytes)                            # bytearray(b'\x01\x02\x03\x04\x05')

#----------------------------------
enBytes = b'ABC'                          # ya defini q es un stream de Bytes.
print(type(enBytes))                      # <class 'bytes'>

# pero si quiero q esos ABC sean lo q representan
streamBytes = bytes(enBytes)
print(streamBytes)                        # b'ABC'

# pero si tengo un String = 'Hola'
# lo podemos poner en su represent d Bytes?
streamBytes = bytes('Hola', 'utf-8')
print(streamBytes)                        # b'Hola'

# ó

streamBytes = 'Hola'.encode()
print(streamBytes)                        # b'Hola'


miPng = 'hola.png'
f = open(miPng,'rb')                      # 'rb' means read as bytes.
png = f.read()
print(png)                                # lee cada byte de la imagen


