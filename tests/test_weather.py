import unittest
from app.weather import Weather


class WeatherTests(unittest.TestCase):
    """

    """

    def test_something(self):

        # let's load and test an instance of the weather model.
        lat, long = 37.7749, -122.4194  # San Francisco coordinates

        w = Weather()
        w.get_weather(lat, long)

        self.assertEqual(True, False)  # add assertion here



# This block allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main()
