'''
En Python, \d+ es una expresión regular que se utiliza para buscar y hacer coincidir secuencias de dígitos en una cadena de texto.
\d: Esto es una abreviatura que representa cualquier dígito decimal (0-9). En una expresión regular, \d coincide con un solo dígito.
+: Este es un cuantificador que sigue a \d. El + significa "una o más veces". Por lo tanto, \d+ significa que se buscará una secuencia de uno o más dígitos en la cadena de texto.
Juntos, \d+ busca una serie continua de dígitos en una cadena.
'''

import re

pattern = r'\d+'                      # Match one or more digits, dígito decimal (0-9)
text = 'Hello, 8wor5ld!'

match = re.search(pattern, text)

# Check if there was a match
if match:
    print(match.group())              # This will print the first matched text, of pattern digit 8
else:
    print('No match found')
