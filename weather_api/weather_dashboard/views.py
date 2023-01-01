import json
import requests
from django.http.response import HttpResponse, JsonResponse


def weather_page(request):
    payload = json.loads(request.body.decode('utf-8'))
    city = payload.get("city", "")
    weather = {
        "city": city
    }
    api_url = "https://api.openweathermap.org/data/2.5/weather?appid=c8777f2ce8c321fbd4c375b29696e1cd&q="
    url = api_url + city
    response = requests.get(url)
    weather_content = response.json()
    if weather_content['cod'] == "404":
        weather.update({
            "city": city,
        })
        print("Invalid city name, Please check your city name".format(city))
    else:
        weather.update({
            "city": city,
            "main": weather_content['weather'][0]['main']
        })
    return JsonResponse(weather)
