import requests
import json
import os
FAV_FILE = "favorite_cities.json"
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
def compare_two_cities(city1, city2):
    print(f"\n🔍 Comparing: {city1} VS {city2}\n")

    data1 = get_weather_info(city1)
    data2 = get_weather_info(city2)

    if not data1 or not data2:
        print("❌ Could not fetch weather for one or both cities.")
        return

    c1 = data1["current"]
    c2 = data2["current"]

    print("========== WEATHER COMPARISON ==========\n")
    print(f"{city1:<20} | {city2:<20}")
    print("-" * 45)

    print(f"Temp: {c1['temp_c']}°C{' ' * 10}| {c2['temp_c']}°C")
    print(f"Feels Like: {c1['feelslike_c']}°C{' ' * 5}| {c2['feelslike_c']}°C")
    print(f"Humidity: {c1['humidity']}%{' ' * 8}| {c2['humidity']}%")
    print(f"Wind: {c1['wind_kph']} km/h{' ' * 7}| {c2['wind_kph']} km/h")
    print(f"Condition: {c1['condition']['text']:<10} | {c2['condition']['text']}")

    print("\n=========================================\n")
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
        print("0. Enter a new city")
        print("R. Remove a favorite city")
        print("C. Compare two cities")

        choice = input("\nChoose a number, 0, 'R', or 'C': ").strip()

        # ---- REMOVE FAVORITE ----
        if choice.lower() == "r":
            print("\nWhich city do you want to remove?")
            for i, city in enumerate(favorites, 1):
                print(f"{i}. {city}")

            remove_choice = input("\nEnter number to remove (0 to cancel): ")

            if remove_choice.isdigit() and int(remove_choice) in range(1, len(favorites) + 1):
                removed_city = favorites.pop(int(remove_choice) - 1)
                save_favorites(favorites)
                print(f"❌ Removed '{removed_city}' from favorites.")
            else:
                print("Removal cancelled.")

            continue

        # ---- CITY COMPARISON ----
        if choice.lower() == "c":
            city1 = input("Enter first city: ").strip().title()
            city2 = input("Enter second city: ").strip().title()
            compare_two_cities(city1, city2)
            continue

        # ---- SELECT FAVORITE OR NEW CITY ----
        if choice.isdigit() and int(choice) in range(0, len(favorites) + 1):
            if choice == "0":
                Location = input("Enter city name: ")
            else:
                Location = favorites[int(choice) - 1]
        else:
            Location = input("Enter city name: ")

    # ------- No Favorites Yet -------
    else:
        Location = input("Enter Location: ")

    location = Location.strip().title()

    # ---- Fetch Weather ----
    weather_data = get_weather_info(location)
    if not weather_data:
        continue

    current = weather_data["current"]
    temp_c = current["temp_c"]
    temp_f = current["temp_f"]
    feelslike_c = current["feelslike_c"]
    humidity = current["humidity"]

    print("\n-------- CURRENT WEATHER --------")
    print(f"📍 Location: {location}")
    print(f"🌡 Temperature: {temp_c}°C / {temp_f}°F")
    print(f"🤔 Feels Like: {feelslike_c}°C")
    print(f"💧 Humidity: {humidity}%")

    print("\n" + feeling_message(temp_c))
    print("👕 Clothing Tip:", clothing_suggestions(temp_c))

    # ---- Add to favorites ----
    add_fav = input("\nAdd this city to favorites? (y/n): ").lower()
    if add_fav == "y":
        if location not in favorites:
            favorites.append(location)
            save_favorites(favorites)
            print("⭐ Added to favorites!")
        else:
            print("⭐ Already in favorites!")

    # ---- Search again ----
    again = input("\nDo you want to search again? (y/n): ").lower()
    if again != "y":
        print("\n🌤 Enjoy the weather! Goodbye!\n")
        break
