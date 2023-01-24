import sys
from PyQt5 import QtWidgets,uic
qtCreatorFile = 'Principal.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi('Principal.ui',self) #ruta donde esta estar la interfas UI
        self.BtnCerrar.clicked.connect(self.Cerrar)
        self.show() #Muestra la ventana
    
    def Cerrar(self):
        self.close()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()