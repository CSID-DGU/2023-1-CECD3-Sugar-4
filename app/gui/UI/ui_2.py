# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_2rfiFEz.ui'
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

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 514)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -70, 851, 621))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:white;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 120, 271, 141))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 270, 271, 141))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 120, 271, 141))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(150, 270, 271, 141))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"background-color:rgb(35, 39, 36);\n"
"color:white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 30, 321, 61))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_3.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 828, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload Sample Image", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Privacy Detection", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Sample List", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \ube44\uc2dd\ubcc4\ud654 \uc2dc\uc2a4\ud15c", None))
    # retranslateUi

