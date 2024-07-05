# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, no-name-in-module
# pylint: disable=missing-module-docstring, invalid-name
# pylint: disable=eval-used
# type: ignore

import math
from typing import TYPE_CHECKING

from constants import MEDIUM_FONT_SIZE
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QGridLayout, QMainWindow, QMessageBox,
                               QPushButton, QVBoxLayout, QWidget)

if TYPE_CHECKING:
    from display import DisplayCalculator, InfoLabel


class MyWindowCalculator(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # Initial configurations
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('Calculator')
        self.vLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.vLayout)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)


class Buttons(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self, display: 'DisplayCalculator',
        info: 'InfoLabel',
        window: MyWindowCalculator,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.display = display
        self.info = info
        self.info.setText('Math operation')
        self.window = window
        self._equation = ''
        self._left = None
        self._right = None
        self._operator = None
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._equal)
        self.display.delPressed.connect(self._delete)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertTextToDisplay)
        self.display.operatorPressed.connect(self._operation)
        self.display.negativePressed.connect(self._negativeNumber)

        for indexRows, rows in enumerate(self._gridMask):
            for indexItem, buttonText in enumerate(rows):
                button = Buttons(buttonText)

                if buttonText not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, indexRows, indexItem)
                slot = self._makeSlot(self._insertTextToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _possibleInt(self, number_: float):
        if number_.is_integer():
            number_ = int(number_)
        return number_

    def isValidNumber(self, string: str):
        valid = False
        try:
            float(string)
            valid = True
        except ValueError:
            valid = False
        return valid

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def inner():
            func(*args, **kwargs)
        return inner

    @Slot()
    def _negativeNumber(self):
        displayValue = self.display.text()

        if not self.isValidNumber(displayValue):
            return

        convertedNumber = float(displayValue) * -1
        newNumber = self._possibleInt(convertedNumber)
        self.display.setText(str(newNumber))
        self.display.setFocus()
        self._left = newNumber

    @Slot()
    def _insertTextToDisplay(self, text):
        # def _insertTextToDisplay(self, button):
        #     buttonText = button.text()
        newDisplayValue = self.display.text() + text
        if not self.isValidNumber(newDisplayValue):
            return
        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self.info.setText('Math operation')
        self._equation = ''
        self._left = None
        self._right = None
        self._operator = None
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _operation(self, text):
        # def _operation(self, button):
        # textButton = button.text()
        displayNow = self.display.text()
        self.display.clear()

        if not self.isValidNumber(displayNow) and self._left is None:
            print('Empty left')
            self._showError("You didn't type anything.")
            return

        if self._left is None:
            isFloat = float(displayNow)
            isIntFloat = self._possibleInt(isFloat)
            self._left = isIntFloat
            self.display.setFocus()

        self._operator = text
        self.equation = f'{self._left} {self._operator} ?'
        self.display.setFocus()

    @Slot()
    def _equal(self):
        # def _equal(self, button):
        # textButton = button.text()
        displayNow = self.display.text()
        self.display.clear()
        self.display.setFocus()

        if not self.isValidNumber(displayNow) and self._right is None \
                or self._left is None:
            # print('Empty right')
            self._showError('Incomplete sentence.')
            return

        if self._right is None:
            isFloat = float(displayNow)
            isIntFloat = self._possibleInt(isFloat)
            self._right = isIntFloat

        self.equation = f'{self._left} {self._operator} {self._right}'

        try:
            if self._operator == '^' and self._left is not None:
                result = round(math.pow(self._left, self._right), 7)
            else:
                result = round(eval(self.equation), 7)

            self.display.setText(str(result))
            self._left = result

        except ZeroDivisionError:
            self._equation = ''
            self.display.setText('Zero division error')
            self.display.setFocus()
            # self._showError('Zero division')
            self._left = None

        except OverflowError:
            self.display.setText('Capacity Overflow')
            self.display.setFocus()
            # self._showError('Capacity Overflow')
            self._equation = ''
            self._left = None

        except SyntaxError:
            self._showError('Syntax Error')
            self._clear()

        self._right = None
        self.display.setFocus()

    @Slot()
    def _delete(self):
        self.display.backspace()
        self.display.setFocus()

    def _configSpecialButton(self, button):
        textButtonSpecial = button.text()

        if textButtonSpecial in '+-*/^':
            slot = self._makeSlot(self._operation, textButtonSpecial)
            self._connectButtonClicked(button, slot)

        if textButtonSpecial == '=':
            # slot = self._makeSlot(self._equal, button)
            slot = self._makeSlot(self._equal)
            self._connectButtonClicked(button, slot)

        if textButtonSpecial == 'C':
            slot = self._makeSlot(self._clear)
            self._connectButtonClicked(button, slot)

        if textButtonSpecial == '◀':
            slot = self._makeSlot(self._delete)
            self._connectButtonClicked(button, slot)

        if textButtonSpecial == 'N':
            slot = self._makeSlot(self._negativeNumber)
            self._connectButtonClicked(button, slot)

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(msgBox.StandardButton.Cancel)
        # msgBox.button(msgBox.StandardButton.Cancel).setText('other language')
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()

    # Developing
    # def _insertTextToDisplay(self, button):
    # buttonText = button.text()
    # self.display.insert(buttonText)
    # newDisplayValue = self.display.text() + buttonText
    # newDisplayValue = (self.display.text() + buttonText)  # [:-1]
    # if not self.isValidNumber(newDisplayValue):
        # newDisplayValue = self.display.text()[:-1]
        # print(f'If {newDisplayValue=}')
        # self.display.setText(newDisplayValue)
        # return
    # self.display.insert(buttonText)
    # newDisplayValue = self.display.text()[:-1]
    # print(f'Else {newDisplayValue=}')
    # self.display.setText(newDisplayValue)

    # print(grid_mask)
    # for index_lines, lines in enumerate(grid_mask):
    #     print(lines)
    #     for index_item, item in enumerate(lines):
    #         print(item, index_lines, index_item)

    # @Slot()
    # def slot_1(status_bar_):
    #     def inner():
    #         status_bar_.showMessage('text')
    #     return inner
    # (slot_1(status_bar))
    # @Slot()
    # def _insertButtonTextToDisplay(self, text: str):
    #     def inner(checked):
    #         self.display.insert(text)
    #         print(text, checked)
    #     return inner

    # new = ''
    # for j in range(5):
    #     text_ = input(':')
    #     new += text_
    #     try:
    #         float(new)
    #         print(new)
    #     except ValueError:
    #         print('Not included')
    #         new = new[:-1]
    #     print(new)

    # Another resolution
    #             if buttonText not in '0123456789.':
    #                 button.setProperty('cssClass', 'specialButton')
    #                 self._configSpecialButton(button)

    #             self.addWidget(button, indexRows, indexItem)
    #             slot = self._insertButtonTextToDisplay(button)
    #             self._connectButtonClicked(button, slot)

    # @Slot()
    # def _insertButtonTextToDisplay(self, button):
    #     def inner():
    #         buttonText = button.text()
    #         self.display.insert(buttonText)
    #         newDisplayValue = (self.display.text() + buttonText)[:-1]
    #         print(f'try {newDisplayValue=}')
    #         try:
    #             float(newDisplayValue)
    #         except ValueError:
    #             newDisplayValue = self.display.text()[:-1]
    #             print(f'except {newDisplayValue=}')
    #             self.display.setText(newDisplayValue)
    #     return inner

    # def _connectButtonClicked(self, button, slot):
    #     button.clicked.connect(slot)

    # def _configSpecialButton(self, button):
    #     textButtonSpecial = button.text()
    #     print(f'Text: {textButtonSpecial}')
    #     if textButtonSpecial == 'C':
    #         print('C')

    # def _equal(self, button):
    #     textButton = button.text()
    #     print(textButton)
    #     displayNow = self.display.text()
    #     print(textButton, displayNow)
    #     self.display.clear()

    #     if not self.isValidNumber(displayNow) and self._right is None:
    #         print('Empty right')
    #         self._showError('Incomplete sentence.')
    #         return

    #     if self._right is None:
    #         self._right = float(displayNow)

    #     self.equation = f'{self._left} {self._operator} {self._right}'
    #     # result = 0.0

    #     try:
    #         if self._operator == '^' and self._left is not None:
    #             result = round(math.pow(self._left, self._right), 5)
    #             # result = self._left ** self._right
    #             # result = eval(self.equation.replace('^', '**'))
    #         else:
    #             result = round(eval(self.equation), 5)

    #         self.display.setText(str(result))
    #         self._left = result

    #     except ZeroDivisionError:
    #         self._equation = ''
    #         self.display.setText('Zero division error')
    #         # self._showError('Zero division')
    #         self._left = None

    #     except OverflowError:
    #         self.display.setText('Capacity Overflow')
    #         # self._showError('Capacity Overflow')
    #         self._equation = ''
    #         self._left = None

    #     except SyntaxError:
    #         self._showError('Syntax Error')
    #         self._clear()

    #     self._right = None

    #     # self.display.setText(str(result))
    #     # if self._operator is None:
    #     #     print('Wrong number inserted')
    #     #     self._clear()
    #     #     return
    #     # self._left = result
    #     # self._operator = None

    # def _eqPressed(self, *args):
    #     print(f'{args} received')
