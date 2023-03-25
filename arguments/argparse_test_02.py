import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

# salida:
# python argparse_test_02.py "echo hola"
# echo hola

# python argparse_test_02.py "ayayay"
# ayayay

# $ python argparse_test_03.py -h
# usage: argparse_test_03.py [-h] echo
# 
# positional arguments:
#   echo        echo the string you use here
# 
# optional arguments:
#   -h, --help  show this help message and exit