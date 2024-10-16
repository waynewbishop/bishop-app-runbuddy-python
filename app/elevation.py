from typing import List, Dict, Any
from logger import AppLog


class Elevation:
    """
    Provides elevation details based on geo-coordinates
    """
    def __init__(self):

        # initialization of JSON dictionary
        self._items: List[Dict[str, Any]] = []

        pass

    def _config(self):
        pass

    def get_elevation(self, lat: float, long: float) -> float | None:
        """
        Obtains elevation from specific coordinates
        :param lat: The supplied latitude
        :param long: The supplied longitude
        :return: Returns the elevation (in meters)
        """

        pass