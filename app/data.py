
import urllib.request
import json

from datetime import datetime

class Data:
    """
    Data class handles the gathering and preprocessing of data for Run Buddy.

    This class is responsible for collecting weather data, user input, and potentially
    historical running data to be used in generating outfit recommendations.

    Attributes:
        (List any important attributes here, e.g., data sources, storage mechanisms)

    Methods:
        (List important methods here, e.g., data collection, cleaning, and storage methods)
    """

    _api_key = None

    def __init__(self):
        """
        Initialize the Data instance.

        Sets up necessary connections to data sources and initializes
        any required data structures or storage mechanisms.
        """

        # TODO: initialize the config.json access here

        pass


    @staticmethod
    def get_weather_by_coords(self, lat, lon, api_key, units):

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}&units={units}"

        with urllib.request.urlopen(url) as response:
            data = response.read().decode()

        weather_data = json.loads(data)
        return weather_data
