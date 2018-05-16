"""
		MODULO DE PREVISOES METEREOLOGICAS
		https://openweathermap.org
"""

import requests, json

response = requests.get('http://samples.openweathermap.org/data/2.5/weather?lat=40.633196&lon=-8.657599&appid=e38b266ae32047bf6700d2ea79f42420')

json_obj = json.loads(response.text, encoding='latin-1')
json_formatted = json.dumps(json_obj, sort_keys=True, indent=2, ensure_ascii=False)

print(json_formatted)


""" OUTRA POSSIBILIDADE """
#import pyowm
#
#owm = pyowm.OWM("e38b266ae32047bf6700d2ea79f42420")
#
#observation = owm.weather_at_place('Avieor,uk')
#
#w = observation.get_weather()
#
#print(w)
