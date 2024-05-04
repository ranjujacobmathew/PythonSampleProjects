
import requests
import json

# Replace with your OpenWeatherMap API Key
api_key = "YOUR_API_KEY"

def get_weather_data(location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  # You can change units to 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data")
        return None

def display_weather(data):
    if data:
        print("\nWeather Information for", data["name"])
        print("Current Temperature:", data["main"]["temp"], "°C")
        print("Weather Condition:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("")

if __name__ == "__main__":
    location = input("Enter a city or location: ")
    weather_data = get_weather_data(location)

    if weather_data:
        display_weather(weather_data)
