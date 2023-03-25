# readMe.txt : # documentation & exercises de BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# reuqest to chatGP:
# make a scraping to this webpage https://subslikescript.com/movies with Python Beautiful Soup.
# locate the tag element <ul class="scripts-list"> and get all label of the elements with tag "<a href"
# get the attibute of text and print out.

from bs4 import BeautifulSoup
import requests
import sys

print(f"python ver = {sys.version}\n")

url = "https://subslikescript.com/movies"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

ul = soup.find("ul", {"class": "scripts-list"})
#print(ul)
for li in ul.find_all("li"):
    #a = li.find("a")
    print(li.text)                                # a.text
    
# out:    
# Freibad (2022)
# Peter Handke: Bin im Wald. Kann sein, dass ich mich verspäte... (2016)
# Thunivu (2023)
# Unexpectedly Expecting (2022)
# . . .
# November (2022)
# The Last Warrior (2021)
# I Am a Cat (1975)
# La isla de los dinosaurios (1967)

    