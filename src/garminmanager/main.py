#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = garminmanager.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed! Ok
"""

import argparse
import sys
import logging
from PyQt5 import QtWidgets

from garminmanager import __version__
import garminmanager.fitparser.FitParserC
import garminmanager.ui
import garminmanager.ui.Version_auto
import garminmanager.ui.MainGui
import garminmanager.utils.FileManagerC

__author__ = "schrma"
__copyright__ = "schrma"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Heatlt viewer for garmin users")
    parser.add_argument(
        '--version',
        action='version',
        version='garminmanager {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s->%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)

    myLevel = args.loglevel
    setup_logging(logging.WARNING)

    #f = garminmanager.utils.FileManagerC.FilemMangerC(myLevel)
    #m = garminmanager.FitParserC.FitParserC(myLevel)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()
    DialogInterface = garminmanager.ui.Version_auto.Ui_Dialog()
    DialogInterface.setupUi(Dialog)
    gui = garminmanager.ui.MainGui.MainWindow(Dialog, DialogInterface)
    gui.setupUi(MainWindow)
    gui.register_signals(MainWindow)
    gui.PrepareApplication()
    MainWindow.show()
    sys.exit(app.exec_())


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
