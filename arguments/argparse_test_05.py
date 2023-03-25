# import the necessary packages
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of the user")
args = vars(ap.parse_args())

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))
print(f"Hola {args['name']}, Buenos Dias!")

# Salida:
# $ python argparse_test_04.py -n "Juan carlos"
# Hi there Juan carlos, it's nice to meet you!
# Hola Juan carlos, Buenos Dias!
# 
# $ python argparse_test_04.py --name "Juan carlos"
# Hi there Juan carlos, it's nice to meet you!
# Hola Juan carlos, Buenos Dias!

# sino coloco argumento:
# $ python argparse_test_04.py
# usage: argparse_test_04.py [-h] -n NAME                                           # me indica q es obligatio usar '-n' ó '--name', el [-h] es opcional
# argparse_test_02.py: error: the following arguments are required: -n/--name       # aqi me lo indica claramente.

# si en ap.add_argument() el parametro sería  'required=False'                      # no medaria error
# $ python argparse_test_04.py
# Hi there None, it's nice to meet you!                                             # sale 'None'
# Hola None, Buenos Dias!
