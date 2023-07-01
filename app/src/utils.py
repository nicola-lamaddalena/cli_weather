import json
from geopy.geocoders import Nominatim


def get_input() -> str:
    while True:
        city: str = input("Type the city: ").strip().capitalize()
        if city != " ":
            return city
        else:
            get_input()


def get_coordinates(city: str) -> tuple:
    geolocator = Nominatim(user_agent="my-app")
    try:
        location = geolocator.geocode(city)
        if location is not None:
            return location.latitude, location.longitude
        else:
            print("Coordinates not found")
            return None
    except Exception as e:
        return None


def parse_data(response: dict) -> dict:
    apparent_temperature_max = {}
    precipitation_probability_max = {}
    for i in range(len(response["daily"]["time"])):
        apparent_temperature_max[
            response["daily"]["time"][i]
        ] = f'{response["daily"]["apparent_temperature_max"][i]} Celsius'

        precipitation_probability_max[
            response["daily"]["time"][i]
        ] = f'{response["daily"]["precipitation_probability_max"][i]} %'
    parse_response = {}
    parse_response["forecasts"] = []
    parse_response["forecasts"].extend(
        (
            {"apparent_temperature_max": apparent_temperature_max},
            {"precipitation_probability_max": precipitation_probability_max},
        )
    )
    return json.dumps(parse_response, indent=4)
