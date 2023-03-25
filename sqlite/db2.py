import sqlite3

conn = sqlite3.connect('music.sqlite')
cmd = conn.cursor()

# Inserto 5 registros a los campos 'title'  y  'playa'
for i in range(6,10):
     cmd.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', (f'Thunderstruck{i}', 20 + i))
     conn.commit()

# cmd.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
# cmd.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
# conn.commit()

print('Tracks:')

# Este select devuelve una Tupla (val1, val2, val3, ...)
# Luego selecciono todo los datos de los campos  'title'  y  'plays'
cmd.execute('SELECT title, plays FROM Tracks')
for row in cmd:
     #print(f'record={row[1]}')                             # Out = 26
     print(f'record={row}')                                 # Out = record=('Thunderstruck6', 26)

# si quisiera borralos: descomento el sgnt sentencia.
cmd.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cmd.close()
