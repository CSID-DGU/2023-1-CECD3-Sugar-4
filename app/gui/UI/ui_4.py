# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_4maQXPe.ui'
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

class Ui_MainWindow4(object):
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-1, 60, 171, 91))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-1, 236, 171, 91))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(161, -30, 16, 521))
        self.line.setStyleSheet(u"color:black;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 10, 71, 21))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 430, 61, 31))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(680, 430, 121, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 30, 71, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(180, 50, 641, 371))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(-1, 148, 171, 91))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload Sample Image", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"File Download", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Sample List", None))
    # retranslateUi

