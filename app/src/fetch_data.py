import requests


def get_weather(
    latitude: float, longitude: float, city: str, unit: bool = False
) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_min,temperature_2m_max,precipitation_probability_mean&current_weather=true&timezone=Europe/Berlin"
    if unit:
        url += "&temperature_unit=fahrenheit"
    response = requests.get(url=url)
    if response.status_code != 404:
        # return response.json()["daily"]
        return response.json()
    else:
        return f"{city} not found."
