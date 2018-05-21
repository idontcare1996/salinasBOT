import aiml
#import pyttsx


kernel = aiml.Kernel()

kernel.learn("startUpGrupo.xml")

kernel.respond("LOAD AIML B")

#engine = pyttsx.init()

while True:
    print ("Enter your message: ")
    frase = input()

    
    texto = kernel.respond(frase)
    print (texto)
    texto = texto.replace('"', '')

    print ("Skynet: %s" % texto)
    #engine.say(texto)
    #engine.runAndWait()
