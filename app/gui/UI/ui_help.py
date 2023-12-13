# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpuGrJhS.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindowhelp(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 515)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-20, -50, 851, 621))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:white;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 211, 21))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(700, 400, 101, 61))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 781, 341))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        self.label_3.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 828, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uadf8\ub7a8 \uc0ac\uc6a9 \uc124\uba85\uc11c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1. Privacy Detection\uc5d0\uc11c \ube44\uc2dd\ubcc4\ud654 \ud560 \uc0d8\ud50c \ubb38\uc11c\ub97c \ub4f1\ub85d\n"
"             -> \uac1c\uc778\uc815\ubcf4 Detection \uc791\uc5c5\uc744 \uc9c4\ud589", None))
    # retranslateUi

