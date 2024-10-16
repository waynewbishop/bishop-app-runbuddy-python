import requests
import certifi
import json

from datetime import datetime, timezone
from typing import List, Dict, Any


class Weather:

    def __init__(self):
        """
        Used to obtain current weather information.
        """

        # item dictionary and logger
        self._items: List[Dict[str, Any]] = []


    def _config(self):
        """
        Provides configuration options for entire recommender service
        :return:
        """

        # check for instance
        if self._items:
            return

        try:
            with open("../config.json", "r") as datafile:
                self._items = json.load(datafile)
                print("config data loaded successfully.")
                return

        except Exception as e:
            print(f"An unexpected error occurred: {e}")



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


        # set the api key
        api_key = self._items['weather_api']['api_key']

        # set the default weather units
        units = self._items['weather_api']['units']

        # set the url endpoint
        base_url = self._items['weather_api']['endpoint']

        # set the full url with querystring
        url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}&units={units}"

        try:
            # Make the API request using certifi for SSL verification
            response = requests.get(url, verify=certifi.where())
            response.raise_for_status()

            # Parse the JSON response
            weather_data = response.json()

            # TODO: Replace with a return Dict of custom results..

            # obtain current forecast - not needed
            forecasts = weather_data['list']

            # Find the closest matching forecast - remove not needed
            closest = self._filter_forecast(forecasts)

            # Convert the timestamp to a datetime object for readability - not needed
            forecast_current = datetime.fromtimestamp(closest['dt'], tz=timezone.utc)

            # review final results - not needed
            print(f"closest forecast time is {forecast_current}: \n{closest}")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


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
