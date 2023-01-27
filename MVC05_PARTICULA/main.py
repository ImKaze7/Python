import sys
from PySide6 import QtCore, QtGui, QtWidgets
from Controlador.calculadora import Fernando


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    venta_Fer = Fernando()
    venta_Fer.show()
    sys.exit(app.exec())
    