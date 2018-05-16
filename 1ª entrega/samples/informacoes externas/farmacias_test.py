"""
		MODULO DE PESQUISA DE FARMACIAS DE SERVIÇO
		FALTA ELABORAR O PARSER DE INFORMAÇÃO DE DADOS
		A INFORMAÇÃO ESTA ORIGINALMENTE REPRESENTADA EM HTML E NÃO EM JSON
"""

import requests

response = requests.get("http://www.farmaciasdeservico.net/ig/api?up_localidade=aveiro|aveiro")

print(response.text)