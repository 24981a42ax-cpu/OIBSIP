import requests

print("===== BASIC WEATHER APP =====")

API_KEY = "YOUR_API_KEY_HERE"

city = input("Enter city name: ").strip()

if city == "":
    print("Error: Please enter a city name.")

else:
    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=parameters, timeout=10)

        if response.status_code == 200:

            data = response.json()

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n===== WEATHER INFORMATION =====")
            print("City:", data["name"])
            print("Temperature:", round(temperature_c, 2), "°C")
            print("Temperature:", round(temperature_f, 2), "°F")
            print("Humidity:", humidity, "%")
            print("Condition:", condition.title())
            print("Wind Speed:", wind_speed, "m/s")

        elif response.status_code == 404:
            print("Error: City not found.")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        else:
            print("Error: Unable to fetch weather information.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Error: Network problem. Please check your internet connection.")