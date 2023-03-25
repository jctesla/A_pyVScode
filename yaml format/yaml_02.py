# data que va leer de fooo.yaml :
# name: John Smith
# contact:
#   home: 1012355532
#   office: 5002586256
# address:
#   street: |
#     123 Tornado Alley
#     Suite 16 - Avenue 52.           
#   city: East Centerville
#   state: TX


import yaml

with open('fooo.yaml', 'r') as file:
    datos = yaml.safe_load(file)

print(f"Contacto Oficina: {datos['contact']['office']}, Phone Casa: {datos['contact']['home']}")
print(f"Direccion: {datos['address']['street']}City:{datos['address']['city']}, {datos['address']['state']}\n")

# salida:
# Contacto Oficina: 5002586256, Phone Casa: 1012355532
# Direccion: 123 Tornado Alley
# Suite 16 - Avenue 52.           
# City:East Centerville, TX

