import sys
from PySide6 import QtCore, QtGui, QtWidgets
from Vista.ui_Calculadora import Ui_MainWindow
 
class Fernando(QtWidgets.QMainWindow):
    def __init__(self,*args,parent=None):
        super(Fernando,self).__init__(parent)
        self.vent = Ui_MainWindow()
        self.vent.setupUi(self)
        self.vent.BtnSuma.clicked.connect(self.Sumar)
        self.vent.BtnResta.clicked.connect(self.Resta)
        self.vent.BtnMultiplicacion.clicked.connect(self.multiplicacion)
        self.vent.BtnDivision.clicked.connect(self.Division)#self.vent.BtnCerrar.clicked.connect(self.salir)

    def Sumar(self):
        self.vent.Txt_resultado.setText(str(int(self.vent.Txt_1.text()) + int(self.vent.Txt_2.text())))
    def Resta(self):
        self.vent.Txt_resultado.setText(str(int(self.vent.Txt_1.text()) - int(self.vent.Txt_2.text())))
    def multiplicacion(self):
        self.vent.Txt_resultado.setText(str(int(self.vent.Txt_1.text()) * int(self.vent.Txt_2.text())))
    def Division(self):
        self.vent.Txt_resultado.setText(str(int(self.vent.Txt_1.text()) / int(self.vent.Txt_2.text())))
 