import requests
import json

city_key = "lagos"
api_key = "43e306648ddb6a3e8e5e3b73a41344e0"
api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_key}&appid={api_key}&unit=metric"

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    data = response.json()
    print(f"error code: {data["cod"]} \nerror message: {data["message"]}")