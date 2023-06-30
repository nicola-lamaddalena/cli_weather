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
    location = geolocator.geocode(city)
    return location.latitude, location.longitude
