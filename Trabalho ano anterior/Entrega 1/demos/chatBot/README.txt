Instruções para correr o AIML na plataforma Windows com o Python 2.7

Este readme tem o intuito de auxiliar a instalação do AIML no sistem que tenha
a versao do Python 2.7.9 ou mais avançada, ou qualquer outro tipo de biblioteca.

Requerimentos:
	- Windows PowerShell
	- Python 2.7.9
	- Python Pip instalado

Caso o utilizador já tenha a versão mais actualizada do Python.

-Efectuar download e instalação da versão do python 2.7.9 através do seguinte website:
https://www.python.org/downloads/release/python-279/
-A instalação irá instalar o Python 2.7.9 irá instalar por defeito no directorio C:\Python2.7
(é recomendado nao mudar o directorio para evitar problemas com a versão mais actualizada)
-Utilizar o pip da versão mais actualizada para instalar o AIML (pip install aiml)
-Aceder a seguinte pasta => ..\AppData\Local\Programs\Python\Python36\Lib\site-packages
(para aceder a pasta oculta AppData eu sugiro Winkey + R e escrever %AppData%, contudo este comando irá aceder a ..\AppData\Roaming. Mas basta retroceder para a pasta AppData e escolher a correcta)
-Selecionar a pasta aiml e colocar na pasta site-packages do python 2.7.9 ( C:\Python27\Lib\site-packages )
-Correr o ficheiro python que tenha o import aiml.

Caso o utilizador esteja a instalar o Python 2.7.9 SEM nenhuma versão no sistema instalada previamente
-Efectuar download e instalação da versão do python 2.7.9 através do seguinte website:
https://www.python.org/downloads/release/python-279/
-A instalação irá instalar o Python 2.7.9 irá instalar por defeito no directorio C:\Python2.7
-Efectuar o download e instalação do ficheiro get-pip.py através do seguinte site,
https://bootstrap.pypa.io/get-pip.py (para instalar, basta inserir a seguinte linha no PowerShell python get-pip.py)
-Correr o ficheiro python que tenha o import aiml.

Para instalar outras bibliotecas, os procedimentos são os mesmos para cada situação

Para o ubuntu basta installar o aiml através do apt-get:
sudo apt-get install python-aiml
Ou instalar o pip e instalar o AIML.