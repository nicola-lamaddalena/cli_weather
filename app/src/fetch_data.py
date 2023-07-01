import requests


def get_weather(latitude: float, longitude: float, city: str) -> dict:
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_min,temperature_2m_max,apparent_temperature_min,apparent_temperature_max,precipitation_probability_max&timezone=Europe/Berlin"
    )
    if response.status_code != 404:
        return response.json()
    else:
        return f"{city} not found."
