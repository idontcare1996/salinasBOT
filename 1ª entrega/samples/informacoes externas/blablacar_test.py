"""
		MODULO DE PESQUISA DE BOLEIAS NO SERVIÇO BLABLACAR
		A AUSENCIA DE DADOS SIGNIFICA A AUSENCIA DE BOLEIAS DISPONIVEIS NO SERVIÇO
	PARA UMA DADA COORDENADA DE PARTIDA E CHEGADA
"""

import http.client
import json
import datetime
now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)

print(now.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))
conn = http.client.HTTPSConnection("public-api.blablacar.com")

headers = {
	'accept': "application/json",
	'key': "1243d7b42542442b94e754e77b4cac68"
	}

conn.request("GET", "/api/v2/trips?"
			 "fn=40.640506,-8.653754"
			 "&tc=38.736946,-9.142685"
			 "&locale=pt_PT"
			 "&_format=json"
			 "&cur=EUR"
			 "&db=" + tomorrow.strftime('%Y-%m-%d')
			 +
			 #"&de=" + tomorrow.strftime('%Y-%m-%d') +
			 #"&seats=1"
			 #"&limit=5"
			 "&sort=trip_price"
			 "&order=asc"
			 , headers=headers)
res = conn.getresponse()
data = res.read().decode()
json_obj = json.loads(data, encoding='latin-1')
json_formatted = json.dumps(json_obj, sort_keys=True, indent=2, ensure_ascii=False)

#print(headers)
#print(type(json_obj))

print(json_obj)

distance = json_obj.get('distance')                 # distancia em KM
duracao = int(json_obj.get('duration') / 60)        # duracao da viagem em minutos

print(distance)
print(duracao)

trip = json_obj.get('trips')


preco = []
chegada = []
chegadaLatitude = []
chegadaLongitude = []

partidaData = []
partidaHora = []
partida = []
partidaLatitude = []
partidaLongitude = []
free_seats = []
id = []

car_type = []

for i in trip:
	chegada.append(i.get('arrival_place').get('address'))
	chegadaLatitude.append(i.get('arrival_place').get('latitude'))
	chegadaLongitude.append(i.get('arrival_place').get('longitude'))

	partidaData.append(i.get('departure_date').split(" ")[0])
	partidaHora.append(i.get('departure_date').split(" ")[1])
	partida.append(i.get('departure_place').get('address'))
	partidaLatitude.append(i.get('departure_place').get('latitude'))
	partidaLongitude.append(i.get('departure_place').get('longitude'))

	preco.append(i.get('price_with_commission').get('value'))
	id.append(i.get('trip_details_id'))

	#car_type.append(i.get('car').get('make') + " " + i.get('car').get('model'))
	free_seats.append(i.get('seats_left'))


print(preco)
print(chegada)
print(chegadaLatitude)
print(chegadaLongitude)
print(partidaData)
print(partidaHora)
print(partida)
print(partidaLatitude)
print(partidaLongitude)
print(id)
print(car_type)
print(free_seats)



#ficheiro = open("out2.json", "w")

#ficheiro.write(json_formatted)
