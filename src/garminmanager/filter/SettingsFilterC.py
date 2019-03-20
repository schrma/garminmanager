import logging
import garminmanager.enumerators.EnumFilterTypeC
import os

_logger = logging.getLogger(__name__)

from garminmanager.enumerators.EnumFilterTypeC import EnumFilterTypeC

class SettingsFilterC:

    def __init__(self, loglevel=logging.INFO):
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s", os.path.basename(__file__))
        self.min = 0
        self.max = 250
        self.filter_type =  EnumFilterTypeC.CALC_RANGE