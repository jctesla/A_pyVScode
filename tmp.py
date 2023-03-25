L = list(range(-1,5))       # [-1, 0, 1, 2, 3, 4]       (star, stop-1, step)
L = list(range(4,-2,-1))    # [4, 3, 2, 1, 0, -1]
try:
  L = list(range(4,-2,0))     # ValueError: range() arg 3 must not be zero
except:
  print("An exception occurred")
L = list(range(4,-2,1))     # [] --> empty
L = list(range(4,-2,2))     # [] --> empty
L = list(range(-1,5,2))     # [-1,0,1,2,3,4]  --> [-1, 1, 3]
L = list(range(4,0,-2))     # [4, 2]
#--------------------------------

x, y = True,False
print("1. ", (x or y)==True)         # True
print("2. ", (x and y)==False)       # True
print("3. ", (not y)==True)          # True
print("4. ", bool("Hello"))          # True
print("5. ", bool(-1))               # False
print("6. ", bool(0))                # False
print("7. ", bool(False))            # False
print("8. ", bool(None))             # False
print("9. ", bool(0))                # False
print("0. ", bool(""))               # False 
print("1. ", bool(()))               # False 
print("2. ", bool([]))               # False
print("3. ", bool({}))               # False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print("4. ", bool(myobj))


print("1.", int(True))            	# 1
print("2.", float(True))          	# 1.0
print("3.", float(False))         	# 0.0
print("4.", bool(1))              	# True
print("5.", bool(0))              	# False
print("6.", bool(0.1))            	# True
print("7.", bool(0.0))            	# False
print("8.", bool(-1))             	# True

#-------------------------
number = 0
for number in range(6):
    if number == 3:
        continue                         		  # dont continue and execute the next sentences, for.
    print('Number = ' + str(number))       		  # if number =5,el PC no llega se va arriba al sgnt for.

print('Out of loop')
#------------
h = [10, 9, 8, 7, 6, 5]
print(6 in h)
#-----------------------

n = [n  for n in range(1,50,2)]	# out: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

def steps(n,b):			# n:nro de spcs , b:nro de ‘0’.
  spc=""
  balls=""
  for s in range(n-(b//2)):
     spc = ' ' + spc
  for ss in range(b):
     balls=balls + '0'
  print(spc+balls)
  
for p in n:
  steps(len(n),p)
print("\n")

#------------------------

x = 'py'   'ho'
print(x)				                  # pyho

text = ('What is the answer?'
                   '  42! ')
print(text)			                  # What is the answer?  42!

x = 55/11
print(x)				                  # 5.0
x = 5 * 3.8 -1
print(x)				                  # 18.0

#------------------------
a='hello'
b='world'
print(a,b,sep=' Python ',end='!')  # hello Python world!
print()
print('\"hello' + " " + "world's end\"")  # "hello world's end"

#------------------------------
import cv2
print(cv2.__version__)                  # 4.5.2
print("packg <<OpenCV>>> Imported")     # 

#-------------------------------



