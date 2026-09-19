# 🌤️ Day 40 - Weather App

A Python program that fetches real-time weather information for any city using the OpenWeatherMap API.

## 🎯 Objective

To create a Weather App that allows users to check current weather conditions such as temperature, humidity, wind speed, and description for any city.

## 🛠️ Concepts Used

- API Handling (HTTP Requests)  
- JSON Data Parsing  
- User Input  
- Exception Handling  
- Data Display  

## 📚 Required Libraries

This project uses the third‑party `requests` library.  

Install it using:

```bash
pip install requests
```

You also need a free API key from [OpenWeatherMap](https://openweathermap.org/api).

## ⚙️ How It Works

1. The user enters the name of a city.  
2. The program sends a request to the OpenWeatherMap API with the city name and API key.  
3. The API returns weather data in JSON format.  
4. The program extracts temperature, humidity, wind speed, and weather description.  
5. Results are displayed in a user‑friendly format.  
6. Errors (e.g., invalid city name or network issues) are handled gracefully.

## 💻 Example Output

```text
Enter city name: London
🌤 Weather in London,GB
----------------------------------------
Temperature: 18.6 °C
Feels Like: 18.6 °C
Weather: Partly Cloudy
Humidity: 72%
Wind Speed: 3.09 m/s
```

*Weather details are displayed clearly for the chosen city.*

## 🧠 What I Learned

- Making API requests with `requests.get()`  
- Parsing JSON responses in Python  
- Handling invalid inputs and network errors  
- Displaying structured weather information  
- Building a practical real‑world application  

## ▶️ How to Run

First, replace `"YOUR_API_KEY_HERE"` in the code with your OpenWeatherMap API key.  

Then run:

```bash
python main.py
```

Make sure you have internet access and the `requests` library installed.

## 📁 Project Structure

```text
Day40_WeatherApp/
│
├── main.py
└── README.md
```

## 🚀 50 Days 50 Python Mini Projects

**Day 40/50** — Learn • Build • Forecast  

👨‍💻 Author: **Omm Prakash Pradhan**  
B.Tech AI & ML Student
