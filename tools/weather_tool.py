
import requests

from config import WEATHER_API_KEY

def get_weather(city):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if data.get("cod") != 200:

            return {
                "success": False,
                "error": "Weather not found"
            }

        result = {

            "location": data["name"],

            "temperature": data["main"]["temp"],

            "humidity": data["main"]["humidity"],

            "weather": data["weather"][0]["description"]
        }

        return {
            "success": True,
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }