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
set_conjBC = set()
set_conjABC = set()
set_compA = set()
set_compB = set()
set_compC = set()
set_compABC = set()


def funcion_conjA():
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


def funcion_conjC():
    string = ui.conjC.text()
    ui.operacion.setText(ui.operacion.text() + 'C')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setC.add(i)
    print(setC)

def funcion_conjU():
    string = ui.universo.text()
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
    ui.operacion.setText(ui.operacion.text() + "A'")


def funcion_igual():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    if "A∪B" in ui.operacion.text():
        set_conjABC = setA.union(setB).union(setC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "A∪C" in ui.operacion.text():
        set_conjAC = setA.union(setC)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    elif "A∩B" in ui.operacion.text():
        set_conjAB = setA.intersection(setB)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    elif "A∩C" in ui.operacion.text():
        set_conjAC = setA.intersection(setC)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    elif "(A∪B)∩C" in ui.operacion.text():
        set_conjABC = setA.union(setB)
        set_conjABC = set_conjABC.intersection(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "A∪(B∩C)" in ui.operacion.text():
        set_conjABC = setB.intersection(setC)
        set_conjABC = set_conjABC.union(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "A∪B∪C" in ui.operacion.text():
        set_conjABC = setA.union(setB)
        set_conjABC = set_conjABC.union(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "A-B" in ui.operacion.text():
        set_conjAB = setA.difference(setB)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    elif "A-C" in ui.operacion.text():
        set_conjAC = setA.difference(setC)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    elif "B-A" in ui.operacion.text():
        set_conjAB = setB.difference(setA)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    elif "B-C" in ui.operacion.text():
        set_conjBC = setB.difference(setC)
        print(set_conjBC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjBC))

    elif "C-A" in ui.operacion.text():
        set_conjAC = setC.difference(setA)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    elif "C-B" in ui.operacion.text():
        set_conjBC = setC.difference(setB)
        print(set_conjBC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjBC))

    elif "(A-B)-C" in ui.operacion.text():
        set_conjABC = setA.difference(setB)
        set_conjABC = set_conjABC.difference(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "(A-C)-B" in ui.operacion.text():
        set_conjABC = setA.difference(setC)
        set_conjABC = set_conjABC.difference(setB)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "(B-A)-C" in ui.operacion.text():
        set_conjABC = setB.difference(setA)
        set_conjABC = set_conjABC.difference(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "(B-C)-A" in ui.operacion.text():
        set_conjABC = setB.difference(setC)
        set_conjABC = set_conjABC.difference(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "(C-A)-B" in ui.operacion.text():
        set_conjABC = setC.difference(setA)
        set_conjABC = set_conjABC.difference(setB)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "(C-B)-A" in ui.operacion.text():
        set_conjABC = setC.difference(setB)
        set_conjABC = set_conjABC.difference(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    elif "A'" in ui.operacion.text():
        string = ui.conjA.text()
        for i in remove:
            if i in string:
                string = string.replace(i, '')
        for i in string.split(','):
            setA.add(i)
        funcion_conjU()
        set_compA = setU.difference(setA)
        print(str(set_compA))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_compA))


def funcion_ac():
    setA.clear()
    setB.clear()
    setC.clear()
    setU.clear()
    ui.operacion.clear()
    ui.conjA.clear()
    ui.conjB.clear()
    ui.conjC.clear()
    ui.universo.clear()
    ui.resultado.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(main_window)

    # Aquí van las funciones
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
