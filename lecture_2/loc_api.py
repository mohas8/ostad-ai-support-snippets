import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 23.8103,
    "longitude": 90.4125,
    "current_weather": True
}

response = requests.get(url, params=params)
if response.status_code == 200:

    data = response.json()
    print("response:", data)

    weather = data["current_weather"]
    print("Current Weather:")
    print(f"Time: {weather['time']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Windspeed: {weather['windspeed']} km/h")
    print(f"Wind Direction: {weather['winddirection']}°")
else:
    print("Error:", response.status_code)