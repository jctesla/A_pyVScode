# Libreria p poder leer documentos en XML
import xml.etree.ElementTree as ET

# por ejemplo tenemos este resutlado de XML de una pagina:
# declaro con triple comilla para q se pueda tratar como texto.
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl"> 993148609 </phone>
  <email hide="yes"/>
</person>'''

# usamos las porpiedades para leer los tags.
# creo un Obj para poder tratat los datos
tree = ET.fromstring(data)
print(f"Name  : {tree.find('name').text}")              # Name
print(f"Attr  : {tree.find('email').get('hide')}")      # Estado de Correo hide/show  
print(f"Phone : {tree.find('phone').text}")             # Phone
