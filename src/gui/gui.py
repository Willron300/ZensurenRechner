import os
import configparser
from PySide.QtCore import *
from PySide.QtGui import *
import sys

class MainWindow:
    """

    """
    def __init__(self, app):
        self.app = app

        self.button_start = QPushButton("Analyse")
        self.vbox = QVBoxLayout()
        self.win = QWidget()
        self.window()
        self.win.setWindowTitle("ZensurenRechner")

    def window(self):
        """
        Generates all layouts
        :return:
        """

        grid_buttons = self.frame_button()

        self.vbox.addSpacing(10)
        self.vbox.addLayout(grid_buttons)

        self.vbox.addStretch()
        self.win.setLayout(self.vbox)

    def frame_button(self):
        def start():
            grid1 = QGridLayout()
            label = QLabel('PLSS')
            grid1.addWidget(label, 0, 0)
            self.vbox.addLayout(grid1)
        grid = QGridLayout()

        self.button_start.clicked.connect(lambda: start())
        grid.addWidget(self.button_start, 0, 0)

        return grid