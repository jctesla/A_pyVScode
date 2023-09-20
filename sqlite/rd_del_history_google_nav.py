# en caso de ERROR : OperationalError: database is locked     # explain, database is locked es por que can't support a high level of concurrency
# Google x c/perfil User, en el navegador, alamcenan las navegaciones en una BD 'History' en una BD SQLite.
# juancarlos.dergan@gmail.com     esta en : C:\\Users\\miclab\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History
# mic.rqst@gmail.com              esta en : C:\\Users\\miclab\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3\\History
# truequeyquipu@gmail.com         esta en :C:\Users\miclab\AppData\Local\Google\Chrome\User Data\Profile 6
# NOTA: dentro de la BD History, hay varias tbls, una de estas es 'keyword_search_terms', q alamacena c/palabra q escribimso en el Navegador

import sqlite3
# Use the EXCLUSIVE mode to connect to the database. The EXCLUSIVE mode prevents other processes from accessing the database while you are connected to it. 
# aqui mostramos el historial de navegacion de Google
conn = sqlite3.connect('History.db', isolation_level="EXCLUSIVE")
c = conn.cursor()

result = True
id=0

while result:
   result=False
   ids=[]
   try:
      qery = c.execute("""SELECT id,url FROM urls WHERE url LIKE '%youtube%' """)  
      for idx,row in enumerate(qery):
         print (f'{idx}.- {row}')
         id=row[0]
         ids.append((id,))
         
      # Si quisieramos borrar los datos insertados descoment sgnt sentence.
      # c.executemany(' DELETE FROM urls WHERE id=?', ids)        # va a borrar de la BD la url seleccionada.
      conn.commit()
   except Exception as e:
      c.close()
      print(f'sqlite3.OperationalError: {e}')

conn.close()

# Out:
# 0.- (33309, 'http://127.0.0.1:5500/youtube.html')
# 1.- (1401, 'http://www.solociencia.com/videos/online/tecnolog-prohibida-las-per/UBhT2Nm3po4&feature=youtube_gdata/')
# 2.- (1532, 'http://www.youtube.com/channel/UC1zZE_kJ8rQHgLTVfobLi_g?sub_confirmation=1')
# 3.- (1533, 'http://www.youtube.com/channel/UC6FDIYgydXIcYBdrWF1490g?sub_confirmation=1')
# 4.- (1534, 'http://www.youtube.com/results?search_query=build+rf+telematic&sm=3')
# 5.- (1535, 'http://www.youtube.com/watch?NR=1&feature=endscreen&v=LfRNRymrv9k')
# 6.- (1536, 'http://www.youtube.com/watch?annotation_id=annotation_455440&feature=iv&src_vid=uyZBH6n2XU8&v=yUYxk-y-tU8')
# 7.- (1537, 'http://www.youtube.com/watch?feature=endscreen&v=fmAhi1N-uL8&NR=1')
# 8.- (1538, 'http://www.youtube.com/watch?feature=fvwp&v=ZUDx_FC3Dro&NR=1')
# 9.- (1539, 'http://www.youtube.com/watch?feature=player_embedded&v=ZYiia4_hJA4#!')
# 10.- (1540, 'http://www.youtube.com/watch?feature=player_embedded&v=hX-hwFtAcOw')
# 11.- (1541, 'http://www.youtube.com/watch?v=-7xOTbRL888&NR=1&feature=endscreen')
# 12.- (1542, 'http://www.youtube.com/watch?v=-I_T3XvzPaM&list=AL94UKMTqg-9C5E4KdvNkQZot3kn7GKrZn&index=3')
# 13.- (1543, 'http://www.youtube.com/watch?v=0iitoSNTmr0')
# 14.- (1544, 'http://www.youtube.com/watch?v=0lc4Fqj6v1w')
# 15.- (1545, 'http://www.youtube.com/watch?v=1ClNTvh7X5Q')