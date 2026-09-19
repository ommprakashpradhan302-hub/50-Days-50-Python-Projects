import requests

API_KEY = "YOUR_API_KEY_HERE"  # Get your free API key from OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data['cod'] != 200:
            print(f"❌ Error: {data['message']}")
            return

        # Extract required data
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']

        print("\n🌤 Weather in", data['name'] + "," + data['sys']['country'])
        print("=" * 40)
        print(f"Temperature: {main['temp']} °C")
        print(f"Feels Like: {main['feels_like']} °C")
        print(f"Weather: {weather['description'].title()}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")

    except requests.exceptions.RequestException as e:
        print("❌ Network Error:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
