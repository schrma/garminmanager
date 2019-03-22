import logging
import os

_logger = logging.getLogger(__name__)


class PlotSettingsC:

    def __init__(self, loglevel=logging.INFO,main_window=[],layout=[]):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self._x_label = "Time"
        self._y_label = "Hearrate"
        self._x_limit = []
        self._y_limit = []
        self._title = []
