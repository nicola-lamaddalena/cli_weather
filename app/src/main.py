from utils import get_input, get_coordinates
from fetch_data import get_weather


def main():
    city = get_input()
    lat, lon = get_coordinates(city=city)
    weather = get_weather(latitude=lat, longitude=lon, city=city)
    print(weather)


if __name__ == "__main__":
    main()
