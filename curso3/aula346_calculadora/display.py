# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, no-name-in-module
# pylint: disable=missing-module-docstring, invalid-name
# type: ignore

from constants import (BIG_FONT_SIZE, DEFAULT_MARGIN, MINIMUM_WIDTH,
                       SMALL_FONT_SIZE)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget


class DisplayCalculator(QLineEdit):
    eqPressed = Signal(str)
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    negativePressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [DEFAULT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px; ')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key_ = event.key()
        KEYS = Qt.Key

        isEnter = key_ in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key_ in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key_ in [KEYS.Key_Escape]
        isEmpty = len(text) == 0
        isNumOrDot = text in '.0123456789'
        isOperator = key_ in [
            KEYS.Key_Plus, KEYS.Key_Minus,
            KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P
        ]
        isNegative = key_ in [KEYS.Key_N]

        if isEnter or text == '=':
            # print('Enter Pressed')
            text = '='
            self.eqPressed.emit(text)
            return event.ignore()

        if isDelete:
            # print('Delete Pressed')
            self.delPressed.emit()
            return event.ignore()

        if isEsc or text.lower() == 'c':
            # print('Esc Pressed')
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty:
            # print("Empty")
            return event.ignore()

        if isNumOrDot:
            # print('Input pressed - Text', text)
            self.inputPressed.emit(text)
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            # print('Operator pressed - Text', text)
            self.operatorPressed.emit(text)
            return event.ignore()

        if isNegative:
            # print('Negative Pressed')
            self.negativePressed.emit()
            return event.ignore()

        # print('Text', text, 'len', len(text))

        # return super().keyPressEvent(event)


class InfoLabel(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px; ')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
