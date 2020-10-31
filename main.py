from PyQt5 import QtWidgets
import UI

setA = set()
setB = set()
setC = set()
setU = set()
setcompA = set()
setcompB = set()
setcompC = set()

quitar = ["A", 'B', 'C', '=', '{', '}', 'U']


def crear_conjunto(string, conjunto, operacion_text=''):
    for i in quitar:
        if i in string:
            string = string.replace(i, '')
    for i in string.split(','):
        conjunto.add(i)
    ui.operacion.setText(ui.operacion.text() + operacion_text)


def add_text(char):
    ui.operacion.setText(ui.operacion.text() + char)


def complemento():
    dic = {"A": setA, "B": setB, "C": setC, "U": setU, "A'": setcompA, "B'": setcompB, "C'": setcompC}
    # Crear conjunto Universo
    crear_conjunto(str(ui.universo.text()), setU)
    # Encontrar conjunto por complementar
    conj = ui.operacion.text()[-1]
    # Agregar '
    ui.operacion.setText(ui.operacion.text() + "'")
    # Encontrar diferencia con U
    comp = setU.difference(dic.get(conj))
    # Cambiar conjunto a complemento del conjunto x --> x'
    conj = conj + "'"
    # Agregar los elementos al complemento correspondiente
    for i in comp:
        dic.get(conj).add(i)
    print(dic.get(conj))


def resultado():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    dic = {"A": setA, "B": setB, "C": setC, "U": setU, "A'": setcompA, "B'": setcompB, "C'": setcompC}
    conjunto = set()  # tambien se puede usar = {} - esta linea se puede comentar pero marca amarillo
    # Si se tiene una operación con parentesis
    if "(" in ui.operacion.text():
        # Encuentra los parentesis y devuelve el index
        parentesis1 = ui.operacion.text().index("(")
        parentesis2 = ui.operacion.text().index(")")
        conj1 = ui.operacion.text()[parentesis1 + 1]
        conj2 = ui.operacion.text()[parentesis2 - 1]
        # si el primer conjunto es complemento
        if ui.operacion.text()[parentesis1 + 2] == "'":
            conj1 = conj1 + "'"
            # recorremos la posicion del parentesis ( porque ahora la operacion estará un indice despues
            parentesis1 += 1
        # si el conjunto es complemento cambia el objeto
        if conj2 == "'":
            conj2 = ui.operacion.text()[parentesis2 - 2] + "'"

        if ui.operacion.text()[parentesis1 + 2] == "∪":
            # se remplaza la clave dentro de var conj que esta dentro del diccionario por el objeto que le corresponde
            conjunto = dic.get(conj1).union(dic.get(conj2))
            print(conjunto)
        elif ui.operacion.text()[parentesis1 + 2] == '∩':
            conjunto = dic.get(conj1).intersection(dic.get(conj2))
            print(conjunto)
        elif ui.operacion.text()[parentesis1 + 2] == '-':
            conjunto = dic.get(conj1).difference(dic.get(conj2))
            print(conjunto)

        # Si antes del parentesis esta la otra operación y es una unión
        if ui.operacion.text()[parentesis1 - 1] == '∪':
            # Si se unia con A con B o con C
            conj1 = ui.operacion.text()[parentesis1 - 2]
            conjunto = conjunto.union(dic.get(conj1))
            print(conjunto)

        # Si antes del parentesis esta la otra operación y es una intersección
        elif ui.operacion.text()[parentesis1 - 1] == '∩':
            # Si es con B o con C
            conj1 = ui.operacion.text()[parentesis1 - 2]
            conjunto = conjunto.intersection(dic.get(conj1))
            print(conjunto)

        # Si antes del parentesis esta la otra operación y es una resta
        elif ui.operacion.text()[parentesis1 - 1] == '-':
            # Si es con B o con C
            conj1 = ui.operacion.text()[parentesis1 - 2]
            conjunto = conjunto.difference(dic.get(conj1))
            print(conjunto)

        # Si despues del parentesis esta la otra operación y es una unión
        elif ui.operacion.text()[parentesis2 + 1] == '∪':
            conj1 = ui.operacion.text()[parentesis2 + 2]
            print(conj1)
            conjunto = conjunto.union(dic.get(conj1))
            print(conjunto)

        # Si despues del parentesis esta la otra operación y es una intersección
        elif ui.operacion.text()[parentesis2 + 1] == '∩':
            conj1 = ui.operacion.text()[parentesis2 + 2]
            conjunto = conjunto.intersection(dic.get(conj1))
            print(conjunto)
        # Si despues del parentesis esta la otra operación y es una resta
        elif ui.operacion.text()[parentesis2 + 1] == '-':
            conj1 = ui.operacion.text()[parentesis2 + 2]
            conjunto = conjunto.difference(dic.get(conj1))
            print(conjunto)
        # Pone el resultado final
        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))

    # Si son operaciones sin parentesis
    else:
        conj1 = ui.operacion.text()[0]
        # Para calcular el complemento de un solo conjunto sin otra operacion
        if len(ui.operacion.text()) == 3 and ui.operacion.text()[1] == "'":
            conj1 = conj1 + "'"
            conjunto = dic.get(conj1)
            print(dic.get(conj1))
        else:
            conj2 = ui.operacion.text()[2]
            # si el primer conjunto es complemento
            if ui.operacion.text()[1] == "'":
                conj1 = conj1 + "'"
                conj2 = ui.operacion.text()[3]
            # si el conjunto es complemento cambia el objeto
            if ui.operacion.text()[-2] == "'":
                conj2 = ui.operacion.text()[-3] + "'"

            # Si es una unión
            if "∪" in ui.operacion.text():
                # se remplaza la clave dentro de var conj que esta dentro del
                # diccionario por el objeto que le corresponde
                conjunto = dic.get(conj1).union(dic.get(conj2))
                print(conjunto)
            # Si es una intersección
            elif '∩' in ui.operacion.text():
                conjunto = dic.get(conj1).intersection(dic.get(conj2))
                print(conjunto)
            # Si es una resta
            elif '-' in ui.operacion.text():
                conjunto = dic.get(conj1).difference(dic.get(conj2))
                print(conjunto)

        ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))


def delete():
    string = ui.operacion.text()
    string = string[:-1]
    ui.operacion.setText(string)


def all_clear():
    setA.clear()
    setB.clear()
    setC.clear()
    setU.clear()
    setcompA.clear()
    setcompB.clear()
    setcompC.clear()
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

    # FUNCIONES
    ##############################################################################

    # CONJUNTOS
    ui.btn_conjA.clicked.connect(lambda: crear_conjunto(ui.conjA.text(), setA, 'A'))
    ui.btn_conjB.clicked.connect(lambda: crear_conjunto(ui.conjB.text(), setB, 'B'))
    ui.btn_conjC.clicked.connect(lambda: crear_conjunto(ui.conjC.text(), setC, 'C'))

    ui.btn_union.clicked.connect(lambda: add_text('∪'))
    ui.btn_interseccion.clicked.connect(lambda: add_text('∩'))
    ui.btn_resta.clicked.connect(lambda: add_text('-'))
    ui.btn_a.clicked.connect(complemento)

    ui.btn_del.clicked.connect(delete)
    ui.btn_ac.clicked.connect(all_clear)
    ui.btn_igual.clicked.connect(resultado)

    # PROPOSICIONES
    ui.btn_p.clicked.connect(lambda: add_text("p"))
    ui.btn_q.clicked.connect(lambda: add_text("q"))
    ui.btn_r.clicked.connect(lambda: add_text("r"))

    ui.btn_equiv.clicked.connect(lambda: add_text("≡"))
    ui.btn_birelaccional.clicked.connect(lambda: add_text("↔"))
    ui.btn_relacional.clicked.connect(lambda: add_text("→"))

    ui.btn_and.clicked.connect(lambda: add_text("^"))
    ui.btn_or.clicked.connect(lambda: add_text("v"))
    ui.btn_not.clicked.connect(lambda: add_text("¬"))

    ui.btn_x.clicked.connect(lambda: add_text("x"))

    # OTRAS FUNCIONES
    ui.btn_modConj.clicked.connect(modo_conj)
    ui.btn_modProp.clicked.connect(modo_prop)

    ##############################################################################

    main_window.show()
    sys.exit(app.exec_())
