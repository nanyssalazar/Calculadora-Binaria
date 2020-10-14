from PyQt5 import QtWidgets
from PySide2.QtCore import SIGNAL
import UI

remove = ["A", 'B', 'C', '=', '{', '}']

setA = set()
setB = set()
setC = set()
set_conjAB = set()
set_conjAC = set()
set_conjABC = set()

def funcion_conjA():
    #ui.operacion.setText(ui.operacion.text() + ui.btn_conjA.text())
    string = ui.conjA.text()
    ui.operacion.setText(ui.operacion.text()+'A')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setA.add(i)

def funcion_conjB():
    string = ui.conjB.text()
    ui.operacion.setText(ui.operacion.text() + 'B')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setB.add(i)
        #set_conj1 = setA.union(setB)
        #print(set_conj1)

    # string = ui.conjB.text()
    # ui.operacion.setText(ui.operacion.text()+'B')
    # remove = ["A", 'B', 'C', '=', '{', '}']
    # for i in remove:
    #     if i in ui.operacion.text():
    #         string = string.replace(i, '')
    # for i in string.split(','):
    #     setB.add(i)
    # print(setB)

def funcion_conjC():
    string = ui.conjC.text()
    ui.operacion.setText(ui.operacion.text() + 'C')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setC.add(i)
    # if 'UC' in ui.operacion.text():
    #     print(setA.union(setB).union(setC))
    # if "AUB∩C" in ui.operacion.text():
    #     print(setA.union(setB).intersection(setC))


def funcion_union():
    ui.operacion.setText(ui.operacion.text() + ui.btn_union.text())

def funcion_inter():
    ui.operacion.setText(ui.operacion.text() + '∩')

def funcion_igual():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    if "AUB" in ui.operacion.text():
        set_conjAB = setA.union(setB)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    if "AUC" in ui.operacion.text():
        set_conjAC = setA.union(setC)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    if "A∩B" in ui.operacion.text():
        set_conjAB = setA.intersection(setB)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    if "A∩C" in ui.operacion.text():
        set_conjAC = setA.intersection(setC)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    if "(AUB)∩C" in ui.operacion.text():
        set_conjABC = setA.union(setB)
        set_conjABC = set_conjABC.intersection(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "AU(B∩C)" in ui.operacion.text():
        set_conjABC = setB.intersection(setC)
        set_conjABC = set_conjABC.union(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "AUBUC" in ui.operacion.text():
        set_conjABC = setA.union(setB)
        set_conjABC = set_conjABC.union(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))


def funcion_ac():
    setA.clear()
    setB.clear()
    setC.clear()
    set_conjAB.clear()
    set_conjAC.clear()
    set_conjABC.clear()
    ui.operacion.clear()
    ui.conjA.clear()
    ui.conjB.clear()
    ui.conjC.clear()
    ui.resultado.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(main_window)

    # Aquí van las funciones
    #ui.btn_union.clicked.connect(funcion)
    ui.btn_conjA.clicked.connect(funcion_conjA)
    ui.btn_conjB.clicked.connect(funcion_conjB)
    ui.btn_union.clicked.connect(funcion_union)
    ui.btn_igual.clicked.connect(funcion_igual)
    ui.btn_conjC.clicked.connect(funcion_conjC)
    ui.btn_interseccion.clicked.connect(funcion_inter)
    ui.btn_ac.clicked.connect(funcion_ac)

    main_window.show()
    sys.exit(app.exec_())
