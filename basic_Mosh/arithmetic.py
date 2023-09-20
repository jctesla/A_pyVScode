print(10/3)             # 3.333333
print(10//3)            # 3
print( 4**2)            # exponencial

# Operator Comparator
x = 3 == 2
print (x)               # False

# Logical Operator
price = 25
print(price > 10 and price < 30)    # True

temp = 32
if temp > 30:
    print("Tempo Normal")
elif temp > 20:
    print('>Temp bajando')
elif temp > 10:
    print('Temp it a bit cold')

# ejemplo de peso
w = input('Peso ? ')
unit = input('(k)ilogramos or (L)ibras ? ')

if unit.upper() =='k':
    converted = float(int(w)) / 0.45
    print(f'Su peso en Kg = {converted}')
else:
    converted = float(int(w)) * 0.45
    print(f'Su Peso en Libras = {converted}')

















