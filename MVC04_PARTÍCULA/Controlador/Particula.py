import sys
from PySide6 import QtCore, QtGui, QtWidgets
from Vista.Ui_MainWindow import Ui_MainWindow

class Fernando(QtWidgets.QMainWindow):
    def __init__(self,*args,parent=None):
        super(Fernando,self).__init__(parent)
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.ventana.BtnCerrar.clicked.connect(self.salir)

    def salir(self):
        self.close()



