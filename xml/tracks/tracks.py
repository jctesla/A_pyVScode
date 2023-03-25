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

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make TABLES using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);

''')


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
# find a child tag, that has a particular key.
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


#----------------------------------- MAIN() ------------------------
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
all = stuff.findall('dict/dict')                                               # apartir del 3r tag = <dict> coge todos los tags hasta </dict>
print(f'Dict count: {len(all)}')

for entry in all:
    print(f'tag = {entry.tag}')
    if ( lookup(entry, 'Track ID') is None ) :                                 # es None hasta q encuentra en la estructura el key = 'Track ID'
        continue                                                               # Si lo consigue True = abandona y pasa al sgnt item del 'for'
                                                                               # el sgnt tag es lo sigue de "Track ID"
    name =   lookup(entry, 'Name')                                             # name, Artist, Album...
    artist = lookup(entry, 'Artist')
    album =  lookup(entry, 'Album')
    count =  lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :                       # valido los resultados de c/tag, si es <> None :. es lo correcto
        continue

    print(f'name={name} / artist={artist} / album{album} / count={count} / rating={rating} / length={length}')

    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) VALUES ( ?, ?, ?, ?, ? )''', ( name, album_id, length, rating, count ) )

    conn.commit()
