from ventana_knn_ui import *
from algoritmos.knn import KNN
import numpy as np
from table_model_pandas import TableModelPandas
from PyQt5.QtWidgets import QWidget, QMessageBox

class VentanaKNN(QWidget, Ui_Form):

    def __init__(self, data, target,  *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.data = data
        self.target = target
        self.knn = KNN(self.data, target)

        self.generar_campos()

        self.btnAceptar.clicked.connect(self.procesar_instancia)

    
    def generar_campos(self):
        """Genera los campos dinamicamente y los muestra"""
        atributos = self.data.columns

        # Crea QLineEdit y QLabel dinamicamente
        for i in range(len(atributos)):
            if atributos[i] == self.target:
                continue

            label = QtWidgets.QLabel(self.formLayoutWidget)
            label.setText(atributos[i])
            edit = QtWidgets.QLineEdit(self.formLayoutWidget)
            edit.setObjectName("edit_" + atributos[i])

            self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
            self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, edit)

        self.scrollAreaWidgetContents.setLayout(self.formLayout)

    def procesar_instancia(self):
        """ Se ejecuta al presionar el boton aceptar """
        self.tablaDistancias.setModel(None) # limpia la tabla

        lista_valores = self.obtener_valores_campos()

        if "" in lista_valores:
            QMessageBox.critical(self, "Error", "Deben llenarse todos los campos")
        else:
            self.knn.set_k(self.spinBoxK.value())

            # Falta verificar que los datos sean del tipo correcto
            resultado, distancias = self.knn.get_prediccion(lista_valores)
            self.labelResultado.setText(str(resultado))

            model = TableModelPandas(distancias)
            self.tablaDistancias.setModel(model)


    def obtener_valores_campos(self):
        """ Retorna en una lista los valores de los atributos insetados por el usuario """
        atributos = self.data.columns
        lista_valores = []

        for atributo in atributos:
            if atributo == self.target:
                continue

            edit = self.findChild(QtWidgets.QLineEdit, "edit_" + atributo)
            val = edit.text()

            # hace la conversion de string a numérico
            if np.issubdtype(self.data[atributo].dtype, np.number):
                try:
                    val = float(val)
                except:
                    pass
            
            lista_valores.append(val)

        return lista_valores