from PyQt5 import QtWidgets
import UI

setA = set()
setB = set()
setC = set()
setU = set()


quitar = ["A", 'B', 'C', '=', '{', '}', 'U']


# Node class
class Nodo:
    # Function to initialise the node object
    def __init__(self, cont):
        self.cont = cont  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.ini = None
        self.fin = None


list = LinkedList()


def crear_conjunto(string, conjunto):
    for i in quitar:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        conjunto.add(i)


def conj_a():
    crear_conjunto(str(ui.conjA.text()), setA)
    ui.operacion.setText(ui.operacion.text() + 'A')


def conj_b():
    crear_conjunto(str(ui.conjB.text()), setB)
    ui.operacion.setText(ui.operacion.text() + 'B')


def conj_c():
    crear_conjunto(str(ui.conjC.text()), setC)
    ui.operacion.setText(ui.operacion.text() + 'C')


def conj_u():
    crear_conjunto(str(ui.universo.text()), setU)


def union():
    ui.operacion.setText(ui.operacion.text() + '∪')


def interseccion():
    ui.operacion.setText(ui.operacion.text() + '∩')


def resta():
    ui.operacion.setText(ui.operacion.text() + '-')


def complemento():
    ui.operacion.setText(ui.operacion.text() + "'")


def btn_p():
    ui.operacion.setText(ui.operacion.text() + "p")


def btn_q():
    ui.operacion.setText(ui.operacion.text() + "q")


def btn_r():
    ui.operacion.setText(ui.operacion.text() + "r")


def equivalencia():
    ui.operacion.setText(ui.operacion.text() + "≡")


def birrelacional():
    ui.operacion.setText(ui.operacion.text() + "↔")


def relacional():
    ui.operacion.setText(ui.operacion.text() + "→")


def btn_and():
    ui.operacion.setText(ui.operacion.text() + "^")


def btn_or():
    ui.operacion.setText(ui.operacion.text() + "v")


def btn_not():
    ui.operacion.setText(ui.operacion.text() + "¬")


def btn_x():
    ui.operacion.setText(ui.operacion.text() + "x")


def formar_lista():
    string = ui.operacion.text()
    print(string)
    for i in string:
        # print(i)
        temp = Nodo(i)
        if list.ini is None:
            list.ini = temp
            list.fin = temp
        else:
            list.fin.next = temp
            list.fin = temp
    temp = list.ini
    while temp is not None:
        print(temp.cont, end=" ")
        temp = temp.next

def resolver():
    global parentesis1, parentesis2
    conjunto_final = ()
    conjuntos = {"A", "B", "C", "U"}
    operaciones = {"∪","∩","-"}
    #saber conj A
    dic1 = {"A": setA, "B": setB, "C": setC, "U": setU}
    op = False
    temp = parentesis1
    signo = ""
    conj1 = ""
    conj2 = ""
    while temp != parentesis2:
        if temp.cont in conjuntos:
            conj1 = temp.cont
            print("3")
            """if temp.next.cont == "'":
                conj_u()
                conjunto_final = setU.difference(dic1.get(conj1))
                # borrar nodo con '
                # borrar nodo con F --conj final
                temp = parentesis1.next
                break"""
        if temp.cont in operaciones:
            signo = temp.cont
            op = True
            print("4")
        if temp.cont in conjuntos and op:
            conj2 = temp.cont
            print("5")
            """if temp.next.cont == "'":
                conj_u()
                conjunto_final = setU.difference(dic1.get(conj2))
                # borrar nodo con '
                # borrar nodo con F --conj final
                break"""
        temp = temp.next
    if op:
        if signo == "∪":
            print(dic1.get(conj1))
            conjunto_final = dic1.get(conj1).union(dic1.get(conj2))
            print("6")
        elif signo == "∩":
            conjunto_final = dic1.get(conj1).intersection(dic1.get(conj2))
            print("6")
        elif signo == "-":
            conjunto_final = dic1.get(conj1).difference(dic1.get(conj2))
            print("6")
    print(conjunto_final)
    borrar = parentesis1
    list.ini = parentesis1.next
    borrar.next = None
    borrar = list.ini
    while borrar.cont != ")":
        """if temp == ")":
            found = True
            break"""
        temp = borrar
        borrar = borrar.next
    temp.next = borrar.next
    borrar.next = None
    temp = list.ini
    while temp is not None:
        print(temp.cont, end=" ")
        temp = temp.next


    #ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto_final))

    #saber operacion
    #saber conj B
    #borrar par (
    #borrar par )

def resultado():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    formar_lista()  # funcion para meter all string en lista
    found = True
    global parentesis1, parentesis2
    while found:
        temp = list.ini
        while temp is not None:
            if temp.cont == "(":
                parentesis1 = temp
                print("1")
            if temp.cont == ")":
                print("2")
                parentesis2 = temp
                resolver()
                break
            temp = temp.next

        temp = list.ini
        while temp is not None:
            if (temp.cont == "(") or (temp.cont == ")"):
                found = True
            temp = temp.next
        if temp == "=":
            found = False

    """string = ui.operacion.text()
    string2 = string
    x = len(string2)
    while x != 1:
        found = False
        string3 = ""
        ini = 0
        print(string2)
        for i in range(len(string2)):
            if string2[i] == "(":
                ini = i
                found = True
                continue
            if string2[i] == i == ")":
                fin = i
                string2 = string2[:ini] + string2[fin:-2]
                break
            if found:
                string3 = string3 + string2[i]
                print(string2)
                print(string3)
            x = 1"""

    """if "A∪B" in ui.operacion.text():
        conjunto = setA.union(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A∪C" in ui.operacion.text():
        conjunto = setA.union(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A∩B" in ui.operacion.text():
        conjunto = setA.intersection(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A∩C" in ui.operacion.text():
        conjunto = setA.intersection(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(A∪B)∩C" in ui.operacion.text():
        conjunto = setA.union(setB)
        conjunto = conjunto.intersection(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A∪(B∩C)" in ui.operacion.text():
        conjunto = setB.intersection(setC)
        conjunto = conjunto.union(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A∪B∪C" in ui.operacion.text():
        conjunto = setA.union(setB)
        conjunto = conjunto.union(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A-B" in ui.operacion.text():
        conjunto = setA.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A-C" in ui.operacion.text():
        conjunto = setA.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "B-A" in ui.operacion.text():
        conjunto = setB.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "B-C" in ui.operacion.text():
        conjunto = setB.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "C-A" in ui.operacion.text():
        conjunto = setC.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "C-B" in ui.operacion.text():
        conjunto = setC.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(A-B)-C" in ui.operacion.text():
        conjunto = setA.difference(setB)
        conjunto = conjunto.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(A-C)-B" in ui.operacion.text():
        conjunto = setA.difference(setC)
        conjunto = conjunto.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(B-A)-C" in ui.operacion.text():
        conjunto = setB.difference(setA)
        conjunto = conjunto.difference(setC)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(B-C)-A" in ui.operacion.text():
        conjunto = setB.difference(setC)
        conjunto = conjunto.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(C-A)-B" in ui.operacion.text():
        conjunto = setC.difference(setA)
        conjunto = conjunto.difference(setB)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "(C-B)-A" in ui.operacion.text():
        conjunto = setC.difference(setB)
        conjunto = conjunto.difference(setA)
        print(conjunto)
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "A'" in ui.operacion.text():
        crear_conjunto(str(ui.conjA.text()), setA)
        conj_u()
        conjunto = setU.difference(setA)
        print(str(conjunto))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "B'" in ui.operacion.text():
        crear_conjunto(str(ui.conjB.text()), setB)
        conj_u()
        conjunto = setU.difference(setB)
        print(str(set_compB))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    elif "C'" in ui.operacion.text():
        crear_conjunto(str(ui.conjC.text()), setC)
        conj_u()
        conjunto = setU.difference(setC)
        print(str(set_compC))
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))"""


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


def modo_conj():
    all_clear()
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
    # a es complemento
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


def modo_prop():
    all_clear()
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
    # Mostrar primera configuracion
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

    # Aquí van las funciones
    # ui.btn_union.clicked.connect(funcion)
    ui.btn_conjA.clicked.connect(conj_a)
    ui.btn_conjB.clicked.connect(conj_b)
    ui.btn_union.clicked.connect(union)
    ui.btn_igual.clicked.connect(resultado)
    ui.btn_conjC.clicked.connect(conj_c)
    ui.btn_interseccion.clicked.connect(interseccion)
    ui.btn_ac.clicked.connect(all_clear)
    ui.btn_resta.clicked.connect(resta)
    ui.btn_a.clicked.connect(complemento)
    ui.btn_del.clicked.connect(delete)
    ui.btn_modConj.clicked.connect(modo_conj)
    ui.btn_modProp.clicked.connect(modo_prop)
    ui.btn_p.clicked.connect(btn_p)
    ui.btn_q.clicked.connect(btn_q)
    ui.btn_r.clicked.connect(btn_r)
    ui.btn_equiv.clicked.connect(equivalencia)
    ui.btn_birelaccional.clicked.connect(birrelacional)
    ui.btn_relacional.clicked.connect(relacional)
    ui.btn_and.clicked.connect(btn_and)
    ui.btn_or.clicked.connect(btn_or)
    ui.btn_not.clicked.connect(btn_not)
    ui.btn_x.clicked.connect(btn_x)
    main_window.show()
    sys.exit(app.exec_())
