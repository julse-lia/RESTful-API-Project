# Simple Weather RESTful API Project
____

This app uses data from the ```https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}``` endpoint to get info about weather description and temperature in the desired city.

Here is a simple view using the __requests__ Python library which can be installed using pip:

``` 
   pip install requests
```

### views.py

```
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
```

### urls.py

```
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
   ]
```

### home.html

```
   {% extends 'app/base.html' %}

   {% block content %}
	<form method="get">
		<div class="row align-items-center">
			<div class="col align-self-start">
				<input class="form-control-md" id="inp" type="text" name="city_name">
			</div>
			<div class="col align-self-end">
				<button class="btn btn-primary btn-sm" id = "but" type="submit" value="Submit">Submit</button>
			</div>
		</div>
	</form>
	{% if city %}
		<p>Weather in <strong>{{ city.name }}</strong> for now:</p>
		<img src="https://api.openweathermap.org/img/w/{{ city.weather.0.icon }}.png" class="rounded-2 border border-secondary border-2">
		<p>Description: <strong>{{ city.weather.0.description }}</strong></p>
		<p>Temperature in Kelvin: <strong>{{ city.main.temp }}</strong></p>
	{% endif %}

   {% endblock %}
```

As the result we get:

![weather app picture](weather.png)
