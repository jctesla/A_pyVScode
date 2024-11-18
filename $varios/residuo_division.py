# como obtener partes de una division de 2 numeros enteros:
dividendo = int(input("Ingrese un dividendo:"))
divisor = int(input("Ingrese divisor:"))

cociente = int(dividendo / divisor)
residuo = dividendo % divisor

print(f"Dividendo = {dividendo}")
print(f"Divisor = {divisor}")
print(f"Cociente = {cociente}")
print(f"Residuo = {residuo}")
