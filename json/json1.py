# Libreria p tratar obj json
import json

# este string representa un DICTIONARY
data = '''
{
  "name" : "Chuck",
  "phone" : {
              "type" : "intl",
              "number" : "993148609"
            },
   "email" : {
              "hide" : "yes"
             }
}'''

info = json.loads(data)                                 # Creo obj JSON = {'name': 'Chuck', 'phone': {'type': 'intl', 'number': '+1 734 303 4456'}, 'email': {'hide': 'yes'}}

print(f'Name         : {info["name"]}')
print(f'E-mail Hide? : {info["email"]["hide"]}')
print(f'Phone        : {info["phone"]["number"]}')
print(f'Phone        : {info["phone"]}')                # {'type': 'intl', 'number': '993148609'}


