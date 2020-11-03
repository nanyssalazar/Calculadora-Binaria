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
        MainWindow.resize(461, 553)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: #002030;\n"
"font: 14pt \"Century Gothic\";\n"
"\n"
"\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(143, 151, 174, 255), stop:1 rgba(157, 167, 189, 255));\n"
"border-radius: 8px;\n"
"color: #D9DDDC;\n"
"font-weight: bold;\n"
"color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(151, 160, 183, 255), stop:1 rgba(163, 172, 196, 255))\n"
"}\n"
"\n"
"QPushButton#btn_igual{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(185, 235, 200, 255), stop:1 rgba(193, 236, 207, 255));\n"
"color: black;\n"
"}\n"
"QPushButton#btn_igual:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(185, 235, 200, 255), stop:1 rgba(197, 241, 211, 255));\n"
"}\n"
"QPushButton#btn_modConj{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(199, 204, 237, 255), stop:1 rgba(216, 219, 240, 255));\n"
"font-weight: normal;\n"
"color: black;\n"
"}\n"
"QPushButton#btn_modConj:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(199, 204, 237, 255), stop:1 rgba(216, 219, 240, 255));\n"
"}\n"
"QPushButton#btn_modProp{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(199, 204, 237, 255), stop:1 rgba(216, 219, 240, 255));\n"
"font-weight: normal;\n"
"color: black;\n"
"}\n"
"QPushButton#btn_modProp:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(199, 204, 237, 255), stop:1 rgba(216, 219, 240, 255));\n"
"}\n"
"\n"
"QPushButton#btn_del{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(41, 59, 72, 255), stop:1 rgba(50, 62, 74, 255));\n"
"}\n"
"QPushButton#btn_del:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(41, 59, 71, 255), stop:1 rgba(50, 62, 74, 255));\n"
"}\n"
"QPushButton#btn_ac{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(41, 59, 72, 255), stop:1 rgba(50, 62, 74, 255));\n"
"}\n"
"QPushButton#btn_ac:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(41, 59, 71, 255), stop:1 rgba(50, 62, 74, 255));\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: #F2F3F5;\n"
"border-radius: 8px;\n"
"}\n"
"QPlainTextEdit{\n"
"background-color:#F2F3F5;\n"
"border-radius: 8px;\n"
"}\n"
"QTableWidget{\n"
"background-color: #F2F3F5;\n"
"border-radius: 8px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(20, 440, 201, 41))
        self.btn_del.setObjectName("btn_del")
        self.btn_ac = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ac.setGeometry(QtCore.QRect(239, 440, 201, 41))
        self.btn_ac.setObjectName("btn_ac")
        self.btn_igual = QtWidgets.QPushButton(self.centralwidget)
        self.btn_igual.setGeometry(QtCore.QRect(20, 490, 421, 41))
        self.btn_igual.setObjectName("btn_igual")
        self.operacion = QtWidgets.QLineEdit(self.centralwidget)
        self.operacion.setGeometry(QtCore.QRect(20, 60, 421, 31))
        self.operacion.setText("")
        self.operacion.setAlignment(QtCore.Qt.AlignCenter)
        self.operacion.setObjectName("operacion")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 90, 451, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.proposiciones = QtWidgets.QWidget()
        self.proposiciones.setObjectName("proposiciones")
        self.layoutWidget = QtWidgets.QWidget(self.proposiciones)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 421, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabla = QtWidgets.QTableWidget(self.layoutWidget)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tabla)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_relacional = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_relacional.setEnabled(True)
        self.btn_relacional.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_relacional.setObjectName("btn_relacional")
        self.gridLayout_2.addWidget(self.btn_relacional, 0, 3, 1, 1)
        self.btn_birelaccional = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_birelaccional.setEnabled(True)
        self.btn_birelaccional.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_birelaccional.setObjectName("btn_birelaccional")
        self.gridLayout_2.addWidget(self.btn_birelaccional, 0, 4, 1, 1)
        self.btn_q = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_q.setEnabled(True)
        self.btn_q.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_q.setObjectName("btn_q")
        self.gridLayout_2.addWidget(self.btn_q, 0, 1, 1, 1)
        self.btn_r = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_r.setEnabled(True)
        self.btn_r.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_r.setObjectName("btn_r")
        self.gridLayout_2.addWidget(self.btn_r, 0, 2, 1, 1)
        self.btn_p = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_p.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_p.setObjectName("btn_p")
        self.gridLayout_2.addWidget(self.btn_p, 0, 0, 1, 1)
        self.btn_par2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_par2.setEnabled(True)
        self.btn_par2.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_par2.setObjectName("btn_par2")
        self.gridLayout_2.addWidget(self.btn_par2, 2, 0, 1, 1)
        self.btn_not = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_not.setEnabled(True)
        self.btn_not.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_not.setObjectName("btn_not")
        self.gridLayout_2.addWidget(self.btn_not, 2, 1, 1, 1)
        self.btn_or = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_or.setEnabled(True)
        self.btn_or.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_or.setObjectName("btn_or")
        self.gridLayout_2.addWidget(self.btn_or, 2, 3, 1, 1)
        self.btn_and = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_and.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_and.setObjectName("btn_and")
        self.gridLayout_2.addWidget(self.btn_and, 2, 2, 1, 1)
        self.btn_equiv = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_equiv.setEnabled(True)
        self.btn_equiv.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_equiv.setObjectName("btn_equiv")
        self.gridLayout_2.addWidget(self.btn_equiv, 2, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.proposiciones)
        self.conjuntos = QtWidgets.QWidget()
        self.conjuntos.setObjectName("conjuntos")
        self.layoutWidget1 = QtWidgets.QWidget(self.conjuntos)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 421, 331))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.resultado = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.resultado.setStyleSheet("text-align: center;")
        self.resultado.setReadOnly(True)
        self.resultado.setPlainText("")
        self.resultado.setBackgroundVisible(False)
        self.resultado.setObjectName("resultado")
        self.gridLayout_3.addWidget(self.resultado, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.universo = QtWidgets.QLineEdit(self.layoutWidget1)
        self.universo.setMinimumSize(QtCore.QSize(0, 35))
        self.universo.setText("")
        self.universo.setAlignment(QtCore.Qt.AlignCenter)
        self.universo.setObjectName("universo")
        self.verticalLayout.addWidget(self.universo)
        self.conjA = QtWidgets.QLineEdit(self.layoutWidget1)
        self.conjA.setMinimumSize(QtCore.QSize(0, 35))
        self.conjA.setText("")
        self.conjA.setAlignment(QtCore.Qt.AlignCenter)
        self.conjA.setObjectName("conjA")
        self.verticalLayout.addWidget(self.conjA)
        self.conjB = QtWidgets.QLineEdit(self.layoutWidget1)
        self.conjB.setMinimumSize(QtCore.QSize(0, 35))
        self.conjB.setText("")
        self.conjB.setAlignment(QtCore.Qt.AlignCenter)
        self.conjB.setObjectName("conjB")
        self.verticalLayout.addWidget(self.conjB)
        self.conjC = QtWidgets.QLineEdit(self.layoutWidget1)
        self.conjC.setMinimumSize(QtCore.QSize(0, 35))
        self.conjC.setText("")
        self.conjC.setAlignment(QtCore.Qt.AlignCenter)
        self.conjC.setObjectName("conjC")
        self.verticalLayout.addWidget(self.conjC)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_parentesis = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_parentesis.setMinimumSize(QtCore.QSize(75, 35))
        self.btn_parentesis.setObjectName("btn_parentesis")
        self.gridLayout.addWidget(self.btn_parentesis, 0, 0, 1, 1)
        self.btn_union = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_union.setMinimumSize(QtCore.QSize(75, 35))
        self.btn_union.setObjectName("btn_union")
        self.gridLayout.addWidget(self.btn_union, 0, 1, 1, 1)
        self.btn_conjA = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_conjA.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_conjA.setObjectName("btn_conjA")
        self.gridLayout.addWidget(self.btn_conjA, 1, 0, 1, 1)
        self.btn_interseccion = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_interseccion.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_interseccion.setObjectName("btn_interseccion")
        self.gridLayout.addWidget(self.btn_interseccion, 1, 1, 1, 1)
        self.btn_conjB = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_conjB.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_conjB.setObjectName("btn_conjB")
        self.gridLayout.addWidget(self.btn_conjB, 2, 0, 1, 1)
        self.btn_a = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_a.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_a.setDefault(False)
        self.btn_a.setFlat(False)
        self.btn_a.setObjectName("btn_a")
        self.gridLayout.addWidget(self.btn_a, 2, 1, 1, 1)
        self.btn_conjC = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_conjC.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_conjC.setStyleSheet("")
        self.btn_conjC.setObjectName("btn_conjC")
        self.gridLayout.addWidget(self.btn_conjC, 3, 0, 1, 1)
        self.btn_resta = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_resta.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_resta.setObjectName("btn_resta")
        self.gridLayout.addWidget(self.btn_resta, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.conjuntos)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setGeometry(QtCore.QRect(20, 10, 301, 41))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.mod_conj = QtWidgets.QWidget()
        self.mod_conj.setObjectName("mod_conj")
        self.btn_modConj = QtWidgets.QPushButton(self.mod_conj)
        self.btn_modConj.setGeometry(QtCore.QRect(0, 10, 190, 31))
        self.btn_modConj.setStyleSheet("")
        self.btn_modConj.setObjectName("btn_modConj")
        self.stackedWidget_2.addWidget(self.mod_conj)
        self.mod_prop = QtWidgets.QWidget()
        self.mod_prop.setObjectName("mod_prop")
        self.btn_modProp = QtWidgets.QPushButton(self.mod_prop)
        self.btn_modProp.setGeometry(QtCore.QRect(0, 10, 190, 31))
        self.btn_modProp.setStyleSheet("")
        self.btn_modProp.setObjectName("btn_modProp")
        self.stackedWidget_2.addWidget(self.mod_prop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora Binaria"))
        self.btn_del.setText(_translate("MainWindow", "DEL"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
        self.btn_igual.setText(_translate("MainWindow", "="))
        self.operacion.setPlaceholderText(_translate("MainWindow", "Operación a realizar"))
        self.btn_relacional.setText(_translate("MainWindow", "→"))
        self.btn_birelaccional.setText(_translate("MainWindow", "↔"))
        self.btn_q.setText(_translate("MainWindow", "q"))
        self.btn_r.setText(_translate("MainWindow", "r"))
        self.btn_p.setText(_translate("MainWindow", "p"))
        self.btn_par2.setText(_translate("MainWindow", "(     )"))
        self.btn_not.setText(_translate("MainWindow", "  ¬"))
        self.btn_or.setText(_translate("MainWindow", "v"))
        self.btn_and.setText(_translate("MainWindow", "^"))
        self.btn_equiv.setText(_translate("MainWindow", "≡"))
        self.resultado.setPlaceholderText(_translate("MainWindow", "Resultado"))
        self.universo.setPlaceholderText(_translate("MainWindow", "Universo"))
        self.conjA.setPlaceholderText(_translate("MainWindow", "Valores de A"))
        self.conjB.setPlaceholderText(_translate("MainWindow", "Valores de B"))
        self.conjC.setPlaceholderText(_translate("MainWindow", " Valores de C"))
        self.btn_parentesis.setText(_translate("MainWindow", "(     )"))
        self.btn_union.setText(_translate("MainWindow", "∪"))
        self.btn_conjA.setText(_translate("MainWindow", "A"))
        self.btn_interseccion.setText(_translate("MainWindow", "∩"))
        self.btn_conjB.setText(_translate("MainWindow", "B"))
        self.btn_a.setText(_translate("MainWindow", "Ā"))
        self.btn_conjC.setText(_translate("MainWindow", "C"))
        self.btn_resta.setText(_translate("MainWindow", "-"))
        self.btn_modConj.setText(_translate("MainWindow", "Modo Conjuntos"))
        self.btn_modProp.setText(_translate("MainWindow", "Modo Proposiciones"))

