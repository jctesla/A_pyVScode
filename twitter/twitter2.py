import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment( TWITTER_URL, {'screen_name': acct, 'count': '5'} )
    print('Retrieving', url)
    
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])


#NOTA: mi cuenta sale los sngt, x q no tengo actua lizado mis datos en twitter.
# https://api.twitter.com/1.1/statuses/user_timeline.json?oauth_consumer_key=h7Lu...Ng&oauth_timestamp=1655123183&oauth_nonce=47569494&oauth_version=1.0&screen_name=jcdergan%40aol.com&count=2&oauth_token=10185562-eibxCp9n2...P4GEQQOSGI&oauth_signature_method=HMAC-SHA1&oauth_signature=ryQrvX%2BvmYehwwhs4Y9ndqs%2Bx8Y%3D
# {"errors":[{"code":89,"message":"Invalid or expired token."}]}