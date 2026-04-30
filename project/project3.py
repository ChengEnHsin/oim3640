import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

MAPBOX_API_KEY = os.getenv('MAPBOX_KEY')
MBTA_API_KEY = os.getenv('MBTA_KEY')

def geocode_place(place_name):
    """
    Takes a place name and returns latitude/longitude using Mapbox API
    Returns: (latitude, longitude) or None if not found
    """
    # URL encode the place name
    encoded_place = quote(place_name)
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{encoded_place}.json"
    params = {
        'access_token': MAPBOX_API_KEY,
        'limit': 1
    }
    
    try:
        response = requests.get(url, params=params)
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
    url = "https://api-v3.mbta.com/stops"
    params = {
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
        'api_key': MBTA_API_KEY,
        'page[limit]': 1
    }
    
    response = None
    try:
        response = requests.get(url, params=params)
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


def main():
    # Test the pipeline
    test_places = ["Boston Common", "Times Square", "Fenway Park"]
    
    for place in test_places:
        print(f"\nSearching for nearest MBTA stop to: {place}")
        result = find_stop_near(place)
        
        if result:
            stop_name, wheelchair_accessible = result
            print(f"  Stop: {stop_name}")
            print(f"  Wheelchair Accessible: {'Yes' if wheelchair_accessible else 'No'}")
        else:
            print(f"  Could not find stop for {place}")


if __name__ == "__main__":
    main()