# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalculadoraNqOtHj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 244)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Txt_1 = QLineEdit(self.centralwidget)
        self.Txt_1.setObjectName(u"Txt_1")
        self.Txt_1.setGeometry(QRect(110, 90, 113, 22))
        self.Txt_2 = QLineEdit(self.centralwidget)
        self.Txt_2.setObjectName(u"Txt_2")
        self.Txt_2.setGeometry(QRect(110, 130, 113, 22))
        self.Txt_resultado = QLineEdit(self.centralwidget)
        self.Txt_resultado.setObjectName(u"Txt_resultado")
        self.Txt_resultado.setEnabled(False)
        self.Txt_resultado.setGeometry(QRect(110, 170, 113, 22))
        self.BtnSuma = QPushButton(self.centralwidget)
        self.BtnSuma.setObjectName(u"BtnSuma")
        self.BtnSuma.setGeometry(QRect(250, 90, 75, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 221, 31))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.BtnResta = QPushButton(self.centralwidget)
        self.BtnResta.setObjectName(u"BtnResta")
        self.BtnResta.setGeometry(QRect(250, 120, 75, 24))
        self.BtnMultiplicacion = QPushButton(self.centralwidget)
        self.BtnMultiplicacion.setObjectName(u"BtnMultiplicacion")
        self.BtnMultiplicacion.setGeometry(QRect(250, 160, 81, 24))
        self.BtnDivision = QPushButton(self.centralwidget)
        self.BtnDivision.setObjectName(u"BtnDivision")
        self.BtnDivision.setGeometry(QRect(250, 190, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BtnSuma.setText(QCoreApplication.translate("MainWindow", u"Suma", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CALCULADORA", None))
        self.BtnResta.setText(QCoreApplication.translate("MainWindow", u"Resta", None))
        self.BtnMultiplicacion.setText(QCoreApplication.translate("MainWindow", u"Multiplicaci\u00f3n", None))
        self.BtnDivision.setText(QCoreApplication.translate("MainWindow", u"Divisi\u00f3n", None))
    # retranslateUi

