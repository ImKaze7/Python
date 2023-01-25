import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'Calculadora.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('Calculadora.ui',self) #ruta donde esta estar la interfas UI
        self.BtnSuma.clicked.connect(self.Sumar)
        self.BtnResta.clicked.connect(self.resta)
        self.BtnMultiplicacion.clicked.connect(self.multiplicacion)

        self.BtnDivision.clicked.connect(self.Division)
        self.show() #Muestra la ventana
    def Sumar(self):
        #calcular
        #numero1 = float(self.Txt_1.text())
        #numero2 = float(self.Txt_2.text())
        #resultado = numero1 + numero2
        #self.Txt_resultado.setText(str(resultado))

        self.Txt_resultado.setText(str(int(self.Txt_1.text()) + int(self.Txt_2.text())))
    def resta(self):
        self.Txt_resultado.setText(str(int(self.Txt_1.text()) - int(self.Txt_2.text())))

    def multiplicacion(self):
        self.Txt_resultado.setText(str(int(self.Txt_1.text()) * int(self.Txt_2.text())))

    def Division(self):
        self.Txt_resultado.setText(str(int(self.Txt_1.text()) / int(self.Txt_2.text())))

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()