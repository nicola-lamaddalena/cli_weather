import unittest
from unittest.mock import patch
from main import get_coordinates, get_weather, parse_data
import pandas as pd


class WeatherAppTests(unittest.TestCase):
    def test_get_coordinates_valid_city(self):
        city = "Bari"
        expected = (41.1257843, 16.8620293)
        result = get_coordinates(city)
        self.assertEqual(result, expected)

    def test_get_coordinates_invalid_city(self):
        city = "InvalidCity"
        expected = (None, None)
        result = get_coordinates(city)
        self.assertEqual(result, expected)

    @patch("requests.get")
    def test_get_weather_success(self, mock_get):
        mock_response = {
            "daily": {
                "time": ["2023-06-30", "2023-07-01"],
                "temperature_2m_max": [25.0, 28.0],
                "temperature_2m_min": [15.0, 18.0],
                "precipitation_probability_mean": [30, 20],
            },
            "current_weather": {"temperature": 23.0},
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        latitude, longitude = 41.1257843, 16.8620293
        unit = "C"
        result = get_weather(latitude, longitude, unit)

        expected = mock_response
        self.assertEqual(result, expected)

    @patch("requests.get")
    def test_get_weather_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        latitude, longitude = 41.1257843, 16.8620293
        unit = "C"
        result = get_weather(latitude, longitude, unit)

        self.assertEqual(result, {})

    def test_parse_data(self):
        response = {
            "daily": {
                "time": ["2023-06-30", "2023-07-01"],
                "temperature_2m_max": [25.0, 28.0],
                "temperature_2m_min": [15.0, 18.0],
                "precipitation_probability_mean": [30, 20],
            },
            "current_weather": {"temperature": 23.0},
        }
        unit = "C"
        result = parse_data(response, unit)

        expected_current_temp = 23.0
        expected_dataframe = pd.DataFrame(
            data={
                "temp_max": ["25.0 °C", "28.0 °C"],
                "temp_min": ["15.0 °C", "18.0 °C"],
                "prec_prob_max": ["30 %", "20 %"],
            },
            index=["2023-06-30", "2023-07-01"],
        )
        self.assertEqual(result[0], expected_current_temp)
        self.assertTrue(result[1].equals(expected_dataframe))


if __name__ == "__main__":
    unittest.main()
