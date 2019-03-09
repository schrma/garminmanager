import pytest
import os
import logging

import garminmanager
import garminmanager.utils
import garminmanager.utils.FileManagerC

__author__ = "marco"
__copyright__ = "copyMarco"
__license__ = "mit"




def test_SetSrcFolder():
    srcFolder = os.getcwd()
    print(srcFolder)
    sc = garminmanager.utils.FileManagerC.FilemMangerC(loglevel=logging.DEBUG)
    sc.SetSrcFolder(srcFolder)
    assert srcFolder == sc._src

def test_SetDstFolder():
    srcFolder = os.getcwd()
    print(srcFolder)
    sc = garminmanager.utils.FileManagerC.FilemMangerC()
    sc.SetDstFolder(srcFolder)
    assert srcFolder == sc._dst