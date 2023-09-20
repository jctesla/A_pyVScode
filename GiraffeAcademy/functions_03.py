# using functions
def cube(num):
    return num * num * num


print("El Cubico de 3 = " + str(cube(3)))

# using if/else
is_male = True
is_tall = True

if is_male or is_tall:
    print("Your are Male")
else:
    print("Your are not a Male")

if is_male or is_tall:
    print("Your are Male")
elif is_male and not(is_tall):
    print("Your are Male and Short")
else:
    print("Your are not a Male")

