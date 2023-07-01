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
    parse_response = {}
    parse_response["forecasts"] = []
    for i in range(len(response["time"])):
        parse_response["forecasts"].append(
            {
                response["time"][i]: [
                    {"temp_max": f'{response["temperature_2m_max"][i]} Celsius'},
                    {"temp_min": f'{response["temperature_2m_min"][i]} Celsius'},
                    {
                        "precipitation_prob_max": f'{response["precipitation_probability_max"][i]} %'
                    },
                ]
            }
        )
    return json.dumps(parse_response, indent=2)
