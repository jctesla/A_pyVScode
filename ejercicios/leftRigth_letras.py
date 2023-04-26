# f={chr(u):u  for u in range(65,75)}
# print(f)

# Este ej vamos a colocar las letras del nombre una/c del lado izq y del lado derech
# NOTA: 
# Caracter Special = u"\u2593" = ▓
# tipo de chr = https://www.fileformat.info/info/charset/UTF-8/list.htm?start=8192
import time
mi = '\u2593' * 20                                         # sepcial Character    
# mi = "##################"                                # my name, string()
# mi = "Hola Juan Carlos"                                  # my name, string()
mi= mi.upper()
r_mi =[' '  for s in mi]                                   # create arrey at the same size of my name = [' ',' ', . . . ' ']
print(f'{r_mi}\n\n')


i = 0                                                      # index to read char from mi
flg = True
while(flg):
   r_mi[i] = mi[i]
   r_mi[len(mi)-1-i] = mi[len(mi)-1-i]
   print(f'r_mi={r_mi} i={i}', end ='\r')
   time.sleep(0.7)
   i+=1
   if (r_mi[i] != ' '):
      flg=False  

'''
['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
r_mi=['J', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'S'] i=0
r_mi=['J', 'U', '-', '-', '-', '-', '-', '-', '-', 'O', 'S'] i=1
r_mi=['J', 'U', 'A', '-', '-', '-', '-', '-', 'L', 'O', 'S'] i=2
r_mi=['J', 'U', 'A', 'N', '-', '-', '-', 'R', 'L', 'O', 'S'] i=3
r_mi=['J', 'U', 'A', 'N', ' ', '-', 'A', 'R', 'L', 'O', 'S'] i=4
r_mi=['J', 'U', 'A', 'N', ' ', 'C', 'A', 'R', 'L', 'O', 'S'] i=5
'''

# r_mi=['▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓', '▓']

h = "Hola\n"
print(h.rstrip('\n'))               # quita el \n de la derecha y solo deja = 'Hola'