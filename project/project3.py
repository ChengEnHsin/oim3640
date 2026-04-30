import math
import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

MAPBOX_API_KEY = os.getenv('MAPBOX_KEY')
MBTA_API_KEY = os.getenv('MBTA_KEY')
BOSTON_CENTER = (42.3601, -71.0589)


def _distance_km(lat1, lon1, lat2, lon2):
    # Haversine distance
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371 * c


def _is_near_boston(latitude, longitude, threshold_km=50):
    return _distance_km(latitude, longitude, BOSTON_CENTER[0], BOSTON_CENTER[1]) <= threshold_km


def geocode_place(place_name):
    """
    Takes a place name and returns latitude/longitude using Mapbox API
    Returns: (latitude, longitude) or None if not found
    """
    def _query_mapbox(query, bbox=None):
        params = {
            'access_token': MAPBOX_API_KEY,
            'limit': 1,
            'country': 'us',
            'proximity': '-71.0589,42.3601'
        }
        if bbox:
            params['bbox'] = bbox
        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{quote(query)}.json"
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data['features']:
            coords = data['features'][0]['geometry']['coordinates']
            return (coords[1], coords[0])
        return None

    try:
        primary_coords = _query_mapbox(place_name)
        if primary_coords and _is_near_boston(*primary_coords):
            return primary_coords

        # Fallback: for ambiguous or out-of-area places, retry with Boston context
        if primary_coords is None or not _is_near_boston(*primary_coords):
            fallback_name = f"{place_name}, Boston, MA"
            fallback_coords = _query_mapbox(fallback_name, bbox='-71.27,42.22,-70.8,42.45')
            if fallback_coords and _is_near_boston(*fallback_coords):
                return fallback_coords
        return primary_coords
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