from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'   
    }
    try:
        result = requests.get(weather_url, params = params)
        result.raise_for_status
        weather = result.json()
        if 'data' in weather:
            if "current_condition" in weather['data']:
                try:
                    weather = weather['data']['current_condition'][0]
                    return weather
                except(IndexError, TypeError,):
                    return False        
    except(requests.RequestException, ValueError,):
        print("Connecting Error")
        return False
    return False

if __name__ == "__main__":
    print(weather_by_city("Moscow,Russia"))