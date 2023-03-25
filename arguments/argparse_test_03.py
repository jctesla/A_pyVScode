import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-sqrt" , "--square", help="No da el Cuadrado de un Nro q le asignemos.")
args = parser.parse_args()
print(f" El Cuadrado de {args.square} = {int(args.square)**2}")

# Salida:
# $ python argparse_test_03.py -sqrt 5
# El Cuadrado de 5 = 25
