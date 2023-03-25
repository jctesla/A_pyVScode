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
