age = 20
price = 19.95
first_name = "juan"
is_OnLine = False
print(f'tu edad es {age}')

name = input('What is ur name?')
print(f'Tu nombre es ' + name)

# input se ingresa como str
bd = input ('Ingrese Edad ? ')
age = 2021 -  int(bd)
print(age)

# int() .- convert to integer
# float() .- convert tp float, ej: 10.1
# bool() .-  convert to True/False  1/0  3/0
# str() .- convert to string

first = input('Num 1: ')
second = input('Num 2: ')
sum = float(first) + float(second)
print(f'La suma es = {sum}')

# String
course = 'Python for Beginnirs'
print(course)
print(f'upper() = {course.upper()}')
print(f'find() = {course.find("f")}')
print(f'using in = {"Python" in course}')       # False /  True


