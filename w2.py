import requests
import json
import os

API_KEY = "a307190edcda41628a8140313251111"
FAV_FILE = "favorite_cities.json"


def load_favorites():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r") as f:
            data = f.read()
        if data.strip() == "":
            return []
        return json.loads(data)
    return []


def save_favorites(favorites):
    with open(FAV_FILE, "w") as f:
        f.write(json.dumps(favorites, indent=2))


# ===========================================================
# WEATHER API
# ===========================================================
def get_weather(location):
    url = (
        "http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={location}&aqi=yes"
    )
    response = requests.get(url)

    if response.status_code != 200:
        print("\n❌ Failed to fetch weather.")
        return None

    return response.json()


# ===========================================================
# HELPERS
# ===========================================================
def weather_icon(cond):
    c = cond.lower()
    if "sun" in c or "clear" in c: return "☀️"
    if "cloud" in c: return "⛅"
    if "rain" in c: return "🌧️"
    if "snow" in c: return "❄️"
    if "thunder" in c: return "⛈️"
    if "fog" in c or "mist" in c: return "🌫️"
    return "🌤"


def feeling_message(temp):
    if temp < 10: return "🥶 It's very cold!"
    if temp < 20: return "🙂 It's cool outside."
    if temp < 30: return "😊 Pleasant weather!"
    return "🥵 It's hot! Stay hydrated!"


def clothing_tip(temp):
    if temp < 10: return "Wear a jacket & warm clothes."
    if temp < 20: return "A light hoodie is enough."
    if temp < 30: return "T-shirt weather."
    return "Wear light, breathable cotton or linen."


# ===========================================================
# DISPLAY
# ===========================================================
def show_current_weather(location, data):
    current = data["current"]
    cond = current["condition"]["text"]
    icon = weather_icon(cond)

    print("\n================ CURRENT WEATHER ================")
    print(f"📍 Location: {location}")
    print(f"{icon} Condition: {cond}")
    print(f"🌡 Temp: {current['temp_c']}°C ({current['temp_f']}°F)")
    print(f"🤔 Feels Like: {current['feelslike_c']}°C")
    print(f"💧 Humidity: {current['humidity']}%")
    print(f"💨 Wind: {current['wind_kph']} km/h")
    print(f"🌫 AQI (PM2.5): {int(current['air_quality']['pm2_5'])}")
    print("--------------------------------------------------")
    print(feeling_message(current["temp_c"]))
    print("👕 Clothing Recommendations:", clothing_tip(current["temp_c"]))
    print("==================================================")


def compare_cities(c1, c2):
    w1 = get_weather(c1)
    w2 = get_weather(c2)

    if w1 is None or w2 is None:
        print("\n❌ Cannot compare cities.\n")
        return

    d1 = w1["current"]
    d2 = w2["current"]

    print("\n=================== COMPARISON ====================")
    print(f"{c1:<20} | {c2:<20}")
    print("-" * 50)
    print(f"{d1['temp_c']}°C{' ' * 12}| {d2['temp_c']}°C   Temperature")
    print(f"{d1['feelslike_c']}°C{' ' * 9}| {d2['feelslike_c']}°C   Feels like")
    print(f"{d1['humidity']}%{' ' * 14}| {d2['humidity']}%   Humidity")
    print(f"{d1['wind_kph']} km/h{' ' * 8}| {d2['wind_kph']} km/h   Wind")
    print("===================================================\n")


# ===========================================================
# MAIN LOOP
# ===========================================================
while True:
    print("\n=============== WEATHER APP ===============")

    favorites = load_favorites()

    if len(favorites) > 0:
        print("\n⭐ Favorites:")
        for i, c in enumerate(favorites, 1):
            print(f" {i}. {c}")

    print("\nOptions:")
    print(" A. Enter a new city")
    print(" B. Remove a favorite")
    print(" C. Compare two cities")
    print(" D. Detect my location (auto)")

    choice = input("\nChoose option or enter city name: ").strip()

    # REMOVE FAVORITE
    if choice.lower() == "b":
        if len(favorites) == 0:
            print("No favorites yet.")
        else:
            print("\nRemove which?")
            for i, c in enumerate(favorites, 1):
                print(f"{i}. {c}")
            ans = input("Enter number: ").strip()
            if ans.isdigit():
                idx = int(ans)
                if 1 <= idx <= len(favorites):
                    removed = favorites.pop(idx - 1)
                    save_favorites(favorites)
                    print(f"❌ Removed {removed}")
        continue

    # COMPARE
    if choice.lower() == "c":
        c1 = input("First city: ").title()
        c2 = input("Second city: ").title()
        compare_cities(c1, c2)
        continue

    # AUTO DETECT LOCATION
    if choice.lower() == "d":
        print("\n📍 Detecting your location...")
        data = get_weather("auto:ip")
        if data:
            location = data["location"]["name"]
            show_current_weather(location, data)
        else:
            print("❌ Location detection failed.")

        again = input("\nSearch again? (y/n): ").lower()
        if again != "y":
            print("\n🌤 Goodbye!\n")
            break
        continue

    # FAVORITE SELECTION
    if choice.isdigit() and 1 <= int(choice) <= len(favorites):
        location = favorites[int(choice) - 1]
        from_favorite = True
    else:
        location = choice.title()
        from_favorite = False

    # GET WEATHER
    data = get_weather(location)
    if data is None:
        continue

    show_current_weather(location, data)

    # ADD TO FAVORITES (only for NEW cities)
    if location in favorites:
        print("⭐ This city is already in your favorites.")
    else:
        add = input("Add to favorites? (y/n): ").lower()
        if add == "y":
            favorites.append(location)
            save_favorites(favorites)
            print("⭐ Added!")

    # AGAIN
    again = input("\nSearch again? (y/n): ").lower()
    if again != "y":
        print("\n🌤 Goodbye!\n")
        break
