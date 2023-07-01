from geopy.geocoders import Nominatim
import pandas as pd


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
    for i in range(len(response["time"])):
        parse_response[response["time"][i]] = [
            f'{response["temperature_2m_max"][i]} °C',
            f'{response["temperature_2m_min"][i]} °C',
            f'{response["precipitation_probability_max"][i]} %',
        ]

    return pd.DataFrame.from_dict(
        parse_response,
        orient="index",
        columns=["temp_max", "temp_min", "prec_prob_max"],
    )
