# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_yuztanimaW(object):
    def setupUi(self, yuztanimaW):
        if yuztanimaW.objectName():
            yuztanimaW.setObjectName(u"yuztanimaW")
        yuztanimaW.resize(400, 300)

        self.retranslateUi(yuztanimaW)

        QMetaObject.connectSlotsByName(yuztanimaW)
    # setupUi

    def retranslateUi(self, yuztanimaW):
        yuztanimaW.setWindowTitle(QCoreApplication.translate("yuztanimaW", u"Form", None))
    # retranslateUi

