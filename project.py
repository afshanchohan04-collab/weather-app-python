import requests

def get_weather(city):
    api_key = "0971f17a69c892069ca6d5e5ae40992e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\n================ WEATHER REPORT ================")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("================================================\n")
    else:
        print("\n❌ Error:", data.get("message", "Something went wrong"))

while True:
    city = input("Enter city name (or type 'exit'): ")

    if city.lower() == "exit":
        print("Goodbye 👋")
        break

    get_weather(city)