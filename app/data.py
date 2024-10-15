from typing import List

from app.weather import Weather


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

        # TODO: instead of this being a list it should be a strongly typed object.

        self._vector = List[float]

    @staticmethod
    def prepare_vector(lat, long):  #37.7749, -122.4194
        """
        Prepares model vector.py for model evaluation.

        :return:
        """

        # new weather instance
        w = Weather()
        w.get_weather(lat, long)

        # TODO; let's also make a call to obtain the elevation based on the coordinates.

        # TODO:


    @staticmethod
    def _get_elevation(lat, long):
        pass


