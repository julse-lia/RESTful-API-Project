from django.shortcuts import render
from django.conf import settings
import requests

def home(request):
	city = {}
	api_key = settings.OPENWEATHERMAP_APP
	if 'city_name' in request.GET:
		city_name = request.GET['city_name']
		url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(city_name, api_key)
		response = requests.get(url)
		city = response.json()
	return render(request, 'app/home.html', {'city': city})

