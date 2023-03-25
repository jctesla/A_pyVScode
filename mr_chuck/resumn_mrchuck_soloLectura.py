0 == 0.00			                  # False
0.1 == True		                  # False
1 == True			                  # True
0%6 			                      # Modulo Operator Residuo de Div rspt = 0
5%6			                        # resid de una Div rpts = 5,  nota: recomiendo verify si el dividendo es < divisor :. procede
10%6			                      # rspt = 4
----------------------------
# lee hasta encontrar un salto de linea o '\n'
f = open ('readeMe.txt')	
lin = f.read()		
print(len(lin))		              # nro caracteres de esta linea
94658

print( lin[:20] )		            # lee los 1ros 20 caracteres de esta linea.

-----------------------------
file = open('reame.txt')
for c in file:
   print( c )		                # imprime toda las lineas del file

------------------------------
file = open('reame.txt')
for c in file:		              # recorre hasta encontrar una palabra.'from'
   if c.startswith('from'):
      print( c)

letAZ = [chr(l)  for l in range(ord('A'),ord('F'))]
-----------------------------
for i in "hola":
   print( i )			              # imprime h, o , l, a
   
strBin = bin(byte).replace('0b','')
print(strBin)

for n,bit in enumerate(strBin):
    if bit=='1':
        print(f'Bit Nº{n}=1')

----------------------------
a = "Dergan"
b = list(a)			                # b = ['D', 'e', 'r', 'g', 'a', 'n']

----------------------------
# para determinar un space en un print = '\s'
sorted( lista, reverse=True)	              # permite de un tipo de collecion 'list' ordernar de forma descendente los elementos.

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5 }	# creo un Collection del tipo  Dicitionary
for key,val in dic.items():		              # leo c/elemento del "Dictionary"  <key, val>
   print(f'{key} - {val} ')	

# crear un Collection dictionarie vacio
# agrego nuevos elementos.
d = dict()
d['a'] = 10
d['b'] = 20

if 'a' in d:
    print( f'Key = a / Val = {d.get("a")} ')	# result:  Key = a / Val = 10

# sino existe el elemento 'x' en el dict :.
print( f'Key = x / Val = {d.get("x",100)} ')	# if key not exist :. arroja = 100 for default  :. 

# Sustraigo tipos de caract de un String
import re
s = "My 2 favorite numbers are 13 and 37"

nros = re.findall('[0-9]+', s)                # el simbolo '+' indica q al encontrar un digito tipo nro q puede ser 0 o hasta 9 '[0-9]' lo debe juntar
> ['2', '13', '37']                           # toma todo los nros con/sin caracteres a su lado. 

nros = re.findall( '[0-9]+ ', s)		          # busca en 's' todo los nros, pero q al encontralo tengan un space a su derecha, sino no lo toma, com el nro 37.
> ['2 ', '13 ']                               # 37 no tiene un espacio a la derecho, no lo toma

nros = re.findall( '[0-9]+\\s', s )		        # otra forma de decirle space es con el simbolo '\\s' = espacio
> ['2 ', '13 ']

nros = re.findall( '[0-9]', s)                # busca y toma solo los caracteres q son nros en el rango de 0 a 9.
> ['2', '1', '3', '3', '7']

nros = re.findall( '[0-3]', s)               # no toma el 7 fuera de rango
> ['2', '1', '3', '3']

nros = re.findall( '[0-9]*', s)              # busca digitos numerico en el rango de 0 a 9, y tambien los q son None, es decir todo. len(s)=35 / len(nros)=34
> ['', '', '', '2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '13', '', '', '', '', '', '37', '']


#---------OPCIONES-------No1 --------------------
# sustraigo los HOST de c/email
s = "From jcdergan@aol.com to juancarlos.dergan@gmail.com to jcdergan@miclabperu.com are my emails"
p1 = s.find('@')
p2 = s.find('@',p1+1)
p3 = s.find('@',p2+1)

print(f"host1 = {s[ p1+1 : s.find(' ',p1) ]}")
> host1 = aol.com

print(f"host1 = {s[ p2+1 : s.find(' ',p2) ]}")
> host1 = gmail.com

print(f"host1 = {s[p3+1:s.find(' ',p3)]}")
> host1 = miclabperu.com

#---------OPCIONES-------No2 --------------------
# Otra forma cn split
s = "From jcdergan@aol.com to juancarlos.dergan@gmail.com to jcdergan@miclabperu.com are my emails"
sp1 = s.split('@')
> ['From jcdergan', 'aol.com to juancarlos.dergan', 'gmail.com to jcdergan', 'miclabperu.com are my emails']

print(sp1[1][0 : sp1[1].find(' ')])                     # similar a d = sp1[1] :.  d[:] =>
> aol.com


#---------OPCIONES-------No3 --------------------
# Otra forma llamda REGEX Version
import re
s = "From jcdergan@aol.com to juancarlos.dergan@gmail.com to jcdergan@miclabperu.com are my emails"

p = re.findall( '@([^ ]*)', s)                          # interpreta 01 --> busca el '@', luego de encontralo desde el 1er caracter sgnt '^', junta todo los caract '[]*', pero q no tengan ' ', espacio dentro
> ['aol.com', 'gmail.com', 'miclabperu.com']            # interpreta 02 --> busca el '@', luego de encontralo toma la sgnt formula '()',
                                                        # '()' = desde el sgnt digito despues del '@' , el 1er caracter '^', juntalos []*', pero q no contengan espacio.
p = re.findall(r'j[a-z.@]*', s)
> ['jcdergan@aol.com', 'juancarlos.dergan@gmail.com', 'jcdergan@miclabperu.com']

s = "From jcdergan@aol.com to juancarlos.dergan@gmail.com to jcdergan_73@miclabperu.com o tambien jcdergan3@miclabperu.com are my emails"
re.findall(r'j[a-z._0-9@]*', s)
['jcdergan@aol.com', 'juancarlos.dergan@gmail.com', 'jcdergan_73@miclabperu.com', 'jcdergan3@miclabperu.com']

#---------MAS EJECICIOS------------------------
x = 'We just received $10.00 for cookies.'
r = re.findall('\$.*[0-9].[0-9]+',x)
> ['$10.00']

r = re.findall('\$[0-9.]+',x)
> ['$10.00']

re.split(r'\W+', 'Words- words- words.')                    # solo lee todolo q sea una palabra sin caracteres extraños es decir : - , ', . $ % etc
re.split(r'\W+', 'Words, words, words.')
re.split(r'\W+', 'Words words words.')
re.split(r'\W+', 'Words#words?words.')
> ['Words', 'words', 'words', '']                           # cualquiera de las anteriores va arrojar lo mismo.

re.split(r'(\W+)', 'Words, words, words.')                  # va tomar encuenta todo los simbolos pero los separa de las palabras puras sin espacio simboos etc.
['Words', ', ', 'words', ', ', 'words', '.', '']

re.split('[a-f]+', '0a32B9xmb13fk34', flags=re.IGNORECASE)  # ignora los caracte del rango de en low a-f y up A-F.
['0', '32', '9xm', '13', 'k34']




#resumen:
^From .*@([^ ]*)
#descripcion:
^ = starting at begining of the line
From= look for this string 'from'
 = space
. *= dot star, any number of characters
@= seguido de un arroba
([^ ]*)= now we are going to extracting the non-blank character.


#-----------------------SOCKETs------------------------------
# A simple web browser.
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

# Which type of encoding do most websites use? rspta : UTF-8
print(ord('A'))
> 65
print(ord('\n'))
> 10

#------>>> import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
   print(line.decode().strip())
>
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief


#--------------------------------------------------------------
#'Web Scraping'
# Es una técnica utilizada p extraer información de sitios web.
# Usualmente, estos simulan la navegación de un humano en la Web p
# evaluar informacion q necesitemos p un proposito.
# when a program or script, pretends to be a browser, and can retrieves web pages
# to extract information for one propouse and do he same for other pages, and so forth

# Spidering the Web or Crawling the Web : Un rastreador web, indexador web
# Programa q inspecciona las páginas Web de forma metódica y automatizada. 
# Uno de los usos más frecuentes que se les da consiste en crear una copia de todas las páginas web visitada.
#--------------------------------------------------------------
# Creacion de un obj, self es una propiedad de las clases de python 
# para crear una representacion propia de si mismo, una instancia del obj
# q se esta creando.
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

# creo una instancia
an = PartyAnimal()
an.party()
an.party()

print()

# creo una instancia nueva self.x se recrea nuevamente
ann = PartyAnimal()
ann.party()
ann.party()

#--------------------------------------------------------------
# el Concpeto de Contructor, se genera cuando se crea el Obj 
# inicializa las variables y estados del obj.
# el Destructor en su lugar, se usa muy rara vez
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

#--------------------------------------------------------------
# inherentance es cuando la clase puede extenderse, por herencia.
# cuando creamos una nueva clase, podemos reutilizar las capacidades
# de la clase padre actual, heredando todas sus propiedades y agregar
# unas propias para crear una diferencia. (Write Ones reuse many times)
# la nueva clase tiene las capacidades de la clase padre mas otras mas.
# esto se llama extender las clase o subclase

class FooballFan(PartyAnimal):
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(f'{self.name} points = {self.points}')

#--------------------------------------------------------------
# Herenciaa:
# creacion de un obj, self es una propiedad de las clases de python 
# para crear una representacion propia de si mismo, del obj.
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self,name):
        self.name = name
        print(f'name: {self.name} constructed')

    def party(self):
        self.x = self.x + 2
        print(f'{self.name} party / count: {self.x}')


# clase que se exteinde de la clase PartyAnimal()
class FootballFan(PartyAnimal):
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(f'{self.name} points = {self.points}')

   def __del__(self):
       print(f'Clase {self.name} Detructed')   
      
s = PartyAnimal("Sally")
s.party()
s.party()

print()

j = FootballFan("Jim")
j.party()
j.touchdown()

#------------
# OutPut:
#
#// Clase Padre
# name: Sally constructed
# Sally party / count: 2
# Sally party / count: 4
#
#// Clase Hijo/ inherith :
# name: Jim constructed
# Jim party / count: 2
# Jim party / count: 4
# Jim points = 7
# Clase Jim Detructed

#--------------------------------------------------------------
#           BD
CREATE TABLE t (
    id          INTEGER PRIMARY KEY,
    name        VARCHAR UNIQUE,                           # la Clave es UNIQUE
    other       INT
);

sqlite> INSERT OR IGNORE INTO t (name) VALUES ('a');
sqlite> INSERT OR IGNORE INTO t (name) VALUES ('a');
sqlite> INSERT OR IGNORE INTO t (name) VALUES ('a');
sqlite> select * from t ;
1|a|


#--------------------------------------------------------------
#           DB eje:01
# NOTE:
# Crea una coneccion a la BD y luego crea una tbl="Tracks" en SQLite con 2 campos = 'title' y 'plays'
# las extensiones pueden ser: .sqlite o .sql
import sqlite3

conn = sqlite3.connect('music.sqlite')                          # abro conecc con la BD y sino existe la BD la Crea
cmd = conn.cursor()

cmd.execute('DROP TABLE IF EXISTS Tracks')                        # Elimino la Tbls q existan para
cmd.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')    # volverla a crear, con los Campos : 'title' y  'plays'

conn.close()


#--------------------------------------------------------------
#           DB eje:02
# NOTE:
# Creo 5 records en la BD creada anteriormente, en los campos 'title'  y  'plays'
import sqlite3

conn = sqlite3.connect('music.sqlite')
cmd = conn.cursor()

# Inserto 5 registros a los campos 'title'  y  'playa'
for i in range(5):
     cmd.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', (f'Thunderstruck{i}', 20 + i))
     conn.commit()

print('Tracks:')

#Luego selecciono todo los datos de los campos  'title'  y  'plays'
cmd.execute('SELECT title, plays FROM Tracks')
for row in cmd:
     print(row)

# si quisiera borralos: descomento el sgnt sentencia.
# cmd.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

cmd.close()

#--------------------------------------------------------------
#        CONVERT .TXT to BD : emaildb.py
# NOTA:
# este ej permite leer los correos que han llegado a un buzon, al bajar el correo en .txt
# se parecen al file =  'mbox-short.txt', y la idea es buscar las direcciones de e.mail si
# existen o no en la BD.
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()                                                                        # creamos un handler de coneccion, x donde pasamos las sentencias
                                                                                           # SQL query a la BD p su ejecucion.
cur.execute('DROP TABLE IF EXISTS Counts')                                                 # lo 1r q hacemos es un Drop Table si existe.


# cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')  
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')                             # crea una tbl de 2 campos: email y count

fname = input('Enter file name: ')                                                         # si solo presiono ENTER sin ingresar nada
if (len(fname) < 1): fname = 'mbox-short.txt'                                              # va leer el file = 'mbox-short.txt'

fh = open(fname)                                                                           # Abre el file
for line in fh:                                                                            # lee c/linea del file (es decir c/CRLF es una linea)                
    if not line.startswith('From: '): continue                                             # busco dentro del file la palabra = 'From: '
    print(f'line contiene = {line}\n')                                                     # line contiene = From: zqian@umich.edu
    pieces = line.split()                                                                  # busca el 'space' en este word, la idea es buscar en la BD si existe este e-mail, sino existe lo INSERTA si existe lo ACTUALZA.
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

#--------------------------------------------------------------
#                       .JSON

#----------------------------------------
# Ej json1.py
import json

# este string representa un DICTIONARY
data = '''
{
  "name" : "Chuck",
  "phone" : {
              "type"  : "intl",
              "number": "993148609"
            },
   "email" : {
              "hide" : "yes"
             }
}'''

info = json.loads(data)                                 # Creo obj JSON = {'name': 'Chuck', 'phone': {'type': 'intl', 'number': '+1 734 303 4456'}, 'email': {'hide': 'yes'}}
print(f'Name         : {info["name"]}')
print(f'E-mail Hide? : {info["email"]["hide"]}')
print(f'Phone        : {info["phone"]["number"]}')
print(f'Phone        : {info["phone"]}')

# Out:
# Name         : Chuck
# E-mail Hide? : yes
# Phone        : 993148609
# Phone        : {'type': 'intl', 'number': 993148609'}


#----------------------------------------
# Ej json2.py
import json

# este string representa un LIST
data = '''
[
  { "id"   : "001",
    "x"    : "2",
    "name" : "Chuck"
  },
  { "id"   : "009",
    "x"    : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)                                               # creo el Obj json

# como es un LIST puedo ref 1ro por orden de item y luego el campo.
print(f"infor[1]['name'] = {info[1]['name']} \n")

print(f'Nro de Users: {len(info)}')
for item in info:
    print("-------------------")
    print(f"Name : {item['name']} ")
    print(f"Id : {item['id']} ")
    print(f"Attribute : {item['x']}")

# Out:
# data[1] = Brent
#
# Nro de Users: 2
# -------------------
# Name : Chuck
# Id : 001
# Attribute : 2
# -------------------
# Name : Brent
# Id : 009
# Attribute : 7

#----------------------------------------
#         CONVERT .json to BD : roster.py
# Este ej nos permite evaluar como desde un .json podemos alamcenarl en la BD
# evaluar si tiene un name repetido en el campo de repeat y crear selects, insert etc.

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
# Corre una serie de querys
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    repeat INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# Formato de los Datos: [ [user,courseID,role], [], ... ]
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],
#   . . .

str_data = open(fname).read()
json_data = json.loads(str_data)                                                            # froma un Obj de Arrays

for entry in json_data:

    name = entry[0]                                                                         # si evaluas el file.json es un LIST
    title = entry[1]

    print(f'name = {name} / title = {title}')
    cur.execute(f'SELECT id FROM User WHERE name = "{name}" ')                              # leo el id q se auto generó x q al crear la tbl indicamos = AUTOINCREMENT
    row = cur.fetchone()                                                                    # leo el valor id
    if row is None:
        cur.execute(f'INSERT OR IGNORE INTO User (name) VALUES ("{name}")' )                # Si inserto 2 veces repetidas el NAME, se genera un IGNORE,asi valida solo UN Name
        cur.execute(f'SELECT id FROM User WHERE name = "{name}" ')                          # leo el id q se auto generó x q al crear la tbl indicamos = AUTOINCREMENT
        user_id = cur.fetchone()[0]
    else:
        cur.execute(f'UPDATE User SET repeat = repeat + 1 WHERE name = "{name}" ')     

    cur.execute(f'INSERT OR IGNORE INTO Course (title) VALUES ("{title}") ')
    cur.execute(f'SELECT id FROM Course WHERE title = "{title}" ')
    course_id = cur.fetchone()[0]

    # Ya teniendo el user_id y  course_id, puedo completat la sgnt tbl
    cur.execute(f'INSERT OR REPLACE INTO Member (user_id, course_id) VALUES ( {user_id}, {course_id} )')
    conn.commit()


#--------------------------------------------------------------
#                   XML    

#-------------------------------
# Ej: xml1.py
# Libreria p poder leer documentos en XML
import xml.etree.ElementTree as ET

# por ejemplo tenemos este resutlado de XML de una pagina:
# declaro con triple comilla para q se pueda tratar como texto.
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl"> 993148609 </phone>
  <email hide="yes"/>
</person>'''

# usamos las porpiedades para leer los tags.
# creo un Obj para poder tratat los datos
tree = ET.fromstring(data)
print(f"Name  : {tree.find('name').text}")              # Name
print(f"Attr  : {tree.find('email').get('hide')}")      # Estado de Correo hide/show  
print(f"Phone : {tree.find('phone').text}")             # Phone

# out:
# Name  : Chuck
# Attr : yes
# Phone :  993148609


#-------------------------------
# Ej: xml2.py
from xml.etree.ElementTree import fromstring, ElementTree as ET

var_xml = '''
<alumnos>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
    <user x="10">
      <id>101</id>
      <name>JCDergan</name>
    </user>
  </users>
</alumnos>'''

# Creo mi Obj para leer los datos XML.
tree = ET(fromstring(var_xml))                                    # mejor que ET.fromstring
lst = tree.findall('users/user')                                  # lst es un List de elementos = Dictionary
print(f'tipo= {type(lst)} / root={tree.getroot()}')               # tipo = <class 'list'>

# forma recorrido: todo los usarios de la lista del tag users:
print(f'\nPerfiles User hay : {len(lst)}')                          # se crea un tipo List y este contiene 3 elementos.
for i in lst:
    print('---------------------')
    print(f'typeOf i = {type(i)}')                                # typeOf i = <class 'xml.etree.ElementTree.Element'>
    print(f'Name   : {i.find("name").text}')                      # Name   : Chuck
    print(f'Id     : {i.find("id").text}')                        # Id     : 001
    print(f'Attrib : {i.get("x")}')                               # Attrib : 2

# Out :
# tipo= <class 'list'> / root=<Element 'alumnos' at 0x0000000002627DB0>
#
# Perfiles User hay : 3
# ---------------------
# typeOf i = <class 'xml.etree.ElementTree.Element'>
# Name   : Chuck
# Id     : 001
# Attrib : 2
# ---------------------
# typeOf i = <class 'xml.etree.ElementTree.Element'>
# Name   : Brent
# Id     : 009
# Attrib : 7
# ---------------------
# typeOf i = <class 'xml.etree.ElementTree.Element'>
# Name   : JCDergan
# Id     : 101
# Attrib : 10


#-------------------------------
# Ej: xml3.py
# Permite leer un arbol de elementos: 
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
  
# root= alumnos
# tag= users / child= user
# tag=user
#   attrib={'prof': 'Medicina'}
#   id=001
#   name=Chuck
#
# tag=user
#   attrib={'prof': 'Ingenieria'}
#   id=009
#   name=Brent
#
# tag=user
#   attrib={'prof': 'Letras'}
#   id=101
#   name=JCDergan

#-----------------------------------
# Ej: tracks_test.py  / probar: modo debbuger.
# NOTA : 
# Con este Ej podemos practicar mas sobre la lectura de files .XML a una BD
# este ej permite ver como leer un file .XML e insertarlo en la BD
#
# To export your own Library.xml from iTunes 
# File -> tracks_Library.xml -> Export Library
# Make sure it is in the correct folder.   Of course iTUnes might change
# UI and/or export format any time - so good luck :)

import xml.etree.ElementTree as ET
import sqlite3
import os

#----- MAIN() --------------
# INPUT FIlE .XML
# en linux import os os.name 'posix' #en win7/win10 import os os.name

# S.O = nt / path=D:\phytonSpace\freeCodeCamp\python\myLessons
print(f'S.O = {os.name} / path={os.getcwd()}')
path = None
if os.name =='nt':
    path = os.getcwd() + '\\xml\\tracks\\'                                     # D:\phytonSpace\freeCodeCamp\python\myLessons\xml\tracks
    print(f'Win path = {path}') 

# Ingreso de FileName.XML
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : 
    fname = path + 'tracks_Library.xml'
    print(f"path File = {fname}  /  Exist File = {os.path.isfile(fname)} ")

# Begin Create XML Obj
stuff = ET.parse(fname)                                                        # input a string file .xml
all = stuff.findall('dict/dict/dict')                                          # apartir del 3r tag = <dict> coge todos los tags hasta </dict>
print(f'Dict count: {len(all)}')

# recorremos todo los Key : Val => Key : 
for childA in all:
    print(f'key = {childA.tag} / lbl={childA.text} ')

    for childB in childA:
        if childB.tag == 'key':
            print(f'key = {childB.tag} / text={childB.text} ')
        else:
            print(f'val = {childB.tag} / text={childB.text} ')    

# Out:
S.O = nt / path=D:\phytonSpace\freeCodeCamp\python\myLessons
Win path = D:\phytonSpace\freeCodeCamp\python\myLessons\xml\tracks\
Enter file name:
path File = D:\phytonSpace\freeCodeCamp\python\myLessons\xml\tracks\tracks_Library.xml  /  Exist File = True
Dict count: 404
key = dict / lbl=

key = key / text=Track ID
val = integer / text=369
key = key / text=Name
val = string / text=Another One Bites The Dust
key = key / text=Artist
val = string / text=Queen
key = key / text=Composer
val = string / text=John Deacon
key = key / text=Album
val = string / text=Greatest Hits
key = key / text=Genre

