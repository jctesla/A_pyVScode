b = b"Lets grab a \xf0\x9f\x8d\x95!"
# Let's check the type
type(b)
#<class 'bytes'>

# Now, let's decode/convert them into a string
s = b.decode('UTF-8')


#--------------------------
prime_numbers = [2, 3, 5, 7]

# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')

#--------------------------
# BYTES = inmutable
txt = 'Hola Mundo'                                        # es un String = arreglo de chars.
arryByts = bytes(txt,'utf-8')                             # 'initialize' an array of byte’s object and 'encoding' = used only when the source is a string
print(f'arryBin ={arryByts}')                             # b'Hola Mundo'  // 'b' indica q es un BYTE x c/digito
print(arryByts.decode(encoding='utf-8'))                  # 'Hola Mundo'   // convierto array de bytes a string de c/chr de 8bits .

nums = [1,2,3,4,5]					                              # esun list cualquiera de nros.
array = bytes(nums)                                       # creo un arreglo de bytes.
print(array)                                              # b'\x01\x02\x03\x04\x05'     // 'b' es q esta en BYTES

num = 10
array = bytes(num)                                        # crea una arreglo de 10 elementos de BYTES.
print(array)                                              # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


