import requests

PRECIPITATION_THRESH = 700


api_key = "dce8c82ef69ba955817b1c0f84710465"
angela_key = "69f04e4613056b159c2761a9d9e664d2"

#"lat": 43.653225,
#              "lon": -79.383186,

parameters = {"lat": 43.653225,
              "lon": -79.383186,
              "exclude": "current,minutely,daily",
              "appid": angela_key}

request_weather = requests.get(url="https://api.openweathermap.org/data/2.8/onecall?", params=parameters)
request_weather.raise_for_status()

weather_data = request_weather.json()["hourly"][0:12]

not_raining = True
i = 0
while not_raining and i < len(weather_data):
    hour_ids = []
    hour = weather_data[i]["weather"]
    for weather in hour:
        hour_ids.append(weather["id"] < PRECIPITATION_THRESH)

    if any(hour_ids):
        print("Bring an umbrella")
        not_raining = False

    i += 1

#https://api.openweathermap.org/data/2.8/onecall?lat=43.653225&lon=-79.383186&exclude={part}&appid=dce8c82ef69ba955817b1c0f84710465