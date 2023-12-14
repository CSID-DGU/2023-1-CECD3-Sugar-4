# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_2LVJhWb.ui'
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
import resources_rc

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1040, 600)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -70, 1361, 721))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:white;\n"
"border-radius: 20px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 320, 281, 151))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 160, 281, 151))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(540, 160, 281, 151))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 50, 371, 81))
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(540, 320, 281, 151))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(0, 0, 51, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color:white;\n"
"border-radius: 20px;")
        icon = QIcon()
        icon.addFile(u":/Icon/Help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        self.pushButton.setCheckable(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1040, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc \ud655\uc778 \ubc0f \uc218\uc815", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \uc790\ub3d9 \uc778\uc2dd", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc0d8\ud50c \ubb38\uc11c \ubaa9\ub85d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \ube44\uc2dd\ubcc4\ud654 \uc2dc\uc2a4\ud15c", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc \ub2e4\uc6b4\ub85c\ub4dc", None))
        self.pushButton.setText("")
    # retranslateUi

