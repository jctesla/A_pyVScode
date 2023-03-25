import requests
 
# Another name space
var = "a class variable."
 
def __init__(self, url):
    self.__response = requests.get(url)
    self.code = self.__response.status_code
 
def server_info(self):
    for key, val in self.__response.headers.items():
        print(key, val)
 
def __del__(self):
    self.__response.close()
    print("[!] closing connection done...")


# Injecting meta from another namespace
# es una forma de asignar un tipo de variable.
Response = type('Response', (), {"classVar":var, "__init__": __init__, "server":server_info, "__del__":__del__})  

# connect to my router
resp = Response("http://192.168.1.1")                 
print(type(Response))                                 # <class 'type'>
print(resp.code)                                      # 200
resp.server()                                         # ver descripcion *:
del resp                                              # [!] closing connection done...      // It will call the DE-CONSTRUCTOR.


# ver descripcion *:
# Server mini_httpd/1.27 07Mar2017
# Date Fri, 30 Dec 2022 21:31:48 GMT
# Content-Type text/html; charset=UTF-8
# X-Frame-Options SAMEORIGIN
# Content-Length 294
# Last-Modified Thu, 04 Feb 2021 08:30:13 GMT
# Connection close