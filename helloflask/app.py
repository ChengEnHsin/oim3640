from flask import Flask
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
OPENWEATHER_KEY = os.getenv('OPENWEATHER_KEY')

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/hello")
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        return 'Hello, World!'
    return f"Hello, {name}!"

@app.route('/weather/<city>')
def weather(city):
    """Get current temperature for a city using OpenWeatherMap API"""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            description = data['weather'][0]['description']
            city_name = data['name']
            country = data['sys']['country']
            
            return f"""
            <h1>Weather in {city_name}, {country}</h1>
            <p><strong>Current Temperature:</strong> {temp}°C</p>
            <p><strong>Feels Like:</strong> {feels_like}°C</p>
            <p><strong>Condition:</strong> {description.capitalize()}</p>
            """
        else:
            return f"<p>Error: City '{city}' not found. Please check the spelling.</p>"
    except Exception as e:
        return f"<p>Error: {str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True)

