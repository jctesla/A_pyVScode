# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
""" Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
It works with your favorite parser to provide idiomatic ways of navigating, searching,
 and modifying the parse tree. It commonly saves programmers hours or days of work.
from bs4 import BeautifulSoup
# works very well with Requests or urllib module 
"""

# Quick Start
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# Here’s an HTML document I’ll be using as an example throughout this document. It’s part of a story from Alice in Wonderland:
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

"""
OUTPUT: 
<html>
 <body>
  <p>
   Some
   <b>
    bad
    <i>
     HTML
    </i>
   </b>
  </p>
 </body>
</html>
"""
soup.find(text="bad")
# 'bad'

soup.i
# <i>HTML</i>

# Another Example
soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
print(soup.prettify())

"""
<?xml version="1.0" encoding="utf-8"?>
<tag1>
 Some
 <tag2/>
 bad
 <tag3>
  XML
 </tag3>
</tag1>
"""