import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class UiVentana(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UiVentana, self).__init__(parent)

        self.puntos = []

        self.visor = QtWidgets.QOpenGLWidget()

        self.valor_do = QtWidgets.QSpinBox()
        self.valor_cota = QtWidgets.QSpinBox()
        self.valor_alej = QtWidgets.QSpinBox()

        self.texto_nombre = QtWidgets.QLabel("Nombre")
        self.nombre = QtWidgets.QLineEdit()
        self.crear_punto = QtWidgets.QPushButton("Crear", clicked=self.crear_punto)

        elementos_widget = QtWidgets.QWidget()

        scroll_widget = QtWidgets.QWidget()
        scroll = QtWidgets.QScrollArea(widgetResizable=True)
        scroll.setWidget(scroll_widget)

        vbox = QtWidgets.QVBoxLayout(scroll_widget)
        vbox.addWidget(elementos_widget)
        vbox.addStretch()

        self.elementos = QtWidgets.QGridLayout(elementos_widget)

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(self.valor_do, 0, 0)
        grid_layout.addWidget(self.valor_cota, 0, 1)
        grid_layout.addWidget(self.valor_alej, 0, 2)
        grid_layout.addWidget(self.texto_nombre, 1, 0)
        grid_layout.addWidget(self.nombre, 1, 1)
        grid_layout.addWidget(self.crear_punto, 1, 2)
        grid_layout.addWidget(scroll, 2, 0, 1, 3)

        for i in range(3):
            grid_layout.setColumnStretch(i, 1)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        lay = QtWidgets.QHBoxLayout(central_widget)
        lay.addWidget(self.visor, stretch=1)
        lay.addLayout(grid_layout)

        self.resize(1280, 960)


    def crear_punto(self):
        do = self.valor_do.value()
        cota = self.valor_cota.value()
        alejamiento = self.valor_alej.value()
        name = QtWidgets.QLabel(
            "{}({}, {}, {})".format(self.nombre.text(), do, cota, alejamiento)
        )

        punto = (self.nombre.text(), do, cota, alejamiento)

        borrar = QtWidgets.QPushButton("X")

        wrapper = partial(self.borrar_punto, (name, borrar), punto)
        borrar.clicked.connect(wrapper)

        row = self.elementos.rowCount()
        self.elementos.addWidget(name, row, 0)
        self.elementos.addWidget(borrar, row, 1)

        self.puntos.append(punto)

    def borrar_punto(self, widgets, punto):
        if self.puntos:
            name, borrar = widgets
            name.deleteLater()
            borrar.deleteLater()
            self.puntos.remove(punto)
            print(self.puntos)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys.excepthook = except_hook
    w = UiVentana()
    w.show()
    exit(app.exec_())