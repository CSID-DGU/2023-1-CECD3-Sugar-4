# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_3VMoCtw.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-20, -50, 1141, 641))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:white;")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(170, -30, 16, 621))
        self.line.setStyleSheet(u"color:black;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 510, 71, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton_3.setFont(font1)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(800, 510, 221, 41))
        self.pushButton_4.setFont(font1)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(710, 510, 71, 41))
        self.pushButton_5.setFont(font1)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(590, 510, 101, 41))
        self.pushButton_9.setFont(font1)
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(200, 80, 831, 411))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 44, 111, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_4.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 10, 151, 31))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(-2, 50, 181, 101))
        self.pushButton_8.setFont(font1)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(-2, 148, 181, 101))
        self.pushButton_6.setFont(font1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-2, 246, 181, 101))
        self.pushButton_2.setFont(font1)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(-2, 344, 181, 101))
        self.pushButton_7.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1040, 22))
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
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \uc790\ub3d9 \uc778\uc2dd", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc5c5\ub85c\ub4dc", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sample Image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \uc790\ub3d9 \uc778\uc2dd", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \uc790\ub3d9 \uc778\uc2dd", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc0d8\ud50c \ubb38\uc11c \ubaa9\ub85d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc \ud655\uc778 \ubc0f \uc218\uc815", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc \ub2e4\uc6b4\ub85c\ub4dc", None))
    # retranslateUi

