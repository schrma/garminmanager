import logging
import os

_logger = logging.getLogger(__name__)


class FitParserC:

    def __init__(self, loglevel=logging.INFO):
        self._filenameOrFolder = []
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))

    def _get_value_of_first_occurence(self):
        pass
