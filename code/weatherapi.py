
import requests
from tomlkit import key
from dotenv import load_dotenv
import os


API_KEY = os.getenv('OPENWEATHER_KEY')  # Don't hardcode this!
url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')
data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")
#How do we protect the key?