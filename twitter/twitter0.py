# NOTA:
# Este Ej permite leer la cuenta de una persona de twitter, e imprimir la cnts de sus amigos q lo siguen y almacenarlo en la BD.
# pueden ser varias cuentas, la idea es q lea las cuentas following de estas cnts de twitter.
import urllib.request, urllib.parse, urllib.error
import twurl                                                               # colocar tocken : https://developer.twitter.com/en/docs/twitter-api
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'               # Out : {"errors":[{"code":215,"message":"Bad Authentication data."}]}


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

acct = input('Enter a Twitter account, or quit: ')

if (len(acct) < 1):
    print(f'No Ingreso cuenta!, FIN')    
else:
    # nota: twurl llama a hidden.py q contiene el token q te entrega la cnt de twitter, debes actualizarlo.
    url = twurl.test_me()                   # si no esta actualizdo el token sale = {"errors":[{"code":89,"message":"Invalid or expired token."}]}
    
