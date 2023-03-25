#import xml.etree.ElementTree as ET
#import xml.etree.ElementTree as fromstring
from xml.etree.ElementTree import fromstring, ElementTree as ET

var_xml = '''
<alumnos>
  <users>

    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>

    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>

    <user x="10">
      <id>101</id>
      <name>JCDergan</name>
    </user>

  </users>
</alumnos>'''

# Creo mi Obj para leer los datos XML.
tree = ET(fromstring(var_xml))                                    # mejor que ET.fromstring
lst = tree.findall('users/user')                                  # retrieve all subelements tags en un Dictionary.
print(f'tipo= {type(lst)} / root={tree.getroot()}')               # tipo = <class 'list'>

# forma recorrido: todo los usarios de la lista del tag users:
print(f'\nPerfiles User hay : {len(lst)}')                        # se crea un tipo List y este contiene 3 elementos.
for i in lst:
    print('---------------------')
    print(f'typeOf i = {type(i)}')                                # typeOf i = <class 'xml.etree.ElementTree.Element'>
    print(f'Name   : {i.find("name").text}')                      # Name   : Chuck
    print(f'Id     : {i.find("id").text}')                        # Id     : 001
    print(f'Attrib : {i.get("x")}')                               # Attrib : 2
