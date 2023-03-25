# 'History' es una BD de sqlLite donde se almacena todas las activididades del navegador y se ref por la cuenta de c/uno.
# Google x c/perfil crea un 'History' ej:
# juancarlos.dergan@gmail.com     C:\\Users\\miclab\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History
# mic.rqst@gmail.com              C:\\Users\\miclab\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3\\History
# truequeyquipu@gmail.com         C:\Users\miclab\AppData\Local\Google\Chrome\User Data\Profile 6

# dentro de la BD History, hay varias tbls, una de estas es 'keyword_search_terms', q alamacena c/palabra q escribimso en el Navegador
import sqlite3
import re

# find your 'History' file created by google browser
conn = sqlite3.connect('C:\\Users\\miclab\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3\\History')
c = conn.cursor()

result = True
id=0

while result:
   result=False
   ids=[]
   qery = c.execute("""SELECT id,url FROM urls WHERE url LIKE '%Traductor%' """)
   for idx,row in enumerate(qery):
      print (f'{idx}.- {row}')
      id=row[0]
      ids.append((id,))
   c.executemany(' DELETE FROM urls WHERE id=?', ids)        # va a borrar de la BD la url seleccionada.
   conn.commit()

conn.close()