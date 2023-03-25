# NOTA:
# Este Ej permite leer la cuenta de una persona de twitter, e imprimir la cnts de sus amigos q lo siguen y almacenarlo en la BD.
# pueden ser varias cuentas, la idea es q lea las cuentas following de estas cnts de twitter.
import urllib.request, urllib.parse, urllib.error
import twurl                                                               # colocar tocken : https://developer.twitter.com/en/docs/twitter-api
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'               # Out : {"errors":[{"code":215,"message":"Bad Authentication data."}]}

# handle conn BD
conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

# create tbls
cur.execute(f'CREATE TABLE IF NOT EXISTS People  (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)')
cur.execute(f'CREATE TABLE IF NOT EXISTS Follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))')
# nota: 
# UNIQUE(from_id, to_id)  signif q la relacion entre los 2 ids son unicas no existe en otros.
# es una relacion de uno a uno.

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# beging 
while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT id, name FROM People WHERE retrieved=0 LIMIT 1')    # retrieved=0 indica q no hay registro d recuperacion.
        try:
            (id, acct) = cur.fetchone()             # devuelve en tupla (id,name)
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',(acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute(f'INSERT OR IGNORE INTO People (name, retrieved) VALUES ("{acct}",  {0})')
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid

    # nota: twurl contiene el token q te entrega la cnt de twitter, debes actualizarlo.
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '10'})                  # count:10 son 10 cuentas de los amigos q siguen tu cuenta twttr
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])                                   # headers['x-rate-limit-remaining']  devuelve cuantos cnts hay p leer

    try:
        js = json.loads(data)                                                               # valido si la sintaxis json no esta bien definida
    except:
        print('Unable to parse json')
        print(data)
        break

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js:                                                                   # p enteder si falla anteriormente, verifico de q cnt
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    # Si tu cnt fue recuperada correctamente :. creamos un LOOP p leer las cnts de tus amigos.    
    cur.execute(f'UPDATE People SET retrieved=1 WHERE name = {acct}')

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = {friend} LIMIT 1')
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute(f'INSERT OR IGNORE INTO People (name, retrieved)VALUES ({friend}, 0)')
            conn.commit()
            if cur.rowcount != 1:                                                               # cur.rowcount nos indica cuantos rows fueron afectados.
                print('Error inserting account:', friend)                                       # en el INSERT    
                continue
            friend_id = cur.lastrowid                                                           # grabo el ID de tu amigo
            countnew = countnew + 1
        cur.execute(f'INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES ({id}, {friend_id})')
    print('New accounts=', countnew, ' revisited=', countold)
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()
