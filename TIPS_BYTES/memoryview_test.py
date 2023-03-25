# Genero Array de Letras de la 'A..Z'  y 'a..z'
L_AZ = [chr(L)  for L in range(ord('A'),ord('Z')+1)]
L_az = [chr(L)  for L in range(ord('a'),ord('z')+1)]

# Uno los 2 Grupos
# convert List[] to Set()
cAZ = set(L_AZ)
caz = set(L_az)
C = cAZ.union(caz)

# convert Set() to List[]
# ordeno el ABC
Letras = list(C)
Letras.sort()
print(Letras)                                           # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Convierto el List[] a string()
strLetrasUp = ''.join(L  for L in Letras)
print(strLetrasUp)                                      # ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

# Si revertimos el Orden
Letras.sort(reverse=True)
strLetDwn = ''.join(L  for L in Letras)
print(strLetDwn)                                        # zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA
print('\n\n')

#-------------------------------------
# Equivalent memoryview()
# created a memory view object
# memoryview() retorna un Obj representativo del arreglo
txt = 'ABC012'
print(bytes('ABC012','utf-8'))                          # b'ABC012'                 // para strings

byteArry = bytearray(txt, 'utf-8')                      # convierto el String a un arreglo de bytes.
mv = memoryview(byteArry)                               # se crea un Obj con acceso al arreglo = <memory at 0x0000000001EC7DC0>

# acceder al índice zero de memoryview()
print(mv[0])                                            # 65 = b'A'                 // byte
print()

# create byte from memoryview()
print(dir(mv))                                          # crea un Obj that represent the binary array = <memory at 0x0000000002637DC0>
print(list(mv))                                         # [65, 66, 67, 48, 49, 50]
print(mv.hex())                                         # 414243303132              // deveulve btes en hexa() y es de tipo = <class 'str'>
print(mv[0:4])                                          # crea Obj con acceso al byte array de los elementos 0 a 4  // out = <memory at 0x0000000002607340>
print(list(mv[0:4]))                                    # [65, 66, 67, 48]          // crea un list del binaryArray creado.   
print(bytes(mv[0:6]))                                   # b'ABC012' = sustrae 6 bytes 656667484950        // para arreglo de bytes
print(mv[0:6].hex())                                    # 414243303132              // en hexa()



