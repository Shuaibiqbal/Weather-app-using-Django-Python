from django.shortcuts import render
import json
import urllib.request
from urllib.error import URLError, HTTPError

def index(request):
    data = {}
    if request.method == 'POST':
        print(request.method)
        city = request.POST['city']

        try:
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' 
                        + city + '&appid={your_api_key}'.strip()).read()

            list_of_data = json.loads(source)

            # Check if the API response indicates an error
            if list_of_data.get('cod') != 200:
                data['error_message'] = f"City '{city}' not found. Please enter the complete name of the city."
            else:
                data = {
                    "country_code": str(list_of_data['sys']['country']),
                    "coordinate": str(list_of_data["coord"]["lon"]) + ' ' + str(list_of_data["coord"]["lat"]),
                    "temp": str(list_of_data["main"]["temp"]) + 'k',
                    "pressure": str(list_of_data["main"]["pressure"]),
                    "humidity": str(list_of_data["main"]["humidity"]),
                }
                print(data)

        except (json.JSONDecodeError, URLError, HTTPError) as e:
            # Handle various exceptions that might occur during the HTTP request or JSON parsing
            data = {'error_message': f"Error response for '{city}'. Please enter complete name of city."}

    else:
        data= {'error_message':"Please enter a city name."}
    return render(request, "main/index.html", data)
