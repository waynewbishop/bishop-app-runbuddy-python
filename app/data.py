
import urllib.request
import json

from typing import List, Dict, Any


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

    def __init__(self):
        """
        Initialize the Data instance.

        Sets up necessary connections to data sources and initializes
        any required data structures or storage mechanisms.
        """

        # initialization of JSON dictionary
        self._config: List[Dict[str, Any]] = []


    def load_config(self):
        """
        Attempts to load JSON data.

        Provides configuration options for entire recommender service
        :return:
        """

        try:
            with open("../config.json", "r") as datafile:
                self._config = json.load(datafile)
                print("json data loaded successfully.")
                return

        except FileNotFoundError:
            print("Error: The file '30DayQuakes.json' was not found.")

        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")



    def get_weather(self, lat, lon):
        """
        Obtains the weather forecast for the current date
        and location.
        :param lat: Latitude
        :param lon: Longitude
        :return:
        """

        # check for an empty list
        if not self._config:
            self.load_config()

        # set the json api key
        api_key = self._config['weather_api']['api_key']

        # set the default weather units
        units = self._config['weather_api']['units']

        # set the url endpoint
        base_url = self._config['weather_api']['endpoint']

        # set the full url with querystring
        url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}&units={units}"

        # TODO: Add try catch statement here as well as logging

        # initiate the connection
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()

        weather_data = json.loads(data)
        return weather_data

        # TODO: Filter down data to match the current date