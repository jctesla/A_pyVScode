import random
# If else
age = 22
if age > 16:
    print("You are enough to have licence to drive car")
else:
    print("You have to wait until 16 years")


if age >= 21:
    print("You are so young to begin as a professional driver")
elif age >= 16:
    print("Prepare your talent to get your licence driver car")
else:
    print("You have less than 16 years")



if ((age >= 1) and (age <= 18)):
    print("Your have good memory for math")
elif (age == 21) or (age >= 65):
    print("Aproach to get your licence driver")
elif not (age == 30):
    print("You have 30 years and this fenimenal to our casting")
else:
    print("You have Condition not aceptable")


# Loops For, note: range(idxBegin=0,idxBegin=1)
for x in range(2,10):
    print(x," ", end="")        # 2  3  4  5  6  7  8  9

print('\n')                     # tab.
frutas = ['Manzana', 'Platano', 'Toronja', 'Grandilla', 'fresa']
for y in frutas:
    print(y)

for x in [2,4,6,8,10]:
    print(x)                                # 2,4,6,8,10

# Recorrdio de Arreglo Bi-Dimensional nota : range(idxBegin=0,idxBegin=1)
print("print a bi-array:")
newNum = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(newNum[x][y])                 # 1,2,3, 10,20,30, 100,200,300


# Using random
num = random.randrange(0,100)
while(num !=15):
    print(num)
    num= random.randrange(0,100)


# Using "While" with "break".
i=0
while (i <=20):
    if (i==9):
        break
    else:
        print(i)
        i +=1


# Using While to detect odd number.
# video = 25minS
i=0
while (i <= 200):
    if (i==0):
        print("Numero ZERO : ", i)
    else:
        if (i%2 == 0):
            print("Numero Par : " ,i)
        else:
            print("Numero InPar : ", i)

    i += 1                              # i = i + 1
    continue


