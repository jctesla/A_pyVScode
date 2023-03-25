# readMe.txt : documentation de BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Beautiful Soup is a Python library for pulling data out of HTML and XML files.

# Here’s an HTML document I’ll be using as an example throughout this document. It’s part of a story from Alice in Wonderland:
html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...
</p>
"""

# Running the “three sisters” document through Beautiful Soup gives us a BeautifulSoup object,
# el cual representa el documento en contexto de la estructura.

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())                          # va imprimir la estructura de los datos q le dimos p q capture y los imprime de forma
                                                # secuencial hacia abajo x <tag>

# Here are some simple ways to navigate that data structure:
print(soup.title)                               # <title>The Dormouse's story</title>
print(soup.title.name)                          # title
print(soup.title.string)                        # The Dormouse's story
print(soup.title.parent.name)                   # head
print(soup.p)                                   # <p class="title"><b>The Dormouse's story</b></p>
print(soup.p['class'])                          # ['title']
print(soup.a)                                   # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.find_all('a'))                       # [ 
                                                #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
                                                #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
                                                #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
                                                # ]
print(soup.find(id="link3"))                    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# una tarea q se usa a menudo es, extraer todo los URLs q encuentre con el tag <a>:
for link in soup.find_all('a'):
  print(link.get('href'))                       # http://example.com/elsie
                                                # http://example.com/lacie
                                                # http://example.com/tillie
  
# otra tarea muy usada es extraer todo los text del documento:
print(soup.get_text())
# The Dormouse's story
# 
# The Dormouse's story
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
# ...
  
    

