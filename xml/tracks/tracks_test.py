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

