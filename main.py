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

def funcion_p():
    ui.operacion.setText(ui.operacion.text() + "p")

def funcion_q():
    ui.operacion.setText(ui.operacion.text() + "q")

def funcion_r():
    ui.operacion.setText(ui.operacion.text() + "r")

def funcion_btnEquiv():
    ui.operacion.setText(ui.operacion.text() + "≡")

def funcion_btnBirrelacional():
    ui.operacion.setText(ui.operacion.text() + "↔")

def funcion_btnRelacional():
    ui.operacion.setText(ui.operacion.text() + "→")

def funcion_btnAnd():
    ui.operacion.setText(ui.operacion.text() + "^")

def funcion_btnOr():
    ui.operacion.setText(ui.operacion.text() + "v")

def funcion_btnNot():
    ui.operacion.setText(ui.operacion.text() + "¬")

def funcion_btnx():
    ui.operacion.setText(ui.operacion.text() + "x")


def funcion_igual():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    if "A∪B" in ui.operacion.text():
        set_conjAB = setA.union(setB)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    if "A∪C" in ui.operacion.text():
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

    if "(A∪B)∩C" in ui.operacion.text():
        set_conjABC = setA.union(setB)
        set_conjABC = set_conjABC.intersection(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "A∪(B∩C)" in ui.operacion.text():
        set_conjABC = setB.intersection(setC)
        set_conjABC = set_conjABC.union(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "A∪B∪C" in ui.operacion.text():
        set_conjABC = setA.union(setB)
        set_conjABC = set_conjABC.union(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "A-B" in ui.operacion.text():
        set_conjAB = setA.difference(setB)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    if "A-C" in ui.operacion.text():
        set_conjAC = setA.difference(setC)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    if "B-A" in ui.operacion.text():
        set_conjAB = setB.difference(setA)
        print(set_conjAB)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAB))

    if "B-C" in ui.operacion.text():
        set_conjBC = setB.difference(setC)
        print(set_conjBC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjBC))

    if "C-A" in ui.operacion.text():
        set_conjAC = setC.difference(setA)
        print(set_conjAC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjAC))

    if "C-B" in ui.operacion.text():
        set_conjBC = setC.difference(setB)
        print(set_conjBC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjBC))

    if "(A-B)-C" in ui.operacion.text():
        set_conjABC = setA.difference(setB)
        set_conjABC = set_conjABC.difference(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "(A-C)-B" in ui.operacion.text():
        set_conjABC = setA.difference(setC)
        set_conjABC = set_conjABC.difference(setB)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "(B-A)-C" in ui.operacion.text():
        set_conjABC = setB.difference(setA)
        set_conjABC = set_conjABC.difference(setC)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "(B-C)-A" in ui.operacion.text():
        set_conjABC = setB.difference(setC)
        set_conjABC = set_conjABC.difference(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "(C-A)-B" in ui.operacion.text():
        set_conjABC = setC.difference(setA)
        set_conjABC = set_conjABC.difference(setB)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "(C-B)-A" in ui.operacion.text():
        set_conjABC = setC.difference(setB)
        set_conjABC = set_conjABC.difference(setA)
        print(set_conjABC)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_conjABC))

    if "A'" in ui.operacion.text():
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

    if "B'" in ui.operacion.text():
        string = ui.conjB.text()
        for i in remove:
            if i in string:
                string = string.replace(i, '')
        for i in string.split(','):
            setB.add(i)
        funcion_conjU()
        set_compB = setU.difference(setB)
        print(str(set_compB))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_compB))

    if "C'" in ui.operacion.text():
        string = ui.conjC.text()
        for i in remove:
            if i in string:
                string = string.replace(i, '')
        for i in string.split(','):
            setC.add(i)
        funcion_conjU()
        set_compC = setU.difference(setC)
        print(str(set_compC))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_compC))

def funcion_del():
    string = ui.operacion.text()
    string = string[:-1]
    ui.operacion.setText(string)


def funcion_ac():
    setA.clear()
    setB.clear()
    setC.clear()
    setU.clear()
    set_conjAB.clear()
    set_conjAC.clear()
    set_conjBC.clear()
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

def funcion_modConj():
    funcion_ac()
    ui.btn_not.setVisible(False)
    ui.btn_and.setVisible(False)
    ui.btn_or.setVisible(False)
    ui.btn_relacional.setVisible(False)
    ui.btn_birelaccional.setVisible(False)
    ui.btn_equiv.setVisible(False)
    ui.btn_q.setVisible(False)
    ui.btn_p.setVisible(False)
    ui.btn_r.setVisible(False)
    ui.tabla.setVisible(False)
    ui.btn_union.setVisible(True)
    ui.btn_interseccion.setVisible(True)
    #a es complemento
    ui.btn_a.setVisible(True)
    ui.btn_resta.setVisible(True)
    ui.resultado.setVisible(True)
    ui.conjA.setVisible(True)
    ui.conjB.setVisible(True)
    ui.conjC.setVisible(True)
    ui.btn_universo.setVisible(True)
    ui.universo.setVisible(True)
    ui.btn_conjA.setVisible(True)
    ui.btn_conjB.setVisible(True)
    ui.btn_conjC.setVisible(True)

def funcion_modProp():
    funcion_ac()
    ui.btn_not.setVisible(True)
    ui.btn_and.setVisible(True)
    ui.btn_or.setVisible(True)
    ui.btn_relacional.setVisible(True)
    ui.btn_birelaccional.setVisible(True)
    ui.btn_equiv.setVisible(True)
    ui.btn_q.setVisible(True)
    ui.btn_p.setVisible(True)
    ui.btn_r.setVisible(True)
    ui.tabla.setVisible(True)
    ui.btn_union.setVisible(False)
    ui.btn_interseccion.setVisible(False)
    # a es complemento
    ui.btn_a.setVisible(False)
    ui.btn_resta.setVisible(False)
    ui.resultado.setVisible(False)
    ui.conjA.setVisible(False)
    ui.conjB.setVisible(False)
    ui.conjC.setVisible(False)
    ui.btn_universo.setVisible(False)
    ui.universo.setVisible(False)
    ui.btn_conjA.setVisible(False)
    ui.btn_conjB.setVisible(False)
    ui.btn_conjC.setVisible(False)


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
    ui.btn_del.clicked.connect(funcion_del)
    ui.btn_modConj.clicked.connect(funcion_modConj)
    ui.btn_modProp.clicked.connect(funcion_modProp)
    ui.btn_p.clicked.connect(funcion_p)
    ui.btn_q.clicked.connect(funcion_q)
    ui.btn_r.clicked.connect(funcion_r)
    ui.btn_equiv.clicked.connect(funcion_btnEquiv)
    ui.btn_birelaccional.clicked.connect(funcion_btnBirrelacional)
    ui.btn_relacional.clicked.connect(funcion_btnRelacional)
    ui.btn_and.clicked.connect(funcion_btnAnd)
    ui.btn_or.clicked.connect(funcion_btnOr)
    ui.btn_not.clicked.connect(funcion_btnNot)
    ui.btn_x.clicked.connect(funcion_btnx)
    main_window.show()
    sys.exit(app.exec_())


