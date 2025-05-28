import requests

# Step 1: Set the base URL
url = "https://api.open-meteo.com/v1/forecast"

# Step 2: Set parameters (example: Toronto)
params = {
    "latitude": 23.8103,
    "longitude": 90.4125,
    "current_weather": True
}

# Step 3: Make the GET request
response = requests.get(url, params=params)

# Step 4: Check response and print
if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data["current_weather"]
    print("Weather in Dhaka:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Windspeed: {weather['windspeed']} km/h")
    print(f"Time: {weather['time']}")
else:
    print("Error:", response.status_code)