# NOTE:
# Crea una coneccion a la BD y luego crea una tbl="Tracks" en SQLite.
# con 2 campos = 'title' y 'plays'
import sqlite3

conn = sqlite3.connect('music.sqlite')                          # abro conecc con la BD y sino existe la BD la Crea
cmd = conn.cursor()

cmd.execute('DROP TABLE IF EXISTS Tracks')                        # Elimino la Tbls q existan para
cmd.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')    # volverla a crear, con los Campos : 'title' y  'plays'

conn.close()

