# tambien funciona:
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--value", required=True, help="name of the user")
arg = vars(ap.parse_args())
print(f" El Cuadrado de {arg['value']} = {int(arg['value'])**2}")

# Salida:
# $ python argparse_test_03.py -v 5
# El Cuadrado de 5 = 25