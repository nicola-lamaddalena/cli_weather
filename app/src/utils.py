from geopy.geocoders import Nominatim
import pandas as pd
from sys import argv
import click


# @click.command()
# @click.option(
#     "--unit",
#     default="C",
#     help="Unit for the temperature. Default is Celsius. Type F for Fahrenheit.",
# )
# @click.option(
#     "--city",
#     help="Location that you want to check",
#     prompt="Insert your desired location",
# )
# def parse_arguments(city: str, unit: str) -> tuple:
#     parse_city, parse_unit = city.strip().capitalize(), unit.strip().upper()
#     return click.echo(parse_city), click.echo(parse_unit)


def get_input() -> str:
    try:
        city = argv[1]
        return city.strip().capitalize()
    except IndexError:
        city = input("Type the city: ").strip().capitalize()


def get_coordinates(city: str) -> tuple | None:
    geolocator = Nominatim(user_agent="my-app")
    try:
        location = geolocator.geocode(city)
        if location is not None:
            return location.latitude, location.longitude
        else:
            print("Coordinates not found.")
            return None
    except Exception as e:
        return None


def parse_data(response: dict, unit: bool = False) -> pd.DataFrame:
    parse_response = {}

    for i in range(len(response["daily"]["time"])):
        if unit:
            parse_response[response["daily"]["time"][i]] = [
                f'{response["daily"]["temperature_2m_max"][i]} °F',
                f'{response["daily"]["temperature_2m_min"][i]} °F',
                f'{response["daily"]["precipitation_probability_mean"][i]} %',
            ]
        else:
            parse_response[response["daily"]["time"][i]] = [
                f'{response["daily"]["temperature_2m_max"][i]} °C',
                f'{response["daily"]["temperature_2m_min"][i]} °C',
                f'{response["daily"]["precipitation_probability_mean"][i]} %',
            ]

    return response["current_weather"]["temperature"], pd.DataFrame.from_dict(
        parse_response,
        orient="index",
        columns=["temp_max", "temp_min", "prec_prob_max"],
    )
