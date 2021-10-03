# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledBjDtRa.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(380, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(27, 27, 27);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.yaziTanima = QPushButton(self.centralwidget)
        self.yaziTanima.setObjectName(u"yaziTanima")
        self.yaziTanima.setGeometry(QRect(-10, 140, 391, 41))
        self.yaziTanima.setStyleSheet(u"background-color: rgb(220, 202, 255);")
        self.nesneTanima = QPushButton(self.centralwidget)
        self.nesneTanima.setObjectName(u"nesneTanima")
        self.nesneTanima.setGeometry(QRect(-10, 250, 391, 41))
        self.nesneTanima.setStyleSheet(u"background-color: rgb(220, 202, 255);")
        self.cinsiyetBelirleme = QPushButton(self.centralwidget)
        self.cinsiyetBelirleme.setObjectName(u"cinsiyetBelirleme")
        self.cinsiyetBelirleme.setGeometry(QRect(-10, 480, 391, 41))
        self.cinsiyetBelirleme.setStyleSheet(u"background-color: rgb(220, 202, 255);")
        self.yasAraligi = QPushButton(self.centralwidget)
        self.yasAraligi.setObjectName(u"yasAraligi")
        self.yasAraligi.setGeometry(QRect(-10, 370, 391, 41))
        self.yasAraligi.setStyleSheet(u"background-color: rgb(220, 202, 255);")
        self.yuzTanima = QPushButton(self.centralwidget)
        self.yuzTanima.setObjectName(u"yuzTanima")
        self.yuzTanima.setGeometry(QRect(-10, 30, 391, 41))
        self.yuzTanima.setStyleSheet(u"background-color: rgb(220, 202, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.yaziTanima.setText(QCoreApplication.translate("MainWindow", u"Yaz\u0131 Tan\u0131ma", None))
        self.nesneTanima.setText(QCoreApplication.translate("MainWindow", u"Nesne Tan\u0131ma", None))
        self.cinsiyetBelirleme.setText(QCoreApplication.translate("MainWindow", u"Cinsiyet Belirleme", None))
        self.yasAraligi.setText(QCoreApplication.translate("MainWindow", u"Ya\u015f Aral\u0131\u011f\u0131", None))
        self.yuzTanima.setText(QCoreApplication.translate("MainWindow", u"Y\u00fcz Tan\u0131ma", None))
    # retranslateUi

