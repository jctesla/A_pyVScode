# Validate YAML - Online YAML Tools:
# https://onlineyamltools.com/validate-yaml
# format : https://docs.fileformat.com/programming/yaml/

import yaml

if __name__ == '__main__':

    stream = open("fooMio.yaml", 'r')
    #with open("data.yaml", 'r') as stream:
    #    data_loaded = yaml.safe_load(stream)
    
    data_loaded = yaml.safe_load(stream)
    print(data_loaded)
    #for key, value in data_loaded.items():
    #    print (key + " : " + str(value))
    
# Salida:
# {'mumero': 16, 'letras': 'Hola Mundo', 'texto': 'Hola Mundo', 'texto2': 'Hola y espero que calnces tus Objetivos', 
# 'lista1': ['Python', 'NodeJs', 'Andorid'], 
# 'lista2': ['Python', 'Nodejs', 'Androids'], 
#  'lista3': [['Python', 'NodeJs', 'Android'], ['gatos', 'monos', 'perros']], 
# 'objeto01': {'numero': 10, 'text': 'hola objeto', 'objeto02': [12, 13, -13]}}