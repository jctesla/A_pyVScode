# NOTA:
# este ej permite leer los correos que han llegado a un buzon,y al bajar el correo en .txt
# se parecen al file =  'mbox-short.txt', y la idea es buscar las direcciones de e.mail si
# existen o no en la BD.
import sqlite3

conn = sqlite3.connect('txtIngles.sqlite')
cur = conn.cursor()                                                                        # creamos un handler de coneccion, x donde pasamos las sentencias
                                                                                           # SQL query a la BD p su ejecucion.
cur.execute('DROP TABLE IF EXISTS Counts')                                                 # lo 1r q hacemos es un Drop Table si existe.


# cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')  
cur.execute('CREATE TABLE myDiccionary (txtEnglish TEXT,txtSpanish TEXT,countFrases count INTEGER)')              # crea una tbl de 2 campos: email y count

fname = input('Enter file name: ')                                                         # si solo presiono ENTER sin ingresar nada
if (len(fname) < 1): fname = 'txtIngles.txt'                                               # va leer el file = 'mbox-short.txt'

fh = open(fname)                                                                           # Abre el file
for line in fh:                                                                            # lee c/linea del file (es decir c/CRLF es una linea)                
    if not line.startswith('• '): continue                                                 # busco dentro del file la palabra = '• '
    #print(f'line contiene = {line}\n')                                                    # line contiene = From: zqian@umich.edu
    pieces = line.split()                                                                # busca el 'space' en este word, la idea es buscar en la BD si existe este e-mail, sino existe lo INSERTA si existe lo ACTUALZA.
    email = pieces[1]                                                                      # [0] = From: y [1]=email@com.pe

    # LEE apartir de aqui es cmo trabjar con un Dictionary
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()                                                                   # devuelve el row completo con un solo campo.
    if row is None:
        # cur.execute('''INSERT INTO Counts (email, count) VALUES (?, ?)''', (email,1))    # INSERTA todo un Registro con los 2 campos: 'email' y 'count'
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))        # MODIFICA solo el campo 'count'
        print(f'UPDATE Counts SET count = {row[0] + 1} WHERE email = {email}')             # UPDATE Counts SET count=2 WHERE email = zqian@umich.edu
        
    # input()    
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"
for row in cur.execute(sqlstr):
    print(f'Correo= {str(row[0])} / veces= {row[1]}')                                       # out = Correo= cwen@iupui.edu / veces= 5

cur.close()
