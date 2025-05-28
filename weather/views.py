import requests
from django.shortcuts import render


def get_weather(request):

    city = request.GET.get("city")

    weather_data = None

    if city:
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {"name": city, "count": 1, "language": "ru", "format": "json"}
        geo_response = requests.get(geo_url, params=geo_params)
        geo_json = geo_response.json()

        if geo_json.get("results"):
            location = geo_json["results"][0]
            latitude = location["latitude"]
            longitude = location["longitude"]

            weather_url = "https://api.open-meteo.com/v1/forecast"
            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": True,
            }
            weather_response = requests.get(weather_url, params=weather_params)
            weather_json = weather_response.json()

            if "current_weather" in weather_json:
                current = weather_json["current_weather"]
                weather_data = {
                    "temperature": current["temperature"],
                    "wind_speed": current["windspeed"],
                }

    return render(request, "home.html", {"city": city, "weather": weather_data})
