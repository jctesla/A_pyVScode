import xml.etree.ElementTree as ET                                # si lo importo de esta forma no FUNCIONA "ET.fromstring"
# from xml.etree.ElementTree import fromstring, ElementTree as ET, parse,tag

# Creo mi Obj XML from file.xml
tree = ET.parse('country_data.xml')
root = tree.getroot()                                             # el root = 'users'

print(f'root = {root.tag}')                                       
for child in root:
  print(f'tag={child.tag} /  child={child.attrib}')


# out:
# tag=country /  child={'name': 'peru'}
# tag=country /  child={'name': 'Singapore'}
# tag=country /  child={'name': 'Panama'}

ele = ET.Element("Animal", Especie="Mono")
ele_str = ET.tostring(ele, encoding="utf8", method='xml')
print(ele_str)

# <?xml version='1.0' encoding='utf8'?>
# <Animal Especie="Mono"/>
