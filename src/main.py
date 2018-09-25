# -*- coding: iso-8859-1 -*-
"""
Created on 10.09.18

@author: Willi Schüler (GNS Systems GmbH)
"""
import os
import configparser
from PySide.QtCore import *
from PySide.QtGui import *
from gui.gui import MainWindow
import sys


def main():
    """
    Main method
    """
    path = os.path.realpath('__file__')
    app = QApplication(sys.argv)
    gui = MainWindow(app)
    gui.win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
