from PyQt5 import QtWidgets
from PySide2.QtCore import SIGNAL
import UI

remove = ["A", 'B', 'C', '=', '{', '}', 'U']

setA = set()
setB = set()
setC = set()
setU = set()
set_conjAB = set()
set_conjAC = set()
set_conjABC = set()
set_difAB = set()
set_difAC = set()
set_difBA = set()
set_difBC = set()
set_difCA = set()
set_difCB = set()
set_difABC = set()
set_compA = set()
set_compB = set()
set_compC = set()
set_compABC = set()


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

def funcion_conjU():
    string = ui.universo.text()
    ui.operacion.setText(ui.operacion.text() + 'U')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setU.add(i)


def funcion_union():
    ui.operacion.setText(ui.operacion.text() + ui.btn_union.text())

def funcion_inter():
    ui.operacion.setText(ui.operacion.text() + '∩')

def funcion_resta():
    ui.operacion.setText(ui.operacion.text() + '-')

def funcion_comp():
    ui.operacion.setText(ui.operacion.text() + "'")


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

    if "A-B" in ui.operacion.text():
        set_difAB = setA.difference(setB)
        print(set_difAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difAB))

    if "A-C" in ui.operacion.text():
        set_difAC = setA.difference(setC)
        print(set_difAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difAC))

    if "B-A" in ui.operacion.text():
        set_difBA = setB.difference(setA)
        print(set_difBA)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difBA))

    if "B-C" in ui.operacion.text():
        set_difBC = setB.difference(setC)
        print(set_difBC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difBC))

    if "C-A" in ui.operacion.text():
        set_difCA = setC.difference(setA)
        print(set_difCA)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difCA))

    if "C-B" in ui.operacion.text():
        set_difCB = setC.difference(setB)
        print(set_difCB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difCB))

    if "(A-B)-C" in ui.operacion.text():
        set_difABC = setA.difference(setB)
        set_difABC = set_difABC.difference(setC)
        print(set_difABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difABC))

    if "(A-C)-B" in ui.operacion.text():
        set_difABC = setA.difference(setC)
        set_difABC = set_difABC.difference(setB)
        print(set_difABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difABC))

    if "(B-A)-C" in ui.operacion.text():
        set_difABC = setB.difference(setA)
        set_difABC = set_difABC.difference(setC)
        print(set_difABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difABC))

    if "(B-C)-A" in ui.operacion.text():
        set_difABC = setB.difference(setC)
        set_difABC = set_difABC.difference(setA)
        print(set_difABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difABC))

    if "(C-A)-B" in ui.operacion.text():
        set_difABC = setC.difference(setA)
        set_difABC = set_difABC.difference(setB)
        print(set_difABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difABC))

    if "(C-B)-A" in ui.operacion.text():
        set_difABC = setC.difference(setB)
        set_difABC = set_difABC.difference(setA)
        print(set_difABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_difABC))

    if "A'" in ui.operacion.text():
        set_compA = setU.difference(setA)
        print(str(set_compA))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_compA))

def funcion_ac():
    setA.clear()
    setB.clear()
    setC.clear()
    setU.clear()
    set_conjAB.clear()
    set_conjAC.clear()
    set_conjABC.clear()
    ui.operacion.clear()
    ui.conjA.clear()
    ui.conjB.clear()
    ui.conjC.clear()
    ui.universo.clear()
    ui.resultado.clear()
    set_compA.clear()
    set_compB.clear()
    set_compC.clear()
    set_compABC.clear()
    set_difAB.clear()
    set_difAC.clear()
    set_difBA.clear()
    set_difBC.clear()
    set_difCA.clear()
    set_difCB.clear()
    set_difABC.clear()

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
    ui.btn_resta.clicked.connect(funcion_resta)
    ui.btn_a.clicked.connect(funcion_comp)

    main_window.show()
    sys.exit(app.exec_())
