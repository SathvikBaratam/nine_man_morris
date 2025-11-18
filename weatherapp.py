import requests
import json
import os
def load_favorites():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r") as f:
            return json.load(f)
    return []
def save_favorites(favorites):
    with open(FAV_FILE, "w") as f:
        json.dump(favorites, f, indent=2)
def get_weather_info(location):
    base_url = f"http://api.weatherapi.com/v1/current.json?key=a307190edcda41628a8140313251111&q={Location}&aqi=yes"
    response = requests.get(base_url)
    if response.status_code == 200:
            weather_data = response.json()
            print(weather_data)
            return weather_data
    else:
        print(f"Failed to get weather data for {Location}")
Location = input("Enter Location: ")
location = Location.capitalize()
weather_data = get_weather_info(location)
temp_in_celius = weather_data["current"]["temp_c"]
temp_feelslike_celcius = weather_data["current"]["feelslike_c"]
temp_feelslike_f = weather_data["current"]["feelslike_f"]
humidity = weather_data["current"]["humidity"]
air_quality = weather_data["current"]["air_quality"]

def feeling_message(temp):
    if temp < 10:
        return "🥶 It's very cold! Stay warm!"
    elif 10 <= temp < 20:
        return "🙂 It's cool outside."
    elif 20 <= temp < 30:
        return "😊 Pleasant weather!"
    else:
        return "🥵 It's hot! Stay hydrated!"

def clothing_suggestions(temp):
    if temp < 10:
        return "Wear a jacket, gloves, and warm clothes."
    elif temp < 20:
        return "A light jacket or hoodie is enough."
    elif temp < 30:
        return "T-shirt and jeans are fine."
    else:
        return "Shorts and cotton clothes recommended."

while(True):
    print("\n=========== WEATHER APP ===========")
    favorites = load_favorites()
    if favorites:
        print("\nYour favorite cities:")
        for i, city in enumerate(favorites, 1):
            print(f"{i}. {city}")
        print("Type '0'to Enter a new city")

        choice = input("\nChoose a favorite city number or 0: ")

        if choice.isdigit() and int(choice) in range(0, len(favorites) + 1):
            if choice == "0":
                Location = input("Enter city name: ")
            else:
                Location = favorites[int(choice) - 1]
        else:
            Location = input("Enter city name: ")
    else:
        Location = input("Enter Location: ")

