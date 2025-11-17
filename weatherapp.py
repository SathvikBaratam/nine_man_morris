import requests
import json
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


