# tengo una lista l = []
l = [chr(i) for i in range(ord('A'),ord('Z')+1)]
for i,itm in enumerate(l):
   print(f'{itm}', end=' ')
   if i%4 ==3:
     print()
     

# Out:
# A B C D
# E F G H
# I J K L
# M N O P
# Q R S T
# U V W X
# Y Z


