import logging
import sys
import os

_logger = logging.getLogger(__name__)

class FilemMangerC():

    def __init__(self,loglevel=logging.INFO):
        self._src = []
        self._dst = []
        _logger.setLevel(loglevel)
        _logger.debug("Init: %s",os.path.basename(__file__))

    def SetSrcFolder(self,foldername):
        self._src = foldername


    def SetDstFolder(self,foldername):
        self._dst = foldername

