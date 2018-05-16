Para executar o script "chatbot.py" é necessário primeiro efetuar instalações de algumas bibliotecas:
	pip install --upgrade --no-deps --force-reinstall pyowm
	pip install aiml
	pip install pyttsx
	pip instal bs4 

Para instalar o corpus wordnet:
	- Executar o script "dwnld_wn".
	- Procurar em "All packages" por wordnet.
	- Instalar.

Por fim, copiar o ficheiro "Kernel.py" para a localização da instalação da biblioteca aiml.
	- Localização da biblioteca aiml em Linux:
		/usr/local/lib/python2.X/dist-packages/aiml/
	- Localização da biblioteca aiml em Windows:
		C:\Python2.X\Lib\site-packages\aiml\
		
Para executar o bot, extrair a pasta zipada "SI_TPFinal" e utilizar Python2:
	- python 2 chatbot.py (normalmente em Linux a versão genérica do Python é a 2.)