
import urllib.request
import urllib.error
import json

from datetime import datetime, timezone
from typing import List, Dict, Any


class Weather:
    """

    """
    def __init__(self):
        """
        Provides class initialization
        """

        # initialization of JSON dictionary
        self._items: List[Dict[str, Any]] = []


    def _config(self):
        """
        Attempts to load JSON data.

        Provides configuration options for entire recommender service
        :return:
        """

        # check for instance
        if not self._items:
            return

        try:
            with open("../config.json", "r") as datafile:
                self._items = json.load(datafile)
                print("json data loaded successfully.")
                return

        except FileNotFoundError:
            print("Error: The file '30DayQuakes.json' was not found.")

        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")



    def get_elevation(self, lat: float, long: float):
        """
        Obtains elevation from specific coordinates
        :param lat:
        :param long:
        :return:
        """

        pass


    def get_weather(self, lat: float, lon: float) -> List[Dict[str, Any]]:
        """
        Obtains the weather forecast for the current date
        and location.
        :param lat: Latitude
        :param lon: Longitude
        :return: The current weather forecast (time-based)
        """

        # container for resulting weather data
        weather_data: List[Dict[str, Any]] = None

        # check for empty configuration list
        if not self._items:
            self._config()


        # set the json api key
        api_key = self._items['weather_api']['api_key']

        # set the default weather units
        units = self._items['weather_api']['units']

        # set the url endpoint
        base_url = self._items['weather_api']['endpoint']

        # set the full url with querystring
        url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}&units={units}"

        try:
            # initiate the connection
            with urllib.request.urlopen(url) as response:
                data = response.read().decode()

            weather_data = json.loads(data)

        except urllib.error.URLError as e:
            print(f"Error accessing URL: {e}")  # replace with log statement

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")  # replace with log statement

        # obtain forecasts
        forecasts = weather_data['list']

        # Find the closest matching forecast
        closest = self._filter_forecast(forecasts)

        # Convert the timestamp to a datetime object for readability
        forecast_current = datetime.fromtimestamp(closest['dt'], tz=timezone.utc)

        # TODO: Build out a condensed JSON model containing only the info I need.
        # However, there's only a single record.


        # review final results
        print(f"closest forecast time is {forecast_current}: \n{closest}")


    @staticmethod
    def _filter_forecast(forecasts) -> List[Dict[str, Any]]:
        """
        Helper method that iterates through the
        daily forecasts (up to 8) and find the closest match to the current datetime.
        :param forecasts:
        :return: the closest forecast
        """
        current_timestamp = datetime.now(timezone.utc).timestamp()

        return min(forecasts, key=lambda forecast: abs(forecast['dt'] - current_timestamp))
