sm = None
for va in [9,41,12,3,74,15]:
   if sm is None:
      sm=va
   elif sm > va:
       sm=va

print(f'El valor Menor es: {sm}\n')
print('\n-----ASCII CODE----------\n')
letra = 'A'
try:
   print(f'{int(letra)} \n')
except ValueError as ex:
   print(f'La letra = {letra}, No puede convertir a ASCII  err:{ex} \n')
# el erro q arrojaria seria = ValueError: invalid literal for int() with base 10: 'A'



print('\n-----COMPARE WORDs----------\n')
wrd = 'h'
if wrd == 'H':
   print('Oke h = H \n')
elif wrd < 'H':
   print('Oke h < H \n')
else:
   print('Oke h > H \n')



	
