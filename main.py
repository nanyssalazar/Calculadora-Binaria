from PyQt5 import QtWidgets
import UI


def funcion():
    print("hola")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(main_window)

    # Aquí van las funciones
    ui.btn_union.clicked.connect(funcion)

    main_window.show()
    sys.exit(app.exec_())
