import unittest
from tools import get_weather


class WeatherIntegrationTest(unittest.TestCase):

    def test_get_weather_existing_city(self):
        city = "London"
        result = get_weather(city)

        self.assertIsInstance(result, str)

        self.assertIn("London", result)
        self.assertIn("Temperature", result)
        self.assertNotIn("Could not", result)
        self.assertNotIn("Invalid data", result)

    def test_get_weather_nonexistent_city(self):

        city = "InvalidCityName12345"
        result = get_weather(city)

        self.assertIsInstance(result, str)

        self.assertTrue(
            "Could not get current weather" in result
        )


if __name__ == '__main__':
    unittest.main()