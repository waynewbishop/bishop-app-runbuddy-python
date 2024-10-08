import logging
import inspect


class AppLog:
    """
    Implements a centralized logging feature for an entire application.
    Organized as a Singleton design pattern.
    """

    _instance = None
    _user = None
    _logger = None

    def __new__(cls, user):
        """
        Override the new method to implement a Singleton
        design pattern.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user):
        """
        Initialize class variables
        """
        if not self._user:
            self._user = user
            self._setup_logger()

    def _setup_logger(self):
        """
        Set up the logger with a custom format
        """
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)

        # Create a custom format message
        log_format = 'user: %(user)s - time: %(asctime)s - caller module: %(caller_module)s - line no: %(caller_lineno)d - message: %(message)s'
        formatter = logging.Formatter(log_format)

        # Create a file handler (logs to file in current directory)
        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self._logger.addHandler(file_handler)

    def log(self, message: str):
        """
        Log a message with additional information about the caller
        """
        if not self._user:
            self._user = 'Anonymous'

        # Get information about the caller
        frame = inspect.currentframe().f_back
        module = inspect.getmodule(frame)
        module_name = module.__name__ if module else "Unknown"
        line_number = frame.f_lineno

        # Used as extra logging data
        ext_data = {
            'user': self._user,
            'caller_module': module_name,
            'caller_lineno': line_number
        }

        # Log the message with extra data
        self._logger.info(message, extra=ext_data)
