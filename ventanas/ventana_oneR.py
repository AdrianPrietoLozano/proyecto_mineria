from ventana_oneR_ui import *
from algoritmos import one_r
import numpy as np
import pandas
import json
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableView, QLabel


class VentanaOneR(QWidget, Ui_Form):

    def __init__(self, data, target,  *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data
        self.target = target

        self.cargar_tablas_frecuencias()


    def cargar_tablas_frecuencias(self):
        frecuencias = one_r.generar_frecuencias(self.data, self.target)
        
        for i in frecuencias:
            label = QLabel(self)
            label.setText(i)
            self.verticalLayout_4.addWidget(label)

            tabla = QTableView(self.scrollAreaWidgetContents)
            tabla.setMinimumSize(QtCore.QSize(0, 200))
            modelo = TableModelPandas(frecuencias[i])
            tabla.setModel(modelo)

            self.verticalLayout_4.addWidget(tabla)

        self.cargar_reglas(frecuencias)

    def cargar_reglas(self, frecuencias):
        reglas = one_r.generar_reglas(frecuencias)

        self.textReglas.setPlainText(json.dumps(reglas, indent=3))

        self.cargar_descripcion_modelo(reglas)

    def cargar_descripcion_modelo(self, reglas):
        menor = one_r.encontrar_error_menor(reglas)
        modelo = menor + "\n"
        for i in reglas[menor]["regla"]:
            modelo += "\t{} -> {}\n".format(i, reglas[menor]["regla"][i][0])

        self.textModelo.setPlainText(modelo)

    
    