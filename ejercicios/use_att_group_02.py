'''
En Python, \d+ es una expresión regular que se utiliza para buscar y hacer coincidir secuencias de dígitos en una cadena de texto. Aquí está el significado desglosado de los componentes de esta expresión regular:
\d: Esto es una abreviatura que representa cualquier dígito decimal (0-9). En una expresión regular, \d coincide con un solo dígito.
+: Este es un cuantificador que sigue a \d. El + significa "una o más veces". Por lo tanto, \d+ significa que se buscará una secuencia de uno o más dígitos en la cadena de texto (si estan seguidos sin espacios ni nada).
Juntos, \d+ busca una serie continua de dígitos en una cadena. Aquí tienes algunos ejemplos de cómo se utilizaría esta expresión regular en Python:

En este ejemplo, la expresión regular \d+ encuentra la secuencia de dígitos "12345" en la cadena de texto.
'''

import re

# Buscar una coincidencia en una cadena que contiene dígitos
texto = "Mi número de telé area(+51) es: 993148609."
coincidencia = re.search(r'\d+', texto)
print(type( coincidencia.span))                             # class            
print(coincidencia.span())                                  # (24, 26) devuelce en que rango se encuentra el match del dig en ese caso.
(posIni,posEnd) =coincidencia.span()
print(f'ini={posIni}, end={posEnd}')                        # ini=24, end=26

if coincidencia:
    print("Número encontrado:", coincidencia.group())
else:
    print("No se encontraron números.")

# Resultado: Número encontrado: 51
