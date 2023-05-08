import requests
import winsound
import yaml

# URL de la API de cambios de divisas
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# enviar una solicitud a la API y obtener la respuesta
response = requests.get(url)
if response.status_code == 200:
  print("Acceso Condedido\n")
  
  # vemos que tipo es de estructura de datos:
  content_type = response.headers.get('Content-Type')
  print("Type Fromat from Serv :" + content_type)
  if content_type == "application/yaml":
    print(" Es del tipo YAML")
  if content_type == "application/json":
    print(" Es del tipo YJON")

# leemos la dat del tipo JSON
data = response.json()
print("Valoer del Euro es=",data['rates']['EUR'])

  