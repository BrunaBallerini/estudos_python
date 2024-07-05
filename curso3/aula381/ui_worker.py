# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worker.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1064, 907)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1011, 841))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.gridLayoutWidget)
        self.label1.setObjectName(u"label1")
        font = QFont()
        font.setPointSize(40)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.label2 = QLabel(self.gridLayoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)

        self.button1 = QPushButton(self.gridLayoutWidget)
        self.button1.setObjectName(u"button1")
        self.button1.setFont(font)

        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)

        self.button2 = QPushButton(self.gridLayoutWidget)
        self.button2.setObjectName(u"button2")
        self.button2.setFont(font)

        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1064, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"L1", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"L2", None))
        self.button1.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"B2", None))
    # retranslateUi

