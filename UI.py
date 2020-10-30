# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(463, 548)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: #1D2226;\n"
"font: 14pt \"Century Gothic\";\n"
"\n"
"\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"background-color: #5A7E85;\n"
"border-radius: 8px;\n"
"color: #D9DDDC;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton#btn_igual{\n"
"background-color: #8BA629;\n"
"}\n"
"QPushButton#btn_modConj{\n"
"background-color: #86898E;\n"
"font-weight: normal;\n"
"}\n"
"QPushButton#btn_modProp{\n"
"background-color: #86898E;\n"
"font-weight: normal;\n"
"}\n"
"QPushButton#btn_del{\n"
"background-color: #9ABBCE;\n"
"}\n"
"QPushButton#btn_ac{\n"
"background-color: #9ABBCE;\n"
"}\n"
"QPushButton#btn_mo{\n"
"background-color: #9ABBCE;\n"
"}\n"
"QPushButton#btn_ac{\n"
"background-color: #9ABBCE;\n"
"}\n"
"QLineEdit{\n"
"background-color: #D9DDDC;\n"
"border-radius: 8px;\n"
"}\n"
"QPlainTextEdit{\n"
"background-color: #D9DDDC;\n"
"border-radius: 8px;\n"
"}\n"
"QTableWidget{\n"
"background-color: #D9DDDC;\n"
"border-radius: 8px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(20, 440, 201, 41))
        self.btn_del.setObjectName("btn_del")
        self.btn_ac = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ac.setGeometry(QtCore.QRect(239, 440, 201, 41))
        self.btn_ac.setObjectName("btn_ac")
        self.btn_union = QtWidgets.QPushButton(self.centralwidget)
        self.btn_union.setGeometry(QtCore.QRect(370, 240, 71, 41))
        self.btn_union.setObjectName("btn_union")
        self.btn_interseccion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_interseccion.setGeometry(QtCore.QRect(370, 290, 71, 41))
        self.btn_interseccion.setObjectName("btn_interseccion")
        self.btn_a = QtWidgets.QPushButton(self.centralwidget)
        self.btn_a.setGeometry(QtCore.QRect(370, 340, 71, 41))
        self.btn_a.setDefault(False)
        self.btn_a.setFlat(False)
        self.btn_a.setObjectName("btn_a")
        self.btn_resta = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resta.setGeometry(QtCore.QRect(370, 390, 71, 41))
        self.btn_resta.setObjectName("btn_resta")
        self.btn_not = QtWidgets.QPushButton(self.centralwidget)
        self.btn_not.setEnabled(True)
        self.btn_not.setGeometry(QtCore.QRect(195, 390, 71, 41))
        self.btn_not.setObjectName("btn_not")
        self.btn_and = QtWidgets.QPushButton(self.centralwidget)
        self.btn_and.setGeometry(QtCore.QRect(20, 390, 71, 41))
        self.btn_and.setObjectName("btn_and")
        self.btn_x = QtWidgets.QPushButton(self.centralwidget)
        self.btn_x.setEnabled(True)
        self.btn_x.setGeometry(QtCore.QRect(284, 390, 71, 41))
        self.btn_x.setObjectName("btn_x")
        self.btn_or = QtWidgets.QPushButton(self.centralwidget)
        self.btn_or.setEnabled(True)
        self.btn_or.setGeometry(QtCore.QRect(108, 390, 71, 41))
        self.btn_or.setObjectName("btn_or")
        self.btn_relacional = QtWidgets.QPushButton(self.centralwidget)
        self.btn_relacional.setEnabled(True)
        self.btn_relacional.setGeometry(QtCore.QRect(284, 340, 71, 41))
        self.btn_relacional.setObjectName("btn_relacional")
        self.btn_birelaccional = QtWidgets.QPushButton(self.centralwidget)
        self.btn_birelaccional.setEnabled(True)
        self.btn_birelaccional.setGeometry(QtCore.QRect(370, 340, 71, 41))
        self.btn_birelaccional.setObjectName("btn_birelaccional")
        self.btn_equiv = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equiv.setEnabled(True)
        self.btn_equiv.setGeometry(QtCore.QRect(370, 390, 71, 41))
        self.btn_equiv.setObjectName("btn_equiv")
        self.btn_conjB = QtWidgets.QPushButton(self.centralwidget)
        self.btn_conjB.setGeometry(QtCore.QRect(284, 340, 71, 41))
        self.btn_conjB.setObjectName("btn_conjB")
        self.btn_conjA = QtWidgets.QPushButton(self.centralwidget)
        self.btn_conjA.setGeometry(QtCore.QRect(284, 290, 71, 41))
        self.btn_conjA.setObjectName("btn_conjA")
        self.btn_conjC = QtWidgets.QPushButton(self.centralwidget)
        self.btn_conjC.setGeometry(QtCore.QRect(284, 390, 71, 41))
        self.btn_conjC.setStyleSheet("")
        self.btn_conjC.setObjectName("btn_conjC")
        self.btn_igual = QtWidgets.QPushButton(self.centralwidget)
        self.btn_igual.setGeometry(QtCore.QRect(20, 490, 421, 41))
        self.btn_igual.setObjectName("btn_igual")
        self.btn_q = QtWidgets.QPushButton(self.centralwidget)
        self.btn_q.setEnabled(True)
        self.btn_q.setGeometry(QtCore.QRect(108, 340, 71, 41))
        self.btn_q.setObjectName("btn_q")
        self.btn_p = QtWidgets.QPushButton(self.centralwidget)
        self.btn_p.setGeometry(QtCore.QRect(20, 340, 71, 41))
        self.btn_p.setObjectName("btn_p")
        self.btn_r = QtWidgets.QPushButton(self.centralwidget)
        self.btn_r.setEnabled(True)
        self.btn_r.setGeometry(QtCore.QRect(195, 340, 71, 41))
        self.btn_r.setObjectName("btn_r")
        self.resultado = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(20, 90, 421, 131))
        self.resultado.setStyleSheet("")
        self.resultado.setReadOnly(True)
        self.resultado.setPlainText("")
        self.resultado.setBackgroundVisible(False)
        self.resultado.setObjectName("resultado")
        self.operacion = QtWidgets.QLineEdit(self.centralwidget)
        self.operacion.setGeometry(QtCore.QRect(20, 50, 421, 31))
        self.operacion.setText("")
        self.operacion.setAlignment(QtCore.Qt.AlignCenter)
        self.operacion.setObjectName("operacion")
        self.conjA = QtWidgets.QLineEdit(self.centralwidget)
        self.conjA.setGeometry(QtCore.QRect(20, 290, 250, 41))
        self.conjA.setText("")
        self.conjA.setAlignment(QtCore.Qt.AlignCenter)
        self.conjA.setObjectName("conjA")
        self.conjB = QtWidgets.QLineEdit(self.centralwidget)
        self.conjB.setGeometry(QtCore.QRect(20, 340, 250, 41))
        self.conjB.setText("")
        self.conjB.setAlignment(QtCore.Qt.AlignCenter)
        self.conjB.setObjectName("conjB")
        self.conjC = QtWidgets.QLineEdit(self.centralwidget)
        self.conjC.setGeometry(QtCore.QRect(20, 390, 250, 41))
        self.conjC.setText("")
        self.conjC.setAlignment(QtCore.Qt.AlignCenter)
        self.conjC.setObjectName("conjC")
        self.btn_universo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_universo.setGeometry(QtCore.QRect(284, 240, 71, 41))
        self.btn_universo.setObjectName("btn_universo")
        self.universo = QtWidgets.QLineEdit(self.centralwidget)
        self.universo.setGeometry(QtCore.QRect(20, 240, 251, 41))
        self.universo.setText("")
        self.universo.setAlignment(QtCore.Qt.AlignCenter)
        self.universo.setObjectName("universo")
        self.btn_modConj = QtWidgets.QPushButton(self.centralwidget)
        self.btn_modConj.setGeometry(QtCore.QRect(20, 10, 190, 31))
        self.btn_modConj.setStyleSheet("")
        self.btn_modConj.setObjectName("btn_modConj")
        self.btn_modProp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_modProp.setGeometry(QtCore.QRect(250, 10, 190, 31))
        self.btn_modProp.setStyleSheet("")
        self.btn_modProp.setObjectName("btn_modProp")
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(20, 90, 421, 241))
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora Binaria"))
        self.btn_del.setText(_translate("MainWindow", "DEL"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
        self.btn_union.setText(_translate("MainWindow", "∪"))
        self.btn_interseccion.setText(_translate("MainWindow", "∩"))
        self.btn_a.setText(_translate("MainWindow", "Ā"))
        self.btn_resta.setText(_translate("MainWindow", "-"))
        self.btn_not.setText(_translate("MainWindow", "  ¬"))
        self.btn_and.setText(_translate("MainWindow", "^"))
        self.btn_x.setText(_translate("MainWindow", "x"))
        self.btn_or.setText(_translate("MainWindow", "v"))
        self.btn_relacional.setText(_translate("MainWindow", "→"))
        self.btn_birelaccional.setText(_translate("MainWindow", "↔"))
        self.btn_equiv.setText(_translate("MainWindow", "≡"))
        self.btn_conjB.setText(_translate("MainWindow", "B"))
        self.btn_conjA.setText(_translate("MainWindow", "A"))
        self.btn_conjC.setText(_translate("MainWindow", "C"))
        self.btn_igual.setText(_translate("MainWindow", "="))
        self.btn_q.setText(_translate("MainWindow", "q"))
        self.btn_p.setText(_translate("MainWindow", "p"))
        self.btn_r.setText(_translate("MainWindow", "r"))
        self.resultado.setPlaceholderText(_translate("MainWindow", "Resultado"))
        self.operacion.setPlaceholderText(_translate("MainWindow", "Operación a realizar"))
        self.conjA.setPlaceholderText(_translate("MainWindow", "Valores de A"))
        self.conjB.setPlaceholderText(_translate("MainWindow", "Valores de B"))
        self.conjC.setPlaceholderText(_translate("MainWindow", " Valores de C"))
        self.btn_universo.setText(_translate("MainWindow", "U"))
        self.universo.setPlaceholderText(_translate("MainWindow", "Universo"))
        self.btn_modConj.setText(_translate("MainWindow", "Modo Conjuntos"))
        self.btn_modProp.setText(_translate("MainWindow", "Modo Proposiciones"))

