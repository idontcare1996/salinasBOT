from pyquery import PyQuery
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.farmaciasdeservico.net/ig/api?up_localidade=aveiro|aveiro")

soup = BeautifulSoup(r.content)

print soup.select("body")
print 

html = "http://www.farmaciasdeservico.net/ig/api?up_localidade=aveiro|aveiro"

pq = PyQuery(html)
tag = pq('body')

print type(tag.text())

tag_utf8 = tag.text()
tag_utf8_replaced = tag_utf8.replace("\n","__")
#.replace("____","")

print "olá"
listaFarmacias = tag_utf8_replaced.split("____")

print listaFarmacias

for i in listaFarmacias:
    if '(Disponibilidade)' in i:
        i.replace("(Disponibilidade)","")
    if '(Permanente)' in i:
        i.replace("(Permanente)","")



listaFinal = []

for i in xrange(0,len(listaFarmacias)):
    listaFinal.append(listaFarmacias[i].split())


#import requests

#response = requests.get("http://www.farmaciasdeservico.net/ig/api?up_localidade=aveiro|aveiro")

#print response.text