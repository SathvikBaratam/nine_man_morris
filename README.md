# Weather CLI Application

A clean, modular, and dependency-light command-line weather application built with Python.
This project fetches real-time weather data from WeatherAPI and presents it in a simple, readable terminal interface.
It includes current weather details, multi-day forecasts, city comparisons, and a persistent favorites system.

## Overview

The Weather CLI project provides a user-friendly terminal experience for retrieving weather information without relying on complex UI libraries or exceptions.
The logic is divided into three clear modules:

**weather_api.py** – Handles all API requests

**weather_utils.py** – Formatting helpers, icons, favorites, and display functions

**main.py** – User interface loop and application control flow

## Features

**Current Weather Information**
Temperature, feels-like temperature, humidity, wind speed, air quality, and condition icons.

**City Comparison**
Side-by-side comparison of temperature, humidity, wind, and more.

#**Favorite Cities**
Save, load, and manage your favorite locations through a built-in JSON file.

**Simple and Dependency-Light**
Only requires the requests library.

## Project Structure

weather-cli/

│

├── main.py              # Main application loop and menu system

├── weather_api.py       # API fetch functions (current weather, forecast)

├── weather_utils.py     # Helpers: icons, UI formatting, favorites, comparison

│

├── favorite_cities.json # Auto-generated favorites file

└── README.md            # Project documentation

## Installation

Install Python 3.8 or later.

Install the required dependency:

**pip install requests**


Clone or download the project files into a single directory.

## Configuration

This project uses WeatherAPI to fetch weather data.

To set your API key, open weather_api.py and update:

**API_KEY = "your_api_key_here"**


You can obtain a free API key from:
**👉 https://www.weatherapi.com/**

## Usage

Run the application from a terminal:

**python main.py**


You will be presented with a menu similar to:

=============== WEATHER APP ===============

⭐ Favorites:
1. London
2. New York

Options:
 A. Enter a new city
 B. Remove a favorite
 C. Compare two cities
 D. Show 3-day forecast


You can then:

Type a city name (e.g., Mumbai)

Enter a number to select from favorites

Use menu options A/B/C/D.

Example Output
##### ================ CURRENT WEATHER ================
📍 Location: Tokyo
##### 🌤 Condition: Partly cloudy
##### 🌡 Temp: 22°C (71°F)
##### 🤔 Feels Like: 21°C
##### 💧 Humidity: 64%
##### 💨 Wind: 13 km/h
##### 🌫 AQI (PM2.5): 14
##### --------------------------------------------------
##### 😊 Pleasant weather!
##### 👕 T-shirt weather.
##### ==================================================
