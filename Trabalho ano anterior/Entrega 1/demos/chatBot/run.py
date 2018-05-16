import aiml
import pyttsx
import urllib2
import re
from bs4 import BeautifulSoup
import os

def translate(linguaParaTraduzir,querie):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    GoogleTranslatorlink = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" #link fixo, old google translator FTW
    link = GoogleTranslatorlink % (linguaParaTraduzir, "pt", querie)
    paginaWiki = opener.open(link)
    dados = paginaWiki.read()
    paginaWiki.close()
    bs = BeautifulSoup(dados, "html.parser")
    linha = bs.find('div',{ "class" : "t0" })
    return linha.getText()


#Dicionario com os codigo dos paises e o respectivo pais
paises = {'afrikaans':'af', 'albanian':'sq', 'arabic':'ar', 'belarusian':'be', 'bulgarian':'bg', 'batalan':'ca', 'bhinese':'zh-CN', 'broatian':'hr', 'bzech':'cs',  'danish':'da', 'dutch':'nl', 'english':'en', 'estonian':'et', 'filipino':'tl', 'finnish':'fi', 'french':'fr', 'galician':'gl', 'german':'de', 'greek':'el', 'hebrew':'iw', 'hindi':'hi', 'hungarian':'hu', 'icelandic':'is', 'indonesian':'id', 'irish':'ga', 'italian':'it', 'japanese':'ja', 'korean':'ko', 'latvian':'lv',  'lithuanian':'lt', 'macedonian':'mk', 'malay':'ms', 'maltese':'mt', 'norwegian':'no', 'persian':'fa', 'polish':'pl', 'portuguese':'pt', 'pomanian':'ro', 'russian':'ru', 'serbian':'sr', 'slovak':'sk', 'slovenian':'sl', 'spanish':'es', 'swahili':'sw', 'swedish':'sv', 'thai':'th', 'turkish':'tr', 'ukrainian':'uk','vietnamese':'vi', 'welsh':'cy', 'yiddish':'yi'}

#padrao regex
re = re.compile("Translate")

engine = pyttsx.init()

kernel = aiml.Kernel()


if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


while True:
    print "Enter your message: "
    frase = raw_input()
    if re.search(frase):
        argumentos = frase.split(' ', 3)
        liguagem = paises[argumentos[2]]
        tra = translate(liguagem, argumentos[3].replace(" ","%20"))
        #engine.say(tra)
        print "Skynet: %s" % tra
    elif frase=="quit":
	       exit()
    elif frase =="save":
	       kernel.saveBrain("bot_brain.brn")
    else:
        texto = kernel.respond(frase)
        #engine.say(texto)
        print "Skynet: %s" % texto
    engine.runAndWait()
