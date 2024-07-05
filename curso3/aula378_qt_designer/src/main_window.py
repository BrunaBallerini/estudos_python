# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, no-name-in-module
# pylint: disable=missing-module-docstring, invalid-name
# type: ignore

import sys

from PySide6.QtCore import QEvent, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.changeLabelName)
        self.lineEdit.installEventFilter(self)

    def changeLabelName(self):
        text = self.lineEdit.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            text = self.lineEdit.text()
            self.labelResult.setText(text + event.text())
        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
