from PyQt5 import QtWidgets
import UI


setA = set()
setB = set()
setC = set()
setU = set()
set_compA = set()
set_compB = set()
set_compC = set()
set_compABC = set()

remove = ['A', 'B', 'C', '=', '{', '}', 'U']

def conj_a():
    string = ui.conjA.text()
    ui.operacion.setText(ui.operacion.text()+'A')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setA.add(i)


def conj_b():
    string = ui.conjB.text()
    ui.operacion.setText(ui.operacion.text() + 'B')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setB.add(i)
    return True

def conj_c():
    string = ui.conjC.text()
    ui.operacion.setText(ui.operacion.text() + 'C')
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setC.add(i)


def conj_u():
    string = ui.universo.text()
    for i in remove:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        setU.add(i)


def union():
    ui.operacion.setText(ui.operacion.text() + '∪')


def interseccion():
    ui.operacion.setText(ui.operacion.text() + '∩')
    if conj_b():
        conjunto = setA.intersection(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))


def resta():
    ui.operacion.setText(ui.operacion.text() + '-')


def complemento():
    ui.operacion.setText(ui.operacion.text() + "A'")


def resultado():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    if "A∪B" in ui.operacion.text():
        pass
        #conjunto = setA.union(setB)
        #print(conjunto)
        # ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A∪C" in ui.operacion.text():
        conjunto = setA.union(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A∩B" in ui.operacion.text():
        pass
        #conjunto = setA.intersection(setB)
        #print(conjunto)
        #ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A∩C" in ui.operacion.text():
        conjunto = setA.intersection(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(A∪B)∩C" in ui.operacion.text():
        conjunto = setA.union(setB)
        conjunto = conjunto.intersection(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A∪(B∩C)" in ui.operacion.text():
        conjunto = setB.intersection(setC)
        conjunto = conjunto.union(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A∪B∪C" in ui.operacion.text():
        conjunto = setA.union(setB)
        conjunto = conjunto.union(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A-B" in ui.operacion.text():
        conjunto = setA.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A-C" in ui.operacion.text():
        conjunto = setA.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "B-A" in ui.operacion.text():
        conjunto = setB.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "B-C" in ui.operacion.text():
        conjunto = setB.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "C-A" in ui.operacion.text():
        conjunto = setC.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "C-B" in ui.operacion.text():
        conjunto = setC.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(A-B)-C" in ui.operacion.text():
        conjunto = setA.difference(setB)
        conjunto = conjunto.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(A-C)-B" in ui.operacion.text():
        conjunto = setA.difference(setC)
        conjunto = conjunto.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(B-A)-C" in ui.operacion.text():
        conjunto = setB.difference(setA)
        conjunto = conjunto.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(B-C)-A" in ui.operacion.text():
        conjunto = setB.difference(setC)
        conjunto = conjunto.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(C-A)-B" in ui.operacion.text():
        conjunto = setC.difference(setA)
        conjunto = conjunto.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "(C-B)-A" in ui.operacion.text():
        conjunto = setC.difference(setB)
        conjunto = conjunto.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    if "A'" in ui.operacion.text():
        string = ui.conjA.text()
        for i in remove:
            if i in string:
                string = string.replace(i, '')
        for i in string.split(','):
            setA.add(i)
        conj_u()
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
        conj_u()
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
        conj_u()
        set_compC = setU.difference(setC)
        print(str(set_compC))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(set_compC))


def delete():
    string = ui.operacion.text()
    string = string[:-1]
    ui.operacion.setText(string)


def all_clear():
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
    ui.btn_conjA.clicked.connect(conj_a)
    #ui.btn_conjB.clicked.connect(conj_b)
    ui.btn_conjC.clicked.connect(conj_c)

    ui.btn_union.clicked.connect(union)
    ui.btn_interseccion.clicked.connect(interseccion)
    ui.btn_resta.clicked.connect(resta)
    ui.btn_a.clicked.connect(complemento)
    ui.btn_igual.clicked.connect(resultado)

    ui.btn_del.clicked.connect(delete)
    ui.btn_ac.clicked.connect(all_clear)

    main_window.show()
    sys.exit(app.exec_())
