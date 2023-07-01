from geopy.geocoders import Nominatim
import pandas as pd
import click
import requests


def get_weather(latitude: float, longitude: float, city: str, unit: str) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_min,temperature_2m_max,precipitation_probability_mean&current_weather=true&timezone=Europe/Berlin"
    if unit == "F":
        url += "&temperature_unit=fahrenheit"
    response = requests.get(url=url)
    if response.status_code != 404:
        return response.json()
    else:
        return f"{city} not found."


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


@click.command()
@click.option(
    "--unit",
    default="C",
    help="Unit for the temperature. Default is Celsius. Type F for Fahrenheit.",
)
@click.option(
    "--city",
    help="Location that you want to check",
    prompt="Insert your desired location",
)
def parse_arguments(city: str, unit: str) -> tuple:
    parse_city, parse_unit = city.strip().capitalize(), unit.strip().upper()
    lat, lon = get_coordinates(parse_city)
    response = get_weather(
        latitude=lat, longitude=lon, city=parse_city, unit=parse_unit
    )
    curr_temp, future_temp = parse_data(response=response, unit=parse_unit)
    print("--------------------")
    print("Today's temperature:", curr_temp, "°C")
    print()
    print(future_temp)


def parse_data(response: dict, unit: str) -> pd.DataFrame:
    parse_response = {}

    for i in range(len(response["daily"]["time"])):
        if unit == "F":
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


def main():
    parse_arguments()


if __name__ == "__main__":
    main()
