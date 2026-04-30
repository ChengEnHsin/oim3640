import requests
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

app = Flask(__name__)

MAPBOX_API_KEY = os.getenv('MAPBOX_KEY')
MBTA_API_KEY = os.getenv('MBTA_KEY')

def geocode_place(place_name):
    """
    Takes a place name and returns latitude/longitude using Mapbox API
    Returns: (latitude, longitude) or None if not found
    """
    encoded_place = quote(place_name)
    params = {
        'access_token': MAPBOX_API_KEY,
        'limit': 1
    }
    
    try:
        response = requests.get(f"https://api.mapbox.com/geocoding/v5/mapbox.places/{encoded_place}.json", params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['features']:
            coords = data['features'][0]['geometry']['coordinates']
            return (coords[1], coords[0])  # Return (latitude, longitude)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error geocoding place: {e}")
        return None


def find_nearest_mbta_stop(latitude, longitude):
    """
    Takes lat/lng and returns the nearest MBTA stop name and wheelchair accessibility
    Returns: (stop_name, wheelchair_accessible) or None if not found
    """
    params = {
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
        'api_key': MBTA_API_KEY,
        'page[limit]': 1
    }
    
    response = None
    try:
        response = requests.get("https://api-v3.mbta.com/stops", params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['data']:
            stop = data['data'][0]
            stop_name = stop['attributes']['name']
            wheelchair_accessible = stop['attributes']['wheelchair_boarding'] == 1
            return (stop_name, wheelchair_accessible)
        return None
    except requests.exceptions.RequestException as e:
        if response is not None:
            print(f"Error finding MBTA stop: {e} - {response.text}")
        else:
            print(f"Error finding MBTA stop: {e}")
        return None


def find_stop_near(place_name):
    """
    Combines geocoding and MBTA search
    Takes a place name and returns (stop_name, wheelchair_accessible)
    """
    coords = geocode_place(place_name)
    if not coords:
        return None
    
    latitude, longitude = coords
    return find_nearest_mbta_stop(latitude, longitude)


@app.route('/', methods=['GET'])
def home():
    """Display home page with search form"""
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    """Handle form submission and return results"""
    place_name = request.form.get('place_name', '').strip()
    
    if not place_name:
        return render_template('results.html', error="Please enter a place name")
    
    result = find_stop_near(place_name)
    
    if result is None and geocode_place(place_name) is None:
        return render_template('results.html', error=f"Could not find location: {place_name}")
    
    if result is None:
        return render_template('results.html', error=f"No MBTA stops found near {place_name}")
    
    stop_name, wheelchair_accessible = result
    
    return render_template('results.html', 
                         place_name=place_name,
                         stop_name=stop_name,
                         wheelchair_accessible=wheelchair_accessible)


if __name__ == '__main__':
    app.run(debug=True)