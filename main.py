from PyQt5 import QtWidgets
import UI
from itertools import product


setA = set()
setB = set()
setC = set()
setU = set()
setcompA = set()
setcompB = set()
setcompC = set()

quitar = ['A', 'B', 'C', '=', '{', '}', 'U']
dic = {"A": setA, "B": setB, "C": setC, "U": setU, "A'": setcompA, "B'": setcompB, "C'": setcompC}


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
    # Crear conjunto Universo
    crear_conjunto(str(ui.universo.text()), setU)
    try:
        # Encontrar conjunto por complementar
        conj = ui.operacion.text()[-1]
        if conj not in "ABC":
            all_clear()
            ui.resultado.setPlainText("Operacion Inválida")
            return 0
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
    except Exception:
        return 0


def parentesis():
    if (ui.operacion.text().count("(") + ui.operacion.text().count(")")) % 2 == 0:
        add_text("(")
    else:
        add_text(")")


# CHECAR OPERACIONES CON COMPLEMENTOS (QUE SI DEN)
def op_parentesis(string):
    print(string)
    conjunto = set()
    # Ya no busca parentesis porque recibe un string sin parentesis ( )
    # op es el index de la operacion
    op = 1
    conj1 = string[0]

    # Para calcular el complemento de un solo conjunto sin otra operacion
    if len(string) == 2 and string[1] == "'":
        conj1 = conj1 + "'"
        conjunto = dic.get(conj1)
        print(dic.get(conj1))
    else:
        conj2 = string[-1]
        # si el primer conjunto es complemento
        if string[1] == "'":
            conj1 = conj1 + "'"
            # recorremos la posicion del parentesis ( porque ahora la operacion estará un indice despues
            op += 1
        # si el conjunto es complemento cambia el objeto
        if conj2 == "'":
            conj2 = string[-2] + "'"
        print(conj1)
        print(conj2)
        if string[op] == "∪":
            # se remplaza la clave dentro de var conj que esta dentro del diccionario por el objeto que le corresponde
            conjunto = dic.get(conj1).union(dic.get(conj2))
            print(conjunto)
        elif string[op] == '∩':
            conjunto = dic.get(conj1).intersection(dic.get(conj2))
            print(conjunto)
        elif string[op] == '-':
            conjunto = dic.get(conj1).difference(dic.get(conj2))
            print(conjunto)
        # Producto Cartesiano
        elif string[op] == 'x':
            if len(dic.get(conj1)) != len(dic.get(conj2)):
                ui.resultado.setPlainText("Operación inválida")
                return 0
            else:
                conjunto = set(product(dic.get(conj1), dic.get(conj2)))
                print(conjunto)
    return conjunto




def resultado():
    ui.operacion.setText(ui.operacion.text() + ui.btn_igual.text())
    conjunto = set()
    # Si no dio click en los botones, entonces no se crea el conjunto y se le notifica
    if ('A' in ui.operacion.text() and len(setA) == 0) or ('B' in ui.operacion.text() and len(setB) == 0) or \
            ('C' in ui.operacion.text() and len(setC) == 0) or ("'" in ui.operacion.text() and len(setU) == 0):
        ui.operacion.clear()
        return 0
    # Si a la operacion le hace falta un parentesis
    if (ui.operacion.text().count("(") + ui.operacion.text().count(")")) % 2 != 0:
        ui.resultado.setPlainText("Operación Inválida")
        return 0
    #Si se intenta calcular más de un producto cartesiano
    if ui.operacion.text().count("x") > 1:
        ui.resultado.setPlainText("Operación Inválida")
        return 0

    # Si se tiene una operación con más de un par de parentesis
    try:
        if ui.operacion.text().count("(") > 1:
            # si en los primeros indices encuentra ' se recorren las posiciones
            count = ui.operacion.text()[1:6].count("'")
            # Se crean substrings de las dos operaciones a realizar
            substring1 = ui.operacion.text()[1:4 + count]
            print(count)
            substring2 = ui.operacion.text()[7 + count:-2]
            x = op_parentesis(substring1)  # x y y se pueden quitar y llamar la función directo en las operaciones
            y = op_parentesis(substring2)
            # Se calculan los resultados de esas dos operaciones según la operación principal
            # Si es una unión
            if ui.operacion.text()[5 + count] == '∪':
                # se remplaza la clave dentro de var conj que esta dentro del
                # diccionario por el objeto que le corresponde
                conjunto = x.union(y)
                print(conjunto)
            # Si es una intersección
            elif ui.operacion.text()[5 + count] == '∩':
                conjunto = x.intersection(y)
                print(conjunto)
            # Si es una resta
            elif ui.operacion.text()[5 + count] == '-':
                conjunto = x.difference(y)
                print(conjunto)

        # Si es operación con un solo paréntesis
        elif "(" in ui.operacion.text():
            # Los pongo aquí aunque ya esten dentro de la función porque si no no los reconoce,
            # para quitar esto se pueden poner globales en la funcion op_parentesis (parentesis1, parentesis2)
            parentesis1 = ui.operacion.text().index("(")
            parentesis2 = ui.operacion.text().index(")")
            # Lo asignamos a una variable (se puede poner directo)
            conjunto = op_parentesis(ui.operacion.text()[parentesis1 + 1:parentesis2])
            # Si antes del parentesis esta la otra operación y es una unión
            if ui.operacion.text()[parentesis1 - 1] == '∪':
                # Si es un complemento
                if ui.operacion.text()[parentesis1 - 2] == "'":
                    conj1 = ui.operacion.text()[parentesis1 - 3] + "'"
                    conjunto = conjunto.union(dic.get(conj1))
                # Si se unia con A con B o con C
                else:
                    conj1 = ui.operacion.text()[parentesis1 - 2]
                    conjunto = conjunto.union(dic.get(conj1))
                print(conjunto)

            # Si antes del parentesis esta la otra operación y es una intersección
            elif ui.operacion.text()[parentesis1 - 1] == '∩':
                # tratar al conjunto como si fuera otro parentesis para evitar todas los ifs de abajo
                # conj1 = op_parentesis(ui.operacion.text()[:parentesis1-1])
                #  CHECAR
                # estas lineas marcar error "unhashable" creo que es porque el conjunto va a salir vacio?
                # conjunto = conjunto.intersection(dic.get(conj1))
                # Si es un complemento
                if ui.operacion.text()[parentesis1 - 2] == "'":
                    conj1 = ui.operacion.text()[parentesis1 - 3] + "'"
                    conjunto = conjunto.intersection(dic.get(conj1))
                else:
                    conj1 = ui.operacion.text()[parentesis1 - 2]
                    conjunto = conjunto.intersection(dic.get(conj1))
                print(conjunto)

            # Si antes del parentesis esta la otra operación y es una resta
            elif ui.operacion.text()[parentesis1 - 1] == '-':
                # Si es un complemento
                if ui.operacion.text()[parentesis1 - 2] == "'":
                    conj1 = ui.operacion.text()[parentesis1 - 3] + "'"
                    conjunto = conjunto.difference(dic.get(conj1))
                else:
                    conj1 = ui.operacion.text()[parentesis1 - 2]
                    conjunto = conjunto.difference(dic.get(conj1))
                print(conjunto)

            # Si despues del parentesis esta la otra operación y es una unión
            elif ui.operacion.text()[parentesis2 + 1] == '∪':
                # Si es un complemento
                if ui.operacion.text()[parentesis2 + 3] == "'":
                    conj1 = ui.operacion.text()[parentesis2 + 2] + "'"
                    conjunto = conjunto.union(dic.get(conj1))
                else:
                    conj1 = ui.operacion.text()[parentesis2 + 2]
                    print(conj1)
                    conjunto = conjunto.union(dic.get(conj1))
                print(conjunto)

            # Si despues del parentesis esta la otra operación y es una intersección
            elif ui.operacion.text()[parentesis2 + 1] == '∩':
                # Si es un complemento
                if ui.operacion.text()[parentesis2 + 3] == "'":
                    conj1 = ui.operacion.text()[parentesis2 + 2] + "'"
                    conjunto = conjunto.intersection(dic.get(conj1))
                else:
                    conj1 = ui.operacion.text()[parentesis2 + 2]
                    conjunto = conjunto.intersection(dic.get(conj1))
                print(conjunto)
            # Si despues del parentesis esta la otra operación y es una resta
            elif ui.operacion.text()[parentesis2 + 1] == '-':
                # Si es un complemento
                if ui.operacion.text()[parentesis2 + 3] == "'":
                    conj1 = ui.operacion.text()[parentesis2 + 2] + "'"
                    conjunto = conjunto.difference(dic.get(conj1))
                else:
                    conj1 = ui.operacion.text()[parentesis2 + 2]
                    conjunto = conjunto.difference(dic.get(conj1))
                print(conjunto)
        # Si son operaciones sin parentesis
        else:
            # calcular solo el complemento de un conjunto esta dentro de la funcion
            conjunto = op_parentesis(ui.operacion.text().replace("=", ""))
        # Muestra el resultado
        if len(conjunto) == 0:  # Si esta vacío
            ui.resultado.setPlainText(ui.operacion.text() + " { }")
        else:
            ui.resultado.setPlainText(ui.operacion.text() + " " + str(conjunto))
    except Exception:
        ui.resultado.setPlainText("Operación Inválida")
        ui.operacion.clear()


def delete():
    #string = ui.operacion.text()
    #string = string[:-1]
    ui.operacion.setText(ui.operacion.text()[:-1])
    ui.resultado.clear()


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


def modo(widget1, widget2):
    all_clear()
    ui.stackedWidget.setCurrentWidget(widget1)
    ui.stackedWidget_2.setCurrentWidget(widget2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.setFixedWidth(461)
    main_window.setFixedHeight(553)
    ui.stackedWidget.setCurrentWidget(ui.conjuntos)
    ui.stackedWidget_2.setCurrentWidget(ui.mod_prop)

    # FUNCIONES
    ##############################################################################

    # CONJUNTOS
    ui.btn_conjA.clicked.connect(lambda: crear_conjunto(ui.conjA.text(), setA, 'A'))
    ui.btn_conjB.clicked.connect(lambda: crear_conjunto(ui.conjB.text(), setB, 'B'))
    ui.btn_conjC.clicked.connect(lambda: crear_conjunto(ui.conjC.text(), setC, 'C'))

    ui.btn_parentesis.clicked.connect(parentesis)
    ui.btn_union.clicked.connect(lambda: add_text('∪'))
    ui.btn_interseccion.clicked.connect(lambda: add_text('∩'))
    ui.btn_resta.clicked.connect(lambda: add_text('-'))
    ui.btn_producto.clicked.connect(lambda: add_text('x'))
    ui.btn_a.clicked.connect(complemento)

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

    ui.btn_par2.clicked.connect(parentesis)

    # OTRAS FUNCIONES
    ui.btn_modConj.clicked.connect(lambda: modo(ui.conjuntos, ui.mod_prop))
    ui.btn_modProp.clicked.connect(lambda: modo(ui.proposiciones, ui.mod_conj))

    # BORRAR
    ui.btn_del.clicked.connect(delete)
    ui.btn_ac.clicked.connect(all_clear)

    # RESULTADO
    ui.btn_igual.clicked.connect(resultado)

    ##############################################################################

    main_window.show()
    sys.exit(app.exec_())
