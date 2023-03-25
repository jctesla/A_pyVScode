# Ej lectura de un txt a JSON
import json

# este string representa un LIST
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)                                               # de .txt a un json obj

# como es un LIST puedo ref 1ro por orden de item y luego el campo.
print(f"data[1] = {info[1]['name']} \n")

print(f'Nro de Users: {len(info)}')
for item in info:
    print("-------------------")
    print(f"Name : {item['name']} ")
    print(f"Id : {item['id']} ")
    print(f"Attribute : {item['x']}")
