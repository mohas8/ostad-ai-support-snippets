import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 43.65107,
    "longitude": -79.347015,
    "current_weather": True
}

response = requests.get(url, params=params)
print(response.text)