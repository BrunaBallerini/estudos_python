# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, no-name-in-module
# pylint: disable=missing-module-docstring, invalid-name
# type: ignore

import sys

from constants import LOGO_PATH
from display import DisplayCalculator, InfoLabel
from main_window import ButtonsGrid, MyWindowCalculator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style import setupTheme

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)
    vWindow = MyWindowCalculator()

    # Setting theme
    setupTheme()

    # Defining icon
    icon = QIcon(str(LOGO_PATH))
    vWindow.setWindowIcon(icon)

    # Info label
    infoLabel = InfoLabel('')
    vWindow.addWidgetToVLayout(infoLabel)

    # Display definition
    display = DisplayCalculator()
    display.setPlaceholderText(' ')
    vWindow.addWidgetToVLayout(display)

    # Grid Buttons
    buttonsGrid = ButtonsGrid(display, infoLabel, vWindow)
    vWindow.vLayout.addLayout(buttonsGrid)

    # Developing
    # buttonsGrid.addWidget(Buttons('1'), 1, 0, 1, 0)  # (X, X, X, 1, 0)

    # Execute
    vWindow.adjustFixedSize()
    vWindow.show()
    app.exec()
