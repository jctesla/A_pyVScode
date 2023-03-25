# import xml.etree                                # si lo importo de esta forma no FUNCIONA "ET.fromstring"
from xml.etree.ElementTree import fromstring, ElementTree as ET


var_xml = '''
<alumnos>
  <users>

    <user prof="Medicina">
      <id>001</id>
      <name>Chuck</name>
    </user>

    <user prof="Ingenieria">
      <id>009</id>
      <name>Brent</name>
    </user>

    <user prof="Letras">
      <id>101</id>
      <name>JCDergan</name>
    </user>

  </users>
</alumnos>'''

# Creo mi Obj para leer los datos XML.
tree = ET(fromstring(var_xml))

root = tree.getroot()                                             # el root = 'users'
print(f'root= {root.tag}')                  

for chld1 in root:
  print(f'tag= {chld1.tag} / child= {chld1[0].tag}')
  
  for ch in list(chld1):                                          #chld2 = chld1.getchildren()   ya no se usa
    print(f'tag={ch.tag}')
    print(f'   attrib={ch.attrib}')
    print(f'   id={ch.find("id").text}')
    print(f'   name={ch.find("name").text}\n')
  
  

# out:
# root = alumnos
# tag=users /  child={}

