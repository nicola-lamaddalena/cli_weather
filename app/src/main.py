from utils import get_input, get_coordinates, parse_data
from fetch_data import get_weather
import json


def main():
    city = get_input()
    try:
        lat, lon = get_coordinates(city=city)
    except TypeError:
        print("An error occured with the name of the location. Check your spelling.")
        return None
    weather = get_weather(latitude=lat, longitude=lon, city=city)
    parse_weather = parse_data(weather)
    print(parse_weather)


if __name__ == "__main__":
    main()
