import sys

from PySide6 import QtCore,QtGui,QtWidgets

import ui_main
import ui_yuztanima
import TextRecog

class YuzTanimaWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui=ui_yuztanima.Ui_yuztanimaW()
        self.ui.setupUi(self)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setFixedSize(380,600)
        self.ui = ui_main.Ui_MainWindow()

        self.yuzTanimaWidget=YuzTanimaWidget()
        self.yuzTanimaWidget.hide()

        self.ui.setupUi(self)
        self.ui.yaziTanima.clicked.connect(self.yaziTanima)
        self.ui.yuzTanima.clicked.connect(self.yuzTanima)
        self.ui.nesneTanima.clicked.connect(self.nesneTanima)
        self.ui.yasAraligi.clicked.connect(self.yasAraligi)
        self.ui.cinsiyetBelirleme.clicked.connect(self.cinsiyetBelirleme)


    def yaziTanima(self):
        if self.yuzTanimaWidget.isHidden():
            self.yuzTanimaWidget.show()
            TextRecog.TextRecognation()
        else:
            self.yuzTanimaWidget.hide()

    def yuzTanima(self):
        if self.yuzTanimaWidget.isHidden():
            self.yuzTanimaWidget.show()
        else:
            self.yuzTanimaWidget.hide()

    def nesneTanima(self):
        if self.yuzTanimaWidget.isHidden():
            self.yuzTanimaWidget.show()
        else:
            self.yuzTanimaWidget.hide()

    def yasAraligi(self):
        if self.yuzTanimaWidget.isHidden():
            self.yuzTanimaWidget.show()
        else:
            self.yuzTanimaWidget.hide()

    def cinsiyetBelirleme(self):
        if self.yuzTanimaWidget.isHidden():
            self.yuzTanimaWidget.show()
        else:
            self.yuzTanimaWidget.hide()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    x=MainWindow()
    x.show()
    app.exec()

