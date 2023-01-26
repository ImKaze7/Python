import sys
from contrasena import generar_contrasena
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'contrasena.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('contrasena.ui',self) #ruta donde esta estar la interfas UI
        self.BtnGenerar.clicked.connect(self.PWD)
        self.show() #Muestra la ventana
    def PWD(self):
        contrasena = generar_contrasena()
        self.TxtContrasena.setText(str(contrasena))


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()