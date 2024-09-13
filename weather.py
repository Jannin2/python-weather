from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city = "Kansas City"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("*** Get Current Weather Conditions ***")
    city = input("Please enter a city name: ")
    
    if not bool(city.strip()):
        city = "Kansas City"
    
    weather_data = get_current_weather(city)
    pprint(weather_data)